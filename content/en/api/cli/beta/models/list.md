# List Models

`$ ant beta:models list`

**GET** `/v1/models`

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

## Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaListResponse_ModelInfo_: object`

  - `data: array of BetaModelInfo`

    - `id: string`

      Unique model identifier.

    - `allowed_fallback_models: array of string`

      Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

    - `capabilities: object`

      Model capability information.

      - `batch: object`

        Whether the model supports the Batch API.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `citations: object`

        Whether the model supports citation generation.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `code_execution: object`

        Whether the model supports code execution tools.

        - `supported: boolean`

          Whether this capability is supported by the model.

      - `context_management: object`

        Context management support and available strategies.

        - `clear_thinking_20251015: object`

          Indicates whether a capability is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `clear_tool_uses_20250919: object`

          Indicates whether a capability is supported.

          - `supported: boolean`

            Whether this capability is supported by the model.

        - `compact_20260112: object`

          Indicates whether a capability is supported.

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

          Indicates whether a capability is supported.

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

            Whether the model supports thinking with type 'adaptive' (auto).

            - `supported: boolean`

              Whether this capability is supported by the model.

          - `enabled: object`

            Whether the model supports thinking with type 'enabled'.

            - `supported: boolean`

              Whether this capability is supported by the model.

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

      format: date-time

    - `display_name: string`

      A human-readable name for the model.

    - `max_input_tokens: number`

      Maximum input context window size in tokens for this model.

    - `max_tokens: number`

      Maximum value for the `max_tokens` parameter when using this model.

    - `type: "model"`

      Object type.

      For Models, this is always `"model"`.

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
