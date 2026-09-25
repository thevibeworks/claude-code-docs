---
title: Models
url: https://platform.claude.com/docs/en/api/php/beta/models
---

# Models

## List Models

`$client->beta->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas, ?string workspaceID): Page<BetaModelInfo>`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->models->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
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
        "compaction": {
          "summarize": {
            "supported": true
          },
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

`$client->beta->models->retrieve(string modelID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaModelInfo`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID: string`

  Model identifier or alias.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaModelInfo = $client->beta->models->retrieve(
  'model_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaModelInfo);
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
    "compaction": {
      "summarize": {
        "supported": true
      },
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

- `class BetaCapabilitySupport`

  - `bool supported`

    Whether this capability is supported by the model.

### Beta Compaction Capability

- `class BetaCompactionCapability`

  - `BetaCapabilitySupport summarize`

    Whether the summarize compaction type is supported.

  - `bool supported`

    Whether this capability is supported by the model.

### Beta Context Management Capability

- `class BetaContextManagementCapability`

  - `?BetaCapabilitySupport clearThinking20251015`

    Whether the clear_thinking_20251015 strategy is supported.

  - `?BetaCapabilitySupport clearToolUses20250919`

    Whether the clear_tool_uses_20250919 strategy is supported.

  - `?BetaCapabilitySupport compact20260112`

    Whether the compact_20260112 strategy is supported.

  - `bool supported`

    Whether this capability is supported by the model.

### Beta Effort Capability

- `class BetaEffortCapability`

  - `BetaCapabilitySupport high`

    Whether the model supports high effort level.

  - `BetaCapabilitySupport low`

    Whether the model supports low effort level.

  - `BetaCapabilitySupport max`

    Whether the model supports max effort level.

  - `BetaCapabilitySupport medium`

    Whether the model supports medium effort level.

  - `bool supported`

    Whether this capability is supported by the model.

  - `?BetaCapabilitySupport xhigh`

    Whether the model supports xhigh effort level.

### Beta Model Capabilities

- `class BetaModelCapabilities`

  - `BetaCapabilitySupport batch`

    Whether the model supports the Batch API.

  - `BetaCapabilitySupport citations`

    Whether the model supports citation generation.

  - `BetaCapabilitySupport codeExecution`

    Whether the model supports code execution tools.

  - `?BetaCompactionCapability compaction`

    Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

  - `BetaContextManagementCapability contextManagement`

    Context management support and available strategies.

  - `BetaEffortCapability effort`

    Effort (reasoning_effort) support and available levels.

  - `BetaCapabilitySupport imageInput`

    Whether the model accepts image content blocks.

  - `BetaCapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

  - `BetaCapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `BetaThinkingCapability thinking`

    Thinking capability and supported type configurations.

### Beta Model Info

- `class BetaModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?list<string> allowedFallbackModels`

    Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

  - `?BetaModelCapabilities capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

### Beta Thinking Capability

- `class BetaThinkingCapability`

  - `bool supported`

    Whether this capability is supported by the model.

  - `BetaThinkingTypes types`

    Supported thinking type configurations.

### Beta Thinking Types

- `class BetaThinkingTypes`

  - `BetaCapabilitySupport adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

  - `BetaCapabilitySupport enabled`

    Whether the model supports thinking with type 'enabled'.
