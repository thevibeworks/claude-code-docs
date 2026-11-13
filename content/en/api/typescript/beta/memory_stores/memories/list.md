---
title: List Memories
url: https://platform.claude.com/docs/en/api/typescript/beta/memory_stores/memories/list
---

# List Memories

- Signature: `client.beta.memoryStores.memories.list(memoryStoreID: string, params?: MemoryListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsMemoryListItem>`
- Endpoint: `GET /v1/memory_stores/{memory_store_id}/memories`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

## Example request

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

## Example response (200)

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

## Parameters

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

## Returns

```ts
/** One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`. */
type BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix;
```

## Types

```ts
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

/** A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=typescript) returns instead of the memories below the requested `depth`. It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`. */
interface BetaManagedAgentsMemoryPrefix {
  type: "memory_prefix";
  /** The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory. */
  path: string;
}
```
