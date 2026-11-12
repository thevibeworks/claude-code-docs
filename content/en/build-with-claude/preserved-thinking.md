---
title: Preserved thinking
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking
description: On Claude models that run the prefix check, preserved thinking determines whether the model can use a thinking block you send back from an earlier turn.
featureMetadata:
  status: stable
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-opus-5-5
    - claude-sonnet-5-5
    - claude-haiku-5-5
  supportedPlatforms:
    Claude API: stable
    Amazon Bedrock: stable
    Amazon Bedrock (bedrock-runtime): stable
    Claude Platform on AWS: stable
    Claude Models on Google Cloud (Anthropic managed): stable
    Claude Models on Google Cloud (Google managed): stable
    Microsoft Foundry: stable
---

Claude can build on its reasoning from earlier turns when your code sends the thinking blocks back. *Preserved thinking* determines which of those blocks it can use. On [models with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes), usable blocks stay in context and are billed as input. [Send assistant turns back exactly](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#append-assistant-turns-exactly-as-returned) as the API returned them.

If a request already failed with `The block is bound to a different conversation`, start at [Fix a thinking block bound to a different conversation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation).

## What a thinking block is tied to

On these models, a thinking block is tied to the following:

* **What came before it:** `system`, `tools`, and every earlier message. If any of them changes, the block fails the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check), and the request can get a 400 error. So only add to a conversation (see [Change tools or instructions without failing the prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions)).
* **The model:** a model reads only some other models’ thinking blocks (see [Which model switches keep the reasoning on the Claude API](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#which-model-switches-keep-reasoning)).
* **The account:** blocks from some models are tied to an account (see [Accounts and cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking)).

[`prefix_mismatch_behavior`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#preserved-thinking-controls) chooses whether a request that fails the prefix check gets a 400 error or the API drops the failing blocks. The response’s [`input_transformations`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#input-transformations) lists thinking blocks the API dropped or let through. Dropping thinking has a cost (see [What dropping thinking costs](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost)).

## Switch models and back

Change `model` and keep sending the whole conversation. A thinking block that the new model or account can’t use never causes an error. The API drops it for that request and doesn’t bill it, and Claude answers without that reasoning.

On a [model with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes), [`thinking: {"type": "enabled"}`](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#thinking-type-on-switch) is a 400 error, and a request that fails the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check) can get one.

<Frame>
  ![One history sent to Claude Fable 5.1, Claude Opus 5.5, then Claude Fable 5.1: its blocks are dropped once, then read again](https://platform.claude.com/docs/images/preserved-thinking-switch-and-back.svg)
</Frame>

Claude Opus 5.5 can’t read Claude Fable 5.1’s blocks, so the API drops them for its request. Back on Claude Fable 5.1, they’re read again, because the API never changes your `messages`. On a switch, reasoning is lost permanently only if your code removes it. So don’t remove thinking, and don’t keep a separate history for each model.

A dropped block doesn’t count as a change to the conversation, so both models’ blocks stay valid.

## Switches your code doesn’t make

A router, [a fallback after a refusal](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#after-a-refusal), or a server-side fallback can switch models for you, and [another provider’s model can take a turn](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#other-provider-turns). Keep sending the whole conversation. A turn that holds a `fallback` block has its own rule. For which blocks to leave out, see [Continuing the conversation](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#continuing-the-conversation).

Any switch can pick a model that doesn’t accept system messages. See [When a model doesn’t accept system messages](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#unchosen-switches-details).

## Accounts and cloud platforms

A move to another account or cloud platform works the same way: keep sending the full history.

Thinking blocks from Claude Fable 5.2, Claude Mythos 5.2, Claude Sonnet 5.5, and Claude Haiku 5.5 work only in the account that produced them or a linked one. In any other account, the API drops them, with no error.

[What counts as your account](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#accounts-by-platform) depends on the platform.

## Secrets and untrusted text

Send [a file your user wouldn’t expect Claude to trust](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#untrusted-text) only in a `tool_result` block. When you [remove secrets, personal data, or injected text](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#remove-sensitive-content) from your history, also remove every thinking block after the first place they appear. Claude then works without that reasoning.

## Have an agent check your code

In Claude Code, run `claude update`, then this prompt in the repository that builds your requests:

Let Claude Code check your code for you

```text
/claude-api preserved-thinking-migration
```

With another agent, give it [Change tools or instructions without failing the prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions), and ask it to fix every place where your code changes `system`, `tools`, or an earlier message between requests.

## Technical details

### Which model switches keep the reasoning on the Claude API

A dash means the model you move to can’t read the blocks. After several switches, read one row for each model in your history.

| Model you move from                   | To Claude Fable 5.2 or Claude Mythos 5.2 | To Claude Fable 5.1 or Claude Mythos 5.1 | To Claude Opus 5.5 | To Claude Sonnet 5.5 | To Claude Haiku 5.5 |
| ------------------------------------- | ---------------------------------------- | ---------------------------------------- | ------------------ | -------------------- | ------------------- |
| Claude Haiku 5.5                      | ✅                                        | —                                        | ✅                  | ✅                    | ✅                   |
| Claude Sonnet 5.5                     | ✅                                        | —                                        | ✅                  | ✅                    | —                   |
| Claude Opus 5                         | ✅                                        | ✅                                        | ✅                  | —                    | —                   |
| Claude Opus 5.5                       | ✅                                        | ✅                                        | ✅                  | —                    | —                   |
| Claude Fable 5 or Claude Mythos 5     | ✅                                        | ✅                                        | —                  | —                    | —                   |
| Claude Fable 5.1 or Claude Mythos 5.1 | ✅                                        | ✅                                        | —                  | —                    | —                   |
| Claude Fable 5.2 or Claude Mythos 5.2 | ✅                                        | —                                        | —                  | —                    | —                   |

If a model has no row or no column, use [Earlier models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#earlier-models).

### Earlier models, such as Claude Opus 5 and Claude Sonnet 5

Every Claude model reads blocks from Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 4.5, and earlier Claude Opus, Claude Sonnet, and Claude Haiku models.

| Models you move to                                                                                                  | Read blocks only from                                                             |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 4.5, and earlier Claude Opus, Claude Sonnet, and Claude Haiku models | Each other                                                                        |
| Claude Opus 5                                                                                                       | Itself, and the models in the first row                                           |
| Claude Fable 5 and Claude Mythos 5                                                                                  | Each other, Claude Mythos Preview, Claude Opus 5, and the models in the first row |

### Thinking settings on the new model

[Models with preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes) reject `thinking: {"type": "enabled"}` with a 400 error. When you move a conversation to one of them from a model whose requests set `"enabled"`, send `"adaptive"` instead. Leaving `thinking` out gives adaptive thinking on these models too.

### When a model doesn’t accept system messages

If a model isn’t on the [list of models that accept system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages), leave system messages out of its requests only. Keep them in your stored history. Back on a model that accepts them, send the full stored history again. Coming back without them is a change, and the request can get the 400 error.

### After a refusal

None of the [permitted fallback models](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#naming-your-own-fallback-models) can read the refusing model’s thinking, so the fallback model answers without it. Back on the model you asked for, Claude reads both models’ thinking.

### A turn from another provider’s model

A turn from another provider’s model goes at the end, as `text` and `tool_use` content. Claude’s earlier thinking stays valid.

### What counts as your account on each platform

| Where you call Claude                                                                                       | Your account              |
| ----------------------------------------------------------------------------------------------------------- | ------------------------- |
| Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), or Microsoft Foundry | Your organization         |
| Amazon Bedrock                                                                                              | Your AWS account          |
| Claude Models on Google Cloud (Google managed)                                                              | Your Google Cloud project |

The API can also leave out a thinking block that another account produced, if that account is no longer in good standing. This applies to requests to Claude Fable and Claude Mythos models, Claude Opus 5, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5. The request still succeeds, and the model answers without that block’s reasoning.

## Availability

Preserved thinking is available on select models.

### API support

The models with preserved thinking are in [What each model does when the prefix check fails](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#outcomes).

#### [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

* Availability: Always on

| Status    | Cloud platforms                                                                                                                                                                                                                                                                                                                                                                  | Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview), [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Claude Mythos 5.1](https://platform.claude.com/docs/en/models/mythos-5-1/overview), [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |
| Available | [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)                                                                                                                                                                                                                                                                                 | [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)                                                                                                                                                                                                                                                              |
| Available | [Amazon Bedrock (bedrock-runtime)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)                                                                                                                                                                                                                                                        | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Available | [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)                                                                                                                                                                                                                       | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview)                                                                                                                                                                                                                                                                                                                                                                                                                                  |

#### [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)

* Availability: Always on

| Status    | Cloud platforms                                                                                                                                                                                                                                                                | Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available | Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed) | [Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Claude Mythos 5.2](https://platform.claude.com/docs/en/models/mythos-5-2/overview), [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Claude Mythos 5.1](https://platform.claude.com/docs/en/models/mythos-5-1/overview), [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |

## Next steps

<CardGroup cols={2}>
  <Card title="Prefix checks on thinking blocks" icon="shield" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks">
    What the prefix check compares, what happens when a request fails it, and how to handle both cases.
  </Card>

  <Card title="Change tools or instructions without failing the prefix check" icon="edit" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions">
    What to send instead of each change your code makes to a conversation.
  </Card>

  <Card title="Fix a thinking block bound to a different conversation" icon="wrench" href="https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation">
    Recover a failing conversation, and see what dropping thinking costs.
  </Card>
</CardGroup>
