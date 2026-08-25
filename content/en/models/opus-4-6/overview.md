---
title: Claude Opus 4.6
url: https://platform.claude.com/docs/en/models/opus-4-6/overview
description: "Claude Opus 4.6 reference: lifecycle status, model IDs on every platform, context window, output limits, pricing, and migration resources. Claude Opus 4.6 is a legacy model; Claude Opus 5 is the current Opus model."
---

**Legacy.** Released February 5, 2026.

Although Claude Opus 4.6 is still available, you should consider migrating to Claude Opus 5 for improved performance. [See Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview) · [Migrate to Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-46)

Model ID: `claude-opus-4-6`

Context window: 1M tokens · Max output: 128K tokens · Input pricing: $5 / MTok · Output pricing: $25 / MTok

[Announcement](https://www.anthropic.com/news/claude-opus-4-6)

## How it compares to the current lineup

| Model                                                                             | Context | Max output | Price / MTok | Thinking                       | Default effort | Knowledge cutoff |
| :-------------------------------------------------------------------------------- | :------ | :--------- | :----------- | :----------------------------- | :------------- | :--------------- |
| [Claude Fable 5](https://platform.claude.com/docs/en/models/fable-5/overview)     | 1M      | 128K       | $10 / $50    | Adaptive (always on)           | `high`         | Jan 2026         |
| [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview)       | 1M      | 128K       | $5 / $25     | Adaptive                       | `high`         | May 2026         |
| **Claude Opus 4.6** (this model)                                                  | 1M      | 128K       | $5 / $25     | Adaptive (extended deprecated) | `high`         | May 2025         |
| [Claude Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5/overview)   | 1M      | 128K       | $2 / $10     | Adaptive                       | `high`         | Jan 2026         |
| [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/haiku-4-5/overview) | 200K    | 64K        | $1 / $5      | Extended                       | —              | Feb 2025         |

* **Context:** 1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens. 200k tokens is roughly 150k words.
* **Max output:** Synchronous Messages API limit. On the Message Batches API, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 support up to 300k output tokens with the output-300k-2026-03-24 beta header.
* **Price / MTok:** Input / output, base price per million tokens. Batch API requests are 50% off; prompt caching reads cost 10% of the base input price. See Pricing for the full list.
* **Thinking:** Adaptive thinking lets the model decide how much to think, steered by effort. Extended thinking is the manual budget\_tokens mode on earlier models.
* **Default effort:** The effort parameter’s default on the Claude API. Models without a value don’t support the parameter.
* **Knowledge cutoff:** Reliable knowledge cutoff: the date through which the model’s knowledge is most extensive and reliable.

## Specifications

### Model IDs

| Platform                                                                                                              | Model ID                       |
| :-------------------------------------------------------------------------------------------------------------------- | :----------------------------- |
| Claude API                                                                                                            | `claude-opus-4-6`              |
| [Amazon Bedrock (InvokeModel)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy) | `anthropic.claude-opus-4-6-v1` |
| [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)                             | `claude-opus-4-6`              |
| [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)                | `claude-opus-4-6`              |
| [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)                | `claude-opus-4-6`              |

### Pricing

| Feature                                                                                | Value                                                               |
| :------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| Input                                                                                  | $5 / MTok                                                           |
| Output                                                                                 | $25 / MTok                                                          |
| [5m cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | $6.25 / MTok                                                        |
| [1h cache write](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | $10 / MTok                                                          |
| [Cache read](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)     | $0.50 / MTok                                                        |
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)    | 50% discount on input and output                                    |
| Full price list                                                                        | [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) |

### Capabilities

| Feature                                                                                                                     | Value                          |
| :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------- |
| [Context window](https://platform.claude.com/docs/en/build-with-claude/context-windows)                                     | 1M tokens                      |
| Max output                                                                                                                  | 128K tokens                    |
| [Max output (Batch API, beta)](https://platform.claude.com/docs/en/build-with-claude/batch-processing#extended-output-beta) | 300K tokens                    |
| [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)                                                  | Adaptive (extended deprecated) |
| [Default effort](https://platform.claude.com/docs/en/build-with-claude/effort)                                              | `high`                         |
| Input → output                                                                                                              | Text and images → text         |
| Reliable knowledge cutoff                                                                                                   | May 2025                       |
| Training data cutoff                                                                                                        | Aug 2025                       |

### Availability

| Feature                                                                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Status](https://platform.claude.com/docs/en/about-claude/model-deprecations) | Active (legacy)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Released                                                                      | February 5, 2026                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Retirement                                                                    | Not sooner than February 5, 2027                                                                                                                                                                                                                                                                                                                                                                                                             |
| Platforms                                                                     | Claude API, [Amazon Bedrock (InvokeModel)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy), [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) |

## Resources

<CardGroup cols={3}>
  <Card title="Migrate to Claude Opus 5" icon="arrows-left-right" href="https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-46">
    What changes when moving from Claude Opus 4.6 and earlier Opus models to Claude Opus 5.
  </Card>

  <Card title="Claude Opus 5" icon="arrow-right" href="https://platform.claude.com/docs/en/models/opus-5/overview">
    The current Opus model: overview, specs, and resources.
  </Card>
</CardGroup>

## Reference

<CardGroup cols={3}>
  <Card title="System prompt" icon="text" href="https://platform.claude.com/docs/en/release-notes/system-prompts#claude-opus-4-6">
    The system prompt Claude Opus 4.6 uses on claude.ai and the Claude apps.
  </Card>

  <Card title="System card" icon="file" href="https://www.anthropic.com/claude-opus-4-6-system-card">
    Safety evaluations and deployment decisions for Claude Opus 4.6.
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

  <Card title="Amazon Bedrock (Opus 4.6 and earlier)" icon="cloud" href="https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy">
    Claude Opus 4.6 uses the InvokeModel Bedrock integration and Bedrock-style model IDs.
  </Card>
</CardGroup>
