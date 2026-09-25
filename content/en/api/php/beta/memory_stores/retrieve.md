---
title: Retrieve a memory store
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/retrieve
---

# Retrieve a memory store

`$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

## Parameters

- `memoryStoreID: string`

  ID of the memory store to retrieve (a `memstore_...` identifier). Required. Enumerate IDs via `GET /v1/memory_stores`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsMemoryStore`

  - `Type type`

  - `string id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `\Datetime createdAt`

    Timestamp when the store was created.

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `\Datetime updatedAt`

    Timestamp when the store's `name`, `description`, or `metadata` was last modified. Memory writes inside the store do not advance this.

  - `?\Datetime archivedAt`

    Timestamp when the store was archived, or `null` if active. Set once and never cleared; archiving is one-way. Archived stores are read-only and cannot be attached to new sessions.

  - `?string description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `?array<string,string> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->retrieve(
  'memory_store_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryStore);
```

### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```
