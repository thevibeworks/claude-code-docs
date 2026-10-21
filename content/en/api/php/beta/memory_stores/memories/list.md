---
title: List Memories
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memories/list
---

# List Memories

`$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsMemoryListItem>`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

## Parameters

- `memoryStoreID: string` (path parameter)

  The ID of the memory store to list memories from (`memstore_...`).

- `depth?:optional int` (query parameter)

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

- `limit?:optional int` (query parameter)

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

- `page?:optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `pathPrefix?:optional string` (query parameter)

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `view?:optional ManagedAgentsMemoryView` (query parameter)

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsMemoryListItem`

  - `class ManagedAgentsMemory`

    - `Type type`

    - `string id`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    - `\Datetime createdAt`

      When this memory was created, in RFC 3339 format.

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=php#audit-memory-changes) to learn more about memory versions.

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `\Datetime updatedAt`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    - `?string content`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `class ManagedAgentsMemoryPrefix`

    - `Type type`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;
use Anthropic\Beta\MemoryStores\Memories\ManagedAgentsMemoryView;

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memories->list(
  'memory_store_id',
  depth: 0,
  limit: 0,
  page: 'page',
  pathPrefix: 'path_prefix',
  view: ManagedAgentsMemoryView::BASIC,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
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
