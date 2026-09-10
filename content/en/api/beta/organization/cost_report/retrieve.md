---
title: Get Cost Report
url: https://platform.claude.com/docs/en/api/beta/organization/cost_report/retrieve
---

# Get Cost Report

**GET** `/v1/organizations/cost_report`

Get Cost Report

## Query parameters

- `starting_at: string`

  Time buckets that start on or after this RFC 3339 timestamp will be returned.
  Each time bucket will be snapped to the start of the minute/hour/day in UTC.

  format: date-time

- `bucket_width: optional "1d"`

  Time granularity of the response data.

  default: 1d

- `ending_at: optional string`

  Time buckets that end before this RFC 3339 timestamp will be returned.

  format: date-time

- `group_by: optional array of "description" or "workspace_id"`

  Group by any subset of the available options.

  - `"description"`

  - `"workspace_id"`

- `limit: optional number`

  Maximum number of time buckets to return in the response.

  default: 7, maximum: 31, minimum: 1

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 42 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"user-profiles-2026-09-04"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

## Returns

- `BetaCostReport object`

  - `data: array of object`

    List of time buckets for this page, oldest first: one per `bucket_width` interval, including intervals with no costs (their `results` list is empty). A page holds at most `limit` buckets.

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

      format: date-time

    - `results: array of object`

      List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

      - `amount: string`

        Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.

      - `context_window: "0-200k" or "200k-1M" or null`

        Input context window used. `null` if not grouping by description or for non-token costs.

        - `"0-200k"`

        - `"200k-1M"`

      - `cost_type: "code_execution" or "session_usage" or "tokens" or "web_search" or null`

        Type of cost. `null` if not grouping by description.

        - `"code_execution"`

        - `"session_usage"`

        - `"tokens"`

        - `"web_search"`

      - `currency: string`

        Currency code for the cost amount. Currently always `"USD"`.

      - `description: string or null`

        Description of the cost item. `null` if not grouping by description.

      - `inference_geo: "global" or "not_available" or "us" or null`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

        - `"global"`

        - `"not_available"`

        - `"us"`

      - `model: string or null`

        Model name used. `null` if not grouping by description or for non-token costs.

      - `service_tier: "batch" or "standard" or null`

        Service tier used. `null` if not grouping by description or for non-token costs.

        - `"batch"`

        - `"standard"`

      - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more or null`

        Type of token. `null` if not grouping by description or for non-token costs.

        - `"cache_creation.ephemeral_1h_input_tokens"`

        - `"cache_creation.ephemeral_5m_input_tokens"`

        - `"cache_read_input_tokens"`

        - `"output_tokens"`

        - `"uncached_input_tokens"`

      - `workspace_id: string or null`

        ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

      format: date-time

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string or null`

    Opaque cursor for the next page, or `null` when `has_more` is false. Pass it as the `page` parameter in the next request.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "amount": "123.78912",
          "context_window": "0-200k",
          "cost_type": "tokens",
          "currency": "USD",
          "description": "Claude Opus 5 Usage - Input Tokens",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "service_tier": "standard",
          "token_type": "uncached_input_tokens",
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
