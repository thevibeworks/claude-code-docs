---
title: List Models
url: https://platform.claude.com/docs/en/api/csharp/models/list
---

# List Models

`ModelListPage Models.List(parameters, cancellationToken = default)`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

## Parameters

- `ModelListParams parameters`

  - `string afterID` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID` (query parameter)

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `IReadOnlyList<Lifecycle> lifecycle` (query parameter)

    Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

    maxItems: 3

    - `Active("active")`

    - `Deprecated("deprecated")`

    - `Retired("retired")`

  - `long limit` (query parameter)

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ModelInfo`

  - `JsonElement Type = "model"`

    Object type.

    For Models, this is always `"model"`.

  - `required string ID`

    Unique model identifier.

  - `required ModelCapabilities? Capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `required CapabilitySupport Batch`

      Whether the model supports the Batch API.

      - `required bool Supported`

        Whether this capability is supported by the model.

    - `required CapabilitySupport Citations`

      Whether the model supports citation generation.

    - `required CapabilitySupport CodeExecution`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `required ContextManagementCapability ContextManagement`

      Context management support and available strategies.

      - `required CapabilitySupport? ClearThinking20251015`

        Whether the clear_thinking_20251015 strategy is supported.

      - `required CapabilitySupport? ClearToolUses20250919`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `required CapabilitySupport? Compact20260112`

        Whether the compact_20260112 strategy is supported.

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

        Whether the model supports xhigh effort level.

    - `required CapabilitySupport ImageInput`

      Whether the model accepts image content blocks.

    - `required CapabilitySupport PdfInput`

      Whether the model accepts PDF content blocks.

    - `required ServerToolsCapability ServerTools`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `required CapabilitySupport CodeExecution`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required CapabilitySupport WebSearch`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `required CapabilitySupport StructuredOutputs`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `required ThinkingCapability Thinking`

      Thinking capability and supported type configurations.

      - `required bool Supported`

        Whether this capability is supported by the model.

      - `required ThinkingTypes Types`

        Supported thinking type configurations.

        - `required CapabilitySupport Adaptive`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `required CapabilitySupport BetweenTools`

          Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `required CapabilitySupport Disabled`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `required CapabilitySupport Enabled`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `required DateTimeOffset? DeprecatedAt`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `required string DisplayName`

    A human-readable name for the model.

  - `required Lifecycle Lifecycle`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    - `Active("active")`

    - `Deprecated("deprecated")`

    - `Retired("retired")`

  - `required ModelLine? Line`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `Haiku("haiku")`

    - `Sonnet("sonnet")`

    - `Opus("opus")`

    - `Fable("fable")`

    - `Mythos("mythos")`

  - `required long? MaxInputTokens`

    Maximum input context window size in tokens for this model.

  - `required long? MaxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

  - `required DateTimeOffset? RetiresAt`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

## Example

```csharp
using System;
using Anthropic.Models.Models;

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
      "id": "claude-opus-5-5",
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
            "between_tools": {
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
      "created_at": "2026-09-21T00:00:00Z",
      "deprecated_at": "2019-12-27T18:11:19.117Z",
      "display_name": "Claude Opus 5.5",
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
