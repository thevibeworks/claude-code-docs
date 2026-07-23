# Manage groups and group spend limits on Enterprise plans

Groups and group spend limits are available for Enterprise plan organizations. Owners, Primary Owners, and custom roles with the **Identity & Access** permission set to "Can manage" can go to **[Organization settings > Groups](http://claude.ai/admin-settings/groups)** to manage groups. Owners, Primary Owners, and custom roles with the **Billing** permission set to "Can manage" can go to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)** to manage group spend limits. Group visibility settings are currently in beta.

## What are groups?

Groups let you organize members into logical collections—by team, department, or any other grouping that fits your organization. Once groups are set up, you can:

- **Set spend limits for groups**, so all members of a group share a per-user spend limit.

- **Control member access through group memberships and custom roles**, so their capabilities and permissions are determined entirely by the groups they belong to. For additional details, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

- **Let members share projects with a group**, so a project shared with the group is available to everyone in it, and access follows membership as it changes. For details, see[**Manage project visibility and sharing**](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing).

Groups can be created manually or synced automatically from your identity provider via SCIM. Each organization can have up to 100 groups. There's no limit on how many groups a member can belong to, though belonging to more than 250 can slow performance.

In addition to spend limits, Enterprise admins can use groups to control plugin access in Cowork. Each plugin in your organization's marketplace can have group-level overrides that determine whether it's available, pre-installed, required, or hidden for members of a specific group. For details, see **[Manage Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

---

## Create a group

1. Navigate to **[Organization settings > Groups](http://claude.ai/admin-settings/groups)**.

2. Click "Add group."

3. Enter a **Group name**.

4. Optionally enter a **Display name**. The display name replaces the group name on in-product surfaces, like the project sharing picker. Leave it blank to use the group name.

5. Select which custom roles to assign to this group (optional).

6. Under **Visibility settings**, choose who can discover the group, share resources like projects with it, and see its members (optional).

7. Search for and add members, or click "Add all members" to add everyone in your organization.

8. Click "Add group."

**Note:** If SCIM directory sync is enabled, you’ll see a “SCIM Sync” button next to "Add group." Clicking this will manually refresh groups from your identity provider.

## Edit a group

Click any group in the list to open its edit form. You can change the group name and display name, update custom role assignments, change visibility settings, and add or remove members.

To change settings for several groups at once, select them with the checkboxes in the groups list, then click the "Edit settings" button that appears.

**Note:** Groups synced from your identity provider via SCIM can't be renamed or deleted in Claude, and their members are managed in your identity provider.

## Delete a group

Click the menu button to the right of any group and select "Delete." Deleting a group doesn't affect the custom roles that were assigned to it and doesn't remove any members from your organization. Deleting a group also removes its access to any projects shared with it. Members lose access to those projects unless they have access another way.

---

## SCIM group sync

If your organization uses SCIM directory sync, groups from your identity provider are automatically synced to Claude. SCIM groups appear with a sync indicator in the groups list.

SCIM groups support custom role assignments and spend limits the same way as manually created groups.

To manually trigger a sync, click “SCIM Sync."

**Note:** Claude supports direct group memberships only. If your identity provider nests groups inside other groups, those relationships are ignored when memberships are pushed via SCIM, and only direct members appear in Claude. Some providers flatten nested memberships before pushing them, which makes members of child groups appear as direct members. Check your provider's SCIM behavior to confirm.

---

## Group visibility

Group visibility settings are currently in beta.

By default, groups appear only on admin surfaces. Visibility settings let you make a group discoverable to members so they can share resources (like projects) with it. You set them in the **Visibility settings** section when creating or editing a group.

There are three settings:

- **Discover this group:** Members can find the group by name. This doesn't expose group members, spend limits, or role assignments.

- **Share projects with this group:** Members can share resources, such as projects, with the group.

- **See group members:** Members can see who belongs to the group, by name and email address.

For each setting, select **Group members** to grant it to members of that group, or **Everyone** to grant it to everyone in your organization. Leave both unchecked to keep the setting off.

Visibility settings don't affect admin access. Owners, Primary Owners, and custom roles with **Identity & Access** access always see every group.

The **Visibility** column in the groups list shows each group's current state. New visibility settings can take a few minutes to appear in-app.

**Important:** Visibility settings are configured per organization. Groups, group membership, and SCIM sync are managed at the parent organization level and shared across child organizations, but visibility settings aren't. An admin changing visibility settings in one organization doesn't affect any other organization.

### Remove a group's access to shared projects

Turning off **Share projects with this group** blocks new shares. It doesn't revoke projects already shared with the group. To revoke those:

1. Open the group's edit form.

2. Under **Visibility settings**, select "Remove this group's access to all [number] projects."

3. Save the group.

This revokes existing shares only. It doesn't block future sharing, so turn off **Share projects with this group** as well if you want both.

**Note:** Removing a group's access runs in the background. For groups with more than 1000 shared projects, it can take several minutes or longer.

---

## Control member access with custom roles

You can control individual members' feature access entirely through groups and custom roles. When a member's role is set to **Custom**, they have no default capabilities or permissions—their access is determined entirely by the custom roles assigned to their groups. This is different from the User, Admin, or Owner roles, which include built-in permissions.

### Set a member's role to Custom

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)**.

2. Find the member and click their role dropdown.

3. Select "Custom."

Owners, Primary Owners, and custom roles with the **User Management** permission set to "Can manage" can change member roles. You can also assign “Custom” at scale by mapping an IdP group using **[group mappings](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

### Recommended setup

1. Create custom roles with the desired permissions in **[Organization settings > Roles](http://claude.ai/admin-settings/roles)**. For details, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

2. Create groups in **[Organization settings > Groups](http://claude.ai/admin-settings/groups)** (or sync them from your identity provider).

3. Assign custom roles to groups.

4. Add members to the appropriate groups.

  1. **Note:** If a member set to a Custom role isn't in any groups, or their groups have no custom roles assigned, they have no permissions and can't access any products. They'll land on their settings page when they sign in.

5. Set each member's organization role to **Custom**.

6. Enable any features at the organization level that you want to control per-group.

The member's effective permissions are now determined by their group memberships and the custom roles assigned to those groups.

**Important:** Always complete steps 1–5 before enabling features at the organization level (step 6). If you enable a feature before changing members' roles to Custom and assigning appropriate custom roles, there's a brief window where some members could access the feature through their previous role. For a detailed walkthrough, see **[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-entitlements-on-enterprise-plans)**.

### Invite new members

When inviting a new member, Owners, Primary Owners, and custom roles with the **User Management** permission set to "Can manage" can select "Custom” as the role.The new member's access is determined by their group memberships after they join.

---

## Group spend limits

Group spend limits let you control spending across your organization by assigning per-user monthly spend limits to groups. Instead of setting spend limits for each member individually, you can set a limit on a group and have it apply to every member of that group.

Group spend limits work alongside individual spend limits. If a member has an individual spend limit set, their individual limit takes precedence over any group limit.

## Set a group spend limit

1. Navigate to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

2. Select the “By group” tab.

3. Find the group and click the menu button to the right, then “Edit limit”

4. Select “Unlimited,” or “Set dollar amount” and enter a dollar amount for the spend limit.

5. Click "Set limit."

The spend limit applies to all members of the group. Members who also have an individual spend limit set are governed by their individual limit instead.

## Choose how multi-group spend limits resolve

If a member belongs to more than one group with a spend limit, the **Multi-group spend limit** setting controls which limit applies.

1. Navigate to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

2. Find **Multi-group spend limit** in the **Spending defaults** section.

3. Select "Higher group limit" or "Lower group limit" from the dropdown.

Select "Lower group limit" to set a broad limit on a large group and create subgroups with tighter budgets. Select "Higher group limit" to set a conservative baseline on a large group and grant more headroom to specific teams.

## How spend limits are resolved

When determining a member's effective spend limit, the system evaluates in this order:

1. **Individual limit**—if the member has an individual spend limit set, that limit applies regardless of group membership.

2. **Group limit**—if the member has no individual limit, the system checks their group memberships. If the member belongs to multiple groups with spend limits, your **Multi-group spend limit** setting determines whether the higher or lower limit applies.

3. **No limit**—if the member has no individual limit and belongs to no groups with spend limits, no spend limit is applied.