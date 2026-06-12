Title: Manage custom roles on Enterprise plans

URL Source: https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Team and Enterprise plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)
3.   [Admin management](https://support.claude.com/en/collections/9811449-admin-management)
4.   Manage custom roles on Enterprise plans

Updated this week

## What are custom roles?

Custom roles let you define which features your members can access. Each custom role contains a set of permissions that grant or restrict access to specific capabilities like chat, Claude Cowork, Claude Code, and web search, plus the connectors your organization has added, such as Slack or Google Drive. Custom roles can also grant admin permissions, which give members access to specific administrative areas like billing, identity, or privacy without making them Owners.

Custom roles work alongside groups. The typical workflow is: create custom roles, assign them to groups, and then set members' roles to “Custom roles” so their access is governed entirely by the custom roles assigned to their groups.

## How feature access works

Feature access is determined by a four-level precedence chain, where the most restrictive level wins:

The key takeaway: the organization-level toggle is a main switch. Custom roles are the per-member switches underneath it. A feature must be enabled at the organization level before custom roles can control who gets access.

## Available capabilities

Each custom role can grant or restrict access to the following capabilities:

**Capability****Description**
Chat Access to chat on web, desktop, and mobile apps.
Code execution and file creation Ability to run code and create files in conversations.
Memory Ability to use memory across conversations.
Web search Ability to use web search in conversations.
Public projects Ability to share projects with everyone in your organization.
Create skills Ability to create or upload custom skills.
Share skills with team members Ability to share skills with specific people in your organization.
Share skills with the full organization Ability to share skills with everyone in your organization at once.
Claude Code Access to Claude Code.
Fast mode Access to faster model options for Claude Code.
Claude Code dynamic workflows*Access to dynamic workflows in Claude Code, which let Claude run large engineering tasks—migrations, audits, codebase-wide bug hunts—from start to finish in a single session. These runs can last for hours and use more tokens than a typical session.
Claude Security Find and fix security vulnerabilities in your code with Claude.
Claude Design Access to Claude Design to generate design artifacts.
Claude Cowork Access to Claude Cowork.
Claude for Chrome Access to Claude for Chrome, the browser extension that lets Claude browse and act on web pages on the user's behalf.

Custom roles also govern access to admin permissions and connectors, which are configured on separate **Permissions** and **Connectors** tabs in the role editor. See **[Admin permissions](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_fde60b08bd)** and **[Connector permissions](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_979e558d00)** below.

## Create a custom role

## Edit a custom role

Capability and connector changes take effect within one minute. Admin permission changes can take up to 15 minutes, and members may need to refresh their browser. All members in groups assigned to this role are affected.

## Delete a custom role

Click the menu button on any custom role and select “Delete role.” Deleting a role removes its permissions from all groups it was assigned to. Members in those groups lose the permissions the role granted, unless another role in their chain also grants them.

## Assign groups to custom roles

Custom roles are assigned to groups, not directly to individual members. To assign a group to a role:

## How permissions combine across multiple roles

If a member belongs to multiple groups with different custom roles, their permissions are **additive**—they get the union of all permissions from all roles in their chain. If any role grants a feature, the member has access to it.

This means you can't use one role to remove a permission granted by another role. This is by design — it enables a layered approach where a base role covers common features and additional roles layer on specific capabilities and admin permissions.

**Example:** A member is in two groups. The "All Users" group is assigned a "Standard Access" role with web search and memory. The "Engineering" group is assigned a "Developer" role with Cowork and Claude Code. The member gets all four: web search, memory, Cowork, and Claude Code.

## Admin permissions

Custom roles can grant admin permissions in addition to capabilities and connector permissions. Admin permissions give members access to specific administrative areas, like billing or privacy, without making them Owners. You can configure admin permissions in the **Permissions** tab of the role editor.

### **Admin permission levels**

On the **Permissions** tab, you set each permission area to one of three levels:

Within an area, you grant all of View or all of Manage. You can't grant or restrict individual pages or settings.

### **Available admin permissions**

There are seven admin permission areas:

**Area****View****Manage**
Identity & Access SSO and SAML configuration, verified domains, domain memberships, IP allowlist, session settings, group definitions, role definitions, and provisioning settings Edit SSO, manage domains, edit the IP allowlist, edit session settings, create and edit groups and roles, and configure provisioning
Billing Plan details, seat counts, invoices, billing addresses, and usage spend Change seats, update payment methods, edit billing addresses, and configure spend limits and extra usage
Analytics Usage analytics, Claude Code analytics, and feature adoption metrics Not available
Privacy Data retention settings, export configuration, sharing settings, geolocation settings, and encryption-key status Edit retention periods, run data exports, change sharing settings, and configure geolocation and encryption
User Management Not available Invite members, change member roles, remove members, and manage pending invitations
Libraries Not available Add, edit, and remove organization-shared skills, plugins, and connectors. Also includes directory management.
Directory management Not available Submit and manage directory listings, and view observability for listings your organization has published

### **Available organization settings pages for each permission**

**Organization settings page****Required permission****Notes**
Billing Billing (View or Manage)Plan, seats, addresses, and invoices
Usage Billing (View or Manage)Spend limits, credits, and extra usage
Members User Management (Manage)No view-only mode
Groups Identity & Access (View or Manage)
Roles Identity & Access (View or Manage)
Organization and access (partial)Identity & Access (View or Manage)Unlocks single sign-on (SSO/SAML, group mappings, provisioning), verified domains and domain memberships, IP allowlist, session settings, restrict organization creation, and organization merger requests. Other sections on this page, like the organization name, default capability settings, and the organization-wide system prompt, still require the Owner role
Data and privacy Privacy (View or Manage)
Analytics Analytics (View)Reached through Analytics in the user menu, not organization settings
Skills Libraries (Manage)
Plugins Libraries (Manage)
Connectors Libraries (Manage)
Directory Directory management (Manage)

### What admin permissions don't cover

The following remain available only to Owners and Primary Owners, even for members with admin permissions:

### What members see when admin permissions are restricted

If a member doesn’t have access to a specific admin permission, the section doesn't appear in their organization settings. Only sections their permissions cover are shown.

## Connector permissions

Custom roles also control which connectors, and which tools on those connectors, a role can use. Where capabilities cover Claude’s built-in features, connector permissions cover the apps and services you’ve connected to your organization, such as Slack, Google Drive, or Jira. You set them on the **Connectors** tab of the role editor, next to the **Capabilities** and **Permissions** tabs.

### Permission levels

On the **Connectors** tab, you set all connectors, each connector, or each tool on a connector, to one of three levels:

### How connector access is determined

A connector or tool passes through several layers before a member can use it, evaluated in this order:

For members using Claude Code, one more layer applies: Managed Settings policies and connector permissions compose by most-restrictive. A tool is callable without a prompt only when both allow it. For more information, see **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.

This table shows how the organization-wide tool policy and a member’s role grant combine:

**Organization-wide tool policy****Highest role grant across the member’s roles****Effective ceiling****Member’s personal options**
Always allow Always allow Always allow Always allow, Ask, Never
Always allow Needs approval Needs approval Ask, Never
Always allow Blocked Blocked Tool grayed out
Needs approval Always allow Needs approval Ask, Never
Needs approval Blocked Blocked Tool grayed out
Blocked Any Blocked Tool grayed out

### Where connector permissions apply

Connector permissions are enforced on Anthropic’s servers, so they apply across every Claude surface that routes connector traffic through Anthropic:

Connector permissions govern connectors your organization has added under **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. They don’t govern connectors a member runs locally on their own machine, and they don’t govern Claude Cowork when it’s deployed on a third-party platform. For third-party Cowork deployments, use MDM instead. See **[Cowork on 3P: MCP, plugins, skills, and hooks](https://claude.com/docs/cowork/3p/extensions).**

### What members see when a connector is restricted

Members can’t tell which layer restricted a tool. The message is the same whether the limit comes from the organization-wide tool policy, a role grant, or both. To find the source, compare the organization-wide policy with the member’s role grants.

## What members see when capability access is restricted

When a capability is restricted, here’s what members see. For connector and tool restrictions, see **Connector permissions** above.

* * *

Related Articles

[Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)[Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
