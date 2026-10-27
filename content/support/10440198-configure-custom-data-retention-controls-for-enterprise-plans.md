# Configure custom data retention controls for Enterprise plans

*This article is about our commercial products, specifically Claude Enterprise. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see **[here](https://privacy.claude.com/en/collections/10663362-consumers)**.*

Custom data retention controls allow organizations to manage how long Claude stores conversation, project, and artifact data. This article explains how to set up and manage data retention periods for your organization.

This feature is available to Enterprise plan customers. To set custom retention periods for your organization, you must have either a Primary Owner or Owner role.

## How data retention works

Data retention is based on the last observed activity:

- **For chats:** The period is measured from the most recent activity in the conversation or in any cloud session Claude started from it.

- **For projects:** Retention period starts from the time of the most recent action that resets it.

  - These actions reset the retention period:

    - Sending a message in an existing chat in the project

    - Creating a new chat in the project

    - Editing the project's knowledge files, instructions, or sharing settings

    - Starting a Claude Cowork session in the cloud from the project, or moving a cloud session into the project (this resets the period once, when the session starts or is moved)

    - Connecting or disconnecting a local folder for Cowork

    - Editing the project's knowledge files from a Cowork session

  - These actions don't reset the retention period:

    - Viewing a project or opening a chat in it

    - Starting a *local* Cowork session

    - Other work in a Cowork session, whether it runs in the cloud or on your computer

  - Project retention always takes precedence over chat retention for chats inside a project. This applies even if you haven’t set a custom project retention period: by default, projects are retained indefinitely, so chats inside projects are not deleted by your chat retention period.

- **For artifacts:** Retention period starts from the last time someone opened or edited the artifact.

The minimum retention period is 30 days, and each month is counted as 30 days. For example, a three-month retention period equals 90 days.

## What gets deleted

When data reaches the end of its retention period:

- **For chats:** All standalone chats (chats not inside a project) will be deleted. Chats inside a project follow the project’s retention period. Moving a chat into a project places it under the project’s retention period; moving a chat out of a project makes it standalone again, and it becomes eligible for deletion under the chat retention period based on its last activity.

- **For projects:** All projects will be deleted, including any chats within those projects.

- **For artifacts:** Artifacts are deleted under a retention period that covers artifacts, not with the chat or project they were made in. This includes artifacts Claude creates in chats, with some exceptions. For example, Research reports and artifacts in some older chats are deleted with their chat, along with any link published from them. A retention period that covers artifacts doesn't delete artifacts published with a public link.

- If your organization has the new unified Claude experience, see “Data retention and deletion” in **Set up and manage the new unified Claude experience for your Enterprise organization** for what custom data retention covers there.

## Important considerations

- Deletion happens after the period ends rather than at an exact moment, and deleted data is removed from our back-end systems. As with chat, we may retain content flagged by our trust and safety systems or as required by law.

- By default, data is retained indefinitely unless a custom retention period is set.

- When you shorten a retention period, any data that falls outside the new period is scheduled for permanent deletion as soon as you save. A daily background process removes it, which can take several days for large amounts of data. Don’t rely on this delay to reverse the change.

- Data past its retention period will be permanently deleted and cannot be recovered.

- If your chat is flagged by our automated trust and safety systems as violating our Usage Policy, we retain inputs and outputs as described here: **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866)**

## Set up data retention

To set custom retention periods:

1. Log in to your Owner Enterprise plan account.

2. Navigate to **[Organization settings > Data and Privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

3. Set your desired retention period (minimum 30 days).

4. Save your changes.

**Important:** Custom retention periods apply to content in chats, projects, and artifacts. They don't apply to standalone **[Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)** at claude.ai/design,[**Claude Tag**](https://support.claude.com/en/articles/15594475-what-is-claude-tag), **[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)**, or any other feature that runs **[Claude Code in the cloud](https://support.claude.com/en/articles/12618689)**. Cloud sessions Claude starts from a chat are deleted with that chat. A Claude Design project or design system that moves, or has already moved, to Claude becomes an artifact. If your organization has a retention period that covers artifacts (a single period for all data, or the private or shared artifact period if you use separate periods), that artifact can be permanently deleted if nobody opens it for that period. The period starts on the day of the move and restarts when someone opens or edits the artifact.

## Example retention calculation

If a conversation’s last message is at 3PM UTC on March 1 with a 30-day retention period, the conversation is deleted after March 31.

## Monitor retention-related activities

All retention-related actions and changes are automatically tracked in **[audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)**. You can access these logs to monitor changes to retention settings and data deletion events.