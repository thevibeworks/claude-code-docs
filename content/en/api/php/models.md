---
title: Models
url: https://platform.claude.com/docs/en/api/php/models
---

# Models

## List Models

`$client->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas, ?string workspaceID): Page<ModelInfo>`

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

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

- `betas?:optional list<AnthropicBeta>`

  **Deprecated**: Deprecated. This parameter will be removed from this method in a future release. To use beta features, call the beta models methods (`client.beta.models`) instead.

  Optional header to specify the beta version(s) you want to use.

### Returns

- `class ModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

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

$page = $client->models->list(
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

`$client->models->retrieve(string modelID, ?list<AnthropicBeta> betas, ?string workspaceID): ModelInfo`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

### Parameters

- `modelID: string`

  Model identifier or alias.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

- `betas?:optional list<AnthropicBeta>`

  **Deprecated**: Deprecated. This parameter will be removed from this method in a future release. To use beta features, call the beta models methods (`client.beta.models`) instead.

  Optional header to specify the beta version(s) you want to use.

### Returns

- `class ModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

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

$modelInfo = $client->models->retrieve(
  'model_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($modelInfo);
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

- `class CapabilitySupport`

  - `bool supported`

    Whether this capability is supported by the model.

### Context Management Capability

- `class ContextManagementCapability`

  - `?CapabilitySupport clearThinking20251015`

    Whether the clear_thinking_20251015 strategy is supported.

  - `?CapabilitySupport clearToolUses20250919`

    Whether the clear_tool_uses_20250919 strategy is supported.

  - `?CapabilitySupport compact20260112`

    Whether the compact_20260112 strategy is supported.

  - `bool supported`

    Whether this capability is supported by the model.

### Effort Capability

- `class EffortCapability`

  - `CapabilitySupport high`

    Whether the model supports high effort level.

  - `CapabilitySupport low`

    Whether the model supports low effort level.

  - `CapabilitySupport max`

    Whether the model supports max effort level.

  - `CapabilitySupport medium`

    Whether the model supports medium effort level.

  - `bool supported`

    Whether this capability is supported by the model.

  - `?CapabilitySupport xhigh`

    Whether the model supports xhigh effort level.

### Model Capabilities

- `class ModelCapabilities`

  - `CapabilitySupport batch`

    Whether the model supports the Batch API.

  - `CapabilitySupport citations`

    Whether the model supports citation generation.

  - `CapabilitySupport codeExecution`

    Whether the model supports code execution tools.

  - `ContextManagementCapability contextManagement`

    Context management support and available strategies.

  - `EffortCapability effort`

    Effort (reasoning_effort) support and available levels.

  - `CapabilitySupport imageInput`

    Whether the model accepts image content blocks.

  - `CapabilitySupport pdfInput`

    Whether the model accepts PDF content blocks.

  - `CapabilitySupport structuredOutputs`

    Whether the model supports structured output / JSON mode / strict tool schemas.

  - `ThinkingCapability thinking`

    Thinking capability and supported type configurations.

### Model Info

- `class ModelInfo`

  - `"model" type`

    Object type.

    For Models, this is always `"model"`.

  - `string id`

    Unique model identifier.

  - `?ModelCapabilities capabilities`

    Object mapping capability names to their support details. Keys are always present for all known capabilities.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

  - `string displayName`

    A human-readable name for the model.

  - `?int maxInputTokens`

    Maximum input context window size in tokens for this model.

  - `?int maxTokens`

    Maximum value for the `max_tokens` parameter when using this model.

### Thinking Capability

- `class ThinkingCapability`

  - `bool supported`

    Whether this capability is supported by the model.

  - `ThinkingTypes types`

    Supported thinking type configurations.

### Thinking Types

- `class ThinkingTypes`

  - `CapabilitySupport adaptive`

    Whether the model supports thinking with type 'adaptive' (auto).

  - `CapabilitySupport enabled`

    Whether the model supports thinking with type 'enabled'.
