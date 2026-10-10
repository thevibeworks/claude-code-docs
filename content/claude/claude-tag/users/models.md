> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose the model Claude Tag uses

> Ask Claude to switch models in a Slack thread, set a channel's default model, pick the model for your direct messages, or run a thread in fast mode. See which models you can use and how to confirm which one replied.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Every Claude Tag reply in Slack comes from one Claude model, and you choose which one by asking Claude for it in plain language, the same way you hand it any other task. The footer of each reply names the model that handled it, so you can confirm a switch took effect.

Model choice is part of Claude Tag, which is available on Team and Enterprise plans. It isn't available on individual plans (Free, Pro, or Max) or for third-party deployments.

Which models you can ask for depends on your organization; see [which models you can use](#which-models-you-can-use).

## Switch the model in a thread

Tell Claude which model you want, in your own words, in the thread.

```text wrap theme={null}
@Claude switch to Claude Opus 5.5 for the rest of this thread.
```

To confirm the switch, check the reply footers. The reply that acknowledges the switch still names the previous model, because Claude writes it before the switch takes effect; the new model appears in the footer of the reply after it. If the session can't switch to the model you named, Claude says so in that same reply. Asking in a thread changes the model for that thread only. To change what new threads in the channel start on, set a [default model for the channel](#set-a-default-model-for-the-channel) instead.

The same request works in a one-to-one direct message, where it applies to that conversation only. In a group DM, the switch applies to the thread you ask in.

You can name a model family instead of a version, for example "use the latest Opus here". Claude switches to the newest model of that family your organization offers.

## Set a default model for the channel

To change what new threads in a channel start on, ask for the channel, not just the thread.

```text wrap theme={null}
@Claude use Sonnet for this thread, and make it the default model for this channel.
```

Claude sets the channel's default model. New threads in the channel start on it. If you asked for a family rather than a version, the default keeps following that family: when your organization gets a newer model in it, new threads start on the newer model without anyone changing the setting. A thread already underway switches to it at the next message anyone posts there, unless someone in that thread has already had Claude switch models. If an Owner or a [Claude Tag admin](/docs/claude-tag/admins/restrict-access#delegate-claude-tag-administration) has set **Channel member edits** to **Block** for the channel, Claude declines to set the channel default; ask for the thread alone instead.

An Owner sets the same default in Claude Tag admin settings for the whole organization or for one workspace or channel, and a Claude Tag admin can set it for a workspace or channel; see [choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope).

## Choose the model for your direct messages

Open the Claude app's **Home** tab in Slack. When model selection is enabled for your organization, the tab includes a model selector for one-to-one direct messages. New direct message conversations you start with Claude use the model you pick there. The selector offers only the models your organization allows, and lists each model family as an option such as **Opus (latest)** ahead of the specific versions; with a family option, each new direct message conversation starts on the newest model of that family.

The selector doesn't change a conversation already underway. To change one of those, ask Claude to switch in that conversation.

## Run a thread in fast mode

Fast mode gives a thread faster output at a higher cost per token. It's the same [fast mode as in Claude Code](https://code.claude.com/docs/en/fast-mode), and that page lists the models that support it and what it costs. Use it where response time matters more than cost, such as a thread working a live alert.

Fast mode is available once an Owner [allows it for your organization](/docs/claude-tag/admins/customize#allow-fast-mode). To turn it on, send the [`!fast` command](/docs/claude-tag/users/commands#turn-fast-mode-on-or-off) in the thread.

```text wrap theme={null}
@Claude !fast
```

Claude confirms with a reply in the thread.

Fast mode runs on Opus models, so a thread on an Opus model stays on it. If the thread is on another model, such as Sonnet, Claude also switches it to the newest Opus model [you can use](#which-models-you-can-use), and the reply names that model. Replies speed up only if that Opus version supports fast mode.

Fast mode applies to the thread you turn it on in, and new threads start at standard speed. The thread goes back to standard speed in any of these cases:

* You send `@Claude !fast off`
* You ask Claude to [switch models](#switch-the-model-in-a-thread)
* The thread's session is replaced, for example when you [restart it](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session)

After `!fast off`, a thread that Claude switched to Opus stays on Opus. To return to the earlier model, ask Claude to switch.

## Which models you can use

Anthropic manages the list of models on offer, and your organization's settings narrow it. The options include Opus and Sonnet models, drawn from the models your organization allows, and in channels that list applies regardless of your own account's model access. Every list you see in Slack, the direct message selector and the models Claude offers to switch to, is already filtered to that set.

To see the current list, ask in the thread.

```text wrap theme={null}
@Claude what models can I use here?
```

If you ask for a model that isn't on the list, Claude tells you it isn't available, and the thread stays on the model it was already using.

For how your organization's model settings apply in Slack, see [Models your organization allows](/docs/claude-tag/admins/customize#models-your-organization-allows).

## Related resources

* [Get started](/docs/claude-tag/users/getting-started): what else the reply footer links to
* [Commands](/docs/claude-tag/users/commands#turn-fast-mode-on-or-off): where `!fast` works and what Claude replies when it can't change the speed
* [Customize Claude Tag](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope): how admins set a default model per workspace or channel, and how the organization's model policy applies
