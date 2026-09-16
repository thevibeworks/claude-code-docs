# What are artifacts and how do I use them?

An artifact is anything Claude makes for you that you'd put in front of someone: a design, a deck, a document, a dashboard, or a small interactive tool. It opens beside your conversation, and you can edit it, come back to it, and share it with a link. Ask for one in any conversation with Claude, including in Claude Code, or pick a template in the **Artifacts** tab.

Artifacts are available on Free, Pro, Max, Team, and Enterprise plans, and in Claude Code on every plan that includes Claude Code. Claude Design, Claude Slides, and Claude Docs are in beta on paid plans only. They're on by default on Pro, Max, and Team plans, and off by default on Enterprise plans until an owner turns each one on. On the Free plan, you can still create artifacts in any conversation.

**Important:** We no longer support artifacts without **Code execution and file creation** enabled in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max) or **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** (Team, Enterprise).

---

## What are artifacts?

Claude creates an artifact when the content it's sharing meets these criteria:

- It is significant and self-contained, typically over 15 lines.

- It is something you're likely to want to edit, iterate on, or reuse outside the conversation.

- It represents a complex piece of content that stands on its own without requiring extra conversation context.

- It is content you're likely to want to refer back to or use later.

Common examples of artifact content include:

- Documents (Markdown or plain text)

- Code snippets

- Single-page HTML websites

- SVG images

- Diagrams and flowcharts

- Interactive React components

---

## Create designs, decks, and docs

Three tools help with work you'll share with others. Ask for a design, deck, or doc in any conversation, select “Output” in the message box and choose one, or pick a template in the **Artifacts** tab. Edit what Claude makes by talking to Claude or directly in the artifact, and it updates live as you work. When it's ready, share it with a link or export it. The final say is always yours.

- **Claude Design:** Visuals, mockups, prototypes, one-pagers, and landing pages, built with your design system. Learn more in **[Get started with Claude Design](https://support.claude.com/en/articles/14604416)**.

- **Claude Slides:** Presentations built from your notes, reports, or the work already in your conversation. Edit any slide directly, present without leaving Claude, and export to PowerPoint or PDF.

- **Claude Docs:** Living documents you write with Claude and your team in real time. Learn more in **[Get started with Claude Docs](https://support.claude.com/en/articles/16923645)**.

Claude Design, Claude Slides, and Claude Docs are in beta and available on paid plans. On Enterprise plans, they're off by default until an owner turns on **Design**, **Slides**, or **Docs** in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

In the Claude app for iOS and Android, you can ask for a design, deck, or doc in any conversation and view the result in the **Artifacts** tab. To start from a template, edit, or change sharing settings, use Claude on web or desktop.

**Note:** Artifacts count toward your plan's usage limits.

**[Create an artifact with Claude](https://claude.ai/artifacts)**

---

## Enable artifacts

To enable artifacts individually on a Free, Pro, or Max plan:

1. Click your initials or name in the lower left corner.

2. Navigate to **[Settings > Capabilities](https://claude.ai/settings/capabilities)**.

3. Toggle **Code execution and file creation** on.

To enable artifacts organization-wide on a Team or Enterprise plan:

1. Log in as an Owner.

2. Click your initials or name in the lower left corner.

3. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

4. Toggle **Code execution and file creation** on.

---

## Access your artifacts

You can access all your artifacts through the dedicated **[Artifacts](https://claude.ai/artifacts)** section in your Claude sidebar. This space allows you to:

- View all your creations in one organized location

- Start a new artifact from a template

- Manage and organize your artifact collection

**Note:** In the new Claude experience, everything you make is saved to the **Artifacts** tab automatically. If you have the previous chat experience, artifacts you create in a conversation don't appear there until you open the artifact and click "Publish."

---

## Work with artifacts

When Claude creates an artifact, you'll see the content displayed in a dedicated window to the right of the main chat.

### Edit and iterate

- Ask Claude to modify or update the artifact content.

- For Markdown documents, you can edit in place: highlight the text you want changed, click "Edit with Claude," and type your request. Claude makes the edit right where you marked it, so you don't have to describe which section you mean in the chat.

- Changes appear directly in the artifact window.

- Switch between different versions using the version selector.

- Your edits won't change Claude's memory of the original content.

- Edit prior chat messages to create a different version of the conversation, with its own set of artifacts—this lets you explore different directions without losing previous work.

**Note:** When Claude drafts content across multiple Markdown files, such as a skill or plugin, you can leave edit requests in several files before submitting. Each request is added to your next message, and the file list shows how many requests are waiting in each file. Send the message and Claude applies the whole batch in one pass.

### View and export

In the lower right corner of the artifact window, you can:

- View the underlying code of any artifact

- Copy content to your clipboard, including the code behind an artifact

- Download files to use outside the conversation

Copying the code is also how you build on an artifact someone else published. Learn more about **[building on a published artifact](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts#h_eb779b5c95)**.

### Multiple artifacts

- Open and work with several artifacts in one conversation

- Use the chat controls (slider icon in upper right) to switch between them

- Select which artifact you want Claude to reference for updates

### Fixing errors

If an artifact generates an error, look for the “Try fixing with Claude” button near the error message. Click the button to automatically copy the error details into a new message, then send it to Claude to diagnose the issue and suggest a fix.

**Note:** While Claude will attempt to fix the error, success isn't guaranteed. Some errors may require additional troubleshooting.

---

## AI-powered artifacts

You can build artifacts that embed AI capabilities, turning them into AI-powered apps. Users of your artifacts can access Claude's intelligence through a text-based API—answering questions, generating creative content, providing personalized coaching, playing games, solving problems, and adapting responses based on input.

### Create AI-powered artifacts

1. Describe what you want to Claude.

2. Claude writes the code.

3. The app runs on Anthropic's infrastructure.

4. Users authenticate with their Claude account and interact with their own instance of the artifact.

### How usage works

When you share AI-powered artifacts, others can use them immediately—no API keys required, and no costs to you. Whether your artifact helps 10 people or 10,000, sharing is free. Usage counts against each user's own Claude subscription limits, not yours.

For Team and Enterprise plans, when you share AI-powered artifacts within your organization, team members can use them without incurring additional costs to the creator.

---

## MCP integration

MCP integration for artifacts is available on Pro, Max, Team, and Enterprise plans on Claude web and desktop.

Artifacts can connect to external services through the Model Context Protocol (MCP), enabling interactive applications that read from and write to tools like Asana, Google Calendar, and Slack. In addition to Anthropic's official MCP integrations, artifacts can connect to any **[custom MCP servers](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)** you've configured.

When an artifact needs to access an MCP tool, you'll be prompted to approve access on first interaction. Your preferences persist for subsequent uses of that artifact.

**Important:** Each user must authenticate MCP servers independently, even when using shared or published artifacts. Organization admins can enable or disable artifact MCP access at the organization level but cannot manage which specific MCP servers artifacts can use.

---

## Persistent storage

Persistent storage for artifacts is available on Pro, Max, Team, and Enterprise plans on Claude web and desktop.

Artifacts can store data across sessions, enabling stateful applications like journals, trackers, and collaborative tools. Storage can be configured as either personal or shared:

- **Personal storage:** Each user maintains their own private data. For example, in a journal artifact, your entries remain visible only to you.

- **Shared storage:** All users see and interact with the same data. For example, in a game leaderboard, everyone sees the same scores and rankings.

When you interact with an artifact that uses shared storage for the first time, you'll see a confirmation dialog explaining that your data will be visible to other users of that artifact.

**Note:** Persistent storage is only available for published artifacts. During development and testing, storage operations will not succeed until the artifact is published.

**Storage specifications:**

- 20 MB storage limit per artifact

- Text-only input—no images, files, or binary data

- Personal and shared storage are isolated

- Unpublishing an artifact permanently deletes all associated storage data

**Privacy consideration:** Artifact creators determine which data uses personal versus shared storage when building the artifact. Before entering sensitive information, consider whether the artifact uses shared storage.

---

## Artifacts in Claude Code

Artifacts are available in Claude Code on every plan that includes Claude Code.

Claude Code can publish its session output as an artifact—a live, interactive page at a private URL. The page updates in place as your session continues, and you can share it with others. An artifact might be a pull-request walkthrough with annotated diffs, a dashboard built from session data, or an investigation timeline that fills in as Claude works.

By default, artifacts in Claude Code are visible only to the person who created them.

- **Team and Enterprise plans:** Share them with people in your organization. Sharing with anyone who has the link requires an owner to turn on **External sharing** in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

- **Pro and Max plans:** Share them with anyone who has the link.

You can also make designs and docs from Claude Code. Use /design for Claude Design, or ask for a doc. On desktop, the doc opens in the side panel. In the terminal, Claude gives you a link to open it on the web.

To learn how to create, update, and share artifacts in Claude Code, see the **[artifacts documentation on Claude Code Docs](https://code.claude.com/docs/en/artifacts)**.

---

## Learn more

To share your artifacts publicly, embed them on websites, or discover artifacts created by others, see **[Publish and share artifacts](https://support.claude.com/en/articles/9547008)**.