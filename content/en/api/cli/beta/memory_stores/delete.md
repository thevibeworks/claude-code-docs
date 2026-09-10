---
title: Delete a memory store
url: https://platform.claude.com/docs/en/api/cli/beta/memory_stores/delete
---

# Delete a memory store

`$ ant beta:memory-stores delete`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

## Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

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
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```
