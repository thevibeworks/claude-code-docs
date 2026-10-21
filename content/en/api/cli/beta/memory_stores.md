---
title: Memory Stores
url: https://platform.claude.com/docs/en/api/cli/beta/memory_stores
---

# Memory Stores

## Create a Memory Store

`$ ant beta:memory-stores create`

**POST** `/v1/memory_stores`

Create a Memory Store

### Parameters

- `--name: string`

  The name of the memory store, 1 to 255 characters long, without control characters. Names don't have to be unique in a workspace.

  In a session, the store's directory under `/mnt/memory/` is based on this name. The name is lowercased and every run of characters other than ASCII letters and digits becomes one hyphen. The session's memory store resource gives the exact path in `mount_path`.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#how-the-agent-accesses-memory) to learn more about how agents access memory stores.

  minLength: 1, maxLength: 255

- `--description: optional string`

  Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  maxLength: 1024

- `--metadata: optional map[string]`

  Key-value pairs for your own use, such as the end user that the store belongs to. The agent doesn't see them.

  A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
ant beta:memory-stores create \
  --api-key my-anthropic-api-key \
  --name x
```

#### Response (200)

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

## List Memory Stores

`$ ant beta:memory-stores list`

**GET** `/v1/memory_stores`

List Memory Stores

### Parameters

- `--created-at-gte: optional string` (query parameter)

  Return only memory stores created at or after this time (inclusive).

  format: date-time

- `--created-at-lte: optional string` (query parameter)

  Return only memory stores created at or before this time (inclusive).

  format: date-time

- `--include-archived: optional boolean` (query parameter)

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `--limit: optional number` (query parameter)

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  format: int32

- `--page: optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsListMemoryStoresResponse: object`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `data: optional array of BetaManagedAgentsMemoryStore`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `type: "memory_store"`

    - `id: string`

      The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

    - `archived_at: string`

      When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

      Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

      format: date-time

    - `created_at: string`

      When the memory store was created, in RFC 3339.

      format: date-time

    - `description: string`

      Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `metadata: map[string]`

      Key-value pairs for your own use, such as the end user that the store belongs to.

      A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

    - `name: string`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `updated_at: string`

      When the memory store was last changed, in RFC 3339.

      Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

      format: date-time

  - `next_page: optional string`

    The value to pass as `page` to get the next page, or `null` if there are no more results.

### Example

```bash
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
```

#### Response (200)

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

## Retrieve a Memory Store

`$ ant beta:memory-stores retrieve`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a Memory Store

### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to retrieve (`memstore_...`).

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
ant beta:memory-stores retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

#### Response (200)

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

## Update a Memory Store

`$ ant beta:memory-stores update`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a Memory Store

### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to update (`memstore_...`).

  The request fails with HTTP status 400 if the store is archived.

- `--description: optional string`

  New description for the store, up to 1,024 characters. Pass an empty string to clear it.

  maxLength: 1024

- `--metadata: optional map[string]`

  Changes to apply to the memory store's metadata. Keys you leave out keep their values.

  Set a key to a string to add or replace it, or to `null` to remove it. After the change, the metadata can hold at most 16 key-value pairs. Keys are 1 to 64 characters long and values at most 512 characters.

- `--name: optional string`

  The new name of the memory store, 1 to 255 characters long, without control characters.

  Sessions created after the change use the new name for the store's directory under `/mnt/memory/`.

  minLength: 1, maxLength: 255

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
ant beta:memory-stores update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

#### Response (200)

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

## Delete a Memory Store

`$ ant beta:memory-stores delete`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a Memory Store

### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to delete (`memstore_...`).

  Deleting a store also deletes all its memories and memory versions. It can't be undone.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_deleted_memory_store: object`

  Confirmation that a `memory_store` was deleted.

  - `type: "memory_store_deleted"`

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Example

```bash
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a Memory Store

`$ ant beta:memory-stores archive`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a Memory Store

### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to archive (`memstore_...`).

  Archiving can't be undone. Archiving a store that is already archived returns it unchanged.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
ant beta:memory-stores archive \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Deleted Memory Store

- `beta_managed_agents_deleted_memory_store: object`

  Confirmation that a `memory_store` was deleted.

  - `type: "memory_store_deleted"`

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Beta Managed Agents Memory Store

- `beta_managed_agents_memory_store: object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

## Memory Stores › Memories

### Create a Memory

`$ ant beta:memory-stores:memories create`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to create the memory in (`memstore_...`).

- `--content: string`

  The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

  The maximum size is 100 kB (102,400 bytes).

- `--path: string`

  The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

  A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

  minLength: 2, maxLength: 1024

- `--view: optional "basic" or "full"` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_memory: object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories create \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --content content \
  --path xx
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

### List Memories

`$ ant beta:memory-stores:memories list`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store to list memories from (`memstore_...`).

- `--depth: optional number` (query parameter)

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

  format: int32

- `--limit: optional number` (query parameter)

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

  format: int32

- `--page: optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `--path-prefix: optional string` (query parameter)

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `--view: optional "basic" or "full"` (query parameter)

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsListMemoriesResult: object`

  A page of results from [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=cli).

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `beta_managed_agents_memory: object`

      A text document at a path inside a memory store.

      `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#view-and-edit-memories) to learn more about working with memories.

      - `type: "memory"`

      - `id: string`

        The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

        To retrieve, update, or delete the memory, pass this ID.

      - `content_sha256: string`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `content_size_bytes: number`

        The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

        format: int32

      - `created_at: string`

        When this memory was created, in RFC 3339 format.

        format: date-time

      - `memory_store_id: string`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `memory_version_id: string`

        The ID of the memory version that holds the memory's current content (`memver_...`).

        Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

        See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

      - `path: string`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `updated_at: string`

        When the memory was last changed, in RFC 3339.

        To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

        format: date-time

      - `content: optional string`

        The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

        The maximum size is 100 kB (102,400 bytes).

    - `beta_managed_agents_memory_prefix: object`

      A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=cli) returns instead of the memories below the requested `depth`.

      It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

      - `type: "memory_prefix"`

      - `path: string`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `next_page: optional string`

    The value to pass as `page` to get the next page, or `null` if there are no more results.

#### Example

```bash
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "mem_011CZkZ9X2dpNyB6YbtxvB6e",
      "content_sha256": "ba7936d94c84d948a2232088f78228f175df6a8353b2d5bc9228eee5794a0024",
      "content_size_bytes": 28,
      "created_at": "2026-03-15T10:00:00Z",
      "memory_store_id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "memory_version_id": "memver_011CZkZBJq5dWxk9fVLNcPht",
      "path": "/preferences/formatting.md",
      "type": "memory",
      "updated_at": "2026-03-15T10:00:00Z",
      "content": null
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Memory

`$ ant beta:memory-stores:memories retrieve`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a Memory

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `--memory-id: string` (path parameter)

  The ID of the memory to retrieve (`mem_...`).

- `--view: optional "basic" or "full"` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_memory: object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
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

### Update a Memory

`$ ant beta:memory-stores:memories update`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a Memory

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store that holds the memory (`memstore_...`).

- `--memory-id: string` (path parameter)

  The ID of the memory to update (`mem_...`).

- `--view: optional "basic" or "full"` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `--content: optional string`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `--path: optional string`

  The new path of the memory, which renames it. Omit it to keep the current path.

  The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `--precondition: optional object`

  The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

  If the condition fails, the request fails with HTTP status 409.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_memory: object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
ant beta:memory-stores:memories update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
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

### Delete a Memory

`$ ant beta:memory-stores:memories delete`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

#### Parameters

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

#### Returns

- `beta_managed_agents_deleted_memory: object`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=cli) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about how long versions are kept.

  - `type: "memory_deleted"`

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

#### Example

```bash
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Memory Stores › Memory Versions

### List Memory Versions

`$ ant beta:memory-stores:memory-versions list`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List Memory Versions

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store whose version history to list (`memstore_...`).

- `--api-key-id: optional string` (query parameter)

  Return only versions written with the API key that has this ID.

- `--created-at-gte: optional string` (query parameter)

  Return versions created at or after this time (inclusive).

  format: date-time

- `--created-at-lte: optional string` (query parameter)

  Return versions created at or before this time (inclusive).

  format: date-time

- `--limit: optional number` (query parameter)

  The maximum number of versions to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 versions.

  format: int32

- `--memory-id: optional string` (query parameter)

  Return only versions of the memory with this ID (`mem_...`).

  The filter still works after the memory is deleted. While that memory's versions are retained, the results include the version whose `operation` is `deleted`.

- `--operation: optional "created" or "modified" or "deleted"` (query parameter)

  Return only versions that record this kind of change.

- `--page: optional string` (query parameter)

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `--service-account-id: optional string` (query parameter)

  Return only versions written by the service account with this ID (`svac_...`).

- `--session-id: optional string` (query parameter)

  Return only versions written by the session with this ID.

- `--view: optional "basic" or "full"` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsListMemoryVersionsResult: object`

  A page of results from [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli).

  - `data: optional array of BetaManagedAgentsMemoryVersion`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `type: "memory_version"`

    - `id: string`

      Unique identifier for this version (a `memver_...` value).

    - `created_at: string`

      When this version was written, in RFC 3339 format.

      format: date-time

    - `memory_id: string`

      The ID of the memory that this version belongs to (`mem_...`).

      The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

    - `memory_store_id: string`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `operation: "created" or "modified" or "deleted"`

      The kind of mutation this version records: `created`, `modified`, or `deleted`.

      - `"created"`

        The memory was created. The first version in any memory's lineage.

      - `"modified"`

        The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

      - `"deleted"`

        The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

    - `content: optional string`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `content_sha256: optional string`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `content_size_bytes: optional number`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

      format: int32

    - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

      Who made this change to the memory, or `null` if the author wasn't recorded.

      Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

      You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) to learn more about where the change came from.

      - `beta_managed_agents_session_actor: object`

        An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

        - `type: "session_actor"`

        - `session_id: string`

          ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) for further provenance.

          minLength: 1

      - `beta_managed_agents_api_actor: object`

        A direct caller of the public API, identified by the API key that authenticated the request.

        - `type: "api_actor"`

        - `api_key_id: string`

          ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

          minLength: 1

      - `beta_managed_agents_user_actor: object`

        A human user, for example acting through the Anthropic Console.

        - `type: "user_actor"`

        - `user_id: string`

          ID of the user (a `user_...` value).

          minLength: 1

      - `beta_managed_agents_service_account_actor: object`

        A workload authenticated as a service account, for example via Workload Identity Federation.

        - `type: "service_account_actor"`

        - `service_account_id: string`

          ID of the service account (a `svac_...` value).

          minLength: 1

    - `path: optional string`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `redacted_at: optional string`

      When the version was redacted, in RFC 3339, or `null` if it hasn't been.

      When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#redact-a-version) to learn more about redaction.

      format: date-time

    - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

      Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

      - `beta_managed_agents_session_actor: object`

        An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `beta_managed_agents_api_actor: object`

        A direct caller of the public API, identified by the API key that authenticated the request.

      - `beta_managed_agents_user_actor: object`

        A human user, for example acting through the Anthropic Console.

      - `beta_managed_agents_service_account_actor: object`

        A workload authenticated as a service account, for example via Workload Identity Federation.

  - `next_page: optional string`

    The value to pass as `page` to get the next page, or `null` if there are no more results.

#### Example

```bash
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "memver_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "memory_id": "mem_011CZkZ9X2dpNyB6YbtxvB6e",
      "memory_store_id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "operation": "created",
      "type": "memory_version",
      "content": null,
      "content_sha256": "ba7936d94c84d948a2232088f78228f175df6a8353b2d5bc9228eee5794a0024",
      "content_size_bytes": 28,
      "created_by": {
        "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
        "type": "session_actor"
      },
      "path": "/preferences/formatting.md",
      "redacted_at": null,
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Memory Version

`$ ant beta:memory-stores:memory-versions retrieve`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a Memory Version

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store that holds the version (`memstore_...`).

- `--memory-version-id: string` (path parameter)

  The ID of the memory version to retrieve (`memver_...`).

- `--view: optional "basic" or "full"` (query parameter)

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_memory_version: object`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

  - `type: "memory_version"`

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `"created"`

      The memory was created. The first version in any memory's lineage.

    - `"modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `"deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) to learn more about where the change came from.

    - `beta_managed_agents_session_actor: object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: "session_actor"`

      - `session_id: string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) for further provenance.

        minLength: 1

    - `beta_managed_agents_api_actor: object`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: "api_actor"`

      - `api_key_id: string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `beta_managed_agents_user_actor: object`

      A human user, for example acting through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `beta_managed_agents_service_account_actor: object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: "service_account_actor"`

      - `service_account_id: string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#redact-a-version) to learn more about redaction.

    format: date-time

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

    - `beta_managed_agents_session_actor: object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

    - `beta_managed_agents_api_actor: object`

      A direct caller of the public API, identified by the API key that authenticated the request.

    - `beta_managed_agents_user_actor: object`

      A human user, for example acting through the Anthropic Console.

    - `beta_managed_agents_service_account_actor: object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

#### Example

```bash
ant beta:memory-stores:memory-versions retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
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

### Redact a Memory Version

`$ ant beta:memory-stores:memory-versions redact`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a Memory Version

#### Parameters

- `--memory-store-id: string` (path parameter)

  The ID of the memory store that holds the version (`memstore_...`).

- `--memory-version-id: string` (path parameter)

  The ID of the memory version to redact (`memver_...`).

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_memory_version: object`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#audit-memory-changes) to learn more about memory versions.

  - `type: "memory_version"`

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=cli) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `"created"`

      The memory was created. The first version in any memory's lineage.

    - `"modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `"deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) to learn more about where the change came from.

    - `beta_managed_agents_session_actor: object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: "session_actor"`

      - `session_id: string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=cli) for further provenance.

        minLength: 1

    - `beta_managed_agents_api_actor: object`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: "api_actor"`

      - `api_key_id: string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `beta_managed_agents_user_actor: object`

      A human user, for example acting through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `beta_managed_agents_service_account_actor: object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: "service_account_actor"`

      - `service_account_id: string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=cli#redact-a-version) to learn more about redaction.

    format: date-time

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

    - `beta_managed_agents_session_actor: object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

    - `beta_managed_agents_api_actor: object`

      A direct caller of the public API, identified by the API key that authenticated the request.

    - `beta_managed_agents_user_actor: object`

      A human user, for example acting through the Anthropic Console.

    - `beta_managed_agents_service_account_actor: object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

#### Example

```bash
ant beta:memory-stores:memory-versions redact \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
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
