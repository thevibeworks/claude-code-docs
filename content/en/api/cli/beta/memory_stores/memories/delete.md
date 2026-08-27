# Delete a memory

`$ ant beta:memory-stores:memories delete`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

## Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--expected-content-sha256: optional string`

  Query param: Query parameter for expected_content_sha256

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_managed_agents_deleted_memory: object`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). Deleting a memory does not erase its version history: its versions remain listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) while they are retained (each version is kept for at least the version retention period after it was written, unless the store itself is deleted).

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

## Example

```bash
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
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
