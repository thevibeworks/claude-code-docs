---
title: Usage and Cost Analytics API
url: https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api
description: Query token usage and cost for your Claude Console or Claude Enterprise organization by model, workspace, API key, actor, and more.
---

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization on the [Organization](https://platform.claude.com/settings/organization) page (`platform.claude.com/settings/organization`) in the Claude Console.
</Tip>

The Usage and Cost Analytics API reports historical token usage and cost for your organization, broken down by the dimensions you choose, such as model, workspace, API key, or the user or service account behind each request. For Claude Console organizations, this data is similar to what the [Usage](https://platform.claude.com/usage) and [Cost](https://platform.claude.com/cost) pages of the Claude Console show.

The API has two endpoints:

* `GET /v1/organizations/analytics/usage` reports token counts and request counts.
* `GET /v1/organizations/analytics/cost` reports cost in USD.

The Usage and Cost Analytics API is in beta. Send the `anthropic-beta: analytics-usage-cost-2026-08-24` header and an [`anthropic-version`](https://platform.claude.com/docs/en/api/versioning) header on every request. The SDK and the `ant` CLI send both headers for you and fetch the remaining pages as you read the results, so `limit` sets only the page size.

Use this API to:

* **Attribute spend:** Break down cost and token usage by workspace, API key, model, service tier, or the identity that made each request.
* **Find top consumers:** Rank results by tokens, requests, or cost to answer questions such as “which API keys spend the most this month?”
* **Build time series:** Split results into daily, hourly, or per-minute buckets for dashboards and finance reports.
* **Integrate once:** The same endpoints, parameters, and response fields serve Claude Console and Claude Enterprise organizations.

<Check>
  **Authentication**

  Claude Console organizations use an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-console-organization) or another [Admin API credential](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication), such as an OAuth token with the `org:admin` scope. Send an OAuth token in an `authorization: Bearer` header instead of the `x-api-key` header; see [Obtain an OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token).

  Claude Enterprise organizations use a key with the `read:analytics` scope, created in claude.ai by the primary owner after the Analytics API is enabled for the organization; see [Get access to the Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api#get-access-to-the-claude-enterprise-analytics-api).

  The examples on this page read a key from the `ANTHROPIC_API_KEY` environment variable, so set it to your key before you run them.

  If you call these endpoints with an Admin API key, give the service that collects this data its own key, store it in a secrets manager, and rotate it regularly; setting a [key expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration) when you create the key enforces the rotation. Where you can, use a [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rule with the [`org:admin` scope](https://platform.claude.com/docs/en/manage-claude/wif-reference#oauth-scopes) instead, so the service gets short-lived tokens and there’s no long-lived key to leak.
</Check>

<Note>
  **Claude Platform on AWS:** Both endpoints are available. Requests use the Claude Platform on AWS base URL and authentication in place of an Admin API key (see [Making requests](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#making-requests)), and AWS IAM authorizes them through the [`ListAccountUsage` and `ListAccountCost` actions](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#usage-and-cost). Each request covers only the workspaces in the AWS region of the endpoint you call, so call each region’s endpoint to cover your whole organization. `user_profile_id`, `claude_tag_category`, `claude_tag_user_id`, and the Claude Managed Agents dimensions (`agent_id`, `environment_id`, `deployment_id`, and `session_id`) are `null` on every row.
</Note>

<Note>
  **Claude Models on Google Cloud (Anthropic managed):** Both endpoints are available. Call them through the [organization-level base URL](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#making-requests) with Google Cloud credentials instead of an Admin API key. The `/usage` endpoint needs the `usageAnalytics.list` [IAM permission](https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions), and the `/cost` endpoint needs `costAnalytics.list`.
</Note>

## Quick start

Get daily token usage for the first week of September, one row for each model and day:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/usage?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-09-08T00:00:00Z&\
  time_bucket_width=1d&\
  group_by[]=model&\
  limit=10" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:usage list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-09-08T00:00:00Z \
    --time-bucket-width 1d \
    --group-by model \
    --limit 10
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.usage.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-09-08T00:00:00Z",
      time_bucket_width="1d",
      group_by=["model"],
      limit=10,
  )

  for row in rows:
      print(f"{row.starting_at} {row.group.model}: {row.usage.total_tokens}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.usage.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-09-08T00:00:00Z",
    time_bucket_width: "1d",
    group_by: ["model"],
    limit: 10
  });

  for await (const row of rows) {
    console.log(`${row.starting_at} ${row.group.model}: ${row.usage.total_tokens}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics;
  using Anthropic.Models.Beta.Organization.Analytics.Usage;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Usage.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-09-08T00:00:00Z"),
          TimeBucketWidth = BetaAnalyticsTimeBucketWidth.Day,
          GroupBy = [BetaAnalyticsUsageGroupBy.Model],
          Limit = 10,
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine($"{row.StartingAt} {row.Group.Model}: {row.Usage.TotalTokens}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Usage.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUsageListParams{
  	StartingAt:      time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:        anthropic.Time(time.Date(2026, time.September, 8, 0, 0, 0, 0, time.UTC)),
  	TimeBucketWidth: anthropic.BetaAnalyticsTimeBucketWidthDay,
  	GroupBy:         []anthropic.BetaAnalyticsUsageGroupBy{anthropic.BetaAnalyticsUsageGroupByModel},
  	Limit:           anthropic.Int(10),
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s %s: %d\n", row.StartingAt.Format(time.RFC3339), row.Group.Model, row.Usage.TotalTokens)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.BetaAnalyticsTimeBucketWidth;
  import com.anthropic.models.beta.organization.analytics.usage.BetaAnalyticsUsageGroupBy;
  import com.anthropic.models.beta.organization.analytics.usage.UsageListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UsageListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-09-08T00:00:00Z"))
          .timeBucketWidth(BetaAnalyticsTimeBucketWidth.DAY)
          .addGroupBy(BetaAnalyticsUsageGroupBy.MODEL)
          .limit(10)
          .build();
      var rows = client.beta().organization().analytics().usage().list(params);

      for (var row : rows.autoPager()) {
          IO.println(row.startingAt() + " " + row.group().model().orElse(null) + ": " + row.usage().totalTokens());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->usage->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-09-08T00:00:00Z'),
      timeBucketWidth: '1d',
      groupBy: ['model'],
      limit: 10,
  );

  foreach ($rows->pagingEachItem() as $row) {
      $startingAt = $row->startingAt->format(\DateTimeInterface::ATOM);
      echo "{$startingAt} {$row->group->model}: {$row->usage->totalTokens}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.usage.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 9, 8),
    time_bucket_width: :"1d",
    group_by: [:model],
    limit: 10
  )

  page.auto_paging_each do |row|
    puts "#{row.starting_at} #{row.group.model}: #{row.usage.total_tokens}"
  end
  ```
</CodeGroup>

The response has one row for each model and day that has usage, largest `total_tokens` first. This example shows a single row:

```json
{
  "data": [
    {
      "starting_at": "2026-09-03T00:00:00Z",
      "ending_at": "2026-09-04T00:00:00Z",
      "group": {
        "product": null,
        "model": "claude-sonnet-5",
        "context_window": null,
        "inference_geo": null,
        "speed": null,
        "slack_channel_id": null,
        "claude_tag_category": null,
        "claude_tag_user_id": null,
        "rbac_group_id": null,
        "workspace_id": null,
        "service_tier": null,
        "user_profile_id": null,
        "agent_id": null,
        "environment_id": null,
        "deployment_id": null,
        "session_id": null,
        "actor": null,
        "actor_type": null,
        "api_key_id": null
      },
      "usage": {
        "uncached_input_tokens": 1284500,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 215300
        },
        "cache_read_input_tokens": 3200000,
        "output_tokens": 891000,
        "total_tokens": 5590800,
        "server_tool_use": {
          "web_search_requests": 12
        },
        "requests": 4210
      }
    }
  ],
  "has_more": true,
  "next_page": "page_V2mQ4dkt9HcbX3pLr...",
  "data_refreshed_at": "2026-09-18T16:02:11Z"
}
```

<Tip>
  **Set a User-Agent header for integrations**

  If you’re building an integration, set your User-Agent header to help Anthropic understand usage patterns:

  ```text wrap
  User-Agent: YourApp/1.0.0 (https://yourapp.com)
  ```
</Tip>

## How results are shaped

* **Every row has three parts:** `starting_at` and `ending_at` give the period the row covers, `group` holds every dimension, and `usage` (or `cost` on the cost endpoint) holds the metrics.
* **Dimensions are null unless grouped:** A dimension in `group` is `null` unless you list it in `group_by[]`. A grouped dimension is also `null` on rows that have no value for it, such as `model` on code execution usage. `group_by[]` takes up to five dimensions.
* **One row for each combination:** Each row is one combination of the grouped dimensions, and every combination that has usage or cost appears exactly once across the pages of a query. With no `group_by[]` and no `time_bucket_width`, the response is a single row that totals the whole range.
* **Time buckets are optional:** Set `time_bucket_width` to `1m`, `1h`, or `1d` to split each combination by UTC bucket; each row’s `starting_at` and `ending_at` are then its bucket’s bounds. Buckets with no usage or cost produce no rows.
* **Ranked by default:** Rows are ordered by the `order_by` metric across the whole range, largest first by default (`order=asc` reverses it). To build a time series, set `time_bucket_width` and `order_by=time`. Rows then come back one time bucket after another, newest bucket first by default (`order=asc` puts the oldest first), with the largest rows first within each bucket. Fill empty buckets with zeros.
* **Filters work alongside grouping:** Most dimensions you can group by have a matching list filter in bracket notation, such as `models[]=claude-opus-5-5`. Repeat the parameter to pass several values, up to 100. Multiple values for the same filter are combined with OR, and different filters are combined with AND. Filters and `group_by[]` are independent; you can filter by any dimension with or without grouping by it, or the reverse.

Dimensions such as `model` and `actor` apply to every organization. Some, such as `api_key_id`, apply only to Claude Console organizations, and others, such as `slack_channel_id`, apply only to Claude Enterprise organizations. A dimension that doesn’t apply to your organization is `null` on every row and its filter matches nothing; the exception is `rbac_group_id`, which returns an error instead when teams aren’t available to your organization. The [usage](https://platform.claude.com/docs/en/api/beta/organization/analytics/usage/list) and [cost](https://platform.claude.com/docs/en/api/beta/organization/analytics/cost/list) API reference lists every dimension, filter, and value.

### Actors

The `actor` dimension is who a request is attributed to: a user, a service account, a federated cloud identity (an AWS or Google Cloud principal, for organizations that access Claude through their cloud platform), or, when none of those is behind the request, the API key itself. When you group by `actor`, each row’s `actor` is an object whose `type` says which kind it is. Usage that can’t be attributed to any identity has `actor: null`.

[Personal keys and service account keys](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) act as the user or service account they’re linked to, so their requests show that identity as the `actor` and the key in `api_key_id`. Legacy workspace keys aren’t linked to an identity, so the key appears as both the `actor` and the `api_key_id`. The exception is a key that Claude Code creates for a member at sign-in: it lives in the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), and its usage is attributed to that member. Requests made without an API key, such as from the Claude Console, from Claude Code after a [sign-in without an API key](https://code.claude.com/docs/en/authentication#sign-in-without-an-api-key), or with a [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) token, have `api_key_id: null`. After a sign-in without an API key, the `actor` is the member who signed in; a federated workload’s `actor` is its service account. To include usage with no API key in an `api_key_ids[]` filter, add an empty entry: `api_key_ids[]=`.

The `api_key_ids[]` and `actor_ids[]` filters answer different questions. `api_key_ids[]=apikey_...` matches every request the key authenticated, whoever it is attributed to. `actor_ids[]=apikey_...` matches only requests attributed to the key itself.

## Usage endpoint

`GET /v1/organizations/analytics/usage` returns token counts by type. `order_by` accepts `total_tokens` (the default), `output_tokens`, `uncached_input_tokens`, `requests`, or `time`.

For example, to see a week of usage for one workspace and one API key, broken down by service tier (one row for each tier, covering the whole week):

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/usage?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-09-08T00:00:00Z&\
  workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
  api_key_ids[]=apikey_01Rj2N8SVvo6BePZj99NhmiT&\
  group_by[]=service_tier" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:usage list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-09-08T00:00:00Z \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --api-key-id apikey_01Rj2N8SVvo6BePZj99NhmiT \
    --group-by service_tier
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.usage.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-09-08T00:00:00Z",
      workspace_ids=["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
      api_key_ids=["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
      group_by=["service_tier"],
  )

  for row in rows:
      print(f"{row.group.service_tier}: {row.usage.total_tokens}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.usage.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-09-08T00:00:00Z",
    workspace_ids: ["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
    api_key_ids: ["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
    group_by: ["service_tier"]
  });

  for await (const row of rows) {
    console.log(`${row.group.service_tier}: ${row.usage.total_tokens}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics.Usage;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Usage.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-09-08T00:00:00Z"),
          WorkspaceIds = ["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
          ApiKeyIds = ["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
          GroupBy = [BetaAnalyticsUsageGroupBy.ServiceTier],
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine($"{row.Group.ServiceTier?.Raw()}: {row.Usage.TotalTokens}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Usage.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUsageListParams{
  	StartingAt:   time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:     anthropic.Time(time.Date(2026, time.September, 8, 0, 0, 0, 0, time.UTC)),
  	WorkspaceIDs: []string{"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"},
  	APIKeyIDs:    []string{"apikey_01Rj2N8SVvo6BePZj99NhmiT"},
  	GroupBy:      []anthropic.BetaAnalyticsUsageGroupBy{anthropic.BetaAnalyticsUsageGroupByServiceTier},
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s: %d\n", row.Group.ServiceTier, row.Usage.TotalTokens)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.usage.BetaAnalyticsUsageGroupBy;
  import com.anthropic.models.beta.organization.analytics.usage.UsageListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UsageListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-09-08T00:00:00Z"))
          .addWorkspaceId("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
          .addApiKeyId("apikey_01Rj2N8SVvo6BePZj99NhmiT")
          .addGroupBy(BetaAnalyticsUsageGroupBy.SERVICE_TIER)
          .build();
      var rows = client.beta().organization().analytics().usage().list(params);

      for (var row : rows.autoPager()) {
          IO.println(row.group().serviceTier().orElse(null) + ": " + row.usage().totalTokens());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->usage->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-09-08T00:00:00Z'),
      workspaceIDs: ['wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ'],
      apiKeyIDs: ['apikey_01Rj2N8SVvo6BePZj99NhmiT'],
      groupBy: ['service_tier'],
  );

  foreach ($rows->pagingEachItem() as $row) {
      echo "{$row->group->serviceTier}: {$row->usage->totalTokens}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.usage.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 9, 8),
    workspace_ids: ["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
    api_key_ids: ["apikey_01Rj2N8SVvo6BePZj99NhmiT"],
    group_by: [:service_tier]
  )

  page.auto_paging_each do |row|
    puts "#{row.group.service_tier}: #{row.usage.total_tokens}"
  end
  ```
</CodeGroup>

To look up API key and workspace IDs, use the [List API Keys](https://platform.claude.com/docs/en/api/organization/api_keys/list) and [List Workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) endpoints or the Claude Console.

To find which users, service accounts, and API keys made the most requests in a month:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/usage?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-10-01T00:00:00Z&\
  group_by[]=actor&\
  order_by=requests&\
  limit=25" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:usage list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-10-01T00:00:00Z \
    --group-by actor \
    --order-by requests \
    --limit 25
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.usage.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-10-01T00:00:00Z",
      group_by=["actor"],
      order_by="requests",
      limit=25,
  )

  for row in rows:
      print(f"{row.group.actor}: {row.usage.requests}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.usage.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-10-01T00:00:00Z",
    group_by: ["actor"],
    order_by: "requests",
    limit: 25
  });

  for await (const row of rows) {
    console.log(`${JSON.stringify(row.group.actor)}: ${row.usage.requests}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics.Usage;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Usage.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-10-01T00:00:00Z"),
          GroupBy = [BetaAnalyticsUsageGroupBy.Actor],
          OrderBy = BetaAnalyticsUsageOrderBy.Requests,
          Limit = 25,
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine($"{row.Group.Actor?.Json}: {row.Usage.Requests}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Usage.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUsageListParams{
  	StartingAt: time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:   anthropic.Time(time.Date(2026, time.October, 1, 0, 0, 0, 0, time.UTC)),
  	GroupBy:    []anthropic.BetaAnalyticsUsageGroupBy{anthropic.BetaAnalyticsUsageGroupByActor},
  	OrderBy:    anthropic.BetaAnalyticsUsageOrderByRequests,
  	Limit:      anthropic.Int(25),
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s: %d\n", row.Group.Actor.RawJSON(), row.Usage.Requests)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.usage.BetaAnalyticsUsageGroupBy;
  import com.anthropic.models.beta.organization.analytics.usage.BetaAnalyticsUsageOrderBy;
  import com.anthropic.models.beta.organization.analytics.usage.UsageListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UsageListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-10-01T00:00:00Z"))
          .addGroupBy(BetaAnalyticsUsageGroupBy.ACTOR)
          .orderBy(BetaAnalyticsUsageOrderBy.REQUESTS)
          .limit(25)
          .build();
      var rows = client.beta().organization().analytics().usage().list(params);

      for (var row : rows.autoPager()) {
          IO.println(row.group().actor().orElse(null) + ": " + row.usage().requests().orElse(null));
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->usage->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-10-01T00:00:00Z'),
      groupBy: ['actor'],
      orderBy: 'requests',
      limit: 25,
  );

  foreach ($rows->pagingEachItem() as $row) {
      $actor = json_encode($row->group->actor);
      echo "{$actor}: {$row->usage->requests}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.usage.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 10, 1),
    group_by: [:actor],
    order_by: :requests,
    limit: 25
  )

  page.auto_paging_each do |row|
    puts "#{row.group.actor}: #{row.usage.requests}"
  end
  ```
</CodeGroup>

## Cost endpoint

`GET /v1/organizations/analytics/cost` accepts the same filters, dimensions, and time buckets as the `/usage` endpoint. Each row’s `cost` object holds `amount` (the cost after discounts and before any credits are applied), `list_amount` (the cost at list prices), `currency` (always `"USD"`), and `requests`. Amounts are decimal strings in cents with six decimal places: `"41280.000000"` is $412.80 USD. `order_by` accepts `amount` (the default), `list_amount`, or `time`.

Two extra dimensions exist only on this endpoint and don’t count toward the five-dimension limit: `group_by[]=cost_type` splits each row into one row for every cost type, and `group_by[]=token_type` splits token cost into one row for every token type. `limit` doesn’t apply to these two dimensions either, so a page can hold more than `limit` rows. For example, cost by model, cost type, and token type for a month:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/cost?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-10-01T00:00:00Z&\
  group_by[]=model&\
  group_by[]=cost_type&\
  group_by[]=token_type" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:cost list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-10-01T00:00:00Z \
    --group-by model \
    --group-by cost_type \
    --group-by token_type
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.cost.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-10-01T00:00:00Z",
      group_by=["model", "cost_type", "token_type"],
  )

  for row in rows:
      print(
          f"{row.group.model} {row.group.cost_type} {row.group.token_type}: {row.cost.amount}"
      )
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.cost.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-10-01T00:00:00Z",
    group_by: ["model", "cost_type", "token_type"]
  });

  for await (const row of rows) {
    console.log(
      `${row.group.model} ${row.group.cost_type} ${row.group.token_type}: ${row.cost.amount}`
    );
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics.Cost;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Cost.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-10-01T00:00:00Z"),
          GroupBy = [BetaAnalyticsCostGroupBy.Model, BetaAnalyticsCostGroupBy.CostType, BetaAnalyticsCostGroupBy.TokenType],
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine(
          $"{row.Group.Model} {row.Group.CostType?.Raw()} {row.Group.TokenType?.Raw()}: {row.Cost.Amount}"
      );
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Cost.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsCostListParams{
  	StartingAt: time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:   anthropic.Time(time.Date(2026, time.October, 1, 0, 0, 0, 0, time.UTC)),
  	GroupBy:    []anthropic.BetaAnalyticsCostGroupBy{anthropic.BetaAnalyticsCostGroupByModel, anthropic.BetaAnalyticsCostGroupByCostType, anthropic.BetaAnalyticsCostGroupByTokenType},
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s %s %s: %s\n", row.Group.Model, row.Group.CostType, row.Group.TokenType, row.Cost.Amount)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.cost.BetaAnalyticsCostGroupBy;
  import com.anthropic.models.beta.organization.analytics.cost.CostListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = CostListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-10-01T00:00:00Z"))
          .addGroupBy(BetaAnalyticsCostGroupBy.MODEL)
          .addGroupBy(BetaAnalyticsCostGroupBy.COST_TYPE)
          .addGroupBy(BetaAnalyticsCostGroupBy.TOKEN_TYPE)
          .build();
      var rows = client.beta().organization().analytics().cost().list(params);

      for (var row : rows.autoPager()) {
          var group = row.group();
          IO.println(
              group.model().orElse(null) + " " + group.costType().orElse(null) + " "
                  + group.tokenType().orElse(null) + ": " + row.cost().amount()
          );
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->cost->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-10-01T00:00:00Z'),
      groupBy: ['model', 'cost_type', 'token_type'],
  );

  foreach ($rows->pagingEachItem() as $row) {
      $group = $row->group;
      echo "{$group->model} {$group->costType} {$group->tokenType}: {$row->cost->amount}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.cost.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 10, 1),
    group_by: [:model, :cost_type, :token_type]
  )

  page.auto_paging_each do |row|
    group = row.group
    puts "#{group.model} #{group.cost_type} #{group.token_type}: #{row.cost.amount}"
  end
  ```
</CodeGroup>

For each model, the response has five `tokens` rows (one for every token type) plus one row each for `web_search`, `code_execution`, and `session_usage`. One of those rows:

```json
{
  "starting_at": "2026-09-01T00:00:00Z",
  "ending_at": "2026-10-01T00:00:00Z",
  "group": {
    "model": "claude-opus-5",
    ...,
    "cost_type": "tokens",
    "token_type": "cache_read_input_tokens"
  },
  "cost": {
    "currency": "USD",
    "amount": "41280.000000",
    "list_amount": "51600.000000",
    "requests": null
  }
}
```

The `group` object carries every dimension and is abbreviated here. With `group_by[]=cost_type` or `token_type` specified, `requests` is `null` on every row.

<Warning>
  Requests served under a Priority Tier commitment appear on the usage endpoint with `service_tier: "priority"` but contribute zero token cost to `amount` and `list_amount`, because your commitment covers them; the commitment fee is billed separately and isn’t in this data. Web search on those requests is billed at the standard rate. Requests beyond your committed capacity are served and priced at the standard tier.
</Warning>

## Date ranges and time buckets

* Timestamps are RFC 3339 with a UTC offset, for example `2026-09-01T00:00:00Z`. `starting_at` is inclusive and `ending_at` is exclusive.
* `starting_at` must be on or after January 1, 2026, and within the last 365 days. A request can span at most 31 days; `ending_at` defaults to 31 days after `starting_at` or the current time, whichever is earlier.
* `ending_at` is required whenever `time_bucket_width` is set, and with `time_bucket_width=1m` a request can span at most 24 hours.
* Both ends of the range are rounded down to a UTC bucket boundary, or to the hour when `time_bucket_width` isn’t set. For example, with `time_bucket_width=1h`, a `starting_at` of `2026-09-01T10:43:00Z` is treated as `2026-09-01T10:00:00Z` and an `ending_at` of `2026-09-01T15:43:00Z` as `2026-09-01T15:00:00Z`, so the response covers 10:00 to 15:00 UTC.

## Data freshness

Every response includes a `data_refreshed_at` timestamp, and usage after that time is missing or partial. When no data is available yet for any part of the requested range, `data_refreshed_at` is `null` and `data` is empty. Data typically refreshes within 4 hours of the underlying usage and can take up to 24 hours. Values can be revised as late events arrive and reconciliation runs, until about 7 days after the end of the calendar month. For example, values for October 1 can change until about November 7. For stable results across repeated calls, set `ending_at` at or before a `data_refreshed_at` you have already seen; for final totals, query only months that ended at least 7 days ago. Every page of a paginated query reads the same data snapshot, so `data_refreshed_at` is identical across pages.

## Migrate from the Usage and Cost API

This section is for Claude Console organizations that call the legacy [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) (`/v1/organizations/usage_report/messages` and `/v1/organizations/cost_report`). Your Admin API key, the `anthropic-version` header, `starting_at` and `ending_at`, the bucket width values (`1m`, `1h`, `1d`), bracket notation, the pagination field names, and the token and cost field names carry over. What changes:

| Usage and Cost API                                                                                                                                      | Usage and Cost Analytics API                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No beta header                                                                                                                                          | `anthropic-beta: analytics-usage-cost-2026-08-24` on every request                                                                                                                                                                                                                                                                                                                    |
| Data typically appears within 5 minutes                                                                                                                 | Data typically refreshes within 4 hours and can take up to 24 hours (see [Data freshness](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#data-freshness))                                                                                                                                                                                                 |
| `data` is a list of time buckets, oldest first, including empty ones, each with a `results` list whose entries hold dimensions and metrics side by side | `data` is a list of rows ranked by `order_by`, each with its own `starting_at` and `ending_at`, dimensions in `group`, and metrics in `usage` or `cost`. Combinations with no usage or cost have no row.                                                                                                                                                                              |
| `bucket_width`, default `1d`                                                                                                                            | `time_bucket_width`, no default. Pass `time_bucket_width=1d` to keep daily rows; omit it for whole-range totals. The cost endpoint also accepts every filter and `1m` and `1h` buckets.                                                                                                                                                                                               |
| `limit` counts time buckets per page                                                                                                                    | `limit` counts rows per page (1 to 1,000, default 20), so the number of pages depends on how many combinations have data                                                                                                                                                                                                                                                              |
| Any date range, paged forward by bucket                                                                                                                 | `starting_at` on or after January 1, 2026, and within the last 365 days, at most 31 days per request, `ending_at` required with `time_bucket_width`, and at most 24 hours with `1m` buckets (see [Date ranges and time buckets](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#date-ranges-and-time-buckets)). Split longer ranges into several requests. |
| `account_ids[]`, `service_account_ids[]`, `group_by[]=account_id`, `group_by[]=service_account_id`                                                      | `actor_ids[]` with the same tagged IDs, and `group_by[]=actor` or `actor_type`; read `actor.user_id` or `actor.service_account_id`. See [Actors](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#actors).                                                                                                                                                  |
| `context_window[]`                                                                                                                                      | `context_windows[]`                                                                                                                                                                                                                                                                                                                                                                   |
| `group_by[]=description` on the cost report, with a `description` string                                                                                | No `description`. Group by the structured dimensions instead: any of `model`, `cost_type`, `token_type`, `context_window`, `service_tier`, `inference_geo`, and `speed`, all of which fit in one request.                                                                                                                                                                             |
| An unknown API key or workspace ID returns an error                                                                                                     | It matches nothing, including a misspelled `models[]` name. Each list takes up to 100 values.                                                                                                                                                                                                                                                                                         |
| `workspace_id: null` for the default workspace                                                                                                          | The default workspace’s real `workspace_id` (see [How is the default workspace represented?](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api#how-is-the-default-workspace-represented))                                                                                                                                                                    |
| `inference_geo: "not_available"` and `service_tier: "standard"` on usage with no geo or tier                                                            | `null` for both. `inference_geos[]=not_available` still matches the rows with no inference geo.                                                                                                                                                                                                                                                                                       |
| Cost `service_tier` is `standard` or `batch`; `amount` such as `"123.45"`                                                                               | The actual tier; `amount` with six decimal places, such as `"123.450000"`, plus `list_amount`.                                                                                                                                                                                                                                                                                        |
| Code execution not in the usage report; no request counts                                                                                               | Code execution appears as usage rows with `model: null`; adds `requests` on both endpoints and `total_tokens` on usage rows                                                                                                                                                                                                                                                           |

To reproduce the legacy daily report, request `time_bucket_width=1d` with the same `group_by[]`, page through with `limit=1000`, then group rows by `starting_at` and fill missing days with zeros. Add `order_by=time&order=asc` to get the days in order. Daily usage by model for 1 week, before:

```bash cURL
curl --globoff "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2026-09-01T00:00:00Z&\
ending_at=2026-09-08T00:00:00Z&\
group_by[]=model&\
bucket_width=1d" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_API_KEY"
```

and after:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/usage?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-09-08T00:00:00Z&\
  group_by[]=model&\
  time_bucket_width=1d&\
  limit=1000" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:usage list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-09-08T00:00:00Z \
    --time-bucket-width 1d \
    --group-by model \
    --limit 1000
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.usage.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-09-08T00:00:00Z",
      time_bucket_width="1d",
      group_by=["model"],
      limit=1000,
  )

  for row in rows:
      print(f"{row.starting_at} {row.group.model}: {row.usage.total_tokens}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.usage.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-09-08T00:00:00Z",
    time_bucket_width: "1d",
    group_by: ["model"],
    limit: 1000
  });

  for await (const row of rows) {
    console.log(`${row.starting_at} ${row.group.model}: ${row.usage.total_tokens}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics;
  using Anthropic.Models.Beta.Organization.Analytics.Usage;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Usage.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-09-08T00:00:00Z"),
          TimeBucketWidth = BetaAnalyticsTimeBucketWidth.Day,
          GroupBy = [BetaAnalyticsUsageGroupBy.Model],
          Limit = 1000,
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine($"{row.StartingAt} {row.Group.Model}: {row.Usage.TotalTokens}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Usage.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUsageListParams{
  	StartingAt:      time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:        anthropic.Time(time.Date(2026, time.September, 8, 0, 0, 0, 0, time.UTC)),
  	TimeBucketWidth: anthropic.BetaAnalyticsTimeBucketWidthDay,
  	GroupBy:         []anthropic.BetaAnalyticsUsageGroupBy{anthropic.BetaAnalyticsUsageGroupByModel},
  	Limit:           anthropic.Int(1000),
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s %s: %d\n", row.StartingAt.Format(time.RFC3339), row.Group.Model, row.Usage.TotalTokens)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.BetaAnalyticsTimeBucketWidth;
  import com.anthropic.models.beta.organization.analytics.usage.BetaAnalyticsUsageGroupBy;
  import com.anthropic.models.beta.organization.analytics.usage.UsageListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UsageListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-09-08T00:00:00Z"))
          .timeBucketWidth(BetaAnalyticsTimeBucketWidth.DAY)
          .addGroupBy(BetaAnalyticsUsageGroupBy.MODEL)
          .limit(1000)
          .build();
      var rows = client.beta().organization().analytics().usage().list(params);

      for (var row : rows.autoPager()) {
          IO.println(row.startingAt() + " " + row.group().model().orElse(null) + ": " + row.usage().totalTokens());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->usage->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-09-08T00:00:00Z'),
      timeBucketWidth: '1d',
      groupBy: ['model'],
      limit: 1000,
  );

  foreach ($rows->pagingEachItem() as $row) {
      $startingAt = $row->startingAt->format(\DateTimeInterface::ATOM);
      echo "{$startingAt} {$row->group->model}: {$row->usage->totalTokens}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.usage.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 9, 8),
    time_bucket_width: :"1d",
    group_by: [:model],
    limit: 1000
  )

  page.auto_paging_each do |row|
    puts "#{row.starting_at} #{row.group.model}: #{row.usage.total_tokens}"
  end
  ```
</CodeGroup>

Daily cost by workspace, model, service tier, context window, and inference geo, split by cost type and token type:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/cost?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-09-08T00:00:00Z&\
  time_bucket_width=1d&\
  group_by[]=workspace_id&\
  group_by[]=model&\
  group_by[]=service_tier&\
  group_by[]=context_window&\
  group_by[]=inference_geo&\
  group_by[]=cost_type&\
  group_by[]=token_type&\
  limit=1000" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:cost list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-09-08T00:00:00Z \
    --time-bucket-width 1d \
    --group-by workspace_id \
    --group-by model \
    --group-by service_tier \
    --group-by context_window \
    --group-by inference_geo \
    --group-by cost_type \
    --group-by token_type \
    --limit 1000
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.cost.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-09-08T00:00:00Z",
      time_bucket_width="1d",
      group_by=[
          "workspace_id",
          "model",
          "service_tier",
          "context_window",
          "inference_geo",
          "cost_type",
          "token_type",
      ],
      limit=1000,
  )

  for row in rows:
      group = row.group
      print(
          f"{row.starting_at} {group.workspace_id} {group.model} {group.service_tier} "
          f"{group.context_window} {group.inference_geo} {group.cost_type} {group.token_type}: "
          f"{row.cost.amount}"
      )
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.cost.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-09-08T00:00:00Z",
    time_bucket_width: "1d",
    group_by: [
      "workspace_id",
      "model",
      "service_tier",
      "context_window",
      "inference_geo",
      "cost_type",
      "token_type"
    ],
    limit: 1000
  });

  for await (const row of rows) {
    const { group } = row;
    console.log(
      `${row.starting_at} ${group.workspace_id} ${group.model} ${group.service_tier} ` +
        `${group.context_window} ${group.inference_geo} ${group.cost_type} ${group.token_type}: ` +
        `${row.cost.amount}`
    );
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics;
  using Anthropic.Models.Beta.Organization.Analytics.Cost;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Cost.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-09-08T00:00:00Z"),
          TimeBucketWidth = BetaAnalyticsTimeBucketWidth.Day,
          GroupBy =
          [
              BetaAnalyticsCostGroupBy.WorkspaceID,
              BetaAnalyticsCostGroupBy.Model,
              BetaAnalyticsCostGroupBy.ServiceTier,
              BetaAnalyticsCostGroupBy.ContextWindow,
              BetaAnalyticsCostGroupBy.InferenceGeo,
              BetaAnalyticsCostGroupBy.CostType,
              BetaAnalyticsCostGroupBy.TokenType,
          ],
          Limit = 1000,
      }
  );

  await foreach (var row in page.Paginate())
  {
      var group = row.Group;
      Console.WriteLine(
          $"{row.StartingAt} {group.WorkspaceID} {group.Model} {group.ServiceTier?.Raw()} "
              + $"{group.ContextWindow?.Raw()} {group.InferenceGeo?.Raw()} {group.CostType?.Raw()} "
              + $"{group.TokenType?.Raw()}: {row.Cost.Amount}"
      );
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Cost.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsCostListParams{
  	StartingAt:      time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:        anthropic.Time(time.Date(2026, time.September, 8, 0, 0, 0, 0, time.UTC)),
  	TimeBucketWidth: anthropic.BetaAnalyticsTimeBucketWidthDay,
  	GroupBy: []anthropic.BetaAnalyticsCostGroupBy{
  		anthropic.BetaAnalyticsCostGroupByWorkspaceID,
  		anthropic.BetaAnalyticsCostGroupByModel,
  		anthropic.BetaAnalyticsCostGroupByServiceTier,
  		anthropic.BetaAnalyticsCostGroupByContextWindow,
  		anthropic.BetaAnalyticsCostGroupByInferenceGeo,
  		anthropic.BetaAnalyticsCostGroupByCostType,
  		anthropic.BetaAnalyticsCostGroupByTokenType,
  	},
  	Limit: anthropic.Int(1000),
  })

  for rows.Next() {
  	row := rows.Current()
  	group := row.Group
  	fmt.Printf("%s %s %s %s %s %s %s %s: %s\n",
  		row.StartingAt.Format(time.RFC3339), group.WorkspaceID, group.Model, group.ServiceTier,
  		group.ContextWindow, group.InferenceGeo, group.CostType, group.TokenType, row.Cost.Amount)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.BetaAnalyticsTimeBucketWidth;
  import com.anthropic.models.beta.organization.analytics.cost.BetaAnalyticsCostGroupBy;
  import com.anthropic.models.beta.organization.analytics.cost.CostListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = CostListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-09-08T00:00:00Z"))
          .timeBucketWidth(BetaAnalyticsTimeBucketWidth.DAY)
          .addGroupBy(BetaAnalyticsCostGroupBy.WORKSPACE_ID)
          .addGroupBy(BetaAnalyticsCostGroupBy.MODEL)
          .addGroupBy(BetaAnalyticsCostGroupBy.SERVICE_TIER)
          .addGroupBy(BetaAnalyticsCostGroupBy.CONTEXT_WINDOW)
          .addGroupBy(BetaAnalyticsCostGroupBy.INFERENCE_GEO)
          .addGroupBy(BetaAnalyticsCostGroupBy.COST_TYPE)
          .addGroupBy(BetaAnalyticsCostGroupBy.TOKEN_TYPE)
          .limit(1000)
          .build();
      var rows = client.beta().organization().analytics().cost().list(params);

      for (var row : rows.autoPager()) {
          var group = row.group();
          IO.println(
              row.startingAt() + " " + group.workspaceId().orElse(null) + " " + group.model().orElse(null) + " "
                  + group.serviceTier().orElse(null) + " " + group.contextWindow().orElse(null) + " "
                  + group.inferenceGeo().orElse(null) + " " + group.costType().orElse(null) + " "
                  + group.tokenType().orElse(null) + ": " + row.cost().amount()
          );
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->cost->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-09-08T00:00:00Z'),
      timeBucketWidth: '1d',
      groupBy: [
          'workspace_id',
          'model',
          'service_tier',
          'context_window',
          'inference_geo',
          'cost_type',
          'token_type',
      ],
      limit: 1000,
  );

  foreach ($rows->pagingEachItem() as $row) {
      $startingAt = $row->startingAt->format(\DateTimeInterface::ATOM);
      $group = $row->group;
      echo "{$startingAt} {$group->workspaceID} {$group->model} {$group->serviceTier} "
          . "{$group->contextWindow} {$group->inferenceGeo} {$group->costType} {$group->tokenType}: "
          . "{$row->cost->amount}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.cost.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 9, 8),
    time_bucket_width: :"1d",
    group_by: [
      :workspace_id,
      :model,
      :service_tier,
      :context_window,
      :inference_geo,
      :cost_type,
      :token_type
    ],
    limit: 1000
  )

  page.auto_paging_each do |row|
    group = row.group
    puts "#{row.starting_at} #{group.workspace_id} #{group.model} #{group.service_tier} " \
      "#{group.context_window} #{group.inference_geo} #{group.cost_type} #{group.token_type}: " \
      "#{row.cost.amount}"
  end
  ```
</CodeGroup>

## Migrate from the Claude Enterprise usage and cost reports

This section is for Claude Enterprise organizations that call the [Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api) report endpoints `usage_report`, `cost_report`, `user_usage_report`, and `user_cost_report` under `/v1/organizations/analytics/`. Those endpoints are legacy and remain supported. Move to `/analytics/usage` and `/analytics/cost` when you want any of the following:

* Every group in every time bucket, rather than the top 100 groups in each bucket
* Grouping by `actor` or `actor_type` together with other dimensions, on both usage and cost
* Rows ranked by a metric of your choice across the whole range, or ordered by time bucket
* One integration that also serves Claude Console organizations

Your key, the earliest date, the 365-day lookback and 31-day span, the filter and dimension names and values (except `user_ids[]` and the Claude Tag product value), the user `actor` fields, the metric and amount fields, `data_refreshed_at`, the cursor rules, and the [organization-level rate limit](https://platform.claude.com/docs/en/manage-claude/analytics-api#working-with-the-api) carry over. The only new header is the `analytics-usage-cost-2026-08-24` beta header. What changes:

| Claude Enterprise reports                                                                                                                                                                     | Usage and Cost Analytics API                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `usage_report` and `cost_report` return time buckets, oldest first, including empty ones, each holding at most its top 100 groups; `bucket_width` defaults to `1d` and `limit` counts buckets | Rows covering every combination with data, ranked by `order_by`, each with its own `starting_at` and `ending_at`, dimensions in `group`, and metrics in `usage` or `cost`. `time_bucket_width` is optional and `limit` counts rows. |
| The time-bucket parameter is `bucket_width`                                                                                                                                                   | It is `time_bucket_width`, with the same values                                                                                                                                                                                     |
| On `usage_report` and `cost_report`, `ending_at` is optional with `bucket_width` and `1m` buckets can span up to 31 days                                                                      | `ending_at` required with `time_bucket_width`; `1m` buckets span at most 24 hours per request                                                                                                                                       |
| `user_usage_report` and `user_cost_report` return one row per user                                                                                                                            | `group_by[]=actor&actor_types[]=user_actor`. Without the filter you also get rows for non-user identities and an `actor: null` row for unattributed usage.                                                                          |
| Claude Tag usage has `product: "claude-tag"`                                                                                                                                                  | `product: "claude_tag"`; `products[]` accepts either spelling                                                                                                                                                                       |
| An unrecognized `models[]` name returns a 400 error                                                                                                                                           | It matches nothing                                                                                                                                                                                                                  |
| `user_ids[]`                                                                                                                                                                                  | `actor_ids[]` with the same tagged `user_...` IDs                                                                                                                                                                                   |
| `exclude_deleted_users` on the per-user reports                                                                                                                                               | Requires `group_by[]=actor`; without it, the request returns a 400 error. It drops only rows whose `actor` is a user with `deleted: true`; rows for other identities and rows with `actor: null` stay.                              |

Per-user cost for a month, before:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/analytics/user_cost_report?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-10-01T00:00:00Z&\
  limit=100" \
    -H "anthropic-version: 2023-06-01" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:user-cost-report list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-10-01T00:00:00Z \
    --limit 100
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.user_cost_report.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-10-01T00:00:00Z",
      limit=100,
  )

  for row in rows:
      print(f"{row.actor.user_id}: {row.amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.userCostReport.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-10-01T00:00:00Z",
    limit: 100
  });

  for await (const row of rows) {
    console.log(`${row.actor.user_id}: ${row.amount}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.UserCostReport.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-10-01T00:00:00Z"),
          Limit = 100,
      }
  );

  await foreach (var row in page.Paginate())
  {
      Console.WriteLine($"{row.Actor.UserID}: {row.Amount}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.UserCostReport.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUserCostReportListParams{
  	StartingAt: time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:   anthropic.Time(time.Date(2026, time.October, 1, 0, 0, 0, 0, time.UTC)),
  	Limit:      anthropic.Int(100),
  })

  for rows.Next() {
  	row := rows.Current()
  	fmt.Printf("%s: %s\n", row.Actor.UserID, row.Amount)
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.usercostreport.UserCostReportListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserCostReportListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-10-01T00:00:00Z"))
          .limit(100)
          .build();
      var rows = client.beta().organization().analytics().userCostReport().list(params);

      for (var row : rows.autoPager()) {
          IO.println(row.actor().userId() + ": " + row.amount());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rows = $client->beta->organization->analytics->userCostReport->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-10-01T00:00:00Z'),
      limit: 100,
  );

  foreach ($rows->pagingEachItem() as $row) {
      echo "{$row->actor->userID}: {$row->amount}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.user_cost_report.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 10, 1),
    limit: 100
  )

  page.auto_paging_each do |row|
    puts "#{row.actor.user_id}: #{row.amount}"
  end
  ```
</CodeGroup>

and after, adding a breakdown by product:

<CodeGroup>
  ```bash cURL
  curl --globoff "https://api.anthropic.com/v1/organizations/analytics/cost?\
  starting_at=2026-09-01T00:00:00Z&\
  ending_at=2026-10-01T00:00:00Z&\
  group_by[]=actor&\
  group_by[]=product&\
  actor_types[]=user_actor&\
  limit=100" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: analytics-usage-cost-2026-08-24" \
    -H "x-api-key: $ANTHROPIC_API_KEY"
  ```

  ```bash CLI
  ant beta:organization:analytics:cost list \
    --starting-at 2026-09-01T00:00:00Z \
    --ending-at 2026-10-01T00:00:00Z \
    --actor-type user_actor \
    --group-by actor \
    --group-by product \
    --limit 100
  ```

  ```python Python
  client = anthropic.Anthropic()

  rows = client.beta.organization.analytics.cost.list(
      starting_at="2026-09-01T00:00:00Z",
      ending_at="2026-10-01T00:00:00Z",
      actor_types=["user_actor"],
      group_by=["actor", "product"],
      limit=100,
  )

  for row in rows:
      actor = row.group.actor
      if actor is not None and actor.type == "user_actor":
          print(f"{actor.user_id} {row.group.product}: {row.cost.amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rows = await client.beta.organization.analytics.cost.list({
    starting_at: "2026-09-01T00:00:00Z",
    ending_at: "2026-10-01T00:00:00Z",
    actor_types: ["user_actor"],
    group_by: ["actor", "product"],
    limit: 100
  });

  for await (const row of rows) {
    const { actor } = row.group;
    if (actor?.type === "user_actor") {
      console.log(`${actor.user_id} ${row.group.product}: ${row.cost.amount}`);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Analytics;
  using Anthropic.Models.Beta.Organization.Analytics.Cost;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Analytics.Cost.List(
      new()
      {
          StartingAt = DateTimeOffset.Parse("2026-09-01T00:00:00Z"),
          EndingAt = DateTimeOffset.Parse("2026-10-01T00:00:00Z"),
          ActorTypes = [BetaAnalyticsActorType.UserActor],
          GroupBy = [BetaAnalyticsCostGroupBy.Actor, BetaAnalyticsCostGroupBy.Product],
          Limit = 100,
      }
  );

  await foreach (var row in page.Paginate())
  {
      if (row.Group.Actor is { } actor && actor.TryPickReportUser(out var user))
      {
          Console.WriteLine($"{user.UserID} {row.Group.Product}: {row.Cost.Amount}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rows := client.Beta.Organization.Analytics.Cost.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsCostListParams{
  	StartingAt: time.Date(2026, time.September, 1, 0, 0, 0, 0, time.UTC),
  	EndingAt:   anthropic.Time(time.Date(2026, time.October, 1, 0, 0, 0, 0, time.UTC)),
  	ActorTypes: []anthropic.BetaAnalyticsActorType{anthropic.BetaAnalyticsActorTypeUserActor},
  	GroupBy:    []anthropic.BetaAnalyticsCostGroupBy{anthropic.BetaAnalyticsCostGroupByActor, anthropic.BetaAnalyticsCostGroupByProduct},
  	Limit:      anthropic.Int(100),
  })

  for rows.Next() {
  	row := rows.Current()
  	if user, ok := row.Group.Actor.AsAny().(anthropic.BetaAnalyticsReportUserActor); ok {
  		fmt.Printf("%s %s: %s\n", user.UserID, row.Group.Product, row.Cost.Amount)
  	}
  }
  if err := rows.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.analytics.BetaAnalyticsActorType;
  import com.anthropic.models.beta.organization.analytics.cost.BetaAnalyticsCostGroupBy;
  import com.anthropic.models.beta.organization.analytics.cost.CostListParams;
  import java.time.OffsetDateTime;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = CostListParams.builder()
          .startingAt(OffsetDateTime.parse("2026-09-01T00:00:00Z"))
          .endingAt(OffsetDateTime.parse("2026-10-01T00:00:00Z"))
          .addActorType(BetaAnalyticsActorType.USER_ACTOR)
          .addGroupBy(BetaAnalyticsCostGroupBy.ACTOR)
          .addGroupBy(BetaAnalyticsCostGroupBy.PRODUCT)
          .limit(100)
          .build();
      var rows = client.beta().organization().analytics().cost().list(params);

      for (var row : rows.autoPager()) {
          row.group().actor().flatMap(actor -> actor.user()).ifPresent(user ->
              IO.println(user.userId() + " " + row.group().product().orElse(null) + ": " + row.cost().amount())
          );
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Analytics\AnalyticsReportUserActor;
  // ...

  $client = new Client();

  $rows = $client->beta->organization->analytics->cost->list(
      startingAt: new \DateTimeImmutable('2026-09-01T00:00:00Z'),
      endingAt: new \DateTimeImmutable('2026-10-01T00:00:00Z'),
      actorTypes: ['user_actor'],
      groupBy: ['actor', 'product'],
      limit: 100,
  );

  foreach ($rows->pagingEachItem() as $row) {
      $actor = $row->group->actor;
      if ($actor instanceof AnalyticsReportUserActor) {
          echo "{$actor->userID} {$row->group->product}: {$row->cost->amount}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.analytics.cost.list(
    starting_at: Time.utc(2026, 9, 1),
    ending_at: Time.utc(2026, 10, 1),
    actor_types: [:user_actor],
    group_by: [:actor, :product],
    limit: 100
  )

  page.auto_paging_each do |row|
    actor = row.group.actor
    if actor.is_a?(Anthropic::Models::Beta::Organization::BetaAnalyticsReportUserActor)
      puts "#{actor.user_id} #{row.group.product}: #{row.cost.amount}"
    end
  end
  ```
</CodeGroup>

## Frequently asked questions

### How is the default workspace represented?

A Claude Console organization’s default workspace has its own `wrkspc_` ID, like every other workspace. Rows for the default workspace have that ID in `workspace_id`, and you can filter on it with `workspace_ids[]`. [List Workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) leaves out the default workspace unless you pass `include_default=true`. To check whether an unfamiliar `workspace_id` is the default workspace, pass it to [Get Workspace](https://platform.claude.com/docs/en/api/organization/workspaces/retrieve): the default workspace returns `"name": "Default"`.

### How do I get per-user cost for Claude Code?

Call the cost endpoint with `products[]=claude_code&group_by[]=actor`. Claude Console organizations can also use the [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api), which reports per-user Claude Code activity and estimated cost.

## See also

* [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) (legacy)
* [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api): which analytics API and key type your organization needs
* [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)
* [Admin API reference](https://platform.claude.com/docs/en/api/beta/organization)
* [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
