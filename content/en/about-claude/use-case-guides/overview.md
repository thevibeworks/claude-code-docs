---
title: Guides to common use cases
url: https://platform.claude.com/docs/en/about-claude/use-case-guides/overview
description: "Explore production guides for building common Claude use cases: ticket routing, customer support agents, content moderation, legal summarization, and commerce agents."
---

Claude is designed to excel in a variety of tasks. Explore these in-depth production guides to learn how to build common use cases with Claude.

<CardGroup cols={2}>
  <Card title="Ticket routing" icon="headset" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing">
    Best practices for using Claude to classify and route customer support tickets at scale.
  </Card>

  <Card title="Customer support agent" icon="robot" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat">
    Build intelligent, context-aware chatbots with Claude to enhance customer support interactions.
  </Card>

  <Card title="Content moderation" icon="verified" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation">
    Techniques and best practices for using Claude to perform content filtering and general content moderation.
  </Card>

  <Card title="Legal summarization" icon="book" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization">
    Summarize legal documents using Claude to extract key information and expedite research.
  </Card>

  <Card title="Commerce agent" icon="building" href="https://platform.claude.com/docs/en/about-claude/use-case-guides/commerce-agents">
    Build shopping and merchant agents from an open-source blueprint that runs on the Messages API, the Claude Agent SDK, and Claude Managed Agents.
  </Card>
</CardGroup>

## Choosing a build path

The three paths for building with Claude differ in how much control you keep and how much of the implementation you offload to Anthropic. The [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) gives you the most control: you write the agent loop and run your own tools and infrastructure. The [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) sits in between, providing the agent loop and tool execution in a process you operate. With [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), you offload the most: Anthropic hosts the agent loop, tool execution, and runtime for you.
