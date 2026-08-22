---
title: Get Token Usage Over Time
url: https://platform.claude.com/docs/en/api/admin/analytics/usage/list
---

## Get Token Usage Over Time

**get** `/v1/organizations/analytics/usage_report`

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time bucket granularity.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `group_by: optional array of "context_window" or "inference_geo" or "model" or 4 more`

  Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"slack_channel_id"`

  - `"speed"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets per page. Defaults and caps vary by bucket_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

- `slack_channel_ids: optional array of string`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

- `speeds: optional array of "fast" or "standard"`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  - `"fast"`

  - `"standard"`

- `user_ids: optional array of string`

  Filter to specific users by tagged user ID.

### Returns

- `UsageBucket object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { ending_at, results, starting_at }`

    Time buckets for this page, oldest first: one per `bucket_width` interval, including intervals with no data (their `results` list is empty). A page holds at most `limit` buckets.

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

    - `results: array of object { cache_creation, cache_read_input_tokens, context_window, 10 more }`

      Rows for this time bucket. Empty when the bucket has no data; otherwise a single combined row when `group_by[]` is omitted, or one row per group (subject to the per-bucket group cap described on the `group_by[]` parameter).

      - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        The number of input tokens for cache creation.

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M" or null`

        Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "us" or null`

        Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

        - `"global"`

        - `"us"`

      - `model: string or null`

        Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-4-6`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

      - `output_tokens: number`

        The number of output tokens generated.

      - `product: string or null`

        Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

      - `rbac_group_id: string or null`

        RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

      - `requests: number or null`

        Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

      - `server_tool_use: object { web_search_requests }`

        Server-side tool usage metrics.

        - `web_search_requests: number`

          The number of web search requests made.

      - `slack_channel_id: string or null`

        Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

      - `speed: "fast" or "standard" or null`

        Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

        - `"fast"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

  - `data_refreshed_at: string or null`

    RFC 3339 timestamp of the export this response was served from. Null when no export yet covers any part of the requested range, in which case every bucket's `results` list is empty. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

    Whether another page is available. When true, pass `next_page` as the `page` parameter to fetch it.

  - `next_page: string or null`

    Opaque cursor for the next page, or null when `has_more` is false. Pass it as the `page` parameter, keeping the other parameters unchanged. A cursor can expire after the underlying data refreshes; the request then returns HTTP 410 and pagination must restart from the first page.

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-4-6",
          "output_tokens": 0,
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "uncached_input_tokens": 0
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```
