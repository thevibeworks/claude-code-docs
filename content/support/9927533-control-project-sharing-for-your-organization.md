# Control project sharing for your organization

This feature is available to Primary Owners and Owners on Team and Enterprise plans. On Enterprise plans, custom roles with the **Privacy** permission set to "Can manage" can also change these settings. Setting project sharing by role is available on Enterprise plans only.

Two settings in the **Sharing** section control how users share projects in your organization:

- **Share projects** controls whether users can share projects with others in your organization.

- **Public projects** controls whether all users in your organization can see and start chats in public projects. It's a sub-setting of Share projects.

Both are on by default.

## Turn off project sharing

1. Go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. In the **Sharing** section, find **Share projects** and toggle it off.

Turning off **Share projects** also turns off **Public projects**.

**When you turn off project sharing**

- Users can't share projects with new users or groups.

- Projects that are already shared stay shared, and users who already have access keep it.

- Existing public projects become private, and users can't create new public projects.

- Users can still open a project's “Share” menu, but they see "Project sharing is turned off by your administrator" and can't add new users or groups. They can still change or remove existing access.

**Note:** If you turn off project sharing, let your teams know. They keep their current projects but can't add new users, and public projects become private.

## Turn off public projects only

1. Go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. In the **Sharing** section, under **Share projects**, toggle **Public projects** off.

**When you turn off public projects:**

- All existing public projects become private.

- Users can't create new public projects.

- Users can't share a project with everyone in your organization.

- Users can still share projects with specific users and groups. Projects already shared keep their sharing settings.

## Set project sharing by role

On Enterprise plans, you can turn project sharing on or off for specific roles.

1. Go to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Open a role, or click "Add role."

3. On the "Capabilities" tab, toggle **Share projects** on or off.

4. Click "Save role."

**Share projects** must be on at the organization level before roles can control it. Role changes can take up to 15 minutes to apply. See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

## Turn project sharing back on

- Turn **Share projects** back on and users can share projects again.

- Projects that became private stay private.

- Turn **Public projects** on and users can create new public projects.

- Existing sharing settings and permissions don't change.

To learn how users share projects, see **[Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)**.