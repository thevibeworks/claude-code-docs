> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Claude Tag

> Claude Tag is customized per channel and workspace (a scope), not per user. See what admins set in claude.ai, what anyone can change from the channel, and what stays fixed.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag's behavior is shaped by four layers, each set in a different place:

| Layer                   | What it is                                                                                                                                           | Who sets it                                                                                                                                         | Where                                                                                                                            |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Connections**         | Credentials for the systems Claude can reach (GitHub, Drive, Datadog, your APIs)                                                                     | Owner; a [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for their assigned channels               | [Access bundles](/docs/claude-tag/admins/add-connections), or the channel's Configure page for a channel manager                      |
| **Plugins and skills**  | Instructions that teach Claude how to use a tool or follow a process. A plugin bundles one or more [skills](https://code.claude.com/docs/en/skills). | Owner                                                                                                                                               | [Bundle Plugins tab](/docs/claude-tag/admins/add-connections#attach-plugins) or a [skills repository](/docs/claude-tag/admins/skills-repo) |
| **Custom instructions** | Standing guidance read in every session at a scope (team conventions, output formats). Outranks channel memory.                                      | Owner for any scope; channel members for the channel scope, from the [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) | [Per-scope instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions)                                             |
| **Channel memory**      | Facts Claude saves while working in a channel                                                                                                        | Anyone in the channel                                                                                                                               | By [telling Claude](/docs/claude-tag/users/memory)                                                                                    |

Connections and plugins decide what Claude *can do*; instructions and memory shape *how it does it*.

## Settings admins control

Access and organization-wide behavior are set at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), per scope (a scope is a channel, a workspace, or your whole organization), so the same agent can work differently in different channels. Most controls below are Owner-only.

| Setting               | What it does                                                                                                                                                                                                                                                                                                                                                                                                                                                             | More                                                                                                                                           |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Custom instructions   | Standing guidance read in every session on a scope, like team conventions. Outranks channel memory.                                                                                                                                                                                                                                                                                                                                                                      | [Add custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions)                                                          |
| Respond automatically | Whether Claude replies to a channel's messages without an @-mention. Channel members can change it too, from Slack or the channel's Configure page.                                                                                                                                                                                                                                                                                                                      | [Turn automatic replies on or off](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off)                                    |
| Plugins               | Bundles of skills that teach Claude how to use a specific tool                                                                                                                                                                                                                                                                                                                                                                                                           | [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins)                                                                            |
| Connections           | Which systems it can reach from each channel                                                                                                                                                                                                                                                                                                                                                                                                                             | [Add connections](/docs/claude-tag/admins/add-connections)                                                                                          |
| Default model         | Which Claude model handles sessions in a scope                                                                                                                                                                                                                                                                                                                                                                                                                           | [Choose the model for a scope](#choose-the-model-for-a-scope)                                                                                  |
| Auto mode allow rules | Actions pre-approved in a scope's sessions that Claude's permission checker would otherwise flag or stop                                                                                                                                                                                                                                                                                                                                                                 | [Auto mode allow rules](#auto-mode-allow-rules)                                                                                                |
| Environment           | Which cloud environment a scope's sessions run in. The picker shows [organization-shared cloud environments](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments), plus runner pools for organizations that use [self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments-quickstart). Environments on an individual account never appear, because Claude runs channel sessions with no user account attached. | [Channel environment troubleshooting](/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one) |
| Claude Tag version    | Which generation answers (New, Legacy, or Off) in a scope                                                                                                                                                                                                                                                                                                                                                                                                                | [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/workspaces#set-the-version-for-a-scope)                                          |

### Channel connections are separate from personal connectors

An Owner configures Claude's connections, plugins, and skills, and they apply per scope. They are separate from the connectors, skills, or MCP servers an individual user has set up in their own claude.ai or Claude Desktop account. A user's personal connectors are not available to Claude in a channel, and the channel's connections are not listed among that user's personal connectors in claude.ai. Projects in claude.ai are separate too. Claude doesn't read a Project's instructions or knowledge in Slack, and a channel can't be pointed at a Project. Put standing guidance for a channel in its [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions).

To give Claude access to a tool that is not in the built-in connection list, including a custom MCP server, see [add a custom connection](/docs/claude-tag/admins/connections/custom).

## Change behavior from the channel

Everything in the table below is open to channel members, with no admin involved.

| To change                      | Say something like                                         | More                                                                       |
| :----------------------------- | :--------------------------------------------------------- | :------------------------------------------------------------------------- |
| How Claude formats output      | "remember for this channel: post reports as a table"       | [Memory](/docs/claude-tag/users/memory)                                         |
| How chatty Claude is           | "ask before posting anything longer than a screen"         | [Memory](/docs/claude-tag/users/memory)                                         |
| When Claude follows a thread   | "stay quiet in this thread unless someone tags you"        | [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds) |
| What Claude does on a schedule | "every morning at 9, post a digest of open threads"        | [Set up routines](/docs/claude-tag/users/proactivity)                           |
| What Claude remembers          | "what do you remember about this channel?" then correct it | [Memory](/docs/claude-tag/users/memory)                                         |

Changes in the table above are saved to channel memory; verify one stuck by asking what it remembers.

Members can also tailor how Claude works in the channel from its Configure page on claude.ai. The **Configure** link in the footer of any Claude reply in the channel opens it, and if a member sends [`@Claude !configure`](/docs/claude-tag/users/commands#get-the-link-to-configure-a-channel) in the channel, Claude replies with a link to it. Anyone in the channel who is also a member of your Claude organization can edit settings for that channel there, unless an admin has [restricted editing to admins](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). The **Channel instructions** field on that page holds standing guidance that outranks memory. See [configure Claude for a channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

The Configure page also shows the channel's resolved access, read-only. Its **Connections** tab lists the channel's resolved connections, which admins set in admin settings. Its **Routines** tab lists the channel's [routines](/docs/claude-tag/users/proactivity) with each one's schedule, status, and last run.

On the Enterprise plan, an Owner can name [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for a channel. They set the channel's default model, repositories, and connections from the same page.

## Choose the model for a scope

Each scope carries a **Default model** setting in its **Advanced** section, alongside the [environment](/docs/claude-tag/concepts/glossary#environment) and guest controls. It sets the model new channel sessions in that scope start on; the options are drawn from the models available to your organization, such as Opus and Sonnet models. A scope without its own setting inherits from its parent, and a channel's setting overrides its workspace's. The **Inherit** option shows which model the scope resolves to.

To keep sessions on a model you chose, set a specific model at the organization scope rather than leaving the setting unset; every scope without an override then follows it.

The setting applies to new sessions; threads already underway keep the model they started with. The footer of each Claude reply in Slack names the model that handled it, so you can confirm what a scope is running.

Channel members can also change the model from Slack, with no admin involved. Asking Claude in a thread switches that thread, and asking it to make a model the channel default changes what new threads in the channel start on. See [choose the model Claude Tag uses](/docs/claude-tag/users/models).

### Models your organization allows

Claude Tag's model lists come from the models your organization makes available for Claude Code, set in the Claude admin console, leaving out any that Claude Tag doesn't support. A model you see in Claude Code can be absent in Slack for that reason. The allowed list applies in two places.

* **Model lists in Slack.** The models Claude offers when someone asks it to switch, and the model selector for direct messages, show only allowed models. Claude declines a request to switch to a model outside the list.
* **Configured defaults.** If your organization also enforces the policy on defaults and a workspace or channel's **Default model** isn't allowed by your organization's Claude Code model policy, Claude declines to start the session and posts a notice in the thread asking the requester to contact an admin. A model excluded by your organization's plan entitlements works differently. Claude starts the session on a fallback model the plan includes, and declines only when the plan excludes every fallback. The footer of the first reply names the model that served it, so check there to see which model the session started on.

A change to the allowed list applies to new sessions, like a change to the **Default model**; a thread already underway keeps its model until someone in it asks Claude to switch.

## Where to change a scope's environment

The environment is the sandboxed compute configuration a scope's sessions run in. You create environments in one place and pin one per scope in another. An Owner or admin creates environments on the **Cloud environments** page in [admin settings](https://claude.ai/admin-settings), as [organization-shared environments](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments). You then pin one per scope, in the **Environment** picker in the scope's **Advanced** section on [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), for **Default Slack access**, a workspace, or a channel. A channel with no pin of its own inherits the nearest pin above it; with nothing pinned anywhere, sessions use the **Organization default**.

A change applies to new sessions; after you pin an environment, start a fresh thread to pick it up. To give a channel broader network access through its environment, see [broad web access through the environment](/docs/claude-tag/admins/add-connections#broad-web-access-through-the-environment). If sessions don't pick up the environment you pinned, see [channel sessions use the wrong environment](/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one).

## Auto mode allow rules

Sessions run in [auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode), where Claude's permission checker reviews each action Claude is about to take and can flag or stop it. When you add an auto mode allow rule to a scope, you pre-approve one action in that scope's sessions, so Claude runs it there without the checker stopping it. The checker keeps reviewing every other action.

A rule is a plain sentence that describes work you approve in the scope, such as "Deploying to our staging cluster from a session in this channel is a normal, approved workflow." To add one:

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open the **Slack** tab under **Claude Tag's access** and find the scope you want to change (the organization-wide **Slack** row, a workspace, or a channel). The **Slack** row opens as **Default Slack access**.
2. Open the scope's **Advanced** section and find **Auto mode allow rules**, below the [**Default model**](#choose-the-model-for-a-scope) setting.
3. Select **Add rule** and write the rule as one plain sentence.

The rules list has three properties:

* **Limits:** a scope holds up to 50 rules, and each rule can be up to 1,024 characters
* **Inheritance:** rules you set on a workspace or on [Default Slack access](/docs/claude-tag/admins/attach-to-scope#how-scopes-inherit) (the organization-wide root) carry down to the channels beneath, the way [custom instructions](/docs/claude-tag/admins/attach-to-scope#custom-instructions) stack. A channel's own rules add to those and never replace them, so put a rule on a single channel's scope to pre-approve an action there without changing any other channel.
* **Access:** you edit the list with the same admin access as the scope's other **Advanced** settings

<Warning>Once you add an allow rule, Claude runs the actions it names in every channel the scope covers without anyone approving them in the moment. Keep each rule narrow: name the tool, the action, and the environment it allows, and put rules that unlock sensitive systems on the narrowest scope that needs them.</Warning>

## Settings no one can change

* The Claude app's name, @-handle, and avatar in Slack are the same in every workspace; there is no rename or rebrand setting.

## Related resources

* [Settings map](/docs/claude-tag/concepts/settings-map): every settings surface, including spend limits and personal connectors
* [What Claude Tag remembers](/docs/claude-tag/users/memory): how channel instructions are stored, shared, and corrected
* [Good habits for working with Claude Tag](/docs/claude-tag/users/good-habits): phrasings that make recurring output consistent
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why access is set per channel
