---
title: List memory versions
url: https://platform.claude.com/docs/en/api/php/beta/memory_stores/memory_versions/list
---

# List memory versions

`$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?ManagedAgentsMemoryVersionOperation operation, ?string page, ?string serviceAccountID, ?string sessionID, ?ManagedAgentsMemoryView view, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsMemoryVersion>`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

## Parameters

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

## Returns

- `class ManagedAgentsMemoryVersion`

  - `Type type`

  - `string id`

    Unique identifier for this version (a `memver_...` value).

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string memoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `string memoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `ManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `?string content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `?string contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?int contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `?ManagedAgentsActor createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

  - `?string path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `?\Datetime redactedAt`

    A timestamp in RFC 3339 format

  - `?ManagedAgentsActor redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/beta/sessions/retrieve).

## Example

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

### Response (200)

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
