> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Restrict where Claude Tag operates

> Claude Tag responds only where it has been added and addressed. See who can invoke it, what changes in guest and Slack Connect channels, the per-scope version setting, how to limit it to chosen channels, how to delegate administration or a channel's setup, and how to quiet or remove it.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

In channels, Claude Tag responds only where it's been added and addressed, and the controls on this page narrow that further. One-to-one DMs are a separate surface. A DM from a member who has connected a Claude account runs on that member's own account; see [how DMs differ from channels](/docs/claude-tag/concepts/agent-identity#direct-message-channels). A [DM from a member who hasn't](#direct-messages-from-members-without-a-claude-account) can bill to your organization. In a [group DM](#group-dms), the work bills to your organization.

<Note>Most controls on this page require the Owner role in your Claude organization; the [permissions table](#permissions-by-role) lists which actions a channel manager or a channel member can take. On the Enterprise plan, an Owner can delegate many of these controls through the [**Claude Tag Admin** permission](#delegate-claude-tag-administration).</Note>

## Control who can invoke Claude Tag

In channels where the app has been added, an @-mention guarantees a response; Claude may also respond to a message that doesn't mention it when it judges a reply is warranted, and once a thread is active it follows replies in that thread. By default, anyone in such a channel can address it. A single toggle narrows that to people in your Claude organization.

<a id="members" />

### Restrict who can use Claude

Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack) and open the **Advanced** tab. Under **Access**, a toggle controls who in your Slack workspace can use Claude at all; its label depends on your plan. You must be an Owner of your Claude organization to change it.

| Plan | Toggle | Off (default) | On |
| :- | :- | :- | :- |
| Enterprise | **Restrict to roles with Claude Tag access** | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only members whose role grants the **Claude Tag in Slack** capability can use Claude |
| Team | **Restrict to your organization** | Anyone in the connected Slack workspace can use Claude, even without a Claude account | Only Slack users with a Claude account in your organization can use Claude |

The toggle applies to channels and DMs alike. While the toggle is off, a [DM from a member who hasn't connected a Claude account](#direct-messages-from-members-without-a-claude-account) can bill to your organization.

<Info>
  You may see the earlier three-option **Members** dropdown instead of the toggle. The **Access** group keeps the dropdown while your organization's stored choice matches neither toggle state. That happens for an Enterprise organization that previously chose **Open to any organization member** (now marked deprecated), and for a Team organization still restricted by role from an earlier Enterprise plan. Switch to one of the toggle's two states. The dropdown is then replaced by the toggle, and the deprecated option is no longer offered.
</Info>

#### Restrict by role on Enterprise

Role restriction requires an Enterprise plan. Team plans don't have role-level control; turning on **Restrict to your organization** is the only restriction available there.

Restricting by role spans three console pages.

1. On the [**Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack) page's **Advanced** tab, turn on **Restrict to roles with Claude Tag access** under **Access**.
2. On [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups), create groups and add the relevant members.
3. On [`claude.ai/admin-settings/roles`](https://claude.ai/admin-settings/roles), create a custom role with the **Claude Tag in Slack** capability turned on or off, and choose which groups hold the role in the role editor.

Three rules govern how role restrictions resolve.

* **The toggle gates the capability.** The **Claude Tag in Slack** capability on a role has no effect until **Restrict to roles with Claude Tag access** is on. While the toggle is off, every member can use Claude regardless of what their role grants.
* **Built-in roles always grant access.** Every built-in role, including User, Owner, and Primary owner, grants **Claude Tag in Slack** automatically, so the restriction only blocks members on a custom role that doesn't grant it.
* **Any grant wins.** A member in more than one group keeps access if any of their roles grants it.

A member whose roles don't grant the capability is excluded everywhere Claude works, in three ways:

* **@-mentions and DMs get a private notice.** Claude doesn't act on the request. The member sees a notice only they can see, saying their role doesn't allow Claude Tag and to ask their admin for access.
* **Automatic replies skip them.** In channels where Claude responds without being tagged, a restricted member's messages never trigger a response.
* **Their thread replies aren't treated as requests.** In a thread an allowed member started, a restricted member's replies reach Claude marked as coming from someone who can't use it. Claude can read them as context and doesn't act on them.

On a Slack Enterprise Grid, each workspace follows the access settings of the Claude organization it's paired to. For a channel shared between workspaces that are paired to different organizations, see [Channels shared across workspaces in your Enterprise Grid](#channels-shared-across-workspaces-in-your-enterprise-grid).

### Restrict who can link a Claude account by email domain

On Enterprise plans, if your organization belongs to a parent enterprise organization, you see one more toggle in the same **Access** group on the **Slack** page's **Advanced** tab, **Restrict to your verified domains**. It needs an Owner to change. The check uses the enterprise's verified domains, which every organization under the enterprise shares.

When the toggle is on, a Slack user whose profile email isn't on one of the enterprise's verified domains can't link a Claude account to this organization; the sign-in is refused.

<Warning>Turning this on in any one organization also stops Slack users on a verified domain from linking a Claude account to any organization outside the enterprise.</Warning>

## Control where Claude Tag operates

The restriction toggle decides who can use Claude. The controls in this section decide where it works at all, from one channel up to a workspace, and which generation answers in each scope (a scope is a channel, a workspace, or your whole organization). Each scope has its own page under [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels), and the **Slack** page there holds the settings for your whole organization.

If the **Slack** page's **General** tab shows a **Respond in channels** switch rather than **Respond in all channels**, your organization has a [single on-or-off switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-on-the-team-plan) in place of the per-scope switches and version settings. The other controls in this section work the same way either way.

### Quiet or remove Claude Tag

Six ways to stop Claude Tag from responding, ordered from quietest to most complete:

1. **Ask it to stay quiet.** Saying "stay quiet in this thread unless tagged" stops Claude following an active thread.
2. **Remove it from the channel.** Run `/remove @Claude`. It can no longer read or post there.
3. **Turn off the scope's switch.**
   * **Stop Claude in one workspace or channel:** open the workspace's or channel's page on the **Channels** tab and turn off the **Enable Claude Tag in this workspace** or **Enable Claude Tag in this channel** switch at the top of its **General** tab. Claude stops responding in that scope even if someone invites it back; an @-mention gets a disabled notice instead of a reply, except in a Slack Connect channel, where Claude posts no notice. Only an Owner or a [Claude Tag admin](#delegate-claude-tag-administration) can change it.
   * **Stop Claude in every channel:** turn off the **Respond in all channels** switch at the top of the **Slack** page's **General** tab. Claude stops responding in every channel except in workspaces and channels whose own switch is on. If the **Slack** page shows **Respond in channels** instead, turning it off stops Claude in every channel of every connected workspace.
4. **Remove the channel's scope.** If the **⋯** menu on the channel's page lists **Remove this scope**, choose it. Claude deletes the channel's sessions, memory, routines, and published artifacts; see [what each action deletes](/docs/claude-tag/concepts/data-lifecycle#actions-in-claude). Where the channel's workspace has its own setting on, or has no setting of its own and the **Slack** page's setting is on, Claude keeps answering in the channel with the access it inherits from its workspace. To stop it answering in that case, run `/remove @Claude` first.
5. **Delete the bundle.** On the bundle's page, choose **Delete bundle** from its menu. This revokes its credentials everywhere it applied (the credentials are removed; memory, routines, and transcripts are not). Running sessions may keep a revoked credential for a short window before the change propagates. An Owner or a [Claude Tag admin](#delegate-claude-tag-administration) can delete a bundle, except that only an Owner can delete one a [channel rule](/docs/claude-tag/admins/attach-to-scope#attach-a-bundle-to-channels-by-name) names.
6. **Uninstall the app.** This removes Claude from the workspace and deletes the workspace's Claude data the same way [disconnecting the workspace](/docs/claude-tag/admins/workspaces#revoke-a-pairing) does.

To keep Claude out of channels by name ahead of time, add a [blocked channel pattern](#block-or-auto-join-channels-by-name) instead.

Steps 1–3 do not delete any data. Removing Claude from a channel stops it responding there; the channel's memory and routines stay on record, and re-adding Claude restores them.

Steps 4 through 6, and disconnecting the workspace, each delete something different:

* **Remove the channel's scope (step 4):** deletes the channel's sessions, memory, routines, and published artifacts; see [what each action deletes](/docs/claude-tag/concepts/data-lifecycle#actions-in-claude).
* **Delete the bundle (step 5):** removes the credentials in that bundle. Memory, routines, and session transcripts stay.
* **Uninstall the app (step 6):** Anthropic deletes the workspace's Claude data, the same set as disconnecting the workspace, plus the app's installation credential; see [what each action deletes](/docs/claude-tag/concepts/data-lifecycle#actions-in-slack).
* **[Disconnect the workspace](/docs/claude-tag/admins/workspaces#revoke-a-pairing)** at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): Anthropic deletes the workspace's sessions and transcripts, memory, routines and artifacts, scopes, and members' account links, and the app stays installed so a workspace admin can pair again; see [what each action deletes](/docs/claude-tag/concepts/data-lifecycle#actions-in-claude).

Bundles belong to your organization, not to a workspace, so uninstalling or disconnecting keeps them; only the places they apply in that workspace go. To delete one channel's data while Claude stays in the workspace, remove that channel's scope (step 4) rather than uninstalling.

### Limit Claude Tag to specific channels

To let Claude respond only in channels you choose, for example during a pilot confined to one channel, turn off **Respond in all channels** on the **Slack** page, then turn on each chosen channel's **Enable Claude Tag in this channel** switch. Both pages are on the **Channels** tab under [**Claude's access**](https://claude.ai/admin-settings/claude-tag?access=channels). One-to-one DMs, guest channels, and shared channels need more than these switches; each gets its own treatment after the steps.

These steps need the per-scope switches. If the **Slack** page shows [**Respond in channels**](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-on-the-team-plan) instead, you can't limit Claude this way. Use [blocked channel patterns](#block-or-auto-join-channels-by-name) to keep it out of specific channels.

<Note>Turning Claude off in a scope silences the earlier Claude in Slack there too.</Note>

<Steps>
  <Step title="Turn Claude Tag off in every channel">
    Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack) and turn off the **Respond in all channels** switch at the top of the **General** tab.
  </Step>

  <Step title="Reset the scopes that override it">
    Open each workspace's or channel's page that has its own setting. Its switch shows **Set for this workspace** or **Set for this channel** underneath. Click the **Use inherited setting** link beside that line. The scope then follows the off state on the **Slack** page.
  </Step>

  <Step title="Switch each chosen channel back on">
    On the **Channels** tab, find the channel with the search field; channels Claude was added to are already listed. If it isn't listed, set it up as described in [Attach to a channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel). Open the channel's page and turn on the **Enable Claude Tag in this channel** switch at the top of its **General** tab.

    A channel's own setting wins over the off setting above it, so Claude responds in the chosen channels and nowhere else.
  </Step>
</Steps>

If someone invites the app into another channel afterward, Claude stays silent there. Mentioning `@Claude` in that channel gets a notice that Claude is disabled in the channel, not a reply. In a Slack Connect channel, Claude posts no notice.

One-to-one DMs, guest channels, and shared channels sit outside the per-scope switches:

* **One-to-one DMs.** The per-scope switches don't cover one-to-one DMs from members who have connected a Claude account. To close those off too, turn off the [**Allow direct messages**](#allow-or-disable-direct-messages) toggle. For members who haven't connected an account, see [Stop direct messages from members without a Claude account](#stop-direct-messages-from-members-without-a-claude-account).
* **Guest channels.** By default Claude is off in any channel that includes a Slack guest. If a chosen channel has guests, also set [**How should Claude work in channels with guests**](#restrict-guest-channels) to **Full access** or **Channel only** on its page's **Advanced** tab.
* **Shared channels.** A [channel shared across workspaces in your Enterprise Grid](#channels-shared-across-workspaces-in-your-enterprise-grid) takes its settings from the **Slack** page only and can't serve as a chosen channel. If a chosen channel is a [Slack Connect channel](#slack-connect-channels), one shared with another company, also set **How should Claude work in channels with guests** to **Channel only** or **Full access** on its page's **Advanced** tab.

The **Enable Claude Tag** switch covers [group DMs](#group-dms), and a group DM can't serve as a chosen channel. While the switch that covers a workspace is off, Claude doesn't answer in that workspace's group DMs.

To control who can use Claude in the allowed channels, turn on the [restriction toggle](#restrict-who-can-use-claude); to cap what a channel spends, [set a per-channel spend limit](#set-spend-limits).

### Block or auto-join channels by name

**Channel name rules** steer where Claude works by channel name instead of channel by channel. The rules sit on the **Advanced** tab of the **Slack** page and of each workspace's page under [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels), in the **Channels** group, as a **Blocked channel patterns** list and an **Auto-join channels** table:

* **Blocked channel patterns**: Claude won't read or respond in a channel whose name matches, even if someone invites it there. When it's added to such a channel or @-mentioned in one, it posts a notice that an admin has blocked it there, and otherwise stays silent. In a Slack Connect channel, it posts no notice.
* **Auto-join channels**: Claude joins a public channel whose name matches one of its patterns when the channel is created or renamed. Private channels still need an invite. To add Claude to an existing channel, invite it as usual.

Each row of the **Auto-join channels** table is one pattern, added with **Add pattern**. A row can also carry [bundles](/docs/claude-tag/admins/attach-to-scope#attach-a-bundle-to-channels-by-name), which attach in every matching channel Claude is in; a row with no bundles is marked **Auto-join only**, and Claude joins matching channels whether or not a row carries bundles. A channel rule added with **Add a channel rule…** on the **Channels** tab shows up as a row here too. Editing the patterns or the bundles on a row needs an Owner of your Claude organization.

Removing a pattern row also detaches the row's bundles. A row marked **Not auto-joined** shows a pattern that still has bundles attached but that the auto-join list no longer carries. Claude joins no new channels for it, but its bundles still attach in matching channels Claude is already in; remove the bundles from the row to end that.

A pattern is written in lowercase, like Slack channel names, plus two wildcards: `*` matches any run of characters and `?` matches exactly one. `inc-*` matches every channel whose name starts with `inc-`, and `*-confidential-*` matches any name containing `-confidential-`. The blocked list and the auto-join table each hold up to 50 patterns of up to 80 characters.

A channel that matches a blocked pattern stays off-limits even when it also matches an auto-join pattern. Patterns on the **Slack** page apply in every connected workspace. A workspace scope can add its own patterns but can't remove the organization's.

About once a week, Claude sends the person who connected the workspace a direct message suggesting public channels to add it to. To stop those messages, select **Stop these suggestions** in any of them.

### Restrict guest channels

By default, Claude is disabled in any channel that includes a Slack guest. You can change this default per scope with the **How should Claude work in channels with guests** setting. It's in the **Access** group on the **Advanced** tab of the **Slack** page and of each workspace's and channel's page under [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels). It also decides whether Claude answers in [Slack Connect channels](#slack-connect-channels), where **Restrict** posts no notice. The setting has three values:

| Value | What Claude does in a channel that includes a guest |
| - | - |
| **Restrict** (default) | Doesn't reply. When someone mentions it, Claude posts a short notice that it doesn't respond in channels that include guests, with a link to this setting. |
| **Channel only** | Replies, but while a guest is present it runs with [channel-only access](#how-channel-only-works). The channel's own instructions still apply. |
| **Full access** | Replies with the full access the scope gives it. Bundles, connectors, and instructions from the workspace and from the **Slack** page apply, along with repositories, memory, and skills. |

A channel without its own value shows **Inherit** and takes the value from its workspace, or from the **Slack** page. An Owner or a [Claude Tag admin](#delegate-claude-tag-administration) can choose **Restrict** or **Channel only**. Only an organization Owner can choose **Full access** or set a scope back to **Inherit**. The setting applies to every guest channel the scope covers. To open one channel rather than a whole workspace, set it on the channel's own page.

Under every value, guests in the channel can read what Claude posts there.

Under **Restrict** and **Channel only**, Claude posts a short notice in the channel when the first guest joins a channel where it had been replying, saying how it responds while guests are present, and another when the last guest leaves, saying it's back to the channel's usual setup. Members don't have to work out from silence or a changed answer that the guest setting took effect. Claude doesn't post these notices in a channel shared across workspaces or with another company.

In any channel that includes a guest, even under **Full access**, Claude won't search the workspace, look up people or channels, or read channels other than the one it's in. The results could include content the guests can't see in Slack, which is also why Claude doesn't search private channels. To have Claude search, look someone up, or read another channel, ask from a channel without guests.

#### How Channel only works

Use **Channel only** to keep Claude available in a channel shared with contractors, clients, or agency partners without exposing the rest of the organization's setup to that conversation. While a guest is in the channel, Claude has:

* No [bundles](/docs/claude-tag/admins/attach-to-scope) inherited from the workspace or the organization. A bundle attached directly to the channel still applies.
* No connections inherited from the workspace or the organization. A connection set directly on the channel still applies.
* No repositories from the workspace or the organization.
* No instructions set on the workspace or the organization. Instructions set on the channel itself still apply.
* No memory, including this channel's own, and no skills.
* No [environment set on the scope](/docs/claude-tag/admins/customize#configure-the-environment-for-a-scope). The session runs on the standard environment, so the setup script, environment variables, and network access level of the environment you chose don't apply while a guest is present.

Claude decides which access applies when a conversation starts. When no guest is in the channel, new conversations get the same access as under **Full access**.

A conversation that was underway before the first guest joined doesn't keep its full access. The next message from a workspace member in that thread starts the conversation over with channel-only access. A guest who writes there before a member does gets the same notice as under **Restrict**.

The channel's [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting works the same while a guest is present, and it's on by default. While it's on, messages from workspace members that don't mention Claude still reach it, and Claude may reply to some of them on its own. Outside the threads Claude is part of, a guest's messages that don't mention Claude reach it only as context, not as requests. To have Claude reply only to @-mentions and in threads it's already part of, turn **Respond automatically** off for that channel.

While a guest is present, Claude doesn't publish [artifacts](/docs/claude-tag/concepts/security-and-data#artifact-visibility), the web pages hosted on claude.ai. To have Claude publish a page, ask from a channel without guests.

A guest can talk to Claude by mentioning `@Claude` or by replying in a thread Claude is part of, and Claude answers them. A guest can't approve a tool or permission request, and can't restart, mute, fork, or stop the session. If a guest clicks approve, nothing is granted.

Treat a channel's instructions, and the instructions in any bundle attached directly to the channel, as visible to everyone in that channel, including guests. Under **Channel only**, Claude follows them in replies that guests can read and respond to.

**Channel only** takes effect where the **New** [Claude Tag version](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) answers. On a scope where **Legacy** answers, a channel that includes a guest is treated as **Restrict**.

### Limit which channels Claude can search

By default, workspace search covers public channels across the workspace, including ones Claude hasn't been added to. The **Channels Claude can search** setting narrows workspace search to channels Claude is in. You set it per scope in the **Channels** group on the **Advanced** tab of the **Slack** page or of a workspace's or channel's page under [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels). Changing it needs an Owner of your Claude organization.

The setting has two values:

| Value | Where workspace search finds messages |
| - | - |
| **All public channels** (default) | Public channels in the workspace, including ones Claude hasn't been added to |
| **Only channels Claude is in** | Public channels Claude has been added to |

Most organizations can leave this on **All public channels**. Under **Only channels Claude is in**, Claude can't find messages in your other public channels, so its answers can miss context your team expects it to have.

On a workspace's or channel's page the setting also offers **Inherit**, which takes the value from the workspace or from the **Slack** page. The most specific scope that sets a value decides, in this order:

1. The channel's own value
2. The workspace's value
3. The value on the **Slack** page, which is **All public channels** until you change it

A value on a channel or workspace replaces the value it would inherit, in either direction. In a channel set to **All public channels**, workspace search covers public channels across the workspace even when the channel's workspace is set to **Only channels Claude is in**.

Neither value adds private channels to workspace search. In a [channel that includes a guest](#restrict-guest-channels), workspace search is unavailable whichever value applies.

<a id="externally-shared-channels" />

### Slack Connect channels

A Slack Connect channel is a channel your Slack workspace shares with another company. The [**How should Claude work in channels with guests**](#restrict-guest-channels) setting decides whether Claude answers in one:

* **Restrict** (default): Claude doesn't answer, and posts no notice when someone mentions it.
* **Channel only** or **Full access**: Claude answers with the [limited access it has in a Slack Connect channel](#what-access-claude-has-in-a-slack-connect-channel). **Full access** gives Claude no more access there than **Channel only**.

To turn Claude on in Slack Connect channels, go to [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels), open the **Slack** page, a workspace's page, or one channel's page, and on its **Advanced** tab set **How should Claude work in channels with guests** to **Channel only**. An Owner or a [Claude Tag admin](#delegate-claude-tag-administration) can make this change. The same value applies to the scope's channels that include guests, so a scope already set to **Channel only** or **Full access** for guests answers in its Slack Connect channels too, except in a channel with its own value. A value on the channel's own page wins over the workspace's, and the workspace's wins over the **Slack** page.

When someone who isn't a full member of your workspace adds Claude to a Slack Connect channel with no value of its own, Claude sets that channel's page to **Restrict**. That includes someone from the other company, a guest, a bot or workflow, and an [auto-join pattern](#block-or-auto-join-channels-by-name). To let Claude answer there, change the value on the channel's page.

Claude also doesn't answer in a Slack Connect channel in these cases, and posts a notice only in a thread from before the channel was shared:

* **Claude Tag turned off.** The [**Enable Claude Tag** switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) that covers the channel is off.
* **Blocked name.** The channel's name matches one of the [**Blocked channel patterns**](#block-or-auto-join-channels-by-name).
* **Legacy version.** The scope's [Claude Tag version](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) is **Legacy**.
* **Enterprise Grid organization-level installs.** Claude is installed for your whole Enterprise Grid organization rather than per workspace, and none of your own workspaces hosts the channel.
* **Threads from before the channel was shared.** Claude doesn't continue a thread it was already working in before the channel was shared. A mention there gets the notice "This channel is now shared with another organization through Slack Connect, so this thread's earlier session can't continue here," and a new thread works.
* **Messages from the other company's Claude.** Claude doesn't reply to the other company's Claude. If the other company also uses Claude, each company's settings decide only whether its own Claude answers.

#### What access Claude has in a Slack Connect channel

When Claude answers in a Slack Connect channel, it follows the channel's own instructions and has:

* No [bundles](/docs/claude-tag/admins/attach-to-scope) or connections, except a bundle an Owner [attaches directly to the channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel) after it's shared with the other company, or one attached specifically for Slack Connect channels. A bundle attached before the channel was shared, or by someone who isn't an Owner, doesn't reach it until an Owner removes it from the channel and attaches it again.
* No instructions set on the workspace or on the **Slack** page.
* No memory, skills, or repositories.
* No [environment set on the scope](/docs/claude-tag/admins/customize#configure-the-environment-for-a-scope). The session runs on the standard environment.

Treat the channel's instructions as visible to the other company. In a Slack Connect channel, Claude also doesn't search your workspace, look up people or channels, read other channels, publish [artifacts](/docs/claude-tag/concepts/security-and-data#artifact-visibility), or set up [routines](/docs/claude-tag/users/proactivity). Routines set up in the channel before it was shared don't run there.

#### Who can use Claude in a Slack Connect channel

People from the other company can talk to Claude by mentioning `@Claude` or by replying in a thread Claude is part of, and Claude answers them. Everyone in the channel, including the other company's people, can read what Claude posts.

* **Limit Claude to your organization.** Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack), open the **Advanced** tab, and turn on **Restrict to your organization** (**Restrict to roles with Claude Tag access** on Enterprise). Someone from the other company who then mentions `@Claude` to start a conversation gets a message only they can see, and in an existing thread Claude declines their request. The toggle applies to channels and DMs alike, so members of your workspace without a Claude account (on Enterprise, without a role that grants **Claude Tag in Slack**) lose access too.
* **Automatic replies.** While the channel's [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting is on, messages from your members that don't mention Claude reach it, and Claude may reply to some of them on its own. Outside the threads Claude is part of, messages from the other company's people that don't mention Claude reach it only as context, not as requests.
* **Commands.** Your organization's members can send `@Claude` followed by `!help`, `!mute`, `!unmute`, `!restart`, or `!fast`. People from the other company can use only `!help`, and other [commands](/docs/claude-tag/users/commands) do nothing there.

### Channels shared across workspaces in your Enterprise Grid

What happens in a channel shared across more than one workspace inside your Enterprise Grid depends on whether every workspace in it is connected to the same Claude organization.

When the workspaces all belong to your one Claude organization, Claude replies in the channel, but only with the access and settings on your organization's [**Slack**](/docs/claude-tag/admins/attach-to-scope) page. Bundles, instructions, and memory set on a workspace or on that channel don't reach it. Claude posts a notice in the thread explaining these limits, but not on every reply. Where guest access is at its default **Restrict**, the [guest check](#restrict-guest-channels) still runs first and can refuse the reply.

When the workspaces belong to different Claude organizations, each with its own settings and plan, Claude won't reply and posts a refusal message instead.

There is no per-channel override for either case.

### Migrate from the earlier Claude in Slack

If your organization used the earlier Claude in Slack app, the **Claude Tag version** setting on the **Advanced** tab of each scope's page chooses which generation answers `@Claude` there. Bundles only apply where the New version answers. See [Turn Claude Tag on or off and set the version for a scope](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) for the values and [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier) for the switch.

### Allow or disable direct messages

The **Allow direct messages** toggle controls whether members can message Claude in a one-to-one DM or in a [group DM](#group-dms). When it's off, Claude is reachable only in channels, and no [DM from a member without a Claude account](#direct-messages-from-members-without-a-claude-account) bills to your organization. The default is on, and you must be an Owner of your Claude organization to change it.

To change it, go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), select **Edit** on the **Direct messages** row, and turn **Allow direct messages** on or off in the dialog. The change saves as soon as you flip the toggle. **Edit** is unavailable while **Enable Claude Tag in Slack**, the switch on the same page, is off. Turning off **Respond in all channels** (or **Respond in channels**) on the **Slack** page doesn't affect direct messages from members who have connected a Claude account. For members who haven't, see [Stop direct messages from members without a Claude account](#stop-direct-messages-from-members-without-a-claude-account).

### Group DMs

A group DM is a Slack direct message among several people. When members add Claude to one, Claude acts with its own [service accounts](/docs/claude-tag/concepts/agent-identity), and the work bills to your organization's [usage balance](/docs/claude-tag/admins/set-spend-limit). [Use Claude Tag in a group DM](/docs/claude-tag/users/group-dms) covers what members can do there.

A group DM has no [scope](/docs/claude-tag/concepts/glossary#scope) of its own, so you can't attach a [bundle](/docs/claude-tag/admins/attach-to-scope) to one group DM or turn Claude off in one. You control every group DM in a workspace together:

* **Access.** Claude works with the bundles, instructions, and repositories on the workspace's page and on the **Slack** page.
* **Stop Claude from answering in group DMs.** Use either control. No setting covers group DMs alone.
  * Turn off the [**Enable Claude Tag** switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) that covers the workspace. Claude also stops answering in the channels that follow that switch.
  * Turn off the [**Allow direct messages**](#allow-or-disable-direct-messages) toggle. Claude also stops answering one-to-one DMs.
* **Who can ask.** If you [restrict who can use Claude](#restrict-who-can-use-claude), the restriction applies in group DMs too. With no restriction, a member who hasn't connected a Claude account can ask in a group DM, and the [limits on one-to-one DMs from those members](#limits-on-direct-messages-from-members-without-a-claude-account) don't apply.
* **Spend.** The organization-wide [spend limit](#set-spend-limits) caps group DM work along with channel work, and the **Default spend limit** applies to each group DM.
* **Version.** Where the **Legacy** [Claude Tag version](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) answers for the workspace, Claude doesn't respond in group DMs.

Who is in a group DM, and how Slack shares it, can change whether Claude answers:

* **A Slack guest is in the group DM.** In a workspace outside Enterprise Grid, Claude follows the [**How should Claude work in channels with guests**](#restrict-guest-channels) value on the workspace's page or on the **Slack** page. Under the default, **Restrict**, Claude posts its guest notice instead of an answer. Under **Channel only**, Claude runs with [channel-only access](#how-channel-only-works). Under **Full access**, Claude answers.
* **Someone from another company is in the group DM, through Slack Connect.** Claude doesn't answer, and no setting changes that.
* **On Enterprise Grid, the people in the group DM share no workspace.** Claude doesn't answer.

### Direct messages from members without a Claude account

A Slack workspace member who hasn't connected a Claude account can use Claude in a one-to-one DM for a limited time, billed to your organization's usage balance. When that member uses Claude in a channel, the work bills to your organization the same way, and the same [restriction toggle](#restrict-who-can-use-claude) governs both. Where the conditions in this section aren't met, Claude doesn't act on that member's DM and nothing bills to your organization. The limited time runs once for each member and starts with their first DM that Claude answers on your organization's bill.

A member's DMs bill to your organization when every one of these is true:

* **The workspace is connected to your organization.** The DMs bill the Claude organization the Slack workspace is paired to.
* **Anyone in the workspace can use Claude.** The [restriction toggle](#restrict-who-can-use-claude) is off, which is its default.
* **Direct messages are allowed.** The [**Allow direct messages**](#allow-or-disable-direct-messages) toggle is on, which is its default.
* **Claude is on for the workspace.** The workspace's [**Enable Claude Tag in this workspace** switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope) is on, or **Respond in all channels** on the **Slack** page is on when the workspace follows it. If the **Slack** page has the single [**Respond in channels** switch](/docs/claude-tag/admins/workspaces#turn-claude-tag-on-or-off-on-the-team-plan) instead, that switch is on.
* **The member is a full member of the Slack workspace.** A Slack guest's DMs don't bill to your organization.

#### Limits on direct messages from members without a Claude account

Claude stops answering a member's DMs on your organization's bill when the member reaches any one of three limits.

| Limit | Amount for each member |
| :- | :- |
| Time | 7 days from the member's first DM billed to your organization |
| Spend | \$50 of usage, or your **Default spend limit** when that amount is lower |
| Sessions | 50 sessions |

The **Default spend limit** is the one at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag) that applies to each channel without a limit of its own. When it's below \$50, each member's DMs stop at that amount. When it's 0, none of these DMs bill to your organization. This usage also counts toward your organization's [spend limit](/docs/claude-tag/admins/set-spend-limit#set-the-spend-limit). The usage page's per-channel breakdown lists channels only, so this usage doesn't appear in it.

Claude checks the limits when each message arrives, so work already running when a limit is reached can finish past it. After a member reaches a limit, their next DM gets a prompt to connect a Claude account, and after connecting, their DMs run on their own Claude account and bill to their own seat.

#### Access in a direct message from a member without a Claude account

A DM session for a member without a Claude account runs as Claude's own identity, the way a [channel session](/docs/claude-tag/concepts/agent-identity#channel-sessions) does. Two facts decide what it can reach:

* **Bundles.** The session reaches the same [bundles](/docs/claude-tag/admins/attach-to-scope) as a channel the member creates in that workspace.
* **Personal connectors.** The member has no Claude account, so the session has no [personal connectors](/docs/claude-tag/concepts/personal-connectors).

#### Daily brief offer for members without a Claude account

The first time a member opens Claude's DM, Claude's greeting can offer a short brief each morning and a wrap at the end of each day, with **Start** and **No thanks** buttons.

* **Start** sets up the two scheduled messages, which read Slack only and bill to your organization inside the same limits. If the member's 7 days haven't started, they start.
* **No thanks** sets up nothing and starts nothing. A message the member sends Claude later starts the 7 days.
* After the member reaches a limit, they get "Your daily briefs are paused. Connect your Claude account to keep them going."

#### Stop direct messages from members without a Claude account

Three controls stop Claude from answering these DMs on your organization's bill. Each one applies to members who have already started and changes something beyond these DMs.

| Control | Where | What else changes |
| :- | :- | :- |
| Turn on the restriction toggle | [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack), under **Access** on the **Advanced** tab | Members without a Claude account in your organization can't use Claude in channels either. See [Restrict who can use Claude](#restrict-who-can-use-claude) |
| Turn off the **Allow direct messages** toggle | [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), in the dialog that **Edit** on the **Direct messages** row opens | Members who have connected a Claude account can't DM Claude either |
| Turn off the workspace's **Enable Claude Tag in this workspace** switch, or, for a workspace that follows the **Slack** page, its **Respond in all channels** (or **Respond in channels**) switch | The top of the page's **General** tab. Open the workspace's page or the **Slack** page from the **Channels** tab under [**Claude's access**](https://claude.ai/admin-settings/claude-tag?access=channels) | Claude stops responding in every channel that follows that switch. One-to-one DMs from members who have connected a Claude account keep working |

To confirm the change, have a member who hasn't connected a Claude account send Claude a DM. With **Allow direct messages** off, Claude answers "Your Claude admin has disabled sending direct messages to Claude." With either of the other two controls, Claude answers with a prompt to connect a Claude account. In both cases nothing bills to your organization.

After you turn a control back on, a member who hasn't reached a limit can use Claude in DMs again, and their daily briefs resume. The 7 days keep counting while the control is off.

### Set spend limits

Spend limits live at [`claude.ai/admin-settings/usage/claude-tag`](https://claude.ai/admin-settings/usage/claude-tag), a different page than the main Claude Tag settings; see [when the usage page is available](/docs/claude-tag/admins/set-spend-limit#set-the-spend-limit). Spend trends and per-channel reports live on a separate analytics page; see [Usage analytics](#usage-analytics) below.

A spend limit is a cap on how much of your organization's usage balance Claude Tag can draw each billing period. Setting a limit doesn't fund the balance; on a Team plan, [fund the usage balance first](/docs/claude-tag/admins/set-spend-limit) or Claude won't respond in channels regardless of the limit.

* **Organization-wide limit.** Caps total Claude Tag spend across every channel.
* **Default spend limit.** A default limit applied to each channel that doesn't have its own.
* **Per-channel limits.** Set on any channel from its row in the per-channel spend table, in addition to the organization limit. A channel doesn't need its own scope to take a limit.
* **Per-channel spend.** How much each channel has spent against its limit in the current billing period, at list price, on the same page. Usage covered by a promotional credit isn't counted here and shows as \$0.00. The **Spend by channel** table at [`claude.ai/analytics/claude-tag`](https://claude.ai/analytics/claude-tag) shows list-price spend including covered usage.

Work that would exceed a limit is declined rather than silently truncated. A user blocked by a limit can request more usage from their admin in Slack, and the admin notification names whether the usage balance or the limit caused the block.

### Usage analytics

Spend trends live at [`claude.ai/analytics/claude-tag`](https://claude.ai/analytics/claude-tag), the Claude Tag section of the Analytics dashboard, refreshed once a day. It shows total and projected month-end spend for the period you pick, spend by channel with a CSV export, DM versus channel spend, [spend by kind of work](/docs/claude-tag/admins/set-spend-limit#see-spend-by-kind-of-work), and any promotional credit. Billed figures are shown after your discount. Anyone with permission to view your organization's Analytics dashboard can open it; it has no controls, so use the usage page to change a limit. The two pages link to each other.

When the period you pick falls within the current month, the **Spend by channel** table shows a **Billed** column and a **List price** column. Usage covered by a promotional credit shows as \$0.00 under **Billed** and at its list price under **List price**.

## Delegate Claude Tag administration

On the Enterprise plan, the **Claude Tag Admin** permission lets a member of your Claude organization administer Claude Tag without the Owner role. It's a permission in [custom roles](https://claude.ai/admin-settings/roles), listed under **Product admin** in the role editor; an Owner sets it up. To delegate the setup of one channel instead, add a [channel manager](#delegate-channel-setup-to-channel-managers).

A member whose custom role includes the permission is a Claude Tag admin. A Claude Tag admin can:

* Create and edit [bundles](/docs/claude-tag/admins/add-connections), including their credentials, domain entries, and repository grants, and attach bundles to the organization, a workspace, or a channel
* Edit workspace and channel settings at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), such as custom instructions and the default model
* Turn Claude on or off for a workspace or a channel with its **Enable Claude Tag** switch, or for every channel with the **Respond in all channels** switch on the **Slack** page
* Add and remove [channel managers](#delegate-channel-setup-to-channel-managers), if the role also sets **Identity & Access** to **Can manage**
* Set up [**Managed by**](/docs/claude-tag/admins/managed-by) for a channel, on the **Admin** tab of the channel's Configure page
* Open [on-call setup](/docs/claude-tag/admins/setup-oncall) at [`claude.ai/oncall`](https://claude.ai/oncall)
* Set a scope's [**How should Claude work in channels with guests**](#restrict-guest-channels) setting to **Restrict** or **Channel only**; choosing **Full access** or setting a scope back to **Inherit** stays with Owners

Some actions stay outside the permission:

* **Owner-only**: the **Enable Claude Tag in Slack** switch, the [**Allow direct messages**](#allow-or-disable-direct-messages) toggle, the [restriction toggle](#restrict-who-can-use-claude), pairing or disconnecting workspaces, [channel name patterns](#block-or-auto-join-channels-by-name) and the bundles on them, and the [**Channels Claude can search**](#limit-which-channels-claude-can-search) setting
* **The Claude GitHub App**: [installing the app](/docs/claude-tag/admins/configure-github) needs an owner of your GitHub organization
* **Spend limits and usage analytics**: [usage analytics](#usage-analytics) is open to anyone with permission to view your organization's Analytics dashboard; [spend limits](/docs/claude-tag/admins/set-spend-limit) live on the usage page

### Give a member the Claude Tag Admin permission

<Steps>
  <Step title="Create a role">
    Go to [**Organization settings > Roles**](https://claude.ai/admin-settings/roles), select **Add role**, and give the role a name.
  </Step>

  <Step title="Grant the permission">
    On the role's **Admin permissions** tab, set **Claude Tag Admin**, under **Product admin**, to **Can manage**. Changing the member's role type to **Custom** takes them off the built-in Admin role, so if the member is an Admin today, also set **User Management** to **Can manage** and **Analytics** to **Can view**, both under **Organization admin**. Leave the **Capabilities** and **Connectors** tabs as they are, then select **Save**.
  </Step>

  <Step title="Assign the role through a group">
    A custom role applies to the members of the groups it's assigned to. Go to [**Organization settings > Groups**](https://claude.ai/admin-settings/groups) and select **Add group**. Name the group and pick the new role under **Roles**. Add the member under **Members**, then select **Add group**. To use a group the member is already in, open the role on the [**Roles** page](https://claude.ai/admin-settings/roles) instead and add that group on its **Details** tab.
  </Step>

  <Step title="Change the member's role to Custom">
    On the [**Members** page](https://claude.ai/admin-settings/members), change the member's role to **Custom**. Custom roles apply only to members whose role type is **Custom**. If member roles are managed through your identity provider, make the change in the identity provider instead.
  </Step>

  <Step title="Confirm the member's access">
    The member can now open **Claude Tag** under **Products** in **Organization settings**. If it isn't listed for them yet, have them refresh the page.
  </Step>
</Steps>

## Delegate channel setup to channel managers

A channel manager is a member of your Claude organization who can set up Claude in specific channels without the Owner role. Channel managers are available on the Enterprise plan. An Owner can add or remove them, and so can a [Claude Tag admin](#delegate-claude-tag-administration) whose role also sets **Identity & Access** to **Can manage**.

You name channel managers one channel at a time. For that channel, a channel manager sets the default model, adds repositories, manages credentials and plugins in the channel's bundle, and edits channel instructions. Every other setting at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) stays with Owners; on the Enterprise plan, an Owner can delegate most of them through the [**Claude Tag Admin** permission](#delegate-claude-tag-administration).

A channel manager is a person. To let the members of another Slack channel write a channel's instructions, see [Manage a channel's instructions from another channel](/docs/claude-tag/admins/managed-by).

### What a channel manager can do on the Configure page

A channel manager has to be a member of the channel in Slack. The channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), which opens on claude.ai from the **Configure** link in any Claude reply, is split into tabs. In a channel you assigned to them, a channel manager sees the **Default model** card on the **General** tab and the repository and access bundle cards on the **Tools and access** tab. Members without the role don't see those cards. Owners and [Claude Tag admins](#delegate-claude-tag-administration) also see an **Admin** tab, whose **Channel settings** card holds some of the channel scope's settings from admin settings.

| Setting | What a channel manager can do |
| :- | :- |
| **Default model** | Choose the model new threads in the channel start on, from the models your organization allows. **Inherit** keeps the workspace or organization default |
| **Repositories** | Add repositories beyond the ones your bundles already grant the channel. They can add only repositories their own GitHub account is an admin of |
| **Access bundles** | Add, rotate, test, and remove credentials, and turn [plugins](/docs/claude-tag/admins/add-connections#attach-plugins) on or off, in the bundle Claude created for the channel and in any bundle they created for it. If the channel has no bundle yet, they can create one. They can't edit a bundle that an Owner or a [Claude Tag admin](#delegate-claude-tag-administration) created, or a bundle that other channels share |

When a channel manager adds a credential, Claude also allows the host that credential uses. Channel managers can't change the bundle's domains or rules in any other way. A channel manager can't add, change, or rotate credentials that use Claude's own identity (mutual TLS, AWS or GCP service identity, and IAP), but can delete one from the channel's bundle, including one an Owner added. If that happens, Claude loses access to that service until an Owner or a [Claude Tag admin](#delegate-claude-tag-administration) adds the credential back.

If you detach the channel's own bundle from the channel, its channel managers can't save settings for the channel; they see an error saying the channel's configuration was suspended by an administrator. They don't get a new bundle. Attach the bundle again to restore their access.

A channel manager can edit channel instructions even when the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block**.

Channel managers see their assigned channels at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag); organization and workspace settings are read-only for them. Tell them when you add them.

### Add a channel manager

Channel managers are built on [custom roles](https://claude.ai/admin-settings/roles). When you add the first manager to a channel, you create a custom role for it, named **Channel managers** plus the channel's name and ID, with the **Claude Tag channel setup** permission. A custom role works only for members on the **Custom roles** access level, so the last step below checks each manager's level.

<Steps>
  <Step title="Open the channel's page">
    Go to [**Claude's access > Channels**](https://claude.ai/admin-settings/claude-tag?access=channels) and open the channel's page. The channel must be a public or private channel. If it isn't listed, [add Claude to the channel](/docs/claude-tag/users/getting-started#add-claude-to-a-channel) in Slack first.
  </Step>

  <Step title="Add people or a group">
    In the page's header, select **Add managers**. Search for people and groups, and select each one to add. People you add join the channel's default group. A group you pick comes from [`claude.ai/admin-settings/groups`](https://claude.ai/admin-settings/groups), and the same group can manage several channels.
  </Step>

  <Step title="Check each manager's access level">
    When you add a member on the User or Claude Code user level, you move them to the **Custom roles** level in the same step; if they already hold other custom roles, you confirm the move first. For a member on any other level, you see **Not in effect** until you change their level on the Members page. Adding a group changes nobody's level.

    If you're a Claude Tag admin, the move also needs **User Management** set to **Can manage** on your role. Without it, the member is still added but shows **Not in effect** until their access level is changed on the Members page.

    If your identity provider manages access levels, you can't change a level on the Members page, and the move doesn't happen. Put the channel managers in an identity provider group and map that group to the **Custom roles** level instead. If you turn on identity provider management after adding channel managers, the next sync sets every member's level from your group mappings, so managers you moved by hand show **Not in effect** until a mapped group covers them. The role and its group are kept; you don't need to add the managers again.
  </Step>
</Steps>

Owners can already configure every channel, so you see them as **Already has full access** and can't add them.

Leave the role as it was created: assigned to its channel, with **Claude Tag channel setup** as its only permission. If the role's permissions are changed on the Roles page, the channel's **Add managers** list stops recognizing the role and refuses to add or remove any, with a notice that points you to the Roles page. To recover, set the role's permissions back to exactly **Claude Tag channel setup**; the group and its members are kept. To give channel managers any other permission, create a separate role for it.

### Remove a channel manager

To remove a channel manager, select **Add managers** on the channel's page. The current managers are listed first, each with a check mark. Select a member you added directly, or a group you added, to remove it. The member keeps their access level and any other custom roles. The manager cards on the channel's Configure page disappear for them.

### Verify a channel manager's access

In the list behind **Add managers** on the channel's page, people added directly show **Not in effect** when their access level doesn't support the role; the role works only on the **Custom roles** access level, so change the member's level on the Members page to put it into effect. An active manager sees the **Default model**, repository, and access bundle cards on the channel's [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), so asking them to open that page confirms the setup.

### Audit channel manager activity

Channel manager activity is recorded in your organization's audit log, which you read through the [Compliance API](https://platform.claude.com/docs/en/api/compliance). The log records:

* **Role channel assignments.** When a channel is assigned to a channel manager role or removed from it, with the role and the number of channels before and after.
* **Credential changes.** Each credential a channel manager creates, updates, rotates, or deletes, with the Slack workspace and channel it was for and the roles that granted the permission, so you can tell a channel manager's change from an Owner's. Secrets are never included.
* **Configure page changes.** Which settings a channel manager saved from the Configure page, such as the default model, repositories, or channel instructions. The log records which fields changed, not the values entered.

The [**Activity** page](/docs/claude-tag/admins/audit) at [`claude.ai/admin-settings/claude-tag/audit`](https://claude.ai/admin-settings/claude-tag/audit) doesn't list these events; it covers scheduled work, memory, and network events.

## Permissions by role

Creating bundles and binding them to scopes need an Owner or a [Claude Tag admin](#delegate-claude-tag-administration). Pairing workspaces needs an Owner. Editing [channel name patterns](#block-or-auto-join-channels-by-name) and changing [which channels Claude can search](#limit-which-channels-claude-can-search) need an Owner too.

A [channel manager](#delegate-channel-setup-to-channel-managers) configures only the channels assigned to them. Everything else happens inside the channel and is open to its members. The built-in **Admin** role doesn't include the **Claude Tag Admin** permission. A member with that role can take the actions in the Channel member column, in channels they belong to.

The table lists each action and who can take it, with no column for Claude Tag admins; the actions that permission covers are listed under [Delegate Claude Tag administration](#delegate-claude-tag-administration).

| Action | Owner | Channel manager | Channel member |
| :- | :- | :- | :- |
| Pair a workspace | Yes | No | No |
| Create, edit, or delete a bundle, or choose where it applies | Yes | Only to create a bundle for an assigned channel | No |
| Edit a bundle's repositories, domains, or instructions | Yes | No | No |
| Edit a bundle's credentials or plugins | Yes | Yes, in a bundle created for an assigned channel | No |
| Add or delete a [channel rule](/docs/claude-tag/admins/attach-to-scope#attach-a-bundle-to-channels-by-name), or change the bundles on one | Yes | No | No |
| Set guest channels to **Full access** or back to **Inherit** | Yes | No | No |
| Change other settings on a scope's page, such as instructions, model, and the **Enable Claude Tag** switch | Yes | No | No |
| Add a channel manager | Yes | No | No |
| Set a channel's default model or repositories from the Configure page | Yes | Yes, in assigned channels | No |
| Set a channel's default model by asking Claude in a thread, unless the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block** | Yes | Yes | Yes |
| Turn a channel's [**Respond automatically**](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting on or off | Yes | Yes, in assigned channels | Yes, unless the scope's [**Channel member edits**](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting is **Block** |
| Write channel memory | Yes, in the channel | Yes, in the channel | Yes |
| Set channel instructions from the Configure link | Yes | Yes, in assigned channels | Yes, unless the scope's [Channel member edits](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) setting blocks it |
| Create, list, or disable a scheduled job in the channel | Yes, in the channel | Yes, in the channel | Yes |
| Remove Claude from a channel | Yes | Yes, with `/remove`, unless your Slack admin restricts it | Yes, with `/remove`, unless your Slack admin restricts it |

Scheduled jobs run with the channel's credentials, so a member creating one can't reach anything the channel itself can't.

## Controls that aren't available

These are controls an admin might look for that Claude Tag doesn't have.

* **Third-party deployment.** Claude Tag runs on Anthropic's first-party service; it isn't available through third-party deployments.
* **Renaming or rebranding the app.** The Claude app's name, @-handle, and avatar in Slack are fixed; there is no per-workspace rename setting.
* **Per-user spend caps on channel work.** Spend limits apply at the organization and channel level. There's no way to cap what one member can spend in channels; one-to-one DM usage from a member who has connected a Claude account bills to that member's own seat and follows the seat's usual limits.
* **A switch for group DMs alone, or settings for one group DM.** You can't attach a bundle to one group DM, turn Claude off in one, or stop Claude from answering in group DMs without also stopping it in one-to-one DMs or the workspace's channels. See [Group DMs](#group-dms).
* **Per-channel responder allowlist.** The restriction toggle governs who can invoke Claude across the workspace; you can't narrow it to a list of people for one channel only.
* **An open-internet switch in Claude Tag settings.** A channel sandbox reaches only allowed hosts. To let Claude reach a public site or API, an Owner or a [Claude Tag admin](#delegate-claude-tag-administration) [adds that hostname to a bundle as a domain](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential); for broad web access, an Owner pins an [environment](/docs/claude-tag/concepts/glossary#environment) whose network access level is Full access on the scope. [Allow-all egress](/docs/claude-tag/admins/add-connections#allow-all-hosts), a `*` domain entry, admits any host on the ports it lists.
* **A web search toggle for channels.** No setting turns web search off for channel sessions; the web search capability setting in claude.ai admin settings governs claude.ai chat, not channels. Web search runs on Anthropic's servers rather than from the channel sandbox, so Domains entries and egress settings don't govern it, and a search opens no new path out of the sandbox; search requests travel to Anthropic the same way the session's model traffic already does. See [Web search vs. network requests](/docs/claude-tag/concepts/agent-identity#web-search-vs-network-requests).
* **A switch to turn workspace search off.** Claude can search public channels by keyword the same way any Slack user can; it can't read a channel's full history unless it's been added there. No setting turns workspace search off. The [**Channels Claude can search**](#limit-which-channels-claude-can-search) setting narrows it to channels Claude is in. No setting enables search in [channels that include guests](#restrict-guest-channels), where it's unavailable.
* **Session length enforcement.** Your organization's Slack session-length policy is not enforced on this surface.

## Related resources

* [Configure per-channel access](/docs/claude-tag/admins/attach-to-scope): change the scopes these controls apply to
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): the model these controls operate on
* [Security and data handling](/docs/claude-tag/concepts/security-and-data): what these controls don't cover (data flow, retention, where credentials are stored)
* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): which of these controls delete data and which only stop Claude responding
