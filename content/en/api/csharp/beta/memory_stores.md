---
title: Memory Stores
url: https://platform.claude.com/docs/en/api/csharp/beta/memory_stores
---

# Memory Stores

## Create a Memory Store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Create(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores`

Create a Memory Store

### Parameters

- `MemoryStoreCreateParams parameters`

  - `required string name`

    The name of the memory store, 1 to 255 characters long, without control characters. Names don't have to be unique in a workspace.

    In a session, the store's directory under `/mnt/memory/` is based on this name. The name is lowercased and every run of characters other than ASCII letters and digits becomes one hyphen. The session's memory store resource gives the exact path in `mount_path`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#how-the-agent-accesses-memory) to learn more about how agents access memory stores.

    minLength: 1, maxLength: 255

  - `string description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

    maxLength: 1024

  - `IReadOnlyDictionary<string, string> metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to. The agent doesn't see them.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreCreateParams parameters = new() { Name = "x" };

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Create(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
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

`MemoryStoreListPage Beta.MemoryStores.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores`

List Memory Stores

### Parameters

- `MemoryStoreListParams parameters`

  - `DateTimeOffset createdAtGte` (query parameter)

    Return only memory stores created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte` (query parameter)

    Return only memory stores created at or before this time (inclusive).

    format: date-time

  - `bool includeArchived` (query parameter)

    When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `int limit` (query parameter)

    Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

    format: int32

  - `string page` (query parameter)

    The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreListParams parameters = new();

var page = await client.Beta.MemoryStores.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a Memory Store

### Parameters

- `MemoryStoreRetrieveParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to retrieve (`memstore_...`).

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
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

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Update(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a Memory Store

### Parameters

- `MemoryStoreUpdateParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to update (`memstore_...`).

    The request fails with HTTP status 400 if the store is archived.

  - `string? description`

    New description for the store, up to 1,024 characters. Pass an empty string to clear it.

    maxLength: 1024

  - `IReadOnlyDictionary<string, string>? metadata`

    Changes to apply to the memory store's metadata. Keys you leave out keep their values.

    Set a key to a string to add or replace it, or to `null` to remove it. After the change, the metadata can hold at most 16 key-value pairs. Keys are 1 to 64 characters long and values at most 512 characters.

  - `string? name`

    The new name of the memory store, 1 to 255 characters long, without control characters.

    Sessions created after the change use the new name for the store's directory under `/mnt/memory/`.

    minLength: 1, maxLength: 255

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Update(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
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

`BetaManagedAgentsDeletedMemoryStore Beta.MemoryStores.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a Memory Store

### Parameters

- `MemoryStoreDeleteParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to delete (`memstore_...`).

    Deleting a store also deletes all its memories and memory versions. It can't be undone.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `JsonElement Type = "memory_store_deleted"`

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsDeletedMemoryStore = await client.Beta.MemoryStores.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemoryStore);
```

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a Memory Store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Archive(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a Memory Store

### Parameters

- `MemoryStoreArchiveParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to archive (`memstore_...`).

    Archiving can't be undone. Archiving a store that is already archived returns it unchanged.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores;

MemoryStoreArchiveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Archive(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
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

- `class BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `JsonElement Type = "memory_store_deleted"`

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Beta Managed Agents Memory Store

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `JsonElement Type = "memory_store"`

  - `required string ID`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `required DateTimeOffset? ArchivedAt`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#archive-a-store) to learn more about archiving.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `required string Description`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required DateTimeOffset UpdatedAt`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

## Memory Stores › Memories

### Create a Memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Create(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

#### Parameters

- `MemoryCreateParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to create the memory in (`memstore_...`).

  - `required string? content`

    The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

    The maximum size is 100 kB (102,400 bytes).

  - `required string path`

    The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

    A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

    minLength: 2, maxLength: 1024

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

    With `full`, list operations return at most 20 items per page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#view-and-edit-memories) to learn more about working with memories.

  - `JsonElement Type = "memory"`

  - `required string ID`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required DateTimeOffset UpdatedAt`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.Memories;

MemoryCreateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    Content = "content",
    Path = "xx",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Create(parameters);

Console.WriteLine(betaManagedAgentsMemory);
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

`MemoryListPage Beta.MemoryStores.Memories.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

#### Parameters

- `MemoryListParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store to list memories from (`memstore_...`).

  - `int depth` (query parameter)

    How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

    Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

    format: int32

  - `int limit` (query parameter)

    The maximum number of items to return per page, from 1 to 100. Defaults to 20.

    With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

    format: int32

  - `string page` (query parameter)

    The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

  - `string pathPrefix` (query parameter)

    Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

    Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

    With `full`, a page holds at most 20 items.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryListItem: union`

  One item in a [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=csharp) response: a `memory`, or a `memory_prefix` marker when `depth` is `1`.

  - `class BetaManagedAgentsMemory`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#view-and-edit-memories) to learn more about working with memories.

    - `JsonElement Type = "memory"`

    - `required string ID`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `required string ContentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `required int ContentSizeBytes`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `required DateTimeOffset CreatedAt`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `required string MemoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `required string MemoryVersionID`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

    - `required string Path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `required DateTimeOffset UpdatedAt`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `string? Content`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=csharp) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `JsonElement Type = "memory_prefix"`

    - `required string Path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.Memories;

MemoryListParams parameters = new() { MemoryStoreID = "memory_store_id" };

var page = await client.Beta.MemoryStores.Memories.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a Memory

#### Parameters

- `MemoryRetrieveParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store that holds the memory (`memstore_...`).

  - `required string memoryID` (path parameter)

    The ID of the memory to retrieve (`mem_...`).

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

    With `full`, list operations return at most 20 items per page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#view-and-edit-memories) to learn more about working with memories.

  - `JsonElement Type = "memory"`

  - `required string ID`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required DateTimeOffset UpdatedAt`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.Memories;

MemoryRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemory);
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

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Update(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a Memory

#### Parameters

- `MemoryUpdateParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store that holds the memory (`memstore_...`).

  - `required string memoryID` (path parameter)

    The ID of the memory to update (`mem_...`).

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

    With `full`, list operations return at most 20 items per page.

  - `string? content`

    New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `string? path`

    The new path of the memory, which renames it. Omit it to keep the current path.

    The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

    minLength: 2, maxLength: 1024

  - `BetaManagedAgentsPrecondition precondition`

    The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

    If the condition fails, the request fails with HTTP status 409.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemory`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#view-and-edit-memories) to learn more about working with memories.

  - `JsonElement Type = "memory"`

  - `required string ID`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required DateTimeOffset UpdatedAt`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.Memories;

MemoryUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Update(parameters);

Console.WriteLine(betaManagedAgentsMemory);
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

`BetaManagedAgentsDeletedMemory Beta.MemoryStores.Memories.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

#### Parameters

- `MemoryDeleteParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store that holds the memory (`memstore_...`).

  - `required string memoryID` (path parameter)

    The ID of the memory to delete (`mem_...`).

  - `string expectedContentSha256` (query parameter)

    Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

    If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsDeletedMemory`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=csharp) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=csharp) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about how long versions are kept.

  - `JsonElement Type = "memory_deleted"`

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.Memories;

MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
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

`MemoryVersionListPage Beta.MemoryStores.MemoryVersions.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List Memory Versions

#### Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store whose version history to list (`memstore_...`).

  - `string apiKeyID` (query parameter)

    Return only versions written with the API key that has this ID.

  - `DateTimeOffset createdAtGte` (query parameter)

    Return versions created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte` (query parameter)

    Return versions created at or before this time (inclusive).

    format: date-time

  - `int limit` (query parameter)

    The maximum number of versions to return per page, from 1 to 100. Defaults to 20.

    With `view=full`, a page holds at most 20 versions.

    format: int32

  - `string memoryID` (query parameter)

    Return only versions of the memory with this ID (`mem_...`).

    The filter still works after the memory is deleted. While that memory's versions are retained, the results include the version whose `operation` is `deleted`.

  - `BetaManagedAgentsMemoryVersionOperation operation` (query parameter)

    Return only versions that record this kind of change.

  - `string page` (query parameter)

    The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

  - `string serviceAccountID` (query parameter)

    Return only versions written by the service account with this ID (`svac_...`).

  - `string sessionID` (query parameter)

    Return only versions written by the session with this ID.

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

    With `full`, list operations return at most 20 items per page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `JsonElement Type = "memory_version"`

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `required string MemoryID`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=csharp) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `Created("created")`

      The memory was created. The first version in any memory's lineage.

    - `Modified("modified")`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `Deleted("deleted")`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) to learn more about where the change came from.

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `JsonElement Type = "session_actor"`

      - `required string SessionID`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsApiActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `JsonElement Type = "api_actor"`

      - `required string ApiKeyID`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `JsonElement Type = "user_actor"`

      - `required string UserID`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `JsonElement Type = "service_account_actor"`

      - `required string ServiceAccountID`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#redact-a-version) to learn more about redaction.

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.MemoryVersions;

MemoryVersionListParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var page = await client.Beta.MemoryStores.MemoryVersions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a Memory Version

#### Parameters

- `MemoryVersionRetrieveParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store that holds the version (`memstore_...`).

  - `required string memoryVersionID` (path parameter)

    The ID of the memory version to retrieve (`memver_...`).

  - `BetaManagedAgentsMemoryView view` (query parameter)

    Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

    With `full`, list operations return at most 20 items per page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `JsonElement Type = "memory_version"`

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `required string MemoryID`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=csharp) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `Created("created")`

      The memory was created. The first version in any memory's lineage.

    - `Modified("modified")`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `Deleted("deleted")`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) to learn more about where the change came from.

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `JsonElement Type = "session_actor"`

      - `required string SessionID`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsApiActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `JsonElement Type = "api_actor"`

      - `required string ApiKeyID`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `JsonElement Type = "user_actor"`

      - `required string UserID`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `JsonElement Type = "service_account_actor"`

      - `required string ServiceAccountID`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#redact-a-version) to learn more about redaction.

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.MemoryVersions;

MemoryVersionRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
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

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Redact(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a Memory Version

#### Parameters

- `MemoryVersionRedactParams parameters`

  - `required string memoryStoreID` (path parameter)

    The ID of the memory store that holds the version (`memstore_...`).

  - `required string memoryVersionID` (path parameter)

    The ID of the memory version to redact (`memver_...`).

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#audit-memory-changes) to learn more about memory versions.

  - `JsonElement Type = "memory_version"`

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `required string MemoryID`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=csharp) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `Created("created")`

      The memory was created. The first version in any memory's lineage.

    - `Modified("modified")`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `Deleted("deleted")`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) to learn more about where the change came from.

    - `class BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `JsonElement Type = "session_actor"`

      - `required string SessionID`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=csharp) for further provenance.

        minLength: 1

    - `class BetaManagedAgentsApiActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `JsonElement Type = "api_actor"`

      - `required string ApiKeyID`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `class BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `JsonElement Type = "user_actor"`

      - `required string UserID`

        ID of the user (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `JsonElement Type = "service_account_actor"`

      - `required string ServiceAccountID`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=csharp#redact-a-version) to learn more about redaction.

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```csharp
using System;
using Anthropic.Models.Beta.MemoryStores.MemoryVersions;

MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
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
