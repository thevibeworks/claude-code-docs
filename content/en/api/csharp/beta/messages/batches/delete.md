---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/csharp/beta/messages/batches/delete
---

# Delete a Message Batch

`BetaDeletedMessageBatch Beta.Messages.Batches.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=csharp)

## Parameters

- `BatchDeleteParams parameters`

  - `required string messageBatchID` (path parameter)

    ID of the Message Batch.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    Optional header to specify the beta version(s) you want to use.

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

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

    - `AdminUserSignOut2026_10_08("admin-user-sign-out-2026-10-08")`

    - `MessageThreads2026_08_12("message-threads-2026-08-12")`

    - `AnalyticsUsageCost2026_08_24("analytics-usage-cost-2026-08-24")`

    - `ExperimentalClaudeTag2026_10_21("experimental-claude-tag-2026-10-21")`

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `FilesApi2025_04_14("files-api-2025-04-14")`

      **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `Skills2025_10_02("skills-2025-10-02")`

      **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaDeletedMessageBatch`

  - `JsonElement Type = "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `required string ID`

    ID of the Message Batch.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=csharp).

- `AnthropicClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `AnthropicOrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Example

```csharp
using System;
using Anthropic.Models.Beta.Messages.Batches;

BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var betaDeletedMessageBatch = await client.Beta.Messages.Batches.Delete(parameters);

Console.WriteLine(betaDeletedMessageBatch);
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
