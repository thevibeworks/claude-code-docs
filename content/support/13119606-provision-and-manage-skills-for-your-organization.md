# Provision and manage skills for your organization

This article explains how organization owners can provision skills for everyone in their organization, and how to scope skills to specific groups using plugins. Provisioning skills lets you distribute approved workflows and capabilities across your organization from one place.

Organization-wide skill management is available to Team and Enterprise plans.

## Prerequisites

Before you can provision skills for your organization, navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**, select the “Policy” tab, and check that both **Cloud code execution and file creation** and **Skills** are toggled on. Skills require code execution to function, so if code execution is disabled, skills will not be available.

---

## Provision skills for everyone

When you upload a skill through organization settings, it becomes available to everyone in your organization in **[Customize > Skills](https://claude.ai/customize/skills)**. Individual users no longer need to upload the same skill themselves. Provisioned skills also load in Claude Code for users who sign in with their Claude account. To stop skills from syncing to Claude Code, set `syncClaudeAiSkills` to `false` in Claude Code managed settings.

**To provision a skill:**

1. Navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**.

2. Click "Add” in the upper right corner.

3. Choose “Upload a skill” or “Create a skill.”

4. If uploading, select a .zip file containing your skill (must include a SKILL.md file).

5. If creating, input the skill name and description in the modal, then click “Create.”

6. The skill is immediately provisioned to all users in your organization.

Owner-provisioned skills are enabled by default for everyone, but users can toggle individual skills off if they choose. This gives your organization consistent, approved workflows while letting users customize their own experience.

---

## Provision skills to specific groups

Provisioning a skill through **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** gives it to everyone. Enterprise plans can give skills to only some users by bundling them into a plugin and assigning that plugin to a group. The group's members see those skills, and members outside the group don't.

For example, if you have 10 skills for your marketing team, add them to a plugin and assign it to the marketing group. Only that group gets those skills.

Skills provisioned this way appear in chat (on the web and the "Chat" tab in Claude Desktop), in Claude Cowork, and in Claude Code in the terminal for users who sign in with their Claude account. Group targeting you've already set up for Cowork carries over to chat with no extra steps.

To set this up, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433)**.

---

## Control whether users can create skills

By default, users can create their own skills in Claude and upload skill files to their personal skills list. If you'd rather users only use skills you've provisioned, you can turn this off for your organization.

To turn off skill creation for users:

1. Navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Policy” tab.

2. Turn off **User-created skills**.

When **User-created skills** is off:

- Users can't create skills in Claude or upload skill files.

- Skills you've provisioned and Anthropic's built-in skills stay available, and users can still enable and use them.

**Note:** If your organization uses custom roles, a user also needs the **Create skills** capability on their role. The organization setting is the main switch: when it's off, users can't create or upload their own skills, regardless of role, but Owners can still provision skills for the organization. When it's on, Enterprise plan users on custom roles still need the role capability. Learn more about **[managing custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

---

## Let users publish skills and plugins to your organization

Users can submit a skill or plugin they've built to your organization's library so everyone can use it. When your organization requires review, an owner approves each submission before it's published, and every later version goes through the same review.

### Set the publishing policy

1. Navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and select the “Policy” tab.

2. Under **Publishing**, choose an option:

  - **Requires review:** Users can submit skills and plugins, and an owner must approve each one before it's published.When submitting, the user proposes how the item is offered. You can accept or change that when you approve.

  - **Open:** Skills and plugins that users submit are published to the organization library without review, and are available to everyone in your organization to install. Users can't choose a different offering. On Enterprise plans with **[Skill and plugin security scanning](https://support.claude.com/en/articles/15927065)** on, a new item isn't listed for others until it passes the scan, which usually takes a few minutes.

  - **Off:** Users don't see the "Publish to org" button. Owners can still add skills and plugins to the organization directly.

Your starting setting depends on your plan:

- **Team plans:** Publishing is set to “Open,” unless you already had **Share with organization** turned off, in which case “Off” is the default.

- **Enterprise plans:** Publishing starts off.

  - If your organization already had **Share with organization** turned on, it starts as “Open” instead.

  - If you haven't chosen a setting, it switches to “Requires review” on October 2, 2026. To keep publishing off, or to choose a different setting, select it yourself before then.

Turning **Publishing** off doesn't remove anything that's already published. Published items stay in the library until an owner removes them.

### Review a submission

Owners, and anyone whose role has Libraries set to “Can manage,” can review requests. You can't approve your own.

**To review a submission:**

1. Navigate to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and select the “Requests” tab.

  - Plugin and skillsubmissions appear here, and each request shows who submitted it, whether it's a skill or plugin, its security scan result, and its status. If a submission looks like a skill or plugin your organization already has, a **Possible duplicate** tag appears next to it.

2. Open a request. You'll see:

  - How the item will be offered

  - The scan result

  - Every file

  - For an update, what changed since the currently published version

  - Up to three possible duplicates, if any, each with a reason and a link

3. Choose how the item is offered and who gets it: everyone or specific groups. The submitter's proposed offering is preselected, and you can change it. Then click "Approve" to publish it, or click "Request changes" and add a note for the person who submitted it.

Keep these points in mind when reviewing:

- **You review a fixed version.** You see exactly the version that was submitted. The author can keep editing their own copy, but those edits don't reach the organization until they submit a new version and it's approved.

- **Possible duplicate hints are a note, not a block.** Only reviewers see them. They don't stop you from approving a submission, and the person who submitted it doesn't see them. No setup is needed. Duplicate checks don't run for organizations with HIPAA, zero data retention, FERPA, or customer-managed keys.

- **For Enterprise plans, submitted versions are scanned.** For Enterprise plans with **Skill and plugin security scanning** enabled, each version is checked for malicious content automatically. A submission that fails the scan can't be approved until the author fixes it and submits again. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065)**.

### Manage published skills and plugins

Every approved item is listed on the “Inventory” tab in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**. To see only your organization's items, set the **Source** filter to “Your organization."

Click the menu button at the end of a row to:

- View details and files

- View version history

- Choose how the item is offered under Default access (Available to install, Installed by default, Not available, or Required)

- Set access for specific groups under “Group access…”

- Copy a link to share with users

The “Inventory” tab also lists skills and plugins that users created or shared.

When you approve a new version, everyone who uses the item gets the update automatically. Until then, users stay on the currently approved version.

Published items are managed by your organization. If the author leaves, the published item stays in the library.

---

## Control skill sharing between users

In addition to provisioning skills top-down, you can let users share skills or plugins they've built with each other. Two independent toggles control this:

- **Skill sharing:** Users can share a skill or plugin with specific colleagues. Recipients see the skill in the **Shared with you** section of their skills list.

- **Share with groups:** Users can share a skill or plugin with an entire group. Recipients see it in the **Shared with you** section of their skills list, the same as items shared with individuals.

To let users add skills and plugins to the organization library, use the **Publishing** setting. Learn more about **[letting users publish skills and plugins to your organization](#h_1abc45a27c)**.

The **Skill sharing** toggle is on by default for Team plans and for Enterprise plans that haven't set a skills preference. For organizations with HIPAA readiness or other regulated configurations, skills and skill sharing are off by default and an admin can enable them in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** in the “Policy” tab. The **Share with groups** toggle is also off by default and can be enabled by an admin.

**Note:** Shared skills and plugins are view-only, and stay off until the recipient chooses to enable them. Recipients can enable and use a shared skill or plugin but can't edit its contents. When the owner saves a new version, everyone it's shared with gets the update automatically at next use. The owner can revoke someone's access at any time, and access is removed automatically if the recipient leaves the organization.

### Share skills with a group

Before you can share with a group, an admin needs to turn on **Share resources with this group** in the group's visibility settings. See **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

If you use custom roles, also make sure the **Share skills with groups** capability is enabled for their role. See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

Once these settings are on, users can begin sharing skills with groups.

### How shared skills differ from provisioned skills

|                               | **Owner-provisioned**  | **Shared peer-to-peer**               | **Published to the organization**                | **Shared with a group**               |
| ----------------------------- | ---------------------- | ------------------------------------- | ------------------------------------------------ | ------------------------------------- |
| **Who can share**             | Owners only            | Any user (if enabled)                 | Any user (if Publishing is on)                   | Any user (if enabled)                 |
| **Where it appears**          | Everyone's skills list | Recipient's "Shared with you" section | Organization library                             | Recipient's "Shared with you" section |
| **Can recipients remove it?** | Disable only           | Disable or delete                     | Depends on how an owner offers it                | Disable only                          |
| **Requires owner approval?**  | Owner uploads directly | No                                    | Yes, when Publishing is set to “Requires review” | No                                    |

**Important:** When Publishing is set to “Open,” anything a user publishes goes straight to the organization library without review and is available to everyone in your organization Choose “Requires review” if you want an owner to check each skill and plugin first.

### Monitor sharing activity

Skill sharing events are captured in the audit log and Compliance API as `role_assignment` events. You can see who shared a skill or plugin, with whom, and whether it was peer-to-peer, a group, or (skills only) organization-wide.

The audit log doesn't capture the contents of shared skills or plugins—only the share event itself. The “Inventory” tab shows metadata, sharing status, and scan status for skills and plugins that users created or shared, but not their contents.

---

## How users see provisioned and shared skills

Skills appear for each user in **[Customize > Skills](https://claude.ai/customize/skills)**, organized into three sections:

- **Personal skills:** Skills the user has created or uploaded.

- **Shared with you:** Skills colleagues have shared directly with a user. These appear grayed out until enabled.

- **Organization skills:** Skills an owner has provisioned and skills published to the organization. Users install these from the directory.

Owner-provisioned skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

For more on how users browse and install from the directory, see **[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)**.

---

## Manage and remove provisioned skills

The “Inventory” tab in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** lists all skills provisioned for your organization. Set **Source** to “Your organization” and **Type** to “Skills,” or search by name. To remove a skill, click the menu button at the end of its row and select “Remove from library.” Once removed, the skill will no longer appear in users' skills lists in **[Customize > Skills](https://claude.ai/customize/skills).**

**Note:** Only owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

---

## Scan skills and plugins for malicious content

On the Enterprise plan, you can turn on skill scanning for your organization. When it's on, Claude checks each third-party skill and plugin your users upload or edit for malicious content before it can run. Scanning is off by default until October 2, 2026. From that date it's on by default, where available, for Enterprise organizations that haven't set it. Organizations that already turned it on or off keep their choice.

To turn on skill scanning for your organization:

1. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and select the “Policy” tab.

2. Turn on **Skill and plugin security scanning**.

If you use custom roles, you can further define who scanning applies to by turning on the **Skill and plugin security scanning** capability for roles that should have access to skill scanning.

Here's what your users see:

- A skill or plugin that passes the scan installs normally.

- A skill or plugin that may carry risk stays usable behind a caution banner the user acknowledges.

- A skill or plugin with malicious content is blocked and can't be used.

A blocked skill can't be overridden by the user who uploaded it, and can't be approved for the organization at this time. Scanning isn't available for organizations using customer-managed encryption keys (CMEK), zero data retention (ZDR), or HIPAA configurations. Learn more about **[skill and plugin scanning](https://support.claude.com/en/articles/15927065)**.

---

## Best practices

- **Test skills before provisioning:** Upload and test skills on your own account first to verify they work as expected before distributing them organization-wide.

- **Scope specialized skills to groups:** When a skill is only relevant to one team, bundle it into a plugin and assign it to that group instead of provisioning it to everyone.

- **Use descriptive names:** Give skills clear names that help users understand their purpose at a glance.

- **Write clear descriptions:** The skill's description helps Claude determine when to use it automatically. Ensure descriptions accurately reflect what the skill does.

- **Consider default status carefully:** Enable skills by default when they're broadly useful to most users. Keep specialized skills disabled by default for the users who don't need them.

- **Decide on publishing deliberately:** Set Publishing to “Requires review” if you want an owner to check skills and plugins before they reach everyone.