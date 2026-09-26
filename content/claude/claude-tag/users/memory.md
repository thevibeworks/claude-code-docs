> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What Claude Tag remembers

> Claude Tag memory belongs to the channel, not to you. See what each channel keeps, which notes are shared across the workspace, and how to check or correct them.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude keeps memory by channel. Each channel, public or private, has its own notes, and channel memory isn't organized by person. From a public channel Claude can also save workspace notes, which it reads in every channel in the workspace. In a direct message, Claude keeps separate notes for its conversation with you; see [Channel and workspace memory](#channel-and-workspace-memory).

Memory accumulates three ways:

* **You tell Claude.** Say "remember for this channel: reports go out as tables" and it saves the instruction. To save details from a document, [attach the file](/docs/claude-tag/users/getting-started#files-you-attach) and name what to remember. Claude saves those details, not the file.
* **Claude saves facts on its own.** While working it keeps notes like decisions the channel made.
* **Claude can read past sessions.** Ask it to look back and it lists earlier sessions in the channel and reads their transcripts; it can't full-text search across them, so name a timeframe or topic.

## Channel and workspace memory

Claude keeps two kinds of notes in a workspace. Channel notes hold what applies to one channel, such as its conventions, who owns what, and decisions made there, and Claude reads them while working in that channel. Workspace notes hold what applies across the workspace, such as organization-wide conventions. Claude can add to the workspace notes from any public channel, and it reads them in every channel in the workspace, private channels included.

A convention Claude saved as a workspace note while working in #data-eng is available when you ask in #analytics. A note it kept for #data-eng itself stays in #data-eng's channel notes.

Reading and saving follow different rules depending on where Claude is working:

| Where Claude is working | Reads from                                                 | Saves to                                                                                     |
| :---------------------- | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| Public channel          | That channel's notes and the workspace notes               | That channel's notes, or the workspace notes for something that applies across the workspace |
| Private channel         | That channel's notes, plus the workspace notes (read-only) | That channel's notes only                                                                    |

Other workspaces stay separate. Direct messages stay separate too. Claude keeps notes for each direct-message conversation, stored with the workspace rather than with your Claude account. Those notes are deleted when an Owner [disconnects the workspace](/docs/claude-tag/admins/workspaces#revoke-a-pairing), not when you disconnect your own Claude account in Slack.

If a channel switches between public and private, its channel notes stay with the channel, and Claude keeps reading and adding to them there. Workspace notes Claude saved from the channel while it was public stay in the workspace notes. If those shouldn't stay shared, ask an Owner to delete them from the workspace scope's memory files.

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
