---
title: Memory Stores
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores
---

# Memory Stores

## Create a memory store

`$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores`

Create a memory store

### Parameters

- `name: string`

  Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

- `description?:optional string`

  Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

- `metadata?:optional array<string,string>`

  Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->create(
  name: 'x',
  description: 'description',
  metadata: ['foo' => 'string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response (200)

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

## List memory stores

`$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<BetaManagedAgentsMemoryStore>`

**GET** `/v1/memory_stores`

List memory stores

### Parameters

- `createdAtGte?:optional \Datetime`

  Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `createdAtLte?:optional \Datetime`

  Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `includeArchived?:optional bool`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit?:optional int`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `page?:optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

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

#### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Retrieve a memory store

`$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `memoryStoreID: string`

  ID of the memory store to retrieve (a `memstore_...` identifier). Required. Enumerate IDs via `GET /v1/memory_stores`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

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

#### Response (200)

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

## Update a memory store

`$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `memoryStoreID: string`

  ID of the memory store to update (a `memstore_...` identifier). Required. Enumerate IDs via `GET /v1/memory_stores`. Updating an archived store returns 400.

- `description?:optional string`

  New description for the store, up to 1024 characters. Pass an empty string to clear it.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name?:optional string`

  New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

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

#### Response (200)

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

## Delete a memory store

`$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeletedMemoryStore`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memoryStoreID: string`

  ID of the memory store to permanently delete (a `memstore_...` identifier). Required. Deletion cascades to all memories and memory versions in the store and cannot be undone.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedMemoryStore`

  - `Type type`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedMemoryStore = $client->beta->memoryStores->delete(
  'memory_store_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedMemoryStore);
```

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `memoryStoreID: string`

  ID of the memory store to archive (a `memstore_...` identifier). Required. Archiving is one-way and idempotent; archived stores cannot be unarchived. Enumerate IDs via `GET /v1/memory_stores`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryStore = $client->beta->memoryStores->archive(
  'memory_store_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryStore);
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Deleted Memory Store

- `class BetaManagedAgentsDeletedMemoryStore`

  - `Type type`

  - `string id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Beta Managed Agents Memory Store

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

## Memory Stores › Memories

### Create a memory

`$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store to create the memory in (`memstore_...`).

- `content: string`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: string`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, or the Unicode line and paragraph separators (U+2028, U+2029), and must be NFC-normalized. Paths are case-sensitive.

- `view?:optional ManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemory`

  - `Type type`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    When this memory was created, in RFC 3339 format.

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `\Datetime updatedAt`

    When this memory was last modified, in RFC 3339 format. Use this as a cheap freshness signal; for who made the change, look up the head version's `created_by` via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

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

##### Response (200)

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

### List memories

`$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsMemoryListItem>`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store to list memories from (`memstore_...`).

- `depth?:optional int`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `limit?:optional int`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `page?:optional string`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `pathPrefix?:optional string`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view?:optional ManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemoryListItem`

  - `class ManagedAgentsMemory`

    - `Type type`

    - `string id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `string contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `int contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `\Datetime createdAt`

      When this memory was created, in RFC 3339 format.

    - `string memoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `string memoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `string path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `\Datetime updatedAt`

      When this memory was last modified, in RFC 3339 format. Use this as a cheap freshness signal; for who made the change, look up the head version's `created_by` via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `?string content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class ManagedAgentsMemoryPrefix`

    - `Type type`

    - `string path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

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

##### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

### Retrieve a memory

`$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memoryID: string`

  The ID of the memory to retrieve (`mem_...`).

- `view?:optional ManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemory`

  - `Type type`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    When this memory was created, in RFC 3339 format.

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `\Datetime updatedAt`

    When this memory was last modified, in RFC 3339 format. Use this as a cheap freshness signal; for who made the change, look up the head version's `created_by` via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->retrieve(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemory);
```

##### Response (200)

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

### Update a memory

`$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?string content, ?string path, ?ManagedAgentsPrecondition precondition, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memoryID: string`

  The ID of the memory to update (`mem_...`).

- `view?:optional ManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

- `content?:optional string`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path?:optional string`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, or the Unicode line and paragraph separators (U+2028, U+2029), and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `precondition?:optional ManagedAgentsPrecondition`

  Optional optimistic-concurrency precondition. When supplied, the update applies only if the memory's current state matches; on mismatch the request returns `memory_precondition_failed_error` (HTTP 409). When omitted, the update is unconditional.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemory`

  - `Type type`

  - `string id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `string contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `int contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `\Datetime createdAt`

    When this memory was created, in RFC 3339 format.

  - `string memoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `string memoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `string path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `\Datetime updatedAt`

    When this memory was last modified, in RFC 3339 format. Use this as a cheap freshness signal; for who made the change, look up the head version's `created_by` via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `?string content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemory = $client->beta->memoryStores->memories->update(
  'memory_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  content: 'content',
  path: 'xx',
  precondition: [
    'type' => 'content_sha256', 'contentSha256' => 'content_sha256'
  ],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemory);
```

##### Response (200)

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

### Delete a memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

#### Parameters

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

#### Returns

- `class ManagedAgentsDeletedMemory`

  - `Type type`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

#### Example

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

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Memory Stores › Memory Versions

### List memory versions

`$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?ManagedAgentsMemoryVersionOperation operation, ?string page, ?string serviceAccountID, ?string sessionID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsMemoryVersion>`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store whose version history to list (`memstore_...`).

- `apiKeyID?:optional string`

  Return only versions written with the API key that has this ID.

- `createdAtGte?:optional \Datetime`

  Return versions created at or after this time (inclusive).

- `createdAtLte?:optional \Datetime`

  Return versions created at or before this time (inclusive).

- `limit?:optional int`

  The maximum number of versions to return per page. Defaults to 20.

- `memoryID?:optional string`

  Return only versions of the memory with this ID (`mem_...`).

  The filter still works after the memory is deleted. The results then include the version whose `operation` is `deleted`.

- `operation?:optional ManagedAgentsMemoryVersionOperation`

  Return only versions that record this kind of change.

- `page?:optional string`

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `serviceAccountID?:optional string`

  Return only versions written by the service account with this ID (`svac_...`).

- `sessionID?:optional string`

  Return only versions written by the session with this ID.

- `view?:optional ManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemoryVersion`

  - `Type type`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    When this version was written, in RFC 3339 format.

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact).

  - `?ManagedAgentsActor redactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->memoryStores->memoryVersions->list(
  'memory_store_id',
  apiKeyID: 'api_key_id',
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  memoryID: 'memory_id',
  operation: ManagedAgentsMemoryVersionOperation::CREATED,
  page: 'page',
  serviceAccountID: 'service_account_id',
  sessionID: 'session_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

### Retrieve a memory version

`$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemoryVersion`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memoryVersionID: string`

  The ID of the memory version to retrieve (`memver_...`).

- `view?:optional ManagedAgentsMemoryView`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemoryVersion`

  - `Type type`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    When this version was written, in RFC 3339 format.

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact).

  - `?ManagedAgentsActor redactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryVersion = $client
  ->beta
  ->memoryStores
  ->memoryVersions
  ->retrieve(
  'memory_version_id',
  memoryStoreID: 'memory_store_id',
  view: ManagedAgentsMemoryView::BASIC,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryVersion);
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

### Redact a memory version

`$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemoryVersion`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `memoryStoreID: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memoryVersionID: string`

  The ID of the memory version to redact (`memver_...`).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsMemoryVersion`

  - `Type type`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    When this version was written, in RFC 3339 format.

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Who performed this write: one of `session_actor`, `api_actor`, `user_actor`, or `service_account_actor`; `null` when no writer is recorded. Captured at write time and preserved through redaction. A `session_actor` is an agent writing through the store's mounted filesystem at `/mnt/memory/`. The API key that created that session is not recorded on agent writes, so attribution names who made the write, not who is ultimately responsible; look up session provenance via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    When this version was redacted, in RFC 3339 format, or `null` if it has not been redacted. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are all `null`. See [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact).

  - `?ManagedAgentsActor redactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsMemoryVersion = $client
  ->beta
  ->memoryStores
  ->memoryVersions
  ->redact(
  'memory_version_id',
  memoryStoreID: 'memory_store_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsMemoryVersion);
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```
