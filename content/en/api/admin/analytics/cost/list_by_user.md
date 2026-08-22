---
title: Get Per-User Cost
url: https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user
---

## Get Per-User Cost

**get** `/v1/organizations/analytics/user_cost_report`

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users
account for the most cost. Only cost attributable to a seat user is
included; for organization-wide totals including direct API-key and
automation traffic, use the bucketed
`/v1/organizations/analytics/cost_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

### Query Parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_windows: optional array of "0-200k" or "200k-1M"`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

- `exclude_deleted_users: optional boolean`

  If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

- `group_by: optional array of "context_window" or "cost_type" or "inference_geo" or 6 more`

  Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

  - `"context_window"`

  - `"cost_type"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"slack_channel_id"`

  - `"speed"`

  - `"token_type"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

- `order: optional "asc" or "desc"`

  Sort direction. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional "amount" or "list_amount"`

  Metric to rank actors by. Defaults to `amount`.

  - `"amount"`

  - `"list_amount"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of string`

  Product surfaces to include. Defaults to all products. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it.

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

- `UserCost object { data, data_refreshed_at, has_more, 2 more }`

  - `data: array of object { actor, amount, context_window, 13 more }`

    Rows for this page, ranked by `order_by` in the `order` direction. One row per user, or several per user when `group_by[]` or `bucket_width` breaks that user's usage or cost out across rows. Rows split out by `cost_type` or `token_type` (cost endpoint only) stay adjacent and are ranked as one unit.

    - `actor: AnalyticsUserActor`

      The user this row's usage or cost is attributed to. Always a `user_actor`.

      - `deleted: boolean`

        True when the user is no longer a member of the organization or its associated organizations: either their membership was removed (for example, deprovisioned via your identity provider) or the account itself has been deleted. The flag reflects organization membership, not account status. `name` and `email` stay populated for removed members; `name` is `"Deleted User"` and `email` null when the account has been deleted. The `user_id` is still populated for reconciliation.

      - `email: string or null`

        The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

      - `name: string or null`

        The user's current name, including for users who are no longer members of the organization or its associated organizations. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

      - `type: "user_actor"`

        Actor type. Always `"user_actor"`.

        - `"user_actor"`

      - `user_id: string`

        Tagged user ID.

    - `amount: string`

      Amount (post-discount, pre-credit) in fractional cents (minor units).

    - `context_window: "0-200k" or "200k-1M" or null`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `"0-200k"`

      - `"200k-1M"`

    - `cost_type: "code_execution" or "tokens" or "web_search" or null`

      Cost component breakdown; null when returning the combined total.

      - `"code_execution"`

      - `"tokens"`

      - `"web_search"`

    - `currency: "USD"`

      Currency code for the cost amount. Currently always `"USD"`.

      - `"USD"`

    - `ending_at: string or null`

      End of the row's UTC time bucket (exclusive), as an RFC 3339 timestamp; equal to `starting_at` plus one `bucket_width`. Null unless `bucket_width` is set.

    - `inference_geo: "global" or "us" or null`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `"global"`

      - `"us"`

    - `list_amount: string`

      List-price amount (pre-discount) in fractional cents.

    - `model: string or null`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-4-6`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `product: string or null`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude_code", "cowork", "office_agent", "claude_in_chrome", "claude_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

    - `rbac_group_id: string or null`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group_by.

    - `requests: number or null`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `slack_channel_id: string or null`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `speed: "fast" or "standard" or null`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `"fast"`

      - `"standard"`

    - `starting_at: string or null`

      Start of the row's UTC time bucket (inclusive), as an RFC 3339 timestamp. Null unless `bucket_width` is set; without `bucket_width`, each row aggregates the full requested range.

    - `token_type: "cache_creation.ephemeral_1h_input_tokens" or "cache_creation.ephemeral_5m_input_tokens" or "cache_read_input_tokens" or 2 more or null`

      Token type when cost_type=tokens; null otherwise.

      - `"cache_creation.ephemeral_1h_input_tokens"`

      - `"cache_creation.ephemeral_5m_input_tokens"`

      - `"cache_read_input_tokens"`

      - `"output_tokens"`

      - `"uncached_input_tokens"`

  - `data_refreshed_at: string or null`

    RFC 3339 timestamp of the export this response was served from. Null when no export yet covers any part of the requested range, in which case `data` is empty. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

  - `has_more: boolean`

    Whether another page is available. When true, pass `next_page` as the `page` parameter to fetch it.

  - `next_page: string or null`

    Opaque cursor for the next page, or null when `has_more` is false. Pass it as the `page` parameter, keeping the other parameters unchanged. A cursor can expire after the underlying data refreshes; the request then returns HTTP 410 and pagination must restart from the first page.

  - `organization_id: string`

    ID of the Organization.

### Example

```http
curl https://api.anthropic.com/v1/organizations/analytics/user_cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "amount": "41280.000000",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "claude-opus-4-6",
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "slack_channel_id": "C0123ABCDEF",
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```
