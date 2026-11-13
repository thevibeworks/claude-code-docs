> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization administration

> Manage the people, seats, and settings for a single organization within your agency: users, roles, seat tiers, usage, billing, and Config.

> **Who this portal is for:** Organization owners. If you manage multiple organizations across your agency, see the [Tenant administration](https://claude.com/docs/government/tenant-admin/overview.md) guide instead.

The organization admin portal is where you manage the people, seats, and settings for a single organization in Claude for Government.

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/KCl5HZFMS3Q5oYkr/images/government/videos/admin-05-organization-owners-users-seat-tiers-and-readiness-v3.mp4?fit=max&auto=format&n=KCl5HZFMS3Q5oYkr&q=85&s=e77c642afb5785e19b1e7519d9310f64" aria-label="Video walkthrough: Organization owners: users, seat tiers, and Readiness" />

Video: Organization owners: users, seat tiers, and Readiness (1 min 48 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#users-seat-tiers-and-readiness-for-organization-owners)

## Key concepts

In an organization, a member's [role](https://claude.com/docs/government/org-admin/users.md#understanding-roles) decides what they can manage, and their [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md) decides which models they can use and how much. For how organizations fit into your agency's tenant, see [How your deployment is organized](https://claude.com/docs/government/overview.md#how-your-deployment-is-organized).

## Who can access it

You can reach the organization admin portal if your role in the organization is **Owner** or **Primary Owner**. Users who hold the standard **User** role are redirected to their personal account page instead.

> **For tenant administrators:** You can also open this portal for any organization in your tenant. When the tenant has more than one organization, an organization switcher appears at the top of the admin view so you can choose which one you're managing. All the changes you make while acting as an organization apply to that organization, and the audit trail records your own identity as the actor.

## Getting around

You can reach the [user view](https://claude.com/docs/government/account/overview.md) from the **Switch to user view** link in the page footer. If you are also a tenant administrator, the footer additionally offers **Switch to tenant view**.

## Pages in this portal

* **[Setup wizard](https://claude.com/docs/government/org-admin/setup-wizard.md)**: finish setting up a new organization
* **[Users](https://claude.com/docs/government/org-admin/users.md)**: find users, change their role or seat tier, and check their usage
* **[Seats](https://claude.com/docs/government/org-admin/seats.md)**: see how many seats of each tier your organization has and how many are currently in use
* **[Tiers](https://claude.com/docs/government/org-admin/seat-tiers.md)**: review the Anthropic-managed seat tiers and create your own tiers with custom model access and spend limits
* **[Group mappings](https://claude.com/docs/government/org-admin/provisioning.md)**: map directory groups to seat tiers and roles so that users added through your directory land in the right place automatically
* **[Analytics](https://claude.com/docs/government/org-admin/analytics.md)**: review requests, tokens, and top users over time across your organization
* **[Billing](https://claude.com/docs/government/org-admin/billing.md)**: see the billing account that funds your organization and any spend caps
* **[Readiness](https://claude.com/docs/government/org-admin/readiness.md)**: see what is blocking users from using Claude and where each item is resolved
* **[Config](https://claude.com/docs/government/org-admin/configuration.md)**: adjust product settings, such as which products members get, for everyone in your organization
* **[Admin API keys](https://claude.com/docs/government/org-admin/admin-api-keys.md)**: create and manage the read-only keys your tools use with the [Compliance API](https://claude.com/docs/government/org-admin/compliance-api.md) and the [Analytics API](https://claude.com/docs/government/org-admin/analytics-api.md)

The **Billing** and **Group mappings** tabs appear in the navigation only when they apply to your organization, and each of those pages says when.

> [!NOTE]
>
> Single sign-on and the SCIM provisioning connection are configured at the tenant level, so they are managed on the [tenant portal's Identity and access page](https://claude.com/docs/government/tenant-admin/identity-and-access.md) rather than here. The routing rules that place people in your organization are managed there too, by tenant administrators.

## How changes take effect

Most changes you make in this portal take effect immediately. Changing a user's seat tier, updating a spend limit, or resetting a user's rate limits applies to their very next request. For when settings on the **Config** page reach your users' Claude applications, see [When changes take effect](https://claude.com/docs/government/config/overview.md#when-changes-take-effect).
