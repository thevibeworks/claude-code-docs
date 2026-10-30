---
title: List Memories
url: https://platform.claude.com/docs/en/api/go/beta/memory_stores/memories/list
---

# List Memories

`client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (*PageCursor[BetaManagedAgentsMemoryListItemUnion], error)`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

## Parameters

- `memoryStoreID string` (path parameter)

  The ID of the memory store to list memories from (`memstore_...`).

- `params BetaMemoryStoreMemoryListParams`

  - `Depth param.Opt[int64] Optional` (query parameter)

    How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

    Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

    format: int32

  - `Limit param.Opt[int64] Optional` (query parameter)

    The maximum number of items to return per page, from 1 to 100. Defaults to 20.

    With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

    format: int32

  - `Page param.Opt[string] Optional` (query parameter)

    The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

  - `PathPrefix param.Opt[string] Optional` (query parameter)

    Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

    Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

  - `View BetaManagedAgentsMemoryView Optional` (query parameter)

    Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

    With `full`, a page holds at most 20 items.

  - `Betas []AnthropicBeta Optional` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

    - `const AnthropicBetaTelemetryDestinations2026_08_11 AnthropicBeta = "telemetry-destinations-2026-08-11"`

    - `const AnthropicBetaWebhooks2026_10_07 AnthropicBeta = "webhooks-2026-10-07"`

    - `const AnthropicBetaMessageThreads2026_08_12 AnthropicBeta = "message-threads-2026-08-12"`

    - `const AnthropicBetaAnalyticsUsageCost2026_08_24 AnthropicBeta = "analytics-usage-cost-2026-08-24"`

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `type BetaManagedAgentsMemoryListItemUnion interface{…}`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=go) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `type BetaManagedAgentsMemory`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=go#view-and-edit-memories) to learn more about working with memories.

    - `Type Memory`

    - `ID string`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `ContentSha256 string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `ContentSizeBytes int64`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `CreatedAt Time`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `MemoryStoreID string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `MemoryVersionID string`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=go#audit-memory-changes) to learn more about memory versions.

    - `Path string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `UpdatedAt Time`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `Content string Optional`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `type BetaManagedAgentsMemoryPrefix`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=go) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `Type MemoryPrefix`

    - `Path string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go/v2"
	"github.com/anthropics/anthropic-sdk-go/v2/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.MemoryStores.Memories.List(
		context.TODO(),
		"memory_store_id",
		anthropic.BetaMemoryStoreMemoryListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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
