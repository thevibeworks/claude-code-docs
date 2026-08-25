---
title: Claude Fable 5
url: https://platform.claude.com/docs/en/models/fable-5/overview
description: "Claude Fable 5 at a glance: what it's for, model IDs on every platform, context window, output limits, pricing, availability, and the guides and resources for building with it."
---

**Latest.** Released June 9, 2026.

Next-generation intelligence for long-running agents

Model ID: `claude-fable-5`

Context window: 1M tokens · Max output: 128K tokens · Input pricing: $10 / MTok · Output pricing: $50 / MTok

[Announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [What’s new](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5) · [Migration guide](https://platform.claude.com/docs/en/models/fable-5/migration-guide)

## Overview

Claude Fable 5 is Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work. Claude Mythos 5 shares the same capabilities and is available only in limited release through [Project Glasswing](https://anthropic.com/glasswing).

The headline change for integrations: Claude Fable 5 includes safety classifiers that can decline requests. Claude Mythos 5 does not include these classifiers. If your integration calls Claude Fable 5, plan for three changes: new response handling for refusals, fallback options for retrying on another Claude model, and new billing rules. [Refusals, fallback, and billing on Claude Fable 5](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5#refusals-fallback-and-billing-on-claude-fable-5) summarizes all three.

[Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5)

## Fable vs. Mythos

[Claude Mythos 5](https://platform.claude.com/docs/en/models/mythos-5/overview) is offered separately, by invitation only, for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). It shares Claude Fable 5's specifications and pricing; Claude Fable 5 includes safety classifiers that can decline requests, and Claude Mythos 5 does not. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares

| Model                                                                             | Context | Max output | Price / MTok | Latency  | Thinking             | Default effort | Knowledge cutoff |
| :-------------------------------------------------------------------------------- | :------ | :--------- | :----------- | :------- | :------------------- | :------------- | :--------------- |
| **Claude Fable 5** (this model)                                                   | 1M      | 128K       | $10 / $50    | Slower   | Adaptive (always on) | `high`         | Jan 2026         |
| [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview)       | 1M      | 128K       | $5 / $25     | Moderate | Adaptive             | `high`         | May 2026         |
| [Claude Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5/overview)   | 1M      | 128K       | $2 / $10     | Fast     | Adaptive             | `high`         | Jan 2026         |
| [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/haiku-4-5/overview) | 200K    | 64K        | $1 / $5      | Fastest  | Extended             | —              | Feb 2025         |

* **Context:** 1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens. 200k tokens is roughly 150k words.
* **Max output:** Synchronous Messages API limit. On the Message Batches API, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 support up to 300k output tokens with the output-300k-2026-03-24 beta header.
* **Price / MTok:** Input / output, base price per million tokens. Batch API requests are 50% off; prompt caching reads cost 10% of the base input price. See Pricing for the full list.
* **Latency:** Comparative latency, relative to the current lineup, as published in the models overview. Actual latency depends on prompt length, output length, and thinking effort.
* **Thinking:** Adaptive thinking lets the model decide how much to think, steered by effort. Extended thinking is the manual budget\_tokens mode on earlier models.
* **Default effort:** The effort parameter’s default on the Claude API. Models without a value don’t support the parameter.
* **Knowledge cutoff:** Reliable knowledge cutoff: the date through which the model’s knowledge is most extensive and reliable.

## Specifications

### Model IDs

| Platform                                                                                               | Model ID                   |
| :----------------------------------------------------------------------------------------------------- | :------------------------- |
| Claude API                                                                                             | `claude-fable-5`           |
| [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)       | `anthropic.claude-fable-5` |
| [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)              | `claude-fable-5`           |
| [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) | `claude-fable-5`           |
| [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) | `claude-fable-5`           |

### Pricing

| Feature                                                                                | Value                                                               |
| :------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Input                                                                                  | $10 / MTok                                                          |
| Output                                                                                 | $50 / MTok                                                          |
| [5m cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | $12.50 / MTok                                                       |
| [1h cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | $20 / MTok                                                          |
| [Cache read](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)     | $1 / MTok                                                           |
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)    | 50% discount on input and output                                    |
| Full price list                                                                        | [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) |

### Capabilities

| Feature                                                                                 | Value                  |
| :-------------------------------------------------------------------------------------- | :--------------------- |
| [Context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) | 1M tokens              |
| Max output                                                                              | 128K tokens            |
| [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)              | Adaptive (always on)   |
| [Default effort](https://platform.claude.com/docs/en/build-with-claude/effort)          | `high`                 |
| Comparative latency                                                                     | Slower                 |
| Input → output                                                                          | Text and images → text |
| Reliable knowledge cutoff                                                               | Jan 2026               |
| Training data cutoff                                                                    | Jan 2026               |

### Availability

| Feature                                                                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Status](https://platform.claude.com/docs/en/about-claude/model-deprecations) | Active (latest)                                                                                                                                                                                                                                                                                                                                                                                                         |
| Released                                                                      | June 9, 2026                                                                                                                                                                                                                                                                                                                                                                                                            |
| Retirement                                                                    | Not sooner than June 9, 2027                                                                                                                                                                                                                                                                                                                                                                                            |
| Platforms                                                                     | Claude API, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) |

## Resources

<CardGroup cols={3}>
  <Card title="Prompting Claude Fable 5" icon="lightbulb" href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5">
    Model-specific prompting guidance for long-horizon and agentic work.
  </Card>

  <Card title="Refusals and fallback" icon="shield" href="https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback">
    Handle classifier refusals and retry on another Claude model with the `fallbacks` parameter.
  </Card>

  <Card title="Adaptive thinking" icon="brain" href="https://platform.claude.com/docs/en/build-with-claude/thinking">
    The only thinking mode on Claude Fable 5. Steer depth with `effort`.
  </Card>
</CardGroup>

## Reference

<CardGroup cols={3}>
  <Card title="System prompt" icon="text" href="https://platform.claude.com/docs/en/release-notes/system-prompts#claude-fable-5">
    The system prompt Claude Fable 5 uses on claude.ai and the Claude apps.
  </Card>

  <Card title="System card" icon="file" href="https://www.anthropic.com/claude-fable-5-mythos-5-system-card">
    Safety evaluations and deployment decisions for Claude Fable 5 and Claude Mythos 5.
  </Card>

  <Card title="Pricing" icon="coins" href="https://platform.claude.com/docs/en/about-claude/pricing">
    Full price list, including batch discounts and prompt caching rates.
  </Card>

  <Card title="Model IDs and versioning" icon="fingerprint" href="https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions">
    How model IDs, aliases, and pinned snapshots work.
  </Card>

  <Card title="Model deprecations" icon="clock" href="https://platform.claude.com/docs/en/about-claude/model-deprecations">
    Lifecycle status and retirement commitments for every Claude model.
  </Card>
</CardGroup>
