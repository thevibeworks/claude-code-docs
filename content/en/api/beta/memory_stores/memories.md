---
title: Memories
url: https://platform.claude.com/docs/en/api/beta/memory_stores/memories
---

# Memories

## Create a Memory

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to create the memory in (`memstore_...`).

### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Body parameters

- `content: string or null`

  The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

  The maximum size is 100 kB (102,400 bytes).

- `path: string`

  The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

  A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

  minLength: 2, maxLength: 1024

### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "content": "content",
          "path": "xx"
        }'
```

#### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## List Memories

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to list memories from (`memstore_...`).

### Query parameters

- `depth: optional number`

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

  format: int32

- `limit: optional number`

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

  format: int32

- `page: optional string`

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `path_prefix: optional string`

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `view: optional BetaManagedAgentsMemoryView`

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `data: optional array of BetaManagedAgentsMemoryListItem`

  One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

  - `BetaManagedAgentsMemory object`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

    - `type: "memory"`

    - `id: string`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `created_at: string`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `updated_at: string`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `content: optional string or null`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix object`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=http) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `type: "memory_prefix"`

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

- `next_page: optional string or null`

  The value to pass as `page` to get the next page, or `null` if there are no more results.

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "mem_011CZkZ9X2dpNyB6YbtxvB6e",
      "content_sha256": "ba7936d94c84d948a2232088f78228f175df6a8353b2d5bc9228eee5794a0024",
      "content_size_bytes": 28,
      "created_at": "2026-03-15T10:00:00Z",
      "memory_store_id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "memory_version_id": "memver_011CZkZBJq5dWxk9fVLNcPht",
      "path": "/preferences/formatting.md",
      "type": "memory",
      "updated_at": "2026-03-15T10:00:00Z",
      "content": null
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Retrieve a Memory

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a Memory

### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to retrieve (`mem_...`).

### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Update a Memory

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a Memory

### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to update (`mem_...`).

### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Body parameters

- `content: optional string or null`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: optional string or null`

  The new path of the memory, which renames it. Omit it to keep the current path.

  The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `precondition: optional BetaManagedAgentsPrecondition`

  The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

  If the condition fails, the request fails with HTTP status 409.

  - `type: "content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

## Delete a Memory

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to delete (`mem_...`).

### Query parameters

- `expected_content_sha256: optional string`

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsDeletedMemory object`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=http) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about how long versions are kept.

  - `type: "memory_deleted"`

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain types

### Beta Managed Agents Conflict Error

- `BetaManagedAgentsConflictError object`

  - `type: "conflict_error"`

  - `message: optional string`

### Beta Managed Agents Content Sha256 Precondition

- `BetaManagedAgentsContentSha256Precondition object`

  A precondition that applies an update only if the memory's current content has the hash in `content_sha256`.

  If the hashes differ, the request fails with HTTP status 409. Retrieve the memory and retry. If the memory already has exactly the requested `content` and `path`, the request succeeds even though the hashes differ.

  - `type: "content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `BetaManagedAgentsDeletedMemory object`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=http) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about how long versions are kept.

  - `type: "memory_deleted"`

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

### Beta Managed Agents Error

- `BetaManagedAgentsError = BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 9 more`

  - `BetaInvalidRequestError object`

    - `type: "invalid_request_error"`

      default: invalid_request_error

    - `message: string`

      default: Invalid request

  - `BetaAuthenticationError object`

    - `type: "authentication_error"`

      default: authentication_error

    - `message: string`

      default: Authentication error

  - `BetaBillingError object`

    - `type: "billing_error"`

      default: billing_error

    - `message: string`

      default: Billing error

  - `BetaPermissionError object`

    - `type: "permission_error"`

      default: permission_error

    - `message: string`

      default: Permission denied

  - `BetaNotFoundError object`

    - `type: "not_found_error"`

      default: not_found_error

    - `message: string`

      default: Not found

  - `BetaRateLimitError object`

    - `type: "rate_limit_error"`

      default: rate_limit_error

    - `message: string`

      default: Rate limited

  - `BetaGatewayTimeoutError object`

    - `type: "timeout_error"`

      default: timeout_error

    - `message: string`

      default: Request timeout

  - `BetaAPIError object`

    - `type: "api_error"`

      default: api_error

    - `message: string`

      default: Internal server error

  - `BetaOverloadedError object`

    - `type: "overloaded_error"`

      default: overloaded_error

    - `message: string`

      default: Overloaded

  - `BetaManagedAgentsMemoryPreconditionFailedError object`

    The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

    The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

    - `type: "memory_precondition_failed_error"`

    - `message: optional string`

      A human-readable explanation of why the precondition failed.

  - `BetaManagedAgentsMemoryPathConflictError object`

    The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path.

    Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

    - `type: "memory_path_conflict_error"`

    - `conflicting_memory_id: optional string`

      The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

      Retry the request when it is empty.

    - `conflicting_path: optional string`

      The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

    - `message: optional string`

      A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

  - `BetaManagedAgentsConflictError object`

    - `type: "conflict_error"`

    - `message: optional string`

### Beta Managed Agents Memory

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory or BetaManagedAgentsMemoryPrefix`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=http) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `BetaManagedAgentsMemory object`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

    - `type: "memory"`

    - `id: string`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `created_at: string`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `updated_at: string`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `content: optional string or null`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix object`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=http) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `type: "memory_prefix"`

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Beta Managed Agents Memory Path Conflict Error

- `BetaManagedAgentsMemoryPathConflictError object`

  The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path.

  Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

  - `type: "memory_path_conflict_error"`

  - `conflicting_memory_id: optional string`

    The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

    Retry the request when it is empty.

  - `conflicting_path: optional string`

    The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

  - `message: optional string`

    A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

### Beta Managed Agents Memory Precondition Failed Error

- `BetaManagedAgentsMemoryPreconditionFailedError object`

  The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

  The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

  - `type: "memory_precondition_failed_error"`

  - `message: optional string`

    A human-readable explanation of why the precondition failed.

### Beta Managed Agents Memory Prefix

- `BetaManagedAgentsMemoryPrefix object`

  A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=http) returns instead of the memories below the requested `depth`.

  It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

  - `type: "memory_prefix"`

  - `path: string`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Beta Managed Agents Memory View

- `BetaManagedAgentsMemoryView = "basic" or "full"`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Beta Managed Agents Precondition

- `BetaManagedAgentsPrecondition object`

  Optional condition that must hold for an update to apply. When omitted, the update is unconditional. Asserts the current state of the memory being updated. When an update changes `path`, the precondition still refers to the memory's current content, not the destination path. Currently the only supported variant is `content_sha256`.

  - `type: "content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.
