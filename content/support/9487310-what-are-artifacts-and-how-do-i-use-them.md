# What are artifacts and how do I use them?

Accessing artifacts in the sidebar and Claude-powered artifacts are supported on Free, Pro, Max, Team, and Enterprise plans. Artifacts are available in Claude Code on Team and Enterprise plans.

Artifacts allow you to turn ideas into shareable apps, tools, or content—build tools, visualizations, and experiences by simply describing what you need. Claude can share substantial, standalone content with you in a dedicated window separate from the main conversation. This makes it easy to work with significant pieces of content that you may want to modify, build upon, or reference later.

**Important:** We no longer support artifacts without **Code execution and file creation** enabled in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max) or **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** (Team, Enterprise).

Artifacts are available in Claude, Claude Desktop, and Claude Code. This article focuses on Claude and Claude Desktop. To learn how to create, update, and share artifacts in Claude Code, see the **[artifacts documentation on Claude Code Docs](https://code.claude.com/docs/en/artifacts)**.

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

- Create new artifacts from scratch or by customizing existing ones

- Manage and organize your artifact collection

**Note:** Artifacts you create in a conversation don't appear in your sidebar automatically. To add an artifact to your **Artifacts** section, open it and click "Publish." Learn more about **[publishing and sharing artifacts](https://support.claude.com/en/articles/9547008)**.

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

- Copy content to your clipboard

- Download files to use outside the conversation

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

Artifacts are available in Claude Code on Team and Enterprise plans.

Claude Code can publish its session output as an artifact—a live, interactive page at a private URL. The page updates in place as your session continues, and you can share it with people in your organization. An artifact might be a pull-request walkthrough with annotated diffs, a dashboard built from session data, or an investigation timeline that fills in as Claude works.

By default, artifacts in Claude Code are only visible to the individual who created them. They can choose to share artifacts with the rest of their organization, and they can’t be shared publicly.

To learn how to create, update, and share artifacts in Claude Code, see the **[artifacts documentation on Claude Code Docs](https://code.claude.com/docs/en/artifacts)**.

---

## Learn more

To share your artifacts publicly, embed them on websites, or discover artifacts created by others, see **[Publish and share artifacts](https://support.claude.com/en/articles/9547008)**.