# Models

## List Models

`ModelListPage Models.List(parameters, cancellationToken = default)`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `ModelListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class ModelInfo:`

  - `required string ID`

    Unique model identifier.

  - `required ModelCapabilities? Capabilities`

    Model capability information.

    - `required CapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required CapabilitySupport Citations`

      Whether the model supports citation generation.

    - `required CapabilitySupport CodeExecution`

      Whether the model supports code execution tools.

    - `required ContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required CapabilitySupport? ClearThinking20251015`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? ClearToolUses20250919`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? Compact20260112`

        Indicates whether a capability is supported.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required EffortCapability Effort`

      Effort (reasoning_effort) support and available levels.

      - `required CapabilitySupport High`

        Whether the model supports high effort level.

      - `required CapabilitySupport Low`

        Whether the model supports low effort level.

      - `required CapabilitySupport Max`

        Whether the model supports max effort level.

      - `required CapabilitySupport Medium`

        Whether the model supports medium effort level.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required CapabilitySupport? Xhigh`

        Indicates whether a capability is supported.

    - `required CapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

    - `required CapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

    - `required CapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `required ThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required ThinkingTypes Types`

        Supported thinking type configurations.

        - `required CapabilitySupport Adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `required CapabilitySupport Enabled`

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

### Example

```csharp
ModelListParams parameters = new();

var page = await client.Models.List(parameters);
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get a Model

`ModelInfo Models.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

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

### Returns

- `class ModelInfo:`

  - `required string ID`

    Unique model identifier.

  - `required ModelCapabilities? Capabilities`

    Model capability information.

    - `required CapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required CapabilitySupport Citations`

      Whether the model supports citation generation.

    - `required CapabilitySupport CodeExecution`

      Whether the model supports code execution tools.

    - `required ContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required CapabilitySupport? ClearThinking20251015`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? ClearToolUses20250919`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? Compact20260112`

        Indicates whether a capability is supported.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required EffortCapability Effort`

      Effort (reasoning_effort) support and available levels.

      - `required CapabilitySupport High`

        Whether the model supports high effort level.

      - `required CapabilitySupport Low`

        Whether the model supports low effort level.

      - `required CapabilitySupport Max`

        Whether the model supports max effort level.

      - `required CapabilitySupport Medium`

        Whether the model supports medium effort level.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required CapabilitySupport? Xhigh`

        Indicates whether a capability is supported.

    - `required CapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

    - `required CapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

    - `required CapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `required ThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required ThinkingTypes Types`

        Supported thinking type configurations.

        - `required CapabilitySupport Adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `required CapabilitySupport Enabled`

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

### Example

```csharp
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var modelInfo = await client.Models.Retrieve(parameters);

Console.WriteLine(modelInfo);
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

## Domain types

### Capability Support

- `class CapabilitySupport:`

  Indicates whether a capability is supported.

  - `required bool Supported`

    Whether this capability is supported by the model.

### Context Management Capability

- `class ContextManagementCapability:`

  Context management capability details.

  - `required CapabilitySupport? ClearThinking20251015`

    Indicates whether a capability is supported.

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required CapabilitySupport? ClearToolUses20250919`

    Indicates whether a capability is supported.

  - `required CapabilitySupport? Compact20260112`

    Indicates whether a capability is supported.

  - `required bool Supported`

    Whether this capability is supported by the model.

### Effort Capability

- `class EffortCapability:`

  Effort (reasoning_effort) capability details.

  - `required CapabilitySupport High`

    Whether the model supports high effort level.

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required CapabilitySupport Low`

    Whether the model supports low effort level.

  - `required CapabilitySupport Max`

    Whether the model supports max effort level.

  - `required CapabilitySupport Medium`

    Whether the model supports medium effort level.

  - `required bool Supported`

    Whether this capability is supported by the model.

  - `required CapabilitySupport? Xhigh`

    Indicates whether a capability is supported.

### Model Capabilities

- `class ModelCapabilities:`

  Model capability information.

  - `required CapabilitySupport Batch`

    Whether the model supports the Batch API.

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required CapabilitySupport Citations`

    Whether the model supports citation generation.

  - `required CapabilitySupport CodeExecution`

    Whether the model supports code execution tools.

  - `required ContextManagementCapability ContextManagement`

    Context management support and available strategies.

    - `required CapabilitySupport? ClearThinking20251015`

      Indicates whether a capability is supported.

    - `required CapabilitySupport? ClearToolUses20250919`

      Indicates whether a capability is supported.

    - `required CapabilitySupport? Compact20260112`

      Indicates whether a capability is supported.

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required EffortCapability Effort`

    Effort (reasoning_effort) support and available levels.

    - `required CapabilitySupport High`

      Whether the model supports high effort level.

    - `required CapabilitySupport Low`

      Whether the model supports low effort level.

    - `required CapabilitySupport Max`

      Whether the model supports max effort level.

    - `required CapabilitySupport Medium`

      Whether the model supports medium effort level.

    - `required bool Supported`

      Whether this capability is supported by the model.

    - `required CapabilitySupport? Xhigh`

      Indicates whether a capability is supported.

  - `required CapabilitySupport ImageInput`

    Whether the model accepts image content blocks.

  - `required CapabilitySupport PdfInput`

    Whether the model accepts PDF content blocks.

  - `required CapabilitySupport StructuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `required ThinkingCapability Thinking`

    Thinking capability and supported type configurations.

    - `required bool Supported`

      Whether this capability is supported by the model.

    - `required ThinkingTypes Types`

      Supported thinking type configurations.

      - `required CapabilitySupport Adaptive`

        Whether the model supports thinking with type 'adaptive' (auto).

      - `required CapabilitySupport Enabled`

        Whether the model supports thinking with type 'enabled'.

### Model Info

- `class ModelInfo:`

  - `required string ID`

    Unique model identifier.

  - `required ModelCapabilities? Capabilities`

    Model capability information.

    - `required CapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required CapabilitySupport Citations`

      Whether the model supports citation generation.

    - `required CapabilitySupport CodeExecution`

      Whether the model supports code execution tools.

    - `required ContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required CapabilitySupport? ClearThinking20251015`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? ClearToolUses20250919`

        Indicates whether a capability is supported.

      - `required CapabilitySupport? Compact20260112`

        Indicates whether a capability is supported.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required EffortCapability Effort`

      Effort (reasoning_effort) support and available levels.

      - `required CapabilitySupport High`

        Whether the model supports high effort level.

      - `required CapabilitySupport Low`

        Whether the model supports low effort level.

      - `required CapabilitySupport Max`

        Whether the model supports max effort level.

      - `required CapabilitySupport Medium`

        Whether the model supports medium effort level.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required CapabilitySupport? Xhigh`

        Indicates whether a capability is supported.

    - `required CapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

    - `required CapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

    - `required CapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `required ThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required ThinkingTypes Types`

        Supported thinking type configurations.

        - `required CapabilitySupport Adaptive`

          Whether the model supports thinking with type 'adaptive' (auto).

        - `required CapabilitySupport Enabled`

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

### Thinking Capability

- `class ThinkingCapability:`

  Thinking capability details.

  - `required bool Supported`

    Whether this capability is supported by the model.

  - `required ThinkingTypes Types`

    Supported thinking type configurations.

    - `required CapabilitySupport Adaptive`

      Whether the model supports thinking with type 'adaptive' (auto).

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required CapabilitySupport Enabled`

      Whether the model supports thinking with type 'enabled'.

### Thinking Types

- `class ThinkingTypes:`

  Supported thinking type configurations.

  - `required CapabilitySupport Adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required CapabilitySupport Enabled`

    Whether the model supports thinking with type 'enabled'.
