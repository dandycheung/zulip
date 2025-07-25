# Rename a topic

Zulip makes it possible to rename topics. This is useful for keeping messages
organized, even if some users are still learning how to use topics effectively.
You can also [move content to another
topic](/help/move-content-to-another-topic).

When a topic is renamed, links [to the
topic](/help/link-to-a-message-or-conversation#get-a-link-to-a-specific-topic)
and [to messages in that
topic](/help/link-to-a-message-or-conversation#get-a-link-to-a-specific-message)
will automatically redirect to the new location of the message. [Muted
topics](/help/mute-a-topic) are automatically migrated when a topic is renamed.

Organization administrators can [configure](/help/restrict-moving-messages) who
is allowed to rename topics.

## Rename a topic

{start_tabs}

{tab|via-message-recipient-bar}

1. Click the **edit topic** (<i class="zulip-icon zulip-icon-pencil"></i>) icon in
   the message recipient bar. If you do not see the
   **edit topic** (<i class="zulip-icon zulip-icon-pencil"></i>) icon, you do not
   have permission to rename this topic.

1. Edit the topic name.

1. Click the **save** (<i class="zulip-icon zulip-icon-check"></i>) icon
   to save your changes.

{tab|via-left-sidebar}

{!topic-actions.md!}

1. Select **Move topic** or **Rename topic**. If you do not see either option,
   you do not have permission to rename this topic.

1. Edit the topic name.

1. _(optional)_  If using the **Move topic** menu, select the destination channel
   for the topic from the channels dropdown list.

1. Toggle whether automated notices should be sent.

1. Click **Confirm** to rename the topic.

{tab|mobile}

Access this feature by following the web app instructions in your
mobile device browser.

Implementation of this feature in the mobile app is tracked [on
GitHub](https://github.com/zulip/zulip-flutter/issues/1439). If
you're interested in this feature, please react to the issue's
description with 👍.

{end_tabs}

## Related articles

* [Move content to another topic](/help/move-content-to-another-topic)
* [Move content to another channel](/help/move-content-to-another-channel)
* [Resolve a topic](/help/resolve-a-topic)
* [Restrict moving messages](/help/restrict-moving-messages)
