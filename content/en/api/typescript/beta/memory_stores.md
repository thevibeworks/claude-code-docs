---
title: Memory Stores
url: https://platform.claude.com/docs/en/api/typescript/beta/memory_stores
---

# Memory Stores

## Create a Memory Store

- Signature: `client.beta.memoryStores.create(params: MemoryStoreCreateParams, options?: RequestOptions): BetaManagedAgentsMemoryStore`
- Endpoint: `POST /v1/memory_stores`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.create({ name: "x" });

console.log(betaManagedAgentsMemoryStore.id);
```

### Example response (200)

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

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

interface MemoryStoreCreateParams {
  /** The name of the memory store, 1 to 255 characters long, without control characters. Names don't have to be unique in a workspace. In a session, the store's directory under `/mnt/memory/` is based on this name. The name is lowercased and every run of characters other than ASCII letters and digits becomes one hyphen. The session's memory store resource gives the exact path in `mount_path`. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#how-the-agent-accesses-memory) to learn more about how agents access memory stores. */
  name: string; // minLength: 1, maxLength: 255
  /** Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. */
  description?: string; // maxLength: 1024
  /** Key-value pairs for your own use, such as the end user that the store belongs to. The agent doesn't see them. A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. */
  metadata?: Record<string, string>;
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write. */
interface BetaManagedAgentsMemoryStore {
  type: "memory_store";
  /** The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session. */
  id: string;
  /** When the memory store was archived, in RFC 3339, or `null` if it hasn't been. Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#archive-a-store) to learn more about archiving. */
  archived_at: string | null; // format: date-time
  /** When the memory store was created, in RFC 3339. */
  created_at: string; // format: date-time
  /** Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset. */
  description: string;
  /** Key-value pairs for your own use, such as the end user that the store belongs to. A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata. */
  metadata: Record<string, string>;
  /** Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name. */
  name: string;
  /** When the memory store was last changed, in RFC 3339. Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't. */
  updated_at: string; // format: date-time
}
```

### Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";
```

## List Memory Stores

- Signature: `client.beta.memoryStores.list(params?: MemoryStoreListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsMemoryStore>`
- Endpoint: `GET /v1/memory_stores`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryStore of client.beta.memoryStores.list()) {
  console.log(betaManagedAgentsMemoryStore.id);
}
```

### Example response (200)

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

### Parameters

```ts
interface MemoryStoreListParams {
  /** Return only memory stores created at or after this time (inclusive). */
  "created_at[gte]"?: string; // query parameter, format: date-time
  /** Return only memory stores created at or before this time (inclusive). */
  "created_at[lte]"?: string; // query parameter, format: date-time
  /** When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded). */
  include_archived?: boolean; // query parameter
  /** Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted. */
  limit?: number; // query parameter, format: int32
  /** The `next_page` value from a previous response, to get the next page. Omit it to get the first page. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Retrieve a Memory Store

- Signature: `client.beta.memoryStores.retrieve(memoryStoreID: string, params?: MemoryStoreRetrieveParams, options?: RequestOptions): BetaManagedAgentsMemoryStore`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.retrieve(
  "memory_store_id"
);

console.log(betaManagedAgentsMemoryStore.id);
```

### Example response (200)

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

### Parameters

```ts
/** The ID of the memory store to retrieve (`memstore_...`). */
memoryStoreID: string; // path parameter

interface MemoryStoreRetrieveParams {
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Update a Memory Store

- Signature: `client.beta.memoryStores.update(memoryStoreID: string, params: MemoryStoreUpdateParams, options?: RequestOptions): BetaManagedAgentsMemoryStore`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.update(
  "memory_store_id",
  {}
);

console.log(betaManagedAgentsMemoryStore.id);
```

### Example response (200)

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

### Parameters

```ts
/** The ID of the memory store to update (`memstore_...`). The request fails with HTTP status 400 if the store is archived. */
memoryStoreID: string; // path parameter

interface MemoryStoreUpdateParams {
  /** New description for the store, up to 1,024 characters. Pass an empty string to clear it. */
  description?: string | null; // maxLength: 1024
  /** Changes to apply to the memory store's metadata. Keys you leave out keep their values. Set a key to a string to add or replace it, or to `null` to remove it. After the change, the metadata can hold at most 16 key-value pairs. Keys are 1 to 64 characters long and values at most 512 characters. */
  metadata?: Record<string, string | null> | null;
  /** The new name of the memory store, 1 to 255 characters long, without control characters. Sessions created after the change use the new name for the store's directory under `/mnt/memory/`. */
  name?: string | null; // minLength: 1, maxLength: 255
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Delete a Memory Store

- Signature: `client.beta.memoryStores.delete(memoryStoreID: string, params?: MemoryStoreDeleteParams, options?: RequestOptions): BetaManagedAgentsDeletedMemoryStore`
- Endpoint: `DELETE /v1/memory_stores/{memory_store_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemoryStore = await client.beta.memoryStores.delete(
  "memory_store_id"
);

console.log(betaManagedAgentsDeletedMemoryStore.id);
```

### Example response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

### Parameters

```ts
/** The ID of the memory store to delete (`memstore_...`). Deleting a store also deletes all its memories and memory versions. It can't be undone. */
memoryStoreID: string; // path parameter

interface MemoryStoreDeleteParams {
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** Confirmation that a `memory_store` was deleted. */
interface BetaManagedAgentsDeletedMemoryStore {
  type: "memory_store_deleted";
  /** ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable. */
  id: string;
}
```

## Archive a Memory Store

- Signature: `client.beta.memoryStores.archive(memoryStoreID: string, params?: MemoryStoreArchiveParams, options?: RequestOptions): BetaManagedAgentsMemoryStore`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/archive`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryStore = await client.beta.memoryStores.archive("memory_store_id");

console.log(betaManagedAgentsMemoryStore.id);
```

### Example response (200)

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

### Parameters

```ts
/** The ID of the memory store to archive (`memstore_...`). Archiving can't be undone. Archiving a store that is already archived returns it unchanged. */
memoryStoreID: string; // path parameter

interface MemoryStoreArchiveParams {
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Memory Stores › Memories

### Create a Memory

- Signature: `client.beta.memoryStores.memories.create(memoryStoreID: string, params: MemoryCreateParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memories`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.create(
  "memory_store_id",
  { content: "content", path: "/P" }
);

console.log(betaManagedAgentsMemory.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory store to create the memory in (`memstore_...`). */
memoryStoreID: string; // path parameter

interface MemoryCreateParams {
  /** The UTF-8 text content of the new memory. Pass `""` to create an empty memory. The maximum size is 100 kB (102,400 bytes). */
  content: string | null;
  /** The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. */
  path: string; // minLength: 2, maxLength: 1024, pattern: ^(/[^/\u0000]+)+$
  /** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
  view?: BetaManagedAgentsMemoryView; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** A text document at a path inside a memory store. `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#view-and-edit-memories) to learn more about working with memories. */
interface BetaManagedAgentsMemory {
  type: "memory";
  /** The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes. To retrieve, update, or delete the memory, pass this ID. */
  id: string;
  /** Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`. */
  content_sha256: string;
  /** The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`. */
  content_size_bytes: number; // format: int32
  /** When this memory was created, in RFC 3339 format. */
  created_at: string; // format: date-time
  /** ID of the memory store this memory belongs to (a `memstore_...` value). */
  memory_store_id: string;
  /** The ID of the memory version that holds the memory's current content (`memver_...`). Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#audit-memory-changes) to learn more about memory versions. */
  memory_version_id: string;
  /** Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes. */
  path: string;
  /** When the memory was last changed, in RFC 3339. To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references. */
  updated_at: string; // format: date-time
  /** The memory's UTF-8 text content, or `null` when the response uses `view=basic`. The maximum size is 100 kB (102,400 bytes). */
  content?: string | null;
}
```

#### Types

```ts
type BetaManagedAgentsMemoryView =
  /** Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content. */
  | "basic"
  /** Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20. */
  | "full";
```

### List Memories

- Signature: `client.beta.memoryStores.memories.list(memoryStoreID: string, params?: MemoryListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsMemoryListItem>`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memories`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryListItem of client.beta.memoryStores.memories.list(
  "memory_store_id"
)) {
  console.log(betaManagedAgentsMemoryListItem);
}
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory store to list memories from (`memstore_...`). */
memoryStoreID: string; // path parameter

interface MemoryListParams {
  /** How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix. Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items. */
  depth?: number; // query parameter, format: int32, beta header: agent-memory-2026-07-22
  /** The maximum number of items to return per page, from 1 to 100. Defaults to 20. With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit. */
  limit?: number; // query parameter, format: int32, beta header: agent-memory-2026-07-22
  /** The `next_page` value from a previous response, to get the next page. Omit it to get the first page. */
  page?: string; // query parameter, beta header: agent-memory-2026-07-22
  /** Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information. Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`. */
  path_prefix?: string; // query parameter, beta header: agent-memory-2026-07-22
  /** Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`. With `full`, a page holds at most 20 items. */
  view?: BetaManagedAgentsMemoryView; // query parameter, beta header: agent-memory-2026-07-22
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`. */
type BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix;
```

#### Types

```ts
/** A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) returns instead of the memories below the requested `depth`. It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`. */
interface BetaManagedAgentsMemoryPrefix {
  type: "memory_prefix";
  /** The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory. */
  path: string;
}
```

### Retrieve a Memory

- Signature: `client.beta.memoryStores.memories.retrieve(memoryID: string, params: MemoryRetrieveParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.retrieve("memory_id", {
  memory_store_id: "memory_store_id"
});

console.log(betaManagedAgentsMemory.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory to retrieve (`mem_...`). */
memoryID: string; // path parameter

interface MemoryRetrieveParams {
  /** The ID of the memory store that holds the memory (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
  view?: BetaManagedAgentsMemoryView; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Update a Memory

- Signature: `client.beta.memoryStores.memories.update(memoryID: string, params: MemoryUpdateParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemory = await client.beta.memoryStores.memories.update("memory_id", {
  memory_store_id: "memory_store_id"
});

console.log(betaManagedAgentsMemory.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory to update (`mem_...`). */
memoryID: string; // path parameter

interface MemoryUpdateParams {
  /** The ID of the memory store that holds the memory (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
  view?: BetaManagedAgentsMemoryView; // query parameter
  /** New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update). */
  content?: string | null;
  /** The new path of the memory, which renames it. Omit it to keep the current path. The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive. */
  path?: string | null; // minLength: 2, maxLength: 1024, pattern: ^(/[^/\u0000]+)+$
  /** The condition that the memory must meet for the update to apply. Omit it to update unconditionally. If the condition fails, the request fails with HTTP status 409. */
  precondition?: BetaManagedAgentsPrecondition;
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Types

```ts
interface BetaManagedAgentsPrecondition {
  type: "content_sha256";
  /** Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes. */
  content_sha256?: string; // pattern: ^[a-f0-9]{64}$
}
```

### Delete a Memory

- Signature: `client.beta.memoryStores.memories.delete(memoryID: string, params: MemoryDeleteParams, options?: RequestOptions): BetaManagedAgentsDeletedMemory`
- Endpoint: `DELETE /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemory = await client.beta.memoryStores.memories.delete(
  "memory_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsDeletedMemory.id);
```

#### Example response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

#### Parameters

```ts
/** The ID of the memory to delete (`mem_...`). */
memoryID: string; // path parameter

interface MemoryDeleteParams {
  /** The ID of the memory store that holds the memory (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally. If the hashes differ, the request fails with HTTP status 409 and nothing is deleted. */
  expected_content_sha256?: string; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=typescript) returns. Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=typescript) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#audit-memory-changes) to learn more about how long versions are kept. */
interface BetaManagedAgentsDeletedMemory {
  type: "memory_deleted";
  /** ID of the deleted memory (a `mem_...` value). */
  id: string;
}
```

## Memory Stores › Memory Versions

### List Memory Versions

- Signature: `client.beta.memoryStores.memoryVersions.list(memoryStoreID: string, params?: MemoryVersionListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsMemoryVersion>`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memory_versions`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryVersion of client.beta.memoryStores.memoryVersions.list(
  "memory_store_id"
)) {
  console.log(betaManagedAgentsMemoryVersion.id);
}
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory store whose version history to list (`memstore_...`). */
memoryStoreID: string; // path parameter

interface MemoryVersionListParams {
  /** Return only versions written with the API key that has this ID. */
  api_key_id?: string; // query parameter
  /** Return versions created at or after this time (inclusive). */
  "created_at[gte]"?: string; // query parameter, format: date-time
  /** Return versions created at or before this time (inclusive). */
  "created_at[lte]"?: string; // query parameter, format: date-time
  /** The maximum number of versions to return per page, from 1 to 100. Defaults to 20. With `view=full`, a page holds at most 20 versions. */
  limit?: number; // query parameter, format: int32
  /** Return only versions of the memory with this ID (`mem_...`). The filter still works after the memory is deleted. While that memory's versions are retained, the results include the version whose `operation` is `deleted`. */
  memory_id?: string; // query parameter
  /** Return only versions that record this kind of change. */
  operation?: BetaManagedAgentsMemoryVersionOperation; // query parameter
  /** The `next_page` value from a previous response, to get the next page. Omit it to get the first page. */
  page?: string; // query parameter
  /** Return only versions written by the service account with this ID (`svac_...`). */
  service_account_id?: string; // query parameter
  /** Return only versions written by the session with this ID. */
  session_id?: string; // query parameter
  /** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
  view?: BetaManagedAgentsMemoryView; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** One entry in a memory's history, recording a single change and who made it. Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#audit-memory-changes) to learn more about memory versions. */
interface BetaManagedAgentsMemoryVersion {
  type: "memory_version";
  /** Unique identifier for this version (a `memver_...` value). */
  id: string;
  /** When this version was written, in RFC 3339 format. */
  created_at: string; // format: date-time
  /** The ID of the memory that this version belongs to (`mem_...`). The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=typescript) to get the memory's retained versions, including its `deleted` version while the lineage is retained. */
  memory_id: string;
  /** ID of the memory store this version belongs to (a `memstore_...` value). */
  memory_store_id: string;
  /** The kind of mutation this version records: `created`, `modified`, or `deleted`. */
  operation: BetaManagedAgentsMemoryVersionOperation;
  /** The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set. */
  content?: string | null;
  /** Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise. */
  content_sha256?: string | null;
  /** Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise. */
  content_size_bytes?: number | null; // format: int32
  /** Who made this change to the memory, or `null` if the author wasn't recorded. Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it. You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=typescript) to learn more about where the change came from. */
  created_by?: BetaManagedAgentsActor;
  /** The memory's path at the time of this write. `null` if and only if `redacted_at` is set. */
  path?: string | null;
  /** When the version was redacted, in RFC 3339, or `null` if it hasn't been. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#redact-a-version) to learn more about redaction. */
  redacted_at?: string | null; // format: date-time
  /** Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability). */
  redacted_by?: BetaManagedAgentsActor;
}
```

#### Types

```ts
type BetaManagedAgentsMemoryVersionOperation =
  /** The memory was created. The first version in any memory's lineage. */
  | "created"
  /** The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`. */
  | "modified"
  /** The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash. */
  | "deleted";

type BetaManagedAgentsActor = BetaManagedAgentsSessionActor | BetaManagedAgentsAPIActor | BetaManagedAgentsUserActor | BetaManagedAgentsServiceAccountActor;

/** An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session. */
interface BetaManagedAgentsSessionActor {
  type: "session_actor";
  /** ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=typescript) for further provenance. */
  session_id: string; // minLength: 1
}

/** A direct caller of the public API, identified by the API key that authenticated the request. */
interface BetaManagedAgentsAPIActor {
  type: "api_actor";
  /** ID of the API key (an `apikey_...` value). This identifies the key, not the secret. */
  api_key_id: string; // minLength: 1
}

/** A human user, for example acting through the Anthropic Console. */
interface BetaManagedAgentsUserActor {
  type: "user_actor";
  /** ID of the user (a `user_...` value). */
  user_id: string; // minLength: 1
}

/** A workload authenticated as a service account, for example via Workload Identity Federation. */
interface BetaManagedAgentsServiceAccountActor {
  type: "service_account_actor";
  /** ID of the service account (a `svac_...` value). */
  service_account_id: string; // minLength: 1
}
```

### Retrieve a Memory Version

- Signature: `client.beta.memoryStores.memoryVersions.retrieve(memoryVersionID: string, params: MemoryVersionRetrieveParams, options?: RequestOptions): BetaManagedAgentsMemoryVersion`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.retrieve(
  "memory_version_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsMemoryVersion.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory version to retrieve (`memver_...`). */
memoryVersionID: string; // path parameter

interface MemoryVersionRetrieveParams {
  /** The ID of the memory store that holds the version (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
  view?: BetaManagedAgentsMemoryView; // query parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Redact a Memory Version

- Signature: `client.beta.memoryStores.memoryVersions.redact(memoryVersionID: string, params: MemoryVersionRedactParams, options?: RequestOptions): BetaManagedAgentsMemoryVersion`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.redact(
  "memory_version_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsMemoryVersion.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** The ID of the memory version to redact (`memver_...`). */
memoryVersionID: string; // path parameter

interface MemoryVersionRedactParams {
  /** The ID of the memory store that holds the version (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```
