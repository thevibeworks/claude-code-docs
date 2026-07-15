# Restrict verified-domain connectors to your Enterprise

This article explains how to prevent Claude accounts outside your Enterprise organization from connecting certain services, like Gmail and Slack, using an email address on your verified domains. Use the **Restrict verified-domain connectors to your enterprise** setting to keep company data from reaching personal Claude accounts through connectors.

This setting is available to Owners, Primary Owners, and custom roles with the Identity & Access permission set to Manage on the Enterprise plan. Your Enterprise organization needs at least one verified domain.

## How it works

When you turn on **Restrict verified-domain connectors to your enterprise**, only Claude accounts in your Enterprise organization can connect the supported connectors using an email address on your verified domains. Anyone who tries to make one of these connections from a Claude account outside your Enterprise is blocked. This setting applies to your entire Enterprise. You manage it at the parent organization level, and it applies to all child organizations.

This check relies on the connected service sharing the account's identity during the connection process. For supported connectors, Claude can confirm the email domain of the account being connected and enforce the restriction. When a service doesn't share account identity, Claude can't perform the check and the connection proceeds normally.

**Note:** This setting applies only to specific supported connectors, which you can view in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

For example, someone has two Claude accounts: a personal account using their personal email, and a work account using their work email. The work email is on a domain your Enterprise organization has verified.

When the setting is off, they can sign in to Claude with their personal account and connect the Gmail account they use for work. That moves company information outside your organization's controls.

When the setting is on, they can't connect their work Gmail from their personal account. They can still connect it from their work account. That keeps company information inside your organization's controls.

---

## Prerequisites

Before you can turn on this setting, your Enterprise organization must verify your domain.

## Turn on the restriction

1. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

2. Scroll to **Connector domain restriction**.

3. Toggle on "Restrict verified-domain connectors to your enterprise."

You can turn off this setting at any time. It's separate from domain capture, which can't be reversed once enabled.

---

## What people see when a connection is restricted

If someone tries to make a connection that’s restricted, the connection fails at sign-in with this message:

“This corporate identity belongs to an Enterprise that manages access through their own Claude account. Sign in to your organization's Claude account to use this connection.”

## What the setting doesn't do

- **It doesn't restrict connections in the other direction.** When the setting is on, people in your Enterprise can still connect services for personal use to their Enterprise Claude account. For example, they can connect their personal Gmail account.

- **It doesn't replace data loss prevention.** It's a safeguard against accidentally connecting a work account to the wrong Claude account, not a control against deliberate data movement.

- **It doesn't disconnect existing connections.** The restriction applies only to new connection attempts. Connections made before you turned on the setting stay connected.

- **It doesn't notify admins.** Only the person attempting the connection sees the message if it fails.

---

## Frequently asked questions

### How is this different from domain claiming?

Domain claiming moves existing personal Claude accounts on your domain into your Enterprise workspace. This setting leaves Claude accounts where they are, and makes it so that only Claude accounts in your Enterprise organization can connect supported connectors using an email address on your verified domains. Learn more about **[claiming and migrating accounts on your domain](https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain)**.

### Is this the same as the Claude in Slack setting, "Restrict to your verified domains"?

No. That setting applies only to Claude in Slack. This setting covers the connectors listed in **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

### What should someone do if their connection is blocked?

Sign in to your organization's Claude account and make the connection there. Anyone who doesn't have a Claude account in your organization should contact their admin for access.