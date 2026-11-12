---
title: What's new in Claude Sonnet 5.5
url: https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5
description: "What changes when you move from Claude Sonnet 5 to Claude Sonnet 5.5: breaking changes, feature support, behavior differences, pricing, and availability."
---

Claude Sonnet 5.5 offers the best combination of speed and intelligence. Five breaking changes can affect code already running on Claude Sonnet 5:

* [Turn off up-front thinking with `between_tools`](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#turn-off-up-front-thinking).
* [Forced tool use returns an error](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#forced-tool-use-is-not-supported).
* [Thinking blocks are tied to the model and the conversation](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them).
* [Some computer use tool versions are not supported](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#computer-20251124-is-not-supported).
* [The advisor tool rejects four models as advisors](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#advisor-tool-pairings): Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5, and Claude Haiku 5.5.

One more change alters the response shape without failing any request: [text between tool calls comes back in `thinking` blocks](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#text-between-tool-calls). An application that streams that text to its users goes quiet between tool calls until it sets a `display` value that returns the text, or turns off up-front thinking with `between_tools`.

## New model

| Model             | Claude API ID     | Description                                    |
| ----------------- | ----------------- | ---------------------------------------------- |
| Claude Sonnet 5.5 | claude-sonnet-5-5 | The best combination of speed and intelligence |

[Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) is on by default, and the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) controls thinking depth. Its default on the Claude API is `high`. The tokenizer is the same as Claude Sonnet 5’s, so the same text produces the same token counts. For the context window, output limits, knowledge cutoff, and prices, see the [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) model page.

For all current models, see [Models overview](https://platform.claude.com/docs/en/models/overview).

## Breaking changes

### Turn off up-front thinking with `between_tools`

To turn off up-front thinking on Claude Sonnet 5.5, send `thinking: {"type": "between_tools"}` instead of `"disabled"`. It’s the lowest thinking setting on this model. It’s available on every platform that offers Claude Sonnet 5.5. The short [progress updates](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates) the model writes between tool calls still come back as `thinking` blocks with their summary text. Pass those blocks back unchanged with the rest of the assistant turn. A progress-update block you send back gives the model the full note it wrote, not the summary. If your requests don’t use tools, the response contains only text, as with `disabled` on Claude Sonnet 5.

On Claude Sonnet 5.5, a request that sends `thinking: {"type": "disabled"}` returns a 400 `invalid_request_error` whose message points to `between_tools`.

`between_tools` is accepted at `low`, `medium`, and `high` effort. At `xhigh` or `max` effort, a request with `between_tools` returns a 400 error. To run at `xhigh` or `max`, use adaptive thinking: omit the `thinking` field or send `thinking: {"type": "adaptive"}`, which is equivalent. With `between_tools`, effort can’t change mid-conversation: a [per-message `output_config.effort`](https://platform.claude.com/docs/en/build-with-claude/effort-per-message) that differs from the level in effect returns a 400 error. To vary effort for each turn, use adaptive thinking.

`between_tools` takes no other field: `display`, `budget_tokens`, or `block_binding` sent with it returns a 400 error. Manual thinking budgets (`thinking: {"type": "enabled", "budget_tokens": N}`) return a 400 error. See [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) and [Turn off up-front thinking](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#turn-off-up-front-thinking) in the migration guide.

### Forced tool use is not supported

Claude Sonnet 5.5 doesn’t support forced tool use. `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`:

```text wrap
tool_choice: type "tool" and "any" are not supported for this model.
```

`tool_choice: {"type": "auto"}` (the default) and `{"type": "none"}` are supported. The same check applies to the [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting) endpoint. For schema-valid tool input, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use), or move the schema to [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs). To make the model call a tool rather than reply in text, say in the prompt when the tool applies. [Forced tool use is not supported](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#forced-tool-use) in the migration guide shows the before and after.

### Thinking blocks are tied to the model and the conversation

Every thinking block records which model produced it. A conversation that switches models keeps its earlier reasoning only if the model that it switches to can read the earlier model’s thinking blocks:

| Switch                                                                                                            | Keeps its reasoning                                                            |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| To Claude Sonnet 5.5, from Claude Sonnet 5 or earlier, Claude Opus 4.8 or earlier, or Claude Haiku 4.5 or earlier | Yes                                                                            |
| To Claude Sonnet 5.5, from Claude Haiku 5.5                                                                       | Yes, on the Claude API and Claude Models on Google Cloud (Google managed) only |
| To Claude Sonnet 5.5, from any other model                                                                        | No                                                                             |
| From Claude Sonnet 5.5, to Claude Opus 5.5, Claude Fable 5.2, or Claude Mythos 5.2                                | Yes, on the Claude API and Claude Models on Google Cloud (Google managed) only |
| From Claude Sonnet 5.5, to any other model                                                                        | No                                                                             |

When a request carries a block the target model can’t read, the API drops it before the model receives it. The request succeeds, and dropped blocks aren’t billed. With the `thinking-binding-controls-2026-08-01` beta header, the API reports the drop in a top-level `input_transformations` array. See [Switch models and back](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models). For switches that don’t involve Claude Sonnet 5.5, see [Which model switches keep the reasoning on the Claude API](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#which-model-switches-keep-reasoning).

The API also checks whether anything before a Claude Sonnet 5.5 thinking block has changed since the model produced the block. This prefix check covers the `system` prompt, the `tools`, and every earlier message. Keep the conversation append-only: change instructions or tools with [mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) rather than edits.

Failing the [prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check) might or might not result in a [400 error](https://platform.claude.com/docs/en/api/errors#thinking-block-conversation-mismatch). To identify and handle both cases, see [Prefix checks on thinking blocks](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks).

The prefix check runs on the Claude API and on [some cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#feature-availability).

See [Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) and the migration guide’s [note on thinking blocks](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#thinking-blocks).

### Some computer use tool versions are not supported

Claude Sonnet 5.5 supports [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) through the `computer_toolset_20260801` toolset. On Amazon Bedrock, Claude Sonnet 5.5 also accepts the `computer_20251124` tool with the `computer-use-2025-11-24` beta header. Claude Sonnet 5.5 returns a 400 error for any computer use tool version it doesn’t accept, such as `computer_20251124` on the Claude API. The Claude API’s `invalid_request_error` message names the rejected type and, after `Did you mean one of`, lists the tool types the model accepts. The message begins:

```text wrap
'claude-sonnet-5-5' does not support tool types: computer_20251124.
```

Integrations that use the toolset need no change. To move a `computer_20251124` integration to the toolset, follow [Migrate from `computer_20251124`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124), which shows the request before and after. Drop the beta header and replace the `tools` entry with `{"type": "computer_toolset_20260801"}`. Then update your agent loop for member `tool_use` blocks, batch actions, and `toolset_name` on results.

### Some advisor tool pairings are not supported

The [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) is in beta. A Claude Sonnet 5.5 executor accepts only these advisors:

* Claude Mythos 5.2 and Claude Fable 5.2
* Claude Mythos 5.1 and Claude Fable 5.1
* Claude Mythos 5 and Claude Fable 5
* Claude Opus 5.5 and Claude Opus 5
* Claude Sonnet 5.5 itself

Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5, and Claude Haiku 5.5 advisors work with a Claude Sonnet 5 executor. With a Claude Sonnet 5.5 executor, they return a 400 `invalid_request_error`. Every advisor that Claude Sonnet 5.5 accepts returns its advice encrypted, as an `advisor_redacted_result` block. So your client can’t read the advice text. See the advisor tool’s [Model compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#model-compatibility) and [Result variants](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#result-variants).

## Feature support

Claude Sonnet 5.5 supports these features:

* [Per-message effort](https://platform.claude.com/docs/en/build-with-claude/effort-per-message), which is in beta
* [Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)
* [Mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes), which are in beta
* [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), with a minimum cacheable prompt of 512 tokens
* [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
* The [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
* [PDF support](https://platform.claude.com/docs/en/build-with-claude/pdf-support)
* [Vision](https://platform.claude.com/docs/en/build-with-claude/vision)
* Server-side and client-side tools (see [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview))

Claude Sonnet 5 doesn’t support per-message effort, mid-conversation system messages, or mid-conversation tool changes. On Claude Sonnet 5, the minimum cacheable prompt is 1,024 tokens. See each feature’s page for model availability.

### Compact on demand (beta)

With the `compact-2026-09-04` beta header, a request that sends the top-level `compaction` parameter returns a signed `compaction` block that summarizes the messages in that request. In later requests, the block goes first in `messages`, in place of the messages it summarizes. You choose when to compact and which turns to keep after the block. On Claude Sonnet 5.5, the thinking blocks in the kept turns can stay valid after compaction. For the conditions, see [Compaction and preserved thinking](https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid). See [Compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) for platform availability and the full request flow.

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block in a mid-conversation system message can carry a full tool definition instead of a reference. You can add a tool, change its schema, or move a server tool to a newer version mid-conversation without editing `tools` and without losing the prompt cache. See [Define tools in a message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#define-tools-in-a-message-beta).

### Thinking blocks stay with the account that produced them

Thinking blocks that Claude Sonnet 5.5 produces work only in the account that produced them, or in an account linked to it. When another account sends one of these blocks, the API drops the block before the model receives it, and the request succeeds. Blocks from Claude Haiku 5.5, Claude Fable 5.2, and Claude Mythos 5.2 follow the same rule.

On the Claude API and Claude Models on Google Cloud (Google managed), you can see which blocks were dropped. Send the `thinking-binding-controls-2026-08-01` beta header, and the response lists each dropped block in `input_transformations` with `reason: "organization_binding_mismatch"`. See [Accounts and cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking).

## Behavior differences

For guidance on each of the following, see [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5). Claude Sonnet 5.5 differs from Claude Sonnet 5 in these ways, which show up without any code change:

* **Effort levels are recalibrated.** An [effort](https://platform.claude.com/docs/en/build-with-claude/effort) level doesn’t produce the same amount of thinking as it did on Claude Sonnet 5. Re-run your effort sweep rather than carrying a setting over. Start at `high` unless your workload is agentic or latency-sensitive. For agentic coding and multistep tool use, start at `medium` for well-specified tasks and move to `high` for harder or longer ones. For chat and other latency-sensitive work, start at `medium` or `low`.
* **Text between tool calls comes back in thinking blocks.** Between tool calls, notes longer than a sentence or two come back as [progress-update `thinking` blocks](https://platform.claude.com/docs/en/build-with-claude/thinking#progress-updates). Shorter remarks stay `text`. At the default `display: "omitted"`, the progress-update blocks’ text is empty, so an application that streams those notes to its users goes quiet between tool calls, with no error. If you [turn off up-front thinking with `between_tools`](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#turn-off-up-front-thinking), the text comes back. To receive it, see [Text between tool calls is returned in thinking blocks](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#text-between-tool-calls) in the migration guide.
* **Safeguard categories.** The model’s safeguards can decline a request in five [`stop_details` categories](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response). `"cyber"` means the request could enable cyber harm. `"bio"` means it could enable biological harm. `"frontier_llm"` means it could help with the development of competing AI models. `"reasoning_extraction"` means it asks the model to reproduce its internal reasoning in the response text. `"general_harms"` means it falls under another usage-policy area. See [Refusals, fallback, and billing](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#refusals-fallback-and-billing).

## Refusals, fallback, and billing

Everything in [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) applies to Claude Sonnet 5.5. A declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) object naming the policy area.

Handle refusals in your code, and configure fallback. With [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) (`fallbacks: "default"`), a request declined in the `"cyber"` or `"frontier_llm"` category runs again on Claude Sonnet 5. A request declined in the `"bio"`, `"reasoning_extraction"`, or `"general_harms"` category isn’t retried. Server-side fallback is in beta on the Claude API and on [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed). You can also use the [SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) or your own retry.

A refusal that arrives before any output is billed in some refusal categories and not in others. Either way, it counts against your rate limits. See [How refusals are billed](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed).

## Pricing

Claude Sonnet 5.5 has the same prices as Claude Sonnet 5, except for prompt cache reads, which cost $0.10 USD per million tokens, half the Claude Sonnet 5 rate. See [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) for the full list, data residency, and tool pricing.

## Availability

Claude Sonnet 5.5 is available on:

* **Claude API:** all customers, as `claude-sonnet-5-5`
* **AWS:** [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), as `anthropic.claude-sonnet-5-5`, and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), as `claude-sonnet-5-5`
* **Google Cloud:** [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), as `claude-sonnet-5-5`, and [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), as `claude-sonnet-5-5`
* **Microsoft Foundry:** [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), as `claude-sonnet-5-5`

## Migrate from Claude Sonnet 5

Update your model ID:

<CodeGroup exclude="shell">
  ```python Python
  model = "claude-sonnet-5"  # Before
  model = "claude-sonnet-5-5"  # After
  ```

  ```typescript TypeScript
  let model = "claude-sonnet-5"; // Before
  model = "claude-sonnet-5-5"; // After
  ```

  ```csharp C#
  var model = Model.ClaudeSonnet5; // Before
  model = Model.ClaudeSonnet5_5; // After
  ```

  ```go Go
  model := anthropic.ModelClaudeSonnet5  // Before
  model = anthropic.ModelClaudeSonnet5_5 // After
  ```

  ```java Java
  Model model = Model.CLAUDE_SONNET_5; // Before
  model = Model.CLAUDE_SONNET_5_5; // After
  ```

  ```php PHP
  $model = Model::CLAUDE_SONNET_5; // Before
  $model = Model::CLAUDE_SONNET_5_5; // After
  ```

  ```ruby Ruby
  model = Anthropic::Model::CLAUDE_SONNET_5 # Before
  model = Anthropic::Model::CLAUDE_SONNET_5_5 # After
  ```
</CodeGroup>

Then check six things:

1. If your code turns thinking off with `disabled`, send `between_tools` instead, at `high` effort or below.
2. Replace `tool_choice` types `any` and `tool` with `auto` plus [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).
3. Keep conversations append-only. A request that replays a Claude Sonnet 5.5 thinking block after an edit to earlier history can return a 400 error. See [Thinking blocks are tied to the model and the conversation](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#thinking-blocks-are-tied-to-the-model-that-produced-them).
4. If you use computer use through `computer_20251124`, [move to the toolset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124). On Amazon Bedrock, `computer_20251124` also works.
5. If you use the advisor tool with a Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5, or Claude Haiku 5.5 advisor, [switch to an advisor that Claude Sonnet 5.5 accepts](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5#advisor-tool-pairings).
6. If your interface shows the text between tool calls, set `thinking.display` when you use adaptive thinking. With `between_tools`, the text comes back without it. See [Text between tool calls is returned in thinking blocks](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#text-between-tool-calls).

The [Claude Sonnet 5.5 migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide) has step-by-step instructions from Claude Sonnet 5 and earlier models, and the full checklist.

## Next steps

<CardGroup cols={3}>
  <Card title="Models overview" icon="arrow-right" href="https://platform.claude.com/docs/en/models/overview">
    Complete specs and pricing for all current Claude models.
  </Card>

  <Card title="Migration guide" icon="code" href="https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide">
    Move code from Claude Sonnet 5 and earlier models to Claude Sonnet 5.5.
  </Card>

  <Card title="Prompting Claude Sonnet 5.5" icon="terminal" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5">
    Behavioral differences and prompting patterns specific to Claude Sonnet 5.5.
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
