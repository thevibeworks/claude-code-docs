# Use artifacts in Claude Cowork

We've recently updated live artifacts to an updated artifacts system. New artifacts created on or after August 19, 2026 use Claude's updated artifacts system: they're saved to your account, can be shared with people in your organization, and open on the web.

Live artifacts created before August 19, 2026 stay in the Artifacts view and keep working. You can still view them, but you can no longer edit them in place. Learn more in the section **[What happens to your existing live artifacts](#h_f13d109966)**.

Claude can build interactive artifacts in Cowork such as dashboards, trackers, reference pages, and comparison tools shaped around your work. New artifacts created in Cowork use Claude's updated artifacts system: they're saved to your account, can be shared with people in your organization, and open on the web. Every artifact you create is saved to the Artifacts view in your Cowork sidebar, marked with a "Cowork" label.

The updated artifacts system is generally available to Pro, Max, Team, and Enterprise plans on Cowork in Claude Desktop and Cowork in the cloud. Using Cowork on Claude Desktop requires the latest version of the app. Download or update at **[claude.com/download](http://claude.com/download)**.

If your organization uses customer-managed encryption keys (CMEK), zero data retention (ZDR), or a HIPAA readiness configuration, you'll keep using live artifacts. The updated artifacts system isn't currently available for these configurations.

---

## What’s new

Artifacts created on or after August 19, 2026 have the following new features:

- **Shareable.** Share an artifact with specific people or everyone in your organization.

- **Available on the web.** Open artifacts from the Artifacts view on Claude Desktop and the web.

- **Connected.** Artifacts can use your connected apps and ask Claude questions. Artifacts that use connected apps or ask Claude questions can only be shared within your organization.

- **Versioned.** Every update saves a new version. Share the latest version or a specific one.

---

## Create an artifact

There are two ways to create an artifact in Cowork: from a Cowork session or from the Artifacts view.

### From a Cowork session

Ask Claude to build what you need. A few examples:

- "Build me a dashboard that shows open tasks by project, pulling from Asana and Linear."

- "Create a tracker that monitors my top five competitors: recent releases, blog posts, pricing changes."

- "Put together a morning brief with my Slack mentions, today's calendar, and open pull requests."

When you describe the artifact, mention the connected apps or local files Claude should use. The result saves automatically to the Artifacts view.

### From the Artifacts view

1. Open Cowork and select "Artifacts" from the sidebar.

2. Click "New artifact" in the top right.

A new session opens with a starting prompt, and Claude asks a few questions about your connectors and what you want to build.

---

## Open and update an artifact

To reopen an artifact, select "Artifacts" from the Cowork sidebar and click the one you want. Use the "Filter by" dropdown at the top right to narrow the view.

To change an artifact you own, paste its link into any session or ask Claude to look up your artifacts, then ask Claude to make changes. Each change saves a new version. Open version history to compare an earlier version with the current one or restore it.

---

## Share an artifact

You can share an artifact with specific people, your organization, or, if enabled, anyone with the link.

1. Open the artifact you want to share.

2. Select "Share."

3. Choose who can view:

  1. Team and Enterprise plans can select: "Only people with access," "Everyone in your organization," or "Anyone with the link" (not available for artifacts that use connected apps or ask Claude questions). An Owner or Primary Owner needs to toggle on **External sharing** in **Organization settings > Artifacts** in order to select "Anyone with the link."

  2. Pro and Max plans can select: "Only you" or "Anyone with the link."

4. Choose the latest or a specific version, then copy the link. When you make changes, the link doesn't update until you select "Latest" under **Shared version**. A link to a specific version always shows that version. Viewers see it with their own access to connected apps.

How sharing works:

- **By default, sharing stays within your organization.** An Owner or Primary Owner can enable external sharing ("Anyone with the link") in **Organization settings › Artifacts**.

- **Shared artifacts use the viewer's access, not yours.** When someone opens your artifact, it connects to their connectors and data sources. If they don't have access to an underlying data source, that part of the artifact shows an error instead of your data.

- **Information stored in an artifact can be shared too.** Artifact creators can decide which information stored in an artifact is shared along with the artifact (like global items in a task tracker) and which are private to each user of the artifact (like personal to-dos). Before entering sensitive information, consider whether the artifact uses shared storage.

**Important:** Only open shared artifacts from people you trust. You're bringing someone else's code and content into your own conversation, so treat it the way you'd treat a file from an unknown sender. If you aren't sure about the source, don't use it.

---

## Example use cases

- **Persistent team dashboard:** A weekly metrics view that pulls from your connected analytics tools and spreadsheets. Built once, it pulls fresh data from your connected apps each time you open it (based on your own access).

- **Working project tracker:** A tracker pulling from Linear, Slack, and your calendar. Close the session, open it next week, and it pulls fresh data from your connected apps each time you open it (based on your own access).

- **Competitive intelligence:** A dashboard that tracks what your top competitors are shipping. Built in one session, updated from future sessions. Only the artifact's owner, and any editors they add (Team and Enterprise), can update it. Everyone else you share it with can view it but not edit it.

- **Morning brief:** A single page with your Slack mentions, today's calendar, and open pull requests. Open it each morning to see the current state.

---

## Current limitations

Before an artifact uses your connected apps, Claude shows which connectors and tools it will use and asks you to allow them. You can turn individual tools off and your choice is saved for that artifact until you change it. It doesn't prompt again for each call.

Each person who opens the artifact approves and uses their own connected apps, never the creator's. Connector tools that require per-action approval aren't available to artifacts.

---

## What happens to your existing live artifacts

You can no longer create live artifacts starting August 19, 2026. Live artifacts created before August 19, 2026 stay in the Artifacts view and keep working. You can still view them, but you can no longer edit them in place**.** To make changes, click "Share" on the live artifact and you'll have the option to republish it as a new artifact, which you can then edit like any other artifact.

If you already shared the live artifact, the republish dialog shows its existing link. Select select "Latest" under **Shared version** to publish the new version to that link. People who have the link see the new version without needing a new link.

Sharing a live artifact still works the way it always has:

- **Sharing stays within your organization.** There are no external or public links and no per-person recipient selection. Anyone in your organization who has the link can open the artifact.

- **Shared artifacts use the viewer's access, not yours.** When someone opens your artifact, it connects to their connectors and data sources. If they don't have access to an underlying data source, that part of the artifact shows an error instead of your data.