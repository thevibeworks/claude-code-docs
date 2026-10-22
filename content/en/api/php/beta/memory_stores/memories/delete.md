---
title: Delete a Memory
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memories/delete
---

# Delete a Memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

## Parameters

- `memoryStoreID: string` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `memoryID: string` (path parameter)

  The ID of the memory to delete (`mem_...`).

- `expectedContentSha256?:optional string` (query parameter)

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsDeletedMemory`

  - `"memory_deleted" type`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemory = $client->beta->memoryStores->memories->delete(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  expectedContentSha256: 'expected_content_sha256',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedMemory);
```

### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```
