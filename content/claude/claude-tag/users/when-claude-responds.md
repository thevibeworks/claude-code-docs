> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Control when Claude Tag responds

> What Claude Tag does with a channel message nobody tagged it in, and how to turn unprompted replies off for a thread or a channel. Read this if Claude is replying too much, or went quiet.

> [!NOTE]
>
> Claude Tag is in public beta. Features and behavior described here may change before general availability.

Claude replies without an @-mention in one-to-one DMs, in any thread it's already part of, and to channel and group DM messages it judges warrant a reply. In a channel, Claude reads the messages and replies to some of them on its own, so an @-mention is how you guarantee a reply, not a requirement for one. This page covers how Claude decides whether to reply to a message nobody tagged it in, how to turn those replies off for a thread or a whole channel, and which messages never get a reply. Work Claude does on a schedule rather than in reply to a message is a [routine](https://claude.com/docs/claude-tag/users/proactivity.md), which has its own controls.

## What triggers a response

Whether Claude replies to a message without an @-mention depends on where you send it.

| Where you write | Replies without an @-mention? |
| :- | :- |
| A one-to-one DM with Claude | Always. Every message is addressed to Claude already |
| A thread Claude is already in | Yes, unless you've [quieted the thread](#quiet-one-conversation). Once Claude has joined, every reply there reaches it without another mention |
| A channel, top-level | Sometimes, under the default [**How Claude participates**](#turn-automatic-replies-on-or-off) setting. [What Claude does with a channel message](#what-claude-does-with-a-channel-message) describes how it decides. Include `@Claude` to guarantee a reply, or [turn unprompted replies off](#quiet-the-whole-channel) |
| A group DM that includes Claude, top-level | Sometimes. See [When Claude replies in a group DM](https://claude.com/docs/claude-tag/users/group-dms.md#when-claude-replies-in-a-group-dm) |
| A message another app or bot posted | No. Claude reads it as context. To get a reply, have the app include `@Claude` in its message. [Messages from other apps and bots](#messages-from-other-apps-and-bots) covers when that mention goes unanswered |

When you @-mention Claude in a channel, it reacts to your message with an emoji within a few seconds to show that it picked the message up. The message goes to the channel's own [session](https://claude.com/docs/claude-tag/concepts/glossary.md#session), the session Claude works from at the channel's top level. It then answers in a thread under your message, or starts a [working session](https://claude.com/docs/claude-tag/concepts/how-it-works.md) in that thread when the request needs investigation, tools, or a longer exchange.

Once a working session starts, a working indicator with a **Stop** button appears at the bottom of the thread. A reaction with no indicator means Claude picked your message up and is either still deciding or answering directly in the thread, not that it missed you.

You can change how much Claude replies on its own. You can [quiet a single thread](#quiet-one-conversation), [turn unprompted replies off for a whole channel](#turn-automatic-replies-on-or-off), or [tell Claude which kinds of untagged messages to answer](#what-claude-does-with-a-channel-message).

## What Claude does with a channel message

Under the default [**Respond automatically**](#turn-automatic-replies-on-or-off) option, Claude reads top-level messages and thread replies in a channel it belongs to, whether anyone tagged it or not, and it can [stop reading the channel](#when-claude-stops-reading-a-channel). For each message, it decides what to do from the channel's recent messages, the channel's [memory](https://claude.com/docs/claude-tag/users/memory.md), and any instructions your admin has set or a channel member has asked it to remember, and does one of these things.

* **Nothing.** This is the usual outcome, especially in a channel where nobody has told Claude which kinds of messages to answer.
* **An offer to help.** When a thread leaves a concrete next step Claude could take for someone, Claude may offer in that thread to take it. The offer is either a one-line reply everyone can see or a [private suggestion](#private-suggestions-from-claude) only that person can see.
* **A short reply in a thread under the message.** Claude may reply on its own when it already has the answer, from the channel's history or its memory, and the answer fits in one message. Replies of this kind carry the plain name **Claude**; see [The name on a reply](#the-name-on-a-reply).
* **A working session in the message's thread.** When a message needs investigation, tools, or a longer exchange, Claude starts a working session there and posts the work in that thread. For an untagged message, Claude does this only when someone in the channel has told it to pick up that kind of work, as described below the list.
* **A hand-off to work already in progress.** When a message adds to something Claude is already working on in another thread, for example a new detail about a bug it's investigating, Claude passes the message to that working session instead of replying. Claude posts nothing in the channel when it does this; anything the new information changes, it reports in the thread where the work is happening.

To have Claude answer more kinds of untagged messages in a channel, tell it which kinds, in the channel, and ask it to remember. For example, `@Claude remember for this channel: answer questions about the deploy process without waiting to be tagged` saves the instruction to channel memory, and Claude applies it to everyone's messages there. Claude also records in channel memory whether people in the channel act on its unprompted replies or ignore them, and replies less in a channel that ignores them. [What Claude Tag remembers](https://claude.com/docs/claude-tag/users/memory.md) covers how to see and change what it saved.

### Private suggestions from Claude

A private suggestion is a card Claude posts in a thread that only one person in the channel can see. It's labeled "From Claude, only you can see this" and states what Claude offers to do for you, with two buttons.

* **Yes, do it**: Claude takes the suggestion as your request and starts on it in the thread. The card disappears, and a message everyone in the thread can see says you accepted the suggestion and quotes it.
* **No thanks**: the card disappears, and Claude posts nothing.

A suggestion expires after a day. To have Claude do the work after that, @-mention Claude in the thread. To stop suggestions for yourself or for a whole channel, see [Stop private suggestions](#stop-private-suggestions).

## Turn automatic replies on or off

Each channel's **How Claude participates** setting controls when Claude replies to the channel's messages.

| Option | What Claude does |
| :- | :- |
| **Only when @-mentioned** | Waits for a person to @-mention it. In a thread it's already part of, it can also reply without a mention |
| **Respond automatically** (the default) | May reply to a message it judges warrants one, as [What Claude does with a channel message](#what-claude-does-with-a-channel-message) describes |
| **Always awake** | Replies as it does under **Respond automatically**, and [keeps reading the channel](#when-claude-stops-reading-a-channel) however quiet or busy the channel gets |
| **Start a thread session for every top-level message** | Starts a [working session](https://claude.com/docs/claude-tag/concepts/how-it-works.md) in a thread under a workspace member's new top-level message, whether the message tags Claude or not. Some messages don't start one |

Each channel has its own copy of the setting, and there is no workspace- or organization-wide version. To make Claude mention-only across many channels, select **Only when @-mentioned** in each one.

All three places below change the same setting, so a change you make in one appears in the others.

| Where | How |
| :- | :- |
| In Slack | Ask Claude in the channel, for example "@Claude only respond in this channel when someone @-mentions you" or "@Claude respond to messages here even when nobody mentions you." Claude confirms the change. |
| The channel's Configure page | Open the **Configure** link in the footer of any Claude reply in the channel, switch the **Respond automatically** toggle, and click **Save**. See [Configure Claude for a channel](https://claude.com/docs/claude-tag/users/good-habits.md#configure-claude-for-a-channel). |
| Claude Tag admin settings (Owners and Claude Tag admins) | Go to [**Organization settings > Claude Tag**](https://claude.ai/admin-settings/claude-tag?access=channels), select the channel on the **Channels** tab, and switch **Respond automatically** on the channel's **General** tab. |

An Owner or a [Claude Tag admin](https://claude.com/docs/claude-tag/admins/restrict-access.md#delegate-claude-tag-administration) can set [**Channel member edits**](https://claude.com/docs/claude-tag/admins/attach-to-scope.md#restrict-who-can-set-channel-instructions) to **Block** for a channel, a workspace, or all of Slack. When the setting is **Block**, Claude declines to change **How Claude participates** when anyone asks in Slack, and channel members can't change **How Claude participates** on the channel's Configure page. An Owner or a Claude Tag admin can still change the setting in Claude Tag admin settings, and a [channel manager](https://claude.com/docs/claude-tag/admins/restrict-access.md#delegate-channel-setup-to-channel-managers) can still change it on the Configure page of a channel assigned to them.

The setting covers the channel's messages, not DMs. To quiet a single thread instead of the whole channel, [ask Claude in that thread](#quiet-one-conversation).

Until Claude has joined a channel, you see "@-mention Claude in this channel to activate" in place of the options under **How Claude participates**, both on the Configure page and on the channel's page in Claude Tag admin settings. You see the same line in a channel shared across workspaces that all belong to your Claude organization, because Claude runs there with your organization's default settings only. [Messages that never get a reply](#messages-that-never-get-a-reply) covers shared channels in more detail.

> [!NOTE]
>
> Separately from **How Claude participates**, an Owner or a Claude Tag admin can [turn Claude off in channels](https://claude.com/docs/claude-tag/admins/workspaces.md#turn-claude-tag-on-or-off-and-set-the-version-for-a-scope).

## Messages from other apps and bots

Claude reads a message that another Slack app or bot posts as channel context, and replies to it only when the message includes `@Claude`. Claude treats alerts an integration posts, messages a Slack workflow posts, and messages from any other bot the same way.

A bot's `@Claude` at the channel's top level gets a reply in a thread under that message, unless any of these is true:

* The channel's [**Respond automatically**](#turn-automatic-replies-on-or-off) setting is off.
* The channel is a [Slack Connect channel](https://claude.com/docs/claude-tag/admins/restrict-access.md#when-claude-does-not-answer-in-a-slack-connect-channel), shared with another company. Claude reads what apps, bots, and workflows post there as context but doesn't reply to them.

A person's mention reaches Claude in each of these cases.

Because Claude reads those messages, when a person asks about an alert a bot posted, Claude can answer from it. To have Claude act on what an integration posts, mention it in the channel or in the message's thread. For example, reply to a bot-posted alert with `@Claude triage this`. To have Claude check the channel on a schedule and post what needs attention, set up a [routine](https://claude.com/docs/claude-tag/users/proactivity.md).

## The name on a reply

Claude doesn't post every reply under the same display name. The name shows which kind of work produced the reply, in two forms:

* **Claude**, the name alone: the reply comes from Claude's ambient presence in the channel, including unprompted replies
* **Claude** followed by a short description of the task in square brackets: the reply comes from a [working session](https://claude.com/docs/claude-tag/concepts/how-it-works.md) handling that task in its thread. The description changes with every task, so a channel might show something like `Claude [reviewing the launch checklist]`, `Claude [debugging a failing deploy]`, or `Claude [summarizing customer feedback]`.

## Make a channel quieter

If Claude is replying to messages that weren't meant for it, turn that down from inside the channel.

### Quiet one conversation

Tell Claude in the thread to respond only when mentioned.

```text wrap theme={null}
@Claude only respond when I @-mention you
```

Claude stops following that thread, and the rest of the channel is unaffected. This is the fix when one busy thread is the noise. The [`!mute` command](https://claude.com/docs/claude-tag/users/commands#mute-or-unmute-a-thread) goes further and silences the thread entirely; `@Claude !unmute`, or an @-mention that carries a request, turns it back on. Selecting the thumbs-down button under one of Claude's replies also mutes the thread, as [Thumbs-down button and muting](https://claude.com/docs/claude-tag/users/commands.md#thumbs-down-button-and-muting) describes.

### Quiet the whole channel

Set the channel's [**How Claude participates**](#turn-automatic-replies-on-or-off) setting to **Only when @-mentioned**. From Slack, ask Claude directly.

```text wrap theme={null}
@Claude only respond in this channel when someone @-mentions you directly.
```

Claude confirms the change, which is channel-wide, not just for you. You can make the same change under **How Claude participates** on the channel's Configure page, and an Owner or a [Claude Tag admin](https://claude.com/docs/claude-tag/admins/restrict-access.md#delegate-claude-tag-administration) can change it in [Claude Tag admin settings](https://claude.ai/admin-settings/claude-tag). If Claude declines because an Owner or a Claude Tag admin has locked the channel's settings, ask one of them to make the change in Claude Tag admin settings, as [Turn automatic replies on or off](#turn-automatic-replies-on-or-off) describes.

Threads Claude already joined keep forwarding replies, so quiet those individually with the in-thread line above. The [`!mute` command](https://claude.com/docs/claude-tag/users/commands#mute-or-unmute-a-thread) quiets one thread at a time and does nothing at a channel's top level.

### Stop private suggestions

You can stop [private suggestions](#private-suggestions-from-claude) for yourself or for everyone in a channel.

* **For yourself**: open the **⋯** menu on a suggestion and select **Mute for a week**. The channel's [Configure page](https://claude.com/docs/claude-tag/users/good-habits.md#configure-claude-for-a-channel) opens and mutes suggestions for you for 7 days, in every channel of your organization. Other people still get theirs. To end the mute early, select **Unmute** in the "Suggestions muted for you" bar on any channel's Configure page. A suggestion in a channel without a Configure page has no **⋯** menu, but a mute you set from another channel's suggestion covers it.
* **For the whole channel**: select **Only when @-mentioned** under **How Claude participates**, as [Turn automatic replies on or off](#turn-automatic-replies-on-or-off) describes. Claude then sends no suggestions in that channel.

### Remove Claude Tag from the channel

When quieting isn't enough, end Claude's presence in the channel.

```text wrap theme={null}
/remove @Claude
```

Claude can no longer read or post in that channel. Any member can run this unless your Slack admin restricts the command. Admins have further options, through full removal from the workspace, on [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access.md).

## When Claude stops reading a channel

Under the default [**Respond automatically**](#turn-automatic-replies-on-or-off) option, unless the channel is [attached to on-call](https://claude.com/docs/claude-tag/admins/setup-oncall.md), Claude stops reading the channel's top-level messages and messages in threads it isn't part of when either of these happens:

* **Message volume.** Claude counts the messages posted in the channel since it last posted there itself, and stops reading when the count gets high enough.
* **Inactivity.** When more than 10 days pass without anyone @-mentioning Claude in the channel and without Claude posting there, Claude stops reading.

Claude posts no notice when it stops.

To start Claude reading again, mention `@Claude` in the channel. A mention from a person reaches Claude in both situations, and once Claude posts its reply, it reads the channel's messages again. A mention inside another app's or bot's message works the same way, except in the [cases that block a bot's reply](#messages-from-other-apps-and-bots).

If unprompted replies don't come back after Claude answers a mention, check **How Claude participates** on the channel's [Configure page](https://claude.com/docs/claude-tag/users/good-habits.md#configure-claude-for-a-channel). Answering a mention doesn't change the setting, so if the page shows **Only when @-mentioned**, change it to **Respond automatically** in one of the three places listed in [Turn automatic replies on or off](#turn-automatic-replies-on-or-off).

## Messages that never get a reply

A few cases produce silence even when the message includes a mention:

* **Editing a message to add the mention.** An edit doesn't trigger a response. Delete the message and send a new one with `@Claude` included.
* **Channels with guest accounts.** By default, Claude is off in channels that include guests; an Owner or a Claude Tag admin can turn it on for a channel, a workspace, or all of Slack. Ask whoever runs your Claude plan, or send them [the guest access setting](https://claude.com/docs/claude-tag/admins/restrict-access.md#restrict-guest-channels).
* **Channels shared across workspaces connected to different Claude organizations.** Every workspace where Claude runs is connected to a Claude organization, the account a company sets up for Claude. When a channel is shared across workspaces connected to different Claude organizations, Claude won't reply there and posts a refusal message instead. You can't tell from Slack how a workspace is connected; the refusal message itself is the signal. Use a channel that belongs to one workspace, or send Claude a DM.
* **Slack Connect channels.** By default, Claude is off in [channels shared with another company](https://claude.com/docs/claude-tag/admins/restrict-access.md#slack-connect-channels), and a mention there gets no reply and no notice. An Owner or a Claude Tag admin can turn it on for a channel, a workspace, or all of Slack. Ask whoever runs your Claude plan to change [**How should Claude work in channels with guests**](https://claude.com/docs/claude-tag/admins/restrict-access.md#slack-connect-channels).

When the workspaces sharing a channel all belong to one Claude organization and an admin hasn't turned Claude off for these channels, Claude replies there, but with only your organization's default access and settings. The repositories, instructions, and memory set up for that channel or its workspaces don't apply, and Claude posts a notice in the thread explaining this from time to time. The guest check above still applies first where guest access is restricted.

To confirm a channel's setting, check **How Claude participates** on its [Configure page](https://claude.com/docs/claude-tag/users/good-habits.md#configure-claude-for-a-channel). To confirm an instruction Claude saved, ask `@Claude what do you remember about responding in this channel?`, and see [What Claude Tag remembers](https://claude.com/docs/claude-tag/users/memory.md) for where instructions are stored and how to change them.

## Related resources

* [Customize Claude Tag](https://claude.com/docs/claude-tag/admins/customize.md): the settings only an admin can change, if channel memory isn't enough
* [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access.md): the admin-side controls, from guest channels to full removal
