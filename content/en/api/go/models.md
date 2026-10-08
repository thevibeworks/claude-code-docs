---
title: Models
url: https://platform.claude.com/docs/en/api/go/models
---

# Models

## List Models

`client.Models.List(ctx, params) (*Page[ModelInfo], error)`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `params ModelListParams`

  - `AfterID param.Opt[string] Optional` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `BeforeID param.Opt[string] Optional` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Lifecycle []string Optional` (query parameter)

    Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

    maxItems: 3

    - `const ModelListParamsLifecycleActive ModelListParamsLifecycle = "active"`

    - `const ModelListParamsLifecycleDeprecated ModelListParamsLifecycle = "deprecated"`

    - `const ModelListParamsLifecycleRetired ModelListParamsLifecycle = "retired"`

  - `Limit param.Opt[int64] Optional` (query parameter)

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `Betas []AnthropicBeta Optional` (header parameter)

    **Deprecated**: Deprecated. This parameter will be removed from this method in a future release. To use beta features, call the beta models methods (`client.beta.models`) instead.

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type ModelInfo`

  - `Type Model`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `ID string`

    Unique model identifier.

  - `Capabilities ModelCapabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `Batch CapabilitySupport`

      Whether the model supports the Batch API.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Citations CapabilitySupport`

      Whether the model supports citation generation.

    - `CodeExecution CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `ContextManagement ContextManagementCapability`

      Context management support and available strategies.

      - `ClearThinking20251015 CapabilitySupport`

        Whether the clear_thinking_20251015 strategy is supported.

      - `ClearToolUses20250919 CapabilitySupport`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Compact20260112 CapabilitySupport`

        Whether the compact_20260112 strategy is supported.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Effort EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `High CapabilitySupport`

        Whether the model supports high effort level.

      - `Low CapabilitySupport`

        Whether the model supports low effort level.

      - `Max CapabilitySupport`

        Whether the model supports max effort level.

      - `Medium CapabilitySupport`

        Whether the model supports medium effort level.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Xhigh CapabilitySupport`

        Whether the model supports xhigh effort level.

    - `ImageInput CapabilitySupport`

      Whether the model accepts image content blocks.

    - `PDFInput CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `ServerTools ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `CodeExecution CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `WebSearch CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `StructuredOutputs CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `Thinking ThinkingCapability`

      Thinking capability and supported type configurations.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Types ThinkingTypes`

        Supported thinking type configurations.

        - `Adaptive CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `Disabled CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `Enabled CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `DeprecatedAt Time`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `DisplayName string`

    A human-readable name for the model.

  - `Lifecycle ModelInfoLifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `const ModelInfoLifecycleActive ModelInfoLifecycle = "active"`

    - `const ModelInfoLifecycleDeprecated ModelInfoLifecycle = "deprecated"`

    - `const ModelInfoLifecycleRetired ModelInfoLifecycle = "retired"`

  - `Line ModelLine`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `const ModelLineHaiku ModelLine = "haiku"`

    - `const ModelLineSonnet ModelLine = "sonnet"`

    - `const ModelLineOpus ModelLine = "opus"`

    - `const ModelLineFable ModelLine = "fable"`

    - `const ModelLineMythos ModelLine = "mythos"`

  - `MaxInputTokens int64`

    Maximum input context window size in tokens for this model.

  - `MaxTokens int64`

    Maximum value for the `max_tokens` parameter when using this model.

  - `RetiresAt Time`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Models.List(context.TODO(), anthropic.ModelListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "claude-opus-5",
      "capabilities": {
        "batch": {
          "supported": true
        },
        "citations": {
          "supported": true
        },
        "code_execution": {
          "supported": true
        },
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          },
          "clear_tool_uses_20250919": {
            "supported": true
          },
          "compact_20260112": {
            "supported": true
          },
          "supported": true
        },
        "effort": {
          "high": {
            "supported": true
          },
          "low": {
            "supported": true
          },
          "max": {
            "supported": true
          },
          "medium": {
            "supported": true
          },
          "supported": true,
          "xhigh": {
            "supported": true
          }
        },
        "image_input": {
          "supported": true
        },
        "pdf_input": {
          "supported": true
        },
        "server_tools": {
          "code_execution": {
            "supported": true
          },
          "supported": true,
          "web_search": {
            "supported": true
          }
        },
        "structured_outputs": {
          "supported": true
        },
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            },
            "disabled": {
              "supported": true
            },
            "enabled": {
              "supported": true
            }
          }
        }
      },
      "created_at": "2026-07-24T00:00:00Z",
      "deprecated_at": "2019-12-27T18:11:19.117Z",
      "display_name": "Claude Opus 5",
      "lifecycle": "active",
      "line": "haiku",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "retires_at": "2019-12-27T18:11:19.117Z",
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get a Model

`client.Models.Get(ctx, modelID, query) (*ModelInfo, error)`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID string` (path parameter)

  Model identifier or alias.

- `query ModelGetParams`

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `Betas []AnthropicBeta Optional` (header parameter)

    **Deprecated**: Deprecated. This parameter will be removed from this method in a future release. To use beta features, call the beta models methods (`client.beta.models`) instead.

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type ModelInfo`

  - `Type Model`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `ID string`

    Unique model identifier.

  - `Capabilities ModelCapabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `Batch CapabilitySupport`

      Whether the model supports the Batch API.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Citations CapabilitySupport`

      Whether the model supports citation generation.

    - `CodeExecution CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `ContextManagement ContextManagementCapability`

      Context management support and available strategies.

      - `ClearThinking20251015 CapabilitySupport`

        Whether the clear_thinking_20251015 strategy is supported.

      - `ClearToolUses20250919 CapabilitySupport`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Compact20260112 CapabilitySupport`

        Whether the compact_20260112 strategy is supported.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Effort EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `High CapabilitySupport`

        Whether the model supports high effort level.

      - `Low CapabilitySupport`

        Whether the model supports low effort level.

      - `Max CapabilitySupport`

        Whether the model supports max effort level.

      - `Medium CapabilitySupport`

        Whether the model supports medium effort level.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Xhigh CapabilitySupport`

        Whether the model supports xhigh effort level.

    - `ImageInput CapabilitySupport`

      Whether the model accepts image content blocks.

    - `PDFInput CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `ServerTools ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `CodeExecution CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `WebSearch CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `StructuredOutputs CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `Thinking ThinkingCapability`

      Thinking capability and supported type configurations.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Types ThinkingTypes`

        Supported thinking type configurations.

        - `Adaptive CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `Disabled CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `Enabled CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `DeprecatedAt Time`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `DisplayName string`

    A human-readable name for the model.

  - `Lifecycle ModelInfoLifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `const ModelInfoLifecycleActive ModelInfoLifecycle = "active"`

    - `const ModelInfoLifecycleDeprecated ModelInfoLifecycle = "deprecated"`

    - `const ModelInfoLifecycleRetired ModelInfoLifecycle = "retired"`

  - `Line ModelLine`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `const ModelLineHaiku ModelLine = "haiku"`

    - `const ModelLineSonnet ModelLine = "sonnet"`

    - `const ModelLineOpus ModelLine = "opus"`

    - `const ModelLineFable ModelLine = "fable"`

    - `const ModelLineMythos ModelLine = "mythos"`

  - `MaxInputTokens int64`

    Maximum input context window size in tokens for this model.

  - `MaxTokens int64`

    Maximum value for the `max_tokens` parameter when using this model.

  - `RetiresAt Time`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	modelInfo, err := client.Models.Get(
		context.TODO(),
		"model_id",
		anthropic.ModelGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", modelInfo.ID)
}
```

#### Response (200)

```json
{
  "id": "claude-opus-5",
  "capabilities": {
    "batch": {
      "supported": true
    },
    "citations": {
      "supported": true
    },
    "code_execution": {
      "supported": true
    },
    "context_management": {
      "clear_thinking_20251015": {
        "supported": true
      },
      "clear_tool_uses_20250919": {
        "supported": true
      },
      "compact_20260112": {
        "supported": true
      },
      "supported": true
    },
    "effort": {
      "high": {
        "supported": true
      },
      "low": {
        "supported": true
      },
      "max": {
        "supported": true
      },
      "medium": {
        "supported": true
      },
      "supported": true,
      "xhigh": {
        "supported": true
      }
    },
    "image_input": {
      "supported": true
    },
    "pdf_input": {
      "supported": true
    },
    "server_tools": {
      "code_execution": {
        "supported": true
      },
      "supported": true,
      "web_search": {
        "supported": true
      }
    },
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "disabled": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-07-24T00:00:00Z",
  "deprecated_at": "2019-12-27T18:11:19.117Z",
  "display_name": "Claude Opus 5",
  "lifecycle": "active",
  "line": "haiku",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "retires_at": "2019-12-27T18:11:19.117Z",
  "type": "model"
}
```

## Domain types

### Capability Support

- `type CapabilitySupport`

  Indicates whether a capability is supported.

  - `Supported bool`

    Whether this capability is supported by the model.

### Context Management Capability

- `type ContextManagementCapability`

  Context management capability details.

  - `ClearThinking20251015 CapabilitySupport`

    Whether the clear_thinking_20251015 strategy is supported.

    - `Supported bool`

      Whether this capability is supported by the model.

  - `ClearToolUses20250919 CapabilitySupport`

    Whether the clear_tool_uses_20250919 strategy is supported.

  - `Compact20260112 CapabilitySupport`

    Whether the compact_20260112 strategy is supported.

  - `Supported bool`

    Whether this capability is supported by the model.

### Effort Capability

- `type EffortCapability`

  Effort (reasoning_effort) capability details.

  - `High CapabilitySupport`

    Whether the model supports high effort level.

    - `Supported bool`

      Whether this capability is supported by the model.

  - `Low CapabilitySupport`

    Whether the model supports low effort level.

  - `Max CapabilitySupport`

    Whether the model supports max effort level.

  - `Medium CapabilitySupport`

    Whether the model supports medium effort level.

  - `Supported bool`

    Whether this capability is supported by the model.

  - `Xhigh CapabilitySupport`

    Whether the model supports xhigh effort level.

### Model Capabilities

- `type ModelCapabilities`

  Model capability information.

  - `Batch CapabilitySupport`

    Whether the model supports the Batch API.

    - `Supported bool`

      Whether this capability is supported by the model.

  - `Citations CapabilitySupport`

    Whether the model supports citation generation.

  - `CodeExecution CapabilitySupport`

    Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

  - `ContextManagement ContextManagementCapability`

    Context management support and available strategies.

    - `ClearThinking20251015 CapabilitySupport`

      Whether the clear_thinking_20251015 strategy is supported.

    - `ClearToolUses20250919 CapabilitySupport`

      Whether the clear_tool_uses_20250919 strategy is supported.

    - `Compact20260112 CapabilitySupport`

      Whether the compact_20260112 strategy is supported.

    - `Supported bool`

      Whether this capability is supported by the model.

  - `Effort EffortCapability`

    Effort (reasoning_effort) support and available levels.

    - `High CapabilitySupport`

      Whether the model supports high effort level.

    - `Low CapabilitySupport`

      Whether the model supports low effort level.

    - `Max CapabilitySupport`

      Whether the model supports max effort level.

    - `Medium CapabilitySupport`

      Whether the model supports medium effort level.

    - `Supported bool`

      Whether this capability is supported by the model.

    - `Xhigh CapabilitySupport`

      Whether the model supports xhigh effort level.

  - `ImageInput CapabilitySupport`

    Whether the model accepts image content blocks.

  - `PDFInput CapabilitySupport`

    Whether the model accepts PDF content blocks.

  - `ServerTools ServerToolsCapability`

    Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

    - `CodeExecution CapabilitySupport`

      Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `Supported bool`

      Whether this capability is supported by the model.

    - `WebSearch CapabilitySupport`

      Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

  - `StructuredOutputs CapabilitySupport`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `Thinking ThinkingCapability`

    Thinking capability and supported type configurations.

    - `Supported bool`

      Whether this capability is supported by the model.

    - `Types ThinkingTypes`

      Supported thinking type configurations.

      - `Adaptive CapabilitySupport`

        Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `Disabled CapabilitySupport`

        Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

      - `Enabled CapabilitySupport`

        Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Model Info

- `type ModelInfo`

  - `Type Model`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `ID string`

    Unique model identifier.

  - `Capabilities ModelCapabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `Batch CapabilitySupport`

      Whether the model supports the Batch API.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Citations CapabilitySupport`

      Whether the model supports citation generation.

    - `CodeExecution CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `ContextManagement ContextManagementCapability`

      Context management support and available strategies.

      - `ClearThinking20251015 CapabilitySupport`

        Whether the clear_thinking_20251015 strategy is supported.

      - `ClearToolUses20250919 CapabilitySupport`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `Compact20260112 CapabilitySupport`

        Whether the compact_20260112 strategy is supported.

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Effort EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `High CapabilitySupport`

        Whether the model supports high effort level.

      - `Low CapabilitySupport`

        Whether the model supports low effort level.

      - `Max CapabilitySupport`

        Whether the model supports max effort level.

      - `Medium CapabilitySupport`

        Whether the model supports medium effort level.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Xhigh CapabilitySupport`

        Whether the model supports xhigh effort level.

    - `ImageInput CapabilitySupport`

      Whether the model accepts image content blocks.

    - `PDFInput CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `ServerTools ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `CodeExecution CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `WebSearch CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `StructuredOutputs CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `Thinking ThinkingCapability`

      Thinking capability and supported type configurations.

      - `Supported bool`

        Whether this capability is supported by the model.

      - `Types ThinkingTypes`

        Supported thinking type configurations.

        - `Adaptive CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `Disabled CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

        - `Enabled CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `DeprecatedAt Time`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `DisplayName string`

    A human-readable name for the model.

  - `Lifecycle ModelInfoLifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `const ModelInfoLifecycleActive ModelInfoLifecycle = "active"`

    - `const ModelInfoLifecycleDeprecated ModelInfoLifecycle = "deprecated"`

    - `const ModelInfoLifecycleRetired ModelInfoLifecycle = "retired"`

  - `Line ModelLine`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `const ModelLineHaiku ModelLine = "haiku"`

    - `const ModelLineSonnet ModelLine = "sonnet"`

    - `const ModelLineOpus ModelLine = "opus"`

    - `const ModelLineFable ModelLine = "fable"`

    - `const ModelLineMythos ModelLine = "mythos"`

  - `MaxInputTokens int64`

    Maximum input context window size in tokens for this model.

  - `MaxTokens int64`

    Maximum value for the `max_tokens` parameter when using this model.

  - `RetiresAt Time`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Model Line

- `type ModelLine string`

  A Claude model line, such as `opus` or `sonnet`. More lines may be added as new values.

  - `const ModelLineHaiku ModelLine = "haiku"`

  - `const ModelLineSonnet ModelLine = "sonnet"`

  - `const ModelLineOpus ModelLine = "opus"`

  - `const ModelLineFable ModelLine = "fable"`

  - `const ModelLineMythos ModelLine = "mythos"`

### Server Tools Capability

- `type ServerToolsCapability`

  Web search and code execution tool support, with one entry per tool.

  - `CodeExecution CapabilitySupport`

    Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `Supported bool`

      Whether this capability is supported by the model.

  - `Supported bool`

    Whether this capability is supported by the model.

  - `WebSearch CapabilitySupport`

    Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

### Thinking Capability

- `type ThinkingCapability`

  Thinking capability details.

  - `Supported bool`

    Whether this capability is supported by the model.

  - `Types ThinkingTypes`

    Supported thinking type configurations.

    - `Adaptive CapabilitySupport`

      Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `Supported bool`

        Whether this capability is supported by the model.

    - `Disabled CapabilitySupport`

      Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

    - `Enabled CapabilitySupport`

      Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Thinking Types

- `type ThinkingTypes`

  Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.

  - `Adaptive CapabilitySupport`

    Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

    - `Supported bool`

      Whether this capability is supported by the model.

  - `Disabled CapabilitySupport`

    Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

  - `Enabled CapabilitySupport`

    Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).
