---
title: List Memories
url: https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/list
---

# List Memories

`$ ant beta:memory-stores:memories list`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

## Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to list memories from (`memstore_...`).

- `--depth: optional number` (query parameter)

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

  format: int32

- `--limit: optional number` (query parameter)

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

  format: int32

- `--page: optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `--path-prefix: optional string` (query parameter)

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `--view: optional "basic" or "full"` (query parameter)

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsListMemoriesResult: object`

  A page of results from [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=cli).

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `beta_managed_agents_memory: object`

      A text document at a path inside a memory store.

      `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#view-and-edit-memories) to learn more about working with memories.

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

        See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

      - `path: string`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `updated_at: string`

        When the memory was last changed, in RFC 3339.

        To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

        format: date-time

      - `content: optional string`

        The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

        The maximum size is 100 kB (102,400 bytes).

    - `beta_managed_agents_memory_prefix: object`

      A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=cli) returns instead of the memories below the requested `depth`.

      It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

      - `type: "memory_prefix"`

      - `path: string`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `next_page: optional string`

    The value to pass as `page` to get the next page, or `null` if there are no more results.

## Example

```bash
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

### Response (200)

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
