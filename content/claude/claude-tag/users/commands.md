> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Commands Claude Tag understands

> A few exact, bang-prefixed words after an @-mention run a fixed action instead of starting a normal turn: see the command list, get the link to a channel's settings page, restart a stuck or wrong-context session, mute or unmute a thread, send feedback, list a channel's routines, and fork a thread's conversation into a new thread, here or in another channel.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

A command is `@Claude` followed immediately by one of a few exact words starting with `!`. Claude matches the message against that word and runs a fixed action instead of starting a normal turn. `!help`, `!configure`, `!restart`, `!mute`, and `!unmute` must stand alone: adding extra words, as in `!restart` with words tacked on, makes the message an ordinary prompt instead. `!feedback`, `!routines`, and `!fork` accept text after the command, covered below.

## See the commands available to you

```text wrap theme={null}
@Claude !help
```

Claude replies with the commands it understands in your workspace. The list can differ by workspace, since a command can be enabled for some workspaces and not others.

## Get the link to configure a channel

```text wrap theme={null}
@Claude !configure
```

Run `!configure` in a channel, and Claude replies in the thread with a link to that channel's Configure page on claude.ai. On that page you [tailor how Claude works in the channel](/docs/claude-tag/users/good-habits#configure-claude-for-a-channel), for example by editing its channel instructions, and it's the same page the **Configure** link in the footer of any Claude reply opens. In a DM with Claude there are no per-channel settings, so Claude replies there with a link to the [Claude Tag admin page](https://claude.ai/admin-settings/claude-tag) instead.

## Restart a stuck or wrong-context session

```text wrap theme={null}
@Claude !restart
```

Use this when a session is stuck, or when it's carrying context you don't want the next reply to build on. Claude archives the current session and starts a fresh one in its place.

Every thread Claude takes part in runs a session of its own, holding that one conversation. Some channels have one more session on top of the per-thread ones. That session belongs to the channel itself, and it's the session Claude works from at the channel's top level, outside any thread. When Claude [replies to a top-level message no one mentioned it in](/docs/claude-tag/users/when-claude-responds), the channel's session is the one replying.

Where you run `!restart` picks which session gets replaced:

* **In a thread**, `!restart` replaces that thread's session. The fresh session rereads the thread, so it keeps what's in the messages and drops everything else the old one was carrying.
* **At a channel's top level**, `!restart` replaces the channel's session. The fresh session picks up from where the old one left off.

Claude confirms once the replacement session is ready. If the restart can't complete, Claude tells you and you can run `!restart` again.

You need the same access to run `!restart` that you'd need to message the session directly; someone who can only observe a thread can't restart it.

## Mute or unmute a thread

```text wrap theme={null}
@Claude !mute
```

Run `!mute` in a thread Claude is part of, and Claude stops replying there. Muting is per thread by design. Other threads, the channel's top level, [routine](/docs/claude-tag/users/proactivity) posts, and service notices are unaffected.

There's no channel-level mute. If you run `!mute` at a channel's top level, Claude posts this hint:

```text wrap theme={null}
:mute: Muting works per thread — reply `@Claude !mute` (or `!unmute`) inside the thread you mean.
```

To quiet unprompted replies across a whole channel, turn the channel's [**Respond automatically** setting](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) off.

Unmute the same way:

```text wrap theme={null}
@Claude !unmute
```

A muted thread also unmutes on any direct `@Claude` mention, so you don't need `!unmute` before asking something new.

You need the same access to mute or unmute a thread that you'd need to message Claude there.

## Send feedback

```text wrap theme={null}
@Claude !feedback
```

Opens a form in Slack for sending feedback on Claude Tag to the team that builds it, along with a note on what the report includes. Add words after `!feedback` and Claude carries them into the form as a starting draft, which you can still edit before submitting:

```text wrap theme={null}
@Claude !feedback the channel summary skipped the pinned thread
```

## List the routines in a channel

```text wrap theme={null}
@Claude !routines
```

Claude replies in the thread with the [routines](/docs/claude-tag/users/proactivity) set up in the channel: the scheduled jobs, watched channels, and other standing work it runs there. The list covers only that channel's routines.

* **For the current channel**, run `!routines` in that channel.
* **For another channel**, add the channel mention or its ID, as in `@Claude !routines #other-channel`. You need to be a member of that channel, and it must belong to your organization. Claude sends the list in a reply only you can see, so that channel's routines aren't posted for everyone in the channel where you asked.

If the single word after `!routines` isn't a channel mention or ID, Claude replies with how to use the command. Adding two or more words makes the message an ordinary prompt that starts a normal turn instead.

## Fork a thread

```text wrap theme={null}
@Claude !fork <prompt>
@Claude !fork #channel <prompt>
```

Run `!fork` from inside a thread Claude is part of, and Claude continues that conversation in a new thread. Leave the channel out to start the new thread in the same channel, or name a channel to continue the conversation there. Use it when a discussion outgrows its thread: a bug report that turns out to belong in the owning team's channel, a request that another team should pick up, or a side question that deserves its own thread.

The fork starts a new thread in Slack and links the two threads together:

* **In the new thread's channel**, Claude posts a new top-level message that links back to the original thread and carries your prompt, then continues in the replies under it. The new conversation starts with the original thread as background, so nobody has to re-explain.
* **Back in the original thread**, Claude replies with a link to the new thread, so anyone following along can see where the conversation continued.

The prompt is required, and it kicks off the new thread: Claude starts working on it there right away.

To fork into another channel, pick it from Slack's `#` autocomplete so it arrives as a channel mention. The channel must be public, and both you and Claude must be members of it; invite Claude with `/invite @Claude` first if it isn't there yet. On Enterprise Grid, a public channel in another workspace of your grid also works when that workspace is paired to the same Claude organization, but a channel shared across workspaces doesn't.

`!fork` works from threads in public channels only. Threads in private channels, DMs, and group DMs can't be forked, since forking would carry the conversation to a different audience.

If the fork can't be set up, Claude replies with a note only you can see, and nothing is posted in either channel.

## Related resources

* [Set up routines](/docs/claude-tag/users/proactivity): the standing work `!routines` lists, and how to create, edit, or disable it
* [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds): what makes Claude reply without any command or mention at all
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the admin controls that decide who can message Claude at all, including its commands
