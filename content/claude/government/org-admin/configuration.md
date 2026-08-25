> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Config at the organization level

> View and change the product settings that apply to everyone in your organization, and see where each effective value comes from.

> **Who this is for:** Organization owners who set product behavior, such as the session timeout, Claude Desktop banner, and product availability, for everyone in their organization.

Use this page to view and change the product settings that apply to everyone in your organization, and to see where each effective value comes from.

The Config page works the same way at the tenant and organization levels, with the same list of settings. See [How Config works](/docs/government/config/overview) for the levels model, locks, groups, comparing across levels, and looking up one person's settings, and [Available settings](/docs/government/config/settings) for what each setting does. This page covers only what is specific to the organization level.

## What is specific to the organization level

**Managed settings.** A setting that your tenant has locked shows as **Managed** and is read-only here. Any value you had previously set is ignored while the lock is in place, and it comes back into effect if the tenant later removes the lock. See [Locks](/docs/government/config/overview#locks).

**Settings only the tenant can change.** [Let organizations manage their own seat tiers](/docs/government/config/settings#let-organizations-manage-their-own-seat-tiers) and [Compliance API](/docs/government/config/settings#compliance-api) are always read-only here, regardless of whether they are locked.

**Inherited plugins.** Plugins the tenant has added are labeled **Inherited from your tenant** and cannot be changed from here. See [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards).

**Group settings within your organization.** A value you set for a directory group at this level applies only to people who are both a member of the group and a member of your organization, and it is the most specific level in the chain. Group priority is set by your tenant administrator and is shown here for reference; you cannot reorder it from the organization portal. See [Group-specific settings](/docs/government/config/overview#group-specific-settings).

**Your own organization only.** Organization owners manage only their own organization's Config page. Tenant administrators can open any organization's Config page and act on that organization's behalf.
