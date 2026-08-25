> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Work from your own channel

> Create a Slack channel for you and Claude Tag alone and run your work from it. See scratch questions, digests of channels you don't follow, a weekly status digest, follow-ups chased until they close, and a handoff that covers your time away.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

A channel with just you and Claude in it works the same way any other channel does. This page is for anyone who wants a place for work that doesn't belong in any specific team's channel, like half-formed questions, personal digests, and the things you said you'd do.

## Your own channel versus a DM

A DM is the other place to work alone with Claude, and the two surfaces run on different accounts. A DM session runs with your own claude.ai connectors, the work is attributed to you (pull requests excepted; the Claude GitHub App authors those), and usage bills to your seat. What Claude does there sits outside channel and workspace memory.

Your own channel runs with the connections an admin set for it, usage bills to the organization, and what Claude learns there accumulates as [channel memory](/docs/claude-tag/users/memory) that later threads build on. [Routines](/docs/claude-tag/users/proactivity) can post there on a schedule. When scratch work turns into a team task, the thread is ready to [hand to a teammate](#hand-a-thread-to-a-teammate).

Pick a DM for personal tasks on your own connections, or for data that shouldn't run through a shared channel connection. Pick your own channel for standing work, and for anything you might later hand off or show someone. [Pick the right surface](/docs/claude-tag/users/good-habits#pick-the-right-surface) compares both against a team channel.

## Set up the channel

1. Create a Slack channel and add Claude with `/invite @Claude`. Make the channel public unless the work needs to be private, since [memory](/docs/claude-tag/users/memory) from a public channel is shared across the workspace and teammates can find and join the work. A private channel works too, and keeps its memory in its own store.
2. Ask `@Claude what can you access from this channel?`. None of the prompts below require a connection, and an admin can [add a connection](/docs/claude-tag/admins/add-connections) your work needs, like the issue tracker or GitHub.
3. Tell Claude how the channel should behave and ask it to remember, as in `@Claude remember for this channel: keep replies short, and format digests as tables`. Later sessions in the channel start from what you saved.

## Prompts to paste

Each prompt below is a Slack message. You paste it in your channel, Claude works with the channel's history and connections, and the result lands in that thread.

### Ask scratch questions

A question is half-formed, or the answer only matters to you. Ask it here instead of in a team channel.

```text wrap theme={null}
@Claude summarize the last week of #product-feedback and pull out anything about the export flow.
```

Naming a public channel works from here, since Claude's Slack search covers public channels in this workspace. For a channel's full history rather than what search finds, Claude needs to be a member of that channel too. The answers stay in your channel, where later sessions read them.

### Get a digest of channels you don't follow

Some channels matter to your work a few times a month, not daily. Have Claude watch them and post here when something is relevant.

```text wrap theme={null}
@Claude watch #product-announce, #eng-announce, and #design-announce. Once a day, post here anything relevant to the billing migration. Skip days with nothing.
```

Naming both the channels and the topic keeps the watch useful, and skipping empty days keeps this channel readable. Instead of skimming three announcement channels yourself, you read at most one post a day here.

### Track your week

Open threads pile up here the way they do in any project channel. A scheduled digest posts a weekly summary of where they all stand.

```text wrap theme={null}
@Claude every Friday at 3pm Pacific, post a digest of this channel: what closed this week, what's still open, and what hasn't moved in five days. Skip anything with a ✅ reaction.
```

Give the digest a concrete threshold, like five days without movement, and stalled work shows up without you asking for it. React ✅ to anything you consider done, and the digest drops it. Include the timezone, since schedules default to UTC. To list, edit, or cancel scheduled work later, see [manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

### Hand a thread to a teammate

Scratch work sometimes turns into a team task. Suppose a thread in this channel started as a half-formed question about the export flow, grew into a reproducible bug, and the fix now belongs to your teammate Marta. That thread is ready to share as it stands, because anyone in the channel can steer a session by replying in it. Invite Marta to the channel (for a public channel, sharing the thread link works too) and ask for a handoff summary in the thread.

```text wrap theme={null}
@Claude summarize this thread for Marta: what's been tried, what's decided, and what's still open.
```

The summary gives Marta the state of the work in one message, with the full history above it. From there the thread is hers to continue, without re-mentioning @Claude or starting over.

If the work belongs in a team channel rather than yours, fork the thread there instead of inviting Marta in. Claude starts a new thread in the channel you name with your thread as background, and leaves a link in your channel so you can follow along.

```text wrap theme={null}
@Claude !fork #export-team summarize the export-flow bug for the team: what's been tried, what's decided, and what's still open.
```

The target must be a public channel that both you and Claude are in, and your own channel must be public for the fork to run. See [Fork a thread](/docs/claude-tag/users/commands#fork-a-thread).

### Chase your open follow-ups

Claude can track the work you've committed to but might have forgotten about. When you agree to do something in another channel, forward that message to this channel, or post a short note here describing the commitment. When the work is somewhere Claude can check through this channel's connections, like a pull request review you owe, include the link.

Then schedule a weekly sweep.

```text wrap theme={null}
@Claude every Monday at 9am Pacific, read this channel and post one line per thing I said I'd do that isn't done yet, with how long it's been open. Check anything linked before calling it done. Keep listing each item until I mark it with a ✅.
```

Monday's post lists each commitment in this channel that isn't done yet. React ✅ when you finish one and it drops off the list, and everything else comes back the next Monday.

## Cover your time away

Your channel can cover for you while you're out. Before you leave, post one handoff message here and pin it. Say who's covering, where each piece of work stands, what to point people at, and what holds until you're back. Then tell Claude to answer from it and to pause the channel's standing work.

```text wrap theme={null}
@Claude I'm out next week and Marta is covering. Where things stand: the billing migration is waiting on legal, the dashboard rebuild is paused until the design review closes, and the onboarding runbook is pinned in this channel. Leave the pricing config alone until I'm back. While I'm out, when anyone asks here, answer from this message and the channel's history. Pause this channel's scheduled posts until I say I'm back.
```

While you're out, a teammate who needs to know where a piece of work stands, or who owns it, tags `@Claude` in your channel and gets the answer from the pinned handoff message, the channel's history, and [channel memory](/docs/claude-tag/users/memory). If you set a Slack status or an out-of-office reply, point people to this channel in it.

The pause covers this channel's own routines, like the Friday digest and the Monday sweep this page sets up, so scheduled posts stop piling up unread. Anyone in the channel can [list, edit, or disable its standing work](/docs/claude-tag/users/proactivity#manage-standing-work), so a teammate can turn a routine back on early if the coverage needs it.

On your first morning back, ask Claude to catch you up.

```text wrap theme={null}
@Claude I'm back. Turn this channel's scheduled posts back on, and post one list of what needs me first, in priority order, built from what happened here while I was away.
```

The reply is one list of everything that happened here while you were away, ordered by what needs your attention first.

## Related resources

<CardGroup cols={2}>
  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    List, edit, or disable the standing work this page sets up
  </Card>

  <Card title="Good habits" href="/docs/claude-tag/users/good-habits" horizontal arrow>
    Pick the right surface and write tasks that close
  </Card>
</CardGroup>
