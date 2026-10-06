> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Tag settings map

> Claude Tag settings map: the admin page for access and behavior, the usage page for spend limits, the in-Slack Configure link for channel instructions, and personal connectors for DMs and your own tasks in channels. Claude Managed Agents is configured separately on the Claude Platform.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag's settings live on claude.ai, split across a few pages that each own a different kind of setting. Which page you need depends on what you're changing. The table maps each surface to what it controls.

| Surface | Who changes it | What it controls |
| :- | :- | :- |
| [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag) | An Owner in your Claude organization, or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) on the Enterprise plan | Access, behavior, and restrictions for channels, mostly per [workspace and channel](/docs/claude-tag/concepts/glossary#scope) |
| [Usage page](https://claude.ai/admin-settings/usage/claude-tag) | An admin | Spend limits and each channel's spend against them |
| [Analytics page](https://claude.ai/analytics/claude-tag) | Anyone who can view the Analytics dashboard | Spend trends, projections, and per-channel reports; read-only |
| The **Configure** link in the footer of any Claude reply in a channel | Channel members (unless an admin restricts editing) and [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for their assigned channels | One channel's instructions and whether Claude replies there without an @-mention. Channel managers also set the channel's default model, repositories, connections, and plugins |
| [Customize > Connectors](https://claude.ai/customize/connectors) on your own claude.ai account | You | Which of your personal tools apply in [one-to-one DMs](/docs/claude-tag/concepts/agent-identity#direct-message-channels) and for [your own tasks in a channel](/docs/claude-tag/concepts/personal-connectors) |

Channel memory and routines aren't in the table because you change them by talking to Claude in the channel; see [what anyone can change from the channel](/docs/claude-tag/admins/customize#change-behavior-from-the-channel). Owners can review both on the **Scheduled work** and **Memory** tabs of the [**Activity** page](/docs/claude-tag/admins/audit). Only an Owner can edit or delete memory entries.

## Claude Tag admin settings

Everything an admin configures for channels lives at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). Most settings there apply per scope (a channel, a workspace, or the whole organization), and each scope has its own page on the **Channels** tab under **Claude's access**. A scope without its own setting inherits from its parent, and a channel's setting overrides its workspace's, so two channels can run with different connectors, models, and instructions. Most controls need the Owner role or, on the Enterprise plan, the [**Claude Tag Admin** permission](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration); the [permissions table](/docs/claude-tag/admins/restrict-access#permissions-by-role) lists each action and who can take it.

* **Bundles**: the connectors, domains, repositories, plugins, and instructions Claude uses in the workspaces and channels a bundle applies to. The **Connectors** and **Skills and plugins** tabs add a new connector, plugin, or skill. See [Give Claude access](/docs/claude-tag/admins/add-connections).
* **Custom instructions**: standing guidance Claude reads in every session on a scope. See [Add custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions).
* **Model**: the model new sessions in a scope start on, set in the **Model** row on the main Claude Tag page for the whole organization and on each workspace's and channel's page. The picker shows the models your organization allows for Claude Code, leaving out any that Claude Tag doesn't support, so it can be missing models you see in Claude Code itself. See [Choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope).
* **Auto mode allow rules**: plain sentences that pre-approve actions Claude's permission checker would otherwise flag or stop in a scope's sessions. See [Auto mode allow rules](/docs/claude-tag/admins/customize#auto-mode-allow-rules).
* **Workspace pairing and restrictions**: which Slack workspaces are paired, whether DMs are allowed, guest-channel behavior, which channels Claude can search, who can invoke Claude, and which generation of the app answers in each scope (some Team plan organizations have a [single on-or-off switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-on-the-team-plan) in place of the per-scope setting). See [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access).
* **Channel name rules**: channel-name patterns that keep Claude out of matching channels, join it automatically to new public ones, or attach a bundle to every matching channel. See [Block or auto-join channels by name](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name).
* **Personal connectors**: on the Enterprise plan, whether Claude holds every result of a member's connector task for that member's review before posting it, and the topics an Owner adds to the sensitive-content check. These settings apply to the whole organization rather than per scope, and you reach them with **Edit** on the **Personal connectors** row of the main Claude Tag page. See [Admin controls for personal connectors](/docs/claude-tag/concepts/personal-connectors#admin-controls-for-personal-connectors).

## Spend limits and usage

Spend limits live on the usage page at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag), separate from Claude Tag admin settings. The usage page holds the organization-wide spend limit, the default spend limit for channels, per-channel limits, and each channel's spend against its limit. If your organization bills through a reseller, this page is not available. See [Set a spend limit](/docs/claude-tag/admins/set-spend-limit) for funding the usage balance and what users see when a limit is reached.

Usage covered by a promotional credit isn't counted on the usage page and shows as \$0.00 there. To see each channel's list-price spend for the current month including covered usage, use the **List price** column of the **Spend by channel** table at [`claude.ai/analytics/claude-tag`](https://claude.ai/analytics/claude-tag).

Spend trends live at [`claude.ai/analytics/claude-tag`](https://claude.ai/analytics/claude-tag), the Claude Tag section of the Analytics dashboard. It shows total and projected spend, spend by channel, and [spend by kind of work](/docs/claude-tag/admins/set-spend-limit#see-spend-by-kind-of-work) for the period you pick, and anyone with permission to view the Analytics dashboard can open it. It has no controls; see [Usage analytics](/docs/claude-tag/admins/restrict-access#usage-analytics).

## The Configure page

Every Claude reply in a channel ends with a footer, and its **Configure** link opens a claude.ai page for that channel; replies in DMs have no Configure link. You can also send [`@Claude !configure`](/docs/claude-tag/users/commands#get-the-link-to-configure-a-channel) in the channel, and Claude replies with a link to the same page.

Anyone in the channel who is also a member of your Claude organization can edit the **Channel instructions** field on that page, unless an admin has [restricted editing to admins](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). The page's **Respond automatically** toggle controls whether Claude replies in the channel without an @-mention; see [Turn automatic replies on or off](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off).

The page's **Tools and access** tab shows the channel's resolved connections and any allowed domains. Members can see those lists but not change them there. The same tab's **Plugins** card lists the channel's plugins, and members can add plugins there unless an admin has restricted editing to admins. A **Routines** tab lists the channel's routines with each one's schedule, status, and last run.

The Configure page and the **Channel instructions** field on the channel's page in admin settings write the same instructions, so a change from either place is visible in the other. See [Configure Claude for a channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

On the Enterprise plan, an Owner can name [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for a channel, and so can a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) whose role also sets **Identity & Access** to **Can manage**. For channel managers, the same page adds editable cards: the channel's default model on the **General** tab, and **GitHub repositories** and **Access bundles** on the **Tools and access** tab.

## Personal connectors on claude.ai

Connectors you add to your own claude.ai account, under **Customize > Connectors**, apply in one-to-one DMs with Claude, because [a DM runs on your own account](/docs/claude-tag/concepts/agent-identity#direct-message-channels). A channel session uses the connections an admin attached to it. Claude can also [use your personal connectors there](/docs/claude-tag/concepts/personal-connectors) for your own tasks, after you allow it. Slack has no connector settings of its own.

See [connectors on claude.ai](/docs/connectors/getting-started) for setting one up, and [the troubleshooting entry](/docs/claude-tag/users/troubleshooting#a-connector-works-on-claude-ai-but-not-in-slack) if a connector you use on claude.ai is missing in Slack.

## Claude Tag versus Claude Managed Agents

[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) is a separate product for developers, a pre-built agent harness that runs in managed infrastructure. You configure it on the Claude Platform through the Managed Agents API, and access requires a Claude API key. An agent there is defined by its model, system prompt, tools, MCP servers, and skills. Environments choose where its sessions run (a cloud sandbox, or a self-hosted sandbox on your own infrastructure), and scheduled deployments run it on a cron schedule.

The two products don't share settings. Nothing in Claude Tag admin settings configures a Managed Agent, and an agent defined on the Claude Platform doesn't change how Claude behaves in Slack.

## Related resources

* [Customize Claude Tag](/docs/claude-tag/admins/customize): the layers that shape Claude's behavior in a channel and who sets each one
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why channels and DMs use different access
* [Set up Claude Tag](/docs/claude-tag/admins/setup-overview): pair a workspace, launch, and give Claude access
