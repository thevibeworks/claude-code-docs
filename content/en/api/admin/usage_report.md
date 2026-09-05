# Usage Report

## Get Messages Usage Report

**GET** `/v1/organizations/usage_report/messages`

Get Messages Usage Report

### Query parameters

- `starting_at: string`

  Time buckets that start on or after this RFC 3339 timestamp will be returned.
  Each time bucket will be snapped to the start of the minute/hour/day in UTC.

  format: date-time

- `account_ids: optional array of string`

  Restrict usage returned to the specified user account ID(s).

- `api_key_ids: optional array of string`

  Restrict usage returned to the specified API key ID(s).

- `bucket_width: optional "1d" or "1h" or "1m"`

  Time granularity of the response data.

  default: 1d

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `context_window: optional array of "0-200k" or "200k-1M"`

  Restrict usage returned to the specified context window(s).

  - `"0-200k"`

  - `"200k-1M"`

- `ending_at: optional string`

  Time buckets that end before this RFC 3339 timestamp will be returned.

  format: date-time

- `group_by: optional array of "account_id" or "api_key_id" or "context_window" or 6 more`

  Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

  - `"account_id"`

  - `"api_key_id"`

  - `"context_window"`

  - `"inference_geo"`

  - `"model"`

  - `"service_account_id"`

  - `"service_tier"`

  - `"speed"`

  - `"workspace_id"`

- `inference_geos: optional array of "global" or "not_available" or "us"`

  Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Maximum number of time buckets to return in the response.

  The default and max limits depend on `bucket_width`:
  • `"1d"`: Default of 7 days, maximum of 31 days
  • `"1h"`: Default of 24 hours, maximum of 168 hours
  • `"1m"`: Default of 60 minutes, maximum of 1440 minutes

- `models: optional array of string`

  Restrict usage returned to the specified model(s).

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

- `service_account_ids: optional array of string`

  Restrict usage returned to the specified service account ID(s).

- `service_tiers: optional array of "batch" or "flex" or "flex_discount" or 3 more`

  Restrict usage returned to the specified service tier(s).

  - `"batch"`

  - `"flex"`

  - `"flex_discount"`

  - `"priority"`

  - `"priority_on_demand"`

  - `"standard"`

- `speeds: optional array of "fast" or "standard"`

  Restrict usage returned to the specified speed(s) (Claude Code research preview).
  Requires the `fast-mode-2026-02-01` beta header.

  - `"fast"`

  - `"standard"`

- `workspace_ids: optional array of string`

  Restrict usage returned to the specified workspace ID(s).

### Headers

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `MessagesUsageReport object`

  - `data: array of object`

    List of time buckets for this page, oldest first: one per `bucket_width` interval, including intervals with no usage (their `results` list is empty). A page holds at most `limit` buckets.

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

      format: date-time

    - `results: array of object`

      List of usage items for this time bucket.  There may be multiple items if one or more `group_by[]` parameters are specified.

      - `account_id: string or null`

        ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

      - `api_key_id: string or null`

        ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

      - `cache_creation: object`

        The number of input tokens for cache creation.

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M" or null`

        Context window used. `null` if not grouping by context window.

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "not_available" or "us" or null`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

        - `"global"`

        - `"not_available"`

        - `"us"`

      - `model: string or null`

        Model used. `null` if not grouping by model.

      - `output_tokens: number`

        The number of output tokens generated.

      - `server_tool_use: object`

        Server-side tool usage metrics.

        - `web_search_requests: number`

          The number of web search requests made.

      - `service_account_id: string or null`

        ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

      - `service_tier: "batch" or "flex" or "flex_discount" or 3 more or null`

        Service tier used. `null` if not grouping by service tier.

        - `"batch"`

        - `"flex"`

        - `"flex_discount"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

      - `workspace_id: string or null`

        ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

      format: date-time

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string or null`

    Opaque cursor for the next page, or `null` when `has_more` is false. Pass it as the `page` parameter in the next request.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

#### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
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

## Get Claude Code Usage Report

**GET** `/v1/organizations/usage_report/claude_code`

Retrieve daily aggregated usage metrics for Claude Code users.
Enables organizations to analyze developer productivity and build custom dashboards.

### Query parameters

- `starting_at: string`

  UTC date in YYYY-MM-DD format. Returns metrics for this single day only.

  pattern: ^\d{4}-\d{2}-\d{2}$, format: date

- `limit: optional number`

  Number of records per page (default: 20, max: 1000).

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque cursor token from previous response's `next_page` field.

### Returns

- `ClaudeCodeUsageReport object`

  - `data: array of object`

    List of Claude Code usage records for the requested date.

    - `actor: object or object`

      The user or API key that performed the Claude Code actions.

      - `UserActor object`

        - `email_address: string`

          Email address of the user who performed Claude Code actions.

        - `type: "user_actor"`

          Actor type. Always `"user_actor"` for a user.

      - `APIActor object`

        - `api_key_name: string`

          Name of the API key used to perform Claude Code actions.

        - `type: "api_actor"`

          Actor type. Always `"api_actor"` for an API key.

    - `core_metrics: object`

      Core productivity metrics measuring Claude Code usage and impact.

      - `commits_by_claude_code: number`

        Number of git commits created through Claude Code's commit functionality.

      - `lines_of_code: object`

        Statistics on code changes made through Claude Code.

        - `added: number`

          Total number of lines of code added across all files by Claude Code.

        - `removed: number`

          Total number of lines of code removed across all files by Claude Code.

      - `num_sessions: number`

        Number of distinct Claude Code sessions initiated by this actor.

      - `pull_requests_by_claude_code: number`

        Number of pull requests created through Claude Code's PR functionality.

    - `customer_type: "api" or "subscription"`

      Type of customer account (api for API customers, subscription for Pro/Team customers).

      - `"api"`

      - `"subscription"`

    - `date: string`

      UTC day the usage metrics cover, as an RFC 3339 timestamp at midnight UTC
      (for example `2025-08-08T00:00:00Z`).

      format: date-time

    - `is_remote: boolean`

      Whether the usage came from remote Claude Code sessions, such as Claude Code
      on the web. Remote and local usage are reported as separate rows.

    - `model_breakdown: array of object`

      Token usage and cost breakdown by AI model used.

      - `estimated_cost: object`

        Estimated cost for using this model

        - `amount: number`

          Estimated cost amount in minor currency units (e.g., cents for USD).

        - `currency: string`

          Currency code for the estimated cost (e.g., 'USD').

      - `model: string`

        Name of the AI model used for Claude Code interactions.

      - `tokens: object`

        Token usage breakdown for this model

        - `cache_creation: number`

          Number of cache creation tokens consumed by this model.

        - `cache_read: number`

          Number of cache read tokens consumed by this model.

        - `input: number`

          Number of input tokens consumed by this model.

        - `output: number`

          Number of output tokens generated by this model.

    - `organization_id: string`

      ID of the organization that owns the Claude Code usage.

    - `terminal_type: string`

      Type of terminal or environment where Claude Code was used.

    - `tool_actions: map[object]`

      Breakdown of tool action acceptance and rejection rates by tool type.

      - `accepted: number`

        Number of tool action proposals that the user accepted.

      - `rejected: number`

        Number of tool action proposals that the user rejected.

    - `subscription_type: optional "enterprise" or "team" or null`

      Subscription tier for subscription customers. `null` for API customers.

      - `"enterprise"`

      - `"team"`

  - `has_more: boolean`

    True if there are more records available beyond the current page.

  - `next_page: string or null`

    Opaque cursor token for fetching the next page of results, or null if no more pages are available.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/usage_report/claude_code \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

#### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      },
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        },
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      },
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "is_remote": false,
      "model_breakdown": [
        {
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          },
          "model": "claude-opus-5",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          }
        },
        {
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          },
          "model": "claude-sonnet-5",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
          }
        }
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 0
        }
      },
      "subscription_type": "enterprise"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Domain types

### Claude Code Usage Report

- `ClaudeCodeUsageReport object`

  - `data: array of object`

    List of Claude Code usage records for the requested date.

    - `actor: object or object`

      The user or API key that performed the Claude Code actions.

      - `UserActor object`

        - `email_address: string`

          Email address of the user who performed Claude Code actions.

        - `type: "user_actor"`

          Actor type. Always `"user_actor"` for a user.

      - `APIActor object`

        - `api_key_name: string`

          Name of the API key used to perform Claude Code actions.

        - `type: "api_actor"`

          Actor type. Always `"api_actor"` for an API key.

    - `core_metrics: object`

      Core productivity metrics measuring Claude Code usage and impact.

      - `commits_by_claude_code: number`

        Number of git commits created through Claude Code's commit functionality.

      - `lines_of_code: object`

        Statistics on code changes made through Claude Code.

        - `added: number`

          Total number of lines of code added across all files by Claude Code.

        - `removed: number`

          Total number of lines of code removed across all files by Claude Code.

      - `num_sessions: number`

        Number of distinct Claude Code sessions initiated by this actor.

      - `pull_requests_by_claude_code: number`

        Number of pull requests created through Claude Code's PR functionality.

    - `customer_type: "api" or "subscription"`

      Type of customer account (api for API customers, subscription for Pro/Team customers).

      - `"api"`

      - `"subscription"`

    - `date: string`

      UTC day the usage metrics cover, as an RFC 3339 timestamp at midnight UTC
      (for example `2025-08-08T00:00:00Z`).

      format: date-time

    - `is_remote: boolean`

      Whether the usage came from remote Claude Code sessions, such as Claude Code
      on the web. Remote and local usage are reported as separate rows.

    - `model_breakdown: array of object`

      Token usage and cost breakdown by AI model used.

      - `estimated_cost: object`

        Estimated cost for using this model

        - `amount: number`

          Estimated cost amount in minor currency units (e.g., cents for USD).

        - `currency: string`

          Currency code for the estimated cost (e.g., 'USD').

      - `model: string`

        Name of the AI model used for Claude Code interactions.

      - `tokens: object`

        Token usage breakdown for this model

        - `cache_creation: number`

          Number of cache creation tokens consumed by this model.

        - `cache_read: number`

          Number of cache read tokens consumed by this model.

        - `input: number`

          Number of input tokens consumed by this model.

        - `output: number`

          Number of output tokens generated by this model.

    - `organization_id: string`

      ID of the organization that owns the Claude Code usage.

    - `terminal_type: string`

      Type of terminal or environment where Claude Code was used.

    - `tool_actions: map[object]`

      Breakdown of tool action acceptance and rejection rates by tool type.

      - `accepted: number`

        Number of tool action proposals that the user accepted.

      - `rejected: number`

        Number of tool action proposals that the user rejected.

    - `subscription_type: optional "enterprise" or "team" or null`

      Subscription tier for subscription customers. `null` for API customers.

      - `"enterprise"`

      - `"team"`

  - `has_more: boolean`

    True if there are more records available beyond the current page.

  - `next_page: string or null`

    Opaque cursor token for fetching the next page of results, or null if no more pages are available.

### Messages Usage Report

- `MessagesUsageReport object`

  - `data: array of object`

    List of time buckets for this page, oldest first: one per `bucket_width` interval, including intervals with no usage (their `results` list is empty). A page holds at most `limit` buckets.

    - `ending_at: string`

      End of the time bucket (exclusive) in RFC 3339 format.

      format: date-time

    - `results: array of object`

      List of usage items for this time bucket.  There may be multiple items if one or more `group_by[]` parameters are specified.

      - `account_id: string or null`

        ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

      - `api_key_id: string or null`

        ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.

      - `cache_creation: object`

        The number of input tokens for cache creation.

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

      - `context_window: "0-200k" or "200k-1M" or null`

        Context window used. `null` if not grouping by context window.

        - `"0-200k"`

        - `"200k-1M"`

      - `inference_geo: "global" or "not_available" or "us" or null`

        Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
        For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

        - `"global"`

        - `"not_available"`

        - `"us"`

      - `model: string or null`

        Model used. `null` if not grouping by model.

      - `output_tokens: number`

        The number of output tokens generated.

      - `server_tool_use: object`

        Server-side tool usage metrics.

        - `web_search_requests: number`

          The number of web search requests made.

      - `service_account_id: string or null`

        ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.

      - `service_tier: "batch" or "flex" or "flex_discount" or 3 more or null`

        Service tier used. `null` if not grouping by service tier.

        - `"batch"`

        - `"flex"`

        - `"flex_discount"`

        - `"priority"`

        - `"priority_on_demand"`

        - `"standard"`

      - `uncached_input_tokens: number`

        The number of uncached input tokens processed.

      - `workspace_id: string or null`

        ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

    - `starting_at: string`

      Start of the time bucket (inclusive) in RFC 3339 format.

      format: date-time

  - `has_more: boolean`

    Indicates if there are more results.

  - `next_page: string or null`

    Opaque cursor for the next page, or `null` when `has_more` is false. Pass it as the `page` parameter in the next request.
