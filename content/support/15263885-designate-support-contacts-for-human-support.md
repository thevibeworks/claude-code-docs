# Designate support contacts for human support

Choose which members of your organization can open tickets with Anthropic's human support team by designating support contacts. Users who aren't configured as support contacts get help from AI support, which can answer many common questions instantly.

Available on the Enterprise plan, and configurable by Primary Owners and Owners.

## How support routing works

When support contacts are turned on, members of designated groups can reach human support. Everyone else in your organization gets AI support, which handles most questions instantly.

When support contacts are turned off, everyone in your organization gets AI support and no one is routed to a human.

You can also extend human support to all Admins and Owners by checking **Always include Admins and Owners** when configuring support contacts.

## Default settings at launch

When the support contacts setting becomes available, the feature is turned on and **Always include Admins and Owners** is checked. This preserves existing behavior: your Admins and Owners keep human support access without any configuration work, and other users get AI support unless you add them to a designated group.

To grant human support access to additional users (such as a central IT team), designate them in a group through organization settings. To remove human support access for Admins and Owners, uncheck **Always include Admins and Owners**.

## Configure support contacts

Before configuring support contacts, make sure the groups you want to designate already exist in organization settings. Groups can be synced from your identity provider through SCIM or created manually. For more information, see **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

To configure support contacts:

1. Navigate to **[Organization settings > Organization and access](http://claude.ai/admin-settings/organization)**.

2. Find the **Support contacts** section and toggle the feature on.

3. Select the groups whose members should receive human support.

4. Check or uncheck **Always include Admins and Owners** to control whether your organization’s Admins and Owners can reach human support.

5. Save your changes.

To stop routing anyone to human support, turn the **Support contacts** toggle off. All users in your organization will receive AI support only.

## When changes take effect

The **Support contacts** setting will be available in organization settings starting on June 1, 2026. Settings configured between June 1 and June 8 don't affect support routing during this window. Organization settings will show a notice that changes are pending until the feature takes effect.

On June 8, 2026, this setting will take effect for all Enterprise plan organizations. After this date, users who aren't designated as support contacts can only access AI support.