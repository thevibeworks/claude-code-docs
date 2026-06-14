Title: Manage groups and group spend limits on Enterprise plans

URL Source: https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans

Markdown Content:
## What are groups?

Groups let you organize members into logical collections — by team, department, or any other grouping that fits your organization. Once groups are set up, you can:

Groups can be created manually or synced automatically from your identity provider via SCIM. Each organization can have up to 100 groups.

In addition to spend limits, Enterprise admins can use groups to control plugin access in Cowork. Each plugin in your organization's marketplace can have group-level overrides that determine whether it's available, pre-installed, required, or hidden for members of a specific group. For details, see **[Manage Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

## Create a group

## Edit a group

Click any group in the list to open its edit form. You can change the name, update custom role assignments, and add or remove members.

## Delete a group

Click the menu button to the right of any group and select "Delete." Deleting a group doesn't affect the custom roles that were assigned to it and doesn't remove any members from your organization.

## SCIM group sync

If your organization uses SCIM directory sync, groups from your identity provider are automatically synced to Claude. SCIM groups appear with a sync indicator in the groups list.

SCIM groups support custom role assignments and spend limits the same way as manually created groups.

To manually trigger a sync, click “SCIM Sync."

## Control member access with custom roles

You can control individual members' feature access entirely through groups and custom roles. When a member's role is set to **Custom roles**, they have no default capabilities or permissions—their access is determined entirely by the custom roles assigned to their groups. This is different from the User, Admin, or Owner roles, which include built-in permissions.

### Set a member's role to Custom roles

Only Owners and Primary Owners can change member roles. You can also assign “Custom roles” at scale by mapping an IdP group using[**group mappings**](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning).

### Recommended setup

The member's effective permissions are now determined by their group memberships and the custom roles assigned to those groups.

### Inviting new members

When inviting a new member, Owners and Primary Owners can select "Custom roles" as the role. The new member's access is determined by their group memberships after they join.

## Group spend limits

Group spend limits let you control spending across your organization by assigning per-user monthly spend limits to groups. Instead of setting spend limits for each member individually, you can set a limit on a group and have it apply to every member of that group.

Group spend limits work alongside individual spend limits. If a member has an individual spend limit set, their individual limit takes precedence over any group limit.

## Set a group spend limit

The spend limit applies to all members of the group. Members who also have an individual spend limit set are governed by their individual limit instead.

## How spend limits are resolved

When determining a member's effective spend limit, the system evaluates in this order:

* * *

Related Articles

[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)[Migrate your organization from Team to Enterprise](https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise)[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)[How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)
