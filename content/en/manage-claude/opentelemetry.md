---
title: OpenTelemetry tracing for the Claude API
url: https://platform.claude.com/docs/en/manage-claude/opentelemetry
description: Trace your Messages API requests, tool uses, and Managed Agents sessions with OpenTelemetry spans from the Claude SDK and the Claude API.
featureMetadata:
  topic:
    title: OpenTelemetry
    url: https://platform.claude.com/docs/en/manage-claude/opentelemetry
  status: beta
---

<Note>
  OpenTelemetry export is in beta. It's provided under your agreement with Anthropic, including the Beta Services section of the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms).
</Note>

<video aria-label="Trace agents with OpenTelemetry on the Claude Platform">
  <source src="https://media.platform.claude.com/docs/opentelemetry/tracing/overview-1080p.mp4" type="video/mp4" media="(min-width: 1280px)" />
  <source src="https://media.platform.claude.com/docs/opentelemetry/tracing/overview-720p.mp4" type="video/mp4" media="(min-width: 640px)" />
  <source src="https://media.platform.claude.com/docs/opentelemetry/tracing/overview-480p.mp4" type="video/mp4" />
</video>

The Claude API and the SDK can trace your Messages API requests, tool uses, and Managed Agents sessions with [OpenTelemetry](https://opentelemetry.io/) (OTel). You can view these traces in the observability platform you already have. Use them to debug failed or slow requests, track token spend and latency, and build evals from real traffic. You can also see each request inside your application's own traces, linked to the user or feature that sent it.

OpenTelemetry is a vendor-neutral standard that most observability platforms support. A *trace* is the full record of one request through your system. A *span* is one step in a trace, such as a model request or a tool use. The API and the SDK use attributes from the [GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai), so platforms that support the conventions can recognize the spans without extra setup.

## Get started

You can set up SDK tracing, API tracing, or both. Set up both to see a request's SDK and API spans in one trace, as in the [example traces](https://platform.claude.com/docs/en/manage-claude/opentelemetry#example-traces-and-how-to-read-them).

Let Claude Code set up this feature for you

```text
Set up OpenTelemetry tracing with the Claude API and Claude SDK
```

<CardGroup cols={3}>
  <Card title="Set up SDK tracing" icon="code-brackets" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk" layout="horizontal">
    Install the SDK and register a tracer provider.
  </Card>

  <Card title="Set up API tracing" icon="cloud" href="https://platform.claude.com/docs/en/manage-claude/opentelemetry/api" layout="horizontal">
    Add a destination in the Claude Console.
  </Card>

  <Card title="Span reference" icon="book" href="https://platform.claude.com/docs/en/api/opentelemetry/spans" layout="horizontal">
    Look up spans and their attributes.
  </Card>
</CardGroup>

| What you get                                                                                                                      | SDK tracing                                                                 | API tracing                                                                                | Both together                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| [Messages API](https://platform.claude.com/docs/en/api/messages/create) requests                                                  | ✅                                                                           | ✅                                                                                          | ✅                                                                                          |
| [Sessions API](https://platform.claude.com/docs/en/managed-agents/sessions) requests                                              | ✅                                                                           | ✅                                                                                          | ✅                                                                                          |
| Token usage (see [Counting tokens](https://platform.claude.com/docs/en/manage-claude/opentelemetry#count-tokens))                 | ✅                                                                           | ✅                                                                                          | ✅                                                                                          |
| Each model run within a request                                                                                                   | —                                                                           | ✅                                                                                          | ✅                                                                                          |
| [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) turns                                               | —                                                                           | ✅                                                                                          | ✅                                                                                          |
| [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), run by the API                        | —                                                                           | ✅                                                                                          | ✅                                                                                          |
| Client tools, run by the [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)                 | ✅                                                                           | —                                                                                          | ✅                                                                                          |
| Tools in a [self-hosted sandbox](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#trace-a-self-hosted-sandbox) | ✅                                                                           | —                                                                                          | ✅                                                                                          |
| Other API requests, such as uploading files                                                                                       | ✅                                                                           | —                                                                                          | ✅                                                                                          |
| Setup                                                                                                                             | [Code](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk) | [Console](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api)             | Both                                                                                       |
| Required permission                                                                                                               | None                                                                        | [Admin](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#what-you-need) | [Admin](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#what-you-need) |
| Coverage                                                                                                                          | Clients using the SDK                                                       | Any client                                                                                 | Any client                                                                                 |
| Cloud platform support                                                                                                            | Any                                                                         | Claude Platform<br />Claude Platform on AWS                                                | Claude Platform<br />Claude Platform on AWS                                                |

For Claude Code, the Agent SDK, or Cowork, see [Claude Code monitoring](https://code.claude.com/docs/en/monitoring-usage), [Agent SDK observability](https://code.claude.com/docs/en/agent-sdk/observability), or [Cowork activity monitoring](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry).

## Send traces to a partner platform

Send traces to any observability platform that accepts OTLP, including these partners:

<CardGroup cols={3}>
  <Card title="Arize AI" image="https://platform.claude.com/docs/images/partner-logos/arize.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/arize-dark.svg" imageOffsetLeft={2} href="https://arize.com/docs/ax/integrations/platforms/claude-managed-agents/claude-managed-agents-tracing">
    Unified observability and evaluation platform for AI.
  </Card>

  <Card title="Braintrust" image="https://platform.claude.com/docs/images/partner-logos/braintrust.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/braintrust-dark.svg" imageHeight={25} imageOffsetLeft={1} href="https://www.braintrust.dev/docs/integrations/ai-providers/anthropic#export-opentelemetry-traces-from-the-claude-api">
    Active observability platform for agents.
  </Card>

  <Card title="Databricks" image="https://platform.claude.com/docs/images/partner-logos/databricks.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/databricks-dark.svg" imageHeight={26} imageOffsetLeft={1} href="https://docs.databricks.com/aws/en/ai-gateway/unified-trace-table">
    Unified AI control plane for observability and evaluation.
  </Card>

  <Card title="Datadog" image="https://platform.claude.com/docs/images/partner-logos/datadog.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/datadog-dark.svg" imageHeight={28} imageOffsetLeft={2} href="https://docs.datadoghq.com/llm_observability/instrument/otel_instrumentation/?tab=python#using-claude-managed-agents">
    AI-powered observability and security.
  </Card>

  <Card title="Dynatrace" image="https://platform.claude.com/docs/images/partner-logos/dynatrace.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/dynatrace-dark.svg" imageHeight={22} href="https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability/integrations/claude-platform">
    Observability built for the age of AI.
  </Card>

  <Card title="Elastic" image="https://platform.claude.com/docs/images/partner-logos/elastic.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/elastic-dark.svg" imageHeight={32} href="https://www.elastic.co/docs/reference/opentelemetry/motlp">
    Observability built on open source.
  </Card>

  <Card title="Grafana Cloud" image="https://platform.claude.com/docs/images/partner-logos/grafana.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/grafana-dark.svg" imageHeight={34} imageOffsetLeft={2} href="https://grafana.com/docs/grafana-cloud/observe-and-act/agent-observability/guides/send-claude-platform-traces/">
    Fully managed open observability platform.
  </Card>

  <Card title="Honeycomb" image="https://platform.claude.com/docs/images/partner-logos/honeycomb.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/honeycomb-dark.svg" imageHeight={36} imageOffsetLeft={4} href="https://docs.honeycomb.io/send-data/use-cases/claude-platform">
    Observability platform for the new shape of software.
  </Card>

  <Card title="Langfuse" image="https://platform.claude.com/docs/images/partner-logos/langfuse.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/langfuse-dark.svg" imageHeight={26} imageOffsetLeft={1} href="https://langfuse.com/integrations/model-providers/claude-platform">
    Open-source agent observability and evaluation platform.
  </Card>

  <Card title="LangSmith" image="https://platform.claude.com/docs/images/partner-logos/langchain.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/langchain-dark.svg" imageHeight={29} href="https://docs.langchain.com/langsmith/trace-anthropic">
    LangSmith agent engineering platform.
  </Card>

  <Card title="New Relic" image="https://platform.claude.com/docs/images/partner-logos/new-relic.svg" imageHeight={27} imageOffsetLeft={1} href="https://docs.newrelic.com/docs/ai-monitoring/opentelemetry-ai-monitoring/#anthropic">
    Intelligent observability platform.
  </Card>

  <Card title="PostHog" image="https://platform.claude.com/docs/images/partner-logos/posthog.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/posthog-dark.svg" imageHeight={29} href="https://posthog.com/docs/ai-observability/installation/anthropic?tab=Claude+Platform&utm_source=anthropic&utm_campaign=anthropic-otel">
    All-in-one platform for building successful products.
  </Card>

  <Card title="Pydantic Logfire" image="https://platform.claude.com/docs/images/partner-logos/pydantic.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/pydantic-dark.svg" imageHeight={24} href="https://pydantic.dev/docs/logfire/integrations/llms/claude-platform/">
    Production-grade AI & general observability.
  </Card>

  <Card title="Sentry" image="https://platform.claude.com/docs/images/partner-logos/sentry.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/sentry-dark.svg" imageHeight={25} href="https://sentry.io/cookbook/trace-claude-platform-with-opentelemetry/">
    Debug your broken code and misbehaving agents.
  </Card>

  <Card title="Snowflake" image="https://platform.claude.com/docs/images/partner-logos/snowflake.svg" imageHeight={30} imageOffsetLeft={2} href="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-gateway/observability#trace-claude-requests">
    Agentic control plane with built-in observability and governance.
  </Card>

  <Card title="Splunk" image="https://platform.claude.com/docs/images/partner-logos/splunk.svg" imageDark="https://platform.claude.com/docs/images/partner-logos/splunk-dark.svg" imageHeight={27} imageOffsetLeft={1} href="https://agent-observability-docs.splunk.com/sdk-api/third-party-integrations/claude">
    Observe, evaluate, and secure agents.
  </Card>
</CardGroup>

## Content modes

Each destination and each SDK client has a content mode, which sets whether spans include model prompts and responses. Set it when you [add a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#add-a-destination) or [configure the SDK](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk#configure-the-sdk).

* **Metadata only** (`metadata_only` in the SDK): The default. Spans include identifiers, timing, status, token counts, and text that you choose, such as the names and descriptions of your agents and tools and the names of your MCP servers.
* **Full content** (`content` in the SDK): Most visibility. Spans include model prompts and responses, and everything in Metadata only.

With Full content, you can also see why a run failed or was slow, read full conversations, and build evals from real traces. In the [OpenTelemetry span reference](https://platform.claude.com/docs/en/api/opentelemetry/spans), attributes that hold prompts and responses are tagged <Badge>Content</Badge>.

<Info>
  Your observability platform stores this content under its own access and retention settings, so check that they meet your organization's requirements.
</Info>

If your organization has a HIPAA, FERPA, or K-12 data-handling restriction with Anthropic, destinations export only metadata regardless of their content mode. SDK spans aren't affected.

With [zero data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention), you can still use Full content. For Messages API requests, the API holds the exported content only in memory until it delivers it to the destination. [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) isn't eligible for zero data retention, and its data retention stays the same when you use OpenTelemetry.

### Content limits

With Full content, each span holds up to 0.75 MB of content by default. That fits a 200k-token context window of English text and stays below the 1 MB request limit of many observability platforms and proxies. If you select a partner platform as the **Provider**, the Console sets a limit that the platform accepts.

When content is over the limit, the SDK or the API shortens it and sets `anthropic.content.truncated` to `true`. Request spans drop the system prompt and the earliest messages first, and tool spans drop blocks from the end of the result. Images and documents appear only as their type.

Change the limit in these cases:

* **Your observability platform accepts larger payloads:** Raise or remove the limit to keep long prompts and responses whole. A full 1M-token context window needs about 4 MB.
* **Your observability platform or a proxy in front of it rejects large requests:** Lower the limit.

In the SDK, set `traces.max_content_bytes` (typescript, java, php: `traces.maxContentBytes`; csharp: `Traces.MaxContentBytes`; go: `option.WithOpenTelemetryTracesMaxContentBytes()`). In the Console, set **Content mode** to **Full content** when you [add a destination](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#add-a-destination), then set **Maximum content size in MB** under **Advanced settings**.

## Example traces and how to read them

### A Messages API request

Under the API span for a request that [creates a message](https://platform.claude.com/docs/en/api/messages/create), the API adds a span for each model request and a tool span for each use of a server tool or an MCP connector tool that the API runs.

In this example, your application calls the [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner), the SDK helper that runs your tools and sends their results back to Claude. Each request that the tool runner sends has a client span from the SDK and a server span from the API. The spans appear in the following order:

1. Your application starts the `answer_question` span and calls the Messages tool runner inside it (shown as the [`anthropic.messages.tool_runner`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-tool-runner) span).
2. The tool runner sends the first request (shown as the first [`anthropic.messages.create`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-create) client span and the spans under it). In this request, the API runs the web search tool between two model requests.
3. In the second model request, the model asks to use the custom `get_weather` tool, so the first request ends.
4. The tool runner runs `get_weather` (shown as the `anthropic.custom_tool_use get_weather` span).
5. The tool runner sends the second request with the tool result (shown as the second `anthropic.messages.create` client span and the spans under it).
6. In the second request, the model gives the final answer.

![Example Messages tool runner trace: two requests with client and server spans, model requests, web\_search, and get\_weather](https://platform.claude.com/docs/images/opentelemetry-sdk-trace-shape.svg)

The SDK in your application emits the [`anthropic.messages.tool_runner`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-tool-runner) span, the [`anthropic.custom_tool_use`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span, and each request's client span. To get these spans, [set up SDK tracing](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk).

Each request has its token usage on several of its spans. To count each token once, see [Counting tokens](https://platform.claude.com/docs/en/manage-claude/opentelemetry#count-tokens).

With [Full content](https://platform.claude.com/docs/en/manage-claude/opentelemetry#choose-a-content-mode), the `anthropic.messages.create` server span has the prompt and the response. The system prompt is in `gen_ai.system_instructions`, the request's messages in `gen_ai.input.messages`, and the response in `gen_ai.output.messages`.

For each span and its attributes, see the [OpenTelemetry span reference](https://platform.claude.com/docs/en/api/opentelemetry/spans).

### A Managed Agents session

A session has a span for each Sessions API request and a turn span for each agent turn. A turn that a request starts is a child of that request's span. A turn contains a span for each model request and each tool that the API runs, except in the [cases listed in the tool span reference](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use). It also contains a span for each outcome evaluation.

This example follows one chat request, in which your application sends a message to a session and runs a custom tool. The trace has spans from both your application and the API, in the following order:

1. Your application receives a `POST /chat` request from a user.
2. Your application starts the SDK's session tool runner, which lists and streams the session's events (shown as the `anthropic.sessions.events.stream` and `anthropic.sessions.events.list` spans).
3. Your application sends the user's message to the session by calling `sessions.events.send`.
4. A turn starts and includes model requests, a `bash` tool use, and a turn on another thread (shown as the first `anthropic.session.turn` span and the spans under it).
5. The model asks to use the [custom tool](https://platform.claude.com/docs/en/managed-agents/tools) `list_issues`, so the turn ends with the stop reason `requires_action`.
6. The session tool runner runs `list_issues` (shown as the `anthropic.custom_tool_use list_issues` span) and sends its result by calling `sessions.events.send`.
7. A second turn starts with the tool result (shown as the last `anthropic.session.turn` span).

![Example Managed Agents session trace: POST /chat, four session event requests, three turns, a bash tool use, and list\_issues](https://platform.claude.com/docs/images/opentelemetry-trace-shape.svg)

The SDK in your application emits the [`anthropic.custom_tool_use`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use) span and each request's client span. To get these spans, [set up SDK tracing](https://platform.claude.com/docs/en/manage-claude/opentelemetry/sdk).

A session's spans can be in several traces, for example when you send a later request from a new root trace. With [multiagent](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) on, a session can also have several threads. To find the spans you need, group them by an ID.

* **One thread:** Group spans by `gen_ai.conversation.id`, which holds the session thread ID. Sort them by start time to read the thread as a transcript.
* **A whole session, with all its threads:** Group spans by `anthropic.session.id`, across traces.

With [Full content](https://platform.claude.com/docs/en/manage-claude/opentelemetry#choose-a-content-mode), you can read a session's content from its spans.

* To read a turn's content, use its [turn span](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-session-turn). The system prompt is in `gen_ai.system_instructions` on a thread's first turn span, the input in `gen_ai.input.messages` (your messages and tool results, `system.message` events, and messages from other threads), and the output in `gen_ai.output.messages` (the agent's messages, tool uses, and tool results).
* To see the arguments and result of a tool use, read its [tool span](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-tool-use-anthropic-mcp-tool-use-and-anthropic-custom-tool-use). The arguments are in `gen_ai.tool.call.arguments`, and the result is in `anthropic.tool_result.content`.

For each span and its attributes, see the [OpenTelemetry span reference](https://platform.claude.com/docs/en/api/opentelemetry/spans).

## Counting tokens

To count each token once, sum the spans of only one source for each request. When a Messages API request has both an SDK span and an API span, sum its API spans. Both are named `anthropic.messages.create`, so tell them apart by kind: the SDK span is `CLIENT` and its child, the API span, is `SERVER`.

For each source, sum only the following spans, because some usage attributes repeat on more than one level of the API spans:

* **SDK spans:** Sum the [`anthropic.messages.create`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-create) spans. If a request has [compactions](https://platform.claude.com/docs/en/build-with-claude/compaction), also add the span's `anthropic.usage.compaction.input_tokens` and `anthropic.usage.compaction.output_tokens`, because the `gen_ai.usage.*` attributes don't include compaction tokens. If a [fallback model](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) served a request, its span has the usage of only the model that served the response.
* **API spans for a Messages API request:** Sum either the [`anthropic.messages.create`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-messages-create) spans or their [`anthropic.model_request`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-model-request) spans, not both. If a request has compactions, also add its [`anthropic.compaction`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-compaction) spans. Don't add the `anthropic.usage.compaction.*` attributes of the `anthropic.messages.create` span as well, because they hold the same tokens.
* **API spans for a Managed Agents session:** Sum the `anthropic.model_request` and [`anthropic.session.outcome_evaluation`](https://platform.claude.com/docs/en/api/opentelemetry/spans#anthropic-session-outcome-evaluation) spans.

Spans can arrive more than once, for example when a delivery is retried. If your observability platform doesn't remove duplicates, count each span once by its trace ID and span ID.

`gen_ai.usage.input_tokens` already includes the tokens read from and written to the prompt cache, so don't add the cache attributes to it. For all usage attributes, see [Token usage](https://platform.claude.com/docs/en/api/opentelemetry/spans#token-usage).

<Note>
  Exported spans aren't guaranteed to be a complete record of your API usage. Their delivery is [best effort](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#delivery-and-health), so a span can be lost. A caller can also leave out a request's spans by turning off the sampled flag in the request's [`traceparent` header](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api#connect-api-spans-to-your-own-traces). To track each API key's usage, for example to spot a leaked key, use the [Usage API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api#usage-api), which also counts the usage of requests without spans.
</Note>
