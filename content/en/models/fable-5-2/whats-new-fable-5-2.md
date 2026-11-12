---
title: What's new in Claude Fable 5.2
url: https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
description: Breaking changes, feature support, pricing, and availability for Claude Fable 5.2 and Claude Mythos 5.2, compared with Claude Fable 5.1 and Claude Mythos 5.1.
---

Claude Fable 5.2 is built for demanding reasoning and long-horizon agentic work. For most workloads, start with the latest Claude Opus model (see [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)), and move to Claude Fable 5.2 when your evals on a Claude Opus model at higher effort still don’t meet your requirements.

Four changes from Claude Fable 5.1 can break your code:

* [Failed prefix checks return a 400 error](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#editing-earlier-turns-invalidates-thinking-blocks).
* [Only Claude Fable 5.2 and Claude Mythos 5.2 read Claude Fable 5.2 thinking blocks](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#thinking-blocks-are-tied-to-the-model-that-produced-them).
* The earlier [`computer_20251124` computer use tool returns an error](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#computer-20251124-is-not-supported) on every platform except Amazon Bedrock.
* With the advisor tool, a Claude Fable 5.2 executor [needs a Claude Fable 5.2 or Claude Mythos 5.2 advisor](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#advisor-tool-pairs).

## Models

| Model             | Claude API ID     | Description                                           | Availability                                                                                                                                                     |
| ----------------- | ----------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude Fable 5.2  | claude-fable-5-2  | For demanding reasoning and long-horizon agentic work | All customers on the Claude API (for other platforms, see [Availability](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#availability)) |
| Claude Mythos 5.2 | claude-mythos-5-2 | Same capabilities as Claude Fable 5.2                 | Organizations verified through Anthropic’s verification programs, such as the [Cyber Verification Program](https://support.claude.com/en/articles/14604842)      |

Claude Fable 5.2 and Claude Mythos 5.2 share these specs:

* **Context window and output:** a [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) (default and maximum) and 128k max output tokens.
* **Thinking:** [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) is always on. Use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.
* **Tokenizer:** the tokenizer introduced with Claude Opus 4.7. See [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting#token-counts-on-claude-fable-5).

For all current models, see [Models overview](https://platform.claude.com/docs/en/models/overview).

## Breaking changes

### Editing earlier turns invalidates thinking blocks

On Claude Fable 5.2 and Claude Mythos 5.2, a request that fails the API’s prefix check gets a [400 error](https://platform.claude.com/docs/en/api/errors#thinking-block-conversation-mismatch). The prefix check tests whether anything before a thinking block has changed since the model produced it. It covers the `system` prompt, the `tools`, and every earlier message (see [What must stay the same, and why](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#prefix-check)). The error message says `The block is bound to a different conversation`.

Nothing changes for you if Claude Code, claude.ai, [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), or the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) builds your requests.

If your own code builds your requests, nothing changes for you either, as long as all of these are true:

* Your code keeps `system` and `tools` the same for the whole conversation.
* Your code only adds to `messages`. It never changes, reorders, or removes an earlier message.
* Your code [sends each assistant turn back exactly as the API returned it](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions#append-assistant-turns-exactly-as-returned): every block, in the same order.
* Your code does none of the things listed in [If your code changes the system prompt, tools, or history](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#what-to-check).

Otherwise, test your code before you switch:

* **Code on Claude Fable 5.1:** Follow the [prefix check section](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide#fable-5-2-preserved-thinking) of the migration guide.
* **Code on Claude Mythos 5.1:** Follow [Migrating to Claude Mythos 5.2 from Claude Mythos 5.1](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide#migrating-from-claude-mythos-5-1-to-claude-mythos-5-2).

For what counts as an edit, see [What counts as a change](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks#what-counts-as-an-edit). To make each change without an edit, see [Change tools or instructions without failing the prefix check](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/change-tools-or-instructions).

To drop the affected thinking blocks and continue without the 400 error, send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. The response then lists each dropped block in a top-level `input_transformations` array. Treat `"drop_block"` as a stopgap while you fix the edit, because [dropping blocks can raise output tokens](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/fix-bound-to-a-different-conversation#drop-block-cost).

### Only Claude Fable 5.2 and Claude Mythos 5.2 read Claude Fable 5.2 thinking blocks

Every thinking block records which model produced it, and a model reads only its own blocks and some other models’ blocks. On the Claude API and Claude Models on Google Cloud (Google managed), Claude Fable 5.2 and Claude Mythos 5.2 read each other’s thinking blocks. On those platforms, they also read blocks from Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5, Claude Fable 5, and Claude Mythos 5. They read blocks from [earlier Claude Opus, Claude Sonnet, and Claude Haiku models](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#earlier-models) too. No other model reads their blocks.

* **Moving onto Claude Fable 5.2 or Claude Mythos 5.2** from one of those models keeps the conversation’s reasoning on the Claude API and Claude Models on Google Cloud (Google managed). So does moving between Claude Fable 5.2 and Claude Mythos 5.2.
* **Moving from Claude Fable 5.2 or Claude Mythos 5.2 to any other model** loses their reasoning for the turns that run there. That includes Claude Opus 5.5, Claude Fable 5.1, Claude Mythos 5.1, and Claude Fable 5.2’s fallback models (Claude Opus 4.8 and Claude Opus 5).

When a request carries a block the current model can’t read, the API drops the block before the model receives it. The request succeeds, and dropped blocks aren’t billed. With the `thinking-binding-controls-2026-08-01` beta header, the response lists the drop in `input_transformations`. See [Switch models and back](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models).

### Use the computer use toolset instead of `computer_20251124`

Claude Fable 5.1 accepts [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) both as the `computer_toolset_20260801` toolset and, with the `computer-use-2025-11-24` beta header, as the earlier `computer_20251124` tool. Claude Fable 5.2 and Claude Mythos 5.2 support computer use through the toolset. A request to either model that declares a `computer_20251124` tool returns a 400 `invalid_request_error` on every platform except Amazon Bedrock. There, both models accept the earlier tool: with the InvokeModel API, send `computer-use-2025-11-24` in the `anthropic_beta` array of the request body.

To move an existing integration, follow [Migrate from `computer_20251124`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#migrate-from-computer-20251124).

### A Claude Fable 5.2 executor needs a Claude Fable 5.2 or Claude Mythos 5.2 advisor

With the [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), which is in beta, the advisor must be at least as capable as the executor. A Claude Fable 5.2 or Claude Mythos 5.2 executor accepts only Claude Fable 5.2 or Claude Mythos 5.2 as its advisor. Any other advisor, including Claude Fable 5.1 and Claude Mythos 5.1, returns a 400 `invalid_request_error`.

If you use the advisor tool and move the executor to one of these models, set the `model` in the advisor tool definition to `claude-fable-5-2` or `claude-mythos-5-2` in the same change. Changing the advisor’s `model` is an edit to `tools`, so make the change in new conversations. A request that sends earlier thinking blocks back after the change fails the [prefix check](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#editing-earlier-turns-invalidates-thinking-blocks) and returns a 400 error, unless you set `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"` (beta, `thinking-binding-controls-2026-08-01` header). To keep your current executor and change only the advisor, set the advisor’s `model` to `claude-fable-5-2`: every executor model accepts it. A Claude Fable 5.2 advisor returns its advice encrypted, so if your code reads the advice text, see [Result variants](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#result-variants). See also [Model compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#model-compatibility).

## Thinking and tool choice

Two Messages API rules apply to every Claude Fable 5.2 request. Neither is a change if you come from Claude Fable 5.1, Claude Mythos 5.1, or Claude Opus 5.5. From Claude Fable 5 or Claude Mythos 5, where adaptive thinking is already always on, only the forced tool use rule is a breaking change. From Claude Opus 5 or an earlier Claude Opus model, both are. The [Claude Fable 5.2 and Claude Mythos 5.2 migration guide](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide) covers each path.

* **Adaptive thinking is always on.** `thinking: {"type": "enabled"}` with `budget_tokens` and `thinking: {"type": "disabled"}` both return a 400 error. Omit `thinking` or send `{"type": "adaptive"}`, and use [effort](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.
* **Forced tool use isn’t supported.** `tool_choice` set to `{"type": "any"}` or `{"type": "tool", "name": "..."}` returns a 400 `invalid_request_error`. For schema-valid JSON, keep `tool_choice: {"type": "auto"}` and set `strict: true` with [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use), or use [JSON outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#usage). In an organization with [customer-managed encryption keys](https://platform.claude.com/docs/en/manage-claude/cmek), [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) aren’t available for Claude Fable 5.2 or Claude Mythos 5.2. That covers both strict tool use and JSON outputs. There, leave out `strict` and validate the tool input in your code.

## Feature support

Claude Fable 5.2 supports these API features, among others:

* **Effort:** all five [effort levels](https://platform.claude.com/docs/en/build-with-claude/effort#effort-levels): `low`, `medium`, `high`, `xhigh`, and `max`. The API default is `high`. Start there, because most of the gain in capability is already present at `high`. Step up to `xhigh` for your hardest long-running coding and agentic work, where you’ve measured a gain. Reserve `max` for measuring the model’s ceiling and for the rare task where time and tokens don’t matter. See [Recommended effort levels for Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-fable-5-2).
* **Compaction on demand (beta):** with the `compact-2026-09-04` beta header, you choose when to replace older turns with a summary. See [Compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand).
* **Mid-conversation tool changes (beta):** you add or remove tools in a `role: "system"` message instead of editing `tools`. On the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), and Microsoft Foundry, send the `inline-tools-2026-09-15` beta header. The `mid-conversation-tool-changes-2026-07-01` header works for changes that name a tool by reference, on the platforms that [Mid-conversation system messages and tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) lists. See [Mid-conversation tool changes](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes).
* **Computer use:** through the `computer_toolset_20260801` toolset. The earlier `computer_20251124` tool returns a 400 error on every platform except Amazon Bedrock. There, Claude Fable 5.2 and Claude Mythos 5.2 also accept the earlier tool. See the [computer use breaking change](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#computer-20251124-is-not-supported) and [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).

Compaction on demand and mid-conversation tool changes help you keep the history append-only, which the [prefix check](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#editing-earlier-turns-invalidates-thinking-blocks) requires. See each feature’s page for model and platform availability.

[Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) is available for Claude Fable 5.2 in Messages API requests on the Claude API, [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), and [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). On Claude in Microsoft Foundry, it’s available for deployments hosted on Anthropic, with its own model ID, `claude-fable-5-2-fast`.

Fast mode is also available for Claude Mythos 5.2 in Messages API requests on the Claude API. [Availability of fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode#feature-availability) lists every platform where Claude Mythos 5.2 has fast mode.

### Thinking blocks stay with the account that produced them

Thinking blocks that Claude Fable 5.2 and Claude Mythos 5.2 produce work only in the account that produced them, or in an account linked to it. When another account sends one of these blocks, the API drops the block before the model receives it, and the request succeeds. On the Claude API and Claude Models on Google Cloud (Google managed), with the `thinking-binding-controls-2026-08-01` beta header, the response lists each dropped block in `input_transformations` with `reason: "organization_binding_mismatch"`. See [Accounts and cloud platforms](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#account-bound-thinking) in Preserved thinking.

## Behavior differences

A few Claude Fable 5.2 behaviors show up without any code change. Check them when you carry prompts over. For guidance on each, see [Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2):

* **Prompt lines that ask for less thinking don’t stop the model from thinking at `medium` effort and above.** Claude Fable 5.1 usually follows a line such as “answer directly without deliberating.” In Anthropic’s testing, such a line didn’t stop Claude Fable 5.2 from thinking at `medium` and above. At `high` and above, the model thinks before almost every reply. If easy requests take too long or cost too much, use a lower effort level for those turns. See [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#calibrate-effort).
* **A turn can end before the work is done.** On long, multistep tasks, the model sometimes ends a turn with a list of what remains, an offer to continue, or a stop at an ordinary obstacle. This occurs more often at `low` and `medium` effort. See [Finish the whole task](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#finish-the-whole-task).
* **What the prompt says about code ownership matters.** In Anthropic’s testing on small coding tasks, when a prompt said nothing about who owns the code, the model tended to add to the existing structure and to report nearby problems instead of fixing them. See [Say who owns the code](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code).
* **Long runs of tool calls can pass with little user-facing text.** The model might also make its first tool call without saying what it’s about to do. See [Keep users informed during long turns](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#keep-users-informed-during-long-turns).
* **How much the model delegates to subagents depends on your harness and tasks.** In an agentic coding product whose prompts invite delegation, the model delegates readily. Subagents can account for a large part of what a session costs. See [Set expectations for subagents](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#set-expectations-for-subagents).
* **The model follows style rules closely.** A hard limit on sentence length can make the model’s prose choppy. See [Review prompts and harnesses designed for earlier models](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#review-instructions-written-for-earlier-models).

## Refusals, fallback, and billing

Claude Fable 5.2 runs safety classifiers, and everything in [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) applies.

* **Refusals:** a declined request returns HTTP 200 with `stop_reason: "refusal"` and a [`stop_details`](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) object naming the policy area that fired.
* **Fallback:** retry a refused request on another model with [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback), the [SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback), or your own retry. Server-side fallback is in beta on the Claude API and Claude Models on Google Cloud (Anthropic managed). With it, `fallbacks: "default"` retries a declined request on the model Anthropic recommends for that category. For categories with no recommended fallback, such as `reasoning_extraction`, the refusal stands. The permitted fallback targets for Claude Fable 5.2 are Claude Opus 4.8 and Claude Opus 5.
* **Billing:** whether a refusal that arrives before any output is billed depends on its refusal category, and it counts against your rate limits either way. See [How refusals are billed](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#how-refusals-are-billed). [Fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) refunds the prompt-cache cost of switching models.

## Pricing

Claude Fable 5.2 and Claude Mythos 5.2 share these prices, in USD:

| Base input | 5m cache writes | 1h cache writes | Cache reads  | Output     |
| ---------- | --------------- | --------------- | ------------ | ---------- |
| $8 / MTok  | $10 / MTok      | $16 / MTok      | $0.20 / MTok | $40 / MTok |

Input and output cost less than on Claude Fable 5.1 and Claude Mythos 5.1. Claude Fable 5.1 and Claude Mythos 5.1 cost $10 USD per million input tokens and $50 USD per million output tokens. Cache reads (hits and refreshes) cost 0.025 times the base input price, the same multiplier as on those models. [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) is $4 USD per million input tokens and $20 USD per million output tokens. [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) for Claude Fable 5.2 and Claude Mythos 5.2 costs $16 USD per million input tokens and $80 USD per million output tokens. See [Fast mode pricing](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing). See [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) for data residency and tool pricing.

## Availability

Claude Fable 5.2 is available on:

* **Claude API:** all customers, as `claude-fable-5-2`
* **AWS:** [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), as `claude-fable-5-2`
* **Amazon Bedrock:** `global.anthropic.claude-fable-5-2` or `us.anthropic.claude-fable-5-2`, on the [`bedrock-runtime` endpoint](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#api-model-ids) only
* **Google Cloud:** [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), as `claude-fable-5-2`, and [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), as `claude-fable-5-2`
* **Microsoft Foundry:** [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), as `claude-fable-5-2`, on Anthropic infrastructure (see [Hosting options](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options))

Claude Mythos 5.2 is available only to organizations verified through Anthropic’s verification programs, such as the [Cyber Verification Program](https://support.claude.com/en/articles/14604842). It’s available on:

* **Claude API:** as `claude-mythos-5-2`
* **Amazon Bedrock:** `global.anthropic.claude-mythos-5-2` or `us.anthropic.claude-mythos-5-2`, on the [`bedrock-runtime` endpoint](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#api-model-ids) only
* **Google Cloud:** [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), as `claude-mythos-5-2`, and [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), as `claude-mythos-5-2`
* **Microsoft Foundry:** [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), as `claude-mythos-5-2`, on Anthropic infrastructure

To request access, apply to the program that covers your use case, or contact your account team.

Claude Fable 5.2 and Claude Mythos 5.2 require 30-day data retention and aren’t available under zero data retention unless expressly authorized by Anthropic. Both are [Covered Models](https://support.claude.com/en/articles/15425695). See [Model-specific data retention requirements](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements).

## Migrate from Claude Fable 5.1

To migrate from Claude Fable 5.1, update your model ID:

<CodeGroup exclude="shell">
  <CodeGroupItem language="cURL">
    Set the `model` field in the request body to `claude-fable-5-2`.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    Set the `--model` flag to `claude-fable-5-2`.
  </CodeGroupItem>

  ```python Python
  model = "claude-fable-5-1"  # Before
  model = "claude-fable-5-2"  # After
  ```

  ```typescript TypeScript
  let model = "claude-fable-5-1"; // Before
  model = "claude-fable-5-2"; // After
  ```

  ```csharp C#
  var model = Model.ClaudeFable5_1; // Before
  model = Model.ClaudeFable5_2; // After
  ```

  ```go Go
  model := anthropic.ModelClaudeFable5_1 // Before
  model = anthropic.ModelClaudeFable5_2  // After
  ```

  ```java Java
  Model model = Model.CLAUDE_FABLE_5_1; // Before
  model = Model.CLAUDE_FABLE_5_2; // After
  ```

  ```php PHP
  $model = Model::CLAUDE_FABLE_5_1; // Before
  $model = Model::CLAUDE_FABLE_5_2; // After
  ```

  ```ruby Ruby
  model = Anthropic::Model::CLAUDE_FABLE_5_1 # Before
  model = Anthropic::Model::CLAUDE_FABLE_5_2 # After
  ```
</CodeGroup>

Then review these items:

1. **Check whether your code edits history.** If your code builds the `messages` array itself, run the test in the migration guide’s [prefix check section](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide#fable-5-2-preserved-thinking).
2. **Check model switches.** If a router or fallback moves conversations between models, expect every model except Claude Mythos 5.2 to drop Claude Fable 5.2’s thinking blocks, Claude Fable 5.1 and Claude Opus 5.5 included. See [Only Claude Fable 5.2 and Claude Mythos 5.2 read Claude Fable 5.2 thinking blocks](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#thinking-blocks-are-tied-to-the-model-that-produced-them).
3. **Move computer use to the toolset.** If you use the `computer_20251124` tool anywhere except Amazon Bedrock, Claude Fable 5.2 returns a 400 error for that tool. Declare `computer_toolset_20260801` instead. For the change itself, see [Use the computer use toolset instead of `computer_20251124`](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#computer-20251124-is-not-supported).
4. **Update the advisor.** If you use the advisor tool with Claude Fable 5.2 as the executor, set the advisor’s `model` to `claude-fable-5-2` or `claude-mythos-5-2`. See [A Claude Fable 5.2 executor needs a Claude Fable 5.2 or Claude Mythos 5.2 advisor](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2#advisor-tool-pairs).
5. **Re-run your evals.** Include an effort sweep that starts at the default, `high`. See [Recommended effort levels for Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-fable-5-2).

See the [Claude Fable 5.2 and Claude Mythos 5.2 migration guide](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide) for step-by-step instructions, including from Claude Mythos 5.1 and from Claude Opus models. For model-specific prompting patterns, see [Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2).

## Next steps

<CardGroup cols={3}>
  <Card title="Models overview" icon="arrow-right" href="https://platform.claude.com/docs/en/models/overview">
    Specs and pricing for every current Claude model.
  </Card>

  <Card title="Migration guide" icon="code" href="https://platform.claude.com/docs/en/models/fable-5-2/migration-guide">
    Move code from Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus models to Claude Fable 5.2 or Claude Mythos 5.2.
  </Card>

  <Card title="Prompting Claude Fable 5.2" icon="terminal" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2">
    Prompting patterns specific to Claude Fable 5.2.
  </Card>
</CardGroup>
