---
title: Redact a Memory Version
url: https://platform.claude.com/docs/en/api/go/beta/memory_stores/memory_versions/redact
---

# Redact a Memory Version

`client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a Memory Version

## Parameters

- `memoryVersionID string` (path parameter)

  The ID of the memory version to redact (`memver_...`).

- `params BetaMemoryStoreMemoryVersionRedactParams`

  - `MemoryStoreID string` (path parameter)

    The ID of the memory store that holds the version (`memstore_...`).

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

    - `const AnthropicBetaExperimentalClaudeTag2026_10_21 AnthropicBeta = "experimental-claude-tag-2026-10-21"`

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `type BetaManagedAgentsMemoryVersion`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=go#audit-memory-changes) to learn more about memory versions.

  - `Type MemoryVersion`

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `MemoryID string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=go) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

      The memory was created. The first version in any memory's lineage.

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `Content string Optional`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string Optional`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64 Optional`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `CreatedBy BetaManagedAgentsActorUnion Optional`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=go) to learn more about where the change came from.

    - `type BetaManagedAgentsSessionActor`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `Type SessionActor`

      - `SessionID string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=go) for further provenance.

        minLength: 1

    - `type BetaManagedAgentsAPIActor`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `Type APIActor`

      - `APIKeyID string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `type BetaManagedAgentsUserActor`

      A human user, for example acting through the Anthropic Console.

      - `Type UserActor`

      - `UserID string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `type BetaManagedAgentsServiceAccountActor`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `Type ServiceAccountActor`

      - `ServiceAccountID string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `Path string Optional`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time Optional`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=go#redact-a-version) to learn more about redaction.

    format: date-time

  - `RedactedBy BetaManagedAgentsActorUnion Optional`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

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
	betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Redact(
		context.TODO(),
		"memory_version_id",
		anthropic.BetaMemoryStoreMemoryVersionRedactParams{
			MemoryStoreID: "memory_store_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
```

### Response (200)

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
