---
title: Delete a memory store
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/delete
---

## Delete a memory store

`$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedMemoryStore`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memoryStoreID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedMemoryStore`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemoryStore = $client->beta->memoryStores->delete(
  'memory_store_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaManagedAgentsDeletedMemoryStore);
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```
