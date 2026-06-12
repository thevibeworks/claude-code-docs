Title: Set up role-based permissions on Enterprise plans

URL Source: https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans

Markdown Content:
This guide walks you through setting up role-based permissions for your Enterprise organization. This lets you control which features and connectors specific teams or groups of members can access, and delegate specific admin access like billing or user management, rather than giving everyone the same permissions.

Before you start, make sure you're familiar with:

## Before you begin

You'll need Owner or Primary Owner access to your Enterprise organization, or a custom role with Identity & Access set to Manage.

**Check which capabilities are enabled at the org level.** Go to **Organization settings**and ensure you know which capabilities members can access currently. For settings managed by RBAC, both the org setting and role setting are required to be on for users to get access.

**Determine which teams or functions need each capability.** For example, Engineering gets Claude Code + Fast Mode and Marketing gets Cowork + Web Search. From here, define your custom roles.

**Dual-seat plans.** If your organization is on a dual-seat Enterprise plan (with Chat and Chat + Claude Code seats), custom roles don't override seat-level restrictions. A member assigned to a Chat-only seat can't access Claude Code even if their custom role grants it. The same applies in reverse: if a member's custom role doesn't grant the chat capability, they won't have chat access regardless of their seat type. Plan your role structure with seat assignments in mind.

**Decide how you'll create groups.** You can create groups manually in Claude, or sync them from your identity provider (IdP) via SCIM. You can also use both methods simultaneously. If you plan to use IdP groups from Okta, Entra ID, or another provider, make sure SCIM directory sync is configured. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

**Add the connectors you plan to govern.**Connector permissions only cover connectors that an Owner or Primary Owner has already added under **Organization settings > Connectors** and connected with admin credentials. Review your organization-wide tool policy there as well, since role grants narrow within it and can’t widen past it. See **[Use connectors to extend Claude’s capabilities](https://support.claude.com/en/articles/11176164-)**.

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

Create roles that delegate parts of administration without granting the Owner role. A custom role with admin permissions does not need any user capabilities, and vice versa. You could create a "Finance" role that grants Billing access but no chat or Claude Code capability, or an "Engineering Lead" role that grants Claude Code plus Analytics view access.

## Step 1: Audit your current settings

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260367415/3e1b2f57cc457a101ce2a424ec86/e3cc8982-ef39-4c19-bd4c-81c60aeef56e?expires=1781274600&signature=6affa4871865e9828595e96a56e4ff87acec23de06875b394fa1c6aa30b250d8&req=diIhFsp4moVeXPMW1HO4zdVuRppMBhEtPwB%2FtcRiWFp0D5m8cFv%2FAgJQDWmd%0ABO8tGXORztBkGNHPO4A%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260367415/3e1b2f57cc457a101ce2a424ec86/e3cc8982-ef39-4c19-bd4c-81c60aeef56e?expires=1781274600&signature=6affa4871865e9828595e96a56e4ff87acec23de06875b394fa1c6aa30b250d8&req=diIhFsp4moVeXPMW1HO4zdVuRppMBhEtPwB%2FtcRiWFp0D5m8cFv%2FAgJQDWmd%0ABO8tGXORztBkGNHPO4A%3D%0A)

Remember: any feature you want to control per-group must be **enabled** at the organization level. If a feature is toggled off at the organization level, no custom role can grant access to it.

## Step 2: Create custom roles

Create your custom roles before enabling any features or migrating members. This ensures your roles are ready to enforce access the moment features turn on.

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260368574/1f06655487bef25512430e3e2899/620bea7b-f6af-4cc9-aa3a-b1d49354e227?expires=1781274600&signature=9285d7cedfe0e1d5f6c3155dd854f17b5d4876f01903f7c0102c3c2c1a307f24&req=diIhFsp4lYRYXfMW1HO4zZqxkwf0vyC08XPTLNWu%2BxNASor%2BycpL2u1tzB%2FG%0AJlhZGcZHQdXj8eFT8UQ%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260368574/1f06655487bef25512430e3e2899/620bea7b-f6af-4cc9-aa3a-b1d49354e227?expires=1781274600&signature=9285d7cedfe0e1d5f6c3155dd854f17b5d4876f01903f7c0102c3c2c1a307f24&req=diIhFsp4lYRYXfMW1HO4zZqxkwf0vyC08XPTLNWu%2BxNASor%2BycpL2u1tzB%2FG%0AJlhZGcZHQdXj8eFT8UQ%3D%0A)

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450911635/b9eeefed6d0afeba84c41e0e5750/b75fcd1e-790c-46ed-a1e1-e3f14a9fc619?expires=1781274600&signature=46d96a4e9ea7651d3083f7f95ca2e52132e998f19ea95dae529666148061f012&req=diQiFsB%2FnIdcXPMW1HO4zTixNGmMLt57mPB%2FOFA1gt4Ha1UtoLibAuU12UCn%0AumeIHvCpYro16%2FbFGI8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450911635/b9eeefed6d0afeba84c41e0e5750/b75fcd1e-790c-46ed-a1e1-e3f14a9fc619?expires=1781274600&signature=46d96a4e9ea7651d3083f7f95ca2e52132e998f19ea95dae529666148061f012&req=diQiFsB%2FnIdcXPMW1HO4zTixNGmMLt57mPB%2FOFA1gt4Ha1UtoLibAuU12UCn%0AumeIHvCpYro16%2FbFGI8%3D%0A)

Changes to custom roles can take up to five minutes to propagate. Members may need to refresh their browsers to see updated access.

## Step 3: Configure admin permissions (optional)

Set admin permissions on each role to delegate access to admin settings, like billing, user management, or privacy, without granting the Owner role. This step is optional. If you don't configure it, roles grant no admin access and administration stays with Owners and Primary Owners. For what each permission area covers, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

### Locate the Permissions tab

[![Image 4](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450919335/b85e8d290319c4dace2564ac12a4/c8753166-7172-4a30-9cf5-1bf660ee63fa?expires=1781274600&signature=b455fb7b5123978854e97492c21bba5ceb33ea74513ce20073e97df1c1ad0971&req=diQiFsB%2FlIJcXPMW1HO4zZO92Z%2FocWVJnDVlWKo2%2B8F8ekocY7WEVoIlHcN5%0AhVlRX%2BV2454TxrbjpQM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450919335/b85e8d290319c4dace2564ac12a4/c8753166-7172-4a30-9cf5-1bf660ee63fa?expires=1781274600&signature=b455fb7b5123978854e97492c21bba5ceb33ea74513ce20073e97df1c1ad0971&req=diQiFsB%2FlIJcXPMW1HO4zZO92Z%2FocWVJnDVlWKo2%2B8F8ekocY7WEVoIlHcN5%0AhVlRX%2BV2454TxrbjpQM%3D%0A)

### **Set admin permissions**

The **Permissions** tab lists each admin area: Identity & Access, Billing, Analytics, Privacy, User Management, and Libraries. Set each admin area to one of the following options:

Within an area, you grant all of View or all of Manage. You can't grant or restrict individual pages or settings.

### **Verify enforcement**

Verify admin permissions after you’ve migrated members to “Custom roles” (Step 7). See **Step 10: Verify and monitor**.

## Step 4: Configure connector permissions (optional)

Set connector permissions on each role to control which connectors, and which tools on those connectors, the role can use. This step is optional. If you don’t configure it, your roles fall back to the default behavior described below. For how the permission model works end to end, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

### Locate the Connectors tab

The default settings for new roles are permissive. When creating or modifying a role, confirm the settings on each tab to avoid granting unintended permissions.

[![Image 5](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450940105/b181b337a4c03cad22b4d98564e9/c3c4e0d4-a38a-4493-b722-c3ed5ce7f199?expires=1781274600&signature=e277a5b86b2a9ce710e5163d0c8532b67884d55c72ae572c6e1c20a3bfcc059f&req=diQiFsB6nYBfXPMW1HO4zdioUCLz1ntP3K2WJtwXcD7l%2BhieAlUHtGu2UZU6%0A0ln0OSAn2qMFyi2%2FSsk%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450940105/b181b337a4c03cad22b4d98564e9/c3c4e0d4-a38a-4493-b722-c3ed5ce7f199?expires=1781274600&signature=e277a5b86b2a9ce710e5163d0c8532b67884d55c72ae572c6e1c20a3bfcc059f&req=diQiFsB6nYBfXPMW1HO4zdioUCLz1ntP3K2WJtwXcD7l%2BhieAlUHtGu2UZU6%0A0ln0OSAn2qMFyi2%2FSsk%3D%0A)

### Set connector-level permissions

The **Connectors** tab lists an **All connectors** row at the top, followed by every connector your organization has added. Each row has a dropdown with four options:

Choosing “Always allow,” “Needs approval,” or “Blocked” applies that level to every tool on the connector. The **All connectors** row works the same way one level up: it sets a baseline for every connector at once, including any connector you add later. Use it to set a role’s default, then override individual connectors.

[![Image 6](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450941048/1b97ded56089d95cf094498318c7/9f61f392-a9cf-4157-ba8e-465078ad6e8d?expires=1781274600&signature=f4c8123ad7816873b7adfa32890ed72a27e62a0080b64a2f95befab6e2bd3717&req=diQiFsB6nIFbUfMW1HO4zfT%2BF%2FbdxkVSHrpE1N7y4OgatnP1TEBJh3rabLzm%0AYSek9NWi5LpiLtEzqw4%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450941048/1b97ded56089d95cf094498318c7/9f61f392-a9cf-4157-ba8e-465078ad6e8d?expires=1781274600&signature=f4c8123ad7816873b7adfa32890ed72a27e62a0080b64a2f95befab6e2bd3717&req=diQiFsB6nIFbUfMW1HO4zfT%2BF%2FbdxkVSHrpE1N7y4OgatnP1TEBJh3rabLzm%0AYSek9NWi5LpiLtEzqw4%3D%0A)

### Set per-tool permissions

Set a connector to **Custom** to reveal its tools as individual rows. Each tool has its own dropdown: “Always allow,” “Needs approval,” or “Blocked.”

Per-tool permissions let a role reach part of a connector. For example, with Jira set to **Custom**, its `search_issues` tool set to “Needs approval,” and every other Jira tool set to “Blocked,” members with the role can search Jira but nothing else. Claude only sees the tools you’ve granted, so asking it to create a ticket returns “I don’t have a tool for that” rather than an error.

[![Image 7](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450943405/935a40308c5d362efdec9ac27c94/ca98a77c-65eb-49da-8692-96770913db59?expires=1781274600&signature=9d943f77499ebfa3fb03d4b025040beaa3fcd7c169c4a1ce95f76986497cc5c4&req=diQiFsB6noVfXPMW1HO4zealvXUxOFIPdZOdfzLm1hb1EArsGrKB9OcKRR7x%0A6ziyn1J07ZVdNYOIT2Q%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450943405/935a40308c5d362efdec9ac27c94/ca98a77c-65eb-49da-8692-96770913db59?expires=1781274600&signature=9d943f77499ebfa3fb03d4b025040beaa3fcd7c169c4a1ce95f76986497cc5c4&req=diQiFsB6noVfXPMW1HO4zealvXUxOFIPdZOdfzLm1hb1EArsGrKB9OcKRR7x%0A6ziyn1J07ZVdNYOIT2Q%3D%0A)

### Review cross-role conflicts

Because connector permissions are additive across roles, blocking a connector in one role has no effect on a member who also holds another role that grants it. Each connector row shows a warning when other roles grant the same connector at a different level. The warning names those roles and links to them, and the most permissive grant is the one that applies.

If you have unsaved edits when you open a linked role, you’re asked to discard them first.

[![Image 8](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450944230/d7d64ec81cc36e35604e194ceb55/228818b4-8130-43a7-86ef-5deab64a4368?expires=1781274600&signature=5e50fac008cf181f7dfe7a45e272e97aa69dc2034a8c33caab24f4b5bfb7ec03&req=diQiFsB6mYNcWfMW1HO4zZhGoZkfnHMmxdmRQIU5rt7P5I0eOeuI3PNV3OxY%0Azyv%2Fq1EvcjdPX%2Bql4fg%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2450944230/d7d64ec81cc36e35604e194ceb55/228818b4-8130-43a7-86ef-5deab64a4368?expires=1781274600&signature=5e50fac008cf181f7dfe7a45e272e97aa69dc2034a8c33caab24f4b5bfb7ec03&req=diQiFsB6mYNcWfMW1HO4zZhGoZkfnHMmxdmRQIU5rt7P5I0eOeuI3PNV3OxY%0Azyv%2Fq1EvcjdPX%2Bql4fg%3D%0A)

### Verify enforcement

Verify connector permissions after you’ve migrated members to “Custom roles” (Step 7). See **Step 10: Verify and monitor**.

## Step 5: Create groups and assign roles

[![Image 9](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260371973/b503c99ef71d8a89b7aff606511b/b1afd593-3b23-4fa9-8b9b-ee6beaf74fd7?expires=1781274600&signature=7ba3f2f0e338fa699b8ae6c4ac77f198cefb67b918ad325dc7785b8d52408db9&req=diIhFsp5nIhYWvMW1HO4zdMu8WF0HQ1sKwlCydrbfL6Jc%2BiPcxdb%2Fr28%2BD5V%0AAvzWAeoc%2BxSh%2B4vTc1U%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260371973/b503c99ef71d8a89b7aff606511b/b1afd593-3b23-4fa9-8b9b-ee6beaf74fd7?expires=1781274600&signature=7ba3f2f0e338fa699b8ae6c4ac77f198cefb67b918ad325dc7785b8d52408db9&req=diIhFsp5nIhYWvMW1HO4zdMu8WF0HQ1sKwlCydrbfL6Jc%2BiPcxdb%2Fr28%2BD5V%0AAvzWAeoc%2BxSh%2B4vTc1U%3D%0A)

[![Image 10](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260372813/83ccc4784bdfc8600101bc42ec4b/6e7456ac-9887-4e04-b757-3972110fbdce?expires=1781274600&signature=84f368311f93ff030fedb0e5b93e2ebb9ffecb090a12d0d94df1e5474718f9ec&req=diIhFsp5n4leWvMW1HO4zQetnyJVY6v%2BczQdKdGFNsdNGQbIasVK9XACjHVP%0AR8xmERhwycoVrz2FUnM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260372813/83ccc4784bdfc8600101bc42ec4b/6e7456ac-9887-4e04-b757-3972110fbdce?expires=1781274600&signature=84f368311f93ff030fedb0e5b93e2ebb9ffecb090a12d0d94df1e5474718f9ec&req=diIhFsp5n4leWvMW1HO4zQetnyJVY6v%2BczQdKdGFNsdNGQbIasVK9XACjHVP%0AR8xmERhwycoVrz2FUnM%3D%0A)

[![Image 11](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260374677/5f9d8febb8ae25153a94d0b827b9/c8314b27-96c1-4743-ae8b-25e511181837?expires=1781274600&signature=b88b3134ce95cc241b0aa36cb05a07643844ade30dc3aa1d74cfe050b48d576e&req=diIhFsp5mYdYXvMW1HO4zXzl64537z%2BcKYkQn0Dd8NWHqiO1bQYjBXODiV92%0ABWPu1c2xXMRvmu%2BP1Tk%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260374677/5f9d8febb8ae25153a94d0b827b9/c8314b27-96c1-4743-ae8b-25e511181837?expires=1781274600&signature=b88b3134ce95cc241b0aa36cb05a07643844ade30dc3aa1d74cfe050b48d576e&req=diIhFsp5mYdYXvMW1HO4zXzl64537z%2BcKYkQn0Dd8NWHqiO1bQYjBXODiV92%0ABWPu1c2xXMRvmu%2BP1Tk%3D%0A)

**Multiple organizations under the same parent organization:** Groups are managed at the parent organization level and propagate to all child organizations. You may see members from other organizations listed in a group—this doesn't mean they have access to your organization. Custom roles assigned to a group only grant capabilities to members who are part of your specific organization.

If you request to move an organization from one parent to another (this is rare in practice), groups and roles will become undefined and you will need to re-create them.

## Step 6: Verify group and role assignments

Before migrating members to custom roles, confirm that every member you plan to migrate is in at least one group assigned to a custom role. Members who are migrated without group or role coverage will lose access to all governed features.

## Step 7: Migrate members to custom roles

For custom role capabilities to take effect, members must have their role set to “Custom roles.” Members with the User, Admin, or Owner roles get their permissions from those roles directly, not from custom roles.

Choose the migration path based on whether your organization already enabled group mappings:

### Path A: Enable group mappings (only if already in use)

Use this path only if your organization already enabled group mappings for role assignment. If you aren't already using this setting, skip to Path B.

[![Image 12](https://downloads.intercomcdn.com/i/o/lupk8zyo/2434934020/d154818947d8d84ebf1aec8d5462/image.png?expires=1781274600&signature=6c098beaab3f6eb191760fd6bf567c765ec160985a92f7ececdc37442efe61ef&req=diQkEsB9mYFdWfMW1HO4zQyCmE7hTkFuSnpHYy0fFQv5zX9EwG%2ByLust9dSN%0AstPYBcu2mwJZDjlLjfk%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2434934020/d154818947d8d84ebf1aec8d5462/image.png?expires=1781274600&signature=6c098beaab3f6eb191760fd6bf567c765ec160985a92f7ececdc37442efe61ef&req=diQkEsB9mYFdWfMW1HO4zQyCmE7hTkFuSnpHYy0fFQv5zX9EwG%2ByLust9dSN%0AstPYBcu2mwJZDjlLjfk%3D%0A)

Members in IdP groups mapped to "Custom roles" follow the permissions of the custom roles assigned to their groups in Claude. Members in IdP groups mapped to User follow the organization-level capability settings. If a member is in groups across both mappings, "Custom roles" takes precedence.

### Path B: Bulk assignment tool

Use this path if your organization hasn’t enabled group mappings.

[![Image 13](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260377969/ba3b7ba08518f0a50e2a84f82655/bdf1aea3-2fe7-4f3c-868b-cc35ae8b7d1d?expires=1781274600&signature=edfe15066b2403efc7603aa79041a509162a543196b3d364e1e51d7f7469ab5e&req=diIhFsp5mohZUPMW1HO4zYFuwIAggs2KlPaXg%2F0URImrSELjq11q2jQ5xDmP%0ACGVQNnodaMDfInOUfqw%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260377969/ba3b7ba08518f0a50e2a84f82655/bdf1aea3-2fe7-4f3c-868b-cc35ae8b7d1d?expires=1781274600&signature=edfe15066b2403efc7603aa79041a509162a543196b3d364e1e51d7f7469ab5e&req=diIhFsp5mohZUPMW1HO4zYFuwIAggs2KlPaXg%2F0URImrSELjq11q2jQ5xDmP%0ACGVQNnodaMDfInOUfqw%3D%0A)

[![Image 14](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260378309/abe25b6478c721a2f965b35361b7/beff124a-0a44-4f7f-97f8-391ce6e8c55b?expires=1781274600&signature=55a56d51ae982801ef4bfe2bf5a23d61923a96dfc752f837d87222dd1ac53ea8&req=diIhFsp5lYJfUPMW1HO4zRgyEFneVO3QZ8KPhClFzQllt9RzWtbZLFBgBJrg%0AsJJDuSnLycY2Gng%2BSyU%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260378309/abe25b6478c721a2f965b35361b7/beff124a-0a44-4f7f-97f8-391ce6e8c55b?expires=1781274600&signature=55a56d51ae982801ef4bfe2bf5a23d61923a96dfc752f837d87222dd1ac53ea8&req=diIhFsp5lYJfUPMW1HO4zRgyEFneVO3QZ8KPhClFzQllt9RzWtbZLFBgBJrg%0AsJJDuSnLycY2Gng%2BSyU%3D%0A)

[![Image 15](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260378764/0640dfbb3f1e3ee83976a64df36e/b7021d51-24a0-4db7-949e-364e1721ad5b?expires=1781274600&signature=6bfa778701aa02dec4341ebb160e4f6f57c861f04f4a1cdc480610d1964bbe68&req=diIhFsp5lYZZXfMW1HO4zbvZDByTsvziG3CUmvrYMDXZEGCoD8wAk1WrzpQj%0AJjglgdsAx%2FFHSrphcD4%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260378764/0640dfbb3f1e3ee83976a64df36e/b7021d51-24a0-4db7-949e-364e1721ad5b?expires=1781274600&signature=6bfa778701aa02dec4341ebb160e4f6f57c861f04f4a1cdc480610d1964bbe68&req=diIhFsp5lYZZXfMW1HO4zbvZDByTsvziG3CUmvrYMDXZEGCoD8wAk1WrzpQj%0AJjglgdsAx%2FFHSrphcD4%3D%0A)

We recommend migrating a pilot group first—one team or department—and verifying their access is correct before expanding to the rest of the organization.

### Gradual rollout

Whichever path you use, we recommend migrating in stages:

## Step 8: Enable features at the organization level

Only enable organization-level features after roles, groups, and member migration are complete. This ensures custom role capabilities are already in place, with no window where unauthorized members could access a feature.

For any feature you want to control per-group:

Enabling a feature at the organization level doesn't mean everyone gets it—custom role permissions are already in place to control who can use it. Think of the organization-level toggle as making the feature "available for role-based assignment" rather than "on for everyone."

## Step 9: Apply a group spend limit (usage-based orgs only)

Navigate to the “Usage” page to assign a per-user monthly spend limit to any group.

[![Image 16](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386576/377ac052069ff5a35b3023f50d12/dface609-9d85-4ee1-8ed3-bfe019a2bd0a?expires=1781274600&signature=35ab6867070ba85610731c880871941bc74bda18dc1312b9263bcd1210a82e06&req=diIhFsp2m4RYX%2FMW1HO4zfvdi5adQgKMBMkPcsY1DF4wPSDeztJiC95BvJhX%0A0%2FBFAPbYhSew4oKtQqM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386576/377ac052069ff5a35b3023f50d12/dface609-9d85-4ee1-8ed3-bfe019a2bd0a?expires=1781274600&signature=35ab6867070ba85610731c880871941bc74bda18dc1312b9263bcd1210a82e06&req=diIhFsp2m4RYX%2FMW1HO4zfvdi5adQgKMBMkPcsY1DF4wPSDeztJiC95BvJhX%0A0%2FBFAPbYhSew4oKtQqM%3D%0A)

[![Image 17](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386575/b9798bb7a2ab92024fa4d97f2ff4/7b2327e1-ab3f-41e5-8be0-77c0f35a4015?expires=1781274600&signature=21cfd43ff7e7cf4c4f87af55043a12266a874ea12a97f410f37bacf34a9cc2b9&req=diIhFsp2m4RYXPMW1HO4zW55wNCbx1U3JuVz%2B3EZKJ6qPvvJ9JsHwMbmUctV%0AKztDZrHnAbb%2BDv3nSPI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2260386575/b9798bb7a2ab92024fa4d97f2ff4/7b2327e1-ab3f-41e5-8be0-77c0f35a4015?expires=1781274600&signature=21cfd43ff7e7cf4c4f87af55043a12266a874ea12a97f410f37bacf34a9cc2b9&req=diIhFsp2m4RYXPMW1HO4zW55wNCbx1U3JuVz%2B3EZKJ6qPvvJ9JsHwMbmUctV%0AKztDZrHnAbb%2BDv3nSPI%3D%0A)

Note the following precedence rules:

Membership changes take effect automatically—users inherit or lose limits as soon as their group membership changes. Relevant only for usage-based billing orgs.

## Step 10: Verify and monitor

**If you configured admin permissions, also check:**

**If you configured connector permissions, also check:**

Permission changes take up to 15 minutes to fully sync across the platform. Members may need to refresh their browser to see updated access.

Connector permission changes reach Claude on the member’s next message and the connector menu on their next page load, usually within a minute.

## Using SCIM with role-based capabilities

SCIM connects to your role-based capabilities through two mechanisms that work together.

### IdP group-to-role mapping

This controls which built-in role a member gets when they're provisioned. Map your IdP groups to “Custom roles” so that new members' access is automatically governed by custom role capabilities.

### Group sync

This pulls your IdP groups into Claude so they can be assigned to custom roles.

### Ongoing management with SCIM

## Rollback plan

If you notice your role structure is misconfigured after migration:

If you enabled group mappings during setup and lost admin access, follow the recovery steps in **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning#h_74979446b3)** under "I lost Admin/Owner access after enabling group mappings."

## Frequently asked questions

### Do I need to enable a feature at the organization level if I only want some members to have it?

Yes. The organization-level toggle must be on for custom roles to control per-member access. If a feature is off at the organization level, no one can access it regardless of their role. Think of it as a main switch—custom roles control who gets access underneath it.

### What happens if a member set to “Custom roles” isn't in any groups?

They have no custom role permissions, so all features that require permissions are greyed out or hidden. Make sure every member set to “Custom roles” is in at least one group that's assigned to a custom role.

### What if a custom role doesn't grant chat access?

Members in that role won't see Claude's chat interface. They'll land on their settings page when they sign in. If their role grants other products like Cowork or Claude Code, those remain accessible from their settings page and from the relevant apps.

Chat is enabled by default in all custom roles, so you only need to worry about this if you intentionally toggled chat off for a role.

### Can I use both built-in and custom roles?

Yes. Members with the User, Admin, or Owner roles are unaffected by custom role permissions because they get their permissions from those roles directly. Only members set to "Custom roles" are controlled by the group-and-role system. This allows gradual migration.

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

Check whether the member holds another role that grants it, since the most permissive grant wins across roles. The conflict warning on the connector row lists those roles. Also confirm the member’s role is set to “Custom roles.”

### My organization-wide tool policy already blocks a tool. Do I need to block it in every role?

No. The organization-wide policy is the ceiling. A tool blocked there is blocked for everyone, regardless of role grants.

### Can a role grant a tool that the organization-wide policy sets to “Needs approval”?

The role can grant it, but the stricter setting wins, so members see it capped at “Needs approval.” To let members set “Always allow,” raise the organization-wide policy to “Always allow” first.

### Can I grant one tool on a connector without granting the whole connector?

Yes. Set the connector to “Custom,” set the one tool to “Always allow” or “Needs approval,” and leave the rest “Blocked.”

### Do connector permissions apply to built-in tools like web search or code execution?

No. Built-in features are governed on the Capabilities tab. The Connectors tab governs connectors your organization has added.

### How quickly do connector permission changes take effect?

They reach Claude on the member’s next message and the connector menu on their next page load. Allow about a minute for changes to propagate. Group and role membership changes propagate within about five minutes like other role changes.

### Can someone in a custom role with permissions give themselves more access?

Only if their role includes Identity & Access set to Manage, which covers editing roles and groups. Reserve that permission for trusted security and IT administrators, since it can be used to change role definitions including their own.

### Can I give admin permissions to a member on the User, Admin, Owner, or Primary Owner role?

No. Admin permissions only apply to members in a custom role. Members on a built-in role keep the access that role grants. To give someone specific admin permissions, change the member to a custom role and add them to a group assigned to a role with the permissions they need. Keep in mind this removes their previous built-in role access.

### What does someone see when they don’t have permissions for a certain setting?

Organization settings only shows the sections their permissions cover. Sections they don’t have access to are hidden entirely from their organization settings.

### How do I audit who has admin access?

**Organization settings > Roles** shows the admin permissions each custom role grants, and **Organization settings > Groups** shows which groups are assigned to each role and who belongs to them. To check a specific member, look up their groups on **Organization settings > Members**, then the roles those groups are assigned to.

### What if someone needs permissions across multiple areas?

Create one role that grants access to multiple areas, or add the member to multiple groups whose roles cover the areas they need. Permissions combine additively.

* * *

Related Articles

[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)[How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)[Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
