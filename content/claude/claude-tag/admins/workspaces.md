> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage workspaces and versions

> Connect more Slack workspaces or an Enterprise Grid to Claude Tag, choose which Claude version each channel uses, and disconnect a workspace.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

This page covers managing Slack workspace pairings after initial setup: adding more workspaces, choosing which Claude Tag version each one runs, and disconnecting one.

A workspace pairing links one Slack workspace (or Enterprise Grid) to your Claude organization so `@Claude` can run there. Your first pairing was created during [setup](/docs/claude-tag/admins/setup-overview). To add more, you must be an Owner in your Claude organization, and a Workspace Admin (or Grid Org Admin) in the Slack workspace you're adding.

## Pair another workspace

You can connect multiple Slack workspaces to one Claude organization. After the first pairing, the page no longer opens on setup, and the Slack row appears under **Where Claude Tag works**.

The reverse doesn't hold. A Slack workspace or Enterprise Grid pairs with one Claude organization at a time.

To move a pairing to a different Claude organization, an Owner in the organization that currently holds it must [disconnect it](#revoke-a-pairing) first. Until then, the console refuses the new pairing as [already connected to a different organization](/docs/claude-tag/admins/pair-workspace#if-the-console-says-“already-connected-to-a-different-organization”). Once the pairing moves, changes the previous organization's admins make in their settings no longer reach that workspace.

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

Every scope routes to one of four versions. In the **Claude Tag's access** section of admin settings, select the scope and use the **Claude Tag version** control. Channels Claude was added to appear in the section automatically, and the **Search channels** field finds a channel's scope by name or ID.

| Label       | Effect                                                                                                                                                               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New**     | Claude Tag. Access bundles, skills, and custom instructions apply                                                                                                    |
| **Legacy**  | The earlier per-user Claude in Slack. Bundles and skills do not apply. Being deprecated; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier) |
| **Off**     | Neither version responds to channel mentions in this scope. Direct messages are unaffected                                                                           |
| **Inherit** | Use the parent scope's value. Not shown at **Default Slack access**                                                                                                  |

Both versions answer through the same @Claude app, so **Off** turns off the Legacy version too. To opt out of Claude Tag while keeping the earlier behavior, set the scope to **Legacy**, not **Off**.

Per-scope version changes (workspace and channel) are reversible; see [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier).

## Revoke a pairing

In the **Connected workspaces** list, select **Disconnect** on the workspace's row, then confirm in the dialog. Claude stops responding in that workspace immediately, and your organization is no longer billed for Claude usage there.

<Warning>
  When you disconnect a workspace, Anthropic permanently deletes its Claude data within 30 days: the workspace's sessions and transcripts, its channel and workspace memory, the routines set up in its channels, its scopes with their instructions and bundle bindings, and the links between members' Slack and Claude accounts. This can't be undone. Routines a person set up in a direct message with Claude belong to that person's account and aren't deleted with the workspace.
</Warning>

Access bundles belong to your organization, not to a workspace, so they stay available to attach to other scopes; only their bindings to the deleted scopes go.

The Slack app stays installed, so a workspace admin can pair the workspace again by sending `@Claude connect` in it, to the same Claude organization or a different one. The new pairing starts without the deleted data. To remove the app from Slack as well, uninstall it from the workspace's Slack app settings; see [Quiet or remove Claude Tag](/docs/claude-tag/admins/restrict-access#quiet-or-remove-claude-tag).

## Related resources

* [Migrate from the earlier app](/docs/claude-tag/admins/migrate-from-earlier): the upgrade path and what changes for existing users
* [Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace): the first pairing, with the Slack-admin handoff
