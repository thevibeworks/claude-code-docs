> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Claude Tag works

> Each Claude Tag thread in Slack runs a working session in a sandbox. See how progress shows in the thread, how to steer mid-task, what survives between turns, and how memory is scoped.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude Tag is Claude, working inside your team's Slack channels. An organization Owner gives it its own accounts to the tools your team uses, so it arrives already able to act, and anyone in a channel can tag it into a problem without setting anything up.

When someone tags Claude in at a channel's top level, the channel's own [session](/docs/claude-tag/concepts/glossary#session) picks the message up. A task that needs investigation, tools, or a longer exchange gets a working session in a thread under the message, and that thread binds to its own session from then on. Claude works through the task and posts the result back into the conversation. The work runs in an ephemeral cloud sandbox, not on your local machine.

This page covers:

* [Walk through a session](#walk-through-a-claude-tag-session): an annotated example thread showing one task end to end
* [Starting a session](#start-a-session), [tracking progress](#track-claude%E2%80%99s-progress), and [steering mid-thread](#reply-in-the-thread-to-steer): what to type, what to watch, and who can redirect
* [Team channels and personal DMs](#team-channels-and-personal-dms): which surface to use, and how access differs between them
* [Key concepts](#key-concepts): agent identity, scheduling, and memory defined
* [Lifecycle of a request](#lifecycle-of-a-request): the five-step loop, [the checklist](#how-the-checklist-updates), [per-channel access](#channel-access), and [scheduled tasks](#one-off-and-scheduled-tasks)
* [Session context and memory](#session-context-and-memory): what Claude reads, what survives idle, and what carries across channels

## Walk through a Claude Tag session

The thread below is one task end to end in Slack: Jordan tags @Claude into `#launch-week` with a question, a colleague steers mid-thread, and the answer lands in the channel.

<div className="tm-slack">
  <div className="tm-slack-head">
    <span className="tm-slack-chan"># launch-week</span>
    <span className="tm-slack-members">19 members</span>
  </div>

  <div className="tm-slack-body">
    <div className="tm-msg">
      <span className="tm-avatar tm-avatar-user" aria-hidden="true">J</span>

      <div className="tm-msg-col">
        <div className="tm-msg-meta"><span className="tm-msg-name">Jordan</span><span className="tm-msg-time">9:02 AM</span></div>
        <p><span className="tm-mention">@Claude</span> where are we on launch prep? Pull together what's still open from this channel.</p>
      </div>
    </div>

    <div className="tm-msg">
      <span className="tm-avatar tm-avatar-claude">
        <img src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12" alt="" noZoom width="94" height="94" data-path="images/claude-tag/logo/clay-spark.svg" />
      </span>

      <div className="tm-msg-col">
        <div className="tm-msg-meta"><span className="tm-msg-name">Claude</span><span className="tm-msg-app">APP</span><span className="tm-msg-time">9:02 AM</span></div>
        <p>On it. I'll go through this channel's open threads and the launch plan.</p>

        <div className="tm-tasklist">
          <span className="tm-task-done"><span className="tm-sr">Done: </span>Read 14 open threads</span>
          <span className="tm-task-done"><span className="tm-sr">Done: </span>Cross-checked the launch plan in Drive</span>
          <span className="tm-task-done"><span className="tm-sr">Done: </span>Listed who each item is waiting on</span>
          <span className="tm-task-done"><span className="tm-sr">Done: </span>Drafted the status summary</span>
        </div>
      </div>
    </div>

    <div className="tm-msg">
      <span className="tm-avatar tm-avatar-user tm-avatar-b" aria-hidden="true">S</span>

      <div className="tm-msg-col">
        <div className="tm-msg-meta"><span className="tm-msg-name">Sam</span><span className="tm-msg-time">9:06 AM</span></div>
        <p>fold in the vendor quotes from last week's thread too</p>
      </div>
    </div>

    <div className="tm-msg">
      <span className="tm-avatar tm-avatar-claude">
        <img src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12" alt="" noZoom width="94" height="94" data-path="images/claude-tag/logo/clay-spark.svg" />
      </span>

      <div className="tm-msg-col">
        <div className="tm-msg-meta"><span className="tm-msg-name">Claude</span><span className="tm-msg-app">APP</span><span className="tm-msg-time">9:08 AM</span></div>
        <p>Done. Full status below: eight items closed, three open. The venue contract is the oldest, waiting on legal since the 2nd.</p>
      </div>
    </div>
  </div>
</div>

Each of the five moments in that thread shows a piece of how Claude Tag works:

1. **Jordan handed Claude a problem, not a prompt.** Typing `@Claude` in a message that asks for something is what starts a working session.
2. **Claude acknowledged, then went quiet.** The "is thinking…" line and the checklist are the progress surface; the silence between 9:02 and 9:06 was the work happening. [How the checklist updates](#how-the-checklist-updates)
3. **Sam steered Claude without `@`-mentioning it again.** Once a session is active in a thread, it belongs to everyone there. [Reply in the thread to steer](#reply-in-the-thread-to-steer)
4. **The work ran somewhere real, with the channel's tools.** Reading fourteen threads happened in a sandbox built for this thread, and the launch plan came through this channel's Drive connection. What a session can reach is set per channel. [Channel access](#channel-access)
5. **The result is in the thread.** The whole channel can see it, use it, and build on it. [What survives between replies](#what-survives-between-replies)

The rest of this page takes each piece apart.

### Start a session

To start a session, type `@Claude` in a Slack message and say what you need in that same message (a question to answer, a task to run, a problem to dig into). Jordan's "`@Claude` where are we on launch prep?" is the whole move. Anyone in the channel can do it.

### Track Claude's progress

Once your message sends, an "is thinking…" line at the bottom of the thread means Claude picked it up. What happens next depends on the size of the ask. Questions and one-off requests get a direct reply. A longer task, like Jordan's, gets a checklist instead. [How the checklist updates](#how-the-checklist-updates) covers how it works and how to read one while it runs.

While a session runs, check in by replying in the same thread. Asking "how's it going?" in the thread is enough; it reads new replies as it works.

### Reply in the thread to steer

Anyone in the channel can steer a running session by replying in its thread, not just the person who started it. That is what Sam did in the walkthrough. Without re-mentioning `@Claude` or starting over, he replied in Jordan's thread, and the session folded his instruction into work already in progress. Add context, redirect the approach, or pick up the result later; a colleague's thread is yours to continue.

Editing or deleting an earlier message doesn't steer the session the way a reply does:

* **Editing a message**: Claude receives a note each time you edit, showing what the message said before the edit and what it says now. Both versions become part of the session's transcript, so editing a message doesn't remove the earlier text from what Anthropic stores. An edit doesn't start a new task or re-address Claude, even if you add `@Claude` to it.
* **Deleting a reply**: Claude gets no notification and keeps the version it already read. Deleting the reply in Slack doesn't remove it from the session's transcript.
* **Deleting the thread's first message**: if the thread already has replies, Claude keeps working and the session stays open. If you delete it before anyone has replied, the session closes. Anything Claude already pushed or posted persists, per [what survives between replies](#what-survives-between-replies), and you start a new thread to pick the task back up. Closing the session archives it rather than deleting it, so its transcript, including the message you deleted, stays with the channel's Claude data until that data is [deleted](/docs/claude-tag/admins/workspaces#revoke-a-pairing).
* **Correcting course**: Claude responds to replies; edits reach it only as notes, and a deleted reply not at all. Say the change in a new reply; the reply is also how you walk back a message it already read.

## Team channels and personal DMs

Where you message Claude determines whose tools and accounts it uses. In a channel, it acts with the connections an organization admin set for that channel, and the work is attributed to its own accounts. In a DM, the same engine runs with your own claude.ai connectors, and the work is attributed to you, except pull requests, which the Claude GitHub App authors from DMs as well.

| Working in… | Access                                     | Attribution              | Best for                           |
| :---------- | :----------------------------------------- | :----------------------- | :--------------------------------- |
| A channel   | The channel's connections, set by an admin | The agent's own accounts | Shared work the team should see    |
| A DM        | Your own claude.ai connectors              | You                      | Personal tasks using your own data |

The Access column is about external systems. A channel session reaches what the channel was granted, and a DM session reaches what your own account is connected to.

Everything below describes channel sessions, where most of the model lives. For the DM side, see [direct message channels](/docs/claude-tag/concepts/agent-identity#direct-message-channels), and for choosing between the two, see [pick the right surface](/docs/claude-tag/users/good-habits#pick-the-right-surface).

## How Claude Tag differs from Cowork and Claude Code

Anthropic offers several ways to work with Claude on real tasks; they reach the same kinds of systems but through different mechanisms.

|                   | Claude Tag                                                        | Cowork                                | Claude Code                                  |
| :---------------- | :---------------------------------------------------------------- | :------------------------------------ | :------------------------------------------- |
| Where             | Slack channels                                                    | claude.ai chat                        | Your terminal or IDE                         |
| Whose access      | The team's: service-account credentials an admin sets per channel | Yours: your personal OAuth connectors | Yours: your local credentials and filesystem |
| Who sees the work | Everyone in the channel                                           | Just you                              | Just you                                     |
| Best for          | Shared work the team should see and steer                         | Personal research and drafting        | Hands-on coding in your own checkout         |

The short version: **team work → Claude Tag; personal work → Cowork or Claude Code.** Claude Tag's connections authenticate the agent itself with service accounts, not any person. Personal connectors apply in a Claude Tag DM, which runs on your own claude.ai account, the same way Cowork does.

## Key concepts

Three ideas recur across this page and the rest of these docs.

* **Agent identity**: in channels, Claude acts under its own service accounts that an admin provisions, not as the person who asked. What it can reach is set per channel, so everyone in a channel works with the same access. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).
* **Scheduling and long-running work**: a task can run on a schedule, follow a pull request and act when it changes, or keep going across many turns in one thread. The same channel access applies whether a person or a schedule started it. See [Set up routines](/docs/claude-tag/users/proactivity).
* **Memory**: what Claude learns in public channels is saved as workspace memory that any channel can use; private channels keep their own. See [What Claude remembers](/docs/claude-tag/users/memory).

## Lifecycle of a request

Every session, in any channel, follows the same five-step loop.

1. **The session starts.** Someone tags `@Claude` with a task that needs a working session, or a [scheduled routine](/docs/claude-tag/users/proactivity) runs. At a channel's top level, the channel's own session picks the message up and starts the thread's session.
2. **A sandbox builds.** Each thread gets its own isolated working environment.
3. **The working loop runs.** Claude works through the task with the channel's access, editing its checklist in place.
4. **The result lands in the thread.** An answer, a doc, a chart, or a pull request.
5. **A quiet period follows.** The sandbox is released while the thread persists; a new reply rebuilds it and starts the loop again.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-loop.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=436dd451c4ab3ab0f0b072f85051e844" alt="Flow diagram of one session in five numbered steps. Step 1, tag Claude in with an @Claude message carrying a task. Steps 2 and 3 happen inside the sandbox. Step 2, a sandbox builds, one per thread; step 3, the working loop runs through the task's steps using the channel's access. Step 4, Claude posts the result in the thread as an answer, a doc, a chart, or a pull request. Step 5, a dashed quiet period follows, where the sandbox is released while the thread persists. A dashed return arrow from the quiet period back up into the sandbox shows that a new reply rebuilds it and the loop continues." width="1000" height="400" data-path="images/claude-tag/diagrams/session-loop.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-loop-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=616c51832cbb9bc57fe6da5346c6ac85" alt="Flow diagram of one session in five numbered steps. Step 1, tag Claude in with an @Claude message carrying a task. Steps 2 and 3 happen inside the sandbox. Step 2, a sandbox builds, one per thread; step 3, the working loop runs through the task's steps using the channel's access. Step 4, Claude posts the result in the thread as an answer, a doc, a chart, or a pull request. Step 5, a dashed quiet period follows, where the sandbox is released while the thread persists. A dashed return arrow from the quiet period back up into the sandbox shows that a new reply rebuilds it and the loop continues." width="1000" height="400" data-path="images/claude-tag/diagrams/session-loop-dark.svg" />

Steps 1 and 2 are [starting a session](#start-a-session): a message tags Claude in, and a sandbox builds for that thread. Step 3, the working loop, is [the checklist](#how-the-checklist-updates) below. Steps 4 and 5, the result and the quiet period that follows, are covered in [What survives between replies](#what-survives-between-replies).

Every session runs in an ephemeral sandbox, a real working environment where Claude can read documents, run code, build charts, and open pull requests. Claude clones your GitHub repositories into the sandbox, edits them there, and pushes changes back to GitHub as a branch or pull request. The sandbox runs the same engine that powers Claude Code on the web, Anthropic's agent for writing and running code, which is why the results are working artifacts rather than chat.

Two threads in the same channel are two separate sessions with separate sandboxes; sessions don't share state directly.

A channel where Claude works at the top level, outside threads, also carries one session for the channel itself, separate from every thread's. That session reads the channel's top-level messages and handles top-level @-mentions, so context carries across separate top-level asks in the same channel; [What survives between replies](#what-survives-between-replies) covers how long it lives. For a task that needs investigation, tools, or a longer exchange, it starts a dedicated session in a thread under the message. At the channel's top level, [`!restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) replaces the channel's session.

Even with nothing connected, every session starts from the same baseline.

* It reads its own thread and the channel's history, including pinned items
* It searches the workspace's content
* It writes and runs code inside the sandbox, which is how a chart comes out of a posted CSV, or a doc out of a long thread, with nothing wired up

### What Claude posts back

Claude posts each session's result in the thread you asked in, choosing the form that fits the work.

| Form                | What it is                                              | When you see it                    |
| :------------------ | :------------------------------------------------------ | :--------------------------------- |
| A reply             | An answer, list, or summary as a Slack message          | Questions and short results        |
| A file or chart     | Attached to the thread the way anyone shares a file     | Data, images, generated documents  |
| A page kept current | Any of the above, edited in place over time             | Digests, indexes, standing reports |
| A hosted page       | A web page published on claude.ai, linked in the thread | Dashboards, prototypes, reports    |

A hosted page stays available after the session ends, and Claude updates it when you ask in the thread. Anyone with access to the channel can open it; [artifact visibility](/docs/claude-tag/concepts/security-and-data#artifact-visibility) covers the access model. These are the same artifacts [Claude Code publishes](https://code.claude.com/docs/en/artifacts), with channel-based access in place of owner-controlled sharing.

For code work, the result is usually a draft pull request opened under the Claude GitHub App, with the link posted in the thread.

### How the checklist updates

For a longer task, Claude's first reply is a checklist, a live task list that it edits in place as it goes. Slack does not send notifications when a message is edited, so the thread can look frozen while the list is still moving.

A quiet thread usually means Claude is mid-task, not stuck. Open the thread. Checklist items checked off since you last looked mean the work is moving. In the walkthrough, nothing new arrived in anyone's notifications between 9:02 and 9:06, while the checklist ticked through fourteen threads of reading. If the work hits a wall, Claude usually says so in a reply rather than going silent. When a thread stays silent well past what the task should need, treat it as a stuck session; see [Claude reacted or started thinking, then never replied](/docs/claude-tag/users/troubleshooting#claude-reacted-or-started-thinking-then-never-replied).

### Channel access

Connections extend a session's reach into your own systems. An organization admin attaches access to a scope (the organization, a workspace, or a single channel), so the same request can do more in one channel than in another, and everyone in a given channel works with the same capability.

A thread locks in its skills, plugins, and custom instructions when it starts, and a running thread keeps that set. Connections and domain rules are enforced on each request, so one an admin adds mid-thread works in a running thread. Claude doesn't announce a new connection in an existing thread; ask it to use the service by name. A new thread picks up every kind of change, so after a configuration change, start a new top-level thread.

#### How to identify access

Because access is set per channel rather than per person, the way to find out what a session can reach is to ask it, not to guess from your own permissions.

* **Ask what Claude can reach.** In any channel, `@Claude what can you access from this channel?` lists its current reach.
* **If Claude cannot reach something, the channel was not granted access.** Another channel may have the access, and an organization Owner can add it. [How agent identity works](/docs/claude-tag/concepts/agent-identity) covers the model.
* **Personal connectors apply only in DMs.** A connection an admin attaches to a channel is separate from a connector on your personal claude.ai account; anything on your own account works in your DMs, not here.

### One-off and scheduled tasks

A session starts the same way whether a person triggers it or a schedule does. A tagged task runs in its thread's session, and the sandbox is released once the work finishes. A routine runs the same loop on a schedule, a channel watch, or a repository event, with the channel's connections, so a recurring digest or watcher gets the same access a typed request would. See [set up routines](/docs/claude-tag/users/proactivity).

## Session context and memory

Every session runs the same lifecycle; what varies by place and thread is [what it can see](#conversation-context), [what survives idle](#what-survives-between-replies), and [what it remembers](#channel-and-workspace-memory).

### Conversation context

A session reads its own thread and its channel. Mentioning `@Claude` partway into an existing thread gives it a window of the thread's messages, not the whole thread, with other bots' replies filtered out. In long threads, restate anything critical.

Claude works in channels it has been added to, but workspace search can still find messages by keyword from public channels it's not a member of (the same search any Slack user has). Workspace search is unavailable in [channels that include guests](/docs/claude-tag/admins/restrict-access#restrict-guest-channels). Finding something is broader than being able to act somewhere; to have it participate in a channel directly, invite it with `/invite @Claude`.

### What survives between replies

A thread is durable, but the sandbox behind it is not. Durable means the thread stays in Slack, and everything Claude read and said in it is kept in the session's transcript on Anthropic's side, so the session can pick up where it left off whenever someone replies. Deleting messages or the thread in Slack doesn't remove them from that transcript. The sandbox is the computer where Claude runs commands and keeps working files for a task. A few minutes after a session finishes its turn, its sandbox is released, and the same session resumes in a fresh one when the next message arrives. A thread's session keeps resuming this way for as long as people use the thread. Claude replaces it with a new session in two cases.

| When                                                                                                                        | What Claude does                                                               |
| :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| Someone sends [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session)                     | Archives the session right away and starts a fresh one that rereads the thread |
| The session [gets stuck and fails](/docs/claude-tag/users/troubleshooting#claude-reacted-or-started-thinking-then-never-replied) | Starts the replacement when the next message arrives in the thread             |

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-lifecycle.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=9a56231787b03f179e8d552d887778fc" alt="Timeline with two lanes. The Slack thread lane is one continuous bar that persists from the moment a task starts. The sandbox lane below it is segmented, built when the task starts, released while the thread goes quiet, and rebuilt fresh when someone replies." width="1000" height="270" data-path="images/claude-tag/diagrams/session-lifecycle.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-lifecycle-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=0693a90b98baa729dcacfd35261f6494" alt="Timeline with two lanes. The Slack thread lane is one continuous bar that persists from the moment a task starts. The sandbox lane below it is segmented, built when the task starts, released while the thread goes quiet, and rebuilt fresh when someone replies." width="1000" height="270" data-path="images/claude-tag/diagrams/session-lifecycle-dark.svg" />

|                                        | Survives idle periods               |
| :------------------------------------- | :---------------------------------- |
| The conversation and its context       | Yes                                 |
| Channel memory                         | Yes                                 |
| Work pushed, posted, or opened as a PR | Yes, in the external system         |
| Files that exist only in the sandbox   | No. Claude recreates them if asked. |

For long tasks, ask it to push branches and post drafts as it goes, so deliverables are saved somewhere durable while the work is still running. See [Good habits](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done).

A running thread isn't told about configuration changes an admin makes after it started, such as a new connection, plugin, skill, repository grant, or custom instruction. A new thread starts from the scope's current configuration, so after changing a scope, start a fresh thread to see the change.

The channel's own session, the one that handles top-level messages outside any thread, lives longer than a thread's. Claude replaces it with a fresh one when a top-level message arrives after about an hour with no top-level activity, when the session is about a day old, or when the channel's configuration has changed since the session started. Channel memory and the channel's history are unaffected, so the only visible effect is that Claude no longer carries what the previous session had been working on.

Claude also stops reading a channel's top-level messages once about 100 of them have arrived since it last posted or replied there. An `@Claude` mention in the channel starts it reading again; see [When Claude stops reading a channel](/docs/claude-tag/users/when-claude-responds#when-claude-stops-reading-a-channel). These thresholds are defaults and can change, so treat the numbers as approximate.

### Channel and workspace memory

Memory follows places the same way access does, and it accumulates for the team rather than for any individual.

Memory from public channels is shared across the workspace, so a decision recorded while working in #launch-week is available when someone asks in #gtm-west. When Claude cites something from a channel you have never used it in, it is reading workspace memory shared from that channel, not a profile of you.

Private channels read workspace memory while working, and what they save is written to that channel's own store rather than the workspace store.

To see what it holds, ask `@Claude what do you remember about this channel?`. Anyone in the channel can correct or remove entries. [What Claude Tag remembers](/docs/claude-tag/users/memory) covers reading, correcting, and adding to memory.

The whole model so far fits in one picture, with access set at the scope, memory shared from public channels, work in progress per thread, and DMs outside all of it.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/three-levels.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=511231c5561da4ade26f91cd395488fa" alt="Diagram showing three nested levels. A scope container holds two channels, #platform-eng and #gtm-west, and each channel holds its own threads, like 'fix checkout latency' or 'pull deal state'. The private channel is marked with a lock. Callouts mark what lives at each level (identity and access at the scope; memory, shared from public channels across the workspace while private channels keep their own; and work in progress at the thread). A DM with Claude sits below, outside every scope, and runs on your own account." width="1000" height="648" data-path="images/claude-tag/diagrams/three-levels.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/three-levels-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=e593920bd85a97c285a56f7b9d3e5019" alt="Diagram showing three nested levels. A scope container holds two channels, #platform-eng and #gtm-west, and each channel holds its own threads, like 'fix checkout latency' or 'pull deal state'. The private channel is marked with a lock. Callouts mark what lives at each level (identity and access at the scope; memory, shared from public channels across the workspace while private channels keep their own; and work in progress at the thread). A DM with Claude sits below, outside every scope, and runs on your own account." width="1000" height="648" data-path="images/claude-tag/diagrams/three-levels-dark.svg" />

DMs are outside this picture; they run on your own account, as covered in [Team channels and personal DMs](#team-channels-and-personal-dms) above. Owners can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

## Related resources

* [Getting started](/docs/claude-tag/users/getting-started): hand Claude your first task
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why an admin sets access per channel, and how credentials stay out of the sandbox
* [Good habits](/docs/claude-tag/users/good-habits): write tasks that survive the sandbox lifecycle
