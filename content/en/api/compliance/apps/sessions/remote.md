---
title: Remote
url: https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote
---

# Remote

## List remote sessions

**get** `/v1/compliance/apps/sessions/remote`

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

### Query Parameters

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter remote sessions created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter remote sessions created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter remote sessions created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter remote sessions created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 500)

- `organization_ids: optional array of string`

  Filter to specific child organization identifiers. Omit to enumerate every child organization the key may read.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter to sessions owned by specific users (max 10 per request). Agent-owned sessions are excluded when this filter is set.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, agent_id, claude_project_id, 7 more }`

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Remote List Response

- `RemoteListResponse object { id, agent_id, claude_project_id, 7 more }`

  Metadata for one remote session, as returned in the list response
  and in the messages response's `session` field.

  Carries session attributes only, not transcript content. Use the
  messages endpoint to retrieve a session's transcript.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

# Messages

## Retrieve remote session messages

**get** `/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages`

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

### Path Parameters

- `claude_remote_session_id: string`

  The remote session identifier (`cse_...`) to retrieve

### Query Parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first) or `desc`.

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum. `0` is not a valid value.

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum. `0` is not a valid value.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, content, content_unavailable, 3 more }`

  Transcript turns for this page, ordered by transcript position. `created_at` is a commit timestamp and may tie or invert under concurrent writes; do not re-sort by it.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

- `session: object { id, agent_id, claude_project_id, 7 more }`

  Session metadata. `started_by_user`, `user.email_address`, and `claude_project_id` are always null on this endpoint; the messages endpoint resolves neither email addresses nor project bindings.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote/$CLAUDE_REMOTE_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Message List Response

- `MessageListResponse object { id, content, content_unavailable, 3 more }`

  A single user or assistant turn in a remote session transcript.

  `content` is a discriminated union of `text`, `tool_use`, and
  `tool_result` blocks.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.
