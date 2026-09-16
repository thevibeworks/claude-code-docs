# Get started with Claude Docs

Claude Docs lets you write living documents with Claude and the people you work with. Ask for a doc in any conversation, and Claude drafts it in front of you, asks clarifying questions up front, and leaves comments explaining its choices. You can edit the doc yourself, ask Claude for the next pass, and share it by link, without moving your work into another tool.

This guide covers creating your first doc, editing it with Claude and your team, and sharing or exporting it when it's ready.

**[Create an artifact with Claude](https://claude.ai/artifacts)**

Claude Docs is available in beta on Pro, Max, Team, and Enterprise plans. It isn't available on the Free plan. It's on by default on Pro, Max, and Team plans, and you can turn it off in **[Settings > Capabilities](https://claude.ai/settings/capabilities)**. On Enterprise plans, Claude Docs is off by default until an owner turns it on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**. It isn't available yet for organizations that use customer-managed encryption keys (CMEK), zero data retention (ZDR), or a HIPAA-ready configuration.

## How Claude Docs works

A doc is a rich-text document saved to your Claude account. It can include headings, tables, and other formatting, and it can have more than one tab, like sections of a notebook. Every doc you create is saved in the **Artifacts** tab, so you can find it again from any conversation.

Claude starts from the context it already has. When you ask for a doc, Claude can draw on your files, memory, projects, skills, and the apps you've connected, so you don't start from a blank page.

The person who creates a doc is its owner. Anyone the owner shares it with can view or edit it. Claude works on a doc only when a signed-in person asks it to, and it can't do anything that person doesn't have permission to do. Every change is attributed to whoever made it, whether that's a person or Claude.

## Create a doc

### From a conversation

Ask Claude for a doc in any conversation. For example:

- "Turn the plan we just worked through into a product spec I can share with the team."

- "Draft this week's status report from my notes and last week's numbers."

- "Write an onboarding guide for new hires from the benefits deck in my Google Drive."

- "Pull my notes on this account into a one-page brief for tomorrow's call."

Claude asks a few questions before it starts, then drafts the doc on screen. You can also start your request with /docs, or by selecting “Output” then “Docs” from the message box.

### From the Artifacts tab

1. Go to the **[Artifacts](https://claude.ai/artifacts)** tab.

2. Select a Docs template from the gallery.

3. Describe the doc you want.

### Where you can create docs

You can ask for a doc wherever you talk to Claude:

- **Claude on web and desktop:** Ask in any conversation, or start from the Artifacts tab.

- **Claude Code:** Ask Claude to turn the session you're in into a spec, runbook, or readout. On desktop, the doc opens in the side panel. In the terminal, Claude gives you a link to open the doc on the web.

- **Claude app for iOS and Android:** Ask for a doc in any conversation and check back later for the result. Open it from the **Artifacts** tab to view it full screen. To start from a template, edit a doc, or change its sharing settings, use Claude on web or desktop.

### Tips for better results

A good request says what the doc is for, who will read it, and what it should cover. "A two-page launch brief for our sales team covering pricing, timing, and the top three customer questions" gets you further than "a launch brief." If the content lives somewhere specific, name the file or connected app Claude should use.

## Edit your doc

Nothing is locked while Claude works. You can edit alongside Claude at any time, and the final say is always yours.

### Edit directly

Click into the doc and type. Your changes save automatically and appear right away for everyone who has the doc open.

### Ask Claude

Ask for changes in the conversation, like "Tighten the intro and add a risks section." Claude edits the doc and tells you what changed.

### Use comments

Select text and leave a comment for your collaborators. To ask Claude for an edit, mention @Claude in a comment. Claude replies in the thread, makes the change, and explains what it did and why. Claude also leaves its own comments while drafting, to explain its choices or ask you a question.

### Add charts and visuals

Instead of pasting in screenshots, ask Claude to add a chart, diagram, graph, or timeline to your doc. Claude pulls the data from your connected apps and builds the chart in the doc. Charts and diagrams don't update on their own, even when the data comes from a connected app like Salesforce or Google Sheets. To refresh one, ask Claude to pull the latest data.

### Work on a doc with your team

People with edit access can work on the same doc at the same time as you and Claude, and everyone's edits appear in real time. Claude always acts with the permissions of the person who asked, so it can't edit a doc for someone who only has view access.

## Share a doc

Docs start private to you. To share one:

1. Open the doc.

2. Click "Share."

3. On Team and Enterprise plans, add the people or groups you want to share with, and choose whether each can view or edit.

4. Choose who else can open the doc: only the people you invite, everyone in your organization (Team and Enterprise plans), or anyone with the link (Pro and Max plans).

### Who you can share with

- **Team and Enterprise plans:** Invite specific people or a group, or share with everyone in your organization. Docs can't be shared outside your organization yet.

- **Pro and Max plans:** Share with anyone who has the link.

Opening a shared doc requires a Claude account.

### Access levels

- **Viewers** can read the doc.

- **Editors** can read, edit, comment on, and export the doc.

There's no comment-only access level yet. Only the owner can rename or delete a doc.

**Important:** Deleting a doc is permanent. There's no trash, and the doc becomes unavailable to everyone you shared it with after you delete it.

## Export a doc

To export a doc, click "Export" and choose a format:

- Word (.docx)

- PDF (.pdf)

- Markdown (.md)

- Google Docs

You can also ask Claude to turn a doc into a presentation with Claude Slides.

## Usage

Claude Docs counts toward your plan's usage limits, like the rest of your work with Claude. Larger requests, like drafting a long doc from several sources, use more of your limit than a typical message. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**.

## Turn on Claude Docs for your organization

This section is for Owners and Primary Owners on Team and Enterprise plans.

Claude Docs is in beta. It's on by default on Team plans and off by default on Enterprise plans. To turn it on:

1. Go to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Turn on **Docs**.

Claude Docs needs artifacts to be on for your organization. On Enterprise plans, you can turn on Claude Docs for specific groups instead of your whole organization, using the **Docs** capability (under **Artifacts**) in custom roles. People outside those groups can still open and work on docs shared with them, based on the access they're given.

A few other things admins should know:

- **Offboarding:** Removing someone from your organization, including through your identity provider, removes their access to docs at the same time.

- **Compliance API:** Events for the doc itself are recorded in the Compliance API activity feed. Activity inside a doc, like edits and comments, isn't recorded yet.

Learn more about **[sharing artifacts in your organization](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)**.

## Known limitations

Claude Docs is in beta. A few things to be aware of:

- **Version history:** Version history isn't available yet.

- **Access levels:** There's no comment-only access level.

- **Charts and diagrams:** Charts and diagrams don't update automatically. Ask Claude to pull the latest data from your connected apps.

- **External sharing:** On Team and Enterprise plans, docs can't be shared outside your organization.

- **Organization configurations:** Claude Docs isn't available yet for organizations using CMEK, ZDR, or a HIPAA-ready configuration.

- **Compliance logging:** Activity inside a doc, like edits and comments, isn't recorded in the Compliance API yet.

- **Mobile:** In the Claude app for iOS and Android, you can view docs, but you can't start from a template, edit, or change sharing settings.