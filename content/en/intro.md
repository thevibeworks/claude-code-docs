---
title: Intro to Claude
url: https://platform.claude.com/docs/en/intro
description: Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.
---

<Note>
  Looking to chat with Claude? Visit [claude.ai](https://claude.ai).
</Note>

Anthropic offers two ways to build with Claude, each suited to different use cases:

|                | Messages API                                | Claude Managed Agents                                                     |
| -------------- | ------------------------------------------- | ------------------------------------------------------------------------- |
| **What it is** | Direct model prompting access               | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for**   | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work                                  |

To learn more about each, see [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) and the [Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview).

## Explore the latest generation of Claude models

If you're unsure which model to use, start with [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview) for most workloads. Use [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.

* [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview) (`claude-fable-5-1`) — New — *For demanding reasoning and long-horizon agentic work* — Most capable · Research · Multi-day tasks
* [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview) (`claude-opus-5`) — *For complex agentic coding and enterprise work* — Complex projects · Agents · Coding
* [Claude Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5/overview) (`claude-sonnet-5`) — *The best combination of speed and intelligence* — Everyday tasks · Writing · Cost-efficient
* [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/haiku-4-5/overview) (`claude-haiku-4-5`) — *The fastest model with near-frontier intelligence* — Fastest · Lowest cost · High volume

[Compare models](https://platform.claude.com/docs/en/models/overview)

***

## Recommended path for new developers

Follow these steps to go from zero to a working Claude integration.

<Steps>
  <Step title="Make your first API call">
    Set up your environment, install an SDK, and send your first message to Claude.

    [Go to the quickstart](https://platform.claude.com/docs/en/get-started)
  </Step>

  <Step title="Secure your credentials">
    Set an expiration when you create your API key. Keep the key out of source control, client-side code, and prompts. Check whether your workload can use Workload Identity Federation instead of a static key.

    [Read the authentication guide](https://platform.claude.com/docs/en/manage-claude/authentication)
  </Step>

  <Step title="Understand the Messages API">
    Learn the core request and response structure, including multi-turn conversations, system prompts, and stop reasons.

    [Read the Messages API guide](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
  </Step>

  <Step title="Choose the right model">
    Compare Claude models by capability and cost to pick the best fit for your use case.

    [See the models overview](https://platform.claude.com/docs/en/models/overview)
  </Step>

  <Step title="Explore features and tools">
    Discover what Claude can do: extended thinking, web search, file handling, structured outputs, and more.

    [Browse the features overview](https://platform.claude.com/docs/en/build-with-claude/overview)
  </Step>
</Steps>

***

## Develop with Claude

Anthropic provides developer tools to help you build and scale applications with Claude.

<CardGroup cols={3}>
  <Card title="Developer Console" icon="computer" href="https://platform.claude.com/">
    Explore and understand the API in your browser with playground.
  </Card>

  <Card title="API Reference" icon="code" href="https://platform.claude.com/docs/en/api/overview">
    Explore the full Claude API and client SDK documentation.
  </Card>

  <Card title="Claude Cookbook" icon="chef-hat" href="https://platform.claude.com/cookbook">
    Learn with interactive Jupyter notebooks covering PDFs, embeddings, and more.
  </Card>
</CardGroup>

***

## Key capabilities

Claude can assist with many tasks that involve text, code, and images.

<CardGroup cols={2}>
  <Card title="Text and code generation" icon="text-aa" href="https://platform.claude.com/docs/en/build-with-claude/overview">
    Summarize text, answer questions, extract data, translate text, and explain and generate code.
  </Card>

  <Card title="Vision" icon="image" href="https://platform.claude.com/docs/en/build-with-claude/vision">
    Process and analyze visual input and generate text and code from images.
  </Card>
</CardGroup>

***

## Support

<CardGroup cols={2}>
  <Card title="Help Center" icon="help" href="https://support.claude.com/en/">
    Find answers to frequently asked account and billing questions.
  </Card>

  <Card title="Service Status" icon="chart" href="https://status.claude.com">
    Check the status of Anthropic services.
  </Card>
</CardGroup>
