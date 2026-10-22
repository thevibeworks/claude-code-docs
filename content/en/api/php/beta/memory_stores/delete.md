---
title: Delete a Memory Store
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/delete
---

# Delete a Memory Store

`$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeletedMemoryStore`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a Memory Store

## Parameters

- `memoryStoreID: string` (path parameter)

  The ID of the memory store to delete (`memstore_...`).

  Deleting a store also deletes all its memories and memory versions. It can't be undone.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsDeletedMemoryStore`

  - `"memory_store_deleted" type`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemoryStore = $client->beta->memoryStores->delete(
  'memory_store_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedMemoryStore);
```

### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```
