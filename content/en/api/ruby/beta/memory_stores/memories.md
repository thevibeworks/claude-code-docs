---
title: Memories
url: https://platform.claude.com/docs/en/api/ruby/beta/memory_stores/memories
---

# Memories

## Create a Memory

`beta.memory_stores.memories.create(memory_store_id, **kwargs) -> BetaManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

### Parameters

- `memory_store_id: String` (path parameter)

  The ID of the memory store to create the memory in (`memstore_...`).

- `content: String`

  The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

  The maximum size is 100 kB (102,400 bytes).

- `path: String`

  The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

  A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

  minLength: 2, maxLength: 1024

- `view: BetaManagedAgentsMemoryView` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

  - `type: :memory`

  - `id: String`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: Time`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: Time`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: String`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.create("memory_store_id", content: "content", path: "xx")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryListItem>`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

### Parameters

- `memory_store_id: String` (path parameter)

  The ID of the memory store to list memories from (`memstore_...`).

- `depth: Integer` (query parameter)

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

  format: int32

- `limit: Integer` (query parameter)

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

  format: int32

- `page: String` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `path_prefix: String` (query parameter)

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `view: BetaManagedAgentsMemoryView` (query parameter)

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `type BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=ruby) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `class BetaManagedAgentsMemory`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

    - `type: :memory`

    - `id: String`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `content_sha256: String`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: Integer`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `created_at: Time`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `memory_store_id: String`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: String`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

    - `path: String`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `updated_at: Time`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `content: String`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=ruby) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `type: :memory_prefix`

    - `path: String`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memories.list("memory_store_id")

puts(page)
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

`beta.memory_stores.memories.retrieve(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a Memory

### Parameters

- `memory_store_id: String` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: String` (path parameter)

  The ID of the memory to retrieve (`mem_...`).

- `view: BetaManagedAgentsMemoryView` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

  - `type: :memory`

  - `id: String`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: Time`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: Time`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: String`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.retrieve("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.update(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a Memory

### Parameters

- `memory_store_id: String` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: String` (path parameter)

  The ID of the memory to update (`mem_...`).

- `view: BetaManagedAgentsMemoryView` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

- `content: String`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: String`

  The new path of the memory, which renames it. Omit it to keep the current path.

  The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `precondition: BetaManagedAgentsPrecondition`

  The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

  If the condition fails, the request fails with HTTP status 409.

  - `type: :content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

  - `type: :memory`

  - `id: String`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: Time`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: Time`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: String`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.update("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
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

`beta.memory_stores.memories.delete(memory_id, **kwargs) -> BetaManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

### Parameters

- `memory_store_id: String` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: String` (path parameter)

  The ID of the memory to delete (`mem_...`).

- `expected_content_sha256: String` (query parameter)

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"message-batches-2024-09-24"`

  - `:"prompt-caching-2024-07-31"`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"pdfs-2024-09-25"`

  - `:"token-counting-2024-11-01"`

  - `:"token-efficient-tools-2025-02-19"`

  - `:"output-128k-2025-02-19"`

  - `:"files-api-2025-04-14"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"extended-cache-ttl-2025-04-11"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"skills-2025-10-02"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"cache-diagnosis-2026-04-07"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"ce-user-management-2026-07-13"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedMemory`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=ruby) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=ruby) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about how long versions are kept.

  - `type: :memory_deleted`

  - `id: String`

    ID of the deleted memory (a `mem_...` value).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory = anthropic.beta.memory_stores.memories.delete("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_deleted_memory)
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

- `class BetaManagedAgentsConflictError`

  - `type: :conflict_error`

  - `message: String`

### Beta Managed Agents Content Sha256 Precondition

- `class BetaManagedAgentsContentSha256Precondition`

  A precondition that applies an update only if the memory's current content has the hash in `content_sha256`.

  If the hashes differ, the request fails with HTTP status 409. Retrieve the memory and retry. If the memory already has exactly the requested `content` and `path`, the request succeeds even though the hashes differ.

  - `type: :content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class BetaManagedAgentsDeletedMemory`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=ruby) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=ruby) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about how long versions are kept.

  - `type: :memory_deleted`

  - `id: String`

    ID of the deleted memory (a `mem_...` value).

### Beta Managed Agents Error

- `type BetaManagedAgentsError = BetaInvalidRequestError | BetaAuthenticationError | BetaBillingError | 9 more`

  - `class BetaInvalidRequestError`

    - `type: :invalid_request_error`

    - `message: String`

  - `class BetaAuthenticationError`

    - `type: :authentication_error`

    - `message: String`

  - `class BetaBillingError`

    - `type: :billing_error`

    - `message: String`

  - `class BetaPermissionError`

    - `type: :permission_error`

    - `message: String`

  - `class BetaNotFoundError`

    - `type: :not_found_error`

    - `message: String`

  - `class BetaRateLimitError`

    - `type: :rate_limit_error`

    - `message: String`

  - `class BetaGatewayTimeoutError`

    - `type: :timeout_error`

    - `message: String`

  - `class BetaAPIError`

    - `type: :api_error`

    - `message: String`

  - `class BetaOverloadedError`

    - `type: :overloaded_error`

    - `message: String`

  - `class BetaManagedAgentsMemoryPreconditionFailedError`

    The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

    The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

    - `type: :memory_precondition_failed_error`

    - `message: String`

      A human-readable explanation of why the precondition failed.

  - `class BetaManagedAgentsMemoryPathConflictError`

    The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path.

    Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

    - `type: :memory_path_conflict_error`

    - `conflicting_memory_id: String`

      The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

      Retry the request when it is empty.

    - `conflicting_path: String`

      The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

    - `message: String`

      A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

  - `class BetaManagedAgentsConflictError`

    - `type: :conflict_error`

    - `message: String`

### Beta Managed Agents Memory

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

  - `type: :memory`

  - `id: String`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: Time`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: Time`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: String`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `type BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=ruby) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `class BetaManagedAgentsMemory`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#view-and-edit-memories) to learn more about working with memories.

    - `type: :memory`

    - `id: String`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `content_sha256: String`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: Integer`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `created_at: Time`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `memory_store_id: String`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: String`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#audit-memory-changes) to learn more about memory versions.

    - `path: String`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `updated_at: Time`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `content: String`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=ruby) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `type: :memory_prefix`

    - `path: String`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Beta Managed Agents Memory Path Conflict Error

- `class BetaManagedAgentsMemoryPathConflictError`

  The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path.

  Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it.

  - `type: :memory_path_conflict_error`

  - `conflicting_memory_id: String`

    The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

    Retry the request when it is empty.

  - `conflicting_path: String`

    The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

  - `message: String`

    A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

### Beta Managed Agents Memory Precondition Failed Error

- `class BetaManagedAgentsMemoryPreconditionFailedError`

  The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete.

  The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=ruby#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions.

  - `type: :memory_precondition_failed_error`

  - `message: String`

    A human-readable explanation of why the precondition failed.

### Beta Managed Agents Memory Prefix

- `class BetaManagedAgentsMemoryPrefix`

  A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=ruby) returns instead of the memories below the requested `depth`.

  It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

  - `type: :memory_prefix`

  - `path: String`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Beta Managed Agents Memory View

- `type BetaManagedAgentsMemoryView = :basic | :full`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `:basic`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `:full`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Beta Managed Agents Precondition

- `class BetaManagedAgentsPrecondition`

  Optional condition that must hold for an update to apply. When omitted, the update is unconditional. Asserts the current state of the memory being updated. When an update changes `path`, the precondition still refers to the memory's current content, not the destination path. Currently the only supported variant is `content_sha256`.

  - `type: :content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.
