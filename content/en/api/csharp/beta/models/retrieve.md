# Get a Model

`BetaModelInfo Beta.Models.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

## Parameters

- `ModelRetrieveParams parameters`

  - `required string modelID`

    Model identifier or alias.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

## Returns

- `class BetaModelInfo:`

  - `required string ID`

    Unique model identifier.

  - `required IReadOnlyList<string>? AllowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `required BetaModelCapabilities? Capabilities`

    Model capability information.

    - `required BetaCapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport Citations`

      Whether the model supports citation generation.

    - `required BetaCapabilitySupport CodeExecution`

      Whether the model supports code execution tools.

    - `required BetaContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required BetaCapabilitySupport? ClearThinking20251015`

        Indicates whether a capability is supported.

      - `required BetaCapabilitySupport? ClearToolUses20250919`

        Indicates whether a capability is supported.

      - `required BetaCapabilitySupport? Compact20260112`

        Indicates whether a capability is supported.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required BetaEffortCapability Effort`

      Effort (reasoning_effort) support and available levels.

      - `required BetaCapabilitySupport High`

        Whether the model supports high effort level.

      - `required BetaCapabilitySupport Low`

        Whether the model supports low effort level.

      - `required BetaCapabilitySupport Max`

        Whether the model supports max effort level.

      - `required BetaCapabilitySupport Medium`

        Whether the model supports medium effort level.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required BetaCapabilitySupport? Xhigh`

        Indicates whether a capability is supported.

    - `required BetaCapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

    - `required BetaCapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

    - `required BetaCapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `required BetaThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required BetaThinkingTypes Types`

        Supported thinking type configurations.

        - `required BetaCapabilitySupport Adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `required BetaCapabilitySupport Enabled`

          Whether the model supports thinking with type 'enabled'.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `required string DisplayName`

    A human-readable name for the model.

  - `required long? MaxInputTokens`

    Maximum input context window size in tokens for this model.

  - `required long? MaxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `JsonElement Type = "model"`

    Object type.

    For Models, this is always `"model"`.

## Example

```csharp
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var betaModelInfo = await client.Beta.Models.Retrieve(parameters);

Console.WriteLine(betaModelInfo);
```

### Response (200)

```json
{
  "id": "claude-opus-5",
  "allowed_fallback_models": [
    "string"
  ],
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
    "structured_outputs": {
      "supported": true
    },
    "thinking": {
      "supported": true,
      "types": {
        "adaptive": {
          "supported": true
        },
        "enabled": {
          "supported": true
        }
      }
    }
  },
  "created_at": "2026-07-24T00:00:00Z",
  "display_name": "Claude Opus 5",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "type": "model"
}
```
