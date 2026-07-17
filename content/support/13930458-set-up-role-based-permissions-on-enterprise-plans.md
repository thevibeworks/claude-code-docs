# Set up role-based permissions on Enterprise plans

This guide walks you through setting up role-based permissions for your Enterprise organization. This lets you control which features and connectors specific teams or groups of members can access, and delegate specific admin access like billing or user management, rather than giving everyone the same permissions.

Before you start, make sure you're familiar with:

- **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)** — how to create and manage groups

- **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)** — how custom roles and capabilities work

---

## Before you begin

You'll need Owner or Primary Owner access to your Enterprise organization, or a custom role with Identity & Access set to Manage.

**Note:** Some of these steps require more than the Identity & Access custom role: enabling features at the organization level requires the Owner role, and changing member roles requires User Management set to Manage.

**Check which capabilities are enabled at the org level.** Go to **Organization settings** and ensure you know which capabilities members can access currently. For settings managed by RBAC, both the org setting and role setting are required to be on for users to get access.

**Back up your member list.** Export a CSV of your current members from **[Organization settings > Members](http://claude.ai/admin-settings/members)** before making any changes. If something goes wrong during migration, this gives you a reference to restore access. See **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)**.

**Determine which teams or functions need each capability.** For example, Engineering gets Claude Code + Fast Mode and Marketing gets Cowork + Web Search. From here, define your custom roles.

**Dual-seat plans.** If your organization is on a dual-seat Enterprise plan (with Chat and Chat + Claude Code seats), custom roles don't override seat-level restrictions. A member assigned to a Chat-only seat can't access Claude Code even if their custom role grants it. The same applies in reverse: if a member's custom role doesn't grant the chat capability, they won't have chat access regardless of their seat type. Plan your role structure with seat assignments in mind.

**Note:** "Chat + Claude Code" refers to a seat type on legacy dual-seat plans. The "chat" capability in custom roles is separate—it governs chat access for any member whose role is set to "Custom" on any plan.

**Decide how you'll create groups.** You can create groups manually in Claude, or sync them from your identity provider (IdP) via SCIM. You can also use both methods simultaneously. If you plan to use IdP groups from Okta, Entra ID, or another provider, make sure SCIM directory sync is configured. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

**Add the connectors you plan to govern.** Connector permissions only cover connectors that an Owner or Primary Owner has already added under **Organization settings > Connectors** and connected with admin credentials. Review your organization-wide tool policy there as well, since role grants narrow within it and can’t widen past it. See **[Use connectors to extend Claude’s capabilities](https://support.claude.com/en/articles/11176164-)**.

---

## Planning your role structure

Before creating anything, decide which features each team or group of members should have access to. Here are four common patterns:

### Base plus additive roles

This is the recommended approach for most organizations. Create a "Standard Access" role for everyone with common features like web search, memory, and projects. Then create additive roles that grant specific capabilities — for example, a "Cowork Enabled" role that only adds Cowork. Assign all members to the base role through an "All Users" group, and add specific members to additional groups that layer on extra features.

This pattern is flexible because permissions are additive — combining a base role with additive roles composes cleanly without conflicts.

### Tier-based roles

Create distinct tiers: "Full Access" with all features, "Standard Access" with most features, and "Restricted Access" with minimal features. Each member goes into exactly one group assigned to one tier.

### Department-based roles

Create roles that map to departments: "Engineering" with chat, Cowork, Claude Code, and code execution; "Research" with chat, web search, memory, and projects; "Business" with chat, web search and projects only. Assign each department group to its corresponding role.

### Admin delegation roles

Create roles that delegate parts of administration without granting the Owner role. A custom role with admin permissions does not need any user capabilities, and vice versa. You could create a "Finance" role that grants Billing access but no chat or Claude Code capability, or an "Engineering Lead" role that grants Claude Code plus Analytics view access. Learn more **[about admin permissions for custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_536123d968)**.

---

## Step 1: Audit your current settings

1. Review which features are currently enabled or disabled at the organization level in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)**.

2. Go to **[Organization settings > Members](http://claude.ai/admin-settings/members)** to export or review your member list.

3. Note each member's current built-in role (User, Admin, or Owner).

4. For each team or department, decide which features they need access to.

![Image of the Organization settings page in Claude, with a box around the People section which contains three options: Members, Groups, and Roles.](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484535492/d17b343f54f754bb3af73fe880a9/Org+settings+-+People.png?expires=1784262600&amp;signature=1cb30ffd258257e9629e7ec7c6d1ee3b5dee71ee9ec96a4b5062b270422a5fae&amp;req=diQvEsx9mIVWW%2FMW1HO4zVA%2FMt6SKY%2BsvDbmWeIt%2FcSOnX%2FEHqKEJaJGPpXj%0Aqppq4LElrLGxSExNmgo%3D%0A)

Remember: any feature you want to control per-group must be **enabled** at the organization level. If a feature is toggled off at the organization level, no custom role can grant access to it.

**Important:** Unlike members with the User role, members assigned to custom roles don't automatically inherit organization-enabled capabilities. Every capability a "Custom" role member needs must be explicitly granted by a custom role assigned to one of their groups.

---

## Step 2: Create custom roles

Create your custom roles before enabling any features or migrating members. This ensures your roles are ready to enforce access the moment features turn on.

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Click "Add  role."

3. Name the role and toggle the appropriate capabilities on the **Capabilities** tab, or choose "All capabilities" or "All generally available" to grant everything at once:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2539844315/2e98adc9b24a95bf64b7ef759c94/a0c6bd31-327c-48b8-9ece-1b985eafccec?expires=1784262600&amp;signature=108c99184aa459712f00facc1c633b2cc884680301163377a20d40a4e328323e&amp;req=diUkH8F6mYJeXPMW1HO4zfzK2OfY4Ns8Jsssa0E%2FK2YNWwRC3HLwqoOHcXPK%0AY6P5%0A)

4. On the **Permissions** tab, set admin permissions for the role. See **Step 3**.

5. On the **Connectors** tab, set connector permissions for the role. See **Step 4**.

6. On the **Models** tab, set model access and a default model for the role. See **Step 5**.

7. Click "Save role."

8. Repeat for each role in your plan.

Role changes may take up to 15 minutes to take effect. Members may need to refresh their browser to see updated access.

See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)** for details on available capabilities, admin permissions, and connectors.

---

## Step 3: Configure admin permissions (optional)

Set admin permissions on each role to delegate access to admin settings, like billing, user management, or privacy, without granting the Owner role. This step is optional. If you don't configure it, roles grant no admin access and administration stays with Owners and Primary Owners. For what each permission area covers, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

### Locate the Permissions tab

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Open an existing role, or click “Add role” to create one.

3. Select the **Permissions** tab, between **Capabilities** and **Connectors**.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484538453/66f52673b2d1fc7b0d4b48ed4ff6/fbf992ce-c4a1-402e-80cd-0c8449f916bd?expires=1784262600&amp;signature=c7d7b8567bfbf98c410b7f78c25be7a176837e569991d799e69733a156c052d1&amp;req=diQvEsx9lYVaWvMW1HO4za6MibalWkCBJQR8u%2B9qQFncXbsMGmA2ZchFsmxR%0A7W75%2BSUggfY9vpcnpm4%3D%0A)

### **Set admin permissions**

The **Permissions** tab lists each admin area: Identity & Access, Billing, Analytics, Privacy, User Management, and Libraries. Set each admin area to one of the following options:

- **No access:** The member doesn't see this area in their organization settings.

- **Can view:** View grants read-only access. The member sees the same pages and settings as someone who can manage that area, but every control is disabled or shown as read-only. Use this permission level for compliance reviewers, finance auditors, security teams, or anyone who needs to see the configuration without changing it.

- **Can manage:** Manage grants full read and write access to the area and includes view access.

Within an area, you grant all of View or all of Manage. You can't grant or restrict individual pages or settings.

**Note:** A role with Identity & Access set to Manage can create and edit groups and roles, including its own role definition. Members with this permission can expand their own access, so reserve it for trusted security and IT administrators.

### **Verify enforcement**

Verify admin permissions after you’ve migrated members to "Custom" roles (Step 7). See **Step 11: Verify and monitor**.

---

## Step 4: Configure connector permissions (optional)

Set connector permissions on each role to control which connectors, and which tools on those connectors, the role can use. This step is optional. If you don’t configure it, your roles fall back to the default behavior described below. For how the permission model works end to end, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

**Important:** When Anthropic enables connector permissions for your organization, every existing custom role is seeded with the “All connectors” grant at “Always allow.” Because “Always allow” is the most permissive grant, your organization-wide tool policy alone determines each member’s effective ceiling at enablement. Members neither gain nor lose access at enablement. Your first configuration pass narrows from that baseline.

**Note:** A newly created role defaults to “Needs approval” on every connector. The create-role flow steps through the Connectors tab so you see this default before saving. Raise a connector to “Always allow” or lower it to “Blocked” as needed.

### Locate the Connectors tab

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Open an existing role, or click “Add role” to create one.

3. Select the **Connectors** tab, next to **Permissions**.

The default settings for new roles are permissive. When creating or modifying a role, confirm the settings on each tab to avoid granting unintended permissions.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484539079/2325428311fffccd6951d5f2dc46/e4326a16-d44b-4e5d-9ecd-5c3dbbc7651a?expires=1784262600&amp;signature=e8704e73ea714875127d41bc964b1a2f1826b5705c1dc52aa7f0f35750f5868e&amp;req=diQvEsx9lIFYUPMW1HO4zZGDXF2hDvR0HNJQDqL6ZaAphRVaTJoIJdtY4Fom%0AtMxszRirTN26naPIBvk%3D%0A)

### Set connector-level permissions

The **Connectors** tab lists an **All connectors** row at the top, followed by every connector your organization has added. Each row has a dropdown with four options:

- **Always allow:** Every tool on the connector is available, and members can set their own approval to “Always allow.”

- **Needs approval:** Every tool is available, but members confirm each call.

- **Blocked:** The connector is hidden from members with this role.

- **Custom:** Set each tool on the connector individually. See “Set per-tool permissions” below.

Choosing “Always allow,” “Needs approval,” or “Blocked” applies that level to every tool on the connector. The **All connectors** row works the same way one level up: it sets a baseline for every connector at once, including any connector you add later. Use it to set a role’s default, then override individual connectors.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484540660/36fd30e963d7881bbff5b85bdf32/cc91e30c-af8c-4271-bff4-b34393d6122e?expires=1784262600&amp;signature=4184042da7fdb0d441a83c31db944d3cd0cc266af7ada489a9a897584c8b40b1&amp;req=diQvEsx6nYdZWfMW1HO4za3dLAKF2oQu%2B48W%2BGCIbmflcIGkTpCtqA58%2FCXv%0AA3NAkmHwVXXuCsfO36Y%3D%0A)

### Set per-tool permissions

Set a connector to **Custom** to reveal its tools as individual rows. Each tool has its own dropdown: “Always allow,” “Needs approval,” or “Blocked.”

Per-tool permissions let a role reach part of a connector. For example, with Jira set to **Custom**, its `search_issues` tool set to “Needs approval,” and every other Jira tool set to “Blocked,” members with the role can search Jira but nothing else. Claude only sees the tools you’ve granted, so asking it to create a ticket returns “I don’t have a tool for that” rather than an error.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484553274/3c0781dc9c7704a7b67d4858b88b/Screenshot+2026-06-17+at+4_28_45%E2%80%AFPM.png?expires=1784262600&amp;signature=e4d54ad21cdc57c7960a9df50cb5b826a1657c2575cc4245264f3a18177d4d43&amp;req=diQvEsx7noNYXfMW1HO4zXcI%2BoNCAt1l1VjQ9K3ENRsCefkOboWg4IEo2V9H%0AbEudLHqML9iRbvL7S6A%3D%0A)

### Review cross-role conflicts

Because connector permissions are additive across roles, blocking a connector in one role has no effect on a member who also holds another role that grants it. Each connector row shows a warning when other roles grant the same connector at a different level. The warning names those roles and links to them, and the most permissive grant is the one that applies.

If you have unsaved edits when you open a linked role, you’re asked to discard them first.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484556183/b644bbfba5350ae2a460117f23e3/Screenshot+2026-06-17+at+4_31_03%E2%80%AFPM.png?expires=1784262600&amp;signature=333f8dae236eae3b2f1805df9f77a72df7df321a09002c8bd506e6d3ddda114f&amp;req=diQvEsx7m4BXWvMW1HO4zX8ytukH59bRGc8KkqwXsZ7BEO7vXLWhSOJCdGwH%0A6UWFfRDHrT2%2FC7MYxBA%3D%0A)

### Verify enforcement

Verify connector permissions after you’ve migrated members to "Custom" roles (Step 7). See **Step 11: Verify and monitor**.

**Important:** If your organization uses Claude Code, enabling connector permissions also applies your organization-wide tool policy to Claude Code. This can only narrow tool access there, never widen it, and it affects all members. Review your organization-wide tool policy before enablement if Claude Code is widely deployed. Connector permissions and Claude Code Managed Settings compose by most-restrictive. See **[Claude Code settings](https://code.claude.com/docs/en/settings#settings-files)**.

**Note:** Whether members can set "Always allow" on write-capable connector tools in Cowork is additionally controlled by the organization setting **Allow "Always allow" for connector tools**, which is off by default. Role grants can't override it. Learn more about the **[Cowork approval setting for write tools](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans#h_1bd1fa754d)**.

---

## Step 5: Configure model access (optional)

Set model access on each role to control which Claude models the role can use, cap the maximum effort level per model, and choose the model new conversations start on. This step is optional; if you don't configure it, new roles can use every model that's enabled at the organization level, at any effort level, and start on the organization default model.

For how the model access and default model settings work end to end, see **[Manage model access for your organization](https://support.claude.com/en/articles/15694740)** and **[Set a default model for your organization](https://support.claude.com/en/articles/15330088)**.

### Locate the Models tab

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)**.

2. Open an existing role, or click "Add role" to create one.

3. Select the **Models** tab, next to **Connectors**.

### Set model access

Under **Model access**, switch each model on or off for this role. Models disabled at the organization level appear but can't be enabled here until you turn them on for the organization in **[Organization settings > Models](http://claude.ai/admin-settings/models)**. Haiku models are always on and can't be disabled.

To cap the effort level a role can select on a model, click the gear icon next to the model and choose a level.

Under **Default model**, optionally select the model new conversations start on for this role. Only models the role has access to can be selected.

### Verify enforcement

Verify model access after you've migrated members to "Custom" roles. See **Step 11: Verify and monitor**.

---

## Step 6: Create groups and assign roles

1. Navigate to **[Organization settings > Groups](http://claude.ai/admin-settings/groups)**.

2. Click “Add group” to create a group for each team or tier in your plan.

3. Add members to the appropriate groups.

4. Assign each group to the custom roles you created in step 2.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260371973/b503c99ef71d8a89b7aff606511b/b1afd593-3b23-4fa9-8b9b-ee6beaf74fd7?expires=1784262600&amp;signature=42f045e238e902101eba0b01b3074b6596414a0ec995dc326b2b8f99c1e3d0be&amp;req=diIhFsp5nIhYWvMW1HO4zdMu8WR0HAtsKwlCydrbfL5q6zH2QxYamyrznKwv%0Ai%2F6H7BeRWRaS%2B6HyxMw%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260372813/83ccc4784bdfc8600101bc42ec4b/6e7456ac-9887-4e04-b757-3972110fbdce?expires=1784262600&amp;signature=a34c7528104a22fc93dede997b4ff57a73a589534bc59427b9d7973dd4bdbf5e&amp;req=diIhFsp5n4leWvMW1HO4zQetnydVYq3%2BczQdKdGFNsdJN2aOQZc0ZKRvNo%2BQ%0A1sz17y%2BwDfoZpFHrS8s%3D%0A)

If you use SCIM directory sync, you can sync groups from your identity provider instead of creating them manually. For details on SCIM group sync, see **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260374677/5f9d8febb8ae25153a94d0b827b9/c8314b27-96c1-4743-ae8b-25e511181837?expires=1784262600&amp;signature=241bd62c6c754b704aeb572baffd90aab1fe29274a1ba4c31bc2cca423bd1f61&amp;req=diIhFsp5mYdYXvMW1HO4zXzl64t37jmcKYkQn0Dd8NWeA%2B40tlDvU7LCecvW%0AmMbgSdq%2BThDJeF%2BOAMY%3D%0A)

**Multiple organizations under the same parent organization:** Groups are managed at the parent organization level and propagate to all child organizations. You may see members from other organizations listed in a group—this doesn't mean they have access to your organization. Custom roles assigned to a group only grant capabilities to members who are part of your specific organization.

If you request to move an organization from one parent to another (this is rare in practice), groups and roles will become undefined and you will need to re-create them.

**Important:** If your organization uses Invite only or JIT provisioning, you can only use manually created groups for RBAC. SCIM-synced groups aren't supported in these modes.

---

## Step 7: Verify group and role assignments

Before migrating members to custom roles, confirm that every member you plan to migrate is in at least one group assigned to a custom role. Members who are migrated without group or role coverage will lose access to all governed features.

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)**.

2. Use the Role and Group filters to identify members who aren't assigned to any group.

3. Alternatively, click "Export CSV" to download the full member list with role and group columns for review.

4. Add any unassigned members to the appropriate groups before continuing.

---

## Step 8: Migrate members to custom roles

For custom role capabilities to take effect, members must have their role set to "Custom." Members with the User, Admin, or Owner roles get their permissions from those roles directly, not from custom roles.

**Important:** Complete this step only after you’ve created your custom roles, configured admin and connector permissions if you’re using them, created your groups, and verified all members are assigned to groups. Members moved to custom roles before setup is complete will immediately lose access to all governed features and their previous role. Switching an Owner or Admin to custom roles removes their Owner or Admin access, so don't migrate Owners or Admins unless you intend to replace that access with custom role permissions.

Choose the migration path based on whether your organization already enabled group mappings:

### Path A: Enable group mappings (only if already in use)

Use this path only if your organization already enabled group mappings for role assignment. If you aren't already using this setting, skip to Path B.

1. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.

2. In the role mappings section, assign the IdP groups you want governed by custom roles to the "Custom" role.

3. Save your changes. Members in those IdP groups are migrated to "Custom" roles on the next sync.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2434934020/d154818947d8d84ebf1aec8d5462/image.png?expires=1784262600&amp;signature=35242b4bc2ca3401430f836caffc6581122dc040f4dd8c2d347d6a5776256104&amp;req=diQkEsB9mYFdWfMW1HO4zQyCmEvhT0duSnpHYy0fFQvRnNo98nxgkgsVJ5KW%0Aj%2BsR2fJC6nKNNYVeP%2BA%3D%0A)

Members in IdP groups mapped to "Custom" roles follow the permissions of the custom roles assigned to their groups in Claude. Members in IdP groups mapped to User follow the organization-level capability settings. If a member is in groups across both mappings, "Custom" roles take precedence.

### Path B: Bulk assignment tool

Use this path if your organization hasn’t enabled group mappings.

**Warning:** If you didn’t already enable group mappings, do not enable it during RBAC setup. Enabling it without first assigning all members to mapped groups can result in members losing access to your organization.

1. Navigate to **[Organization settings > Members](http://claude.ai/admin-settings/members)**.

2. Use the Role and Group filters to select the members you want to migrate.

3. Use the bulk assignment tool in the Members table to change the selected members' role to "Custom."

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260377969/ba3b7ba08518f0a50e2a84f82655/bdf1aea3-2fe7-4f3c-868b-cc35ae8b7d1d?expires=1784262600&amp;signature=a9a68c321481417083f668fe51b6b9c464cc0f9a43c075e7c2212f7c8983ccc6&amp;req=diIhFsp5mohZUPMW1HO4zYFuwIUgg8uKlPaXg%2F0URIk1BpLmzFMNFSpM%2B%2BDA%0ANR919LZtOppY7bVgDl0%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260378309/abe25b6478c721a2f965b35361b7/beff124a-0a44-4f7f-97f8-391ce6e8c55b?expires=1784262600&amp;signature=c26455a93c474dc8131a6cbcbdd44092fd46ac6d6b8661de4b889c7f1d8c445f&amp;req=diIhFsp5lYJfUPMW1HO4zRgyEFzeVevQZ8KPhClFzQnD6jauFNjFRNlivEku%0A8cr7mhmnMW5qePMBTX4%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2484560173/7abf3438fa3d65afa03c4a99d4d4/Screenshot+2026-06-17+at+4_34_49%E2%80%AFPM.png?expires=1784262600&amp;signature=fb886937e32c6aa900a84d50f5a884f6fa3674b03b0533d712cb5c2baeb27afa&amp;req=diQvEsx4nYBYWvMW1HO4zUXuwkp%2BLYFWiQnXWL6R1K8UUkbgCgylgXVqAUJh%0ADlQaSWFfzX%2F%2BGd0NqWo%3D%0A)

We recommend migrating a pilot group first—one team or department—and verifying their access is correct before expanding to the rest of the organization.

### Gradual rollout

Whichever path you use, we recommend migrating in stages:

1. Start with a pilot group of one team or department.

2. After migration, verify the pilot group has the correct feature access based on their group and role assignments.

3. If something isn't right, switch the affected members back to their previous role while you adjust.

4. Expand to more members once you've confirmed the setup works.

---

## Step 9: Enable features at the organization level

Only enable organization-level features after roles, groups, and member migration are complete. This ensures custom role capabilities are already in place, with no window where unauthorized members could access a feature.

For any feature you want to control per-group:

1. Navigate to the feature's settings page in **Organization settings** (for example, **[Organization settings > Cowork](http://claude.ai/admin-settings/cowork)**).

2. Enable the feature at the organization level.

Enabling a feature at the organization level doesn't mean everyone gets it—custom role permissions are already in place to control who can use it. Think of the organization-level toggle as making the feature "available for role-based assignment" rather than "on for everyone."

---

## Step 10: Apply a group spend limit (usage-based orgs only)

Navigate to the “Usage” page to assign a per-user monthly spend limit to any group.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386576/377ac052069ff5a35b3023f50d12/dface609-9d85-4ee1-8ed3-bfe019a2bd0a?expires=1784262600&amp;signature=4a8ebb79f8bf3ef1e8d930ed12403b67d127ecf7a3c13c9bbcb865cc229fc9d5&amp;req=diIhFsp2m4RYX%2FMW1HO4zfvdi5OdQwSMBMkPcsY1DF5H3YaGNw58pEtvN9qA%0Aw1arfA%2F28FE4mpVj%2BGc%3D%0A)

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386575/b9798bb7a2ab92024fa4d97f2ff4/7b2327e1-ab3f-41e5-8be0-77c0f35a4015?expires=1784262600&amp;signature=2ffa0103d14c39e976e28c67fc9ef462315f832e75ae25ea2ffcab839d9bb8cb&amp;req=diIhFsp2m4RYXPMW1HO4zW55wNWbxlM3JuVz%2B3EZKJ5YcfITMC7FhO%2F2RAiP%0AeoQNesua4R4k%2BMVKKLM%3D%0A)

Note the following precedence rules:

- Individual limits always override group limits, regardless of which is higher.

- If a user belongs to multiple groups with different limits, the **Multi-group spend limit** setting under **Spending defaults** controls whether the higher or lower limit applies.

- Org-wide limits remain the hard ceiling.

Membership changes take effect automatically—users inherit or lose limits as soon as their group membership changes. Relevant only for usage-based billing orgs.

---

## Step 11: Verify and monitor

1. **Spot-check access**: Open the "⋮" menu on a the right side of a member's row in **[Organization settings > Members](https://claude.ai/admin-settings/members)** and select "View effective role." The modal shows every capability, admin permission, and connector the member has across all their roles, with a "Granted by" label naming which role provides each one. You can do the same for a group from **[Organization settings > Groups](https://claude.ai/admin-settings/groups)**. For details, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

2. **Test the restricted state**: Log in as (or ask) a member who should not have a feature like Cowork. They should see it greyed out with the message "Contact your admin to request access to this feature."

3. **Test the granted state**: Confirm a member who should have the feature sees it working normally.

4. **Check edge cases**: Test members in multiple groups, members with no group, and new members joining via SSO.

**If you configured admin permissions, also check:**

- **Group and role assignments:** Owners can verify a member's access by checking their group assignments on the Members page and the roles those groups are assigned to on the Roles page.

- **Organization settings:** In organization settings, the member only sees the sections their admin permissions cover. Everything else is hidden from their settings. Members with view access see pages as read-only, with controls disabled.

- **Analytics access:** Members with Analytics access will view analytics in **[Settings > Analytics](https://claude.ai/analytics/activity)**, not organization settings.

**If you configured connector permissions, also check:**

- **Connector menu:** blocked connectors don’t appear, and connectors with at least one granted tool do.

- **Connector settings:** blocked tools are grayed out with “This tool is not enabled for your role. Contact your administrator.” Tools capped at “Needs approval” show a personal approval menu limited to “Ask” and “Never.”

- **In a conversation:** ask Claude to use a blocked tool, and it reports it has no tool for the task. Ask it to use a “Needs approval” tool, and the approval prompt appears without an “Always allow” option.

**If you configured model access, also check:**

- **Model picker:** disabled models don't appear, and the effort menu stops at the role's cap.

- **In a conversation:** ask the member to switch to a disabled model. It shouldn't be listed, and in Claude Code CLI, /model <disabled-model> returns an error.

Role changes may take up to 15 minutes to take effect across the platform. Members may need to refresh their browser to see updated access.

---

## Using SCIM with role-based capabilities

SCIM connects to your role-based capabilities through two mechanisms that work together.

### IdP group-to-role mapping

This controls which built-in role a member gets when they're provisioned. Map your IdP groups to "Custom" roles so that new members' access is automatically governed by custom role capabilities.

1. Navigate to **[Organization settings > Organization and access](http://claude.ai/admin-settings/organization)**.

2. In the role mappings table, map your IdP groups to "Custom" roles.

### Group sync

This pulls your IdP groups into Claude so they can be assigned to custom roles.

1. Navigate to **[Organization settings > Groups](http://claude.ai/admin-settings/groups)**

2. Click “Check for updates” in the **SCIM sync** section.

3. When prompted to sync Groups, Members, or Both, select Groups only. Syncing Members can affect provisioning and member access.

4. Your IdP groups appear as SCIM-sourced groups in the list.

5. Assign SCIM groups to custom roles just like manually created groups.

6. In your IdP, only push the groups you actually intend to use for RBAC or spend limits. Syncing all IdP groups can slow page loads in the Groups section.

**Note:** Custom role permissions only apply to members with "Custom" roles selected in **[Organization settings > Members](https://claude.ai/admin-settings/members)**. If you map an IdP group to a different role (like User) through the group-to-role mapping but assign that same SCIM group to a custom role, the custom role's permissions have no effect—the member gets their permissions from their assigned role instead. To use custom roles, make sure the IdP group is mapped to "Custom."

### Ongoing management with SCIM

- To grant a member access to a feature, add them to the appropriate IdP group. On the next sync, they pick up the custom role assigned to that group.

- To revoke access, remove them from the IdP group. On the next sync, the permission is removed.

- Click “SCIM sync” in the Groups section to force an immediate sync rather than waiting for the next scheduled sync.

---

## Rollback plan

If you notice your role structure is misconfigured after migration:

1. Turn off any organization-level features that were enabled as part of the migration.

2. Change affected members back to their previous built-in role (for example, User).

3. They immediately regain the static permissions from that role, and custom role permissions stop applying.

4. Adjust roles and groups as needed, then re-migrate.

If you enabled group mappings during setup and lost admin access, follow the recovery steps in **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning#h_74979446b3)** under "I lost Admin/Owner access after enabling group mappings."

---

## Frequently asked questions

### Do I need to enable a feature at the organization level if I only want some members to have it?

Yes. The organization-level toggle must be on for custom roles to control per-member access. If a feature is off at the organization level, no one can access it regardless of their role. Think of it as a main switch—custom roles control who gets access underneath it.

### What happens if a member whose role is set to "Custom" isn't in any groups?

They have no custom role permissions, so all features that require permissions are greyed out or hidden. Make sure every member whose roles is set to "Custom" is in at least one group that's assigned to a custom role.

### A model is missing from a member's model picker.

Either the model is disabled at the organization level (**[Organization settings > Models](http://claude.ai/admin-settings/models)**) or none of the member's custom roles grant it. Org-level disables affect everyone, including Owners and Admins.

### What if a custom role doesn't grant chat access?

Members in that role won't see Claude's chat interface. They'll land on their settings page when they sign in. If their role grants other products like Cowork or Claude Code, those remain accessible from their settings page and from the relevant apps.

Chat is enabled by default in all custom roles, so you only need to worry about this if you intentionally toggled chat off for a role.

### Can I use both built-in and custom roles?

Yes. Members with the User, Admin, or Owner roles are unaffected by custom role permissions because they get their permissions from those roles directly. Only members with a role set to "Custom" are controlled by the group-and-role system. This allows gradual migration.

### What if a member is in two groups with different roles?

Permissions are additive. If any role in a member's chain grants a feature, they have it. You can't use a role to remove a permission granted by another role.

### Can I use SCIM groups and manual groups together?

Yes. Both types can be assigned to custom roles. The difference is that SCIM group membership is managed in your identity provider, while manual group membership is managed in Claude's organization settings.

### Are Owners and Primary Owners affected by custom role permissions?

No. Owners and Primary Owners always have full access to all features.

### How does this work across parent and child organizations?

Groups and SCIM sync are managed at the parent organization level and shared across all child organizations. Role and spend limit assignments are configured independently in each child organization—changes in one child organization don't affect others. Group membership changes and SCIM resyncs propagate across all child organizations under the same parent.

### What happens to my existing custom roles when connector permissions are enabled?

Each existing role is seeded with the “All connectors” grant at “Always allow,” so members’ access doesn’t change at enablement. You narrow access from there.

### What’s the default connector permission on a new role?

“Needs approval” on every connector. The create-role flow steps through the Connectors tab so you see this before saving.

### What happens when I add a new connector after my roles exist?

A role whose “All connectors” row is set to “Always allow,” “Needs approval,” or “Blocked” covers the new connector at that level automatically. A role whose “All connectors” row is set to “Custom” treats the new connector as “Blocked” until you set it.

### I blocked a connector in a role, but a member with that role can still use it. Why?

Check whether the member holds another role that grants it, since the most permissive grant wins across roles. The conflict warning on the connector row lists those roles. Also confirm the member’s role is set to "Custom."

### My organization-wide tool policy already blocks a tool. Do I need to block it in every role?

No. The organization-wide policy is the ceiling. A tool blocked there is blocked for everyone, regardless of role grants.

### A member's role and the organization-wide policy are both set to "Always allow," but "Allow for all tasks" is grayed out in Cowork. Why?

Cowork has a separate organization setting, **Allow "Always allow" for connector tools**, that gates write-capable connector tools. It's off by default. Until it's turned on, "Allow for all tasks" stays grayed out regardless of role grants and tool policies, and previously saved always-allow preferences aren't honored. Read-only tools are exempt only when the connector annotates them as read-only, which most custom connectors don't. For more information, see **[Connector tool approvals](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans#h_1bd1fa754d).**

### Can a role grant a tool that the organization-wide policy sets to “Needs approval”?

The role can grant it, but the stricter setting wins, so members see it capped at “Needs approval.” To let members set “Always allow,” raise the organization-wide policy to “Always allow” first.

### Can I grant one tool on a connector without granting the whole connector?

Yes. Set the connector to “Custom,” set the one tool to “Always allow” or “Needs approval,” and leave the rest “Blocked.”

### Do connector permissions apply to built-in tools like web search or code execution?

No. Built-in features are governed on the Capabilities tab. The Connectors tab governs connectors your organization has added.

### How quickly do connector permission changes take effect?

Role changes may take up to 15 minutes to take effect. Members may need to refresh their browser.

### Can someone in a custom role with permissions give themselves more access?

Only if their role includes Identity & Access set to Manage, which covers editing roles and groups. Reserve that permission for trusted security and IT administrators, since it can be used to change role definitions including their own.

### Can I give admin permissions to a member on the User, Admin, Owner, or Primary Owner role?

No. Admin permissions only apply to members in a custom role. Members on a built-in role keep the access that role grants. To give someone specific admin permissions, change the member to a custom role and add them to a group assigned to a role with the permissions they need. Keep in mind this removes their previous built-in role access.

### What does someone see when they don’t have permissions for a certain setting?

Organization settings only shows the sections their permissions cover. Sections they don’t have access to are hidden entirely from their organization settings.

### How do I audit who has admin access?

**[Organization settings > Roles](https://Organization%20settings%20>%20Roles)** shows the admin permissions each custom role grants, and **[Organization settings > Groups](http://claude.ai/admin-settings/groups)** shows which groups are assigned to each role and who belongs to them. To check a specific member, look up their groups on **[Organization settings > Members](http://claude.ai/admin-settings/members)**, then the roles those groups are assigned to.

### What if someone needs permissions across multiple areas?

Create one role that grants access to multiple areas, or add the member to multiple groups whose roles cover the areas they need. Permissions combine additively.