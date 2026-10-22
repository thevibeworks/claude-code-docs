---
title: Delete a Memory Store
url: https://platform.claude.com/docs/en/api/cli/beta/memory_stores/delete
---

# Delete a Memory Store

`$ ant beta:memory-stores delete`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a Memory Store

## Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to delete (`memstore_...`).

  Deleting a store also deletes all its memories and memory versions. It can't be undone.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_deleted_memory_store: object`

  Confirmation that a `memory_store` was deleted.

  - `type: "memory_store_deleted"`

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

## Example

```bash
ant beta:memory-stores delete \
  --memory-store-id memory_store_id
```

### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```
