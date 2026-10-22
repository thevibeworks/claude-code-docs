---
title: Update a Memory Store
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/update
---

# Update a Memory Store

`$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a Memory Store

## Parameters

- `memoryStoreID: string` (path parameter)

  The ID of the memory store to update (`memstore_...`).

  The request fails with HTTP status 400 if the store is archived.

- `description?:optional string`

  New description for the store, up to 1,024 characters. Pass an empty string to clear it.

- `metadata?:optional array<string,string>`

  Changes to apply to the memory store's metadata. Keys you leave out keep their values.

  Set a key to a string to add or replace it, or to `null` to remove it. After the change, the metadata can hold at most 16 key-value pairs. Keys are 1 to 64 characters long and values at most 512 characters.

- `name?:optional string`

  The new name of the memory store, 1 to 255 characters long, without control characters.

  Sessions created after the change use the new name for the store's directory under `/mnt/memory/`.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsMemoryStore`

  - `"memory_store" type`

  - `string id`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `?\Datetime archivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=php#archive-a-store) to learn more about archiving.

  - `\Datetime createdAt`

    When the memory store was created, in RFC 3339.

  - `string description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `array<string,string> metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `string name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `\Datetime updatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->update(
  'memory_store_id',
  description: 'description',
  metadata: ['foo' => 'string'],
  name: 'x',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryStore);
```

### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
