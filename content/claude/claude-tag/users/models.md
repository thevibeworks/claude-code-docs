> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose the model Claude Tag uses

> Ask Claude to switch models in a Slack thread, set a channel's default model, or pick the model for your direct messages. See which models you can use and how to confirm which one replied.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Every Claude Tag reply in Slack comes from one Claude model, and you choose which one by asking Claude for it in plain language, the same way you hand it any other task. The footer of each reply names the model that handled it, so you can confirm a switch took effect.

Which models you can ask for depends on your organization; see [which models you can use](#which-models-you-can-use).

## Switch the model in a thread

Tell Claude which model you want, in your own words, in the thread.

```text wrap theme={null}
@Claude switch to Claude Opus 4.8 for the rest of this thread.
```

To confirm the switch, check the reply footers. The reply that acknowledges the switch still names the previous model, because Claude writes it before the switch takes effect; the new model appears in the footer of the reply after it. Asking in a thread changes the model for that thread only. To change what new threads in the channel start on, set a [default model for the channel](#set-a-default-model-for-the-channel) instead.

The same request works in a direct message, where it applies to that conversation only.

## Set a default model for the channel

To change what new threads in a channel start on, ask for the channel, not just the thread.

```text wrap theme={null}
@Claude use Sonnet for this thread, and make it the default model for this channel.
```

Claude sets the channel's default model, which applies to new threads in that channel. Threads already underway keep the model they started with until someone in them asks Claude to switch. If an admin has set the scope's **Channel member edits** setting to **Block**, Claude declines to set the channel default; ask for the thread alone instead.

Admins set the same default from claude.ai, per workspace or channel; see [choose the model for a scope](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope).

## Choose the model for your direct messages

Open the Claude app's **Home** tab in Slack. When model selection is enabled for your organization, the tab includes a model selector for direct messages. New direct message conversations you start with Claude use the model you pick there. The selector offers only the models your organization allows.

The selector doesn't change a conversation already underway. To change one of those, ask Claude to switch in that conversation.

## Which models you can use

Anthropic manages the list of models on offer, and your organization's settings narrow it. The options include Opus and Sonnet models, drawn from what's available to your organization. Every list you see in Slack, the direct message selector and the models Claude offers to switch to, is already filtered to that set.

To see the current list, ask in the thread.

```text wrap theme={null}
@Claude what models can I use here?
```

If you ask for a model that isn't on the list, Claude tells you it isn't available, and the thread stays on the model it was already using.

## Related resources

* [Get started](/docs/claude-tag/users/getting-started): what else the reply footer links to
* [Customize Claude Tag](/docs/claude-tag/admins/customize#choose-the-model-for-a-scope): how admins set a default model per workspace or channel, and how the organization's model policy applies
