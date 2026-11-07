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

To add a mapping, choose a group and a tier and click **Add**. Members of the group are moved to that tier, existing users included. To change a group's tier, click **Remove** on its mapping and add a new one. Each group can be mapped to at most one tier.

* **Someone who leaves a mapped group, or whose group's mapping is removed,** keeps the tier, with its models and spend limits, until another mapping or an owner moves them. On a tier with a seat limit, a [reconciliation](#how-mappings-are-applied) can move them too.
* **Mapping a group to a tier with a seat limit** can move other people off it. At a reconciliation, provisioned users on it who are in no mapped group can be moved to the tier in [step 3](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically) if it comes before theirs. On the tier marked **New members start here**, they stay.

If no groups have appeared at all, ask your tenant administrator to assign groups to the Claude for Government application in your identity provider and run a provisioning sync first.

## Group to role

Make your first role mapping a group that holds all your Owners, mapped to **Owner**. An Owner left out of it can lose access to this portal. You cannot map a group to Primary Owner; grant that role on the [Users](https://claude.com/docs/government/org-admin/users.md) page.

While this organization has no group-to-role mapping, members keep their roles unless a rule [moves them to another organization](https://claude.com/docs/government/tenant-admin/identity-and-access.md#when-rules-move-people). Once it has one, every member [linked to your directory](https://claude.com/docs/government/tenant-admin/identity-and-access.md#existing-accounts-when-you-connect-scim) except a Primary Owner gets their mapped role, or **User** if none of their groups is mapped. So you don't need to map any group to **User**.

## How mappings are applied

Each push from your identity provider is applied to your user list by a reconciliation pass.

* **After a mapping change.** Adding or removing a mapping starts a full reconciliation, so existing users are re-evaluated without waiting for your identity provider's next sync. In a very large directory, it can take hours.
* **Several mapped groups.** When a provisioned user belongs to several groups mapped to a seat tier, the one highest in your tenant's [group priority](https://claude.com/docs/government/tenant-admin/identity-and-access.md#directory-groups) decides. For roles, an order you can't see or change decides, and **User** can win over **Owner**. So don't map a group that includes your Owners, such as an all-staff group, to **User**.
* **No mapped group.** See [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically).
* **No free seats.** If a new person's mapped or marked tier is full, provisioning doesn't add them yet. An existing member whose mapped tier is full keeps their current tier or stays **Unassigned**. They are tried again at each full reconciliation, which changing seat allocations or mappings starts, and when your directory updates their entry.

## What your directory controls

* Provisioning is the source of truth while it is connected. A seat tier (**Unassigned** included) or role you set manually on the [Users](https://claude.com/docs/government/org-admin/users.md) page can be overwritten on the next reconciliation. Make permanent changes in your directory or in your group mappings instead.
* Deactivating a user in your directory deactivates their linked account in Claude for Government and releases its seat, unless provisioning refuses the deactivation. Reactivating them in the directory reactivates them here if a seat is free for them. If they stay deactivated, free a seat for them, then deactivate and reactivate them in your directory.
* Provisioning will not deactivate or demote a Primary Owner, or deactivate your tenant's only active tenant administrator. To deactivate a Primary Owner, first change their role on the [Users](https://claude.com/docs/government/org-admin/users.md) page (if they are the only one, make someone else Primary Owner first), then have your directory send or resend the deactivation.
* Provisioning can also refuse to deactivate a user whose account is not yet linked to your directory: see [Existing accounts when you connect SCIM](https://claude.com/docs/government/tenant-admin/identity-and-access.md#existing-accounts-when-you-connect-scim).
