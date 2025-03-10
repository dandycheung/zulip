from datetime import datetime
from typing import Any

from django.db import transaction
from django.utils.timezone import now as timezone_now

from zerver.lib.timestamp import datetime_to_timestamp
from zerver.lib.topic import maybe_rename_general_chat_to_empty_topic
from zerver.lib.user_topics import (
    bulk_set_user_topic_visibility_policy_in_database,
    get_topic_mutes,
)
from zerver.models import Stream, UserProfile
from zerver.tornado.django_api import send_event_on_commit


@transaction.atomic(savepoint=False)
def bulk_do_set_user_topic_visibility_policy(
    user_profiles: list[UserProfile],
    stream: Stream,
    topic_name: str,
    *,
    visibility_policy: int,
    last_updated: datetime | None = None,
    skip_muted_topics_event: bool = False,
) -> None:
    if last_updated is None:
        last_updated = timezone_now()

    topic_name = maybe_rename_general_chat_to_empty_topic(topic_name)

    user_profiles_with_changed_user_topic_rows = bulk_set_user_topic_visibility_policy_in_database(
        user_profiles,
        stream.id,
        topic_name,
        visibility_policy=visibility_policy,
        recipient_id=stream.recipient_id,
        last_updated=last_updated,
    )

    # Users with requests to set the visibility_policy to its current value
    # or to delete a UserTopic row that doesn't exist shouldn't
    # send an unnecessary event.
    if len(user_profiles_with_changed_user_topic_rows) == 0:
        return

    for user_profile in user_profiles_with_changed_user_topic_rows:
        # This first muted_topics event is deprecated and will be removed
        # once clients are migrated to handle the user_topic event type
        # instead.
        if not skip_muted_topics_event:
            muted_topics_event = dict(
                type="muted_topics", muted_topics=get_topic_mutes(user_profile)
            )
            send_event_on_commit(user_profile.realm, muted_topics_event, [user_profile.id])

        user_topic_event: dict[str, Any] = {
            "type": "user_topic",
            "stream_id": stream.id,
            "topic_name": topic_name,
            "last_updated": datetime_to_timestamp(last_updated),
            "visibility_policy": visibility_policy,
        }

        send_event_on_commit(user_profile.realm, user_topic_event, [user_profile.id])


def do_set_user_topic_visibility_policy(
    user_profile: UserProfile,
    stream: Stream,
    topic_name: str,
    *,
    visibility_policy: int,
    last_updated: datetime | None = None,
    skip_muted_topics_event: bool = False,
) -> None:
    # For conciseness, this function should be used when a single
    # user_profile is involved. In the case of multiple user profiles,
    # call 'bulk_do_set_user_topic_visibility_policy' directly.
    bulk_do_set_user_topic_visibility_policy(
        [user_profile],
        stream,
        topic_name,
        visibility_policy=visibility_policy,
        last_updated=last_updated,
        skip_muted_topics_event=skip_muted_topics_event,
    )
