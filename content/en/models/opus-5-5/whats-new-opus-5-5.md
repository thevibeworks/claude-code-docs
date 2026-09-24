---
title: What's new in Claude Opus 5.5
url: https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5
description: Overview of breaking changes, feature support, and behavior differences in Claude Opus 5.5.
---

Claude Opus 5.5 is built for long-running agentic coding and knowledge work, priced at $4 / $20 USD per million input / output tokens. Four breaking changes affect code already running on Claude Opus 5: [thinking can't be disabled](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-cant-be-disabled), [forced tool use returns an error](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#forced-tool-use-is-not-supported), [thinking blocks are tied to the model and the conversation](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them), and, on the Claude API and Google Cloud, [the earlier `computer_20251124` computer use tool is not accepted](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#computer-20251124-is-not-supported). The first three also apply on Claude Fable 5.1. A further change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#text-between-tool-calls) whose text is empty at the default `display` setting. An application that streams that text to its users as progress updates goes quiet between tool calls until it sets a `display` value that returns the text.

## New model

| Model           | Claude API ID   | Description                                        |
| --------------- | --------------- | -------------------------------------------------- |
| Claude Opus 5.5 | claude-opus-5-5 | For long-running agentic coding and knowledge work |

[Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) is always on, and the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) controls thinking depth; its default on this model is `medium`. For the context window, output limits, knowledge cutoff, and prices, see the [Claude Opus 5.5 model page](https://platform.claude.com/docs/en/models/opus-5-5/overview); for all current models, see the [models overview](https://platform.claude.com/docs/en/models/overview).

## Breaking changes

### Thinking can't be disabled

On Claude Opus 5, thinking is on by default and `thinking: {"type": "disabled"}` is accepted at effort `high` or below. On Claude Opus 5.5, thinking is always on: a request that sets `thinking: {"type": "disabled"}`, or a manual budget with `thinking: {"type": "enabled", "budget_tokens": N}`, returns a 400 `invalid_request_error`. Omit the `thinking` field, or send `thinking: {"type": "adaptive"}`, which is equivalent. No beta header is involved.

The error messages are:

```text wrap
"thinking.type.disabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

```text wrap
"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

The [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) is the control for thinking depth, latency, and cost: lower it where you previously disabled thinking; [Optimizing for cost and intelligence](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort) has measured results for choosing a level. Because every response can begin with one or more `thinking` blocks (returned with an empty `thinking` field at the default `display: "omitted"`), select content blocks by their `type` field rather than by position, and pass `thinking` blocks back unmodified in tool-use loops. Code that already runs on Claude Opus 5 with thinking on needs no change. See [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) and the migration guide's [before and after](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#thinking-cant-be-disabled).

### Forced tool use is not supported

Claude Opus 5.5 doesn't support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

```text wrap
tool_choice: type "tool" and "any" are not supported for this model.
```

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are supported, and the same validation applies to the [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use), or move the schema to [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs). To make the model call a tool rather than reply in text, say in the prompt when the tool applies. The migration guide shows the [before and after](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#forced-tool-use).

### Thinking blocks are tied to the model and the conversation

Every thinking block records which model produced it, and each model reads its own blocks and only some other models'. Claude Opus 5.5 reads thinking blocks from Claude Opus 5 and earlier Opus, Sonnet, and Haiku models, but not from Claude Fable or Claude Mythos models. On the Claude API, Claude Fable 5.1 and Claude Mythos 5.1 read thinking blocks from Claude Opus 5.5; no other model does. A conversation that moves from Claude Opus 5 onto Claude Opus 5.5, or from Claude Opus 5.5 up to Claude Fable 5.1 or Claude Mythos 5.1 on the Claude API, keeps its reasoning. One that moves from Claude Opus 5.5 to any model other than those two, or onto it from a Claude Fable or Claude Mythos model, runs the turns after the switch without the previous model's reasoning. When a request carries a block the target model can't read, the API drops it before the model sees it: the request succeeds, and dropped blocks aren't billed. With the `thinking-binding-controls-2026-08-01` beta header the drop is reported in a top-level `input_transformations` array. See [Switching models mid-conversation](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models).

The API also checks whether anything before a Claude Opus 5.5 thinking block (the `system` prompt, the `tools`, or an earlier message) has changed since the block was produced. As on Claude Fable 5.1, it enforces that check by default for accounts created on or after August 31, 2026, 00:00 UTC, on the Claude API and on cloud platforms. On those accounts, a request that replays a block after such a change returns a 400 error. To drop the affected blocks instead, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. On older accounts, setting that field to either value opts the request in. Keep the conversation append-only so the question never arises: change instructions or tools with [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) rather than edits. See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) and the migration guide's [note on this change](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#thinking-blocks).

### The `computer_20251124` computer use tool is not supported on the Claude API and Google Cloud

Claude Opus 5 accepts [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) both as the `computer_toolset_20260801` toolset and, with the `computer-use-2025-11-24` beta header, as the earlier `computer_20251124` tool. On the Claude API and Google Cloud, Claude Opus 5.5 supports only the toolset: a request that declares a `computer_20251124` tool returns a 400 `invalid_request_error`. The message names the rejected type, then lists the tool types the model does accept (`computer_toolset_20260801` among them) after `Did you mean one of`; it begins:

```text wrap
'claude-opus-5-5' does not support tool types: computer_20251124.
```

To move an existing integration on the Claude API or Google Cloud, follow [Migrate from `computer_20251124`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124): drop the beta header, replace the `tools` entry with `{"type": "computer_toolset_20260801"}`, and update your agent loop for member `tool_use` blocks, batch actions, and `toolset_name` on results. On Amazon Bedrock, the earlier `computer_20251124` tool continues to work on Claude Opus 5.5 as it does on Claude Opus 5, so no change is needed there. For other platforms, see the computer use tool's [Compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#compatibility) section. Integrations that already use the toolset, and the [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool), need no change. The migration guide shows the request [before and after](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#computer-use-toolset).

## Feature support

Claude Opus 5.5 supports [per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) (beta), [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages), [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets), [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) with a 512-token minimum cacheable prompt, [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing), the [Files API](https://platform.claude.com/docs/en/build-with-claude/files), [PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support), [vision](https://platform.claude.com/docs/en/build-with-claude/vision), and server-side and client-side [tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview). On the Claude API and Google Cloud, computer use requires the `computer_toolset_20260801` toolset (see the [breaking change](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#computer-20251124-is-not-supported)). See each feature's page for model availability.

### Fast mode

[Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) (research preview) is available for Claude Opus 5.5 on the Claude API only; it is not available on Amazon Bedrock, Claude Platform on AWS, Google Cloud, or Microsoft Foundry. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header. See [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) for access, supported models, and pricing.

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block in a mid-conversation system message can carry a full tool definition instead of a reference, so you can add a tool, change its schema, or move a server tool to a newer version mid-conversation without editing `tools` and without losing the prompt cache. This works on every model that supports mid-conversation tool changes, including Claude Opus 5.5. See [Define tools in a message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#define-tools-in-a-message-beta).

### Compact on demand (beta)

With the `compact-2026-09-04` beta header, a request that sends the top-level `compaction` parameter returns a signed `compaction` block summarizing the whole conversation, which you then send first in place of the summarized messages. It is available on the models that support compaction, Claude Opus 5.5 included. You choose when to compact, the request can run in the background, and the thinking blocks in the turns you keep can stay valid after the swap (under the conditions in [Compaction and preserved thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid)), which matters on Claude Opus 5.5 because its [thinking blocks are tied to the conversation](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them). See [Compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) for platform availability and the full request flow.

## Behavior differences

Claude Opus 5.5 differs from Claude Opus 5 in several ways that show up without any code change. Each has guidance in [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5):

* **The default effort is `medium`.** A request that omits `effort` runs at `medium`; on Claude Opus 5 it ran at `high`. Set `effort` explicitly and re-run your sweep; see [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#calibrate-effort).
* **More thinking per turn at a given effort level.** At the same [effort](https://platform.claude.com/docs/en/build-with-claude/effort) setting the model tends to think more per turn than Claude Opus 5, most of all at `xhigh` and `max`. Re-run your effort sweep rather than carrying a setting over, and leave room in `max_tokens` for the thinking. See [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#calibrate-effort).
* **Text between tool calls comes back in thinking blocks.** The short notes the model writes between tool calls arrive as [progress-update `thinking` blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates) rather than `text` blocks, so at the default `display: "omitted"` an application that streams them to its users goes quiet between tool calls, with no error. The [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#text-between-tool-calls) has the fix for receiving them, and [User-facing progress updates](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#user-facing-progress-updates) covers how to ask for more of them.
* **More safeguard categories.** The model runs a biology safety classifier in addition to the cybersecurity one, and requests that push it to reproduce its internal reasoning in the response text can be declined with the `reasoning_extraction` category. See [Refusals and fallback](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#refusals-and-fallback) and [Safeguard refusals](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#safeguard-refusals).
* **Sharper reading of charts, diagrams, and screenshots.** The model reads values off dense charts and layout-dependent visuals much more precisely without tools, so prompt-side vision workarounds built for earlier models may no longer be needed; image tools still add accuracy on the densest inputs. See [Tools for complex visual inputs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#tools-for-complex-visual-inputs).

If your Claude Opus 5 integration ran with thinking disabled, see [Prompts written for thinking disabled](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#prompts-written-for-thinking-disabled) alongside the [breaking change](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-cant-be-disabled). For the capability gains in agentic coding and code review, knowledge work, communication, visual inputs, and computer use, see [Capabilities relevant to prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#capability-improvements).

## Refusals and fallback

Claude Opus 5.5 ships with safety classifiers, and everything in [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) applies. A declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) object naming the policy area, so handle refusals and configure fallback: retry on another model with [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) (`fallbacks: "default"`, in beta, retries on the model Anthropic recommends for that category), the [SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback), or your own retry. Whether a refusal that arrives before any output is billed depends on its refusal category, and it counts against your rate limits either way; see [How refusals are billed](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed).

## Pricing

Claude Opus 5.5 costs $4 USD per million input tokens and $20 USD per million output tokens, below Claude Opus 5's $5 and $25, with 5-minute cache writes at $5, 1-hour cache writes at $8, and cache reads at $0.20 per million tokens (0.05x the base input price). [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) is half price: $2 and $10. See [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) for data residency and tool pricing.

## Availability

Claude Opus 5.5 is available on:

* **Claude API:** all customers, as `claude-opus-5-5`.
* **AWS:** [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), as `anthropic.claude-opus-5-5`, and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), as `claude-opus-5-5`.
* **Google Cloud:** [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), as `claude-opus-5-5`.
* **Microsoft Foundry:** [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), as `claude-opus-5-5`.

## Migrate from Claude Opus 5

Update your model ID:

<CodeGroup exclude="shell">
  ```python Python
  model = "claude-opus-5"  # Before
  model = "claude-opus-5-5"  # After
  ```

  ```typescript TypeScript
  let model = "claude-opus-5"; // Before
  model = "claude-opus-5-5"; // After
  ```

  ```csharp C#
  var model = Model.ClaudeOpus5; // Before
  model = Model.ClaudeOpus5_5; // After
  ```

  ```go Go
  model := anthropic.ModelClaudeOpus5  // Before
  model = anthropic.ModelClaudeOpus5_5 // After
  ```

  ```java Java
  Model model = Model.CLAUDE_OPUS_5; // Before
  model = Model.CLAUDE_OPUS_5_5; // After
  ```

  ```php PHP
  $model = Model::CLAUDE_OPUS_5; // Before
  $model = Model::CLAUDE_OPUS_5_5; // After
  ```

  ```ruby Ruby
  model = Anthropic::Model::CLAUDE_OPUS_5 # Before
  model = Anthropic::Model::CLAUDE_OPUS_5_5 # After
  ```
</CodeGroup>

Then remove any `thinking: {"type": "disabled"}` or `thinking: {"type": "enabled", ...}` settings and choose an [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level instead. Replace `tool_choice` types `any` and `tool` with `auto` plus [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use). If you use computer use through `computer_20251124` on the Claude API or Google Cloud, [move to the toolset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124). If your interface shows the text between tool calls, also set `thinking.display`; see [Text between tool calls is returned in thinking blocks](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#text-between-tool-calls). See the [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) for step-by-step instructions from Claude Opus 5 and earlier models, and the full checklist.

## Next steps

<CardGroup cols={3}>
  <Card title="Models overview" icon="arrow-right" href="https://platform.claude.com/docs/en/models/overview">
    Complete specs and pricing for all current Claude models.
  </Card>

  <Card title="Migration guide" icon="code" href="https://platform.claude.com/docs/en/models/opus-5-5/migration-guide">
    Move code from Claude Opus 5 and earlier models to Claude Opus 5.5.
  </Card>

  <Card title="Prompting Claude Opus 5.5" icon="terminal" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5">
    Behavioral differences and prompting patterns specific to Claude Opus 5.5.
  </Card>

  <Card title="Effort" icon="gauge" href="https://platform.claude.com/docs/en/build-with-claude/effort">
    Control how many tokens Claude uses when responding, from low to max.
  </Card>

  <Card title="Thinking" icon="brain" href="https://platform.claude.com/docs/en/build-with-claude/thinking">
    How adaptive thinking works and how thinking blocks are preserved.
  </Card>

  <Card title="Refusals and fallback" icon="shield" href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">
    Handle `stop_reason: "refusal"` and retry on another model.
  </Card>
</CardGroup>
