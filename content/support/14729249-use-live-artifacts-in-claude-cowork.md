# Use live artifacts in Claude Cowork

This article explains how to use live artifacts in **[Claude Cowork](https://claude.com/product/cowork)**. Live artifacts are persistent, interactive HTML dashboards that Claude builds for you. They refresh with current data from your connected apps and appear alongside your chat artifacts in the Artifacts view on Claude Desktop.

## Availability

Live artifacts are available on paid Claude plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

- **Claude Desktop for Windows**

- **Claude Desktop for Linux (beta)**

Using Cowork on Claude Desktop requires the latest version of the app. Download or update at **[claude.com/download](https://claude.com/download)**.

**Note:** Live artifacts are available on the desktop app only. They don't appear in the Artifacts view on web or mobile.

---

## What are live artifacts?

A live artifact is a persistent, interactive HTML page that Claude creates for you in Cowork, shaped around your specific work. It might be a tracker, a dashboard, a comparison tool, or a reference. Every live artifact you create is saved to the Artifacts view in your Cowork sidebar, marked with a "Cowork" label.

Live artifacts differ from **[artifacts in chat](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)** in a few ways:

- **They live on their own.** You don’t have to find the chat they came from. Every live artifact shows up in the “Live artifacts” tab in your Cowork sidebar.

- **They refresh with current data.** When you open a live artifact, it can pull from your connected apps and local files so the view reflects today, not the day it was built.

- **They keep their history.** Each update saves a version. You can review how the artifact has evolved and restore an earlier version.

Artifacts you create in chat and in Cowork appear together in the Artifacts view. Live artifacts show a "Cowork" label so you can tell them apart from chat artifacts, and because they're desktop-only, they appear in the Artifacts view on Claude Desktop only.

---

## Create a live artifact

There are two ways to create a live artifact in Cowork.

### From a Cowork task

Ask Claude to build what you need. A few examples:

- “Build me a dashboard that shows open tasks by project, pulling from Asana and Linear.”

- “Create a tracker that monitors my top five competitors: recent releases, blog posts, pricing changes.”

- “Put together a morning brief with my Slack mentions, today’s calendar, and open pull requests.”

When you describe the artifact, mention the connected apps or local files Claude should use. The result saves automatically to the Artifacts view.

### From the Artifacts view

1. Open Cowork on Claude Desktop and select "Artifacts" from the sidebar.

2. Click “New artifact” in the top right.

3. Select "Create Cowork artifact."

A new session opens with a starting prompt, and Claude asks a few questions about your connectors and what you want to build.

**Note:** In the Artifacts view, live artifacts are labeled "Cowork."

---

## Open and refresh an artifact

To reopen an artifact, select "Artifacts" from the Cowork sidebar and click the one you want. Use the "Filter by" dropdown at the top right to narrow the view.

When you open a live artifact, it pulls fresh data from your connected apps. Most of the time you won’t need to refresh manually, as a short cache holds recent data so the artifact loads quickly, and it re-queries your connected apps on its own. If you want to force new data, use the refresh button in the artifact’s header.

---

## Version history

Each time you iterate on a live artifact with Claude, the previous version is saved. Open the artifact’s version history to:

- See how the artifact has changed over time.

- Compare an earlier version with the current one.

- Restore an earlier version if an update didn’t work out.

---

## Share a live artifact

Sharing live artifacts is available on Team and Enterprise plans. On Pro and Max plans, live artifacts can't be shared or published.

You can share a live artifact with other people in your Claude organization:

1. Open the artifact you want to share.

2. In the artifact's header, click the "Share" button

3. Click "Share & copy link" and copy the link.

4. Send the link to people in your organization. The artifact opens in the Claude Desktop app.

If someone shares a live artifact with you, open the link on a computer with Claude Desktop installed. You can also click "Import from link" at the top of the Artifacts view and paste the link.

How sharing works:

- **Sharing stays within your organization.** There are no external or public links and no per-person recipient selection. Anyone in your organization who has the link can open the artifact.

- **Shared artifacts use the viewer's access, not yours.** When someone opens your artifact, it connects to their connectors and data sources. If they don't have access to an underlying data source, that part of the artifact shows an error instead of your data.

---

## Example use cases

- **Persistent team dashboard:** A weekly metrics view that pulls from your connected analytics tools and spreadsheets. Built once, refreshed every time you open it.

- **Working project tracker:** A tracker pulling from Linear, Slack, and your calendar. Close the session, open it next week, and it's refreshed with current data.

- **Competitive intelligence:** A dashboard that tracks what your top competitors are shipping. Built in one session, updated from any future thread.

- **Morning brief:** A single page with your Slack mentions, today’s calendar, and open pull requests. Open it each morning to see the current state.

---

## Current limitations

- **Local, not remote.** Live artifacts live on your computer. If you switch devices, they don’t come with you.

- **Live artifacts use your connectors without asking.** Live artifacts can only use the connectors you approved during creation or update. However, artifacts don't ask for permission before using connectors, even if your session mode would normally require approval. Use care when creating live artifacts that use connectors that can make changes to your data.