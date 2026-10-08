---
title: What's new in Claude Haiku 5.5
url: https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5
description: Overview of new capabilities, breaking changes, and behavior changes in Claude Haiku 5.5, with a link to each feature's guide and to the migration guide for code changes.
---

Claude Haiku 5.5 is built for high-volume, latency-sensitive work such as classification, routing, extraction, and subagent tasks. It supports adaptive thinking with the effort parameter, a 1M token context window, and up to 128k output tokens. It uses the same newer tokenizer as Claude 4.7 and later models, so the same text counts as approximately 30% more tokens than on Claude Haiku 4.5. Its thinking blocks work only in the account that produced them, or in an account linked to it.

For code changes, see the [migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide). For model IDs, pricing, and limits, see the [Claude Haiku 5.5 overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview). For prompting guidance, see [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5).

## Summary of changes from Claude Haiku 4.5

Each row names one change, whether it is new, changed, or breaking, and what your code has to do.

| Change                                                                                                                                                          | Type     | Action needed                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| [Adaptive thinking and effort](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#adaptive-thinking-and-effort)                           | New      | Optional: set `effort` to trade response quality against speed and cost.                                          |
| [Larger context window and output](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#larger-context-window-and-output)                   | New      | None. Existing `max_tokens` values stay valid, but thinking tokens count toward them.                             |
| [Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)                                                              | New      | None. Available on the Claude API and Google Cloud.                                                               |
| [Safety classifiers can decline a request](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response)                        | New      | Handle `stop_reason: "refusal"` in your client. Server-side fallback isn't available.                             |
| [Manual extended thinking returns an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking)                            | Breaking | Replace `budget_tokens` with adaptive thinking.                                                                   |
| [Non-default sampling parameters return an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#remove-sampling-parameters)              | Breaking | Omit `temperature`, `top_p`, and `top_k`.                                                                         |
| [Assistant message prefill returns an error](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replace-assistant-prefill)                    | Breaking | End `messages` with a user turn.                                                                                  |
| [Computer use needs the toolset on the Claude API and Google Cloud](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#computer-use-toolset)  | Breaking | Replace `computer_20250124` with `computer_toolset_20260801`.                                                     |
| [Changing earlier turns invalidates thinking blocks](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#keep-earlier-turns-unchanged)         | Breaking | Keep conversations append-only if you send thinking blocks back.                                                  |
| [Responses can begin with thinking blocks](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#responses-can-begin-with-thinking-blocks)   | Changed  | Select content blocks by `type`, not by position.                                                                 |
| [Thinking text is omitted by default](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking)                                  | Changed  | To receive summarized thinking, set `thinking.display` to `"summarized"`.                                         |
| [Same text counts as more tokens](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#same-text-counts-as-more-tokens)                     | Changed  | Recount prompts and revisit `max_tokens` and cost estimates.                                                      |
| [Replaying thinking blocks across accounts](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5#replaying-thinking-blocks-across-accounts) | Changed  | If you replay stored conversations through a different account, replay each through the account that produced it. |

## New capabilities

### Adaptive thinking and effort

With [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking), Claude Haiku 5.5 determines when and how much to think. Adaptive thinking is on by default. While you can still turn thinking off with `thinking: {"type": "disabled"}` at `high` effort or below, the better way to trade response quality against speed and cost is to use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort).

### Larger context window and output

Claude Haiku 5.5 has a 1M token [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) and returns up to 128k output tokens, up from 200k and 64k on Claude Haiku 4.5. Existing `max_tokens` values stay valid, but thinking tokens count toward `max_tokens`, so a small limit can stop after a `thinking` block and before any text. See [Configure thinking](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking).

## Behavior changes

### Responses can begin with thinking blocks

Adaptive thinking is on by default, so a response can begin with one or more `thinking` blocks even when the request doesn't mention thinking. Code that reads the first content block as the answer needs to select blocks by their `type` field. See [Configure thinking](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#configure-thinking) in the migration guide.

### Same text counts as more tokens

Claude Haiku 5.5 uses the same newer tokenizer as Claude 4.7 and later models. As with all models that use this tokenizer, the same input text produces approximately 30% more tokens on Claude Haiku 5.5 than on Claude Haiku 4.5. The exact increase depends on the content. The shape of requests and responses doesn't depend on the tokenizer, but anything you measure or budget in tokens changes. See [Recount tokens](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#recount-tokens) in the migration guide.

### Replaying thinking blocks across accounts

Thinking blocks from Claude Haiku 5.5 work only in the account that produced them, or in an account linked to it. This matters only if you store conversations and replay them through a different account. See [Replay thinking blocks through the account that produced them](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#replay-thinking-blocks-through-the-producing-account).
