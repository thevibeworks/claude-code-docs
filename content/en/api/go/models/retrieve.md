---
title: Get a Model
url: https://platform.claude.com/docs/en/api/go/models/retrieve
---

# Get a Model

`client.Models.Get(ctx, modelID, query) (*ModelInfo, error)`

**GET** `/v1/models/{model_id}`

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

## Parameters

- `modelID string` (path parameter)

  Model identifier or alias.

- `query ModelGetParams`

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

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

        - `BetweenTools CapabilitySupport`

          Whether the model accepts thinking with type 'between_tools' (thinking turned off, and any short progress updates the model writes between tool calls come back as thinking blocks). False exactly when a request that sends it gets a 400 from this model. A request that sends 'between_tools' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

        - `Disabled CapabilitySupport`

          Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking. A request that sends 'disabled' can still be rejected for another reason, such as an effort level the model does not allow with thinking off.

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

### Response (200)

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
  "line": "haiku",
  "max_input_tokens": 0,
  "max_tokens": 0,
  "retires_at": "2019-12-27T18:11:19.117Z",
  "type": "model"
}
```
