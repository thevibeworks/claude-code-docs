# Preserved thinking: changing how the Messages API handles thinking blocks to protect against distillation

We're changing how the Messages API handles thinking blocks to protect against distillation. A thinking block is a record of the reasoning Claude may produce while working on a response. On Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5, new API accounts can no longer edit the context around a thinking block, such as the messages, tools, or system prompt, during a multi-turn conversation. On Claude Fable 5.2 and Claude Mythos 5.2, preserved thinking applies to all API accounts.

Modifying this prior context has legitimate applications, which we continue to support using the adjustments outlined below. However, such modifications are also a common and **[publicly documented technique](https://arxiv.org/abs/2608.09867)** for industrial-scale illicit distillation, which is prohibited by our **[Usage Policy](https://www.anthropic.com/legal/aup)** and Terms of Service.

The API now verifies that a thinking block is sent back with the same system prompt, tools, and messages that produced it, and will return an error if they don't match. In order for modified requests to succeed, developers may opt-in to instead have the thinking blocks *removed* from such requests; the model will respond without seeing the thinking block.

In this article, we share details on why we're doing this and the adjustments you can make to minimize disruption.

## What are thinking blocks?

Claude produces reasoning steps before providing its final answer. On the API, these are returned to the user as encrypted "thinking blocks." In a multi-turn conversation, API users send these blocks back with each exchange (along with the system prompt, tools, and earlier messages), so that Claude has full conversational context.

## What’s changing?

For affected accounts using the models listed below, the API will return an error if the system prompt, tools, or messages preceding a prior thinking block have been modified.

To avoid an error message, you can choose to drop the affected thinking blocks (see the docs below for the header and setting). The request will then go through, but the model won’t see those blocks. This allows you to continue your conversation or task uninterrupted despite the prior turns’ thinking not being shown to the model. When this happens, the API response will tell you which blocks were dropped. Dropping blocks can significantly increase output tokens, so use it as a stopgap while you update your integration, not as a long-term setting.

## Why are we making this change?

Altering the earlier turns of a conversation is a **[common technique](https://arxiv.org/abs/2608.09867)** used in illicit distillation campaigns, which aim to extract the capabilities of advanced models—especially thinking—to train another model, without authorization. Distillation is often employed on an industrial scale, using thousands of fake accounts. We encrypt Claude's thinking blocks to prevent this, but by editing the conversation before a thinking block, a user could get Claude to decrypt and print its reasoning. Systems trained this way can inherit capabilities they wouldn’t otherwise have, *without* inheriting the safeguards that we've built to prevent a broad range of misuse like cyberattacks and weapons development.

This change aims to make distillation campaigns more difficult to execute. It builds on existing anti-distillation measures like **[enhanced distillation classifiers](https://www.anthropic.com/research/next-generation-constitutional-classifiers)** and restrictions on transferring sessions or reasoning from more advanced models to less capable models with weaker safeguards.

## What does this mean for API integrations?

Certain integrations—particularly those that involve rewriting earlier turns mid-conversation, like context compaction, injected system reminders, or changing tools mid-session—may need adjustment.

Here are the resources to help guide you through this update:

- The **[preserved thinking documentation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)** covers where the change applies, how to check whether your integration is affected, and **[how to make common edits](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#replace-prefix-edits)** without breaking preserved thinking.

- **[Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)** (beta) can summarize older turns while keeping the most recent turns word for word, and can build the summary in the background while your agent keeps working. It replaces client-side compaction, which is likely the most common reason integrations need to change.

- **[Mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes)** (beta) let you add or remove tools during a conversation without editing earlier turns.

- Our **[migration guides](https://platform.claude.com/docs/en/about-claude/models/migration-guide)** have a full checklist for moving to each model.

Check each page for availability on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

There are additional benefits to keeping thinking blocks consistent: it means that the API can reuse cached prompts more often, which reduces costs and response time.

## Who will this impact?

Preserved thinking applies to these models and accounts:

| **Model**         | **API accounts created on or after August 31, 2026 (00:00 UTC)** | **Accounts created before then** |
| ----------------- | ---------------------------------------------------------------- | -------------------------------- |
| Claude Mythos 5.2 | Applies                                                          | Applies                          |
| Claude Fable 5.2  | Applies                                                          | Applies                          |
| Claude Fable 5.1  | Applies                                                          | Doesn't apply                    |
| Claude Opus 5.5   | Applies                                                          | Doesn't apply                    |
| Claude Sonnet 5.5 | Applies                                                          | Doesn't apply                    |
| Claude Haiku 5.5  | Applies                                                          | Doesn’t apply                    |

This covers Claude Platform organizations, Amazon Bedrock accounts, Google Cloud Vertex AI projects, and Microsoft Foundry projects.

We took a phased approach to enforcement, starting with new accounts, where we see the highest concentration of distillation-related abuse. On Claude Fable 5.2 and Claude Mythos 5.2, preserved thinking applies to all API accounts.

If you use Claude Code, Claude Cowork, or Claude.ai, there's nothing you need to change; those products handle thinking blocks for you.

## Thinking can only be read by the account that created it

On Claude Mythos 5.2, Claude Fable 5.2, Claude Sonnet 5.5, and Claude Haiku 5.5, a thinking block can only be read by the account that created it, or by an account linked to it.

Thinking blocks can contain private information. Because they are encrypted, that information isn't visible when you inspect a transcript. This check helps keep a shared or leaked transcript from exposing the reasoning inside it. It also makes it harder for distillers to move harvested transcripts to new accounts after we ban the account that produced them.

If a request includes thinking from an account that isn't linked, the API drops that thinking and the request continues. It doesn't return an error. The next response may be slower and use more tokens, similar to a compaction.

Accounts in the same Claude Platform parent organization, AWS organization, or Google Cloud organization are linked automatically.

In Claude Code, switching accounts in the middle of a session has the same effect: the next response is slower and uses more tokens.