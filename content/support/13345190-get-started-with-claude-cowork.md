# Get started with Claude Cowork

This article explains how to use **[Claude Cowork](https://claude.com/product/cowork)**, which brings Claude Code's agentic capabilities to knowledge work beyond coding.

## Availability

Claude Cowork is available for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS** — **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows** —  Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](http://claude.com/download)**.

- **Web**, at claude.ai

- **Claude Mobile**, in the latest version of Claude for iOS and Claude for Android

Chat and Cowork share one home, so you start both from the same place. On any surface, find the message box and select "Cowork," then describe your task. To go back to a regular conversation, select "Chat."

Claude Cowork is in beta on web and mobile, and rolling out over the next several weeks starting with the Max plan, with more plans to follow.

---

## What is Claude Cowork?

Claude Cowork uses the same agentic architecture that powers Claude Code, with no terminal required. Instead of responding to prompts one at a time, Claude can take on complex, multi-step tasks and execute them on your behalf.

With Cowork, you can describe an outcome, step away, and come back to finished work—formatted documents, organized files, synthesized research, and more. Cowork runs your sessions remotely (in beta), so your sessions and files live with your Claude account and follow you across desktop, web, and mobile. Chat and Cowork now share one home, so handing Claude a task starts from the same message box as a conversation. With scheduled tasks, Claude can complete work for you automatically. With projects, you can organize related tasks into persistent, self-contained workspaces with their own files, links, instructions, and memory.

**Important:**

- Cowork has unique risks due to its agentic nature and internet access.

- Cowork respects your current network egress permissions.

  - **Important:** Network egress permissions don't apply to the web fetch or **[web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)** tools or MCPs, including Claude in Chrome. Web fetch runs server-side and is limited to search results and URLs you've shared.

  - Team or Enterprise plan owners can turn off web search for Cowork and Chat in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**, or Claude in Chrome via **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension).**

- You control your Cowork tasks and can delete a task at any time using the "Delete" option (click "⋮" next to the task, or select tasks from your Tasks list and click the trash icon). Your Cowork task will be removed from your task history immediately, and deleted from our backend storage systems within 30 days, in accordance with our **[data retention periods](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

- Cowork activity is not captured in the Compliance API at this time.

- If you're a Team or Enterprise plan admin, you can **[use OpenTelemetry (OTel) to monitor Claude Cowork activity](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)** across your organization.

- Please review **[Use Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)** for more information.

For important limitations and considerations for Team and Enterprise organizations using Cowork, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)**.

### Key capabilities

- **Work from anywhere:** Remote sessions follow your Claude account. Start a task on one surface, steer it from another, and pick up the finished output wherever you are. See **[Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349)**.

- **Work that continues without you:** In remote sessions, Claude keeps working when you close your laptop or step away.

- **Direct local file access:** On desktop, Claude can read from and write to your local files without manual uploads or downloads.

- **Sub-agent coordination:** Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them.

- **Professional outputs:** Generate polished deliverables like Excel spreadsheets with working formulas, PowerPoint presentations, and formatted documents.

- **Edit drafts in place:** When Claude drafts a Markdown document, highlight the text you want changed, click "Edit with Claude," and type your request. Claude makes the edit right where you marked it, with no need to describe the section in your task thread.

- **Long-running tasks:** Work on complex tasks for extended periods without conversation timeouts or context limits interrupting your progress.

- **Scheduled tasks:** Create and save tasks that you can have Claude run on-demand or automatically on a cadence of your choosing. Scheduled tasks run remotely, with no device online.

- **Spreadsheets and presentations:** Cowork can produce spreadsheets and slides that can be further edited with Claude for Excel and Powerpoint.

- **Projects:** Group related tasks into separate workspaces with their own files, context, instructions, and memory. See **[Organize your tasks with projects in Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork).**

- **Browser actions:** Claude can open Chrome and work on websites—clicking, typing, navigating, and filling forms—for tasks that touch websites. See **[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)**.

---

## How Claude Cowork runs your tasks

Cowork runs your tasks remotely (in beta). Claude's work runs on Anthropic's servers, in an isolated environment, and your sessions and files are saved to your Claude account. Work continues if you close your laptop, and you can open the same session from any surface.

When a task needs something on your computer, like a local file or your browser, Claude reaches it through the Claude Desktop app on that computer. When you start a task in Cowork, Claude:

1. Analyzes your request and creates a plan.

2. Breaks complex work into subtasks when needed.

3. Runs code and shell commands in an isolated environment on Anthropic's servers.

4. Coordinates multiple workstreams in parallel if appropriate.

5. Delivers finished outputs to your session, where you can preview and download them.

You maintain visibility into what Claude is planning and doing throughout the process so you can steer when it matters, or let Claude run independently.

---

## Get started

### Requirements

- **Paid Claude subscription:** Cowork is available to paid Claude plans (Pro, Max, Team, Enterprise) only.

- **For local file access, browser use, and computer use:** The **[Claude Desktop app](https://support.claude.com/en/articles/10065433-installing-claude-desktop)** for macOS or Windows, open and connected. These capabilities reach things on your computer, so they need the app even though your session runs remotely.

- **Active internet connection:** Required throughout the session.

## Start a Cowork session

Chat and Cowork share one home. To start a session on any surface:

1. Open Claude on the web at claude.ai, in the Claude Desktop app, or in the Claude mobile app.

2. In the message box, select "Cowork."

3. Describe the task you want Claude to complete.

4. Review Claude's approach, then let it run.

**Note:** Sessions keep running even when the desktop app is closed or your computer is asleep. If your task uses local files, your browser, or your computer, keep the desktop app open so Claude can reach them.

## What to expect during a task

When Claude is working on a task in Cowork:

- **Progress indicators** show what Claude is doing at each step.

- **Transparency:** Claude surfaces its reasoning and approach so you can follow along.

- **Steering:** You can jump in to course-correct or provide additional direction mid-task.

- **Check in from anywhere:** Open the same session on another surface to monitor progress, answer Claude's questions, or redirect the work.

- **Parallel work:** For complex tasks, Claude may coordinate multiple sub-agents working simultaneously.

- **Deletion protection:** When using Cowork, Claude requires your explicit permission before permanently deleting any files. You will see a permission prompt and will need to select "Allow" before Claude is allowed to perform deletion tasks.

Tasks can run for extended periods depending on complexity. You can monitor progress or step away and return when Claude finishes.

---

## Choose how Claude checks with you

Cowork has three modes that control when Claude asks your permission before taking an action, like using your connectors. You can change the mode at any time from the mode selector in the chat box.

|                   | **Connector tool permission: "Always allow"**                          | **Connector tool permission: "Needs approval"** | **Connector tool permission: "Blocked"** |
| ----------------- | ---------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| **"Manual" mode** | Approved                                                               | Asks for permission                             | Denied                                   |
| **"Auto" mode**   | Read-only tools are approved<br>For write/delete tools, Claude decides | Claude decides                                  | Denied                                   |
| **"Skip" mode**   | Approved                                                               | Approved                                        | Denied                                   |

As a reminder, you control which connectors Claude can use via the + menu in the chat box or the **[Customize > Connectors](https://claude.ai/customize/connectors)** page.

**Note:** On Team and Enterprise plans, your organization may require per-task approval for write-capable connector tools, so "Always allow" preferences may not apply. See **[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans#h_1bd1fa754d)**.

**Manually approve (Manual)**, formerly "Ask before acting." Claude pauses and asks for approval for actions. You review each request and choose Allow or Deny.

**Automatically approve (Auto).** Claude keeps working without stopping to ask about every step. Instead, Claude reviews each action for safety (such as checking for data exfiltration or **[prompt injection](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)**) and automatically blocks anything it determines to be unsafe. When an action is blocked, Claude looks for a safer way to finish the task or pauses and asks you directly. If Claude keeps running into blocks, it switches back to asking your permission for each step.

We tested Claude's safety check extensively before releasing it, including working with outside security experts who tried to sneak dangerous actions past it. It gives you the speed of letting Claude work without interruptions, with a layer of protection that "Skip all approvals" doesn't have: every action still gets reviewed before it happens. *Of course, no defense is perfect and no mode replaces your judgment. For work with real consequences—money, messages sent as you, important files—stay close and review what Claude does or consider switching back to "Manually approve."*

Auto mode applies to all of your existing connectors, plugins, Claude in Chrome, and some Cowork actions like fetching websites. Auto mode won't approve certain sensitive actions like allowing Cowork to access additional folders on your computer, allowing Cowork to delete files in a given folder it has access to, creating scheduled tasks, and others. Because Claude does this extra checking for you, **auto mode consumes more of your usage limit than the other modes**.

**Skip all approvals (Skip)**, formerly "Act without asking." Claude doesn't pause to ask and nothing checks its actions automatically. Only use this when you completely trust every action, connector, file, app, etc. involved in the task.

---

## Add global and folder instructions

### Global instructions

You can give Claude standing instructions that apply to every Cowork session. Use this to specify your preferred tone, output format, or background on your role.

To set global instructions:

1. Navigate to **[Settings > Cowork](https://claude.ai/settings/cowork)**.

2. Click "Edit" next to **Global instructions**.

3. Type your instructions in the text box and click "Save":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2525926874/15324ac4155d7802272e8bdef04b/ec66cd09-a4db-4f1d-8f30-226c9d126333?expires=1784481300&amp;signature=5e0e60801f3c6bf27dc47275d2387374da01022227f80cf1f5809e9b7b5313de&amp;req=diUlE8B8m4lYXfMW1HO4zcDl6tzoPlCz8iWjaktE941m7skwi48OLPNPvKsA%0AgGyyUfWvgV0h2LbMyFo%3D%0A)

### Folder instructions

Folder instructions add project-specific context to Cowork when you select a local folder on desktop. Claude can also update these on its own during a session.

---

## Claude Cowork plugins

Plugins customize how Claude works for your role, team, and company in Cowork. Each one bundles skills, connectors, and sub-agents into a single package. For details on finding, installing, and customizing plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

---

## Schedule recurring tasks

You can set up tasks that Claude runs automatically or on demand. To schedule a task, type `/schedule` in any Cowork task. You can also click "Scheduled" in the left sidebar to view, create, and manage your scheduled tasks.

Scheduled tasks run remotely, so they don't need your computer to be awake or the desktop app open.

For more in-depth details, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

---

## Usage limits

Working on tasks with Cowork consumes more of your usage allocation than chatting with Claude. This is because complex, multi-step tasks are compute-intensive and require more tokens to execute.

If you find yourself hitting usage limits frequently when using Cowork, consider:

- Batching related work into single sessions.

- Using standard chat for simpler tasks that don't require file access or extended execution.

- Monitoring your individual usage in **[Settings > Usage](http://claude.ai/settings/usage)**.

See **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)** for more information.

---

## Permissions and security

Cowork runs with layered protections:

- **Session isolation:** Claude's work runs in an isolated environment on Anthropic's servers, separate from your computer and your network. Shell commands and code Claude writes run inside that environment. Isolation protects your computer; it doesn't change what Claude can read or do through the access you've granted.

- **Controlled file and network access:** Claude can only read and write files in folders you've connected, and network access follows the egress settings you've configured.

**Important:** Claude has access to the local files you grant it permission to access, and can take real actions on your behalf. Review Claude's planned actions before allowing it to proceed, especially when working with sensitive files.

Permissions work the same as for chat. You control:

1. Which **[MCPs you connect to Claude](https://claude.ai/settings/connectors)** and how often they ask for permission.

2. **[Claude's internet access](https://claude.ai/settings/capabilities)**

Please carefully assess how much you trust an MCP or website before extending access beyond Claude's default settings.

---

## Example use cases

Cowork is designed for complex, multi-step work that benefits from file access and extended execution time. Here are some examples:

### File and document management

- **Organize files:** "Organize my Downloads folder by type and date" — Claude can sort hundreds of files into categorized folders.

- **Process receipts:** Drop receipts in a folder and ask Claude to create a formatted expense report.

- **Batch rename:** Rename files with consistent patterns like YYYY-MM-DD formatting.

### Research and analysis

- **Research synthesis:** Combine information from web searches, articles, papers, and notes into coherent reports or summaries.

- **Transcript analysis:** Extract themes, key points, and action items from meeting notes, interviews, or lecture recordings.

- **Personal knowledge synthesis:** Analyze your notes, journals, or research files to surface patterns, themes, and connections you might have missed.

### Document creation

- **Spreadsheets with formulas:** Generate Excel files with working VLOOKUP, conditional formatting, and multiple tabs—not just CSVs that need fixing.

- **Presentations:** Create slide decks from rough notes or meeting transcripts.

- **Reports from messy inputs:** Turn voice memos and scattered notes into polished documents.

### Data and analysis

- **Statistical analysis:** Outlier detection, cross-tabulation, and time-series analysis on your data files.

- **Data visualization:** Generate charts using your data.

- **Data transformation:** Clean, transform, and process datasets.

For more detailed examples, see our **[use cases](https://claude.com/resources/use-cases)** and filter by the "Cowork" category.

---

## Current limitations

Some Cowork capabilities are not yet available:

- **Memory:** What Claude remembers about you in chat doesn't carry into Cowork sessions yet. Within Cowork, memory is supported in projects only**.**

- **No session sharing:** Sessions can't be shared with others. On Team and Enterprise plans, you can share live artifacts within your organization. Learn more about **[using live artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249)**.

- **Some features are desktop-only:** Live artifacts and plugins that include local MCP servers work through the desktop app only.

We're iterating on Cowork based on feedback. If you encounter issues or have suggestions, use the feedback button in the app to share feedback with our team.

---

## Troubleshooting

### I'm seeing "Setting up Claude's workspace" when I start Cowork; what does this mean?

This message is expected and indicates that Cowork is updating to the most recent version to apply any fixes and improvements.

### I don't see Cowork on web or mobile

Cowork on web and mobile is rolling out gradually across paid plans. Make sure you're on an eligible plan and, on mobile, that you've updated to the latest version of the app.

### Claude stopped working on my task

For local sessions, ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended. Remote sessions keep running in the background; open the session from any surface to check its progress.

### I'm hitting usage limits quickly

Cowork consumes more usage than standard chat. Try using standard chat for simpler tasks and reserve Cowork for complex, multi-step work that benefits from file access.

### Files aren't appearing where expected

Check that you've granted Claude the appropriate file access permissions. Review the output location Claude specified when completing the task.