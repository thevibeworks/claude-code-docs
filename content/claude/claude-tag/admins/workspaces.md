> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage workspaces and versions

> Connect more Slack workspaces or an Enterprise Grid to Claude Tag, choose which Claude version each channel uses, and disconnect a workspace.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

This page covers managing Slack workspace pairings after initial setup: adding more workspaces, choosing which Claude Tag version each one runs, turning Claude on or off on the Team plan, and disconnecting one.

A workspace pairing links one Slack workspace (or Enterprise Grid) to your Claude organization so `@Claude` can run there. Your first pairing was created during [setup](/docs/claude-tag/admins/setup-overview). To add more, you must be an Owner in your Claude organization, and a Workspace Admin (or Grid Org Admin) in the Slack workspace you're adding.

## Pair another workspace

You can connect multiple Slack workspaces to one Claude organization. After the first pairing, the page no longer opens on setup, and the Slack row appears under **Where Claude Tag works**.

The reverse doesn't hold. A Slack workspace or Enterprise Grid pairs with one Claude organization at a time.

To move a pairing to a different Claude organization, an Owner in the organization that currently holds it must [disconnect it](#revoke-a-pairing) first. Until then, the console refuses the new pairing as [already connected to a different organization](/docs/claude-tag/admins/troubleshooting#already-connected-to-a-different-organization). Once the pairing moves, changes the previous organization's admins make in their settings no longer reach that workspace.

If your company has more than one Claude organization (a subsidiary with its own, for example), agree on which one holds the pairing before connecting.

<Steps>
  <Step title="Open the pairing dialog">
    At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), under **Where Claude Tag works**, either select **+ Connect** at the top right, or open the **⋮** menu on the Slack row and select **+ Add workspace**.
  </Step>

  <Step title="Get a pairing code from Slack">
    In any channel of the new workspace, send `@Claude connect` with no other text, as a new top-level message or in a thread where Claude isn't already working, then paste the code Claude sends you into the dialog.

    Pick a channel that belongs to just the new workspace. Claude can decline to reply in [guest and shared channels](/docs/claude-tag/admins/troubleshooting#guest-and-shared-channels).
  </Step>
</Steps>

<Note>If your organization used the earlier Claude in Slack app, the dialog header reads **Switch to Claude Tag** instead of **Set up Claude Tag for your workspace**. The steps are the same, and the new workspace is added alongside your existing one, not in place of it.</Note>

**You'll see:** the new workspace in the Slack row's connected list and as a scope in the **Claude Tag's access** section.

### Pair an Enterprise Grid

When a Grid Org Owner or Org Admin sends `@Claude connect`, the reply includes two codes. The `workspace_` code pairs only the workspace it was sent from. The `enterprise_` code pairs every workspace in the grid at once; redeem it when Claude should work across the grid.

The choice matters for direct messages. On Enterprise Grid, DMs follow each user's home workspace rather than the workspace you paired, so pairing a single workspace leaves DMs unanswered for users homed in the grid's other workspaces. The `enterprise_` code covers them all.

## Set the version for a scope

Every scope routes to one of four versions. On the Team plan, a single [**Enable Claude Tag** switch](#turn-claude-tag-on-or-off-on-the-team-plan) replaces the control this section describes. The control is at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → the scope → **Advanced** → **Claude Tag version**. Channels Claude was added to appear under **Slack** automatically, and the **Search channels** field finds a channel's scope by name or ID.

| Label       | Effect                                                                                                                                                               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New**     | Claude Tag. Access bundles, skills, and custom instructions apply                                                                                                    |
| **Legacy**  | The earlier per-user Claude in Slack. Bundles and skills do not apply. Being deprecated; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) |
| **Off**     | Neither version responds to channel mentions in this scope. Direct messages are unaffected                                                                           |
| **Inherit** | Use the parent scope's value. Not shown at **Default Slack access**                                                                                                  |

Both versions answer through the same @Claude app, so **Off** turns off the Legacy version too. To opt out of Claude Tag while keeping the earlier behavior, set the scope to **Legacy**, not **Off**.

Per-scope version changes (workspace and channel) are reversible; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier).

## Turn Claude Tag on or off on the Team plan

On the [Team plan](https://claude.com/pricing), you turn Claude on or off in every connected Slack workspace with one switch, at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → **Default Slack** → **Enable Claude Tag**. The switch doesn't override a workspace set to **Off** on its own. On the Enterprise plan, and in a Team organization whose Slack configuration can't be expressed as one on-or-off choice (a scope set to **Legacy**, a workspace or channel set to **New**, a channel set to **Off**, an access bundle attached to a channel, or a migration from the earlier Claude in Slack still in progress), the workspace and channel entries under **Slack** show a **Claude Tag version** setting instead of the switch; use [Set the version for a scope](#set-the-version-for-a-scope).

### Turn Claude off in channels

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → **Default Slack** → **Enable Claude Tag** and turn the switch off. An @-mention in any channel gets "Claude is disabled in this channel" while the switch is off. Direct messages keep working. To stop those too, turn off the [**Allow direct messages**](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages) toggle.

### Turn Claude back on

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → **Default Slack** → **Enable Claude Tag** and turn the switch on. Everything you set on each scope, such as [access bundles](/docs/claude-tag/admins/attach-to-scope) and [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions), applies again. A workspace set to **Off** on its own stays off, along with its channels; the switch doesn't override a workspace's own **Off** setting.

### Turn Claude off for the whole organization

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) and turn off the **Enable Claude Tag for your organization** toggle at the top of the page, above **Claude Tag's access**. That toggle turns off direct messages too.

### Keep Claude out of specific channels

The switch has no per-channel setting. Add [blocked channel patterns](/docs/claude-tag/admins/restrict-access#block-or-auto-join-channels-by-name) for the channels instead.

### Notices that settings aren't applied

When a workspace or channel entry shows a notice that its settings aren't applied, nothing you set there is lost.

| Notice                                                                                                                                                                                                                   | What to do                                                                                                                                                                                          |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "These settings aren't applied while Claude Tag is disabled. They're saved and will take effect once it's enabled."                                                                                                      | Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag) → **Claude Tag's access** → **Slack** → **Default Slack** → **Enable Claude Tag** and turn the switch on |
| "These settings aren't applied while Claude Tag is turned off for this workspace or channel; the org-wide Enable Claude Tag setting doesn't override that. They're saved and will take effect once it's turned back on." | The workspace, or the channel's workspace, is set to **Off** on its own, and the switch doesn't override it. While you have the switch, the admin page has no control for that setting              |
| "These settings aren’t applied while Claude Tag setup is incomplete for this workspace or channel."                                                                                                                      | Select **Resume** beside the notice and finish that workspace's setup                                                                                                                               |

## Revoke a pairing

In the **Connected workspaces** list, select **Disconnect** on the workspace's row, then confirm in the dialog. Claude stops responding in that workspace's channels immediately, and your organization is no longer billed for Claude usage there. Direct messages run on each member's own Claude account, so they keep working until the deletion below removes the member's account link. A member who reconnects their account afterward can use direct messages again while the app stays installed.

<Warning>
  When you disconnect a workspace, Anthropic deletes its Claude data:

  * The workspace's sessions and their transcripts, including members' direct-message conversations with Claude in that workspace
  * Its channel, workspace, and direct-message memory
  * The routines set up in its channels, and the artifacts published from them
  * Its scopes, with their instructions and bundle bindings
  * The links between members' Slack and Claude accounts

  Deletion starts as soon as you confirm and runs to completion in the background. This can't be undone. Routines a person set up in a direct message with Claude belong to that person's account and keep running; an Owner can delete them from the [**Scheduled work** tab](/docs/claude-tag/admins/audit).
</Warning>

Access bundles belong to your organization, not to a workspace, so they stay available to attach to other scopes; only their bindings to the deleted scopes go.

After you disconnect, the Slack row under **Where Claude Tag works** shows **Disconnected** with the workspace's name, and offers a **Reconnect** action, as a button on that row and in the row's **⋮** menu. **Reconnect** reopens the pairing dialog, where you redeem a fresh code from `@Claude connect`.

The Slack app stays installed, so a workspace admin can pair the workspace again by sending `@Claude connect` in it, to the same Claude organization or a different one. If you intend the data to be deleted, wait a few minutes before pairing the workspace to the same organization again, because a new pairing that arrives while the deletion is still starting can cancel it. Once the deletion has run, the new pairing starts without the deleted data. Uninstalling the app from the workspace in Slack deletes the same data, whether or not you disconnected first; see [Quiet or remove Claude Tag](/docs/claude-tag/admins/restrict-access#quiet-or-remove-claude-tag).

## Related resources

* [Data lifecycle and deletion](/docs/claude-tag/concepts/data-lifecycle): what disconnecting deletes, what it keeps, and what other actions do to Claude-side data
* [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier): the upgrade path and what changes for existing users
* [Pair your Slack workspace](/docs/claude-tag/admins/setup-overview#pair-your-slack-workspace): the first pairing, with the Slack-admin handoff
