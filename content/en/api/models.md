---
title: Models
url: https://platform.claude.com/docs/en/api/models
---

# Models

## List Models

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `lifecycle: optional array of "active" or "deprecated" or "retired"`

  Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

  maxItems: 3

  - `"active"`

  - `"deprecated"`

  - `"retired"`

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `data: array of ModelInfo`

  - `type: "model"`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `id: string`

    Unique model identifier.

  - `capabilities: ModelCapabilities or null`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: CapabilitySupport or null`

        Whether the clear_thinking_20251015 strategy is supported.

      - `clear_tool_uses_20250919: CapabilitySupport or null`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `compact_20260112: CapabilitySupport or null`

        Whether the compact_20260112 strategy is supported.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `xhigh: CapabilitySupport or null`

        Whether the model supports xhigh effort level.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `server_tools: ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `code_execution: CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `web_search: CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `between_tools: CapabilitySupport`

          Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `disabled: CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `enabled: CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `deprecated_at: string or null`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `display_name: string`

    A human-readable name for the model.

  - `lifecycle: "active" or "deprecated" or "retired"`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `"active"`

    - `"deprecated"`

    - `"retired"`

  - `line: ModelLine or null`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `"haiku"`

    - `"sonnet"`

    - `"opus"`

    - `"fable"`

    - `"mythos"`

  - `max_input_tokens: number or null`

    Maximum input context window size in tokens for this model.

  - `max_tokens: number or null`

    Maximum value for the `max_tokens` parameter when using this model.

  - `retires_at: string or null`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```bash
curl https://api.anthropic.com/v1/models \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

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
      "line": "opus",
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

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Path parameters

- `model_id: string`

  Model identifier or alias.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `ModelInfo object`

  - `type: "model"`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `id: string`

    Unique model identifier.

  - `capabilities: ModelCapabilities or null`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: CapabilitySupport or null`

        Whether the clear_thinking_20251015 strategy is supported.

      - `clear_tool_uses_20250919: CapabilitySupport or null`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `compact_20260112: CapabilitySupport or null`

        Whether the compact_20260112 strategy is supported.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `xhigh: CapabilitySupport or null`

        Whether the model supports xhigh effort level.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `server_tools: ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `code_execution: CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `web_search: CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `between_tools: CapabilitySupport`

          Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `disabled: CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `enabled: CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `deprecated_at: string or null`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `display_name: string`

    A human-readable name for the model.

  - `lifecycle: "active" or "deprecated" or "retired"`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `"active"`

    - `"deprecated"`

    - `"retired"`

  - `line: ModelLine or null`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `"haiku"`

    - `"sonnet"`

    - `"opus"`

    - `"fable"`

    - `"mythos"`

  - `max_input_tokens: number or null`

    Maximum input context window size in tokens for this model.

  - `max_tokens: number or null`

    Maximum value for the `max_tokens` parameter when using this model.

  - `retires_at: string or null`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/models/$MODEL_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
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
  "line": "opus",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "retires_at": "2019-12-27T18:11:19.117Z",
  "type": "model"
}
```

## Domain types

### Capability Support

- `CapabilitySupport object`

  Indicates whether a capability is supported.

  - `supported: boolean`

    Whether this capability is supported by the model.

### Context Management Capability

- `ContextManagementCapability object`

  Context management capability details.

  - `clear_thinking_20251015: CapabilitySupport or null`

    Whether the clear_thinking_20251015 strategy is supported.

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `clear_tool_uses_20250919: CapabilitySupport or null`

    Whether the clear_tool_uses_20250919 strategy is supported.

  - `compact_20260112: CapabilitySupport or null`

    Whether the compact_20260112 strategy is supported.

  - `supported: boolean`

    Whether this capability is supported by the model.

### Effort Capability

- `EffortCapability object`

  Effort (reasoning_effort) capability details.

  - `high: CapabilitySupport`

    Whether the model supports high effort level.

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `low: CapabilitySupport`

    Whether the model supports low effort level.

  - `max: CapabilitySupport`

    Whether the model supports max effort level.

  - `medium: CapabilitySupport`

    Whether the model supports medium effort level.

  - `supported: boolean`

    Whether this capability is supported by the model.

  - `xhigh: CapabilitySupport or null`

    Whether the model supports xhigh effort level.

### Model Capabilities

- `ModelCapabilities object`

  Model capability information.

  - `batch: CapabilitySupport`

    Whether the model supports the Batch API.

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `citations: CapabilitySupport`

    Whether the model supports citation generation.

  - `code_execution: CapabilitySupport`

    Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

  - `context_management: ContextManagementCapability`

    Context management support and available strategies.

    - `clear_thinking_20251015: CapabilitySupport or null`

      Whether the clear_thinking_20251015 strategy is supported.

    - `clear_tool_uses_20250919: CapabilitySupport or null`

      Whether the clear_tool_uses_20250919 strategy is supported.

    - `compact_20260112: CapabilitySupport or null`

      Whether the compact_20260112 strategy is supported.

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `effort: EffortCapability`

    Effort (reasoning_effort) support and available levels.

    - `high: CapabilitySupport`

      Whether the model supports high effort level.

    - `low: CapabilitySupport`

      Whether the model supports low effort level.

    - `max: CapabilitySupport`

      Whether the model supports max effort level.

    - `medium: CapabilitySupport`

      Whether the model supports medium effort level.

    - `supported: boolean`

      Whether this capability is supported by the model.

    - `xhigh: CapabilitySupport or null`

      Whether the model supports xhigh effort level.

  - `image_input: CapabilitySupport`

    Whether the model accepts image content blocks.

  - `pdf_input: CapabilitySupport`

    Whether the model accepts PDF content blocks.

  - `server_tools: ServerToolsCapability`

    Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

    - `code_execution: CapabilitySupport`

      Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `supported: boolean`

      Whether this capability is supported by the model.

    - `web_search: CapabilitySupport`

      Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

  - `structured_outputs: CapabilitySupport`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `thinking: ThinkingCapability`

    Thinking capability and supported type configurations.

    - `supported: boolean`

      Whether this capability is supported by the model.

    - `types: ThinkingTypes`

      Supported thinking type configurations.

      - `adaptive: CapabilitySupport`

        Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `between_tools: CapabilitySupport`

        Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

      - `disabled: CapabilitySupport`

        Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

      - `enabled: CapabilitySupport`

        Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Model Info

- `ModelInfo object`

  - `type: "model"`

    Object type.

    For Models, this is always `"model"`.

    default: model

  - `id: string`

    Unique model identifier.

  - `capabilities: ModelCapabilities or null`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

    - `batch: CapabilitySupport`

      Whether the model supports the Batch API.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `citations: CapabilitySupport`

      Whether the model supports citation generation.

    - `code_execution: CapabilitySupport`

      Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

    - `context_management: ContextManagementCapability`

      Context management support and available strategies.

      - `clear_thinking_20251015: CapabilitySupport or null`

        Whether the clear_thinking_20251015 strategy is supported.

      - `clear_tool_uses_20250919: CapabilitySupport or null`

        Whether the clear_tool_uses_20250919 strategy is supported.

      - `compact_20260112: CapabilitySupport or null`

        Whether the compact_20260112 strategy is supported.

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `effort: EffortCapability`

      Effort (reasoning_effort) support and available levels.

      - `high: CapabilitySupport`

        Whether the model supports high effort level.

      - `low: CapabilitySupport`

        Whether the model supports low effort level.

      - `max: CapabilitySupport`

        Whether the model supports max effort level.

      - `medium: CapabilitySupport`

        Whether the model supports medium effort level.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `xhigh: CapabilitySupport or null`

        Whether the model supports xhigh effort level.

    - `image_input: CapabilitySupport`

      Whether the model accepts image content blocks.

    - `pdf_input: CapabilitySupport`

      Whether the model accepts PDF content blocks.

    - `server_tools: ServerToolsCapability`

      Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

      - `code_execution: CapabilitySupport`

        Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `web_search: CapabilitySupport`

        Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `structured_outputs: CapabilitySupport`

      Whether the model supports structured output / JSON mode / strict tool schemas.

    - `thinking: ThinkingCapability`

      Thinking capability and supported type configurations.

      - `supported: boolean`

        Whether this capability is supported by the model.

      - `types: ThinkingTypes`

        Supported thinking type configurations.

        - `adaptive: CapabilitySupport`

          Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

        - `between_tools: CapabilitySupport`

          Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `disabled: CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `enabled: CapabilitySupport`

          Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

    format: date-time

  - `deprecated_at: string or null`

    RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

    format: date-time

  - `display_name: string`

    A human-readable name for the model.

  - `lifecycle: "active" or "deprecated" or "retired"`

    The model's current lifecycle stage.

    - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
    - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
    - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

    default: active

    - `"active"`

    - `"deprecated"`

    - `"retired"`

  - `line: ModelLine or null`

    The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

    - `"haiku"`

    - `"sonnet"`

    - `"opus"`

    - `"fable"`

    - `"mythos"`

  - `max_input_tokens: number or null`

    Maximum input context window size in tokens for this model.

  - `max_tokens: number or null`

    Maximum value for the `max_tokens` parameter when using this model.

  - `retires_at: string or null`

    RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

    format: date-time

### Model Line

- `ModelLine = "haiku" or "sonnet" or "opus" or 2 more`

  A Claude model line, such as `opus` or `sonnet`. More lines may be added as new values.

  - `"haiku"`

  - `"sonnet"`

  - `"opus"`

  - `"fable"`

  - `"mythos"`

### Server Tools Capability

- `ServerToolsCapability object`

  Web search and code execution tool support, with one entry per tool.

  - `code_execution: CapabilitySupport`

    Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `supported: boolean`

    Whether this capability is supported by the model.

  - `web_search: CapabilitySupport`

    Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

### Thinking Capability

- `ThinkingCapability object`

  Thinking capability details.

  - `supported: boolean`

    Whether this capability is supported by the model.

  - `types: ThinkingTypes`

    Supported thinking type configurations.

    - `adaptive: CapabilitySupport`

      Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

      - `supported: boolean`

        Whether this capability is supported by the model.

    - `between_tools: CapabilitySupport`

      Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

    - `disabled: CapabilitySupport`

      Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

    - `enabled: CapabilitySupport`

      Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

### Thinking Types

- `ThinkingTypes object`

  Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.

  - `adaptive: CapabilitySupport`

    Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

    - `supported: boolean`

      Whether this capability is supported by the model.

  - `between_tools: CapabilitySupport`

    Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

  - `disabled: CapabilitySupport`

    Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

  - `enabled: CapabilitySupport`

    Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).
