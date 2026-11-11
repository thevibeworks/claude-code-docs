> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Config works

> Config levels in Claude for Government: how tenant, directory group, and organization settings combine, what locks do, and when changes reach members.

> **Who this is for:** Tenant administrators and organization owners who set product behavior for the people they manage.

The Config page is where you set product behavior, such as session limits, which products members get, and telemetry, for the people you manage. To open it, go to **Settings > Config** in the admin portal. The same page appears at both the tenant and the organization level, with the same list of settings. For the settings themselves, see [Available settings](https://claude.com/docs/government/config/settings.md).

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/QW2rDqtpaxS9YU5m/images/government/videos/admin-06-config-essentials-v2.mp4?fit=max&auto=format&n=QW2rDqtpaxS9YU5m&q=85&s=96c86f606126bba3b006c1950d4fa19d" aria-label="Video walkthrough: Config essentials" />

Video: Config essentials (2 min 23 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#config-essentials)

## How settings are applied

Each setting is resolved through a chain of levels, and a value set at any level becomes the starting point for the levels below it:

1. The Anthropic default
2. Your tenant
3. [Tenant-wide group settings](#group-specific-settings)
4. The organization
5. [Organization group settings](#group-specific-settings)

Expand a setting to see its chain view, which shows the value in effect and where it came from. Settings that may contain secrets, such as telemetry headers, are never echoed back in the chain view. You see that a value is set, but not what it is.

### Setting kinds

Each setting has a fixed kind, which decides how its values combine across the chain:

* A **simple value** is replaced at each level, and the most specific level that set it wins. Most settings work this way, including lists of values such as network hosts, where a lower level's list replaces the one above it.
* A **restriction** is a limit that each level below the tenant can tighten but not loosen from what the levels above it set. The tightest of those values takes effect, except that values set below a [lock](#locks) don't apply. For example, if the tenant sets a session timeout of 30 minutes, an organization can set 15, but a value of 60 has no effect.
* A **collection** accumulates entries from each level. A level can add entries to what the level above provided. Connectors and plugins work this way.

### Locks

A **lock** prevents levels below from changing a setting. To lock a setting on the tenant Config page or at either group level, expand it, choose **Must use this value**, and save. Levels below then see it marked **Locked by** your level and can't change it. Any value a lower level had previously set is ignored while your lock is in place, and it comes back into effect if you later remove the lock.

How far a lock reaches depends on where you set it:

* **On the tenant Config page**, the lock reaches everyone in the tenant. The setting becomes read-only for every organization and at both group levels.
* **On a tenant-wide group setting**, the lock reaches the people that group's settings apply to. They get the locked value even if their organization has set a different one, and organizations cannot set their own value for that group while the lock is in place. Other people in those organizations are not affected.

A group lock does not keep anyone on that group's settings. If someone in the group also belongs to a higher-priority group that has any configuration, that group's settings apply to them instead and the lock does not, as described under [When someone belongs to more than one group](#when-someone-belongs-to-more-than-one-group).

**Locked by Anthropic** means the lock was applied by Anthropic at the application level rather than by your own tenant. It appears on features that are not available in Claude for Government, and only Anthropic can change or unlock those settings.

## Group-specific settings

In addition to setting values for your whole tenant or organization, you can set values for the members of a directory group. A directory group is a group that your identity provider has pushed to Claude for Government over SCIM, as described on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md) page.

A group's settings can be tenant-wide or scoped to one organization:

* **Tenant-wide group settings** sit between the tenant and the organization in the chain. Tenant administrators manage these.
* **Organization group settings** are scoped to one organization. A value set here applies only to people who are both a member of the group and a member of that organization, and it is the most specific level in the chain. Organization owners manage these for their own organization and see the same list of groups the tenant does.

To edit settings for a group, choose the group in the scope bar on the Config page, which says whose settings you are editing. Groups appear there once your directory has pushed them. To add connectors for a group's members, see [Who receives a connector](https://claude.com/docs/government/connectors/overview.md#who-receives-a-connector).

> [!NOTE]
>
> The **Organization instructions**, **Organization Analytics connector**, and **Analytics API** settings can be set at the tenant and organization levels, but not at either group level. Settings that [only a tenant administrator can set](#what-differs-between-the-tenant-and-organization-levels) can't be set for a group.

### Turn a feature on for one group

How you give a feature to one group and nobody else depends on the setting:

* **A simple value, such as Code in Claude Desktop**: turn the feature off on the organization's Config page, then choose the group in the scope bar on that page and turn it on.
* **The switch for a whole product that is off until a level turns it on, such as Claude Code**: leave it unset for the tenant and the organization, and turn it on for the group. An off saved at the tenant or the organization takes priority over the group's on, so [reset](#working-with-the-list) it there first.

To do this for every organization at once, make the same changes on the tenant Config page and choose **Must use this value** for the group, so that an organization's own value can't override it. You can't also lock the feature off for everyone else, because that lock would apply to the group too. An organization can still turn it on for its own members.

### When someone belongs to more than one group

Only one group's settings apply to any given person. When someone is a member of more than one group, the settings from their highest-priority group that has any configuration are used, and the other groups are ignored for that person. A group has configuration for a person once any setting is set or locked for it, either as a tenant-wide group setting or as an organization group setting in that person's organization.

When a higher-priority group gains configuration for someone, it takes the place of the lower-priority group that applied to them before, and the lower-priority group's settings, including locked ones, stop applying to them. Removing a group's last setting, changing the priority order, or changing someone's group memberships in your identity provider can change which group applies to a person in the same way.

A tenant administrator sets the priority order on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md#directory-groups) page. It cannot be reordered at the organization level.

## What differs between the tenant and organization levels

Almost all settings can be set at either level, with these differences:

* **Some settings can be set only by a tenant administrator.** [Let organizations manage their own seat tiers](https://claude.com/docs/government/config/settings.md#let-organizations-manage-their-own-seat-tiers) and [Compliance API](https://claude.com/docs/government/config/settings.md#compliance-api) appear on both pages, but are always read-only at the organization level.
* **Tenant administrators can open any organization's Config page** and act on that organization's behalf, as described under [Config at the tenant level](https://claude.com/docs/government/tenant-admin/configuration.md). Organization owners see only [their own organization](https://claude.com/docs/government/org-admin/configuration.md).

## When changes take effect

Settings that govern the admin portal apply immediately. Settings that govern the Claude applications themselves are delivered to each member's application the next time it [refreshes its configuration](https://claude.com/docs/government/deploy-desktop/configure.md#things-to-know). You do not need to push anything.

Most changes take effect when the member restarts the application. Claude Desktop prompts for that restart, and requires it once the [Restart deadline for configuration changes](https://claude.com/docs/government/config/settings.md#restart-deadline-for-configuration-changes) has passed. On Claude Desktop 2.2553.0 and later, a few settings take effect in a running application without a restart, such as the **Claude Desktop banner**. The Claude Code command-line tool applies its settings [at startup and on an hourly poll](https://code.claude.com/docs/en/claude-apps-gateway#whats-enforced-on-developers).

Changes to the session limits reach members as follows:

* **Session idle timeout**: A shorter session idle timeout applies to new sign-ins immediately. Members who are already signed in move to it within the timeout period their session already had.
* **Maximum session length**: Raising or removing the maximum session length applies to new sign-ins only. Lowering the maximum session length, or setting one for the first time, also reaches members who are already signed in, taking up to one idle timeout period to do so.

## Working with the list

To remove your value and return to whatever the level above provides, expand the setting, select **Reset to default**, and save. Values set at other levels are unaffected and remain in effect once yours is gone.

### Previewing impact

On the tenant Config page, change a setting and select **Preview impact** before you save to see what each organization has now and what it would get. Preview isn't available for settings whose values are hidden for security reasons (for example, settings that can contain authorization tokens).

### Comparing settings across levels

On the Config page, select **Compare config across levels** to see every setting side by side across the full chain.

Type a name into the search box above the table to see what settings apply to that person. Select a row to see how its final value was reached.
