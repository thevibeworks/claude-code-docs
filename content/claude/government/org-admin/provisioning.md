> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Group mappings

> Use this page to map the groups pushed from your identity provider to seat tiers and roles in this organization.

> **Who this is for:** Organization owners who want directory groups to drive seat tiers and roles automatically.

Use this page to map the groups pushed from your identity provider to seat tiers and roles in this organization.

<Note>
  The **Group mappings** tab only appears in the navigation if automatic directory provisioning has been set up for your tenant. If you don't see the tab, your tenant administrator has not connected a directory.
</Note>

**SCIM** (System for Cross-domain Identity Management) is the standard protocol that identity providers such as Okta and Microsoft Entra use to push user accounts and group memberships into other applications. Once a SCIM connection is in place, your directory groups appear here and you can map each one to a **seat tier** (a named level of access that determines which Claude models and usage limits a user gets) and a **role** (which controls whether a user can access this admin portal).

<Note>
  The SCIM connection itself, including the base URL and secret token, is set up once for the whole tenant on the [tenant portal's Identity and access page](/docs/government/tenant-admin/identity-and-access). This page only covers the group mappings for your organization.
</Note>

## How provisioning works

Your identity provider pushes users and groups to Claude for Government whenever something changes in your directory, and most providers also run a full sync periodically (the default interval depends on your identity provider). Each push is written to a staging area first and then applied to your real user list by a reconciliation pass.

Reconciliation runs automatically whenever your identity provider pushes a change and also whenever you add, edit, or remove a mapping on this page. You do not need to trigger it manually, and you do not need to wait for a scheduled cycle after changing a mapping.

## Group to seat tier

To add a mapping, choose a group and a tier and click **Add**. Existing mappings are listed with a **Remove** button. Each group can be mapped to at most one tier, and you can only select tiers that are available to this organization (either an Anthropic-managed tier you have been allocated or a self-managed tier you created on the [Tiers](/docs/government/org-admin/seat-tiers) page).

<Note>
  The **Add** form only appears when at least one synced group is still unmapped. If no groups have appeared at all, assign groups to the Claude for Government application in your identity provider and run a provisioning sync first.
</Note>

## Group to role

The same mechanism can set a user's role. Map a directory group to **User** or **Owner**, and members of that group receive that role when they are provisioned. You cannot map a group to Primary Owner; that role must always be granted manually on the [Users](/docs/government/org-admin/users) page.

## How mappings are applied

When a provisioned user belongs to several mapped groups, the first matching tier mapping and the first matching role mapping in a fixed order win. This order is deterministic but not one you can configure, so it is best to avoid assigning a user to overlapping mapped groups.

A provisioned user who belongs to no mapped group is placed on a seat using the automatic assignment described on the [Seats](/docs/government/org-admin/seats) page and is given the standard **User** role.

If a mapped tier has no free seats when a user is provisioned, the user is created but left **Unassigned** and has no model access. They will be seated automatically on the next reconciliation after seats become available, for example after you increase the allocation on the [Billing](/docs/government/org-admin/billing) page or another user is deactivated.

Adding, changing, or removing a mapping triggers a full reconciliation immediately, so existing users are re-evaluated against the new mapping without waiting for your identity provider's next sync.

## Group to organization routing

> **For tenant administrators:** Mapping directory groups to organizations is handled on the [tenant portal's Identity and access page](/docs/government/tenant-admin/identity-and-access) rather than here.

## Things to know

* Provisioning is the source of truth while it is connected. A seat tier or role you set manually on the [Users](/docs/government/org-admin/users) page will be overwritten on the next reconciliation if the user's group mappings say otherwise. Make permanent changes in your directory instead.
* Deactivating a user in your directory deactivates them in Claude for Government and releases their seat. Reactivating them in the directory reactivates them here and attempts to seat them again.
* The reconciliation pass protects against removing your last administrator. It will not deactivate the organization's only active Primary Owner, and it will not deactivate the tenant's only tenant administrator, even if your directory says to.
* A group mapping cannot be saved if it points at a seat tier that no longer exists, and a seat tier cannot be deleted on the [Tiers](/docs/government/org-admin/seat-tiers) page while a mapping still points at it.
