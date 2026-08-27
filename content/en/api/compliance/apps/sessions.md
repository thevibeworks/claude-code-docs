# Sessions

## Sessions › Local

### List local sessions

**GET** `/v1/compliance/apps/sessions/local`

List local sessions across the organizations the key may read.

Results are ordered by `created_at` descending. Pagination is
forward-only via `next_page`; there is no reverse cursor.

#### Query parameters

- `created_at: optional object`

  - `gte: optional string`

    Only return sessions whose first inference call is at or after this time (RFC 3339; a UTC offset is required).

    format: date-time

  - `lt: optional string`

    Only return sessions whose first inference call is strictly before this time (RFC 3339; a UTC offset is required).

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 500)

  default: 100, maximum: 500, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gte: optional string`

    Only return sessions whose last inference call is at or after this time (RFC 3339; a UTC offset is required). Combines with `created_at.gte` / `created_at.lt`; the ordering and pagination are unchanged. Use it to poll for sessions that have been active since a previous pass — a session that becomes active later can only enter the result, never leave it.

    format: date-time

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Page of local sessions, ordered by `created_at` descending; ties are broken by a fixed server-side order. `updated_at` never participates in the ordering; the `updated_at.gte` query parameter filters on it without changing the order or the pagination cursor.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

    format: date-time

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    default: compliance_local_session

  - `updated_at: string`

    Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

    format: date-time

  - `user: object`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z",
      "updated_at": "2026-07-09T15:47:33Z"
    }
  ]
}
```

### Retrieve a local session

**GET** `/v1/compliance/apps/sessions/local/{local_session_id}`

Retrieve one local session.

The response is the same session object the list endpoint returns,
with `user.email_address` resolved the same way. Retention is
enforced when the response is served: a session whose every
inference call has aged out returns 404.

#### Path parameters

- `local_session_id: string`

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

- `created_at: string`

  Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  format: date-time

- `organization_uuid: string`

  UUID of the child organization the session belongs to

- `product_surface: string or null`

  The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

- `type: "compliance_local_session"`

  default: compliance_local_session

- `updated_at: string`

  Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

  format: date-time

- `user: object`

  The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

  - `id: string`

    User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

  - `email_address: string or null`

    User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

- `workspace_id: string or null`

  Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "type": "compliance_local_session",
  "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
  "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
  "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
  "user": {
    "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
    "email_address": "engineer@example.com"
  },
  "product_surface": "cowork",
  "created_at": "2026-07-09T14:02:11Z",
  "updated_at": "2026-07-09T15:47:33Z"
}
```

## Sessions › Local › Messages

### Retrieve local session messages

**GET** `/v1/compliance/apps/sessions/local/{local_session_id}/messages`

Read one local session's transcript, oldest-first by default.

Retention is enforced read-side: turns at or before the child
organization's retention boundary are never returned; a session
that straddles the boundary carries one leading
`content_unavailable` placeholder (`reason: "retention_elapsed"`)
in their place. The boundary is pinned on the walk's first page and
honored for 24 hours: a cursor older than that is rejected with an
explicit 400; restart the walk to read under the current boundary.

#### Path parameters

- `local_session_id: string`

#### Query parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, maximum: 1000, minimum: 1

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first, default) or `desc`.

  default: asc

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

  default: 10000, maximum: 2147483647, minimum: -1

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

  default: 10000, maximum: 2147483647, minimum: -1

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Transcript turns for this page, in call order: oldest call first by default, newest call first with `order=desc`. The messages of one call carry the call's timestamp and follow each other in transcript order; a page boundary can fall between them.

  - `id: string`

    Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.

  - `content: array of object or object or object`

    Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

    - `Text object`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

        default: false

      - `type: "text"`

        default: text

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

        default: false

      - `type: "tool_use"`

        default: tool_use

    - `ToolResult object`

      Result returned by a tool invocation.

      - `content: array of object`

        Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          default: text

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

        default: false

      - `type: "tool_result"`

        default: tool_result

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

    format: date-time

  - `model: string or null`

    The model that served this assistant turn, as reported in the `model` field of the underlying Messages API response. Null on user messages and on any assistant message whose `provenance` is set: client-asserted history and synthetic markers were not produced by a model during this session, and for unavailable content the serving model is not known.

  - `provenance: object or object or object or null`

    Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

    - `ContentUnavailable object`

      The turn's content cannot be returned; `content` is empty.

      - `reason: string`

        Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `client_aborted` (the client closed the connection or cancelled the request before the response completed, so the response was not captured for this turn; any partial output already streamed to the client is not included; assistant-role turns only), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.

      - `type: "content_unavailable"`

        default: content_unavailable

    - `ClientAsserted object`

      Assistant content the client supplied as conversation history
      rather than produced by Claude during this session. `content` shows
      what the model received but its authorship is not verified; this can
      result from normal request or client processing, not only client
      modification. Never on user-role messages.

      - `type: "client_asserted"`

        default: client_asserted

    - `SyntheticMarker object`

      A transcript marker generated by the endpoint rather than sent by
      either party during the session. Marker messages indicate that the
      prompt history diverged from what was captured, that the request's
      `system` field was present but is not shown, or that
      prompt-carried history was suppressed because the session spans the
      child organization's retention boundary and those turns cannot be
      placed against it (the marker's text names the cause). Markers that
      report a mismatch with captured history can result from normal request
      or client processing, not only client modification.

      - `type: "synthetic_marker"`

        default: synthetic_marker

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `type: "compliance_local_session_message"`

    default: compliance_local_session_message

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

- `session: object`

  The local session the messages belong to. `user.email_address` is always null on this endpoint; the messages endpoint does not resolve email addresses.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

    format: date-time

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    default: compliance_local_session

  - `updated_at: string`

    Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

    format: date-time

  - `user: object`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "clsm_eyJ2IjoxLCJsIjoi…",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "created_at": "2025-03-12T18:22:41.123456Z",
      "model": "claude-opus-5",
      "provenance": {
        "reason": "not_captured",
        "type": "content_unavailable"
      },
      "role": "assistant",
      "type": "compliance_local_session_message"
    }
  ],
  "next_page": "page_eyJ2IjoxLCJmIjoibSIs…",
  "session": {
    "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
    "created_at": "2025-03-12T18:22:41.123456Z",
    "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
    "product_surface": "cowork",
    "type": "compliance_local_session",
    "updated_at": "2025-03-12T18:22:41.123456Z",
    "user": {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "email_address": "jane.doe@example.com"
    },
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR"
  }
}
```

## Sessions › Remote

### List remote sessions

**GET** `/v1/compliance/apps/sessions/remote`

List remote sessions (Cowork sessions that run in Anthropic-managed
cloud environments) across the organizations the key may read.

Each entry carries session metadata only; retrieve a session's
transcript from the messages endpoint. By default the list spans every
such organization; pass up to 500 `organization_ids[]` values to
narrow it. Pass 1 to 10 `user_ids[]` values to scope the
list to specific users: that filter matches the session's owning user,
so agent-owned sessions are excluded whenever it is set. Bound results
in time with the `created_at` range parameters (`created_at.gte`,
`created_at.gt`, `created_at.lt`, `created_at.lte`; RFC 3339). There
is no `updated_at` filter.

Results are sorted newest first by `created_at`, with at most `limit`
sessions per page (default 100, maximum 500). Pagination is
forward-only: pass the response's `next_page` value back as `page` to
retrieve the next page, and stop when `next_page` is null.

#### Query parameters

- `created_at: optional object`

  - `gt: optional string`

    Filter remote sessions created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter remote sessions created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter remote sessions created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter remote sessions created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 500)

  default: 100, maximum: 500, minimum: 1

- `organization_ids: optional array of string`

  Filter to specific child organization identifiers. Omit to enumerate every child organization the key may read.

  maxItems: 500

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter to sessions owned by specific users (max 10 per request). Agent-owned sessions are excluded when this filter is set.

  maxItems: 10

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

    format: date-time

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

    format: date-time

  - `user: object or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "cse_01A0000000000000000000000",
      "organization_uuid": "00000000-0000-0000-0000-000000000000",
      "user": {
        "id": "user_01A0000000000000000000000",
        "email_address": "user@example.com"
      },
      "status": "active",
      "created_at": "2026-01-02T03:04:05.000000Z",
      "updated_at": "2026-01-02T03:04:05.000000Z",
      "product_surface": "cowork_remote",
      "claude_project_id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH"
    }
  ],
  "next_page": "page_AAE..."
}
```

## Sessions › Remote › Messages

### Retrieve remote session messages

**GET** `/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages`

Retrieve one remote session's transcript: user prompts, assistant
responses, and tool calls and results. Thinking blocks and images are
not included.

Messages are returned oldest first by default; pass `order=desc` to
reverse. Pagination uses the same `page`/`next_page` scheme as the
list endpoint, with at most `limit` messages per page (default 100,
maximum 1000); keep paginating until `next_page` is null.
`tool_use_input_max_bytes` and `tool_result_max_bytes` cap how many
bytes of each tool-use input and each tool-result text item are
returned; a block shortened by either cap carries `truncated: true`.

The response embeds the session's metadata under `session` alongside
the paginated `data` array. On this endpoint `session.user.email_address`
and `session.started_by_user` are always null; read them from the list
endpoint instead.

Returns 404 while the session is still `pending`, for deleted sessions,
and for sessions outside the organizations the key may read. A
malformed session identifier returns 400.

#### Path parameters

- `claude_remote_session_id: string`

  The remote session identifier (`cse_...`) to retrieve

#### Query parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, maximum: 1000, minimum: 1

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first) or `desc`.

  default: asc

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum. `0` is not a valid value.

  default: 10000, maximum: 2147483647, minimum: -1

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum. `0` is not a valid value.

  default: 10000, maximum: 2147483647, minimum: -1

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Transcript turns for this page, ordered by transcript position. `created_at` is a commit timestamp and may tie or invert under concurrent writes; do not re-sort by it.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of object or object or object`

    Content blocks within the message

    - `Text object`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

        default: false

      - `type: "text"`

        default: text

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

        default: false

      - `type: "tool_use"`

        default: tool_use

    - `ToolResult object`

      Result returned by a tool invocation.

      - `content: array of object`

        Text content returned by the tool. Non-text item types are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          default: text

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

        default: false

      - `type: "tool_result"`

        default: tool_result

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

    default: false

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

    format: date-time

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

- `session: object`

  Session metadata. `started_by_user`, `user.email_address`, and `claude_project_id` are always null on this endpoint; the messages endpoint resolves neither email addresses nor project bindings.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

    format: date-time

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

    format: date-time

  - `user: object or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote/$CLAUDE_REMOTE_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "content_unavailable": true,
      "created_at": "2019-12-27T18:11:19.117Z",
      "role": "assistant",
      "sent_by_user_id": "sent_by_user_id"
    }
  ],
  "next_page": "next_page",
  "session": {
    "id": "id",
    "agent_id": "agent_id",
    "claude_project_id": "claude_project_id",
    "created_at": "2019-12-27T18:11:19.117Z",
    "organization_uuid": "organization_uuid",
    "product_surface": "product_surface",
    "started_by_user": {
      "id": "id",
      "email_address": "email_address"
    },
    "status": "status",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "user": {
      "id": "id",
      "email_address": "email_address"
    }
  }
}
```
