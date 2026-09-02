# Models

## List Models

`ModelListPage Beta.Models.List(parameters, cancellationToken = default)`

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

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

    - `MidConversationOutputConfig2026_07_01`

    - `ThinkingBindingControls2026_08_01`

    - `MidConversationSystemClearAt2026_08_21`

### Returns

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

  - `JsonElement Type constant`

    Object type.

    For Models, this is always `"model"`.

### Example

```csharp
ModelListParams parameters = new();

var page = await client.Beta.Models.List(parameters);
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get a Model

`BetaModelInfo Beta.Models.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `ModelRetrieveParams parameters`

  - `required string modelID`

    Model identifier or alias.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

    - `MidConversationOutputConfig2026_07_01`

    - `ThinkingBindingControls2026_08_01`

    - `MidConversationSystemClearAt2026_08_21`

### Returns

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

  - `JsonElement Type constant`

    Object type.

    For Models, this is always `"model"`.

### Example

```csharp
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var betaModelInfo = await client.Beta.Models.Retrieve(parameters);

Console.WriteLine(betaModelInfo);
```

#### Response (200)

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

## Domain types

### Beta Capability Support

- `class BetaCapabilitySupport:`

  Indicates whether a capability is supported.

  - `required bool Supported`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `class BetaContextManagementCapability:`

  Context management capability details.

  - `required BetaCapabilitySupport? ClearThinking20251015`

    Indicates whether a capability is supported.

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required BetaCapabilitySupport? ClearToolUses20250919`

    Indicates whether a capability is supported.

  - `required BetaCapabilitySupport? Compact20260112`

    Indicates whether a capability is supported.

  - `required bool Supported`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `class BetaEffortCapability:`

  Effort (reasoning_effort) capability details.

  - `required BetaCapabilitySupport High`

    Whether the model supports high effort level.

    - `required bool Supported`

      Whether this capability is supported by the model.

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

### Beta Model Capabilities

- `class BetaModelCapabilities:`

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

### Beta Model Info

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

  - `JsonElement Type constant`

    Object type.

    For Models, this is always `"model"`.

### Beta Thinking Capability

- `class BetaThinkingCapability:`

  Thinking capability details.

  - `required bool Supported`

    Whether this capability is supported by the model.

  - `required BetaThinkingTypes Types`

    Supported thinking type configurations.

    - `required BetaCapabilitySupport Adaptive`

      Whether the model supports thinking with type 'adaptive' (auto).

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required BetaCapabilitySupport Enabled`

      Whether the model supports thinking with type 'enabled'.

### Beta Thinking Types

- `class BetaThinkingTypes:`

  Supported thinking type configurations.

  - `required BetaCapabilitySupport Adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

    - `required bool Supported`

      Whether this capability is supported by the model.

  - `required BetaCapabilitySupport Enabled`

    Whether the model supports thinking with type 'enabled'.
