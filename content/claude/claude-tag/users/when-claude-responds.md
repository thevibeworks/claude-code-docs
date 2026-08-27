> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Control when Claude Tag responds

> What Claude Tag does with a channel message nobody tagged it in, and how to turn unprompted replies off for a thread or a channel. Read this if Claude is replying too much, or went quiet.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Claude replies without an @-mention in DMs, in any thread it's already part of, and to channel messages it judges warrant a reply. In a channel, Claude reads the messages and replies to some of them on its own, so an @-mention is how you guarantee a reply, not a requirement for one. This page covers how Claude decides whether to reply to a message nobody tagged it in, how to turn those replies off for a thread or a whole channel, and which messages never get a reply. Work Claude does on a schedule rather than in reply to a message is a [routine](/docs/claude-tag/users/proactivity), which has its own controls.

## What triggers a response

Whether Claude replies to a message without an @-mention depends on where you send it.

| Where you write                     | Replies without an @-mention?                                                                                                                                                                                                       |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A DM with Claude                    | Always. Every message is addressed to Claude already                                                                                                                                                                                |
| A thread Claude is already in       | Yes, unless you've [quieted the thread](#quiet-one-conversation). Once Claude has joined, every reply there reaches it without another mention                                                                                      |
| A channel, top-level                | Sometimes. [What Claude does with a channel message](#what-claude-does-with-a-channel-message) describes how it decides. Include `@Claude` to guarantee a reply, or [turn unprompted replies off](#quiet-the-whole-channel)         |
| A message another app or bot posted | No guaranteed reply. Claude reads it as context. `@Claude` in a bot's message doesn't wake a quiet channel; in an active channel Claude may pick it up. See [Messages from other apps and bots](#messages-from-other-apps-and-bots) |

When you @-mention Claude in a channel, it reacts to your message with an emoji within a few seconds to show that it picked the message up. The message goes to the channel's own [session](/docs/claude-tag/concepts/glossary#session), the session Claude works from at the channel's top level. It then answers in a thread under your message, or starts a [working session](/docs/claude-tag/concepts/how-it-works) in that thread when the request needs investigation, tools, or a longer exchange. Once a working session starts, Claude shows an "is thinking…" line under your message. A reaction with no line under it means Claude picked your message up and is either still deciding or answering directly in the thread, not that it missed you.

You can change how much Claude replies on its own. You can [quiet a single thread](#quiet-one-conversation), [turn unprompted replies off for a whole channel](#turn-automatic-replies-on-or-off), or [tell Claude which kinds of untagged messages to answer](#what-claude-does-with-a-channel-message).

## What Claude does with a channel message

Claude reads every top-level message in a channel it belongs to, and the replies in the channel's threads, whether or not anyone tagged it. For each message, it decides what to do from the channel's recent messages, the channel's [memory](/docs/claude-tag/users/memory), and any instructions your admin has set or a channel member has asked it to remember, and does one of four things.

* **Nothing.** This is the usual outcome. In a channel where nobody has told Claude which kinds of messages to answer, Claude leaves untagged messages alone. The one exception is a message in which someone states a concrete need Claude can meet; Claude may then reply once, in a thread, offering to do it.
* **A short reply in a thread under the message.** Claude replies on its own only when it already has the answer, from the channel's history or its memory, and the answer fits in one message. Replies of this kind carry the plain name **Claude**; see [The name on a reply](#the-name-on-a-reply).
* **A working session in the message's thread.** When a message needs investigation, tools, or a longer exchange, Claude starts a working session there and posts the work in that thread. For an untagged message, Claude does this only when someone in the channel has told it to pick up that kind of work, as described below the list.
* **A hand-off to work already in progress.** When a message adds to something Claude is already working on in another thread, for example a new detail about a bug it's investigating, Claude passes the message to that working session instead of replying. Claude posts nothing in the channel when it does this; anything the new information changes, it reports in the thread where the work is happening.

To have Claude answer more kinds of untagged messages in a channel, tell it which kinds, in the channel, and ask it to remember. For example, `@Claude remember for this channel: answer questions about the deploy process without waiting to be tagged` saves the instruction to channel memory, and Claude applies it to everyone's messages there. Claude also records in channel memory whether people in the channel act on its unprompted replies or ignore them, and replies less in a channel that ignores them. [What Claude Tag remembers](/docs/claude-tag/users/memory) covers how to see and change what it saved.

## Turn automatic replies on or off

The **Respond automatically** setting controls whether Claude replies to a channel's messages without an @-mention. When it's on, Claude may reply to a message it judges warrants one, as [What Claude does with a channel message](#what-claude-does-with-a-channel-message) describes. When it's off, Claude replies in that channel only when someone @-mentions it.

The setting is on by default, so a channel Claude was just added to replies without @-mentions from the start.

Each channel has its own copy of the setting, and there is no workspace- or organization-wide version. To make Claude mention-only across many channels, turn it off in each one.

All three places below change the same setting, so a change you make in one appears in the others.

| Where                                   | How                                                                                                                                                                                                                                      |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In Slack                                | Ask Claude in the channel, for example "@Claude only respond in this channel when someone @-mentions you" or "@Claude respond to messages here even when nobody mentions you." Claude confirms the change.                               |
| The channel's Configure page            | Open the **Configure** link in the footer of any Claude reply in the channel and switch the **Respond automatically** toggle. See [Configure Claude for a channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).        |
| The Claude Tag admin page (admins only) | At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), on the **Slack** tab under **Claude Tag's access**, open the channel's scope and switch **Respond automatically** in its **Advanced** settings. |

The setting covers the channel's messages, not DMs. To quiet a single thread instead of the whole channel, [ask Claude in that thread](#quiet-one-conversation).

Until Claude has joined a channel, you see "@-mention Claude in this channel to activate" in place of the toggle on the Configure page and the admin page. You see the same line in a channel shared across workspaces that all belong to your Claude organization, because Claude runs there with your organization's default settings only. [Messages that never get a reply](#messages-that-never-get-a-reply) covers shared channels in more detail.

## Messages from other apps and bots

Claude reads a message that another Slack app or bot posted as channel context, but a bot's message never gets the guaranteed reply that a person's @-mention gets. If the channel's [Respond automatically](#turn-automatic-replies-on-or-off) setting is off, or Claude has [stopped reading the channel](#when-claude-stops-reading-a-channel), a bot's `@Claude` doesn't wake it. In a channel where Claude is active, a bot's `@Claude` reaches Claude as a hand-off it may pick up or leave, and it may answer in a thread. Claude treats alerts an integration posts, messages a Slack workflow posts, and messages from any other bot the same way.

Because Claude reads those messages, when a person asks about an alert a bot posted, Claude can answer from it. To have Claude act on what an integration posts, mention it in the channel or in the message's thread. For example, reply to a bot-posted alert with `@Claude triage this`. To have Claude check the channel on a schedule and post what needs attention, set up a [routine](/docs/claude-tag/users/proactivity).

## The name on a reply

Claude doesn't post every reply under the same display name. The name shows which kind of work produced the reply, in two forms:

* **Claude**, the name alone: the reply comes from Claude's ambient presence in the channel, including unprompted replies
* **Claude** followed by a short description of the task in square brackets: the reply comes from a [working session](/docs/claude-tag/concepts/how-it-works) handling that task in its thread. The description changes with every task, so a channel might show something like `Claude [reviewing the launch checklist]`, `Claude [debugging a failing deploy]`, or `Claude [summarizing customer feedback]`.

## Make a channel quieter

If Claude is replying to messages that weren't meant for it, turn that down from inside the channel.

### Quiet one conversation

Tell Claude in the thread to respond only when mentioned.

```text wrap theme={null}
@Claude only respond when I @-mention you
```

Claude stops following that thread, and the rest of the channel is unaffected. This is the fix when one busy thread is the noise. The [`!mute` command](/docs/claude-tag/users/commands#mute-or-unmute-a-thread) goes further and silences the thread entirely; any direct `@Claude` mention turns it back on.

### Quiet the whole channel

Turn the channel's [**Respond automatically**](#turn-automatic-replies-on-or-off) setting off, so Claude replies there only when @-mentioned. From Slack, ask Claude directly.

```text wrap theme={null}
@Claude only respond in this channel when someone @-mentions you directly.
```

Claude confirms the change, which is channel-wide, not just for you. You can make the same change with the toggle on the channel's Configure page, and an admin can make it from the Claude Tag admin page.

Threads Claude already joined keep forwarding replies, so quiet those individually with the in-thread line above. The [`!mute` command](/docs/claude-tag/users/commands#mute-or-unmute-a-thread) quiets one thread at a time and does nothing at a channel's top level.

### Remove Claude Tag from the channel

When quieting isn't enough, end Claude's presence in the channel.

```text wrap theme={null}
/remove @Claude
```

Claude can no longer read or post in that channel. Any member can run this unless your Slack admin restricts the command. Admins have further options, through full removal from the workspace, on [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access).

## When Claude stops reading a channel

Claude counts the messages posted in a channel since it last posted there itself. When the count gets high enough, Claude stops reading that channel's messages, and unprompted replies stop with it. Claude doesn't announce this. To start it reading again, mention `@Claude` in the channel; the mention reaches it regardless, and once Claude posts its reply, it reads the channel's messages again.

If unprompted replies don't come back after Claude answers a mention, the channel's [**Respond automatically**](#turn-automatic-replies-on-or-off) setting is off. Answering a mention doesn't turn the setting on, and Claude changes the setting only when a channel member asks it to, so turn it back on in any of the three places listed in that section.

## Messages that never get a reply

A few cases produce silence even when the message includes a mention:

* **Editing a message to add the mention.** An edit doesn't trigger a response. Delete the message and send a new one with `@Claude` included.
* **Channels with guest accounts.** By default, Claude is off in channels that include guests; your admin can turn it on per scope. Ask whoever runs your Claude plan, or send them [the guest access setting](/docs/claude-tag/admins/restrict-access#restrict-guest-channels).
* **Channels shared across workspaces connected to different Claude organizations.** Every workspace where Claude runs is connected to a Claude organization, the account a company sets up for Claude. When a channel is shared across workspaces connected to different Claude organizations, Claude won't reply there and posts a refusal message instead. You can't tell from Slack how a workspace is connected; the refusal message itself is the signal. Use a channel that belongs to one workspace, or send Claude a DM.
* **Slack Connect channels.** Channels shared with another company are always off.

When the workspaces sharing a channel all belong to one Claude organization, Claude replies there, but with only your organization's default access and settings. The repositories, instructions, and memory set up for that channel or its workspaces don't apply, and Claude posts a notice in the thread explaining this from time to time. The guest check above still applies first where guest access is restricted.

To confirm a channel's setting, check the **Respond automatically** toggle on its [Configure page](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel). To confirm an instruction Claude saved, ask `@Claude what do you remember about responding in this channel?`, and see [What Claude Tag remembers](/docs/claude-tag/users/memory) for where instructions are stored and how to change them.

## Related resources

* [Customize Claude Tag](/docs/claude-tag/admins/customize): the settings only an admin can change, if channel memory isn't enough
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the admin-side controls, from guest channels to full removal
