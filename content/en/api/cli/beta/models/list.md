---
title: List Models
url: https://platform.claude.com/docs/en/api/cli/beta/models/list
---

# List Models

`$ ant beta:models list`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

## Parameters

- `--after-id: optional string` (query parameter)

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string` (query parameter)

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--lifecycle: optional array of "active" or "deprecated" or "retired"` (query parameter)

  Filter the list to models in any of the given lifecycle stages (`active`, `deprecated`, or `retired`). Up to 3 values. When omitted, the list contains the `active` and `deprecated` models; `retired` models appear only when `retired` is requested explicitly.

  maxItems: 3

- `--limit: optional number` (query parameter)

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--beta: optional array of AnthropicBeta` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaListResponse_ModelInfo_: object`

  - `data: array of BetaModelInfo`

    - `type: "model"`

      Object type.

      For Models, this is always `"model"`.

    - `id: string`

      Unique model identifier.

    - `allowed_fallback_models: array of string`

      Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

    - `capabilities: object`

      Object mapping capability names to their support details. Keys are always present for all known capabilities.

      - `batch: object`

        Whether the model supports the Batch API.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `citations: object`

        Whether the model supports citation generation.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `code_execution: object`

        Whether code that the model runs in the code execution tool can call the request's other tools, as in programmatic tool calling and dynamic filtering for web search and web fetch. Support for the code execution tool itself is in `server_tools.code_execution`.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `compaction: object`

        Server-side compaction support (the top-level `compaction` parameter) and the accepted `compaction.type` values.

        - `summarize: object`

          Whether the summarize compaction type is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `context_management: object`

        Context management support and available strategies.

        - `clear_thinking_20251015: object`

          Whether the clear_thinking_20251015 strategy is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `clear_tool_uses_20250919: object`

          Whether the clear_tool_uses_20250919 strategy is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `compact_20260112: object`

          Whether the compact_20260112 strategy is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `effort: object`

        Effort (reasoning_effort) support and available levels.

        - `high: object`

          Whether the model supports high effort level.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `low: object`

          Whether the model supports low effort level.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `max: object`

          Whether the model supports max effort level.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `medium: object`

          Whether the model supports medium effort level.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `supported: boolean`

          Whether this capability is supported by the model.

        - `xhigh: object`

          Whether the model supports xhigh effort level.

          - `supported: boolean`

            Whether this capability is supported by the model.

      - `image_input: object`

        Whether the model accepts image content blocks.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `pdf_input: object`

        Whether the model accepts PDF content blocks.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `server_tools: object`

        Whether this model supports the web search and code execution server tools. `supported` is true when the model supports at least one of the tools. A supported tool can still be rejected for your organization, for example when an admin has turned web search off.

        - `code_execution: object`

          Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `supported: boolean`

          Whether this capability is supported by the model.

        - `web_search: object`

          Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

          - `supported: boolean`

            Whether this capability is supported by the model.

      - `structured_outputs: object`

        Whether the model supports structured output / JSON mode / strict tool schemas.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `thinking: object`

        Thinking capability and supported type configurations.

        - `supported: boolean`

          Whether this capability is supported by the model.

        - `types: object`

          Supported thinking type configurations.

          - `adaptive: object`

            Whether the model accepts thinking with type 'adaptive' (the model decides whether and how much to think).

            - `supported: boolean`

              Whether this capability is supported by the model.

          - `disabled: object`

            Whether the model accepts thinking with type 'disabled' (thinking turned off). False exactly when a request that sends it gets a 400 from this model. True on a model that does not support thinking.

            - `supported: boolean`

              Whether this capability is supported by the model.

          - `enabled: object`

            Whether the model accepts thinking with type 'enabled' (extended thinking with a caller-set `budget_tokens`).

            - `supported: boolean`

              Whether this capability is supported by the model.

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

      format: date-time

    - `deprecated_at: string`

      RFC 3339 datetime string representing the time of the model's most recent deprecation. Populated for `deprecated` and `retired` models; `null` while the model is `active`.

      format: date-time

    - `display_name: string`

      A human-readable name for the model.

    - `lifecycle: "active" or "deprecated" or "retired"`

      The model's current lifecycle stage.

      - `active`: The model is available for use, open to new adopters, and not scheduled for retirement.
      - `deprecated`: The model remains callable for organizations with existing access, but is headed for retirement and closed to new adopters.
      - `retired`: The model is no longer available for use; inference requests naming it fail. It remains in the catalogue as the historical record of its retirement.

      - `"active"`

      - `"deprecated"`

      - `"retired"`

    - `line: "haiku" or "sonnet" or "opus" or 2 more`

      The model line this model belongs to, such as `opus` for both Claude Opus 4.5 and Claude Opus 4.6. More lines may be added. `null` when the model belongs to no line; do not infer a line from the `id`.

      - `"haiku"`

      - `"sonnet"`

      - `"opus"`

      - `"fable"`

      - `"mythos"`

    - `max_input_tokens: number`

      Maximum input context window size in tokens for this model.

    - `max_tokens: number`

      Maximum value for the `max_tokens` parameter when using this model.

    - `retires_at: string`

      RFC 3339 datetime string representing the model's currently scheduled retirement date. The schedule can be revised until retirement occurs; `null` while the model is `active` or while no retirement is scheduled. A past date on a `deprecated` model means retirement is overdue, not that it has occurred: `lifecycle` is the retirement signal.

      format: date-time

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

## Example

```bash
ant beta:models list \
  --api-key my-anthropic-api-key
```

### Response (200)

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
