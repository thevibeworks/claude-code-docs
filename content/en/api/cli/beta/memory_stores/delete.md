# Delete a memory store

`$ ant beta:memory-stores delete`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

## Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_managed_agents_deleted_memory_store: object`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

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
