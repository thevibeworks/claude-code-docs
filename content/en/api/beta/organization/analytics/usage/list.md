---
title: Get Token Usage By Dimension
url: https://platform.claude.com/docs/en/api/beta/organization/analytics/usage/list
---

# Get Token Usage By Dimension

**GET** `/v1/organizations/analytics/usage`

Get token usage across a date range, broken out by dimension.

Returns one row per combination of the requested `group_by[]`
dimensions (and time bucket, when `time_bucket_width` is set) that has
usage in the range, ranked by the `order_by` metric or ordered by time
bucket; every combination is returned across pages. With no `group_by[]`
and no `time_bucket_width`, a single row aggregates the whole range.
Includes all usage, whether or not it is attributable to a seat user.
Requires an API key with the `read:analytics` scope, or an Admin API key.

## Query parameters

- `starting_at: string`

  Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

  format: date-time

- `actor_ids: optional array of string`

  Filter to usage attributed to specific identities, by tagged ID: a `user_...`, `svac_...` (service account), or `apikey_...` ID. An `apikey_` entry matches only usage attributed to the key itself, not usage on that key attributed to a user or service account (use `api_key_ids[]` for every request a key authenticated). Federated identities have no tagged ID; select them with `actor_types[]`. Use `group_by[]=actor` to break out per-identity values.

  maxItems: 100

- `actor_types: optional array of BetaAnalyticsActorType`

  Filter to usage attributed to specific kinds of identity. Use `group_by[]=actor_type` to break out per-kind values.

  maxItems: 100

  - `"api_actor"`

  - `"federated_actor"`

  - `"service_account_actor"`

  - `"user_actor"`

- `agent_ids: optional array of string`

  Filter to usage incurred by sessions of specific Claude Managed Agents agents. Use `group_by[]=agent_id` to break out per-agent values. Claude Developer Platform organizations only.

  maxItems: 100

- `api_key_ids: optional array of string`

  Filter to usage authenticated by specific API keys, by tagged API key ID (`apikey_...`), whichever identity the usage is attributed to. Include an empty entry (`api_key_ids[]=`) to also match usage that no API key authenticated. Use `group_by[]=api_key_id` to break out per-key values; usage without a key has a null `api_key_id`. Claude Developer Platform organizations only.

  maxItems: 100

- `claude_tag_categories: optional array of BetaAnalyticsClaudeTagCategory`

  Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude_tag`, so combining this filter with `products[]=claude_tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

  maxItems: 100

  - `"dm"`

  - `"engaged"`

  - `"monitoring"`

  - `"proactive"`

  - `"scheduled"`

- `claude_tag_user_ids: optional array of string`

  Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

  maxItems: 100

- `context_windows: optional array of BetaAnalyticsContextWindow`

  Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

  maxItems: 100

  - `"0-200k"`

  - `"200k-1M"`

- `deployment_ids: optional array of string`

  Filter to usage incurred by Claude Managed Agents sessions that specific deployments started. Use `group_by[]=deployment_id` to break out per-deployment values. Claude Developer Platform organizations only.

  maxItems: 100

- `ending_at: optional string`

  End of range, exclusive. Required when `time_bucket_width` is set. Without `time_bucket_width`, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

  format: date-time

- `environment_ids: optional array of string`

  Filter to usage incurred by Claude Managed Agents sessions that ran in specific environments. Use `group_by[]=environment_id` to break out per-environment values. Claude Developer Platform organizations only.

  maxItems: 100

- `exclude_deleted_users: optional boolean`

  If true, omit rows whose `actor` is a `user_actor` with `deleted: true`. Requires `group_by[]=actor`. Rows for other actor types, and rows whose `actor` is null, are always kept. A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

  default: false

- `group_by: optional array of BetaAnalyticsUsageGroupBy`

  Dimensions to break usage out by (at most 5): one row per combination of their values with usage in the range (and per time bucket, when `time_bucket_width` is set), every combination returned across pages rather than a capped top set. When omitted, a single row aggregates the whole range.

  maxItems: 100

  - `"actor"`

  - `"actor_type"`

  - `"agent_id"`

  - `"api_key_id"`

  - `"claude_tag_category"`

  - `"claude_tag_user_id"`

  - `"context_window"`

  - `"deployment_id"`

  - `"environment_id"`

  - `"inference_geo"`

  - `"model"`

  - `"product"`

  - `"rbac_group_id"`

  - `"service_tier"`

  - `"session_id"`

  - `"slack_channel_id"`

  - `"speed"`

  - `"user_profile_id"`

  - `"workspace_id"`

- `inference_geos: optional array of BetaAnalyticsInferenceGeoFilter`

  Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

  maxItems: 100

  - `"global"`

  - `"not_available"`

  - `"us"`

- `limit: optional number`

  Number of rows per page (1-1000, default 20). `cost_type`/`token_type` fan-out rows (cost endpoint only) do not count toward this limit, so `data` can exceed it.

  default: 20, minimum: 1, maximum: 1000

- `models: optional array of string`

  Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

  maxItems: 100

- `order: optional BetaAnalyticsUsageCostSortOrder`

  Sort direction of the `order_by` metric, or of the time buckets when `order_by` is `time` and `time_bucket_width` is set. Defaults to `desc`.

  - `"asc"`

  - `"desc"`

- `order_by: optional BetaAnalyticsUsageOrderBy`

  Row order. A metric ranks rows by that metric in the `order` direction. `time` orders rows by time bucket in the `order` direction (newest first by default) and, within a bucket, by `total_tokens`, highest first. `time` takes effect only with `time_bucket_width`; without it, `time` is the same as `total_tokens`. Defaults to `total_tokens`.

  - `"output_tokens"`

  - `"requests"`

  - `"time"`

  - `"total_tokens"`

  - `"uncached_input_tokens"`

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `products: optional array of BetaAnalyticsUsageCostProductFilter`

  Product surfaces to include. Defaults to all products.

  maxItems: 100

  - `"chat"`

  - `"chat_cowork_unified"`

  - `"claude_code"`

  - `"claude_console"`

  - `"claude_design"`

  - `"claude_in_chrome"`

  - `"claude_tag"`

  - `"cowork"`

  - `"managed_agents_api"`

  - `"message_batches_api"`

  - `"messages_api"`

  - `"office_agent"`

- `rbac_group_ids: optional array of string`

  Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

  maxItems: 100

- `service_tiers: optional array of BetaAnalyticsServiceTier`

  Filter to specific service tiers. Use `group_by[]=service_tier` to break out per-tier values. Claude Developer Platform organizations only; matches nothing for a Claude Enterprise organization.

  maxItems: 100

  - `"batch"`

  - `"flex"`

  - `"flex_discount"`

  - `"priority"`

  - `"priority_on_demand"`

  - `"standard"`

- `session_ids: optional array of string`

  Filter to usage incurred by specific Claude Managed Agents sessions, by tagged session ID (`sesn_...`). Use `group_by[]=session_id` to break out per-session values. Claude Developer Platform organizations only.

  maxItems: 100

- `slack_channel_ids: optional array of string`

  Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

  maxItems: 100

- `speeds: optional array of BetaAnalyticsSpeed`

  Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

  maxItems: 100

  - `"fast"`

  - `"standard"`

- `time_bucket_width: optional BetaAnalyticsTimeBucketWidth`

  Time-bucket granularity. When set, rows are returned per time bucket (one per bucket and dimension combination with usage) and each row's `starting_at` and `ending_at` are that bucket's bounds; the time bucket counts toward `limit`. `ending_at` is required when `time_bucket_width` is set, and with `time_bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the requested range with `starting_at` and `ending_at` each rounded down to the hour.

  - `"1d"`

  - `"1h"`

  - `"1m"`

- `user_profile_ids: optional array of string`

  Filter to usage attributed to specific user profiles, by tagged user profile ID (`uprof_...`). Use `group_by[]=user_profile_id` to break out per-profile values. Claude Developer Platform organizations only.

  maxItems: 100

- `workspace_ids: optional array of string`

  Filter to usage in specific workspaces, by tagged workspace ID (`wrkspc_...`). Use `group_by[]=workspace_id` to break out per-workspace values. Claude Developer Platform organizations only; matches nothing for a Claude Enterprise organization.

  maxItems: 100

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `analytics-usage-cost-2026-08-24` in this header.

  - `string`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

## Returns

- `data: array of BetaAnalyticsUsageItem`

  Rows for this page, in the order set by `order_by` and `order`: one per combination of the `group_by[]` dimensions (and per time bucket, when `time_bucket_width` is set) with usage or cost in the range, or a single row when neither is set. Rows split out by `cost_type` or `token_type` (cost endpoint only) stay adjacent and are ranked as one unit.

  - `ending_at: string`

    End of the period this row covers (exclusive), as an RFC 3339 UTC timestamp: the end of the row's time bucket when a time-bucket width is set; otherwise the requested `ending_at` (or, when omitted, the earlier of now and `starting_at` plus 31 days) rounded down to the hour, because without a time bucket the report covers whole hours.

    format: date-time

  - `group: BetaAnalyticsUsageGroup`

    The dimension values this row's usage is broken out by.

    - `actor: BetaAnalyticsActor or null`

      The identity the usage is attributed to: the user if one is attributed, else the service account, else the federated (cloud-platform) identity, else the API key. Populated only when `actor` is in `group_by[]`; null for usage with no attributable identity, and for users' and federated identities' usage when the reader is a member who can see only some workspaces. Distinct identities the server cannot render also read null, each as its own row.

      - `BetaAnalyticsReportUserActor object`

        - `type: "user_actor"`

          Actor type. Always `"user_actor"`.

        - `deleted: boolean`

          True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

        - `email_address: string or null`

          The user's current email address, including for users who are no longer members of the organization. Null when the account has been deleted and for system-minted service accounts.

        - `name: string or null`

          The user's current full name. Null when the user has not set one. `"Deleted User"` when the account has been deleted, or when the user is no longer a member and the organization hides removed users' names.

        - `user_id: string`

          Tagged user ID.

      - `BetaAnalyticsServiceAccountActor object`

        - `type: "service_account_actor"`

        - `service_account_id: string`

          Tagged service account ID.

      - `BetaAnalyticsFederatedActor object`

        - `type: "federated_actor"`

        - `provider: BetaAnalyticsFederatedActorProvider`

          The trusted provider that asserted the caller's identity.

          - `BetaAnalyticsFederatedActorAWSProvider object`

            - `type: "aws"`

            - `account_id: string`

              The AWS account the organization is bound to.

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that made the requests.

          - `BetaAnalyticsFederatedActorAzureProvider object`

            - `type: "azure"`

            - `subscription_id: string`

              The Azure subscription the organization is bound to.

          - `BetaAnalyticsFederatedActorGCPProvider object`

            - `type: "gcp"`

            - `project_number: string`

              The Google Cloud project the organization is bound to.

          - `BetaAnalyticsFederatedActorOIDCProvider object`

            - `type: "oidc"`

            - `issuer: string or null`

              The federation issuer's URL.

        - `subject: string or null`

          The provider's identifier for the caller: on `aws`, the IAM principal ARN (one role is one actor across its sessions); on `gcp`, the caller's IAM principal identifier as Google Cloud reports it, such as `serviceAccount:<email>`, `user:<email>`, or a `principal://...` URI.

      - `BetaAnalyticsAPIActor object`

        - `type: "api_actor"`

        - `api_key_id: string`

          Tagged API key ID.

    - `actor_type: BetaAnalyticsActorType or null`

      Kind of identity the usage is attributed to; matches `actor.type` when `actor` is set. Populated only when `actor_type` is in `group_by[]`.

      - `"api_actor"`

      - `"federated_actor"`

      - `"service_account_actor"`

      - `"user_actor"`

    - `agent_id: string or null`

      Claude Managed Agents agent whose session incurred the usage. Populated only when `agent_id` is in `group_by[]`; null for usage outside a managed session.

    - `api_key_id: string or null`

      API key that authenticated the requests, as a tagged API key ID, whichever identity `actor` resolves to. Populated only when `api_key_id` is in `group_by[]`; null for usage not authenticated by an API key.

    - `claude_tag_category: BetaAnalyticsClaudeTagCategory or null`

      Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude_tag`. New categories may be added over time.

      - `"dm"`

      - `"engaged"`

      - `"monitoring"`

      - `"proactive"`

      - `"scheduled"`

    - `claude_tag_user_id: string or null`

      Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

    - `context_window: BetaAnalyticsContextWindow or null`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `"0-200k"`

      - `"200k-1M"`

    - `deployment_id: string or null`

      Deployment that started the Claude Managed Agents session. Populated only when `deployment_id` is in `group_by[]`; null for usage outside a managed session and for sessions no deployment started.

    - `environment_id: string or null`

      Claude Managed Agents environment the session ran in. Populated only when `environment_id` is in `group_by[]`; null for usage outside a managed session.

    - `inference_geo: BetaAnalyticsUsageCostInferenceGeo or null`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `"global"`

      - `"us"`

    - `model: string or null`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `product: string or null`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, `claude_tag`, and `chat_cowork_unified`. `claude_tag` is Claude Tag, the Claude product in Slack. `chat_cowork_unified` is Chat and Cowork unified, Cowork's features inside claude.ai chat: chat and Cowork usage by a member who has it turned on is reported under this value instead of `chat` or `cowork`. It is accepted as a filter only on deployments that offer Chat and Cowork unified. Some unattributed usage is reported as "other".

    - `rbac_group_id: string or null`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

    - `service_tier: BetaAnalyticsServiceTier or null`

      Service tier the usage was served at. Populated only when `service_tier` is in `group_by[]`; null for usage with no service tier (for example, code execution) and for Claude Enterprise usage.

      - `"batch"`

      - `"flex"`

      - `"flex_discount"`

      - `"priority"`

      - `"priority_on_demand"`

      - `"standard"`

    - `session_id: string or null`

      Claude Managed Agents session that incurred the usage. Populated only when `session_id` is in `group_by[]`; null for usage outside a managed session.

    - `slack_channel_id: string or null`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `speed: BetaAnalyticsSpeed or null`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `"fast"`

      - `"standard"`

    - `user_profile_id: string or null`

      User profile the usage was attributed to, as a tagged `uprof_` ID. Populated only when `user_profile_id` is in `group_by[]`; null for usage that named no profile and for Claude Enterprise usage.

    - `workspace_id: string or null`

      Workspace the usage occurred in, as a tagged workspace ID, including the organization's default workspace. Populated only when `workspace_id` is in `group_by[]`; null for Claude Enterprise usage.

  - `starting_at: string`

    Start of the period this row covers (inclusive), as an RFC 3339 UTC timestamp: the start of the row's time bucket when a time-bucket width is set, otherwise the requested `starting_at` rounded down to the hour.

    format: date-time

  - `usage: BetaAnalyticsUsageMetrics`

    Token usage for this row.

    - `cache_creation: BetaCacheCreation`

      The number of input tokens for cache creation.

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

        default: 0, minimum: 0

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

        default: 0, minimum: 0

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `output_tokens: number`

      The number of output tokens generated.

    - `requests: number or null`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `server_tool_use: BetaAnalyticsServerToolUse`

      Server-side tool usage metrics.

      - `web_search_requests: number`

        The number of web search requests made.

    - `total_tokens: number`

      Total token count across all token types. This is the value the default `order_by` (`total_tokens`) sorts on.

    - `uncached_input_tokens: number`

      The number of uncached input tokens processed.

- `data_refreshed_at: string or null`

  RFC 3339 timestamp of the export this response was served from. Null when no export yet covers any part of the requested range, in which case `data` is empty. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours. Values can be revised as late events arrive and reconciliation runs, until about 7 days after the end of the calendar month the usage falls in; for example, values for October 1 can change until about November 7.

  format: date-time

- `has_more: boolean`

  Whether another page is available. When true, pass `next_page` as the `page` parameter to fetch it.

- `next_page: string or null`

  Opaque cursor for the next page, or null when `has_more` is false. Pass it as the `page` parameter, keeping the other parameters unchanged. A cursor can expire after the underlying data refreshes; the request then returns HTTP 410 and pagination must restart from the first page.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/analytics/usage \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: analytics-usage-cost-2026-08-24' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2026-10-01T00:00:00Z",
      "group": {
        "actor": {
          "deleted": false,
          "email_address": "user@emaildomain.com",
          "name": "Jane Doe",
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "actor_type": "user_actor",
        "agent_id": "agent_01VHd3EAGJ6PLkP9LM7DDu3f",
        "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
        "claude_tag_category": "dm",
        "claude_tag_user_id": "U0123ABCDEF",
        "context_window": "0-200k",
        "deployment_id": "depl_01JFC6ihzZHtAuyHsaENdJhY",
        "environment_id": "env_017oTjuGedHtjhJauVC5xGJD",
        "inference_geo": "global",
        "model": "claude-opus-5-5",
        "product": "chat",
        "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
        "service_tier": "standard",
        "session_id": "sesn_0187kPDyNCwibNNvfaPEApCJ",
        "slack_channel_id": "C0123ABCDEF",
        "speed": "fast",
        "user_profile_id": "uprof_01M33NeYUQK2WV9PpYcsPHLi",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "starting_at": "2026-09-01T00:00:00Z",
      "usage": {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 3200000,
        "output_tokens": 891000,
        "requests": 128,
        "server_tool_use": {
          "web_search_requests": 10
        },
        "total_tokens": 5375500,
        "uncached_input_tokens": 1284500
      }
    }
  ],
  "data_refreshed_at": "2026-10-01T04:02:11Z",
  "has_more": true,
  "next_page": "next_page"
}
```
