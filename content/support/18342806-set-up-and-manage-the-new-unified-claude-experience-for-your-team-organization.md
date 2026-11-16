# Set up and manage the new unified Claude experience for your Team organization

The new unified Claude experience brings chat and Cowork together on web, desktop, and mobile. Users no longer choose between chat and Cowork before they start. Every chat starts the same way, and when a task needs to run code or work with files, Claude continues the same chat in an Anthropic-managed cloud environment and returns the finished work for review.

This article explains how Team plan owners turn on the new unified Claude experience, which settings apply to it, and how to manage its cost.

The new unified Claude experience is available on Team plans, where it appears in admin settings as **Chat and Cowork unified**. It turns on by default on December 1, 2026, unless an owner keeps it off.

---

## How the new unified Claude experience works

- **One conversation, two modes.** A chat moves into a Cowork cloud session when a task needs it. Users aren't asked to switch modes.

- **Longer tasks run in an isolated cloud environment.** Each chat that needs one gets its own virtual machine, managed by Anthropic. After a few minutes idle, the virtual machine is stopped and its disk is saved as an encrypted snapshot. The environment expires 30 days after it was created.

- **Work moves across devices.** A task started on the web can be picked up on desktop or mobile.

- **Local access stays optional.** Through Claude Desktop, users can link their computers so Claude can work with local folders and applications.

---

## Before you begin

The new unified Claude experience requires **Cloud code execution and file creation** to be on for your organization, since longer tasks run remotely.

It doesn't require **Cowork** or **Cowork in the cloud** to be on.

The new unified Claude experience isn't available yet for organizations that use zero data retention (ZDR). Learn more in **[Current limitations](#h_6650484050)** below.

---

## Turn on the new unified Claude experience

### For your whole organization

1. Sign in to Claude as an Owner or Primary Owner.

2. Go to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

3. Turn on **Chat and Cowork unified**.

4. Ask users to refresh the Claude app if they don't see the new experience right away.

Scheduled tasks and session history keep working after the change. You don't need to update or recreate anything.

### If you take no action

- **December 1, 2026:** The new unified Claude experience turns on by default for your organization. To keep it off, select "Keep disabled" in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** before then. If **Cloud code execution and file creation** is off, there's no notice and nothing turns on. After December 1, the new experience turns on as soon as you turn that setting on. If you already turned **Chat and Cowork unified** on or off, that choice stays. New Team organizations already start with it on.

- **February 1, 2027:** The separate chat and Cowork experience is retired. Any users still on it move to the new unified Claude experience automatically.

These dates don't apply to organizations with zero data retention.

The separate chat and Cowork experience isn't planned to get new features, apart from new model launches. New features are planned only for the new unified Claude experience, so we recommend starting your move now.

---

## Admin settings that apply to the new unified Claude experience

| **Setting**                                  | **Where**                                             | **How it applies**                                                                                                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chat and Cowork unified                      | Organization settings > Capabilities                  | Turns the new unified Claude experience on for the organization.                                                                                                                                               |
| Allow network egress                         | Organization settings > Capabilities > Code execution | Controls which internet destinations code in the cloud environment can reach: off, package managers only, a custom list of domains, or all domains.                                                            |
| Connector policies (Blocked, Needs approval) | Organization settings > Connectors                    | Enforced by Anthropic outside the cloud environment, on every connector call.                                                                                                                                  |
| Allow "Always allow" for connector tools     | Organization settings > Capabilities                  | When off, users can't choose "Always allow" for connector tools that can make changes, so Claude asks each time. Read-only tools aren't affected. Claude might still edit a doc in Claude Docs without asking. |
| Allow "Skip all approvals" mode              | Organization settings > Capabilities                  | When off, users can't choose "Skip all approvals" for scheduled tasks and the built-in browser.                                                                                                                |
| Allow "Automatically approve" mode           | Organization settings > Capabilities                  | When off, "Automatically approve" doesn't appear in users' mode selector.                                                                                                                                      |
| Share chats and Share cloud sessions         | Organization settings > Data and privacy              | A chat that has used its cloud environment can be shared only when both settings are on.                                                                                                                       |
| Computer access                              | Organization settings > Capabilities                  | When off, web, mobile, and scheduled tasks can't use a user's linked computer.                                                                                                                                 |
| Require trusted devices                      | Organization settings > Capabilities                  | Requires users to verify each new device before it can connect to Claude on their computer remotely.                                                                                                           |
| Scheduled tasks                              | Organization settings > Capabilities                  | When off, scheduled tasks that run remotely are disabled for your organization.                                                                                                                                |
| OpenTelemetry                                | Organization settings > Data and privacy              | If you've set up OpenTelemetry export, a chat's cloud session sends the same events as other cloud sessions.                                                                                                   |
| Device policy for Claude Desktop             | Your device management (MDM) tool                     | On managed computers, can disable local MCP servers and desktop extensions.                                                                                                                                    |

For recommended security settings, see **[Unified Claude and Cowork security best practices](https://trust.anthropic.com/resources?s=3puokpm2aa1nn24nbcp0l&name=unified-claude-security-best-practices)**.

---

## Data retention and deletion

- **Conversations.** Conversations are kept until the member deletes them. Conversations in a project are deleted with the project, once deleted by the user.

- **Cloud sessions started from a chat.** When a chat is deleted, the cloud sessions Claude started in it are deleted too, including their transcripts. Cowork cloud sessions a member starts directly, scheduled tasks and their runs, and Cowork history on a member's computer aren't deleted with a chat.

- **Memory.** Project memory is deleted when the project is deleted.

Deletion finishes in the background. We may retain content flagged by our trust and safety systems or as required by law. See **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**

---

## Manage usage

Tasks that run code or work with files can use more of a member’s seat allowance than a quick chat. If your organization has turned on **[usage credits](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)**, work beyond that allowance is billed at standard rates, up to any organization-wide spend limit you set in **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**. Per-member limits are also available for some organizations.

---

## Usage and analytics

The new unified Claude experience gets its own line in your reports. When a member has access to the new unified Claude experience, their chat and Cowork usage is reported under Chat and Cowork unified, not under Chat or Cowork. Think of it as a new folder for the same work: only where the usage is filed changes, so moving usage to this line doesn't change how it's counted or billed.

### How usage is counted

- **Counting follows each member.** Usage counts toward the new unified Claude experience if the member has access to it when the usage happens. Your reports can show Chat, Cowork, and Chat and Cowork unified on the same day.

- **It covers chat and Cowork.** A member's chats, their cloud sessions, and their use of the Cowork desktop app count toward the new unified Claude experience.

- **Other products keep their own line.** For example, Claude Code and Claude in Chrome usage is still reported under those products.

- **Past usage stays where it is.** Data for the new unified Claude experience starts the day a member first gets access. Usage from before then stays under Chat or Cowork. If you turn the new unified Claude experience off, past unified usage keeps its Chat and Cowork unified label, and new usage goes back to Chat and Cowork.

- **Include it when you add things up.** When you add up spend, tokens, or messages for Chat and Cowork, include Chat and Cowork unified too. Otherwise your Chat and Cowork numbers will seem to drop as members move over. For the number of people, use the overall active users count rather than adding products together, since one person can be active in more than one.

### In the analytics dashboard

**A page of its own.** Admins who can view analytics will find a Chat and Cowork unified page under Apps. It shows daily active users.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2806001895/531860da20ab38cc20552671aa8a/60d7f385-93e4-44cb-a767-3c68bb033f2e)

**Across the dashboard.** You can pick "Chat and Cowork unified" in the **Active members** and **Spend by model** charts, and **Total spend** shows it as its own line. Spend charts appear only if usage credits are on.

**Who sees it.** The page appears for every organization that can turn on the new unified Claude experience, whether or not it is on yet.

**Give it a day or two.** New activity can take up to two days to show up.

---

## Current limitations

- **ZDR.** The new unified Claude experience isn't available to organizations with zero data retention. These organizations keep using chat and Cowork as they do today, and owners can't turn on **Chat and Cowork unified**.

- **Efficient mode.** Efficient mode isn't available on Team plans.