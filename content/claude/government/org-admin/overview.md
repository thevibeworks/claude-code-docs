> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization administration

> Manage the people, seats, and settings for a single organization within your agency.

> **Who this portal is for:** Organization owners. If you manage multiple organizations across your agency, see the [Tenant administration](/docs/government/tenant-admin/overview) guide instead.

The organization admin portal is where you manage the people, seats, and settings for a single organization in Claude for Government. It covers the day-to-day work of administering who has access, how much they can use, and how the Claude products behave for your users.

## Key concepts

Before you use the portal, it helps to understand how the pieces fit together.

Your agency's deployment is a **tenant**, which is the top-level container that holds one or more **organizations**. An organization is a self-contained group of users with its own seats, settings, and usage. Most administrators work at the organization level, while tenant administrators oversee all of the organizations together and control tenant-wide resources such as single sign-on, directory provisioning, and billing accounts.

Every person in an organization holds a **role**, which determines whether they can reach this portal at all, and occupies a **seat** on a **seat tier**, which determines which Claude models they can use and how much they can use them. Seat tiers come in two kinds:

* **Anthropic-managed tiers** that are supplied to you as a fixed number of seats.
* **Self-managed tiers** that your organization defines itself and that draw from the billing account's balance.

## Who can access it

You can reach the organization admin portal if your role in the organization is **Owner** or **Primary Owner**. Users who hold the standard **User** role are redirected to their personal account page instead.

> **For tenant administrators:** You can also open this portal for any organization in your tenant. When your tenant contains more than one organization, an **Acting as** selector appears at the top of every admin page so you can choose which organization you are currently managing. All the changes you make while acting as an organization apply to that organization, and the audit trail records your own identity as the actor.

## Getting around

The portal header shows your organization's name, and a navigation bar below it gives you access to each admin page.

<Note>
  If the account your organization draws from crosses a warning threshold, a banner appears just below the navigation on every page of this portal. When your organization manages the account or is the only one using it, the banner tells you the percentage of credits used. When the account is shared with other organizations and yours does not manage it, the banner instead says credits are running low and points you to your tenant administrators. The banner stays in place until more credits are added to the account, and it escalates in color and wording if usage crosses a higher threshold. Every owner sees the banner, including when the Billing tab is hidden, so that you always know when your organization is running low.
</Note>

> **For owners and tenant administrators:** You can reach the user view from the **Switch to user view** link in the page footer. If you are also a tenant administrator, the footer additionally offers **Switch to tenant view**.

## Pages in this portal

The navigation groups the pages into three sections.

**People**

| Page                                                 | What it's for                                                                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Users](/docs/government/org-admin/users)                 | Find users, change their role or seat tier, check their usage, and reset their rate limits.                                    |
| [Seats](/docs/government/org-admin/seats)                 | See how many seats of each tier your organization has and how many are currently in use.                                       |
| [Tiers](/docs/government/org-admin/seat-tiers)            | Review the Anthropic-managed seat tiers and create your own tiers with custom model access and spend limits.                   |
| [Group mappings](/docs/government/org-admin/provisioning) | Map directory groups to seat tiers and roles so that users added through your directory land in the right place automatically. |

**Usage**

| Page                                                   | What it's for                                                                                                          |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| [Analytics](/docs/government/org-admin/analytics)           | Review requests, tokens, spend, top users, and credit balance over time across your organization.                      |
| [Compliance API](/docs/government/org-admin/compliance-api) | Create and manage read-only API keys that stream your organization's audit events to a SIEM or log management system.  |
| [Billing](/docs/government/org-admin/billing)               | See the billing account that funds your organization, its balance and any spend caps, and adjust your seat allocation. |

**Settings**

| Page                                          | What it's for                                                                                                                     |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [Config](/docs/government/org-admin/configuration) | Adjust product settings such as telemetry, the Claude Desktop banner, and product availability for everyone in your organization. |
| [Readiness](/docs/government/org-admin/readiness)  | See what is blocking users from using Claude and where each item is resolved.                                                     |

<Warning>
  The **Billing** tab only appears when the billing account is active and your own organization is active on it. If you don't see it, contact your tenant administrators about credits or spend caps.
</Warning>

<Warning>
  The **Group mappings** tab only appears if automatic directory provisioning has been set up for your tenant. If you don't see it, your tenant administrator has not connected a directory, and users are placed by the tenant's routing rules alone.
</Warning>

<Note>
  Single sign-on and the SCIM provisioning connection are configured at the tenant level, so they are managed on the [tenant portal's Identity and access page](/docs/government/tenant-admin/identity-and-access) rather than here.
</Note>

## How changes take effect

Most changes you make in this portal take effect immediately. Changing a user's seat tier, updating a spend limit, or resetting a user's rate limits applies to their very next request. Product configuration changes are picked up the next time a user's Claude application refreshes its settings, which happens when the application is launched or when the user signs in. Group mapping changes trigger an immediate re-sync so you do not need to wait for a scheduled cycle.
