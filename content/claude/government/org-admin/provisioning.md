> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Group mappings

> Map directory groups to seat tiers and roles in your organization, and see how mappings are applied and what a deactivation in your directory does.

> **Who this is for:** Organization owners who want directory groups to drive seat tiers and roles automatically.

Once a SCIM connection is in place, your directory groups appear here and you can map each one to a **seat tier** (a named level of access that determines which Claude models and usage limits a user gets) and a **role** (which controls whether a user can access this admin portal).

> [!NOTE]
>
> The **Group mappings** tab only appears in the navigation if automatic directory provisioning has been set up for your tenant. If you don't see the tab, your tenant administrator has not connected a directory. These cases are covered on other pages:
>
> * **SCIM connection**: the base URL and secret token are set up once for the whole tenant under [SCIM provisioning](https://claude.com/docs/government/tenant-admin/identity-and-access.md#scim-provisioning) on the tenant portal's Identity and access page
> * **Group to organization routing**: mapping directory groups to organizations is handled under [Provisioning rules](https://claude.com/docs/government/tenant-admin/identity-and-access.md#provisioning-rules-scim) on the same page

## Group to seat tier

To add a mapping, choose a group and a tier and click **Add**. Members of the group are moved to that tier, existing users included. To change a group's tier, click **Remove** on its mapping and add a new one. Each group can be mapped to at most one tier, and you can only select tiers that are available to this organization (either an Anthropic-managed tier you have been allocated or a self-managed tier you created on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#creating-a-self-managed-tier) page).

* **Someone who leaves a mapped group** keeps the tier, with its models and spend limits, until another mapping or an owner moves them. On a tier with a seat limit, a [reconciliation](#how-mappings-are-applied) can move them too.
* **Mapping a group to a tier with a [seat limit](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically)** can move other people off it. At a reconciliation, provisioned users on it who are in no mapped group can be moved to another tier with a free seat. If none is free, they stay.

If no groups have appeared at all, ask your tenant administrator to assign groups to the Claude for Government application in your identity provider and run a provisioning sync first.

## Group to role

Map a directory group to **User** or **Owner**, and members of that group receive that role when they are provisioned. You cannot map a group to Primary Owner; that role must always be granted manually on the [Users](https://claude.com/docs/government/org-admin/users.md) page.

Once this organization has any group-to-role mapping, every provisioned member except a Primary Owner gets their mapped role, or **User** if none of their groups is mapped. Map your Owners' group first, so that they keep access to this portal.

## How mappings are applied

Each push from your identity provider is applied to your user list by a reconciliation pass.

* **After a mapping change.** Adding or removing a mapping starts a full reconciliation, so existing users are re-evaluated against the new mapping without waiting for your identity provider's next sync. In a very large directory, a full reconciliation can take hours.
* **Several mapped groups.** When a provisioned user belongs to several groups mapped to a seat tier, the one highest in your tenant's [group priority](https://claude.com/docs/government/tenant-admin/identity-and-access.md#directory-groups) decides. Role mappings follow a fixed order, so avoid mapping groups that share members to different roles.
* **No mapped group.** See [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically).
* **No free seats.** If a user's mapped tier has no free seats, provisioning doesn't add a new person yet, and an existing member keeps their current seat tier or stays **Unassigned**. Increasing the tier's allocation places them, up to the new limit.

## What your directory controls

* Provisioning is the source of truth while it is connected. A seat tier (**Unassigned** included) or role you set manually on the [Users](https://claude.com/docs/government/org-admin/users.md) page can be overwritten on the next reconciliation. Make permanent changes in your directory or in your group mappings instead.
* Deactivating a user in your directory deactivates their linked account in Claude for Government and releases its seat, unless provisioning refuses the deactivation. Reactivating them in the directory reactivates them here if a seat is free for them. If they stay deactivated, free a seat for them, then deactivate and reactivate them in your directory.
* Provisioning will not deactivate or demote a Primary Owner, or deactivate your tenant's only active tenant administrator. To deactivate a Primary Owner, first change their role on the [Users](https://claude.com/docs/government/org-admin/users.md) page (if they are the only one, make someone else Primary Owner first), then have your directory send or resend the deactivation.
* Provisioning can also refuse to deactivate a user whose account is not yet linked to your directory: see [Existing accounts when you connect SCIM](https://claude.com/docs/government/tenant-admin/identity-and-access.md#existing-accounts-when-you-connect-scim).
