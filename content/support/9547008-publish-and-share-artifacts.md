# Publish and share artifacts

Artifacts let you make things with Claude, like dashboards, apps, designs, decks, and docs, and share them with others. How you share an artifact depends on where you made it:

- **Artifacts you share from the "Share" dialog** include everything you make in the new Claude experience and everything you make with Claude Design, Claude Slides, Claude Docs, or Claude Code. If you're still on the previous experience, this also covers artifacts made in Claude Cowork on or after August 19, 2026. Everyone who opens these artifacts needs a Claude account.

- **Artifacts you publish or share by link from chat** are artifacts made in chat on the previous experience. They're shared with "Publish" (Free, Pro, and Max plans) or "Share & copy link" (Team and Enterprise plans).

The new Claude experience is rolling out gradually to Pro and Max plans. If your message box still shows "Chat" and "Cowork" options, you're on the previous experience, and artifacts you make after selecting "Chat" are chat artifacts. Learn more in **Claude Cowork and chat are one Claude**.

Live artifacts made in Claude Cowork before August 19, 2026 have their own sharing rules. Learn more in **Use artifacts in Claude Cowork**.

**Important:** To use artifacts, you need to enable **Code execution and file creation** in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max) or **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** (Team, Enterprise).

---

## Share an artifact

Artifacts start private to you. To share one:

1. Open the artifact.

2. Click "Share."

3. On Team and Enterprise plans, add specific people or groups and choose their access.

4. Choose who else can open it:

  - **Team and Enterprise plans:** "Only people with access," "Everyone in your organization," or "Anyone with the link"

  - **Pro and Max plans:** "Only you" or "Anyone with the link"

5. Choose whether the link shows the latest version or a specific one, then copy the link. If you share the latest version, people with the link see your changes when you make them.

### Access levels

- **Claude Docs:** View or edit.

- **Claude Design and Claude Slides:** View, comment, or edit.

- **Other artifacts:** View or edit.

### Who can open a shared artifact

- **A Claude account is required.** People without a Claude account can't open or interact with a shared artifact, even if they have the link.

- **Everyone in your organization:** Only people signed in to your organization can open it.

- **Anyone with the link:** On Enterprise plans, an Owner or Primary Owner must turn on **External sharing** first. This option isn't available for artifacts that use connected apps or ask Claude questions. On Team and Enterprise plans, it isn't available for Claude Docs yet.

### What people see when they open your artifact

- **Viewers use their own access.** An artifact that pulls from connected apps uses the viewer's connections, not yours. If a viewer can't access a data source, that part of the artifact shows an error instead of your data.

- **Stored information can be shared.** Some artifacts save information that everyone who opens them can see, like items in a shared tracker. Before you enter sensitive information, check whether the artifact uses shared storage.

**Important:** Only open shared artifacts from people you trust. Treat someone else's artifact the way you'd treat a file from an unknown sender.

Publishing, embed codes, and copying an artifact's code are available only for artifacts made in chat. You can't change sharing settings in the Claude app for iOS and Android.

---

## Publish artifacts made in chat

Publishing is available on Free, Pro, and Max plans, for artifacts made in chat in the previous experience.

**To publish an artifact:**

1. Navigate to the artifact you want to publish.

2. Ensure you're on the correct artifact version.

3. Click the “Publish” button.

4. Copy the public link to share with others.

Publishing adds the artifact to the **[Artifacts](https://claude.ai/artifacts)** section in your sidebar so you can find it again outside the original conversation.

### Who can open published chat artifacts

This applies only to artifacts published from chat. Everyone who opens an artifact shared from the **Share** dialog needs a Claude account.

**Non-users:**

- View and interact with any published artifact without signing up.

- Try all basic functionality without a Claude account.

- Prompted to sign up only for advanced features like using AI-powered capabilities.

**Claude users (Free, Pro, Max):**

- Full access to view, interact with, and copy any published artifact.

- Can use AI-powered features within their usage limits.

- Can save and organize artifacts they discover.

### Embed artifacts

After publishing, you'll see a “Get embed code” button.

Click it to open a modal with automatically generated code you can copy and paste to embed your artifact on another website.

You must specify which websites can embed your artifact by entering URLs in the **Allowed domains** field, separated by commas.

### Unpublish artifacts

After publishing an artifact, an “Unpublish” button appears, giving you the option to revoke access.

**Important:** Once you unpublish an artifact, you cannot publish that same artifact again. You'll need to create a new artifact if you want to publish it later. Unpublishing also permanently deletes all associated storage data (both personal and shared) if the artifact used persistent storage.

### Build on a published artifact

Building on a published artifact is available on Free, Pro, and Max plans, for artifacts published from chat

If someone publishes an artifact you like, you can use it as a starting point for your own version. Copy the code into a new chat and ask Claude to make the changes you want. Your version is separate from the original, so nothing you do affects the artifact you started from.

**Important:** Only do this with artifacts from people you trust. You're bringing someone else's code and content into your own conversation, so treat it the way you'd treat a file from an unknown sender. If you aren't sure about the source, don't use it.

**To build on a published artifact**

1. Open the published artifact and click “Copy” to copy the code to your clipboard.

2. Start a new chat, paste the code, and describe the changes you want. For example: "Here's the code for a quiz game. Can you change the questions to be about movies and add a timer?"

3. Claude creates a new artifact with your changes. Refine it from there the same way you would any artifact you made yourself.

**What happens when you build on an artifact**

- The code you paste becomes the starting point for a new artifact in your own chat.

- You can modify it, expand on it, or use it as inspiration.

- Your changes don't affect the original. You're working on your own copy.

---

## Share chat artifacts on Team and Enterprise plans

Internal sharing is available on Team and Enterprise plans.

On Team and Enterprise plans, you can share artifacts only within your organization by default. An owner can turn on **External sharing** so users can share artifacts with anyone who has the link.

**To share an artifact:**

1. Navigate to the artifact you want to share.

2. Ensure you're on the correct artifact version.

3. Click the “Share” button.

4. Click “Share & copy link” to make this version shareable.

### Who can access shared artifacts

- Users in your Team or Enterprise organization, plus anyone with the link if the artifact is shared with "Anyone with the link." This option requires **External sharing** to be on.

- Viewers must sign in with a Claude account. For artifacts shared only within your organization, that's their Team or Enterprise account.

- If the artifact was created from a project, viewers must also have access to that project.

### Share artifacts with attachments

When you share an artifact made in chat, viewers also get access to any attachments and files in the conversation that created it. Consider this before sharing artifacts from conversations that contain sensitive documents.

### Unshare artifacts

**To unshare an artifact:**

1. Click the “Share” button in the upper right corner of the artifact.

2. In the **Artifact shared** modal, click “Unshare.”

### Turn on external sharing

On Enterprise plans, Owners and Primary Owners can let users share artifacts outside the organization:

1. Go to **Organization settings > Artifacts**.

2. Turn on **External sharing**.

External sharing applies to artifacts made in chat, in the new Claude experience, in Cowork, and in Claude Code. Claude Docs can't be shared outside your organization yet, and neither can artifacts that use connected apps or ask Claude questions. Even with External sharing on, people need a Claude account to open any artifact except one published from chat.

**Important:** If you turn External sharing off later, existing public links stop working until it's turned back on.

---

## Learn more

For information about creating artifacts, AI-powered capabilities, MCP integration, and persistent storage, see **[What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)**