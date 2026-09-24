# Artifacts admin guide for Team and Enterprise plans

This guide is for Owners and Primary Owners of Team and Enterprise plans, and explains how to turn on artifacts for your organization, choose which templates users can start from, control who has access, and manage whether or not artifacts can be shared outside your organization.

## Turn on artifacts for your organization

To change organization settings, you need to be an Owner or Primary Owner, or in a custom role (Enterprise plans) with the appropriate admin permissions.

1. Turn on “Cloud code execution and file creation” in Organization settings > Capabilities first.

2. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

3. Turn on **Artifacts**.

This lets users create and publish artifacts to a shareable Anthropic-hosted page, and share artifacts within your organization.

**Important:** Turning **Artifacts** off stops users from sharing artifacts with your organization. Links they already shared keep working.

## Choose which templates users can start from

Templates are the starting points users pick when they create an artifact.

| **Template**   | **What users can do with it**                                                                |
| -------------- | -------------------------------------------------------------------------------------------- |
| Slides         | Start decks they can present, restyle with a design system, and export to PowerPoint         |
| Design         | Lay out screens, flows, and graphics as artboards they can edit by hand                      |
| Design systems | Capture colors, fonts, and components once so Claude applies them to new decks and designs   |
| Docs           | Start docs their team reads, comments on, and edits in place while Claude keeps them current |

**To enable a template:**

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Under **Templates**, turn on the templates you want to make available.

**Note:** Turning a template off doesn't impact artifacts users already made using that template.

### Standalone Claude Design at claude.ai/design

Standalone Claude Design is a separate product from the **Design** template, and it has its own setting in **[Organization settings > Claude Design](https://claude.ai/admin-settings/claude-design)**. Turning one on doesn't turn on the other. Users' existing projects stay at **claude.ai/design** and also appear in the **Artifacts** tab.

---

## Manage sharing outside your organization

Two separate settings control what users can share outside your organization. Turning on one doesn't turn on the other. For what users see and which artifacts can't leave your organization, see **[Share artifacts](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)**.

### External sharing

**External sharing** lets users share artifacts with anyone who has the link.

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Turn on **External sharing**.

**Important:** Turning **External sharing** off also stops existing public links from working until you turn it back on, except for artifacts you allow individually.

### Allow external sharing for a single artifact

While **External sharing** is off, you can still let a specific artifact be shared with anyone who has the link.

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Under **Published artifacts**, find the artifact. It must already be shared with your organization or invited people to appear here.

3. Open the artifact's menu and select "Allow external sharing."

4. Confirm by selecting "Allow external sharing."

The artifact's owner can then share it with anyone who has the link. **External sharing** stays off for every other artifact in your organization.

### Email invitations outside your organization

**Email invitations outside your organization** lets users invite specific people outside your organization to an artifact by email. It's a separate setting from **External sharing**, so turning on one doesn't turn on the other.

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Turn on **Email invitations outside your organization**.

**Important:** Turning **Email invitations outside your organization** off blocks access for people users already invited, until you turn it back on. Accepted invitations aren't deleted, and pending ones still expire 30 days after they were sent.

### See and remove outside access

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Under **Published artifacts**, find an artifact marked **Shared outside**.

3. Open the artifact's menu and select "Manage outside access."

4. Select the remove button next to the person, then confirm with "Remove access" or "Remove invitation."

Owners can remove people here but can't change their access level.

### What stays inside your organization

Some artifacts can't leave your organization even with these settings on:

- Docs can't be shared outside your organization yet.

- Artifacts that use connected apps, or that ask Claude questions, can't use “Anyone with the link.”

People need a Claude account to open any artifact except a legacy artifact published from chat.

Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**.

---

## Let users see who else has an artifact open

**Artifact presence** lets users see who else in your organization has an artifact open, along with live activity in it. Turn it on or off in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

It's on by default on Team and Enterprise plans, and it only applies while **Artifacts** is on for your organization.

**Note:** Turning **Artifact presence** off applies to new page loads right away, and to tabs that are already open within an hour.

---

## Let artifacts use connected apps

**Enable artifact connectors** lets users work with artifacts that read from and write to their connected apps. Each user connects their own apps, even in a shared artifact. You can turn this on or off for your whole organization, but you can't limit which apps artifacts can reach.

1. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

2. Under **Visuals**, turn on **Enable artifact connectors**.

---

## Limit access to specific groups on Enterprise plans

On Enterprise plans, custom roles let you turn a feature on for specific groups instead of your whole organization. The organization setting is the main switch, and custom roles are the per-user switches underneath it. If a feature is off at the organization level, no custom role can grant access to it.

The capabilities that cover artifacts are:

| **Capability**             | **What it grants**                                                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Artifacts                  | Creating and publishing artifacts from Claude Code and Cowork, and sharing chat and Cowork artifacts within the organization |
| Design                     | Starting artifacts from the Design template                                                                                  |
| Design systems             | Creating and editing design systems                                                                                          |
| Docs                       | Starting artifacts from the Docs template                                                                                    |
| Slides                     | Starting artifacts from the Slides template                                                                                  |
| Claude Design [standalone] | Access to standalone Claude Design at claude.ai/design                                                                       |

Users outside those groups can still open, comment on, and use artifacts shared with them.

Learn more about **[managing custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)** and **[setting up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458)**.

---

## Manage your organization's design systems

Design systems shared with everyone in your organization are listed in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**, under **Design systems**, with their owner and when they were last updated. Users see these when they start a new artifact, and the default is preselected.

### Restrict who can manage design systems

By default, any user with access to design systems can publish one, set the organization default, and delete design systems. On Enterprise plans using custom roles, the **Claude Design Admin** permission reserves these actions for specific users, so your organization keeps one authoritative set of design systems.

Users in custom roles with the permission set to “Can manage” can:

- **Publish a design system:** make it available across your organization so anyone can attach it to a project.

- **Set the organization default:** choose the design system new artifacts use automatically.

- **Delete a design system:** permanently remove it from your organization.

Everyone else can still create, edit, and use any published design system. If a user without the permission tries to publish, set the default, or delete, they'll see a note directing them to contact their administrator.

**Note:** If you don't assign this permission to anyone, nothing changes. All users keep the same access to design systems as before.

**To grant the permission:**

1. Navigate to **[Organization settings > Roles](https://claude.ai/admin-settings/roles)** and create or edit a custom role.

2. In the “Admin permissions” tab, find **Claude Design Admin** under **Product admin** and set it to “Can manage.”

3. Assign the role to a group. Users in that group inherit the permission.

4. Set each user's role to “Custom.”

Learn more about **[setting up your design system](https://support.claude.com/en/articles/14604397)**.

---

## Usage and billing

Artifacts, including designs, decks, and docs, count toward each user's existing usage limits, shared with the rest of Claude, including Claude Code. There's no separate allowance to provision.

- **Team and seat-based Enterprise plans:** Usage draws from each user's seat usage limits, including session and weekly limits. Admins can purchase **[usage credits](https://support.claude.com/en/articles/12005970)** for users who need more.

- **Usage-based Enterprise plans:** Usage bills from your organization's consumption at standard API rates. Organization, group, and per-user spend limits apply.

## Monitor usage

- **Compliance API:** Artifacts made in conversations and the **Artifacts** tab are recorded at the artifact level. For docs, events for the doc itself are recorded, but activity inside a doc, like edits and comments, isn't recorded yet.

- **Analytics:** Navigate to **[Analytics > Claude Design](https://claude.ai/analytics/claude-design)** for daily, weekly, and monthly active users. These analytics cover claude.ai/design only, and don't include designs made in conversations or the **Artifacts** tab.

- **Audit logs:** Standalone Claude Design doesn't support audit logs.

Learn more about **[viewing usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420)**.

---

## Data handling and privacy

When users create designs and docs, they may upload design assets, brand guidelines, screenshots, and other materials.

- Uploaded assets are stored persistently, and fall under the same **[data retention and deletion policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** as other Anthropic products for organizations.

- Claude Design doesn't currently support data residency requirements.

### When someone leaves your organization

Removing someone from your organization, including through your identity provider, removes their access to artifacts at the same time.

### Organizations with special configurations

- **CMEK, ZDR, or a HIPAA-ready configuration:** The new artifacts experience, including templates, design systems, and email invitations, isn't available yet. These organizations keep using live artifacts in Cowork.

- **Education and K-12 organizations:** Email invitations aren't available.

---

## Third-party platform availability

Artifacts are available in Claude on web and desktop, in Claude Code, and at claude.ai/design for standalone Claude Design. In Claude for iOS and Claude for Android, users can ask for an artifact and view the result. Artifacts aren't available through third-party cloud platforms.

---

## Frequently asked questions

### Do I need to turn a feature on for the whole organization if only some users need it?

Yes. The organization setting must be on before custom roles can control per-user access. If a feature is off at the organization level, no one can use it regardless of their role.

### Can I restrict templates to specific departments?

Yes, on Enterprise plans, with custom roles. Each template has its own capability, and standalone Claude Design has a separate capability from the **Design** template.

### What's the difference between external sharing and email invitations?

**External sharing** lets users publish an artifact that anyone outside your organization can open with a link. **Email invitations outside your organization** lets users invite named people outside your organization to a specific artifact. Each has its own setting.

### Who can publish, set the default, or delete design systems?

If you haven't assigned the **Claude Design Admin** permission to anyone, any user with access to design systems can take these actions. On Enterprise plans, you can reserve them for specific users.

### Can users export what they make?

Yes. For more information, refer to **[View and export](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them#h_71205f2c4b)** in **[What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310)**