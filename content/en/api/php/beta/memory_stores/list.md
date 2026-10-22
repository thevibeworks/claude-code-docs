---
title: List Memory Stores
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/list
---

# List Memory Stores

`$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<BetaManagedAgentsMemoryStore>`

**GET** `/v1/memory_stores`

List Memory Stores

## Parameters

- `createdAtGte?:optional \Datetime` (query parameter)

  Return only memory stores created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime` (query parameter)

  Return only memory stores created at or before this time (inclusive).

- `includeArchived?:optional bool` (query parameter)

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit?:optional int` (query parameter)

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `page?:optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

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

$page = $client->beta->memoryStores->list(
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  includeArchived: true,
  limit: 0,
  page: 'page',
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
      "id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Per-user preferences and project context.",
      "metadata": {},
      "name": "User Preferences",
      "type": "memory_store",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
