# Turn on data retention for a Workspace in a zero data retention organization

This article shows you how to turn on 30-day data retention for a Workspace in your Claude Console organization when your organization uses zero data retention (ZDR).

This is only available to organizations on the Claude API that use zero data retention. Organizations that already retain data for 30 days don’t have this setting.

## Why a Workspace needs data retention

**[Covered Models](https://support.claude.com/en/articles/15425695-covered-models)**, such as Claude Fable 5.1, require 30-day data retention and aren't available under zero data retention unless Anthropic has expressly authorized it for your organization (for example, under Enterprise Frontier Safeguards). If not, you need to turn on data retention. Data retention is configured at the Workspace level, so you need to turn it on for each Workspace you’d like to use Covered Models in.

Requests to Covered Models from a Workspace with retention off return an error like this one:

"In order to access this model, your organization or Workspace must have data retention enabled."

## Before you begin

Before you start, make sure that:

- You're an Admin, Owner, or Primary Owner of the organization. Users with other roles who are members of the Workspace can see the setting but can't change it.

- You're working in a Workspace other than the default Workspace. Retention for the default Workspace is managed at the organization level, so create a new Workspace if you need one. Learn more about **[creating and managing Workspaces](https://support.claude.com/en/articles/9796807)**.

## Turn on data retention for a Workspace

The setting lives in each Workspace's privacy controls, at the bottom of the Workspace's left sidebar.

To turn on data retention for a Workspace:

1. Log in to the **[Claude Console](https://platform.claude.com/login)**.

2. Click your initials (or name) in the lower left corner to open your account menu.

3. Navigate to **[Organization settings > Workspaces](https://platform.claude.com/settings/workspaces)**. The **Data retention** column shows the current setting for each Workspace.

4. Click the Workspace you want to change.

5. In the left sidebar, click "Manage" to expand the section if it's collapsed.

6. Click "Privacy controls."

7. In the **Data retention** card, toggle the **This workspace** switch on or off.

8. Click "Accept" in the confirmation dialog. By accepting, you acknowledge that Section F of the **[Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms)** applies to this Workspace and supplements your organization's agreement with Anthropic.

The **This workspace** row now shows **On · 30 days**. There's no separate confirmation message, so this label is how you know the change took effect.

## See which Workspaces have retention on

To see which Workspaces have data retention on, navigate to **[Organization settings > Workspaces](https://platform.claude.com/settings/workspaces)** and check the **Data retention** column for each Workspace. You'll see either **Zero data retention** or **30 day retention**.

## What changes after you turn it on

- The change applies to new requests right away. In rare cases it can take up to an hour.

- Inputs, Outputs, and other data from this Workspace are retained for 30 days by default and may be accessed by Anthropic for safety and security purposes.

- The change isn't retroactive. It applies only to requests sent after you turn on retention.

- Your organization's zero data retention no longer applies to this Workspace while retention is on. Other Workspaces aren't affected.

- Requests to Covered Models from this Workspace's API keys now succeed, as long as your organization already has access to the model. You don't need new API keys.

**Important:** This setting covers API requests and responses from the Workspace. It doesn't cover features that need to store data to work, such as the Batch API, the Files API, and Claude Managed Agents sessions. Learn more about **[which features are eligible for zero data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility)**.

## Turn off data retention for a Workspace

You can turn retention off again from the same switch. If the Workspace uses customer-managed encryption keys, you can't turn retention off. If a program on the Workspace requires retention, turning it off removes that program.