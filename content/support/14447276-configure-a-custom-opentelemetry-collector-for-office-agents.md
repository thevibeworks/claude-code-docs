# Configure a custom OpenTelemetry collector for Office agents

You can route full audit telemetry from Office agents to your own OpenTelemetry (OTEL) collector. This gives your organization complete control over retention, encryption, and integration with your SIEM or observability platform.

This guide covers how to enable a custom collector, what data you'll receive, and the full span schema reference.

Custom OTEL collectors are available to Claude Enterprise organizations and to direct-provider deployments (Amazon Bedrock, Google Vertex AI, or a gateway).

## What you'll receive

When you configure a custom collector, Office agents send trace data covering every user turn. Each turn produces a tree of spans capturing the prompt, model calls, tool executions, file uploads, and context compaction events.

Your collector receives all span attributes, including those carrying user-generated content (prompt text, tool inputs and outputs, document URLs, and filenames). No attributes are redacted or filtered. Assistant response text is not included in the emitted span data. Your organization owns this data.

**Important:** Metrics aren't sent to custom collectors. The `office_agent.*` counter namespace routes to Anthropic only. However, every counter increment also appears as a span event on the active span, so the same signals are available in your traces.

Telemetry is sent via OTLP/HTTP to your endpoint at `{your_url}/v1/traces`. gRPC isn't supported because the add-in runs in an Office WebView.

---

## Enable a custom collector

Setup differs depending on how your organization authenticates with Claude.

**Important:** When a custom endpoint is configured, telemetry goes exclusively to your collector. Spans aren't dual-sent to Anthropic.

### Claude Enterprise (OAuth) organizations

An organization administrator sets the collector endpoint in the Claude.ai admin console under **[Organization settings > Office agents](https://claude.ai/admin-settings/office-agents)**. The setting applies organization-wide.

| **Setting**     | **Description**                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------- |
| `otlp_endpoint` | Base URL of your OTLP collector. The add-in appends /v1/traces. HTTPS strongly recommended.    |
| `otlp_headers`  | Optional authentication headers, formatted per the OpenTelemetry spec: key1=value1,key2=value2 |

The protocol must be HTTP-based OTLP. gRPC is rejected at configuration time.

### Direct provider deployments (Amazon Bedrock, Google Vertex AI, gateway)

For deployments that authenticate against your own model provider rather than Claude.ai, the collector endpoint is supplied through one of three configuration channels. All three use the same two keys.

**Recommended:** Use the **[claude-in-office plugin](https://github.com/anthropics/financial-services-plugins/tree/main/claude-in-office)** for Claude Code. It walks you through generating the manifest, registering Entra extension attributes, and standing up a bootstrap endpoint with `otlp_endpoint` and `otlp_headers` pre-wired. The three channels below are documented for reference and manual setup.

| **Key**         | **Format**              | **Description**                                                                                                       |
| --------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `otlp_endpoint` | HTTPS URL               | Base URL of your OTLP collector. The add-in strips any trailing slash and appends /v1/traces.                         |
| `otlp_headers`  | key1=value1,key2=value2 | Optional authentication headers. Same format as the OpenTelemetry OTEL\_EXPORTER\_OTLP\_HEADERS environment variable. |

If `otlp_endpoint` is unset or empty, no custom collector is configured and the add-in falls back to default behavior.

**Note:** These configuration channels apply to Microsoft Office deployments only. Google Workspace add-ins are configured separately.

**Channel 1: Manifest URL parameter**

Append the keys as query string parameters to the taskpane URL in your custom add-in manifest:

<https://<addin-host>/taskpane.html?otlp_endpoint=https://otel-collector.your-domain.com&otlp_headers=Authorization=Bearer%20<token>`>`

URL-encode the values. This applies the configuration to every user who installs the manifest.

**Channel 2: Azure Entra ID directory extension**

For per-user configuration, register the keys as Entra ID directory extension attributes and assign them via Microsoft Graph. The add-in reads them from the user's ID token using Nested App Authentication (NAA).

The claim names in the issued ID token follow Azure's directory extension format:

| **Claim**            | **Maps to**    |
| -------------------- | -------------- |
| `extn.otlp_endpoint` | otlp\_endpoint |
| `extn.otlp_headers`  | otlp\_headers  |

Set these per-user with a Graph PATCH against the user object. Azure encodes directory extension values as single-element arrays in the ID token; the add-in unwraps them automatically. This channel requires `entra_sso=1` in the manifest URL parameters to enable NAA token acquisition.

**Channel 3: Bootstrap endpoint response**

If your deployment uses a bootstrap endpoint (a JSON endpoint your organization hosts that the add-in calls at startup), include the keys in the response body:

```
{
  "otlp_endpoint": "https://otel-collector.your-domain.com",
  "otlp_headers": "Authorization=Bearer <token>"
}
```

The bootstrap endpoint URL itself is configured via `bootstrap_url` in either the manifest URL parameters or an Entra `extn.bootstrap_url` claim. If an Entra ID token was acquired, it is passed to the bootstrap endpoint as a Bearer authorization header so your endpoint can authenticate the user before returning per-user configuration.

**Precedence**

When multiple channels supply a value, later channels override earlier ones: manifest parameters are read first, then Entra claims, then the bootstrap response. The bootstrap response wins.

If you haven't already, the fastest path is the **[claude-in-office plugin](https://github.com/anthropics/financial-services-plugins/tree/main/claude-in-office)**.

---

## Deployment modes

Custom collector export is available on both deployment modes:

- Claude.ai Enterprise (OAuth): full audit trail including user identity (`user.email`, `user.account_uuid`, `organization.id`), MCP server metadata, and file upload records.

- Direct provider (Bedrock, Vertex AI, gateway): core audit trail (prompts, tool inputs and outputs, document URLs) but no user identity, no MCP metadata, and no file upload spans. User attribution requires correlating `session.id` against your own identity provider logs.

The core audit payload is identical in both modes. Direct provider deployments lack Claude.ai account context, so attributes derived from the Claude.ai user or organization profile are absent. See the `[claude.ai-only]` tags in the span schema below for the complete list.

## Surface and vendor labels

Every span includes two labels identifying which Office application and platform generated it. Use these as your primary dimensions for filtering and dashboards.

| **Label**       | **Values**                                                    |
| --------------- | ------------------------------------------------------------- |
| `agent.surface` | sheet (Excel), doc (Word), slide (PowerPoint), mail (Outlook) |
| `agent.vendor`  | m (Microsoft)                                                 |

---

## Span reference

Each user turn produces a parent/child tree of up to five span types. Attributes marked [content] carry user-generated data; these form your audit payload. Attributes marked [`claude.ai-only`] are populated only when the user signs in with a Claude account; they are absent on Bedrock, Vertex AI, and gateway deployments. Absent attributes are omitted from the span entirely (no key with a null value).

The `file.upload` span and all `mcp.*` attributes are also [`claude.ai-only`], since file upload and MCP server connections are Claude platform features.

For direct provider deployments, user identity should be correlated via `session.id` and `document.url`, joined against your identity provider's session logs.

### Resource attributes

These attributes appear on every span:

| **Attribute**     | **Description**           |
| ----------------- | ------------------------- |
| `service.name`    | Fixed value: office-agent |
| `service.version` | Fixed value: 1.0.0        |
| `git.sha`         | Build commit identifier   |

### agent.query (root span)

One span per user turn. This is the root of the span tree and carries session identity, document context, and MCP server status. SpanKind: INTERNAL.

| **Attribute**                                 | **Description**                                                    |
| --------------------------------------------- | ------------------------------------------------------------------ |
| `agent.surface`                               | sheet \| doc \| slide \| mail                                      |
| `agent.vendor`                                | m                                                                  |
| `user.message [content]`                      | The user's prompt (first 4000 characters)                          |
| `session.id`                                  | Opaque session identifier                                          |
| `user.email [claude.ai-only]`                 | User's email address                                               |
| `user.bucket [claude.ai-only]`                | Deterministic hash bucket (SHA-256 of email, mod 30)               |
| `user.account_uuid [claude.ai-only]`          | Claude account UUID                                                |
| `document.url [content]`                      | URL of the open Office document                                    |
| `organization.id [claude.ai-only]`            | Claude organization UUID                                           |
| `org.rate_limit_tier [claude.ai-only]`        | Claude subscription tier                                           |
| `org.type [claude.ai-only]`                   | Claude organization type                                           |
| `agent.selected_model`                        | Model selected by the user for this session                        |
| `office.platform`                             | PC \| Mac \| OfficeOnline \| iOS \| Android \| Universal           |
| `office.version`                              | Office build number                                                |
| `mcp.configured_count [claude.ai-only]`       | Number of MCP servers configured                                   |
| `mcp.connected_count [claude.ai-only]`        | Number of MCP servers successfully connected                       |
| `mcp.failed_count [claude.ai-only]`           | Number of MCP servers that failed to connect                       |
| `mcp.fetch_status [claude.ai-only]`           | success \| error \| timeout \| no\_auth \| not\_attempted          |
| `mcp.fetch_duration_ms [claude.ai-only]`      | MCP registry fetch duration                                        |
| `mcp.fetch_http_status [claude.ai-only]`      | MCP registry fetch HTTP status code                                |
| `mcp.servers [content] [claude.ai-only]`      | Serialized MCP server details (names, tool counts, error messages) |
| `file.upload.count [claude.ai-only]`          | Number of files attached to this turn                              |
| `file.upload.total_bytes [claude.ai-only]`    | Total bytes uploaded                                               |
| `file.upload.image_count [claude.ai-only]`    | Number of image attachments                                        |
| `file.upload.document_count [claude.ai-only]` | Number of document attachments                                     |
| `file.upload.other_count [claude.ai-only]`    | Number of other attachments                                        |
| `error.name`                                  | Exception class name (present on failure)                          |
| `agent.query_phase`                           | Phase at which the query failed (present on failure)               |

### agent.stream

One span per API call to Claude, as a child of the query span. SpanKind: CLIENT.

| **Attribute**           | **Description**                                                 |
| ----------------------- | --------------------------------------------------------------- |
| `model`                 | Model ID used for this call                                     |
| `max_tokens`            | Maximum output tokens requested                                 |
| `agent.message_count`   | Number of messages in the conversation at stream start          |
| `input_tokens`          | Input tokens billed (from API response)                         |
| `output_tokens`         | Output tokens billed (from API response)                        |
| `cache_read_tokens`     | Tokens served from prompt cache                                 |
| `cache_creation_tokens` | Tokens written to prompt cache                                  |
| `stop_reason`           | end\_turn \| tool\_use \| max\_tokens \| etc.                   |
| `request_id`            | Anthropic API request-id header, usable for support correlation |

**Note on prompt caching:** The add-in requests prompt caching unconditionally. The `cache_read_tokens` and `cache_creation_tokens` attributes are set from the provider's API response and are omitted when the response doesn't include them. Prompt caching is available for Claude Platform; as of this writing, Amazon Bedrock and Google Vertex AI don't yet return these fields through the client the add-in uses. When support lands on your provider, these attributes will begin appearing automatically.

### agent.tool_execution

One span per tool call, as a child of the stream span. SpanKind: INTERNAL. This is the primary record of what actions the model took against the document.

| **Attribute**           | **Description**                                                                 |
| ----------------------- | ------------------------------------------------------------------------------- |
| `tool_name`             | Tool identifier (e.g. get\_cell\_ranges, execute\_office\_js, edit\_slide\_xml) |
| `tool.id`               | Unique ID of this tool invocation                                               |
| `tool.caller`           | server \| client                                                                |
| `tool.owner`            | first\_party \| mcp \| server                                                   |
| `tool.read_write`       | read \| write \| read\_write                                                    |
| `tool.accept_decision`  | manual \| auto\_accept \| deferred                                              |
| `tool.input [content]`  | Serialized tool input (first 4000 characters)                                   |
| `tool.success`          | Boolean                                                                         |
| `tool.output [content]` | Serialized tool output (first 4000 characters)                                  |
| `tool.output_chars`     | Full output length in characters (use to detect truncation)                     |
| `tool.error_type`       | Error classification (present on failure)                                       |
| `sheet.cells_read`      | Cells read (sheet surface only)                                                 |
| `sheet.cells_written`   | Cells written (sheet surface only)                                              |
| `sheet.cells_copied`    | Cells copied (sheet surface only)                                               |

**Note:** The `tool.accept_decision` attribute records how the permission decision was made: `manual` (the user approved this specific action), `auto_accept` (the user had previously granted standing approval), or `deferred` (the action was queued for later review). Use this to audit approval patterns across your organization.

### agent.compaction

One span per conversation auto-summarization, fired when context approaches the window limit. SpanKind: CLIENT.

| **Attribute**             | **Description**                  |
| ------------------------- | -------------------------------- |
| `compaction.pre_tokens`   | Token count before summarization |
| `compaction.post_tokens`  | Token count after summarization  |
| `compaction.tokens_saved` | Delta                            |
| `compaction.success`      | Boolean                          |
| `compaction.trigger`      | Currently always reactive        |

This span also carries `agent.surface`, `agent.vendor`, `session.id`, `user.email [claude.ai-only]`, `user.bucket [claude.ai-only]`, `office.platform`, and `office.version`, duplicated from the root span so you can query compaction events independently.

### file.upload [claude.ai-only]

One span per individual file upload, as a child of the query span. SpanKind: CLIENT. This span type only appears when users sign in with a Claude.ai account. File upload isn't available on direct provider deployments.

| **Attribute**                    | **Description**                |
| -------------------------------- | ------------------------------ |
| `file.upload.filename [content]` | Original filename              |
| `file.upload.size_bytes`         | File size                      |
| `file.upload.mime_type`          | MIME type                      |
| `file.upload.file_id`            | Anthropic Files API identifier |
| `file.upload.success`            | Boolean                        |

---

## Span events

Span events are timestamped markers attached to the spans above. They capture lifecycle transitions and counter-equivalent signals.

- `agent.query`: exception {exception.type}; file_upload {file_id, mime_type, content_category}

- `agent.stream`: first_token; stream_complete; stream_error {exception.type}

- `agent.tool_execution`: tool_init; tool_run; tool_result; tool_error {error_type}

- `agent.compaction`: compaction_start; compaction_complete; compaction_error {exception.type}

- `file.upload`: exception {exception.type}

Every internal product counter also records a span event with the same name on the currently active span, providing the equivalent of the metrics stream within your trace data. The `office_agent.token.usage` event is emitted on each `agent.stream` span, once per non-zero token type, with attributes {token_usage.type: input | output | cacheRead | cacheCreation, token_usage.model, token_usage.token_count}. This mirrors the `*.token.usage` counter shape emitted by other Anthropic products, so a single collector can aggregate token cost across products by grouping on `service.name`.

---

## Surface-specific behavior

The telemetry schema is consistent across all surfaces. These are the differences:

- Sheets (Excel): `agent.tool_execution` spans include `sheet.cells_read`, `sheet.cells_written`, and `sheet.cells_copied` attributes. `office_agent.cell_edit_collision_total` span events appear when a user is mid-cell-edit while a tool tries to write.

- Documents (Word): document-edit funnel events track the edit lifecycle: `office_agent.doc_edit_received_total`, `office_agent.doc_edit_parsed_total`, `office_agent.doc_edit_applied_total`, `office_agent.doc_proposed_edit_reviewed_total`. No `sheet.cells_*` attributes.

- Slides (PowerPoint): no surface-specific attributes or events beyond the common schema.

- Mail (Outlook): no surface-specific attributes or events beyond the common schema.

---

## Reconstructing a user session

### Claude.ai deployments

- Filter spans by `user.email` (or `user.account_uuid`) and `session.id`.

- Order `agent.query` spans by start timestamp; each is one user turn.

- For each turn, `user.message` is the prompt and `document.url` is the file being worked on.

- Child `agent.tool_execution` spans, ordered by timestamp, are the actions taken: `tool.input` is what was attempted, `tool.output` is the result, `tool.accept_decision` records whether the user explicitly approved.

### Direct provider deployments

The add-in has no Claude.ai user identity in this mode, so spans carry no `user.email` or `user.account_uuid`. To attribute activity to a user:

- Filter spans by `session.id` to isolate one continuous add-in session.

- Use `document.url` to identify the file being worked on.

- Correlate the session against your identity provider's logs: Entra sign-in events, gateway access logs, or your bootstrap endpoint's request log (which receives the user's Entra ID token as a Bearer header).

- Once a session is attributed to a user, the per-turn reconstruction is identical: agent.query spans ordered by timestamp, with `user.message`, `tool.input`, `tool.output`, and `tool.accept_decision` providing the audit trail.

This produces a complete, ordered transcript of the interaction in both deployment modes.