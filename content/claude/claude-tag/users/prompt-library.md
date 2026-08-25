> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt library

> Copy-paste prompts for Claude Tag in Slack, each with why it works. See first messages, forwarded-message handoffs, channel rules, memory checks, routines, and mid-thread steering.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

These prompts are ready to copy, paste, and adapt: swap in your own channel names, services, and repositories. Each comes with the reason it works, so you can keep the mechanism when you change the words.

## First messages in a new channel

Ask what Claude can access from this channel:

```text wrap theme={null}
@Claude what can you access from this channel?
```

**Why it works**: what Claude can do differs per channel, and without this grounding Claude may suggest tasks it can't do here.

Get a personalized starting point:

```text wrap theme={null}
@Claude learn what you can about my role from this workspace, then tell me three tasks you could take off my plate this week.
```

**Why it works**: it's a discovery task with a bounded output. By asking for three tasks, you get a list you can judge in ten seconds and reuse as a menu of next tasks.

Start with a low-stakes task:

```text wrap theme={null}
@Claude catch me up on this channel since Monday.
```

**Why it works**: you bound the task with "since Monday", and you can grade the result yourself because you were there.

## Forward a message as a task

To turn an existing Slack message into a task, for example a bug report or a request someone posted, forward it to a channel Claude is in. In the message you attach when forwarding, name the deliverable and say what Claude should do if it isn't possible. Claude reads the forwarded message, so you don't need to retype its contents.

```text wrap theme={null}
@Claude investigate this. If it's something we can fix, open a draft PR; if not, post who owns it and why it's theirs.
```

**Why it works**: by giving Claude both branches, you get a useful result whether or not a fix is possible.

To hand over a discussion too long to forward, paste the thread's link instead:

```text wrap theme={null}
@Claude read the thread linked below and take over the fix it describes. Post your plan here before changing anything.
```

**Why it works**: Claude works in the thread where you pasted the link, not in the thread you linked, so it uses this channel's connections and this channel can see the result. By asking Claude to post its plan first, you can redirect it before it starts. To read a linked thread in a public channel, Claude must be a member of that channel, and it can read a private channel's threads [only from inside that channel](/docs/claude-tag/users/good-habits#pick-the-right-surface). If Claude says it can't read the link, `/invite @Claude` in the linked public channel, or forward the messages instead.

## Shape how the channel works

Use the prompts below to set channel-wide behavior that applies to every thread, not just yours.

```text wrap theme={null}
@Claude remember for this channel: keep replies short, and always include a link to the source.
```

**Why it works**: you're explicitly telling Claude to save the rule. Claude usually doesn't keep preferences you mention in passing.

```text wrap theme={null}
@Claude stay quiet in this channel unless tagged.
```

**Why it works**: you're stating standing channel behavior, so Claude applies it beyond the current conversation.

```text wrap theme={null}
@Claude remember for this channel: treat every top-level post as a task and pick it up without waiting for a mention.
```

**Why it works**: Claude already [picks up untagged posts when it judges a reply is warranted](/docs/claude-tag/users/when-claude-responds), and it weighs this channel-memory rule in that judgment, so teammates don't have to remember to tag Claude on posts with a concrete ask. If you don't specify a need, or if a teammate has already claimed the task, Claude may not respond to the message. In [a channel Claude has stopped reading](/docs/claude-tag/users/when-claude-responds#when-claude-stops-reading-a-channel), mention `@Claude` so that it replies and starts reading the channel again.

## Check and correct memory

```text wrap theme={null}
@Claude what do you remember about this channel?
```

**Why it works**: memory is a curated note and Claude decides what's worth keeping, so you have to ask to know what stuck.

```text wrap theme={null}
@Claude that's outdated — forget the entry about the old project name.
```

**Why it works**: you name the specific entry, so Claude doesn't have to guess what's stale the way it does with "clean up your memory".

```text wrap theme={null}
@Claude update your memory for this channel so this doesn't happen again.
```

**Why it works**: when you correct Claude in a thread, you fix that thread only. With this message, Claude saves the correction and applies it in everyone's future threads.

## Manage routines

Create, audit, and stop the scheduled jobs Claude runs in this channel. For paste-ready schedules by scenario, like a daily standup summary or a weekly digest, see [Routine recipes](/docs/claude-tag/users/proactivity#routine-recipes).

```text wrap theme={null}
@Claude every Friday at 3pm, post a summary of this week's requests: how many, top themes, and anything still unrouted.
```

**Why it works**: you name the schedule and the post's contents, so every week Claude posts the same shape and you can compare to last week. By asking for anything still unrouted, you get a sweep for dropped requests, not just a recap.

```text wrap theme={null}
@Claude what routines do you have set up in this channel?
```

**Why it works**: schedules are channel state, and someone else may have set them up. Check what exists before you create a duplicate digest.

```text wrap theme={null}
@Claude disable the daily digest job.
```

**Why it works**: you name which job. Any channel member can disable a scheduled job; you don't need to find an admin to stop a noisy routine.

## Steer work mid-thread

Reply in the same thread; once Claude is working there, you don't need to @-mention it again.

```text wrap theme={null}
Status check — what's done and what's left?
```

**Why it works**: you're replying into the session that's running the task, with full context. If you ask in a new thread instead, Claude starts a second session that knows nothing about the first.

```text wrap theme={null}
Change of plan: target the staging config instead, and post the diff here before applying anything.
```

**Why it works**: when you redirect in the thread, Claude keeps everything the session has already learned. By asking for the diff first, you and the channel can review the change before Claude applies it.

```text wrap theme={null}
Post the draft to the thread, or commit and push what you have, then keep going.
```

**Why it works**: the thread is durable but [the isolated workspace behind it isn't](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies). Anything Claude posts to the thread or pushes to a branch survives idle recycling; files that exist only in that workspace don't.

## Task starters, by shape

Each entry in the use case library gets one starter here; the linked page has the full setup and the reasoning behind its prompts.

| To do this                                                                  | Paste this                                                                                                                                                                                                                                                   |
| :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Triage requests](/docs/claude-tag/users/use-cases/triage-requests)              | "remember for this channel: when someone tags you on a request, check whether it duplicates something already reported, answer it directly if the answer exists, and otherwise route it to the right owner with a one-line summary. Track recurring themes." |
| [Catch up](/docs/claude-tag/users/use-cases/catch-up)                            | "what got decided in this thread, and what's still open?"                                                                                                                                                                                                    |
| [Create an artifact](/docs/claude-tag/users/use-cases/create-artifacts)          | "turn this thread into a one-page decision doc"                                                                                                                                                                                                              |
| [Track a project](/docs/claude-tag/users/use-cases/track-projects)               | "where are we on the migration? What's blocked and on whom?"                                                                                                                                                                                                 |
| [Answer a data question](/docs/claude-tag/users/use-cases/answer-data-questions) | "show signup growth by week, and explain the dips discussed above"                                                                                                                                                                                           |
| [Find an answer in the docs](/docs/claude-tag/users/use-cases/find-answers)      | "what's our policy on data retention, and which doc says so?"                                                                                                                                                                                                |
| [Pull deal state](/docs/claude-tag/users/use-cases/pull-deal-state)              | "what's the state of the Acme renewal?"                                                                                                                                                                                                                      |
| [Watch monitors](/docs/claude-tag/users/use-cases/watch-monitors)                | "every morning at 7, check the dashboards and post one line per service"                                                                                                                                                                                     |
| [Fix a bug](/docs/claude-tag/users/use-cases/fix-bugs)                           | "in acme/data-pipeline, reproduce the bug in this thread, fix it, and open a draft PR"                                                                                                                                                                       |

## Related resources

* [Use case library](/docs/claude-tag/users/use-cases): the full setup behind each starter
* [Good habits](/docs/claude-tag/users/good-habits): the habits these prompts are built from
* [Getting started](/docs/claude-tag/users/getting-started): the basics, if you haven't sent a first message yet
