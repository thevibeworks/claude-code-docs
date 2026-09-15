# Configure custom data retention controls for Enterprise plans

This feature is available to Enterprise plan customers. To set custom retention periods for your organization, you must have either a Primary Owner or Owner role.

*This article is about our commercial products, specifically Claude Enterprise. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see **[here](https://privacy.claude.com/en/collections/10663362-consumers)**.*

Custom data retention controls allow organizations to manage how long Claude stores conversation and project data. This article explains how to set up and manage data retention periods for your organization.

## How data retention works

Data retention is based on the last observed activity:

- **For chats:** Retention period starts from the time of the last message in the conversation.

- **For projects:** Retention period starts from the time the project was last updated (this includes chat creation or project knowledge base modifications).

  - Project retention always takes precedence over chat retention for chats inside a project. This applies even if you haven’t set a custom project retention period: by default, projects are retained indefinitely, so chats inside projects are not deleted by your chat retention period.

The minimum retention period is 30 days, and each month is counted as 30 days. For example, a three-month retention period equals 90 days.

## What gets deleted

When data reaches the end of its retention period:

- **For chats:** All standalone chats (chats not inside a project) and any artifacts within those chats will be deleted. Chats inside a project follow the project’s retention period. Moving a chat into a project places it under the project’s retention period; moving a chat out of a project makes it standalone again, and it becomes eligible for deletion under the chat retention period based on its last activity.

- **For projects:** All projects will be deleted, including any chats and artifacts within those projects.

## Important considerations

- Deletion occurs at midnight UTC on the scheduled day.

- By default, data is retained indefinitely unless a custom retention period is set.

- When you shorten a retention period, any data that falls outside the new period is scheduled for permanent deletion as soon as you save. A daily background process removes it, which can take several days for large amounts of data. Don’t rely on this delay to reverse the change.

- Data past its retention period will be permanently deleted and cannot be recovered.

- If your chat is flagged by our automated trust and safety systems as violating our Usage Policy, we retain inputs and outputs as described here: **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866)**

## Setting up data retention

## To set custom retention periods:

1. Log in to your Owner Enterprise plan account.

2. Navigate to **[Organization settings > Data and Privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

3. Set your desired retention period (minimum 30 days).

4. Save your changes.

**Important:** Custom retention periods apply to content in chats and projects. They do not apply to **[Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)**, **[Claude Tag](https://support.claude.com/en/articles/15594475-what-is-claude-tag)**, **[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)**, or any other features built on **[Claude Code on the web](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)**.

## Example retention calculation

If a conversation’s last message is at 3PM UTC on March 1 with a 30-day retention period, the deletion will occur at midnight UTC on March 31.

## Monitoring retention-related activities

All retention-related actions and changes are automatically tracked in **[audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)**. You can access these logs to monitor changes to retention settings and data deletion events.