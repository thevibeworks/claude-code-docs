# Apps

## Apps › Chats

### List chats

**GET** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by the `order_by` key, with ties broken by id.

**Deprecation notice:** Combining `user_ids[]` with any `updated_at.*`
filter is deprecated and will be rejected with HTTP 400 after
2026-09-22. For incremental polling by update time, omit `user_ids[]`
and set `order_by=updated_at` with `after_id` cursor pagination —
this returns the same chats across the whole organization in a single
request stream. For per-user listing, use `created_at.*` filters (or
no time filter) with the default `order_by`. `user_ids[]` with
`order_by=updated_at` is already rejected.

#### Query parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, maximum: 1000, minimum: 1

- `order_by: optional "created_at" or "updated_at"`

  Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids[]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

  default: created_at

  - `"created_at"`

  - `"updated_at"`

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids[]; not supported for org-wide queries.

- `updated_at: optional object`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

- `user_ids: optional array of string`

  Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`. Deprecated combination: passing `user_ids[]` together with any `updated_at.*` filter is deprecated and will be rejected after 2026-09-22. For `updated_at`-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

  maxItems: 10

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Deletion timestamp if deleted

    format: date-time

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string or null`

    Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string or null`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

    format: date-time

  - `user: object or null`

    User information for compliance responses.

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization ID this chat belongs to

- `first_id: string or null`

  Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string or null`

  Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-5",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9",
  "last_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9"
}
```

### Delete chat

**DELETE** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

#### Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the Claude chat that was deleted

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  default: claude_chat_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

## Apps › Chats › Messages

### Get chat messages

**GET** `/v1/compliance/apps/chats/{claude_chat_id}/messages`

Retrieves message history and file metadata for a specific chat.

#### Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

#### Query parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object`

  - `gt: optional string`

    Filter messages created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter messages created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter messages created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter messages created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

  maximum: 1000, minimum: 1

- `order: optional "asc" or "desc"`

  Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

  default: asc

  - `"asc"`

  - `"desc"`

- `tool_result_max_chars: optional number`

  Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

  default: 10000, minimum: -1

- `tool_use_input_max_chars: optional number`

  Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

  default: 10000, minimum: -1

- `updated_at: optional object`

  - `gt: optional string`

    Filter messages updated after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter messages updated at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter messages updated before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter messages updated at or before this time (RFC 3339 format)

    format: date-time

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Chat ID

- `chat_messages: array of object`

  Array of chat messages in order of created_at

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object or null`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string or null`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string or null`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object or object or object`

    Content blocks within the message

    - `Text object`

      Text content block.

      - `text: string`

        Text content from human or assistant

      - `thinking_redacted: boolean`

        True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

        default: false

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

        default: false

      - `type: "text"`

        default: text

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `integration_name: string or null`

        Name of the integration that provides this tool, when applicable

      - `mcp_server_url: string or null`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass the endpoint's tool-use input max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

        default: false

      - `type: "tool_use"`

        default: tool_use

    - `ToolResult object`

      Result returned by a tool invocation.

      - `content: array of object`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          default: text

      - `integration_name: string or null`

        Name of the integration that provides this tool, when applicable

      - `is_error: boolean`

        True when the tool reported an error

      - `mcp_server_url: string or null`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass the endpoint's tool-result max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

        default: false

      - `type: "tool_result"`

        default: tool_result

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

    format: date-time

  - `files: array of object or null`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `created_at: string`

      File creation timestamp

      format: date-time

    - `filename: string`

      Display name of the file

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.

  - `generated_files: array of object or null`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `md5: string or null`

      Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type reported by the tool that produced the file

    - `size_bytes: number or null`

      Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

- `created_at: string`

  Creation timestamp

  format: date-time

- `deleted_at: string or null`

  Deletion timestamp if deleted

  format: date-time

- `first_id: string or null`

  Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

  default: false

- `href: string`

  URL to view this chat in claude.ai

- `last_id: string or null`

  Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `model: string or null`

  Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

- `name: string`

  Chat name

- `organization_uuid: string`

  Organization UUID this chat belongs to

- `project_id: string or null`

  Project ID this chat belongs to

- `updated_at: string`

  Last update timestamp

  format: date-time

- `user: object or null`

  User information for compliance responses.

  - `id: string`

    User identifier

  - `email_address: string`

    User's email address

- `organization_id: string`

  **Deprecated**

  Organization ID this chat belongs to

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-5",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

## Apps › Chats › Files

### Get file metadata

**GET** `/v1/compliance/apps/chats/files/{claude_file_id}`

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  File ID

- `claude_chat_ids: array of string`

  Chats this file is attached to. A file can be referenced by messages across multiple chats.

- `created_at: string`

  File creation timestamp

  format: date-time

- `filename: string or null`

  Display name of the file, if set

- `md5: string or null`

  Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

- `message_ids: array of string`

  Chat message IDs this file is attached to. A file can be referenced by multiple messages.

- `mime_type: string or null`

  MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

- `size_bytes: number or null`

  Size in bytes of the file's preferred downloadable variant, if known

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ],
  "claude_chat_ids": [
    "claude_chat_def456"
  ]
}
```

### Delete file

**DELETE** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the file that was deleted

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  default: claude_file_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

### Download file content

**GET** `/v1/compliance/apps/chats/files/{claude_file_id}/content`

Downloads the binary content of a file referenced in chat messages.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Apps › Chats › Generated Files

### Get Claude-generated file metadata

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}`

Returns metadata for a file the assistant created via tool use.

Use the sibling `/content` endpoint to download the bytes.

#### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

- `claude_chat_id: string`

  The chat this generated file belongs to

- `created_at: string or null`

  File creation timestamp, when available

  format: date-time

- `filename: string`

  Display name of the generated file

- `md5: string or null`

  Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

- `mime_type: string or null`

  MIME type of the stored file, when available

- `size_bytes: number or null`

  Size in bytes of the stored file, when available

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

### Download a Claude-generated file

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

#### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Apps › Projects

### List projects

**GET** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

#### Query parameters

- `created_at: optional object`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gt: optional string`

    Filter projects updated after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects updated at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects updated before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects updated at or before this time (RFC 3339 format)

    format: date-time

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

    format: date-time

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

    format: date-time

  - `user: object or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

### Get project details

**GET** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

  format: date-time

- `deleted_at: string or null`

  Timestamp when the project was deleted by an end user, or null otherwise

  format: date-time

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

  format: date-time

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

- `organization_id: string`

  **Deprecated**

  Organization identifier (tagged ID)

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Delete project

**DELETE** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  default: claude_project_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

## Apps › Projects › Attachments

### List project attachments

**GET** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object or object`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference object`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `mime_type: string`

      MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `type: "project_file"`

      Discriminator marking this as a binary file

      default: project_file

  - `ComplianceProjectDocReference object`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      default: text/plain

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      default: project_doc

    - `updated_at: string or null`

      Last-modified timestamp of the document. Reserved for future use — currently always null.

      format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Apps › Projects › Collaborators

### List project collaborators

**GET** `/v1/compliance/apps/projects/{project_id}/collaborators`

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object or object or object or object`

  List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

  - `ComplianceProjectUserCollaborator object`

    An individual user granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      default: user

    - `user_id: string or null`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object`

    An RBAC group granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "group"`

      Discriminator marking this as a group collaborator

      default: group

  - `ComplianceProjectOrganizationCollaborator object`

    An entire organization granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      default: organization

  - `ComplianceProjectOrganizationRoleCollaborator object`

    All holders of an organization-level role granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      default: organization_role

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Apps › Projects › Documents

### Get project document content

**GET** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Get project document metadata

**GET** `/v1/compliance/apps/projects/documents/{document_id}/metadata`

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `claude_project_id: string`

  The project this document belongs to

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `md5: string`

  Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

- `mime_type: "text/plain"`

  MIME type of the document content, always plain text

  default: text/plain

- `size_bytes: number`

  Size in bytes of the document content (UTF-8 encoded)

- `user: object or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Delete project document

**DELETE** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the project document that was deleted

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  default: claude_project_document_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

## Apps › Artifacts

### Get artifact metadata

**GET** `/v1/compliance/apps/artifacts/{artifact_version_id}`

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

#### Path parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Artifact ID e.g. 'claude_artifact_abc123'

- `artifact_type: string or null`

  MIME-like artifact type e.g. 'application/vnd.ant.code'

- `claude_chat_id: string`

  The chat this artifact belongs to

- `created_at: string`

  Artifact version creation timestamp

  format: date-time

- `md5: string`

  Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

- `size_bytes: number`

  Size in bytes of the artifact content (UTF-8 encoded)

- `title: string or null`

  Artifact title

- `version_id: string`

  Artifact version ID e.g. 'claude_artifact_version_abc123'

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```

### Download artifact content

**GET** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

#### Path parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Apps › Sessions › Local

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

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

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

  The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

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

## Apps › Sessions › Local › Messages

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

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

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

## Apps › Sessions › Remote

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

## Apps › Sessions › Remote › Messages

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
