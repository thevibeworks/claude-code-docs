# List Models

`ModelListPage Models.List(parameters, cancellationToken = default)`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

## Parameters

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

## Returns

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

  - `JsonElement Type constant`

    Object type.

    For Models, this is always `"model"`.

## Example

```csharp
ModelListParams parameters = new();

var page = await client.Models.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

### Response (200)

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
