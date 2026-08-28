> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure per-channel access

> Choose which Slack channels and workspaces a set of Claude Tag credentials applies to. Covers inheritance, overlap rules, and adding channels after setup.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

This page covers adding access to more workspaces and channels, and how access stacks when several bundles apply to the same place. It assumes you have already [paired a workspace](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace) and [created an Access bundle](/docs/claude-tag/admins/add-connections). You must be an Owner in your Claude organization to attach bundles.

A scope is where a bundle applies: **Default Slack access** (the organization-wide root), a workspace, or a single channel. Bundles inherit downward through those scopes, and when credentials overlap, the narrowest scope wins.

## How scopes inherit

Bundles stack downward. A channel gets whatever is attached at Default Slack access, plus its workspace, plus anything attached to the channel itself.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/scope-inheritance.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=673f78c6c43aceb03ed9c81a2de7b0b2" alt="Nested boxes. The outermost box is the Default Slack access scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the default bundle. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the default plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the default, workspace, and channel bundles." width="1000" height="320" data-path="images/claude-tag/diagrams/scope-inheritance.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/scope-inheritance-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=b53a534b076e6c22f0d86a81841b00a8" alt="Nested boxes. The outermost box is the Default Slack access scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the default bundle. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the default plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the default, workspace, and channel bundles." width="1000" height="320" data-path="images/claude-tag/diagrams/scope-inheritance-dark.svg" />

| Scope                | What it covers                            | Access                                                                  |
| :------------------- | :---------------------------------------- | :---------------------------------------------------------------------- |
| Default Slack access | Every Slack workspace and channel         | The baseline set every channel gets                                     |
| Workspace            | All channels in one Slack workspace       | Inherits Default Slack access, plus workspace-level bundles             |
| Channel              | A single Slack channel, public or private | Inherits Default Slack access and workspace, plus channel-level bundles |

The same stacking applies in reverse. Detaching a bundle from a channel removes only that channel's additions, and bundles attached at the workspace or Default Slack access still apply there.

Memory is also scoped, but differently: there is no organization-wide memory, public-channel entries are shared across the workspace, and a private channel reads workspace memory but writes only to its own store. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

DMs run under the user's own claude.ai account, so bundles attached here apply only in channels. See [how DMs work in this model](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

## Attach the bundle

Attaching binds the bundle to a workspace scope or to a single channel under it.

The binding takes full effect in new threads only. A thread already running keeps the skills, plugins, and custom instructions it started with. A connection added after a thread started still works there if you ask Claude to use the service by name, but Claude doesn't announce it, so test with a new top-level thread after attaching a bundle. See [What survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

At the channel's top level, outside any thread, Claude works from a single long-lived channel session. After a configuration change, Claude replaces that session on the next channel message, so top-level replies pick up the change from then on.

### Attach to a workspace

Each paired workspace already has a scope; bind a bundle in the scope's **Access bundles** section. On the **Access bundles** page in the left navigation, each bundle's card shows how many places it's used in. To see which scopes those are, open the bundle's **Manage** dialog and hover over the usage count in its footer. To add another workspace, [pair it](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace) first.

### Attach to a channel

Channels Claude was added to appear on the **Slack** tab automatically, each as a scope under its workspace. To give one of these channels access beyond the workspace baseline, select its row and bind bundles in the scope's **Access bundles** section. A channel row shows the name an admin gave the scope, the channel's name in Slack, or the raw channel ID.

To find a channel, use the **Search channels** field. It matches channel names and channel IDs (pasting a channel link copied from Slack also works), and searching a workspace's name shows that workspace's channels.

To bind one bundle to several channels in one pass, open the bundle from a scope's **Access bundles** section on the **Slack** tab and select **Add to channels**. The dialog lists channel scopes grouped by workspace, with a search field and a checkbox per channel. Check the channels you want and select **Add**. The bundle binds to each checked channel, and channels it's already bound to directly are marked **Already added**.

A channel that doesn't appear in the list yet needs a scope created for it:

1. On [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), find the workspace on the **Slack** tab under **Claude Tag's access** and select **Add channel**.
2. Paste the channel's ID into the **Channel ID** field. Channel IDs start with `C`, or with `G` for some older private channels. Copy the ID from the channel's details in Slack.
3. Save, then bind bundles in the new scope's **Access bundles** section, the same as for a workspace.

In a channel shared across more than one workspace in your Enterprise Grid, bundles bound to the channel or its workspace don't apply. See [Channels shared across workspaces in your Enterprise Grid](/docs/claude-tag/admins/restrict-access#channels-shared-across-workspaces-in-your-enterprise-grid) for what Claude does there instead.

<Warning>A bundle attached to a public channel grants its access to anyone who joins that channel. In most Slack workspaces, anyone can join a public channel, so the channel's join policy becomes the effective access control for whatever the bundle grants. Keep elevated credentials in private-channel scopes.</Warning>

### Attach a single repository or connector

To grant a single repository or connector without opening a bundle first, use the **Repositories** and **Connectors** sections on the scope's own panel and select the **+** button (**Add repo** or **Add connector**). When you save the repository or finish connecting, the item is attached to that scope.

Each connector or repository row in these sections carries an origin line that says which scope or bundle gave the scope that item.

| Origin line                | What it means                                                                                                       |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **Inherited from** *scope* | The row comes from a wider scope. When an admin-made bundle carries it, the line adds **via** and the bundle's name |
| **Attached from** *bundle* | The row was added on this scope through that admin-made bundle                                                      |

Select the scope name to open that scope, or the bundle name to open the bundle.

The grant still lives in a bundle. The item is added to the bundle that was created for that scope, or to the scope's only bundle when that bundle is bound nowhere else, and otherwise a new bundle is created for the scope. If the bundle created for the scope is now bound to other scopes too, the add is refused with a message telling you to manage that bundle's repositories and connectors in **Access bundles** instead, so adding here never widens another scope's access.

## Precedence when bundles overlap

A channel sees the **union** of every bundle bound at the channel itself, its workspace, and Default Slack access. Narrower scopes don't replace wider ones; they add to them. When two bundles in the resolved set carry rules for the same host, the rule from the narrower scope wins. Within that union, fixed rules decide which credential and which instructions apply.

### Which credential wins

When two bundles each carry a credential for the same host:

* The credential from the **narrowest scope** is used: channel beats workspace, which beats Default Slack access.
* Within the same scope, the order isn't admin-configurable. Avoid binding overlapping credentials at the same scope; if you can't predict which key acts, neither can a security review.
* There is no fallback. If the winning credential gets a `401` or `403`, Claude does not retry with the next one.

### Repositories and plugins

Repository grants and plugins from every bound bundle are combined as a union; a channel gets every repo and plugin from any bundle in its chain. The **Access summary** section, shown when a scope you select on the Slack tab has any resolved connections or repositories, lists them with the bundle each one comes from. Plugins aren't listed there. The scope's **Plugins** section shows only the plugins attached at that scope, and plugins inherited from wider scopes and from bundles apply without appearing in it.

### Custom instructions

Per-scope custom instructions are **concatenated**, Default Slack access first, then workspace, then channel. A channel's instructions add to, rather than replace, what's set above it.

### Instruction layers

Three kinds of standing instruction can apply in a channel, written by different people:

| Layer               | Who writes it                                                                                                                                                                                                                                 | Where                                                                                                    |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| Custom instructions | Owner for any scope; channel members and [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for the channel scope, unless members are [restricted](#restrict-who-can-set-channel-instructions) | The scope's panel in admin settings, or the **Configure** link in any reply footer for the channel scope |
| Channel memory      | Anyone in the channel                                                                                                                                                                                                                         | By telling Claude to remember                                                                            |
| Task prompt         | The requester                                                                                                                                                                                                                                 | The message itself                                                                                       |

Channel members can shape how Claude responds in their channel through memory, but they can't change which credentials or repositories it has; that's bundle configuration. See [who controls what](/docs/claude-tag/admins/customize) for the full split.

Custom instructions are read ahead of the conversation and take priority in practice, but they're guidance, not an enforced guardrail. Don't rely on them to block actions; use access controls for that.

### Add custom instructions

Each scope can carry custom instructions, which are standing guidance Claude reads in every session there, like team conventions or where to file tickets. The **Custom instructions** field is on the scope's panel, shown when you select the scope on the **Slack** tab in admin settings.

Channel members reach the same field for the channel scope through the **Configure** page, linked in the footer of any Claude reply in the channel, without going through admin settings. Both entry points write the same instructions, so a change from either place is visible in the other.

The field is plain text, inserted as written; there is no include or template syntax, and `{{include:...}}` is passed through literally. To give Claude a repository's `CLAUDE.md`, [grant the repository](/docs/claude-tag/admins/configure-github#grant-repository-access) and name it in the request; its `CLAUDE.md` loads after the clone completes.

What Claude reads in a channel is the concatenated custom instructions of its scope chain, plus the `CLAUDE.md` of any repository it clones. Projects in claude.ai don't apply here; Claude doesn't read a Project's instructions or knowledge in Slack, and a channel can't be pointed at a Project.

A new instruction applies to sessions started after you save it. Claude reads it in every new thread right away, keeps the old text in a thread that's already running, and picks it up at the channel's top level on the next channel message, when it replaces the channel's session (see [Attach the bundle](#attach-the-bundle)). Claude doesn't read a channel's instructions in another channel or in a DM. To confirm what a session is reading, start a new thread and ask Claude to repeat its admin instructions.

### Restrict who can set channel instructions

By default, anyone in a channel who is also a member of your Claude organization can edit that channel's instructions from the **Configure** link in Claude's reply footer. The **Channel member edits** setting in a scope's **Advanced** settings controls this.

| Option      | Effect                                                                                                                                                                                           |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inherit** | Follow the parent scope's setting                                                                                                                                                                |
| **Allow**   | Members can edit channel instructions from the Configure link                                                                                                                                    |
| **Block**   | The Configure page is read-only for members, with a note that only admins can change channel instructions. Claude also declines to make a model the channel default when anyone asks in a thread |

A chain of scopes that all inherit resolves to **Allow**. Set **Block** at the workspace or Default Slack access scope to lock channel instructions across every channel beneath it. A [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can still edit instructions and the default model from the Configure page in a channel assigned to them when **Block** is set.

## Verify the bundle is live

* The bundle card's usage count includes the new scope. To see it named, open the bundle's **Manage** dialog and hover over the count in its footer.
* A test task in the pilot channel uses the bundle's connections, and the action appears in the connected service's audit log under your service account.

Repeat the attach step for any additional scopes that need elevated access.

## Related resources

* [Getting started for users](/docs/claude-tag/users/getting-started): what your team does once the bundle is live
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): narrow where it responds
