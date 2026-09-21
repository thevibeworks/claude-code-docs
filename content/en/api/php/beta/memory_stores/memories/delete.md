---
title: Delete a memory
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memories/delete
---

# Delete a memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

## Parameters

- `memoryStoreID: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memoryID: string`

  The ID of the memory to delete (`mem_...`).

- `expectedContentSha256?:optional string`

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsDeletedMemory`

  - `Type type`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

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
