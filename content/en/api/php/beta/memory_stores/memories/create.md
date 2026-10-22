---
title: Create a Memory
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memories/create
---

# Create a Memory

`$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

## Parameters

- `memoryStoreID: string` (path parameter)

  The ID of the memory store to create the memory in (`memstore_...`).

- `content: string`

  The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

  The maximum size is 100 kB (102,400 bytes).

- `path: string`

  The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

  A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

- `view?:optional ManagedAgentsMemoryView` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsMemory`

  - `"memory" type`

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

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;
use Anthropic\Beta\MemoryStores\Memories\ManagedAgentsMemoryView;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->create(
  'memory_store_id',
  content: 'content',
  path: 'xx',
  view: ManagedAgentsMemoryView::BASIC,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemory);
```

### Response (200)

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
