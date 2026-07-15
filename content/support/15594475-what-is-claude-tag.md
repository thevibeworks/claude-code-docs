# What is Claude Tag?

Claude in Slack will be switched over to the new Claude Tag experience on August 3, 2026. To integrate Claude and Slack, use Claude Tag instead.

Claude Tag is a new way to work with Claude: tag @Claude into a conversation and it takes on real work, using your organization's tools and the shared context around it. Claude works under its own identity, builds context by remembering relevant information from the channels it’s in, and can follow up on its own.

Claude Tag is available on Team and Enterprise plans in beta. Claude Tag works in Slack today.

It’s how we’ve brought Claude’s capabilities directly to Slack, bringing AI assistance into your team’s workspace. This integration allows you to work with Claude without leaving Slack through three convenient surfaces:

- **Channel tagging:** Tag @Claude in any channel to hand it a task, and follow along as it works in the thread.

- **Direct message with Claude**: Start a private conversation with @Claude.

- **AI assistant panel**: Click the Claude icon in Slack's AI assistant header to open a panel on the right side of your Slack window, allowing you to access Claude from anywhere in the Slack app.

When you tag @Claude in a channel, Claude works through the task while the whole exchange stays visible to everyone in the channel. Everyone in a channel works with the same Claude, so anyone can steer it or pick up where it left off. Claude can also check in on its own, like posting when a job finishes or tagging you when a thread stalls. To learn more, see the **[Claude Tag overview](https://claude.com/docs/claude-tag/overview)**.

In direct messages and the assistant panel, Claude has the capabilities you've enabled in your own Claude account, like web search and your connected tools. Channel tagging works differently: Claude acts under your organization's identity, using the tools and access an admin set up for that channel, and the work is billed to your organization rather than to you.

---

## Set up Claude Tag

After the Claude app is installed, a Primary Owner or Owner sets up Claude Tag: provision Claude's identity, connect your organization's tools and repositories, and choose which channels Claude Tag can work in. People on your team don't need to set up anything individually once a channel is ready. For the full walkthrough, see the **[Claude Tag setup guide](https://claude.com/docs/claude-tag/admins/setup-overview)**.

**Important:** Only a Primary Owner or Owner can set up Claude Tag's access and channels. The Admin role can't.

---

## Control who can use Claude Tag

In **Organization settings > Claude in Slack**, Member Access has three modes: open to anyone in the Slack workspace, open to any member of your Claude organization, or only members whose role allows it. The third option is role-based access and is available on the Claude Enterprise plan. To restrict by role, set Member Access to "Only members whose role allows it" and grant the "Claude in Slack" capability to a custom role. This setting applies to both channel mentions and direct messages. To set member access, see **[Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access)**.

[https://www.youtube.com/embed/JhipXUs1Y98?rel=0](https://www.youtube.com/embed/JhipXUs1Y98?rel=0)

## Manage spend limits for Claude Tag

Claude Tag is consumption-based, so spend is based on usage rather than the number of people. As a Primary Owner or Owner, you control it from the usage settings in your admin console.

- **Organization-wide limit:** a hard cap on total Claude Tag spend across every channel. Spend can't exceed it.

- **Per-channel limits:** set a limit on any individual channel, on top of the organization-wide cap. New channels inherit a default limit.

- **Threshold alerts:** admins are notified at 75% and 95% of any limit.

- **Usage analytics:** a per-channel spend breakdown lives on the same page.

**Note:** Work that would go over a limit is declined, never silently cut short. A blocked user can request more from their admin without leaving Slack, and the alert says whether the limit or the available balance caused the block.

Tagging Claude in a channel is billed to your organization. Direct messages are billed to your own Claude account instead.

To set limits, see **[Set spend limits for Claude Tag](https://claude.com/docs/claude-tag/admins/restrict-access#set-spend-limits)**.

## Set access and permissions for Claude Tag

You decide what Claude Tag can reach by setting credentials and repository access at three levels. Each level inherits the permissions and memory of the one above it.

- **Organization-wide:** credentials and repositories that apply everywhere Claude Tag is installed.

- **Workspace:** access that applies to every public channel inside a Slack workspace. Inherits organization-wide permissions and memory.

- **Private channel:** extra credentials or repositories on top of what the workspace already grants. Use a private channel to keep sensitive connections to a smaller group. For example, a channel set up for legal work keeps its tools and memory separate from an engineering channel.

To configure access, see **[Claude Tag identity and access](https://claude.com/docs/claude-tag/concepts/agent-identity)**.

## Review memory and activity for Claude Tag

Claude Tag keeps context per channel and per workspace. Admins can view, edit, and delete that memory.

An Audit view in **Organization settings > Claude Tag > Audit** lists every scheduled and one-time task across your organization in addition to all network calls made using Agent Identity. Each action is also traceable in the tool where it happened: posts come from the Claude app in Slack, and commits and pull requests show the Claude GitHub App as the author with a link back to the Slack thread that started them. In any channel, you can ask "@Claude what triggers do you have set up here?" to see and turn off standing work.

---

## Privacy and data

### Data storage

Your Slack conversations with Claude remain separate from your Claude history, keeping work organized across platforms.

### Data visibility

- Conversations initiated in Slack are not visible in **[your Claude chat history](http://claude.ai/recents)**.

- Conversations initiated in the Claude web app are not accessible in Slack.

- Each platform maintains separate conversation histories.

### Data deletion

- Conversations are automatically deleted from Claude within 30 days if you disconnect the integration or uninstall the app.

- Your conversations in Slack follow your organization's Slack retention policies.

### Claude Tag memory

Claude Tag remembers context to do its work, so channel and workspace memory is retained rather than discarded after each task. Memory and activity respect channel boundaries, and admins can review or delete what Claude remembers. Channel work is attributed to your organization's Claude identity, while work done in a direct message runs on your own account.

---

## Frequently asked questions

### How is Claude Tag different from the Claude in Slack I already use?

Claude Tag is the next generation of that experience, in the same place. The familiar ways of working still apply, and Claude can now do more: it remembers context across days, schedules its own follow-ups, checks in proactively, and acts under its own identity. An organization’s Primary Owner or Owner opts your organization in to move over.

### Who can set up Claude Tag, and who pays for it?

Only an organization's Primary Owner or Owner can set up Claude Tag's access and channels. Tagging Claude in a channel is billed to your organization. Direct messages are billed to the person’s own Claude account instead.