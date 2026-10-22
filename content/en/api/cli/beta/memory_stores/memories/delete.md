---
title: Delete a Memory
url: https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/delete
---

# Delete a Memory

`$ ant beta:memory-stores:memories delete`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

## Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `--memory-id: string` (path parameter)

  The ID of the memory to delete (`mem_...`).

- `--expected-content-sha256: optional string` (query parameter)

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_deleted_memory: object`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=cli) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about how long versions are kept.

  - `type: "memory_deleted"`

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

## Example

```bash
ant beta:memory-stores:memories delete \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```
