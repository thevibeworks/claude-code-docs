> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Claude Tag

> Claude Tag is customized per channel and workspace (a scope), not per user. See what admins set in claude.ai, what anyone can change from the channel, and what stays fixed.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag's behavior is shaped by four layers, each set in a different place:

| Layer | What it is | Who sets it | Where |
| :- | :- | :- | :- |
| **Connectors** | The systems Claude can reach and the credentials it uses for each (GitHub, Drive, Datadog, your APIs) | Owner or [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration); a [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for their assigned channels | The **Connectors** tab and [bundles](/docs/claude-tag/admins/add-connections) under **Claude's access**, or the channel's Configure page for a channel manager |
| **Plugins and skills** | Instructions that teach Claude how to use a tool or follow a process. A plugin bundles one or more [skills](https://code.claude.com/docs/en/skills). | Owner or [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration); channel members can add plugins to their channel unless an admin restricts editing | The **Skills and plugins** tab under **Claude's access**, a [bundle](/docs/claude-tag/admins/add-connections#attach-plugins), a [skills repository](/docs/claude-tag/admins/skills-repo), or the channel's Configure page |
| **Custom instructions** | Standing guidance read in every session at a scope (team conventions, output formats). Outranks channel memory. | Owner for any scope; [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) for workspace and channel scopes; channel members for the channel scope, from the [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) | [Per-scope instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) |
| **Channel memory** | Facts Claude saves while working in a channel | Anyone in the channel | By [telling Claude](/docs/claude-tag/users/memory) |

Connectors and plugins decide what Claude *can do*; instructions and memory shape *how it does it*.

## Settings admins control

Access and organization-wide behavior are set at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), per scope (a scope is a channel, a workspace, or your whole organization), so the same agent can work differently in different channels. Each scope has its own page on the **Channels** tab under **Claude's access**, and the **Slack** page there covers your whole organization. Most controls below need the Owner role or, on the Enterprise plan, the [**Claude Tag Admin** permission](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration); the [permissions table](/docs/claude-tag/admins/restrict-access#permissions-by-role) lists each action and who can take it.

| Setting | What it does | More |
| :- | :- | :- |
| Custom instructions | Standing guidance read in every session on a scope, like team conventions. Outranks channel memory. | [Add custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) |
| Managed by | Which other Slack channels' members can write a channel's standing instructions by asking Claude, including from a private channel. On the Enterprise plan, an Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) sets it on the **Admin** tab of the channel's Configure page. | [Manage a channel's instructions from another channel](/docs/claude-tag/admins/managed-by) |
| Respond automatically | Whether Claude replies to a channel's messages without an @-mention. **Respond automatically** exists only on channels, not on workspaces or your whole organization. Channel members can change it too, from Slack or the channel's Configure page, unless the scope's [**Channel member edits**](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block**. | [Turn automatic replies on or off](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) |
| Plugins | Bundles of skills that teach Claude how to use a specific tool | [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins) |
| Connectors | Which systems Claude can reach from each channel | [Add a connector](/docs/claude-tag/admins/add-connections) |
| Model | Which Claude model handles sessions in a scope | [Choose the model for a scope](#choose-the-model-for-a-scope) |
| Auto mode allow rules | Actions pre-approved in a scope's sessions that Claude's permission checker would otherwise flag or stop | [Auto mode allow rules](#auto-mode-allow-rules) |
| Environment | Which cloud environment a scope's sessions run in | [Configure the environment for a scope](#configure-the-environment-for-a-scope) |
| Enable Claude Tag | Turns Claude on or off in a scope. On the **Slack** page, the switch is labeled **Respond in all channels** or **Respond in channels** | [Turn Claude Tag on or off and set the version for a scope](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) |
| Claude Tag version | Which generation answers in a scope (**New** or **Legacy**) | [Turn Claude Tag on or off and set the version for a scope](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) |

<a id="channel-connections-are-separate-from-personal-connectors" />

### Claude Tag connectors are separate from personal connectors

An Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) configures Claude Tag connectors, plugins, and skills, and they apply per scope. They are separate from the personal connectors, skills, or MCP servers an individual user has set up in their own claude.ai or Claude Desktop account. A user's personal connectors are not part of a channel's configuration, and the channel's connectors are not listed among that user's personal connectors in claude.ai. Claude can [use a user's personal connectors in a channel](/docs/claude-tag/concepts/personal-connectors) for that user's own tasks, after the user allows it. That work runs with the user's permissions and is recorded under their name. Projects in claude.ai are separate too. Claude doesn't read a Project's instructions or knowledge in Slack, and a channel can't be pointed at a Project. Put standing guidance for a channel in its [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions).

To give Claude access to a tool that isn't in the **Add a connector** list, including a custom MCP server, see [Connect a service that isn't in the list](/docs/claude-tag/admins/connections/custom).

## Change behavior from the channel

Everything in the table below is open to channel members, with no admin involved.

| To change | Say something like | More |
| :- | :- | :- |
| How Claude formats output | "remember for this channel: post reports as a table" | [Memory](/docs/claude-tag/users/memory) |
| How chatty Claude is | "ask before posting anything longer than a screen" | [Memory](/docs/claude-tag/users/memory) |
| When Claude follows a thread | "stay quiet in this thread unless someone tags you" | [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds) |
| What Claude does on a schedule | "every morning at 9, post a digest of open threads" | [Set up routines](/docs/claude-tag/users/proactivity) |
| What Claude remembers | "what do you remember about this channel?" then correct it | [Memory](/docs/claude-tag/users/memory) |

Changes in the table above are saved to channel memory; verify one stuck by asking what it remembers.

Members can also tailor how Claude works in the channel from its Configure page on claude.ai. The **Configure** link in the footer of any Claude reply in the channel opens it, and if a member sends [`@Claude !configure`](/docs/claude-tag/users/commands#get-the-link-to-configure-a-channel) in the channel, Claude replies with a link to it. Anyone in the channel who is also a member of your Claude organization can edit settings for that channel there, unless an admin has [restricted editing to admins](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). The **Channel instructions** field on that page holds standing guidance that outranks memory. See [configure Claude for a channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

The Configure page also shows the channel's resolved access. Its **Tools and access** tab lists the channel's resolved connections and any allowed domains. Members can see those lists but not change them there. The same tab's **Plugins** card lists the plugins available to Claude in the channel; members can add plugins there unless an admin has [restricted editing to admins](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). The card groups plugins **Added by your admin**, which members can't remove, separately from plugins **Added by members**, which members can remove. The Configure page's **Routines** tab lists the channel's [routines](/docs/claude-tag/users/proactivity) with each one's schedule, status, and last run.

On the Enterprise plan, an Owner can name [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for a channel, and so can a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) whose role also sets **Identity & Access** to **Can manage**. Channel managers set the channel's default model, repositories, connections, and plugins from the same page.

## Choose the model for a scope

The **Model** setting sets the model new channel sessions in a scope start on. For your whole organization, it's the **Model** row on the main [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) page. For a workspace or channel, it's on the **General** tab of that scope's page on the **Channels** tab under **Claude's access**. The options are the models your organization allows, such as Opus and Sonnet models, regardless of any individual member's own model access. The picker also lists model families. A scope set to a family option starts sessions on the newest model of that family your organization allows, and moves to a newer one when your organization gets it, without you changing the setting.

A workspace or channel without its own setting shows **Inherit** and takes the model from its parent, and a channel's setting overrides its workspace's. The line under the setting names the model the scope uses and which scope it comes from.

To keep sessions on a model you chose, set a specific model in the organization's **Model** row rather than leaving it unset; every scope without an override then follows it.

When you change the setting, new sessions start on the new model. A thread already underway switches to it at the next message anyone posts there, unless someone in that thread has already had Claude switch models. The footer of each Claude reply in Slack names the model that handled it, so you can confirm what a scope is running.

Channel members can also change the model from Slack. Asking Claude in a thread switches that thread, and asking it to make a model the channel default changes this setting for the channel, unless the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block**. See [choose the model Claude Tag uses](/docs/claude-tag/users/models).

### Models your organization allows

On the Team plan, Claude Tag doesn't apply the [`availableModels` allowlist](https://code.claude.com/docs/en/model-config#restrict-model-selection) from your Claude Code [server-managed settings](https://code.claude.com/docs/en/server-managed-settings), and on the Enterprise plan it applies the allowlist in only some organizations.

* **Where the allowlist doesn't apply**: Claude offers your organization's full Claude Tag model list, both when someone asks it to switch and in the model selector for direct messages. It starts sessions on a scope's **Model** setting without checking that model against the allowlist. The **Model** picker in admin settings still lists only allowed models.
* **Where the allowlist applies**: sessions in a channel run as the [agent identity](/docs/claude-tag/concepts/agent-identity) you provisioned and without your server-managed settings. When someone in a channel asks Claude to switch models, Claude may decline a model outside the allowlist, though that check doesn't always run. In one-to-one direct messages from a member whose linked Claude account belongs to your organization, Claude runs on that member's own account, which receives your allowlist; see [Restrict model selection](https://code.claude.com/docs/en/model-config#restrict-model-selection) for what happens to a model the allowlist blocks.

In either case, Claude Tag offers only the models it supports, so a model your allowlist includes can be absent in Slack.

On the Enterprise plan, turning a model off for the whole organization on your **Models** page removes it from the lists in Slack, and Claude declines requests to switch to it. If you turn off the model a scope's **Model** setting names, Claude still starts sessions there on a fallback model that's still on, and declines only when every fallback is off too. The footer of the first reply names the model that served it.

### Allow fast mode

[Fast mode](/docs/claude-tag/users/models#run-a-thread-in-fast-mode) gives a thread faster output at a higher cost per token. Claude in Slack and Claude Code share one fast mode setting, so turning it on allows fast mode in both. The setting is off by default on the Team and Enterprise plans.

To allow fast mode, an Owner goes to [**Admin settings > Claude Code**](https://claude.ai/admin-settings/claude-code) and turns on the **Fast mode** toggle under **Capabilities**. Fast mode draws from usage credits, so also turn those on at [**Admin settings > Usage**](https://claude.ai/admin-settings/usage). For an organization billed through AWS Marketplace, the toggle is locked.

Turning the toggle on has these effects in Slack:

* **Speed**: every session starts at standard speed until someone turns fast mode on for it, and no per-channel setting starts sessions in fast mode
* **Who turns it on**: any member who can message Claude in a channel can turn fast mode on for a thread there by sending [`@Claude !fast`](/docs/claude-tag/users/commands#turn-fast-mode-on-or-off)
* **Model**: when a thread is on a model other than Opus, such as Sonnet, `!fast` moves it to the newest Opus model among the [models your organization allows](#models-your-organization-allows), and the thread stays on that model after `!fast off`
* **Where**: sessions stay at standard speed in a channel that runs with [channel-only access](/docs/claude-tag/admins/restrict-access#how-channel-only-works) because a guest is present, and in a channel shared with another company
* **Cost**: a channel thread in fast mode bills to your organization like other [channel work](/docs/claude-tag/admins/set-spend-limit#how-claude-tag-usage-is-billed), at the [fast mode rates](https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff)

## Configure the environment for a scope

Claude runs every channel session in a sandbox that starts with a standard set of tools. When a channel's work needs something that sandbox doesn't have, such as a language runtime, a database client, a set of environment variables, or broader web access, give the channel an environment. An environment is an [organization-shared cloud environment](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments): you create it once, then choose it on a scope, meaning a channel, a workspace, or the **Slack** page for your whole organization. Both steps take an Owner; a [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can't change a channel's environment.

### Decide what goes in the environment

An environment carries a setup script, environment variables, and a network access level. Not everything a channel needs belongs there, so match each need to its place before you create one:

| What the channel needs | Where to put it |
| :- | :- |
| A tool installed before Claude starts, such as a runtime or a database client | The environment's setup script, a Bash script whose installs are on disk before Claude starts work |
| A value every session should see, such as a deployment target or a feature flag | The environment's environment variables, as `KEY=value` pairs, one per line |
| Web access without a credential | The environment's network access level; see [broad web access through the environment](/docs/claude-tag/admins/add-connections#broad-web-access-through-the-environment) |
| An API key, token, or other credential | A [connector](/docs/claude-tag/admins/add-connections), never an environment variable |
| Setup for one repository, such as installing its dependencies | That repository's `CLAUDE.md`; see [install project dependencies](/docs/claude-tag/admins/configure-github#install-project-dependencies) |

Keep credentials out of environment variables because every session on the environment reads them and Claude can print them. There is no separate secrets store. A connector stores the credential outside the sandbox and attaches it to matching requests at the network layer, so Claude uses the service without holding the raw value. [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) describes how. A connector in a bundle also travels with that bundle, so you choose channel by channel which sessions can use it. Repository-specific setup goes in `CLAUDE.md` so the people who maintain the repository keep it current. Claude reads it when it starts work in that repository.

### Create the environment and choose it on a scope

Creating the environment and choosing it on a scope happen on two different admin pages. Choose it on a channel to change only that channel's sessions, on a workspace to cover every channel in the workspace where you haven't chosen one, or on the **Slack** page to cover every workspace.

<Steps>
  <Step title="Create the environment">
    From the **Cloud environments** page in [admin settings](https://claude.ai/admin-settings), add an [organization-shared environment](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments) and fill in its setup script, environment variables, and network access level.
  </Step>

  <Step title="Set the scope's environment">
    Go to [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels) and open the scope's page (**Slack** for the whole organization). On its **Advanced** tab, pick the environment in **Environment** under **Sessions**.
  </Step>

  <Step title="Confirm the environment in a new thread">
    Start a fresh thread in the channel and ask Claude to use what you added, such as running the tool your setup script installed. Threads already underway keep the environment they started on, so an existing thread won't show the change.
  </Step>
</Steps>

### Which environment a channel's sessions use

When a session starts, Claude uses the first environment it finds, in this order:

1. The channel's **Environment** setting
2. The workspace's **Environment** setting
3. The **Environment** setting on the **Slack** page
4. The [organization's default environment](https://code.claude.com/docs/en/cloud-environments#the-default-environment), which an Owner chooses under **Cloud sessions** at [`claude.ai/admin-settings/claude-code`](https://claude.ai/admin-settings/claude-code)

If you haven't chosen an environment on a scope, its picker shows **Organization default**, but sessions there may still run on an environment you chose on the workspace or on the **Slack** page. In a channel where Claude runs with [channel-only access](/docs/claude-tag/admins/restrict-access#how-channel-only-works) because a guest is present, sessions run on the standard environment regardless of these settings. If a channel's sessions aren't on the environment you expect, see [channel sessions use the wrong environment](/docs/claude-tag/admins/troubleshooting#channel-sessions-use-the-wrong-environment-or-can%E2%80%99t-find-one).

## Auto mode allow rules

Sessions run in [auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode), where Claude's permission checker reviews each action Claude is about to take and can flag or stop it. When you add an auto mode allow rule to a scope, you pre-approve one action in that scope's sessions, so Claude runs it there without the checker stopping it. The checker keeps reviewing every other action.

A rule is a plain sentence that describes work you approve in the scope, such as "Deploying to our staging cluster from a session in this channel is a normal, approved workflow." To add one:

1. Go to [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels) and open the page of the scope you want to change: **Slack** for the whole organization, a workspace, or a channel.
2. Open the page's **Advanced** tab and find **Auto mode allow rules** under **Sessions**.
3. Select **Add rule** and write the rule as one plain sentence.

The rules list has three properties:

* **Limits:** a scope holds up to 50 rules, and each rule can be up to 1,024 characters
* **Inheritance:** rules you set on a workspace or on the [**Slack** page](/docs/claude-tag/admins/attach-to-scope#how-scopes-inherit) (the organization-wide root) carry down to the channels beneath, the way [custom instructions](/docs/claude-tag/admins/attach-to-scope#custom-instructions) stack. A channel's own rules add to those and never replace them, so put a rule on a single channel's scope to pre-approve an action there without changing any other channel.
* **Access:** you edit the list with the same admin access as the scope's other **Advanced** settings

<Warning>Once you add an allow rule, Claude runs the actions it names in every channel the scope covers without anyone approving them in the moment. Keep each rule narrow: name the tool, the action, and the environment it allows, and put rules that unlock sensitive systems on the narrowest scope that needs them.</Warning>

## Name, handle, and avatar of the Claude app

The Claude app's name, @-handle, and avatar in Slack are the same in every workspace; there is no rename or rebrand setting.

## Related resources

* [Settings map](/docs/claude-tag/concepts/settings-map): every settings surface, including spend limits and personal connectors
* [What Claude Tag remembers](/docs/claude-tag/users/memory): how channel instructions are stored, shared, and corrected
* [Good habits for working with Claude Tag](/docs/claude-tag/users/good-habits): phrasings that make recurring output consistent
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why access is set per channel
