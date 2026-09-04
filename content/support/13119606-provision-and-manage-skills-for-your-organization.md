# Provision and manage skills for your organization

This article explains how organization owners can provision skills for everyone in their organization, and how to scope skills to specific groups using plugins. Provisioning skills lets you distribute approved workflows and capabilities across your organization from one place.

Organization-wide skill management is available to Team and Enterprise plans.

## Prerequisites

Before you can provision skills for your organization, navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** and check that both **Code execution and file creation** and **Skills** are toggled on. Skills require code execution to function, so if code execution is disabled, skills will not be available.

---

## Provision skills for everyone

When you upload a skill through organization settings, it becomes available to everyone in your organization in **[Customize > Skills](https://claude.ai/customize/skills)**. Individual users no longer need to upload the same skill themselves.

**To provision a skill:**

1. Navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**.

2. In the **Organization skills** section, click "+ Add."

3. Select a .zip file containing your skill (must include a SKILL.md file).

4. The skill is immediately provisioned to all users in your organization.

Admin-provisioned skills are enabled by default for everyone, but users can toggle individual skills off if they choose. This gives your organization consistent, approved workflows while letting users customize their own experience.

---

## Provision skills to specific groups

Provisioning a skill through **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** gives it to everyone. To give a skill to only some users, bundle your skills into a plugin and assign that plugin to a group. The group's members see those skills, and members outside the group don't.

For example, if you have 10 skills for your marketing team, add them to a plugin and assign it to the marketing group. Only that group gets those skills.

Skills provisioned this way appear in chat, on the web and the Chat tab in Claude Desktop, as well as in Claude Cowork. Group targeting you've already set up for Cowork carries over to chat with no extra steps.

To set this up, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433)**.

---

## Control whether users can create skills

By default, users can create their own skills in Claude and upload skill files to their personal skills list. If you'd rather users only use skills you've provisioned, you can turn this off for your organization.

To turn off skill creation for users:

1. Navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**.

2. Turn off **User-created skills**.

When **User-created skills** is off:

- Users can't create skills in Claude or upload skill files.

- Skills you've provisioned and Anthropic's built-in skills stay available, and users can still enable and use them.

**Note:** If your organization uses custom roles, a user also needs the **Create skills** capability on their role. The organization setting is the main switch: when it's off, users can't create or upload their own skills, regardless of role, but Owners can still provision skills for the organization. When it's on, Enterprise plan users on custom roles still need the role capability. Learn more about **[managing custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

---

## Control skill sharing between users

In addition to provisioning skills top-down, you can let users share skills or plugins they've built with each other. Three independent toggles control this:

- **Skill sharing:** Users can share a skill or plugin with specific colleagues. Recipients see the skill in the **Shared with you** section of their skills list.

- **Share with organization:** Users can publish a skill to the organization directory, where anyone can find and install it.

- **Share with groups:** Users can share a skill or plugin with an entire group. Recipients see it in the **Shared with you** section of their skills list, the same as items shared with individuals.

The **Skill sharing** toggle is on by default for Team plans and for Enterprise plans that haven't set a skills preference. For organizations with HIPAA readiness or other regulated configurations, skills and skill sharing are off by default and an admin can enable them in **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**. The **Share with organization** and **Share with groups** toggles are also off by default and can be enabled by an admin.

**Note:** Shared skills and plugins are view-only, and stay off until the recipient chooses to enable them. Recipients can enable and use a shared skill or plugin but can't edit its contents. When the owner saves a new version, everyone it's shared with gets the update automatically at next use. The owner can revoke someone's access at any time, and access is removed automatically if the recipient leaves the organization.

### Share skills with a group

Before you can share with a group, an admin needs to turn on **Share resources with this group** in the group's visibility settings. See **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

If you use custom roles, also make sure the **Share skills with groups** capability is enabled for their role. See **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

Once these settings are on, users can begin sharing skills with groups.

### How shared skills differ from provisioned skills

|                               | **Owner-provisioned**  | **Shared peer-to-peer**               | **Shared org-wide**    | **Shared with a group**               |
| ----------------------------- | ---------------------- | ------------------------------------- | ---------------------- | ------------------------------------- |
| **Who can share**             | Owners only            | Any user (if enabled)                 | Any user (if enabled)  | Any user (if enabled)                 |
| **Where it appears**          | Everyone's skills list | Recipient's "Shared with you" section | Organization directory | Recipient's "Shared with you" section |
| **Can recipients remove it?** | Disable only           | Disable or delete                     | Disable only           | Disable only                          |
| **Requires owner approval?**  | Owner uploads directly | No                                    | No                     | No                                    |

**Important:** There's no approval workflow for org-wide sharing. If you enable **Share with organization**, any user can publish a skill to the directory without review. Consider enabling peer-to-peer sharing only if this is a concern.

### Monitor sharing activity

Skill sharing events are captured in the audit log and Compliance API as `role_assignment` events. You can see who shared a skill, with whom, and whether it was peer-to-peer, organization-wide, or group.

The audit log doesn't capture the contents of shared skills—only the share event itself. There's no admin dashboard to browse or inspect the contents of skills shared between users.

---

## How users see provisioned and shared skills

Skills appear for each user in **[Customize > Skills](https://claude.ai/customize/skills)**, organized into three sections:

- **Personal skills:** Skills the user has created or uploaded.

- **Shared with you:** Skills colleagues have shared directly with a user. These appear grayed out until enabled.

- **Organization skills:** Skills an owner has provisioned and skills users have shared organization-wide. Users install these from the directory.

Owner-provisioned skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

For more on how users browse and install from the directory, see **[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)**.

---

## Manage and remove provisioned skills

The **Organization skills** section in **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** displays all skills provisioned for your organization. Use search and the section headings to navigate them.

To remove a skill from your organization, locate it in the **Organization skills** list and select the option to remove it. Once removed, the skill will no longer appear in users' skills lists in **[Customize > Skills](https://claude.ai/customize/skills).**

**Note:** Only owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

---

## Scan skills and plugins for malicious content

On the Enterprise plan, you can turn on skill scanning for your organization. When it's on, Claude checks each third-party skill and plugin your users upload or edit for malicious content before it can run. Scanning is off by default, and it applies only to new uploads and edits, so skills and plugins already in your organization keep working.

To turn on skill scanning for your organization:

1. Go to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**.

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

- **Decide on sharing deliberately:** Organization-wide sharing has no approval step. If you want to review skills before they reach everyone, keep organization-wide sharing off and ask users to submit skills to an owner for provisioning instead.