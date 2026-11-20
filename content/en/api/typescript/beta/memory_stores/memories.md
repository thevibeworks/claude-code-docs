---
title: Memories
url: https://platform.claude.com/docs/en/api/typescript/beta/memory_stores/memories
---

# Memories

## Create a Memory

- Signature: `client.beta.memoryStores.memories.create(memoryStoreID: string, params: MemoryCreateParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memories`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

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

### Example response (200)

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

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

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

### Returns

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

### Types

```ts
/** Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations. With `full`, list operations return at most 20 items per page. */
type BetaManagedAgentsMemoryView =
  /** Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content. */
  | "basic"
  /** Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20. */
  | "full";

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
  | "ce-claude-code-managed-settings-2026-10-06"
  | "user-profiles-billing-2026-10-01"
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

## List Memories

- Signature: `client.beta.memoryStores.memories.list(memoryStoreID: string, params?: MemoryListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsMemoryListItem>`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memories`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

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

### Example response (200)

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

### Parameters

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

### Returns

```ts
/** One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`. */
type BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix;
```

### Types

```ts
/** A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) returns instead of the memories below the requested `depth`. It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`. */
interface BetaManagedAgentsMemoryPrefix {
  type: "memory_prefix";
  /** The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory. */
  path: string;
}
```

## Retrieve a Memory

- Signature: `client.beta.memoryStores.memories.retrieve(memoryID: string, params: MemoryRetrieveParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

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

### Example response (200)

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

### Parameters

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

## Update a Memory

- Signature: `client.beta.memoryStores.memories.update(memoryID: string, params: MemoryUpdateParams, options?: RequestOptions): BetaManagedAgentsMemory`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

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

### Example response (200)

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

### Parameters

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

### Types

```ts
/** Optional condition that must hold for an update to apply. When omitted, the update is unconditional. Asserts the current state of the memory being updated. When an update changes `path`, the precondition still refers to the memory's current content, not the destination path. Currently the only supported variant is `content_sha256`. */
interface BetaManagedAgentsPrecondition {
  type: "content_sha256";
  /** Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes. */
  content_sha256?: string; // pattern: ^[a-f0-9]{64}$
}
```

## Delete a Memory

- Signature: `client.beta.memoryStores.memories.delete(memoryID: string, params: MemoryDeleteParams, options?: RequestOptions): BetaManagedAgentsDeletedMemory`
- Endpoint: `DELETE /v1/memory_stores/{memory_store_id}/memories/{memory_id}`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

### Example request

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

### Example response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

### Parameters

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

### Returns

```ts
/** The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=typescript) returns. Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=typescript) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#audit-memory-changes) to learn more about how long versions are kept. */
interface BetaManagedAgentsDeletedMemory {
  type: "memory_deleted";
  /** ID of the deleted memory (a `mem_...` value). */
  id: string;
}
```

## Types

```ts
interface BetaManagedAgentsConflictErrorObject {
  type: "conflict_error";
  message?: string;
}

/** A precondition that applies an update only if the memory's current content has the hash in `content_sha256`. If the hashes differ, the request fails with HTTP status 409. Retrieve the memory and retry. If the memory already has exactly the requested `content` and `path`, the request succeeds even though the hashes differ. */
interface BetaManagedAgentsContentSha256Precondition {
  type: "content_sha256";
  /** Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes. */
  content_sha256?: string; // pattern: ^[a-f0-9]{64}$
}

type BetaManagedAgentsErrorObject = BetaInvalidRequestErrorObject | BetaAuthenticationErrorObject | BetaBillingErrorObject | BetaPermissionErrorObject | BetaNotFoundErrorObject | BetaRateLimitErrorObject | BetaGatewayTimeoutErrorObject | BetaAPIErrorObject | BetaOverloadedErrorObject | BetaManagedAgentsMemoryPreconditionFailedErrorObject | BetaManagedAgentsMemoryPathConflictErrorObject | BetaManagedAgentsConflictErrorObject;

/** The error returned with HTTP status 409 when you create or rename a memory and the path you give is already used by another memory or overlaps another memory's path. Two paths overlap when one is an ancestor of the other, such as `/notes` and `/notes/todo.md`. To free the path, rename or delete the memory that `conflicting_memory_id` references, then retry. To change that memory instead of creating a new one, update it. To handle the error in code, use `conflicting_path` and `conflicting_memory_id` instead of `message`. */
interface BetaManagedAgentsMemoryPathConflictErrorObject {
  type: "memory_path_conflict_error";
  /** The ID of the memory that blocked the write (`mem_...`), or an empty string if that memory can't be identified. Retry the request when it is empty. */
  conflicting_memory_id?: string;
  /** The path that blocked the write: the requested path, or the path of a memory that is an ancestor or descendant of it. */
  conflicting_path?: string;
  message?: string;
}

/** The error returned with HTTP status 409 when a request's precondition doesn't hold for the memory's current state, such as `precondition` on an update or `expected_content_sha256` on a delete. The error doesn't include the memory's current state. Retrieve the memory to see its current content and `content_sha256` before you retry. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#safe-content-edits-optimistic-concurrency) to learn more about safe content edits with content hash preconditions. */
interface BetaManagedAgentsMemoryPreconditionFailedErrorObject {
  type: "memory_precondition_failed_error";
  message?: string;
}

interface BetaInvalidRequestErrorObject {
  /** The broad category of the error. */
  type: "invalid_request_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Invalid request
}

interface BetaAuthenticationErrorObject {
  /** The broad category of the error. */
  type: "authentication_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Authentication error
}

interface BetaBillingErrorObject {
  /** The broad category of the error. */
  type: "billing_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Billing error
}

interface BetaPermissionErrorObject {
  /** The broad category of the error. */
  type: "permission_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Permission denied
}

interface BetaNotFoundErrorObject {
  /** The broad category of the error. */
  type: "not_found_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Not found
}

interface BetaRateLimitErrorObject {
  /** The broad category of the error. */
  type: "rate_limit_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Rate limited
}

interface BetaGatewayTimeoutErrorObject {
  /** The broad category of the error. */
  type: "timeout_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Request timeout
}

interface BetaAPIErrorObject {
  /** The broad category of the error. */
  type: "api_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Internal server error
}

interface BetaOverloadedErrorObject {
  /** The broad category of the error. */
  type: "overloaded_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Overloaded
}
```
