---
title: Memories
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memories
---

# Memories

## Create a memory

`$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## List memories

`$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsMemoryListItem>`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## Retrieve a memory

`$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## Update a memory

`$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?ManagedAgentsMemoryView view, ?string content, ?string path, ?ManagedAgentsPrecondition precondition, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## Delete a memory

`$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

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

### Returns

- `class ManagedAgentsDeletedMemory`

  - `Type type`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

### Example

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

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Domain types

### Beta Managed Agents Conflict Error

- `class ManagedAgentsConflictError`

  - `Type type`

  - `?string message`

### Beta Managed Agents Content Sha256 Precondition

- `class ManagedAgentsContentSha256Precondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `class ManagedAgentsDeletedMemory`

  - `Type type`

  - `string id`

    ID of the deleted memory (a `mem_...` value).

### Beta Managed Agents Error

- `class ManagedAgentsError`

  - `class BetaInvalidRequestError`

    - `"invalid_request_error" type`

    - `string message`

  - `class BetaAuthenticationError`

    - `"authentication_error" type`

    - `string message`

  - `class BetaBillingError`

    - `"billing_error" type`

    - `string message`

  - `class BetaPermissionError`

    - `"permission_error" type`

    - `string message`

  - `class BetaNotFoundError`

    - `"not_found_error" type`

    - `string message`

  - `class BetaRateLimitError`

    - `"rate_limit_error" type`

    - `string message`

  - `class BetaGatewayTimeoutError`

    - `"timeout_error" type`

    - `string message`

  - `class BetaAPIError`

    - `"api_error" type`

    - `string message`

  - `class BetaOverloadedError`

    - `"overloaded_error" type`

    - `string message`

  - `class ManagedAgentsMemoryPreconditionFailedError`

    - `Type type`

    - `?string message`

      A human-readable explanation of why the precondition failed.

  - `class ManagedAgentsMemoryPathConflictError`

    - `Type type`

    - `?string conflictingMemoryID`

      The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

      Retry the request when it is empty.

    - `?string conflictingPath`

      The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

    - `?string message`

      A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

  - `class ManagedAgentsConflictError`

    - `Type type`

    - `?string message`

### Beta Managed Agents Memory

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

### Beta Managed Agents Memory List Item

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

### Beta Managed Agents Memory Path Conflict Error

- `class ManagedAgentsMemoryPathConflictError`

  - `Type type`

  - `?string conflictingMemoryID`

    The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified.

    Retry the request when it is empty.

  - `?string conflictingPath`

    The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it.

  - `?string message`

    A human-readable explanation of the conflict. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead.

### Beta Managed Agents Memory Precondition Failed Error

- `class ManagedAgentsMemoryPreconditionFailedError`

  - `Type type`

  - `?string message`

    A human-readable explanation of why the precondition failed.

### Beta Managed Agents Memory Prefix

- `class ManagedAgentsMemoryPrefix`

  - `Type type`

  - `string path`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

### Beta Managed Agents Memory View

- `enum ManagedAgentsMemoryView`

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

### Beta Managed Agents Precondition

- `class ManagedAgentsPrecondition`

  - `Type type`

  - `?string contentSha256`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.
