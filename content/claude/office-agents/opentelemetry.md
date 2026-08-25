> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure a custom OpenTelemetry collector

> Route the full Claude for M365 audit trail, including prompts, tool inputs and outputs, and document references, to an OpenTelemetry collector you operate.

Route complete audit telemetry from Claude for Excel, PowerPoint, Word,
and Outlook to your own OpenTelemetry (OTEL) collector. This gives you
control over retention and encryption and lets you feed the data into a
SIEM or observability platform.

This capability is available to Claude Enterprise organizations and to
direct-provider deployments on Amazon Bedrock, Google Cloud Vertex AI,
Azure AI Foundry, or an LLM gateway.

## What the collector receives

When a custom collector is configured, the add-in sends trace data for
every user turn. Each turn produces a tree of spans covering the prompt,
each model call, each tool execution, file uploads, and context
compaction.

All span attributes are included. They carry user-generated content:
prompt text, tool inputs and outputs, and document URLs. The allowlist
filter that strips sensitive attributes on the Anthropic path does not
run on this path. One normalization still applies: MCP connector tool
names are recorded as the literal `mcp_tool` rather than the
connector-specific name. Assistant response text is not included in
span data. Your organization owns the collected data; treat the
endpoint as containing prompt and document content when you scope
access controls and retention.

Metrics are not sent to custom collectors. The `office_agent.*` counter
namespace routes to Anthropic only. Every counter increment is also
recorded as a span event on the active span, so the same signals are
recoverable from the trace stream.

Telemetry is sent over OTLP/HTTP to `{your_url}/v1/traces`. gRPC is not
supported because of Office WebView constraints.

## Endpoint requirements

The add-in exports telemetry from each user's browser: the taskpane at
`https://pivot.claude.ai` posts directly to your collector, so every
export is a cross-origin request. The endpoint must:

* Answer the `OPTIONS` preflight with `Access-Control-Allow-Origin`
  covering `https://pivot.claude.ai` and `Access-Control-Allow-Headers`
  covering `Content-Type` plus any headers you configure, such as
  `Authorization`.
* Return the same `Access-Control-Allow-Origin` header on the `POST`
  response.

Managed OTLP ingest endpoints such as Grafana Cloud are built for
server-to-server export and generally do not answer browser CORS
preflights. Point the add-in at an OpenTelemetry Collector you run,
configure the `cors` block on its OTLP HTTP receiver, and have that
collector forward to your backend. The collector makes the authenticated
call to your backend, so no credential needs to appear in export headers
that reach every signed-in user's browser.

## Set up the collector

Configuration differs by how your users sign in.

### Claude Enterprise organizations

An organization administrator sets the collector endpoint in the
Claude admin console under Organization settings, Office agents. Two
settings are available:

| Setting         | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| `otlp_endpoint` | Base URL of your OTLP collector. The add-in appends `/v1/traces`                  |
| `otlp_headers`  | Optional authentication headers in OpenTelemetry `key1=value1,key2=value2` format |

### Direct-provider deployments

Deployments that authenticate against Bedrock, Vertex AI, Foundry, or a
gateway supply the same two keys through the customer-configuration
channels described in
[Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms).

| Key             | Format                    | Description                                       |
| --------------- | ------------------------- | ------------------------------------------------- |
| `otlp_endpoint` | HTTPS URL                 | Collector base URL. Trailing slashes are stripped |
| `otlp_headers`  | `key1=value1,key2=value2` | Optional authentication headers                   |

The `claude-for-msft-365-install` setup plugin writes these for you. To
set them by hand, use any of the three channels below. Later channels override
earlier ones: manifest parameters are read first, then Entra claims,
then the bootstrap response.

**Manifest URL parameter.** Append the keys to the taskpane URL in your
custom manifest.

```text theme={null}
https://pivot.claude.ai/taskpane.html?otlp_endpoint=https://otel-collector.example.com&otlp_headers=Authorization=Bearer%20<token>
```

**Entra ID directory extension.** Register the keys as directory
extension attributes and assign them per user through Microsoft Graph.
The add-in reads them from the user's ID token via Nested App
Authentication. `extn.otlp_endpoint` maps to `otlp_endpoint` and
`extn.otlp_headers` maps to `otlp_headers`.

**Bootstrap endpoint response.** Include the keys in the JSON body your
bootstrap endpoint returns.

```json theme={null}
{
  "otlp_endpoint": "https://otel-collector.example.com",
  "otlp_headers": "Authorization=Bearer <token>"
}
```

### Attribute size cap

Prompt, tool-input, and tool-output attributes are truncated in the
add-in at 4,000 characters each by default and marked with a trailing
`…[truncated]`. Set the `otlp_attr_max_chars` configuration key to a
positive integer to change the cap. Values are clamped to between 256
and 32,000. Before raising the cap, confirm your collector and tracing
backend accept attribute values of the configured size: many backends
truncate or drop over-limit attributes at ingest, and a dropped span is
lost from the audit trail entirely.

## Deployment modes

The audit trail differs slightly depending on the sign-in path.

**Claude Enterprise (OAuth):** full audit trail including user identity
(`user.email`, `user.account_uuid`, `organization.id`), MCP server
metadata, and file-upload spans.

**Direct provider (Bedrock, Vertex AI, Foundry, gateway):** core audit
trail with prompts, tool inputs and outputs, and document URLs. No
Claude user identity, MCP metadata, or file-upload spans. Attribute
activity to a user by correlating `session.id` against your identity
provider or gateway logs.

## Span reference

Each user turn produces up to five span types. `agent.query` is the
root; `agent.stream` and `agent.compaction` are its children;
`agent.tool_execution` is a child of `agent.stream`; `file.upload`
arrives as a separate root span. The `agent.query` and
`agent.compaction` spans carry `agent.surface` (`sheet`, `doc`,
`slide`, or `mail`) and `agent.vendor` (`m` for Microsoft); the other
three do not. To filter those by surface, join `agent.stream` and
`agent.tool_execution` to their parent `agent.query` by trace ID, and
correlate `file.upload` to a turn by `session.id` and timestamp, since
it has its own trace ID and no surface attribute. Attributes marked
*content* carry user-generated data. Attributes marked *Claude sign-in
only* are populated only when users sign in with a Claude account.

### Resource attributes

These are set on every span.

| Attribute         | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `service.name`    | Fixed value `office-agent`                               |
| `service.version` | Fixed value `1.0.0`. Use `git.sha` to identify the build |
| `git.sha`         | Build commit                                             |

### agent.query

Root span, one per user turn. SpanKind `INTERNAL`.

| Attribute                                       | Description                                                   |
| ----------------------------------------------- | ------------------------------------------------------------- |
| `agent.surface`                                 | `sheet`, `doc`, `slide`, or `mail`                            |
| `agent.vendor`                                  | `m`                                                           |
| `user.message` *content*                        | User prompt, truncated per the attribute cap                  |
| `user.message_chars`                            | Pre-truncation length of the prompt                           |
| `session.id`                                    | Opaque session identifier                                     |
| `document.url` *content*                        | URL of the open Office document                               |
| `agent.selected_model`                          | Model selected for the session                                |
| `office.platform`                               | `PC`, `Mac`, `OfficeOnline`, `iOS`, `Android`, or `Universal` |
| `office.version`                                | Office build number                                           |
| `user.email` *Claude sign-in only*              | User email                                                    |
| `user.account_uuid` *Claude sign-in only*       | Claude account UUID                                           |
| `organization.id` *Claude sign-in only*         | Claude organization UUID                                      |
| `org.rate_limit_tier` *Claude sign-in only*     | Subscription tier                                             |
| `mcp.configured_count` *Claude sign-in only*    | Configured MCP servers                                        |
| `mcp.connected_count` *Claude sign-in only*     | Connected MCP servers                                         |
| `mcp.failed_count` *Claude sign-in only*        | Failed MCP connections                                        |
| `file.upload.count` *Claude sign-in only*       | Files attached to the turn                                    |
| `file.upload.total_bytes` *Claude sign-in only* | Total uploaded bytes                                          |
| `error.name`                                    | Exception class name, on failure                              |
| `agent.query_phase`                             | Phase at failure, on failure                                  |

### agent.stream

One span per model API call, child of `agent.query`. SpanKind `CLIENT`.

| Attribute               | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `model`                 | Model ID used                                     |
| `max_tokens`            | Maximum output tokens requested                   |
| `agent.message_count`   | Messages in the conversation at stream start      |
| `input_tokens`          | Input tokens billed                               |
| `output_tokens`         | Output tokens billed                              |
| `cache_read_tokens`     | Tokens served from prompt cache                   |
| `cache_creation_tokens` | Tokens written to prompt cache                    |
| `stop_reason`           | `end_turn`, `tool_use`, `max_tokens`, and similar |
| `request_id`            | Provider request ID for support correlation       |

The add-in requests prompt caching on every call. Cache token attributes
are set from the provider's response and omitted when the provider does
not return them.

### agent.tool\_execution

One span per tool call, child of `agent.stream`. SpanKind `INTERNAL`.
This is the primary record of what the model did to the document.

| Attribute               | Description                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `tool_name`             | Tool identifier, for example `get_cell_ranges` or `execute_office_js`. MCP connector tools are recorded as `mcp_tool` |
| `tool.id`               | Unique invocation ID                                                                                                  |
| `tool.caller`           | `direct` for tools the add-in runs, or `server_tool` for tools the model provider runs                                |
| `tool.owner`            | `first_party` for built-in tools, or `third_party` for MCP connector tools                                            |
| `tool.read_write`       | `read` or `write`                                                                                                     |
| `tool.accept_decision`  | `manual` (user approved this action), `auto_accept` (standing approval), or `deferred` (queued for review)            |
| `tool.input` *content*  | Serialized tool input, truncated per the attribute cap                                                                |
| `tool.success`          | Boolean                                                                                                               |
| `tool.output` *content* | Serialized tool output, truncated per the attribute cap                                                               |
| `tool.output_chars`     | Full output length in characters                                                                                      |
| `tool.error_type`       | Error classification, on failure                                                                                      |
| `sheet.cells_read`      | Cells read, sheet surface only                                                                                        |
| `sheet.cells_written`   | Cells written, sheet surface only                                                                                     |
| `sheet.cells_copied`    | Cells copied, sheet surface only                                                                                      |

### agent.compaction

One span per automatic conversation summarization when context nears
the window limit, child of `agent.query`. SpanKind `CLIENT`. Also
carries `agent.surface`, `agent.vendor`, `session.id`,
`office.platform`, `office.version`, and `user.email` (Claude sign-in
only).

| Attribute                 | Description                      |
| ------------------------- | -------------------------------- |
| `compaction.pre_tokens`   | Token count before summarization |
| `compaction.post_tokens`  | Token count after summarization  |
| `compaction.tokens_saved` | Delta                            |
| `compaction.success`      | Boolean                          |
| `compaction.trigger`      | Currently always `reactive`      |

### file.upload

One span per uploaded file, emitted as its own root span rather than
under `agent.query`. SpanKind `CLIENT`. Claude sign-in only. Also
carries `session.id` and `user.email`. Correlate to the turn by
`session.id` and timestamp.

| Attribute                | Description                    |
| ------------------------ | ------------------------------ |
| `file.upload.size_bytes` | File size                      |
| `file.upload.mime_type`  | MIME type                      |
| `file.upload.file_id`    | Anthropic Files API identifier |
| `file.upload.success`    | Boolean                        |

## Span events

Spans carry timestamped events for lifecycle transitions:

* `agent.query`: `exception`, `file_upload`
* `agent.stream`: `first_token`, `stream_complete`, `stream_error`
* `agent.tool_execution`: `tool_init`, `tool_run`, `tool_result`, `tool_error`
* `agent.compaction`: `compaction_start`, `compaction_complete`, `compaction_error`
* `file.upload`: `exception`

Every internal product counter also records a span event with the same
name on the active span. For example, `office_agent.token.usage` is
emitted on each `agent.stream` span with `token_usage.type` (`input`,
`output`, `cacheRead`, or `cacheCreation`), `token_usage.model`, and
`token_usage.token_count`.

Surface-specific events include `office_agent.cell_edit_collision_total`
on Excel when a user is mid-edit while a tool writes, and the Word
document-edit funnel (`office_agent.doc_edit_received_total`,
`doc_edit_parsed_total`, `doc_edit_applied_total`,
`doc_proposed_edit_reviewed_total`). PowerPoint and Outlook add no
events beyond the common schema.

## Reconstruct a user session

The span tree produces a complete, ordered transcript in both deployment
modes.

For Claude Enterprise deployments, filter `agent.query` spans by
`user.email` or `user.account_uuid` and `session.id`, order them by
timestamp, and read `user.message` and `document.url` for each turn.
Then follow each `agent.query` span's trace ID to its
`agent.tool_execution` descendants, ordered by timestamp, to see what
was attempted (`tool.input`), the result (`tool.output`), and how it was
approved (`tool.accept_decision`).

For direct-provider deployments, filter `agent.query` spans by
`session.id` to isolate one session, use `document.url` to identify the
file, and correlate the session against your Entra sign-in events,
gateway access logs, or bootstrap endpoint logs to attribute it to a
user. Per-turn reconstruction then follows the same trace-ID walk.
