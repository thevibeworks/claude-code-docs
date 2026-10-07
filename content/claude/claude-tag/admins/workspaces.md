> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage workspaces and versions

> Connect more Slack workspaces or an Enterprise Grid to Claude Tag, choose which Claude Tag version each channel uses, and disconnect a workspace.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

This page covers managing Slack workspace pairings after initial setup: adding more workspaces, installing the app and pairing across a Slack Enterprise Grid, choosing which Claude Tag version each one runs, turning Claude on or off on the Team plan, and disconnecting a workspace.

A workspace pairing links one Slack workspace (or Enterprise Grid) to your Claude organization so `@Claude` can run there. Your first pairing was created during [setup](/docs/claude-tag/admins/setup-overview). To add more, you must be an Owner in your Claude organization, and a Workspace Admin (or Grid Org Admin) in the Slack workspace you're adding.

## Pair another workspace

You can connect multiple Slack workspaces to one Claude organization.

A Slack workspace or Enterprise Grid pairs with one Claude organization at a time.

To move a pairing to a different Claude organization, an Owner in the organization that currently holds it must [disconnect it](#revoke-a-pairing) first. Until then, Claude Tag refuses the new pairing as [already connected to a different organization](/docs/claude-tag/admins/troubleshooting#already-connected-to-a-different-organization). Once the pairing moves, changes the previous organization's admins make in their settings no longer reach that workspace.

If your company has more than one Claude organization (a subsidiary with its own, for example), agree on which one holds the pairing before connecting.

<Steps>
  <Step title="Open the pairing dialog">
    Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack). On the **General** tab, under **Connected workspaces**, click **Connect new**.
  </Step>

  <Step title="Get a pairing code from Slack">
    In any channel of the new workspace, send `@Claude connect` with no other text, as a new top-level message or in a thread where Claude isn't already working, then paste the code Claude sends you into the dialog.

    Pick a channel that belongs to just the new workspace. Claude can decline to reply in [guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels).
  </Step>

  <Step title="Finish the dialog and launch">
    Once the code is accepted, click **Next**, work through the dialog's remaining steps, and click **Launch Claude** on the last one.
  </Step>
</Steps>

<Note>If your organization used the earlier Claude in Slack app, the new workspace is added alongside your existing one, not in place of it.</Note>

**You'll see:** the new workspace in the **Connected workspaces** list with the status **Active**, and as a row on the **Channels** tab.

## Set up Claude Tag on Enterprise Grid

On Slack Enterprise Grid, installing the Claude app takes two Slack actions instead of one. A Slack Org Owner or Org Admin installs the app once for the entire Slack organization, then adds the installed app to each workspace where people will use Claude. After that, an Owner in your Claude organization pairs the whole Grid with a single Grid-wide pairing code.

### Install the app across the Grid

<Steps>
  <Step title="Sign in to a workspace in the Grid">
    As a Slack Org Owner or Org Admin, sign in to one of the Grid's workspaces rather than the Slack organization admin dashboard. Slack offers **Install to entire organization** only when you start from inside a workspace.
  </Step>

  <Step title="Install to the entire organization">
    On the [Claude for Slack](https://claude.com/claude-for-slack) listing, select **Add to Slack > Install to entire organization**.

    If some workspaces in the Grid already installed the app on their own, leave those installations in place and choose **Install to entire organization** anyway. Don't uninstall first, because uninstalling the app from a workspace [deletes that workspace's Claude data](/docs/claude-tag/concepts/data-lifecycle#actions-in-slack).
  </Step>

  <Step title="Add the app to each workspace">
    From the Slack organization admin dashboard, add the Claude app to each workspace where people will use Claude. Each workspace still needs the app added before people there can invite and mention `@Claude`.
  </Step>
</Steps>

### Pair an Enterprise Grid

To get the Grid's pairing codes, a Slack Org Owner or Org Admin sends `@Claude connect`, with no other text, in a channel of any workspace in the Grid. Claude's reply includes two codes, one beginning `enterprise_` and one beginning `workspace_`. The `enterprise_` code pairs every workspace in the Grid that isn't already paired on its own. The `workspace_` code pairs only the workspace where `@Claude connect` was sent.

Paste the `enterprise_` code in one of these places:

* **During setup:** paste the code into the **Paste the pairing code** field on the [setup page](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace)
* **After setup:** click **Connect new** under **Connected workspaces** on the **Slack** page, as in [Pair another workspace](#pair-another-workspace), and paste the code into the dialog. If a workspace you've already paired belongs to a Grid you haven't paired, the list also has an **Enterprise Grid** row with the status **Not connected**, and **Connect** on that row opens the same dialog.

<Note>Leave the workspaces you've already paired connected while you pair the Grid. They stay paired and keep their Claude data.</Note>

**You'll see:** the Grid in the **Connected workspaces** list with **Enterprise Grid** and **Active** in the **Status** column.

Claude answers a one-to-one direct message according to the pairing of the sender's home workspace, so only the Grid-wide pairing covers DMs from every workspace in the Grid.

To move the Grid-wide pairing to a different Claude organization, an Owner in the Claude organization that holds it disconnects the Grid first. Disconnecting deletes the Claude-side data listed under [Revoke a pairing](#revoke-a-pairing) for every workspace the Grid-wide pairing covered. Messages Claude already posted stay in Slack.

## Turn Claude Tag on or off and set the version for a scope

Each workspace and channel has its own page with two controls: an enable switch that turns Claude on or off there, and a **Claude Tag version** setting that chooses which version answers while it's on. On the Team plan, a [single switch on the **Slack** page](#turn-claude-tag-on-or-off-on-the-team-plan) replaces them. To open a workspace's or channel's page, go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open the **Channels** tab under **Claude's access**, and select the workspace or channel. To find a channel, search for it by name.

The enable switch, **Enable Claude Tag in this workspace** or **Enable Claude Tag in this channel**, sits at the top of the page's **General** tab. While the switch is off, Claude doesn't respond to @-mentions there. One-to-one direct messages from members who have connected a Claude account are unaffected. Turning the switch on routes the workspace or channel to **New**. To make it follow its parent again, click **Use inherited setting** under the switch.

The **Claude Tag version** setting is on the page's **Advanced** tab and is unavailable while Claude Tag is off there. Choosing **Inherit** clears the workspace's or channel's own setting entirely, so it also follows its parent for on or off.

| Label | Effect |
| :- | :- |
| **New** | Claude Tag. Bundles, skills, and custom instructions apply |
| **Legacy** | The earlier per-user Claude in Slack. Bundles and skills do not apply. Being deprecated; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) |
| **Inherit** | Use the parent's value. Not shown on the **Slack** page |

Turning off **Respond in all channels** doesn't stop Claude in a workspace or channel whose own enable switch is on. On the Enterprise plan, launching setup for a single workspace turns on that workspace's enable switch, so Claude keeps responding in that workspace. The switch is at the top of the **General** tab on the **Slack** page, which sets the default for every workspace and channel. Direct messages from members who have connected a Claude account are unaffected.

Both versions answer through the same @Claude app, so turning off a workspace's or channel's enable switch silences the Legacy version there too. To opt out of Claude Tag while keeping the earlier behavior, leave the switch on and set **Claude Tag version** to **Legacy**.

Per-scope version changes (workspace and channel) are reversible; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier).

### What each Claude Tag switch turns off

Each of these switches turns Claude off in a different part of Slack. To stop only direct messages, see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

| Switch | Where it is | When it's off |
| :- | :- | :- |
| **Enable Claude Tag in Slack** | The top of [Claude Tag admin settings](https://claude.ai/admin-settings/claude-tag) | Claude is off in every channel and in direct messages |
| **Respond in all channels** | The top of the **General** tab on the [**Slack** page](https://claude.ai/admin-settings/claude-tag/channels/slack) | Claude is off in channels, except where the channel's or its workspace's own enable switch is on |
| **Respond in channels** | The same place as **Respond in all channels**, [on the Team plan](#turn-claude-tag-on-or-off-on-the-team-plan) | Claude is off in the channels of every connected workspace |
| **Enable Claude Tag in this workspace** | The top of the **General** tab on the workspace's page | Claude is off in that workspace's channels, except a channel whose own enable switch is on |
| **Enable Claude Tag in this channel** | The top of the **General** tab on the channel's page | Claude is off in that channel |

## Turn Claude Tag on or off on the Team plan

On the [Team plan](https://claude.com/pricing), one switch turns Claude on or off in the channels of every connected Slack workspace: **Respond in channels**, at the top of the **General** tab at [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack). The switch doesn't override a workspace that was turned off on its own.

On the Enterprise plan, and in a Team organization whose Slack configuration can't be expressed as one on-or-off choice, the **Slack** page shows **Respond in all channels** instead, and each workspace and channel page has its own enable switch and **Claude Tag version** setting. A Team organization gets those controls when any of these is true:

* The **Slack** page, a workspace, or a channel is set to **Legacy**
* A workspace or channel is set to **New** on its own page
* A channel is switched off on its own page
* A bundle or connector is added directly to a channel

For those controls, see [Turn Claude Tag on or off and set the version for a scope](#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope).

### Turn Claude off in channels

Turn off **Respond in channels** on the **Slack** page. An @-mention in any channel gets "Claude is disabled in this channel" while the switch is off. One-to-one direct messages from members who have connected a Claude account keep working. To stop those too, go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), click **Edit** on the **Direct messages** row, and turn off [**Allow direct messages**](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages). For members who haven't connected an account, see [Stop direct messages from members without a Claude account](/docs/claude-tag/admins/restrict-access#stop-direct-messages-from-members-without-a-claude-account).

### Turn Claude back on

Turn on **Respond in channels** on the **Slack** page. Everything you set on the **Slack** page and on each workspace's and channel's page, such as [bundles](/docs/claude-tag/admins/attach-to-scope) and [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions), applies again. A workspace that was turned off on its own stays off, along with its channels.

### Turn Claude off for the whole organization

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and turn off the **Enable Claude Tag in Slack** switch at the top of the page. That switch turns off direct messages too.

### Keep Claude out of specific channels

The switch has no per-channel setting. Add [blocked channel patterns](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) for the channels instead.

### Notices that settings aren't applied

When a workspace's or channel's page shows a notice that its settings aren't applied, nothing you set there is lost.

| Notice | What to do |
| :- | :- |
| "These settings aren't applied while Claude Tag is disabled. They're saved and will take effect once it's enabled." | Turn on **Respond in channels** on the **Slack** page |
| "These settings aren't applied while Claude Tag is turned off for this workspace or channel; the org-wide Enable Claude Tag setting doesn't override that. They're saved and will take effect once it's turned back on." | The workspace, or the channel's workspace, was turned off on its own, and the switch doesn't override that. While you have the single switch, the admin page has no control for that workspace setting |
| "These settings aren’t applied while Claude Tag setup is incomplete for this workspace or channel." | Select the **Resume** *workspace* **setup** button beside the notice and finish that workspace's setup. On a channel's page, the button's label names the channel's workspace |

## Revoke a pairing

Go to [**Claude's access > Channels > Slack**](https://claude.ai/admin-settings/claude-tag/channels/slack). Under **Connected workspaces** on the **General** tab, click **Disconnect** on the workspace's row, type the workspace's name to confirm, and click **Disconnect**. While **Enable Claude Tag in Slack** is off, the same list appears under **Claude Tag in Slack** in Claude Tag admin settings.

Claude stops responding in that workspace's channels immediately, and your organization is no longer billed for Claude usage there. One-to-one direct messages from members who have connected a Claude account run on the member's own account, so they keep working until the deletion below removes the member's account link. A member who reconnects their account afterward can use direct messages again while the app stays installed.

<Warning>
  When you disconnect a workspace, Anthropic deletes its Claude data:

  * The workspace's sessions and their transcripts, including members' direct-message conversations with Claude in that workspace
  * Its channel, workspace, and direct-message memory
  * The routines set up in its channels, and the artifacts published from them
  * Its scopes, with their instructions and bundle bindings
  * The links between members' Slack and Claude accounts

  Deletion starts as soon as you confirm and runs to completion in the background. This can't be undone. Routines a person set up in a one-to-one direct message with Claude belong to that person's account and keep running.
</Warning>

Bundles belong to your organization, not to a workspace, so they stay available to add to other workspaces and channels; only their bindings to the deleted workspace and its channels go.

After you disconnect, the workspace leaves the **Connected workspaces** list. If it was your only connected workspace, the top of Claude Tag admin settings shows that it was disconnected from Slack, with a **Reconnect** button. **Reconnect** reopens the pairing dialog, where you redeem a fresh code from `@Claude connect`.

The Slack app stays installed, so a workspace admin can pair the workspace again by sending `@Claude connect` in it, to the same Claude organization or a different one. If you intend the data to be deleted, wait a few minutes before pairing the workspace to the same organization again, because a new pairing that arrives while the deletion is still starting can cancel it. Once the deletion has run, the new pairing starts without the deleted data. Uninstalling the app from the workspace in Slack deletes the same data, whether or not you disconnected first; see [Quiet or remove Claude Tag](/docs/claude-tag/admins/restrict-access#quiet-or-remove-claude-tag).

## Related resources

* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): what disconnecting deletes, what it keeps, and what other actions do to Claude-side data
* [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier): the upgrade path and what changes for existing users
* [Pair your Slack workspace](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace): the first pairing, with the Slack-admin handoff
