> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Config works

> Understand how product settings in Claude for Government are resolved across the tenant, directory groups, and organizations, and how to find, change, compare, and lock them.

> **Who this is for:** Tenant administrators and organization owners who set product behavior for the people they manage.

The **Config** page in the admin portal is where you set product behavior such as the session timeout, Claude Desktop banner, product availability, and telemetry for the people you manage. The same page appears at both the tenant and the organization level, with the same list of settings, and this page explains how the two levels fit together. For the settings themselves, see [Available settings](/docs/government/config/settings).

## How settings are applied

Each setting is resolved through a chain that runs from the Anthropic default, to your tenant, to each organization. Directory groups add two further levels, described under [Group-specific settings](#group-specific-settings) below. A value set at any level becomes the starting point for the levels below it. An organization that doesn't set a value uses the tenant's value, and a tenant that doesn't set a value uses the Anthropic default. When you expand a setting you can see each step of this chain, which value is currently **In effect**, where it came from, and (in the tenant view) which organizations have set their own value.

### Setting kinds

Settings combine across the chain in one of three ways, and the kind is fixed per setting (you don't choose it):

* A **simple value** is replaced at each level, and the most specific level that set it wins. Most settings work this way.
* A **restriction** is a limit where the tightest value across all levels wins. Any level can tighten the limit but none can loosen it. For example, if the tenant sets a session timeout of 30 minutes, an organization can set 15 but cannot set 60. The value that takes effect is always the shortest one in the chain.
* A **collection** accumulates entries from each level. A level can add entries to what the level above provided, or replace the list entirely.

### Locks

A **lock** prevents levels below from changing a setting. When you lock a setting at your level it shows as **Enforced** to you, and levels below see it as **Managed**, which means it is read-only for them. Any value a lower level had previously set is ignored while your lock is in place, and it comes back into effect if you later remove the lock.

A tenant lock makes the setting read-only for every organization. A lock you set at the organization level prevents any group-level value within your organization from taking priority over it.

**Locked by Anthropic** is the **Managed** state when the lock was applied by Anthropic at the application level rather than by your own tenant. It appears on features that are not available in Claude for Government, and only Anthropic can change or unlock those settings.

Settings that may contain secrets, such as telemetry headers, are never echoed back in the chain view. You see that a value is set, but not what it is.

## When changes take effect

Settings that govern the admin portal, such as whether organizations may manage seat tiers, apply immediately. Settings that govern the Claude applications themselves, such as the Claude Desktop banner, product availability, and telemetry endpoint, are delivered to each member's application the next time it refreshes its configuration, which happens when the application is launched or the member signs in. You do not need to push anything, but members who are currently running the application may need to restart it to pick up a change. Lowering the session idle timeout applies to new sign-ins only, and so does raising or removing the maximum session length. Lowering the maximum session length, or setting one for the first time, also reaches members who are already signed in, taking up to one idle timeout period to do so, as described under [Maximum session length](/docs/government/config/settings#maximum-session-length).

## Working with the list

Settings are grouped by category in the sidebar on the left. Select a category to see its settings; the number beside each category shows how many settings it contains.

Each setting appears as an expandable card showing its name, a one-line description, which products it applies to, its current value, and where that value comes from (for example, **From Anthropic default** or **Set at tenant**). Click a card to expand the full chain and the editor.

The scope bar above the list shows which level you are editing and lets you switch between levels when you have access to more than one. Use **Compare config across levels** to see every setting side by side across the full chain.

To change a setting, expand it, adjust the value, and save. To remove your value and return to whatever the level above provides, reset it.

## Previewing impact

After you change a setting at the tenant level, a **Preview impact** button appears next to **Save changes**. Select it to see a table listing every organization with its current effective value and what it would become after your change. Organizations where nothing would change are marked **unchanged**. This is especially useful when locking a setting, so you can see which organizations currently have a different value that your lock will take priority over.

Preview isn't available for settings whose values are hidden for security reasons (for example, settings that can contain authorization tokens). For those settings the preview shows whether a value is set rather than what it is.

<Note>
  **Preview impact** is available at the tenant level because it shows the effect of a tenant change across every organization. It does not appear at the organization level.
</Note>

## Comparing settings across levels

Select **Compare config across levels** at the top of the Config page to open a read-only table that lays every setting out side by side across the full chain. This view is for understanding how a value got to be what it is, and for spotting which levels have set their own value for which settings. You can't change anything from here; each row has an **Edit** link that takes you back to that setting on the main Config page.

The table has one row per setting and one column per level in the chain: the **Anthropic default**, your **Tenant**, **Groups** (tenant-wide group settings), each **Organization** you can see, **Org groups** (group settings scoped to one organization), and the **Final value** that actually takes effect. A dash means that level has not set a value for that setting. A lock icon next to a value means that level has locked it, and anything below it in the chain is ignored. Use the **All levels** / **Final only** toggle to hide the middle columns and show just the setting, where it was set, and the final value.

Before you pick a person, the **Groups** and **Organization** columns list every group and organization that has set its own value for that setting, so you can see at a glance where different values have been set across the levels you can see.

### Looking up one person's settings

Type a name into the search box above the table to see exactly what settings apply to that person. The table re-resolves every setting from that person's point of view: the **Groups** column shows the value from the one group that applies to them (with any lower-priority groups they belong to shown faded, since those do not count), the **Organization** column shows their organization's value, and the **Final value** column shows what they actually get. A summary card above the table lists the tenant, group, and organization being used for the lookup.

Click any row to expand a plain-English explanation of how the final value was reached, for example "Anthropic's default is On. Your tenant hasn't changed it. The Program-Reviewers group sets this to Off." This is the quickest way to answer a question like "why is this turned off for this person?" or "why can't this person use Code in Claude Desktop?"

## Group-specific settings

In addition to setting values for your whole tenant or organization, you can set values for the members of a directory group. A directory group is a group that your identity provider has pushed to Claude for Government over SCIM, as described on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page.

There are two kinds of group level:

* **Tenant-wide group settings** sit between the tenant and the organization in the chain. A value set here takes priority over the tenant default for the group's members, in every organization they belong to. Tenant administrators manage these.
* **Organization group settings** are scoped to one organization. A value set here applies only to people who are both a member of the group and a member of that organization, and it is the most specific level in the chain. Organization owners manage these for their own organization and see the same list of groups the tenant does.

To edit settings for a group, open the scope bar above the settings list and choose the group's name from the dropdown. The page switches to show the same settings editor, now scoped to that group. Editing, saving, resetting, and locking all work the same way as at the other levels. Anything locked at a higher level still shows as **Managed** here and cannot be changed.

### When someone belongs to more than one group

Only one group's settings apply to any given person. When someone is a member of more than one group, the settings from their highest-priority group that has any configuration are used, and the other groups are ignored for that person. The priority order is set by a tenant administrator on the [Identity and access](/docs/government/tenant-admin/identity-and-access) page by dragging the groups into the order they want. The same priority order is used wherever configuration is resolved for a person; seat-tier group mappings on the [Provisioning](/docs/government/org-admin/provisioning) page use a separate fixed order. At the organization level the priority order is shown for reference and cannot be reordered there.

If no groups appear in the scope bar dropdown, none have been synced from the identity provider yet. Connect SCIM on the Identity and access page and push groups from your directory, and they will appear automatically.

<Note>
  Two settings, **Organization instructions** and **Organization Analytics connector**, can be set at the tenant and organization levels but not at either group level.
</Note>

## What differs between the tenant and organization levels

The Config page shows the same list of settings at both levels, and almost all of them can be set at either level. The genuine differences are:

* **Two settings can be set only by a tenant administrator.** [Let organizations manage their own seat tiers](/docs/government/config/settings#let-organizations-manage-their-own-seat-tiers) and [Compliance API](/docs/government/config/settings#compliance-api) appear on both pages, but are always read-only at the organization level.
* **Preview impact appears only at the tenant level.** See [Previewing impact](#previewing-impact) above.
* **Group priority is set at the tenant level.** Organization owners see the priority order for reference but cannot change it.
* **Tenant administrators can open any organization's Config page** and act on that organization's behalf. Organization owners see only their own organization.
* **Inherited plugins are labeled at the organization level.** Plugins the tenant has added appear under a **From levels above** heading on the organization page; see [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards).

For more detail see [Config at the tenant level](/docs/government/tenant-admin/configuration) and [Config at the organization level](/docs/government/org-admin/configuration).

## Things to know

* Some settings can only be changed by tenant administrators (and not by organization owners at all), regardless of whether they are locked. These are noted in the [Available settings](/docs/government/config/settings) descriptions.
* Resetting a setting removes only that level's value. Values set at other levels are unaffected and remain in effect once yours is gone.
