---
title: Model IDs and versioning
url: https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
description: How Claude model IDs are structured and versioned, including the dateless format introduced with the Claude 4.6 generation and what it means for stability.
---

Each Claude model ID identifies a pinned version of the model. When you use a model ID in an API request, the underlying model remains constant for the lifetime of that ID. This guarantee covers model IDs, not the convenience aliases that the Claude API accepts for some earlier models (see [Before the 4.6 generation](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions#before-the-4-6-generation)).

## Model ID format

Claude model IDs follow a versioned naming scheme.

### The 4.6 generation and later

Starting with the Claude 4.6 generation, model IDs use a dateless format:

```text wrap
claude-{name}-{major}[-{minor}]
```

Major-version releases such as Claude Sonnet 5 and Claude Opus 5 omit the minor segment.

For example: `claude-sonnet-4-6`, `claude-sonnet-5`, `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, and `claude-opus-5`

On Amazon Bedrock, the corresponding format is:

```text wrap
anthropic.claude-{name}-{major}[-{minor}]
```

For example: `anthropic.claude-sonnet-4-6`, `anthropic.claude-sonnet-5`, `anthropic.claude-opus-4-7`, `anthropic.claude-opus-4-8`, `anthropic.claude-opus-5`

Claude Opus 4.6 is the last Bedrock model ID to include the `-v1` suffix (`anthropic.claude-opus-4-6-v1`). Anthropic dropped the suffix starting with Claude Sonnet 4.6.

On the `bedrock-runtime` endpoint, models that AWS serves through cross-region inference, including Claude Fable 5.2 and Claude Mythos 5.2, take an inference profile ID: the base model ID with a prefix such as `global.` or `us.`, for example `global.anthropic.claude-fable-5-2`. See [API model IDs](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#api-model-ids).

On [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed) and [Claude Models on Google Cloud (Google managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed), the format matches the Claude API.

### Before the 4.6 generation

Models before the 4.6 generation include a snapshot date in the ID:

```text wrap
claude-{name}-{major}-{minor}-{YYYYMMDD}
```

For example: `claude-haiku-4-5-20251001`

On the Claude API, the Claude 4.5 models also have shorter aliases, such as `claude-haiku-4-5`. Each alias points to the most recent dated snapshot for its minor version.

On Amazon Bedrock (`bedrock-runtime`), dated IDs use the format:

```text wrap
anthropic.claude-{name}-{major}-{minor}-{YYYYMMDD}-v1:0
```

For example: `anthropic.claude-haiku-4-5-20251001-v1:0`

To call these models, add an inference profile prefix, such as `global.` or `us.`, to the ID. For details, see [API model IDs](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#api-model-ids) on the Amazon Bedrock (`bedrock-runtime`) page.

On [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#api-model-ids), the format matches the Claude API.

On Claude Models on Google Cloud (Google managed), the date is separated with `@`:

```text wrap
claude-{name}-{major}-{minor}@{YYYYMMDD}
```

For example: `claude-haiku-4-5@20251001`

[Amazon Bedrock (`bedrock-mantle`)](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock#supported-models), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#available-models), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#api-model-ids-and-deployments) list these models by an ID without the date. Each link opens that platform’s model table, which has the ID to use.

## Dateless IDs are pinned snapshots

A common misconception is that dateless model IDs such as `claude-sonnet-4-6` behave as evergreen pointers that route to the latest or best-performing version. That is not the case.

For the 4.6 generation and later, the dateless ID is the canonical model ID for that release. It maps to a single, fixed model snapshot. Anthropic does not update the weights or configuration of an existing model ID. When an updated version is available, it ships under a new model ID.

An ID from the 4.6 generation or later, such as `claude-sonnet-4-6`, looks like the aliases in [Before the 4.6 generation](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions#before-the-4-6-generation). However, it is not an alias. It is the snapshot.

Every model ID, whether dated or dateless, has its own distinct deprecation and retirement schedule.

## Model weights versus serving infrastructure

Model weights are fixed for a given ID, but the serving infrastructure around the model can change over time. This infrastructure includes components such as the request router, safety classifiers, and sampling logic.

Occasionally, infrastructure updates produce minor differences in observable behavior even when the model ID and weights have not changed. If you notice unexpected behavioral differences on a previously stable model ID, an infrastructure update is the most likely cause.

## Current model IDs

For the current model IDs on every platform, see [Models overview](https://platform.claude.com/docs/en/models/overview).
