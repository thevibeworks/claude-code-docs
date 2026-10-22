---
title: List Memories
url: https://platform.claude.com/docs/en/api/java/beta/memory_stores/memories/list
---

# List Memories

`MemoryListPage beta().memoryStores().memories().list(params = MemoryListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

## Parameters

- `MemoryListParams params`

  - `Optional<String> memoryStoreId` (path parameter)

    The ID of the memory store to list memories from (`memstore_...`).

  - `Optional<Long> depth` (query parameter)

    How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

    Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

    format: int32

  - `Optional<Long> limit` (query parameter)

    The maximum number of items to return per page, from 1 to 100. Defaults to 20.

    With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

    format: int32

  - `Optional<String> page` (query parameter)

    The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

  - `Optional<String> pathPrefix` (query parameter)

    Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

    Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

  - `Optional<BetaManagedAgentsMemoryView> view` (query parameter)

    Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

    With `full`, a page holds at most 20 items.

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsMemoryListItem: union`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=java) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `class BetaManagedAgentsMemory`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=java#view-and-edit-memories) to learn more about working with memories.

    - `JsonValue type = "memory"`

    - `String id`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `String contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `long contentSizeBytes`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `LocalDateTime createdAt`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `String memoryStoreId`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `String memoryVersionId`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=java#audit-memory-changes) to learn more about memory versions.

    - `String path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `LocalDateTime updatedAt`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `Optional<String> content`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=java) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `JsonValue type = "memory_prefix"`

    - `String path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.MemoryListPage;
import com.anthropic.models.beta.memorystores.memories.MemoryListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryListPage page = client.beta().memoryStores().memories().list("memory_store_id");
    }
}
```

### Response (200)

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
