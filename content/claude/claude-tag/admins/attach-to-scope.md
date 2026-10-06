> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure per-channel access

> Choose which Slack workspaces and channels a Claude Tag bundle applies to, attach bundles to channels by name, and see how access stacks when bundles overlap.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

A bundle applies at one of three levels, called scopes, and each has its own page on the **Channels** tab under **Claude's access** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). The **Slack** page covers every connected workspace and channel, a workspace's page covers the channels in that workspace, and a channel's page covers one channel. Bundles inherit downward through those scopes, and when credentials overlap, Claude uses the one from the narrowest scope.

An Owner in your Claude organization, or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration), can choose where a bundle applies. Attaching a bundle to channels by name needs an Owner.

This page assumes you have already [paired a workspace](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace) and [created a bundle](/docs/claude-tag/admins/add-connections).

## How scopes inherit

Bundles stack downward. A channel gets whatever applies on the **Slack** page, plus its workspace, plus anything added to the channel itself.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/RSTtvSydy0FU_pcP/images/claude-tag/diagrams/scope-inheritance.svg?fit=max&auto=format&n=RSTtvSydy0FU_pcP&q=85&s=7a225f1cefadc49cd6efaaf093f0b041" alt="Nested boxes. The outermost box is the Slack scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the baseline. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the baseline plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the baseline, workspace, and channel bundles." width="1000" height="320" data-path="images/claude-tag/diagrams/scope-inheritance.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/RSTtvSydy0FU_pcP/images/claude-tag/diagrams/scope-inheritance-dark.svg?fit=max&auto=format&n=RSTtvSydy0FU_pcP&q=85&s=02fd9b9128af1d3c681f3883ab47223d" alt="Nested boxes. The outermost box is the Slack scope: a bundle attached here is the baseline every channel gets. Inside it, two examples. Outside the workspace box, a channel called another-team in a different workspace gets only the baseline. Inside the workspace box, which adds an optional bundle for channels inside it, two channel boxes: a public channel called general, with no channel bundle, gets the baseline plus the workspace bundle; a private channel, marked with a lock, with its own channel bundle, gets all three, the baseline, workspace, and channel bundles." width="1000" height="320" data-path="images/claude-tag/diagrams/scope-inheritance-dark.svg" />

| Scope | What it covers | Access |
| :- | :- | :- |
| **Slack** | Every connected Slack workspace and channel | The baseline set every channel gets |
| Workspace | All channels in one Slack workspace | Inherits **Slack**, plus workspace-level bundles |
| Channel | A single Slack channel, public or private | Inherits **Slack** and the workspace, plus channel-level bundles |

The same stacking applies in reverse. Removing a bundle from a channel removes only that channel's additions, and bundles on the workspace or on **Slack** still apply there.

Memory is also scoped, but differently: there is no organization-wide memory, each channel keeps its own notes, workspace notes saved from public channels are read across the workspace, and a private channel reads the workspace notes but writes only to its own store. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

One-to-one DMs from members who have connected a Claude account run under the member's own claude.ai account. See [how DMs work in this model](/docs/claude-tag/concepts/agent-identity#direct-message-channels). A [DM from a member who hasn't connected a Claude account](/docs/claude-tag/admins/restrict-access#access-in-a-direct-message-from-a-member-without-a-claude-account) reaches bundles. A [group DM](/docs/claude-tag/admins/restrict-access#group-dms) gets the bundles on the workspace's page and on the **Slack** page.

<a id="attach-the-bundle" />

## Choose where a bundle applies

A bundle applies nowhere until you add places to it. A place is **Slack**, a workspace, or a channel, the same three scopes, or a [group of channels matched by name](#attach-a-bundle-to-channels-by-name). You can add a place from either side:

* **From the bundle's page**: on the **Bundles** tab, open the bundle. Under **Where it applies**, turn on the switch for **Slack** or for a workspace, or select **Add place**, pick a channel under **Where**, and select **Add**. Then select **Save changes**.
* **From a workspace's or channel's page**: on the **Channels** tab, open the page, select **Add** under **Claude's access**, choose **Bundle**, and pick the bundle.

To stop a bundle applying somewhere, open the bundle's page and turn off that place's switch under **Where it applies**. For a workspace or channel, you can instead choose **Remove from bundle** from its row menu. Then select **Save changes**. A workspace's or channel's page lists the bundles that reach it, and each links to the bundle's page, but the page itself doesn't remove them.

The change takes full effect in new threads only. A thread already running keeps the skills, plugins, and custom instructions it started with. A connector added after a thread started still works there if you ask Claude to use the service by name. Test with a new top-level thread after changing where a bundle applies. See [What survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

At the channel's top level, outside any thread, Claude works from a single long-lived channel session. After a configuration change, Claude replaces that session on the next channel message, so top-level replies pick up the change from then on.

### Attach to a workspace

While a bundle is off for **Slack**, every paired workspace is listed under **Where it applies** on the bundle's page. Turn on the workspace's switch and select **Save changes**, or open the workspace's page on the **Channels** tab and add the bundle with **Add > Bundle** under **Claude's access**. To add another workspace, [pair it](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace) first.

### Attach to a channel

Channels Claude was added to appear on the **Channels** tab automatically, each listed under its workspace. To give one of these channels access beyond the workspace baseline, open its page and add bundles with **Add > Bundle** under **Claude's access**. A channel row shows the name an admin gave the channel's page, the channel's name in Slack, or the raw channel ID.

To find a channel, use the search field on the **Channels** tab. It matches channel names and channel IDs (pasting a channel link copied from Slack also works), and searching a workspace's name shows that workspace's channels.

In a channel shared across more than one workspace in your Enterprise Grid, bundles on the channel or its workspace don't apply. See [Channels shared across workspaces in your Enterprise Grid](/docs/claude-tag/admins/restrict-access#channels-shared-across-workspaces-in-your-enterprise-grid) for what Claude does there instead.

<Warning>A bundle attached to a public channel grants its access to anyone who joins that channel. In most Slack workspaces, anyone can join a public channel, so the channel's join policy becomes the effective access control for whatever the bundle grants. Keep elevated credentials in private channels.</Warning>

#### Set up a channel before Claude joins

A channel Claude isn't in yet has no page. To set up a public channel before Claude joins it, type at least two characters of its name in the search field. Public channels without a page are listed under **Channels Claude isn't in**. Select **Add Claude here** to create the channel's page, then add bundles to it. The page's settings apply once someone adds Claude to the channel in Slack, since selecting **Add Claude here** doesn't add Claude to the channel. For a private channel, add Claude to the channel in Slack, and its page appears on the **Channels** tab.

## Attach a bundle to channels by name

A channel rule attaches a bundle to every channel whose name matches a pattern, instead of channel by channel. Adding or removing a bundle on a pattern, or editing the patterns themselves, needs an Owner of your Claude organization.

### Add a channel rule

You can add a rule in any of three places under **Claude's access** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag):

* **The Channels tab**: select **Add**, then **Add a channel rule…**. In the dialog, choose all workspaces or one workspace under **Applies to**, enter the **Channel name pattern**, pick the **Bundle**, and select **Add**. The rule's page opens.
* **The Auto-join channels table**: on the **Advanced** tab of the **Slack** page or of a workspace's page, find **Auto-join channels** under **Channels**. Each row is one channel-name pattern. Select **Add bundle** on the pattern's row and pick the bundle. If the pattern isn't listed yet, add it with **Add pattern** first.
* **The bundle's page**: under **Where it applies**, select **Add place** and type a pattern, such as `inc-*`, under **Where**. Select the **Create channel group** option for that pattern, choose the workspace under **Applies to** if you have more than one, and select **Add**. The rule saves at once and covers that one workspace.

Whichever way you add it, the pattern is also an [auto-join pattern](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name), so Claude starts joining matching public channels when they're created or renamed. After adding or changing a rule, test with a new thread in a matching channel.

For example, if your incident channel names start with `inc-`, add a channel rule for `inc-*` with your incident-response bundle. Claude then joins each new public incident channel and has the bundle's access there.

### What a channel rule covers

A channel rule grants its bundle under these conditions:

* **Workspaces**: a rule for all workspaces, or on the **Slack** page, covers matching channels in every connected workspace. A rule on one workspace covers only that workspace's matching channels.
* **Channels Claude is already in**: the rule grants the bundle in every matching channel Claude is in under the scope, including channels it was invited to before the rule existed
* **Joining channels**: only the auto-join patterns, or an invite, add Claude to a channel. The rule itself doesn't.
* **Blocked patterns**: a channel whose name matches a [blocked pattern](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) stays off-limits even when a rule matches it

A rule's pattern has its own constraints:

* **Pattern syntax**: a rule's pattern follows the same syntax as the other [channel name patterns](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name), lowercase with `*` matching any run of characters and `?` matching exactly one
* **Number of rules**: each scope holds up to 20 channel rules
* **Organization patterns**: on a workspace's page, the **Auto-join channels** table also lists the organization's patterns, marked **Org-wide**. You can attach a bundle to an **Org-wide** pattern from the workspace's table, and that rule covers only the workspace's matching channels. You edit the pattern itself on the **Slack** page.

<Warning>A channel rule grants its bundle in every matching channel Claude is in, now or in the future, and anyone who can rename a channel can move it into or out of a pattern. Keep elevated credentials out of broad patterns, and add a [blocked channel pattern](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) for name shapes that should never carry access; a blocked channel stays off-limits whatever rules match it.</Warning>

### Where rule-attached bundles appear

Each channel rule is listed on the **Channels** tab, and its row opens the rule's page. The rule's page lists its bundles, with **Add bundle** for an Owner, and its **Matching channels** section lists the channels on the **Channels** tab whose names match the pattern. To delete the rule, an Owner chooses **Delete rule** from the page's **⋮** menu.

A channel's own page lists the bundles a rule attaches there as rows in its **Claude's access** table, alongside bundles added to the channel directly. A channel doesn't take rules of its own. To change which bundles a rule attaches, edit the rule. Rules for all workspaces and rules on the channel's workspace apply together.

## Add a single connector, repository, plugin, or skill

To give a place one item without going through a bundle, open the **Slack** page or a workspace's or channel's page from the **Channels** tab, select **Add** under **Claude's access**, and choose **Connector**, **Repository**, **Plugin**, or **Skill**. The dialog opens on that kind's tab, and its **Connectors**, **Plugins**, **Skills**, and **Repositories** tabs switch between kinds. To let Claude reach a host without a credential in that place, choose **Domain** from the same menu, as [Add a domain](/docs/claude-tag/admins/add-connections#add-a-domain) describes.

The dialog's **Connectors** tab lists the connectors already on the **Connectors** tab of **Claude's access**, and below them, under **Connect new**, services you can connect for that place; see [Add a connector](/docs/claude-tag/admins/add-connections#add-a-connection). A credential connected from a workspace's or channel's page applies only in that place, and one connected from the **Slack** page applies everywhere. The dialog's **Plugins** and **Skills** tabs list only the plugins and skills already on the **Skills and plugins** tab of **Claude's access**.

### Check or remove what a place has

The **Claude's access** table lists every connector, plugin, skill, and repository that reaches the place. A bundle from the **Bundles** tab that reaches the place has a row of its own, with the items it brings listed beneath it. The **Inheritance** column says where each bundle, and each item outside a bundle, comes from.

Some items are removed on that page, and others elsewhere:

* **A plugin, skill, or domain whose row reads Added here**: use the row's menu
* **A connector**: the row has no menu. Select the row to open the connector's page, and change where it applies under **Assign access**.
* **A repository**: the row has no menu. [Configure GitHub access](/docs/claude-tag/admins/configure-github) covers where a repository applies.

## Precedence when bundles overlap

A channel sees the **union** of every bundle that applies at the channel itself, its workspace, and **Slack**. Narrower scopes don't replace wider ones; they add to them. When two bundles in the resolved set carry rules for the same host, the rule from the narrower scope wins. Within that union, fixed rules decide which credential and which instructions apply.

### Which credential wins

When two bundles each carry a credential for the same host:

* The credential from the **narrowest scope** is used: channel beats workspace, which beats **Slack**.
* Within the same scope, the order isn't admin-configurable. Avoid binding overlapping credentials at the same scope; if you can't predict which key acts, neither can a security review.
* There is no fallback. If the winning credential gets a `401` or `403`, Claude does not retry with the next one.

### Repositories and plugins

Repository grants and plugins from every bundle that applies are combined as a union; a channel gets every repo and plugin from any bundle in its chain. To see what applies to a channel, open its page from the **Channels** tab. Its **Claude's access** table lists everything that applies there, inherited items included, as [Add a single connector, repository, plugin, or skill](#add-a-single-connector-repository-plugin-or-skill) describes.

### Custom instructions

Per-scope custom instructions are **concatenated**, **Slack** first, then workspace, then channel. A channel's instructions add to, rather than replace, what's set above it. To write them, see [Add custom instructions](#add-custom-instructions).

## Set and restrict custom instructions

[Add custom instructions](#add-custom-instructions) on a scope's page, check the [other instruction layers](#instruction-layers) that apply in the same channel, and [restrict who can edit a channel's instructions](#restrict-who-can-set-channel-instructions).

### Add custom instructions

Each scope can carry custom instructions, which are standing guidance Claude reads in every session there, like team conventions or where to file tickets. The field is on the **General** tab of each scope's page on the **Channels** tab. It's labeled **Slack instructions** on the **Slack** page, and **Workspace instructions** or **Channel instructions** on a workspace's or channel's page. The field doesn't save as you type, so save your edit from the bar that appears under it.

Channel members reach the same field for the channel scope through the **Configure** page, linked in the footer of any Claude reply in the channel, without going through admin settings. Both entry points write the same instructions, so a change from either place is visible in the other.

To let a central team write a channel's instructions from its own Slack channel, see [Manage a channel's instructions from another channel](/docs/claude-tag/admins/managed-by).

#### Instruction format

The field is plain text, inserted as written; there is no include or template syntax, and `{{include:...}}` is passed through literally. To give Claude a repository's `CLAUDE.md`, [grant the repository](/docs/claude-tag/admins/configure-github#grant-repository-access) and name it in the request; its `CLAUDE.md` loads after the clone completes.

#### What Claude reads in a channel

What Claude reads in a channel is the concatenated custom instructions of its scope chain, the instructions of each bundle that applies there, the channel's [managed instructions](/docs/claude-tag/admins/managed-by#how-managed-instructions-load) if another channel manages it, and the `CLAUDE.md` of any repository it clones. Projects in claude.ai don't apply here; Claude doesn't read a Project's instructions or knowledge in Slack, and a channel can't be pointed at a Project.

#### When a new instruction applies

A new instruction applies to sessions started after you save it. Claude reads it in every new thread right away, keeps the old text in a thread that's already running, and picks it up at the channel's top level on the next channel message, when it replaces the channel's session (see [Choose where a bundle applies](#attach-the-bundle)). Claude doesn't read a channel's instructions in another channel or in a DM. To confirm what a session is reading, start a new thread and ask Claude to repeat its admin instructions.

### Instruction layers

The table lists the kinds of standing instruction that can apply in a channel and who writes each.

| Layer | Who writes it | Where |
| :- | :- | :- |
| Custom instructions | Owner for any scope; [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) for workspace and channel scopes; channel members and [channel managers](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for the channel scope, unless members are [restricted](#restrict-who-can-set-channel-instructions) | The instructions field on a scope's page in admin settings, or the **Configure** link in any reply footer for the channel scope |
| Bundle instructions | An Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) | The **Instructions** section of the bundle's page. They apply wherever the bundle applies |
| Managed instructions | Full workspace members in one of the channel's [managing channels](/docs/claude-tag/admins/managed-by), which an Owner or a Claude Tag admin selects under **Managed by** on the channel's Configure page | By asking Claude in the managing channel and confirming the card it posts |
| Channel memory | Anyone in the channel | By telling Claude to remember |
| Task prompt | The requester | The message itself |

Channel members can shape how Claude responds in their channel through memory, but they can't change which credentials or repositories it has; that's bundle configuration. See [who controls what](/docs/claude-tag/admins/customize) for the full split.

Custom instructions are read ahead of the conversation and take priority in practice, but they're guidance, not an enforced guardrail. Don't rely on them to block actions; use access controls for that.

### Restrict who can set channel instructions

By default, anyone in a channel who is also a member of your Claude organization can edit that channel's instructions from the **Configure** link in Claude's reply footer. The **Channel member edits** setting controls this. It's under **Channels** on the **Advanced** tab of the **Slack** page and of each workspace's and channel's page.

| Option | Effect |
| :- | :- |
| **Inherit** | Follow the parent scope's setting |
| **Allow** | Members can edit channel instructions from the Configure link |
| **Block** | Members can't change channel instructions, the channel's default model, or its [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting |

A chain of scopes that all inherit resolves to **Allow**. Set **Block** on a workspace's page or on the **Slack** page to lock channel instructions across every channel beneath it. A [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can still edit instructions, change the default model, and switch the **Respond automatically** toggle from the Configure page in a channel assigned to them when **Block** is set.

## Verify the bundle is live

* The bundle's page lists the new place under **Where it applies**, and the place's page lists the bundle as a row in its **Claude's access** table.
* A test task in the pilot channel uses the bundle's connections, and the action appears in the connected service's audit log under your service account.

Repeat the steps in [Choose where a bundle applies](#attach-the-bundle) for any other workspaces and channels that need the bundle's access.

## Related resources

* [Getting started for users](/docs/claude-tag/users/getting-started): what your team does once the bundle is live
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): narrow where it responds
