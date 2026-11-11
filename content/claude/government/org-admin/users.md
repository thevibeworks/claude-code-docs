> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Users

> Find a user, change their role or seat tier, sign them out everywhere, check and reset their usage limits, and see what each organization role can do.

> **Who this is for:** Organization owners who need to manage individual users' roles, seat tiers, and usage limits.

The **Users** page lists everyone in your organization and lets you manage their access. Use **Filters** to narrow the list by role or seat tier, or to include deactivated accounts.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Adding people to your organization**: see [How people get access](https://claude.com/docs/government/overview.md#how-people-get-access)
> * **Users your directory provisions**: provisioning can overwrite a role or seat tier you set here, **Unassigned** included, as described under [What your directory controls](https://claude.com/docs/government/org-admin/provisioning.md#what-your-directory-controls)

## Understanding roles

A **role** controls what a person can do in the admin portal. It has no effect on which Claude models they can use or how much they can use them; those are controlled by the [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md).

* A **User** can use the Claude products but has no admin access.
* An **Owner** can access this organization admin portal and manage its users, seats, and settings.
* A **Primary Owner** can do everything an Owner can, can grant or remove the Primary Owner role, and can create [admin API keys](https://claude.com/docs/government/org-admin/admin-api-keys.md) that read usage and cost reports.

There are no additional roles such as Billing or Developer. Tenant administrator access is a separate tenant-level membership managed on the [Admins](https://claude.com/docs/government/tenant-admin/admins.md) page, not an organization role.

An organization may have up to three active Primary Owners. If your organization no longer has a Primary Owner who can sign in, ask a tenant administrator to promote a replacement, unless your organization [manages its own billing account](https://claude.com/docs/government/org-admin/billing.md#seats). If it does, contact Anthropic instead to have a new Primary Owner appointed. Until then, your Owners and tenant administrators can keep managing users and settings.

## Change a role

Use the **Role** dropdown on a user's card to change their role. The change applies immediately, and a user who is promoted to Owner can open the admin portal as soon as they refresh.

The following safeguards apply and the dropdown will refuse the change if any of them would be violated.

* You cannot change your own role.
* An Owner can freely move people between User and Owner, but can't grant or remove the Primary Owner role. A Primary Owner can grant or remove it. A tenant administrator can too, unless your organization [manages its own billing account](https://claude.com/docs/government/org-admin/billing.md#seats).
* You cannot demote the organization's only active Primary Owner. Promote a second person to Primary Owner first, then demote the original.
* You cannot promote a deactivated user to Primary Owner. Reactivate them first.

## Assigning a seat tier

Use the **Seat tier** dropdown to move a user onto a different tier or back to **Unassigned**. An unassigned user has no model access at all, but keeps their account and any admin access. If a tier has no seats remaining it appears marked **(at capacity)** and cannot be selected, unless the user is already on it. Only a Primary Owner can change a Primary Owner's seat tier here. If one of the user's directory groups is mapped to another seat tier, the mapping puts them back on it, so first change the [mapping](https://claude.com/docs/government/org-admin/provisioning.md#group-to-seat-tier) or the user's groups.

Changing a user's tier takes effect on their very next request. If you move someone to a tier with a different set of allowed models, any model that is not among their new tier's allowed models becomes unavailable to them immediately. Moving a user between tiers does not reset their usage counters, which are measured against the new tier's limit on their next request.

## Reset usage limits

Every [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md) sets a **5-hour** and a **7-day** spend limit for each user. When a user reaches either limit, further requests are refused until that limit resets. The **Usage** bars on a user's card show how much of the user's 5-hour and 7-day spend limits are currently used. Hover over the bars to see when each limit resets.

If a user on a self-managed tier has hit a limit and you want them to continue working immediately, use **Reset usage limits** in the **…** menu on their card. This clears both of their current windows so their next request is admitted. Their usage still shows on the [Analytics](https://claude.com/docs/government/org-admin/analytics.md) page.

> [!NOTE]
>
> You cannot reset limits for users on [Anthropic-managed tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers).

## Sign out everywhere

The **…** menu on each card has **Sign out everywhere**, which ends every session the user has open, in the browser and in Claude apps on all their devices. They can sign in again unless their account is deactivated.

## Deactivated users

Accounts are deactivated through your directory's SCIM provisioning rather than from this page. A deactivated user cannot sign in. Deactivating a user releases their [seat](https://claude.com/docs/government/org-admin/seats.md). Reactivating them brings the account back if a seat is free for them, as described under [What your directory controls](https://claude.com/docs/government/org-admin/provisioning.md#what-your-directory-controls).

Deactivated users keep their role. Deactivating a user leaves their Claude Desktop conversations and projects on the devices they used. To remove them, see [Removing data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#removing-data) in the Claude Desktop documentation.

## Copy user email addresses

To email everyone in your organization, select the **Copy user email addresses** button at the top of the **Users** page. The page that opens lists every user's email address except deactivated users.
