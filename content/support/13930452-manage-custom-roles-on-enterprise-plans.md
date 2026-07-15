# Manage custom roles on Enterprise plans

Custom roles are available for Enterprise plan organizations. Owners, Primary Owners, and custom roles with the **Identity & Access** permission set to "Can manage" can go to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)** to manage custom roles.

## What are custom roles?

Custom roles let you define which features your members can access. Each custom role contains a set of permissions that grant or restrict access to specific capabilities like chat, Claude Cowork, Claude Code, and web search, plus the connectors your organization has added, such as Slack or Google Drive. Custom roles can also grant admin permissions, which give members access to specific administrative areas like billing, identity, or privacy without making them Owners.

Custom roles work alongside groups. The typical workflow is: create custom roles, assign them to groups, and then set members' roles to “Custom” so their access is governed entirely by the custom roles assigned to their groups.

**Note:** Custom roles only affect members whose role is set to “Custom.” Members with the User, Admin, or Owner roles get their permissions from those roles directly, not from custom roles.

---

## How feature access works

Feature access is determined by a four-level precedence chain, where the most restrictive level wins:

1. **Platform-level overrides**: Some features may be force-enabled or force-disabled for your organization by Anthropic as part of your contract. These can't be changed in organization settings.

2. **Organization-level setting**: An Owner or Primary Owner can toggle a feature on or off for the entire organization. If a feature is disabled at the organization level, no custom role can grant access to it.

3. **Custom role permissions**: If the feature is enabled at the organization level, the member's custom roles determine whether they can access it. If any of the member's custom roles grant the feature, they have it.

4. **User-level setting**: If the feature is granted at the role level, it's available unless the member has disabled it in their own settings.

The key takeaway: the organization-level toggle is a main switch. Custom roles are the per-member switches underneath it. A feature must be enabled at the organization level before custom roles can control who gets access.

**Note:** This precedence chain applies to capabilities. Admin permissions aren't gated by an organization-level toggle or a member's own settings. If a member's custom role grants an admin permission, they have that access.

---

## Available capabilities

Each custom role can grant or restrict access to the following capabilities:

| **Capability**                          | **Description**                                                                                                                                                                                                                                          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chat                                    | Access to chat on web, desktop, and mobile apps.                                                                                                                                                                                                         |
| Code execution and file creation        | Ability to run code and create files in conversations.                                                                                                                                                                                                   |
| Memory                                  | Ability to use memory across conversations.                                                                                                                                                                                                              |
| Web search                              | Ability to use web search in conversations.                                                                                                                                                                                                              |
| Public projects                         | Ability to share projects with everyone in your organization.                                                                                                                                                                                            |
| Create skills                           | Ability to create or upload custom skills.                                                                                                                                                                                                               |
| Share skills with org members           | Ability to share skills with specific people in your organization.                                                                                                                                                                                       |
| Share skills with the full organization | Ability to share skills with everyone in your organization at once.                                                                                                                                                                                      |
| Claude Code                             | Access to Claude Code.                                                                                                                                                                                                                                   |
| Fast mode                               | Access to faster model options for Claude Code.                                                                                                                                                                                                          |
| Claude Code dynamic workflows\*         | Access to dynamic workflows in Claude Code, which let Claude run large engineering tasks—migrations, audits, codebase-wide bug hunts—from start to finish in a single session. These runs can last for hours and use more tokens than a typical session. |
| Claude Security                         | Find and fix security vulnerabilities in your code with Claude.                                                                                                                                                                                          |
| Claude Code artifacts                   | Ability to create artifacts in Claude Code, which turn a session's work into a live, shareable page built from the session's context.                                                                                                                    |
| Claude Design                           | Access to Claude Design to generate design artifacts.                                                                                                                                                                                                    |
| Claude Cowork                           | Access to Claude Cowork.                                                                                                                                                                                                                                 |
| Claude for Chrome                       | Access to Claude for Chrome, the browser extension that lets Claude browse and act on web pages on the user's behalf.                                                                                                                                    |

*Claude Code dynamic workflows are on for your whole organization by default. Because a single run can last for hours and use more tokens than a typical session, decide which roles should have access. For members on custom roles, this capability follows the additive model like any other—a role must grant it for those members to use it. To restrict a specific group, leave this capability off in their role.

This can be disabled organization-wide via `managed-settings.json` by adding `"disableWorkflows": true` to your managed settings.

An owner can turn it off across your entire organization by going to **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)** and toggling **Workflows** off.

Custom roles also govern admin permissions, connectors, and model access, which are configured on separate **Permissions**, **Connectors**, and **Models** tabs in the role editor. See **[Admin permissions](#h_fde60b08bd)**, **[Connector permissions](#h_979e558d00)**, and **[Model access](#h_fca0f9a6b5)** below.

**Note:** Chat is enabled by default for all custom roles, including ones created before this capability was added. If you want to restrict chat for a specific role, toggle it off when editing the role.

### Grant all capabilities at once

Instead of toggling capabilities individually, you can grant a role every capability. When creating or editing a role, choose an option on the **Capabilities** tab for **Capability access**:

- **All capabilities:** Grants the role every capability, including capabilities in beta and research preview.

- **All generally available:** Grants the role every generally available capability.

Roles set to either option pick up new capabilities automatically as they launch. Roles set to “Only selected” only include the capabilities you select.

---

## Create a custom role

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click “Add role.”

3. Enter a name for the role (for example, “Developer,” “Standard Access,” or “Restricted”).

4. Select the groups you want to assign to the role.

5. Toggle each capability on or off to define what this role grants, or choose "All capabilities" or "All generally available" to grant every capability at once.

6. Configure permissions. You can choose No access, Can view, and Can manage for each admin setting.

7. Configure connectors. You can choose Always allow, Needs approval, or Blocked for all connectors, or customize per connector or connector tool.

8. Configure models. Select which models this role can use, optionally set a maximum effort level per model, and optionally choose a default model for the role.

9. Click “Save role.”

## Edit a custom role

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to edit.

3. Update the name and groups, or toggle capabilities, permissions, connectors, and models as needed.

4. Click “Save role” to save your changes.

Role changes may take up to 15 minutes to take effect, and members may need to refresh their browser. All members in groups assigned to this role are affected.

## Delete a custom role

Click the menu button on any custom role and select “Delete role.” Deleting a role removes its permissions from all groups it was assigned to. Members in those groups lose the permissions the role granted, unless another role in their chain also grants them.

---

## Assign groups to custom roles

Custom roles are assigned to groups, not directly to individual members. To assign a group to a role:

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click the role you want to assign.

3. In the groups selector, select one or more groups.

4. Click "Save role."

You can also assign custom roles when creating or editing a group in **[Organization settings > Groups](http://claude.ai/admin-settings/groups)**. See **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

---

## How permissions combine across multiple roles

If a member belongs to multiple groups with different custom roles, their permissions are **additive**—they get the union of all permissions from all roles in their chain. If any role grants a feature, the member has access to it.

This means you can't use one role to remove a permission granted by another role. This is by design — it enables a layered approach where a base role covers common features and additional roles layer on specific capabilities and admin permissions.

**Example:** A member is in two groups. The "All Users" group is assigned a "Standard Access" role with web search and memory. The "Engineering" group is assigned a "Developer" role with Cowork and Claude Code. The member gets all four: web search, memory, Cowork, and Claude Code.

---

## See a member or group's effective role

When a member belongs to several groups whose roles grant different capabilities, it can be hard to tell what they can actually do. The "View effective role" option shows the combined result: every capability, admin permission, and connector the member has, with the role that grants each one.

1. Navigate to **[Organization settings > Members](https://claude.ai/admin-settings/members)** (or **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**).

2. Find the member or group and open the "⋮" menu on the right side of their row.

3. Select "View effective role."

The modal lists the member's assigned roles and three tabs:

- **Capabilities:** each capability with a "Granted by *[role name]*" label showing which role turned it on.

- **Permissions:** each admin permission area with its effective level (No access, Can view, or Can manage) and which role grants it.

- **Connectors:** each connector's effective permission level and which role grants it.

This view is read-only. To change what a member can do, edit the roles assigned to their groups.

**Note:** "View effective role" appears only for members whose role is set to "Custom" and who have at least one custom role assigned through a group. Members with a built-in role (User, Admin, Owner, or Primary Owner) get their permissions from that role directly, so there's nothing to compute.

---

## Admin permissions

Custom roles can grant admin permissions in addition to capabilities and connector permissions. Admin permissions give members access to specific administrative areas, like billing or privacy, without making them Owners. You can configure admin permissions in the **Permissions** tab of the role editor.

**Note:** Admin permissions only apply to members whose role is set to "Custom." Members with the User, Admin, Owner, or Primary Owner roles keep the access those roles grant.

### Admin permission levels

On the **Permissions** tab, you set each permission area to one of three levels:

- **No access:** The member doesn't see this area in their organization settings.

- **Can view:** View grants read-only access. The member sees the same pages and settings as someone who can manage that area, but every control is disabled or shown as read-only. Use this permission level for compliance reviewers, finance auditors, security teams, or anyone who needs to see the configuration without changing it.

- **Can manage:** Manage grants full read and write access to the area and includes view access.

Within an area, you grant all of View or all of Manage. You can't grant or restrict individual pages or settings.

### Available admin permissions

There are seven admin permission areas:

| **Area**             | **View**                                                                                                                                                         | **Manage**                                                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Identity & Access    | SSO and SAML configuration, verified domains, domain memberships, IP allowlist, session settings, group definitions, role definitions, and provisioning settings | Edit SSO, manage domains, edit the IP allowlist, edit session settings, create and edit groups and roles, and configure provisioning |
| Billing              | Plan details, seat counts, invoices, billing addresses, and usage spend                                                                                          | Change seats, update payment methods, edit billing addresses, and configure spend limits and extra usage                             |
| Analytics            | Usage analytics, Claude Code analytics, and feature adoption metrics                                                                                             | Not available                                                                                                                        |
| Privacy              | Data retention settings, export configuration, sharing settings, geolocation settings, US-only inference setting, and encryption-key status                      | Edit retention periods, run data exports, change sharing settings, and configure geolocation, US-only inference, and encryption      |
| User Management      | Not available                                                                                                                                                    | Invite members, change member roles, remove members, and manage pending invitations                                                  |
| Libraries            | Not available                                                                                                                                                    | Add, edit, and remove organization-shared skills, plugins, and connectors. Also includes directory management.                       |
| Directory management | Not available                                                                                                                                                    | Submit and manage directory listings, and view observability for listings your organization has published                            |

**Note:** A role with **Identity & Access** set to "Can manage" can create and edit groups and roles, including its own role definition. Members with this permission can expand their own access, so reserve it for trusted security and IT administrators.

### Available organization settings pages for each permission

| **Organization settings page**    | **Required permission**            | **Notes**                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Billing                           | Billing (View or Manage)           | Plan, seats, addresses, and invoices                                                                                                                                                                                                                                                                                                                                    |
| Usage                             | Billing (View or Manage)           | Spend limits, credits, and extra usage                                                                                                                                                                                                                                                                                                                                  |
| Members                           | User Management (Manage)           | No view-only mode                                                                                                                                                                                                                                                                                                                                                       |
| Groups                            | Identity & Access (View or Manage) |                                                                                                                                                                                                                                                                                                                                                                         |
| Roles                             | Identity & Access (View or Manage) |                                                                                                                                                                                                                                                                                                                                                                         |
| Models                            | Identity & Access (View or Manage) | Default model and model access                                                                                                                                                                                                                                                                                                                                          |
| Organization and access (partial) | Identity & Access (View or Manage) | Unlocks single sign-on (SSO/SAML, group mappings, provisioning), verified domains and domain memberships, IP allowlist, session settings, restrict organization creation, and organization merger requests. Other sections on this page, like the organization name, default capability settings, and the organization-wide system prompt, still require the Owner role |
| Data and privacy                  | Privacy (View or Manage)           |                                                                                                                                                                                                                                                                                                                                                                         |
| Analytics                         | Analytics (View)                   | Reached through Analytics in the user menu, not organization settings                                                                                                                                                                                                                                                                                                   |
| Skills                            | Libraries (Manage)                 |                                                                                                                                                                                                                                                                                                                                                                         |
| Plugins                           | Libraries (Manage)                 |                                                                                                                                                                                                                                                                                                                                                                         |
| Connectors                        | Libraries (Manage)                 |                                                                                                                                                                                                                                                                                                                                                                         |
| Directory                         | Directory management (Manage)      |                                                                                                                                                                                                                                                                                                                                                                         |

### What admin permissions don't cover

The following remain available only to Owners and Primary Owners, even for members with admin permissions:

- **Managing Owners and Admins.** Admin permissions can't grant or revoke the Owner, Admin, or Primary Owner built-in roles. Only Owners can manage other Owners.

- **API keys and workspaces.** API key management, workspace settings, and Claude Console administration aren't covered by admin permissions.

- **Compliance and security keys.** Compliance API settings and security-key administration remain Owner-only.

- **Organization-level capability settings.** Which capabilities are enabled at the organization level is governed separately and isn't part of admin permissions.

### What members see when admin permissions are restricted

If a member doesn’t have access to a specific admin permission, the section doesn't appear in their organization settings. Only sections their permissions cover are shown.

---

## Connector permissions

Custom roles also control which connectors, and which tools on those connectors, a role can use. Where capabilities cover Claude’s built-in features, connector permissions cover the apps and services you’ve connected to your organization, such as Slack, Google Drive, or Jira. You set them on the **Connectors** tab of the role editor, next to the **Capabilities** and **Permissions** tabs.

**Note:** Connector permissions apply only to members whose role is set to “Custom.” Members with the User, Admin, or Owner roles see every connector enabled for your organization, subject to your organization-wide tool policies per connector. Owners and Admins always see every connector so they can configure it, regardless of any role’s connector permissions.

### Permission levels

On the **Connectors** tab, you set all connectors, each connector, or each tool on a connector, to one of three levels:

- **Always allow:** Every tool on the connector is available, and members can set their own approval to “Always allow” to skip the per-call confirmation.

- **Needs approval:** Every tool is available, but members confirm each call. The “Always allow” option is removed from their personal approval menu for these tools.

- **Blocked:** The connector or tool is hidden. Claude can’t see it or call it.

A connector can also be set to **Custom**, which lets you set each of its tools individually. For the full setup, see **[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-)**.

### How connector access is determined

A connector or tool passes through several layers before a member can use it, evaluated in this order:

1. **Role grant.** Each connector or tool on a role is set to “Always allow,” “Needs approval,” or “Blocked.”

2. **Across the member’s roles.** If a member’s groups give them more than one role, the most permissive grant for each tool applies. Connector permissions are additive across roles, the same as capabilities.

3. **Organization-wide tool policy.** The per-tool policy you set under **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** per connector is the ceiling. For each tool, Claude compares the member’s role grant to this policy and applies the stricter of the two. Role grants narrow access within the policy; they can’t widen past it. Learn more about setting tool access in **[Use connectors to extend Claude’s capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**.

4. **The member’s own setting.** The result of the steps above is the member’s effective ceiling. It limits the options in their personal per-tool approval menu (“Always allow,” “Ask,” or “Never”). A ceiling of “Needs approval” removes “Always allow.” A ceiling of “Blocked” grays the tool out.

For members using Claude Code, one more layer applies: Managed Settings policies and connector permissions compose by most-restrictive. A tool is callable without a prompt only when both allow it. For more information, see **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.

For members using Claude Cowork, write-capable connector tools pass through one more gate. See **[Cowork approval setting for write tools](#h_85bd7c30e9)** below.

This table shows how the organization-wide tool policy and a member’s role grant combine:

| **Organization-wide tool policy** | **Highest role grant across the member’s roles** | **Effective ceiling** | **Member’s personal options** |
| --------------------------------- | ------------------------------------------------ | --------------------- | ----------------------------- |
| Always allow                      | Always allow                                     | Always allow          | Always allow, Ask, Never      |
| Always allow                      | Needs approval                                   | Needs approval        | Ask, Never                    |
| Always allow                      | Blocked                                          | Blocked               | Tool grayed out               |
| Needs approval                    | Always allow                                     | Needs approval        | Ask, Never                    |
| Needs approval                    | Blocked                                          | Blocked               | Tool grayed out               |
| Blocked                           | Any                                              | Blocked               | Tool grayed out               |

### Cowork approval setting for write tools

Claude Cowork has a separate organization setting, **Allow "Always allow" for connector tools**, that gates write-capable connector tools. It's off by default, and custom role grants can't override it: even when the organization-wide tool policy and every role grant are set to "Always allow," members approve these tools per task in Cowork until the setting is turned on. Learn more about **[connector tool approvals in Cowork](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans#h_1bd1fa754d)**.

### Where connector permissions apply

Connector permissions are enforced on Anthropic’s servers, so they apply across every Claude surface that routes connector traffic through Anthropic:

| **Surface**                       | **Coverage**                                                                                                                                                                                                  |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude on web and desktop         | Full enforcement. Blocked connectors are hidden, blocked tools are grayed out, and the personal approval menu is limited to what the ceiling allows.                                                          |
| Claude Mobile (iOS and Android)   | Enforced. Blocked tools are stripped from Claude’s view and calls to them are rejected. A blocked tool may still look active in mobile connector settings until interface updates ship, but it can’t be used. |
| Claude Cowork (cloud and desktop) | Same as web.                                                                                                                                                                                                  |
| Claude Code                       | Enforced. Blocked tools are rejected and appear as disabled. See **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.                                                         |

Connector permissions govern connectors your organization has added under **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. They don’t govern connectors a member runs locally on their own machine, and they don’t govern Claude Cowork when it’s deployed on a third-party platform. For third-party Cowork deployments, use MDM instead. See **[Cowork on 3P: MCP, plugins, skills, and hooks](https://claude.com/docs/cowork/3p/extensions).**

### What members see when a connector is restricted

| **Restriction**                                                      | **What the member sees**                                                                                                                                              |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A connector is blocked for their role                                | The connector doesn’t appear in their connector menu.                                                                                                                 |
| A tool is blocked on a visible connector                             | The tool is grayed out in their connector settings, with the message “This tool is not enabled for your role. Contact your administrator.”                            |
| A tool is capped at “Needs approval”                                 | The tool works, but the personal approval menu offers only “Ask” and “Never,” and Claude asks before each call.                                                       |
| The Cowork “Allow “Always allow” for connector tools” setting is off | In Cowork, write-capable tools work, but "Allow for all tasks" is grayed out and members approve each task.                                                           |
| Connector permissions can’t load briefly                             | A banner reports that connectors couldn’t load, with a retry. No blocked tool ever reaches the connected service. Access fails toward denying, never toward granting. |

Members can’t tell which layer restricted a tool. The message is the same whether the limit comes from the organization-wide tool policy, a role grant, or both. To find the source, compare the organization-wide policy with the member’s role grants.

---

## Model access

Custom roles also control which Claude models a role can use and the maximum effort level members can select on each one. You set these on the **Models** tab of the role editor, alongside the role's default model.

The organization-level model setting is the ceiling. A role can't grant a model that's disabled at the organization level. Across a member's roles, model access is additive and effort limits take the highest cap any role allows. Haiku models are always available and can't be disabled.

For setup steps and what members see, see **[Manage model access for your organization](https://support.claude.com/en/articles/15694740)**. For default model behavior, see **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

---

## What members see when capability access is restricted

When a capability is restricted, here’s what members see. For connector and tool restrictions, see **[Connector permissions](#h_979e558d00)** above.

| **Reason**                                    | **What the member sees**                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Feature is disabled at the organization level | The feature appears greyed out or hidden, with the message "This feature is disabled for your organization."       |
| Member's roles don't grant the feature        | The feature appears greyed out or hidden, with the message "Contact your admin to request access to this feature." |
| Member's roles don't grant any product access | The member lands on their settings page when they sign in, with no products available to use.                      |