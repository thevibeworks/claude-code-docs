> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What Claude Tag remembers

> Claude Tag memory belongs to the channel, not to you. See how public channels share workspace memory, why private channels stay isolated, and how to check or correct it.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude keeps memory by channel. Memory from public channels is shared across the workspace. What it learns working in a private channel is saved to that channel's own store, and channel memory isn't organized by person. In a direct message, Claude keeps separate notes for its conversation with you; see [Workspace memory](#workspace-memory).

Memory accumulates three ways:

* **You tell Claude.** Say "remember for this channel: reports go out as tables" and it saves the instruction.
* **Claude saves facts on its own.** While working it keeps notes like decisions the channel made.
* **Claude can read past sessions.** Ask it to look back and it lists earlier sessions in the channel and reads their transcripts; it can't full-text search across them, so name a timeframe or topic.

## Workspace memory

Memory generated in public channels is shared across the workspace automatically. A decision recorded in #data-eng is available when you ask in #analytics. You can still point it at a specific channel, like "check what #data-eng knows about this."

Reading and saving follow different rules depending on where Claude is working:

| Where Claude is working | Reads from                                               | Saves to                                                                  |
| :---------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------ |
| Public channel          | Workspace memory                                         | This channel's notes or workspace-shared, both inside the workspace store |
| Private channel         | That channel's memory, plus workspace memory (read-only) | That channel's own store                                                  |

Other workspaces stay separate. Direct messages stay separate too. Claude keeps notes for each direct-message conversation, stored with the workspace rather than with your Claude account. Those notes are deleted when an Owner [disconnects the workspace](/docs/claude-tag/admins/workspaces#revoke-a-pairing), not when you disconnect your own Claude account in Slack.

If a private channel is later made public, its accumulated memory does not move with it: new sessions there read and write the workspace store, and the memory it saved while private is no longer read by new sessions.

If a public channel is later made private, what Claude saved to workspace memory while the channel was public stays in workspace memory, where sessions in the workspace's other channels can still read it, and new sessions in the now-private channel save to the channel's own store. If those earlier entries shouldn't stay shared, ask an Owner to delete them from the workspace scope's memory files.

## Manage what Claude Tag remembers

Anyone in the channel can save, read, and correct memory by talking to Claude directly in the channel.

### Make an instruction stick

Memory is a curated note, not a transcript. To make something permanent, say so explicitly:

```text wrap theme={null}
@Claude remember for this channel: changes go to acme/data-pipeline, never acme/website, and run the lint check before opening any pull request.
```

Keep saved instructions short. Long entries crowd out everything else; memory works best holding stable facts, not a running log of events.

For longer playbooks, put them in a repository Claude can read. The documents that onboard a person to your team work as context the same way. Link the runbook, style guide, or review checklist in the channel, or store them where it can read them, instead of re-describing their contents in memory.

### Check and correct what Claude Tag remembers

Ask Claude in the channel to list everything it has saved to memory.

```text wrap theme={null}
@Claude what do you remember about this channel?
```

If something is wrong or stale, tell it to update or forget the entry. Anyone in the channel can read and change channel memory.

Two habits keep memory useful over time:

* **After correcting an entry, have Claude record the fix.** "Update your memory for this channel so this doesn't happen again" turns a one-time fix into a standing one.
* **Prune what your work has outgrown.** Entries written weeks ago can describe a repository, owner, or convention that no longer exists. Ask Claude in the channel to review its memory and drop the entries that no longer apply. For ongoing upkeep, set up a [routine](/docs/claude-tag/users/proactivity) that repeats the review on a schedule; weekly works well.

An Owner in your Claude organization can view, edit, or delete a scope's memory files at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), under the scope's options menu.

## Related resources

* [How Claude Tag works](/docs/claude-tag/concepts/how-it-works): the scope, channel, and thread model behind memory
* [Good habits](/docs/claude-tag/users/good-habits): habits that keep memory accurate
