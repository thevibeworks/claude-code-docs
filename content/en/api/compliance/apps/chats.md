# Chats

## List chats

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

### Query parameters

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

### Headers

- `"x-api-key": optional string`

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

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

## Delete chat

**DELETE** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

### Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Headers

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude chat that was deleted

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  default: claude_chat_deleted

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

## Domain types

### Chat List Response

- `ChatListResponse object`

  Chat metadata for listing chats (without messages).

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

### Chat Delete Response

- `ChatDeleteResponse object`

  Response for deleting a Claude chat.

  - `id: string`

    The ID of the Claude chat that was deleted

  - `type: optional "claude_chat_deleted"`

    Constant string confirming deletion

    default: claude_chat_deleted

## Chats › Messages

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

## Chats › Files

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

## Chats › Generated Files

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
