---
title: Claude API skill
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill
description: An open-source Agent Skill that provides Claude with up-to-date API reference material, SDK documentation, and best practices for building applications with the Claude API and Claude Managed Agents.
---

The `claude-api` skill is an open-source [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) that provides Claude with detailed, up-to-date reference material for building applications on two Anthropic surfaces:

* **Messages API:** The primary surface for single requests, streaming chat, tool use, batch processing, prompt caching, structured outputs, and custom agent loops
* **Claude Managed Agents (beta):** An Anthropic-hosted surface for server-managed stateful agents with Anthropic-hosted tool execution, persistent agent configs, and per-session sandboxes

It covers eight programming languages for both the Messages API and Managed Agents: Python, TypeScript, C#, Go, Java, PHP, Ruby, and cURL.

The skill comes bundled with [Claude Code](https://code.claude.com/docs/en/overview) and is also available in the open-source [Anthropic skills repository](https://github.com/anthropics/skills), where you can install it in any environment that supports Agent Skills.

The skill uses [progressive disclosure](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work) to keep context efficient: Claude loads only the documentation relevant to your project's language, surface (Messages API or Managed Agents), and the specific task at hand (tool use, streaming, batches, and so on), rather than loading everything at once.

## What the skill provides

When triggered, the skill equips Claude with:

**For the Messages API:**

* **Language-specific SDK documentation:** Installation, quick start, common patterns, and error handling for your project's language
* **Tool use guidance:** Language-specific examples and [conceptual foundations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for function calling, including the beta tool runner where available
* **Streaming patterns:** Implementation details for building chat UIs and handling incremental display
* **Batch processing:** Offline batch processing at 50 percent cost
* **Prompt caching:** Prefix-stability design, breakpoint placement, and silent-invalidator audit
* **Model migration:** Step-by-step guidance for migrating to newer Claude models (including the breaking changes and behavior shifts on [Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-5), [Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#migrating-from-claude-sonnet-5), [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide), and [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide))
* **Preserved thinking migration:** Finding, measuring, and fixing the history edits that invalidate `thinking` blocks, available through the `/claude-api preserved-thinking-migration` subcommand
* **Current model information:** Model IDs, context window sizes, and pricing
* **Common pitfalls:** Detailed guidance on avoiding frequent mistakes when integrating with the API

**For Managed Agents (beta):**

* **Onboarding flow:** An interview-driven walkthrough for setting up a new Managed Agent, available through the `/claude-api managed-agents-onboard` subcommand
* **Security guide check:** A read-only check of an agent's settings against [Secure your Managed Agents deployment](https://platform.claude.com/docs/en/managed-agents/secure-deployment), available through the `/claude-api managed-agents-secure` subcommand of the skill bundled with Claude Code
* **Language-specific Managed Agents docs:** Creating persistent agents, starting sessions, streaming events, and handling tool confirmations for Python, TypeScript, C#, Go, Java, PHP, Ruby, and cURL
* **Client patterns:** Lossless stream reconnect, `processed_at` queued/processed gate, interrupt handling, file-mount gotchas, and credential handling
* **Deployment constraints:** Managed Agents is available on the Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) only (not on Amazon Bedrock, Google Cloud, or Microsoft Foundry). The skill routes other deployments to the Messages API and tool use instead.

## When the skill activates

The skill activates in two ways:

**Automatic activation** occurs when:

* Your code imports an Anthropic SDK (`anthropic` for Python, `@anthropic-ai/sdk` for TypeScript/JavaScript)
* You ask Claude to help build, debug, or optimize something with the Claude API, an Anthropic SDK, or Managed Agents
* You add, modify, or tune a Claude feature in a file (prompt caching, adaptive thinking, compaction, tool use, batch, files, citations, memory) or a model reference

**Manual invocation** occurs when you type `/claude-api` (with optional subcommand or prose) in any environment where the skill is installed.

The skill does not activate for general programming tasks, ML/data-science work, or code that imports other AI SDKs (such as OpenAI).

## Supported languages

The skill detects your project's language automatically by examining project files (for example, `requirements.txt` for Python, `tsconfig.json` for TypeScript, `go.mod` for Go) and loads the appropriate documentation.

| Language   | Messages API SDK | Tool runner | Managed Agents |
| ---------- | ---------------- | ----------- | -------------- |
| Python     | Yes              | Yes (beta)  | Yes (beta)     |
| TypeScript | Yes              | Yes (beta)  | Yes (beta)     |
| C#         | Yes              | Yes (beta)  | Yes (beta)     |
| Go         | Yes              | Yes (beta)  | Yes (beta)     |
| Java       | Yes              | Yes (beta)  | Yes (beta)     |
| PHP        | Yes              | Yes (beta)  | Yes (beta)     |
| Ruby       | Yes              | Yes (beta)  | Yes (beta)     |
| cURL       | Yes              | N/A         | Yes (beta)     |

If your project uses multiple languages, Claude asks which one applies. For unsupported languages (Rust, Swift, C++), the skill provides cURL/raw HTTP examples.

## How to use the skill

### In Claude Code (bundled)

The skill ships with [Claude Code](https://code.claude.com/docs/en/overview) and requires no installation. When you ask Claude to help build something with the Claude API, or when your project already imports an Anthropic SDK, the skill activates automatically.

You can also invoke it directly:

Use this skill in Claude Code

```text
/claude-api
```

For more about how bundled skills work in Claude Code, see the [Claude Code skills documentation](https://code.claude.com/docs/en/skills#bundled-skills).

### From the skills repository

The skill source is available in the [Anthropic skills repository](https://github.com/anthropics/skills). You can install it using the `npx` command:

```bash
npx skills add https://github.com/anthropics/skills --skill claude-api
```

Or ask Claude Code to install it as a [Claude Code plugin](https://code.claude.com/docs/en/plugins):

Let Claude Code install this for you

```text
Install the claude-api plugin from the anthropics/skills plugin marketplace
```

<Accordion title="Manual install commands">
  ```text wrap
  /plugin marketplace add anthropics/skills
  /plugin install claude-api@anthropic-agent-skills
  ```
</Accordion>

## Migrating to a newer Claude model

The Claude API skill can perform Claude model migrations across a code base. Invoke it directly with the `migrate` subcommand:

Let Claude Code migrate your code for you

```text
/claude-api migrate this project to the latest Claude Opus model
```

You can also pass a specific scope up front to skip the scope-confirmation question:

Let Claude Code migrate your code for you

```text
/claude-api migrate everything under src/ to the latest Claude Opus model
```

Let Claude Code migrate your code for you

```text
/claude-api migrate apps/api.py and apps/worker.py to the latest Claude Opus model
```

When the scope is ambiguous (for example, a bare `/claude-api migrate to claude-opus-5-5`), the skill asks you to choose among the entire working directory, a specific subdirectory, or an explicit file list before editing any files. This applies to both Messages API and Managed Agents callers.

The skill handles:

* **Model ID swaps**, including typed SDK constants (`Model.CLAUDE_OPUS_4_8` → `Model.CLAUDE_OPUS_5_5`) across all supported languages, and classifying each file as a caller, a model definer, or an opaque string reference before editing
* **Cloud platform detection**, preserving platform-specific model ID formats (for example, the `anthropic.` prefix on Amazon Bedrock) and skipping changes for features that are unavailable on partner-operated platforms
* **Breaking parameter changes**, such as removing `temperature`, `top_p`, and `top_k` for Claude Opus 4.8 and Claude Opus 4.7, and converting `thinking: {type: "enabled", budget_tokens: N}` to `thinking: {type: "adaptive"}`
* **Prefill replacement**, converting assistant-message prefill patterns to [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) where applicable
* **Beta header cleanup**, removing beta headers that the target model doesn't require (for example, `effort-2025-11-24`, `fine-grained-tool-streaming-2025-05-14`, `interleaved-thinking-2025-05-14`) and switching back from `client.beta.messages.create()` (go: `client.Beta.Messages.New()`; java: `client.beta().messages().create()`; csharp: `client.Beta.Messages.Create()`; php: `$client->beta->messages->create()`) to `client.messages.create()` (go: `client.Messages.New()`; java: `client.messages().create()`; csharp: `client.Messages.Create()`; php: `$client->messages->create()`)
* **Effort calibration**, recommending an `output_config.effort` starting point for the target model (for example, the default `high` on Claude Opus 5, and `xhigh` for coding and agentic use cases on Claude Opus 4.8 and Claude Opus 4.7)
* **Prompt-behavior tuning**, flagging length-control, tool-triggering, subagent, and instruction-following prompts that might behave differently on the target model
* **Silent default handling**, opting back into thinking summarization (`thinking.display: "summarized"`) when reasoning is surfaced to users on Claude Opus 4.8 and Claude Opus 4.7
* **Refusal fallback configuration**, adding `stop_reason: "refusal"` handling before reading response content and setting up a [fallback retry path](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) when the target is Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, or Claude Sonnet 5.5 (the server-side `fallbacks` parameter, typically in its `"default"` mode, the SDK refusal-fallback middleware, or a fallback-credit retry), and updating fallback code written against earlier preview shapes

As it edits, the skill explains each change and its motivation inline. On completion, it produces a checklist of items that require manual verification (typically integration tests, length-control prompt tuning, and cost/rate-limit re-baselining).

For the full list of model-specific changes the skill applies, see [Migrating to Claude Opus 5.5 from Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-5), [Migrating to Claude Opus 5.5 from Claude Opus 4.8](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide#migrating-from-claude-opus-4-8), [Migrating to Claude Sonnet 5.5 from Claude Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#migrating-from-claude-sonnet-5), [Claude Haiku 5.5 migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide), and [Claude Fable 5.1 and Claude Mythos 5.1 migration guide](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide).

## Checking an integration for preserved thinking

[Preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) keeps a `thinking` block valid only while the `system` prompt, `tools`, and messages before it stay unchanged. To find and fix the places where your code edits that history, open the repository that builds your requests and invoke the `preserved-thinking-migration` subcommand:

Let Claude Code check your code for you

```text
/claude-api preserved-thinking-migration
```

The skill works through five steps:

1. **Scope:** Checks whether your integration is affected, then sends three test requests to confirm that the API reports a deliberate edit.
2. **Find:** Captures a few of your own multi-turn sessions, diffs consecutive requests, and lists each place your code edits the prefix.
3. **Measure:** Replays the sessions with `"drop_block"` and reports which conversations lose `thinking` blocks, at which turn, and why.
4. **Fix:** Replaces one edit at a time with the matching pattern in [Make changes without editing the prefix](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#replace-prefix-edits), and measures again after each change.
5. **Report:** Summarizes each cause, the change made for it, and the counts before and after.

If your project has an eval, the skill also compares scores and token usage with and without dropped `thinking` blocks.

The test requests and replays are real Messages API requests, billed at the model's normal rates. Each replay requests only a few output tokens and sets `tool_choice` to `none`, so no tool runs. The skill states the cost and asks for your approval before it sends them.

## Setting up a Managed Agent

To scaffold a new Managed Agent, invoke the `managed-agents-onboard` subcommand:

Let Claude Code set up your agent for you

```text
/claude-api managed-agents-onboard
```

The skill runs an interview that walks you through the Managed Agents mental model (Agent configs versus Sessions), templates an agent config, configures environments and tools, sets up the session loop, and emits runnable code for your language. The skill also covers the mandatory **Agent (once) → Session (every run)** flow: `model`, `system`, and `tools` live on the agent, never on the session, and agents should be created once and referenced by ID.

Managed Agents requires the `managed-agents-2026-04-01` beta header, which the SDK sets automatically for all `client.beta.agents.*`, `client.beta.environments.*`, `client.beta.sessions.*`, and `client.beta.vaults.*` calls.

## Checking a Managed Agents deployment

To compare an agent's settings with the guide [Secure your Managed Agents deployment](https://platform.claude.com/docs/en/managed-agents/secure-deployment), invoke the `managed-agents-secure` subcommand of the skill bundled with Claude Code:

Let Claude Code check your agent against the security guide

```text
/claude-api managed-agents-secure
```

Add the agent's ID after the subcommand, or the skill asks for it. The skill fetches the guide, then reads the agent, its recent sessions and [scheduled deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments), and the environments and vaults they use. Unless you ask it not to, it also searches the current folder's files for text that looks like a secret key. It lists only the names of matching files. It changes nothing. The report lists each setting to change with its recommended value, the questions only you can answer, and what it did not read.

The skill reads the agent with the `ant` CLI, so first set up the CLI for the agent's workspace, as the [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) shows. It needs a current version of Claude Code; run `claude update` to upgrade.

## Example usage

Here are examples of tasks the skill helps Claude handle:

**Building a chat application:**

Let Claude Code build this for you

```text
Build a streaming chat UI with the Claude API in TypeScript
```

**Migrating an existing project:**

Let Claude Code migrate your code for you

```text
/claude-api migrate this code base to the latest Claude Opus model and re-tune effort
```

**Onboarding a new Managed Agent:**

Let Claude Code set up your agent for you

```text
/claude-api managed-agents-onboard
```

In each case, the skill loads the relevant language-specific documentation and guides Claude through the implementation using current API patterns and best practices.

## Next steps

<CardGroup cols={2}>
  <Card title="Agent Skills" icon="graduation-cap" href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview">
    Learn about how Agent Skills work and the progressive disclosure model
  </Card>

  <Card title="Client SDKs" icon="code" href="https://platform.claude.com/docs/en/cli-sdks-libraries/overview">
    Browse the official Anthropic SDKs for all supported languages
  </Card>

  <Card title="Skills repository" icon="github-logo" href="https://github.com/anthropics/skills">
    Explore the public Anthropic skills repository on GitHub
  </Card>
</CardGroup>
