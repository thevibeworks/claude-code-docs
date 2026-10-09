---
title: Rate Limits API
url: https://platform.claude.com/docs/en/manage-claude/rate-limits-api
description: Programmatically query your organization's API rate limits with the Rate Limits API.
---

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The Rate Limits API provides programmatic access to the rate limits configured for your organization and its workspaces. This is the same information shown on the [Rate limits](https://platform.claude.com/usage/limits) page in the Claude Console.

Use this API to:

* **Keep gateways and proxies in sync:** Read your current limits at startup and on a schedule instead of hardcoding values that drift when Anthropic adjusts them.
* **Power internal alerting:** Compare usage data from the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) against your configured limits.
* **Audit workspace configuration:** Verify that workspace overrides match what your provisioning automation expects.

<Check>
  **Admin API credentials required.** These endpoints are part of the Admin API. You can access them using an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys), an OAuth token with the `org:admin` scope, or a personal or service account key that isn't scoped to a workspace; workspace API keys don't work. See [Authentication](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication) for details.
</Check>

The SDK and CLI examples on this page construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable. The SDKs expose these endpoints as `client.organization.rate_limits` (typescript: `client.organization.rateLimits`; csharp, go: `client.Organization.RateLimits`; java: `client.organization().rateLimits()`; php: `$client->organization->rateLimits`) and `client.organization.workspaces.rate_limits` (typescript: `client.organization.workspaces.rateLimits`; csharp, go: `client.Organization.Workspaces.RateLimits`; java: `client.organization().workspaces().rateLimits()`; php: `$client->organization->workspaces->rateLimits`); the Python, TypeScript, C#, Go, and Java list methods return an iterator that follows `next_page` for you, while the PHP, Ruby, and curl examples read one page.

## Quick start

List the rate limits configured for your organization:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:rate-limits list
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.rate_limits.list()

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.rateLimits.list();

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Organization.RateLimits.List();

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.OrganizationRateLimitListParams{})

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.organization().rateLimits().list();

  for (var entry : rateLimits.autoPager()) {
      var models = entry.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(entry.group().type().asString() + models);
      for (var limit : entry.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->organization->rateLimits->list();

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.organization.rate_limits.list

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

## Organization rate limits

The `/v1/organizations/rate_limits` endpoint returns the rate limits applied at the organization level for the Messages API and its supporting resources. Limits for other products, such as [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), are not included.

### Key concepts

* **Rate limit groups:** Each entry in the response represents one rate limit group. Model rate limits are grouped so that several model versions share a single set of limits, and other groups cover resources such as the Message Batches API, the Files API, the Token Counting API, agent skills, and the web search tool.
* **`group` object:** Present on every entry, it identifies the rate limit group the entry applies to. It always has `type`, which is one of the `group_type` values, and `id`, an opaque identifier with the `rlg_` prefix. On `model_group` entries it also has `display_name`, Anthropic's current label for the group, such as `Claude Sonnet 4.x`. The label is for display only and may change. Other group types have no `display_name`.
* **The `id` inside `group`:** A group has the same `id` in every organization and on every workspace override, and it never changes. Use it to match entries across organizations or against your own catalog. The entry's own `id` differs per organization, and `models` changes when Anthropic moves a model between groups. Neither is a stable key for the group.
* **`group_type`:** Deprecated in favor of the `type` inside `group`. It's still returned, always equals that value, and has no removal date. The `group_type` query parameter isn't deprecated. See [Filtering by group type](https://platform.claude.com/docs/en/manage-claude/rate-limits-api#filtering-by-group-type) for the list of values.
* **`models` list:** For `model_group` entries, the `models` field lists every model ID and alias that counts against that group's limits. Use this list to look up which group any model string falls under. For other group types, `models` is `null`.
* **`limits` list:** Each group carries a list of `{type, value}` pairs. The `type` field identifies the limiter (such as `requests_per_minute`, `input_tokens_per_minute`, or `output_tokens_per_minute`) and `value` is the configured limit. See [Rate limits](https://platform.claude.com/docs/en/api/rate-limits) for how each limiter is measured and enforced.
* **`source` on workspace limits:** On the workspace endpoint, every limit value also carries `source`, which says where `value` comes from: `{"type": "workspace"}` for an override stored on the workspace, or `{"type": "organization"}` for a value inherited from the organization. By default, the workspace endpoint returns overrides only, so `source.type` is always `workspace` there; inherited values appear when you pass `include_inherited=true`. See [Workspace rate limits](https://platform.claude.com/docs/en/manage-claude/rate-limits-api#workspace-rate-limits).

For complete parameter details and response schemas, see the [Organization Rate Limits API reference](https://platform.claude.com/docs/en/api/organization/rate_limits/list).

### List all organization rate limits

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:rate-limits list
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.rate_limits.list()

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.rateLimits.list();

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Organization.RateLimits.List();

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.OrganizationRateLimitListParams{})

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.organization().rateLimits().list();

  for (var entry : rateLimits.autoPager()) {
      var models = entry.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(entry.group().type().asString() + models);
      for (var limit : entry.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->organization->rateLimits->list();

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.organization.rate_limits.list

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

```text wrap
{
  "data": [
    {
      "type": "rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Hq7YkP3mZ9dTwRx4cVbN2s",
        "display_name": "Claude Opus 5.5"
      },
      "models": ["claude-opus-5-5"],
      "limits": [
        { "type": "requests_per_minute", "value": 4000 },
        { "type": "input_tokens_per_minute", "value": 10000000 },
        { "type": "output_tokens_per_minute", "value": 800000 }
      ]
    },
    {
      "type": "rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Kd5wMv8nSq2LcXy6tRfJ4b",
        "display_name": "Claude Opus 4.x"
      },
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        { "type": "requests_per_minute", "value": 4000 },
        { "type": "input_tokens_per_minute", "value": 10000000 },
        { "type": "output_tokens_per_minute", "value": 800000 }
      ]
    },
    {
      "type": "rate_limit",
      "group_type": "batch",
      "group": { "type": "batch", "id": "rlg_01Wn3pBz6kCg9vHtQ7mLxD5a" },
      "models": null,
      "limits": [{ "type": "enqueued_batch_requests", "value": 500000 }]
    }
  ],
  "next_page": null
}
```

### Look up the limits for a specific model

Pass any model ID or alias as the `model` query parameter to return only the entry that contains it:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits?model=claude-opus-5" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:rate-limits list --model claude-opus-5
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.rate_limits.list(model="claude-opus-5")

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.rateLimits.list({ model: "claude-opus-5" });

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Organization.RateLimits.List(new()
  {
      Model = "claude-opus-5"
  });

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.OrganizationRateLimitListParams{
  	Model: anthropic.String(anthropic.ModelClaudeOpus5),
  })

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.organization.ratelimits.RateLimitListParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RateLimitListParams.builder()
          .model(Model.CLAUDE_OPUS_5.asString())
          .build();
      var rateLimits = client.organization().rateLimits().list(params);

      for (var entry : rateLimits.autoPager()) {
          var models = entry.models()
              .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
              .orElse("");
          IO.println(entry.group().type().asString() + models);
          for (var limit : entry.limits()) {
              IO.println("  " + limit.type() + ": " + limit.value());
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;

  $client = new Client();

  $rateLimits = $client->organization->rateLimits->list(
      model: Model::CLAUDE_OPUS_5->value,
  );

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.organization.rate_limits.list(model: Anthropic::Model::CLAUDE_OPUS_5)

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

If the model string doesn't match any group, the endpoint returns a 404 error. The `model` parameter is supported on the organization endpoint only; the workspace endpoint doesn't accept it.

## Workspace rate limits

The `/v1/organizations/workspaces/{workspace_id}/rate_limits` endpoint returns the rate limit overrides configured for a single workspace. To also see the values the workspace inherits, pass `include_inherited=true` (see [Include inherited values](https://platform.claude.com/docs/en/manage-claude/rate-limits-api#include-inherited-values)).

By default, the response only includes overrides, so anything missing from it is inherited from the organization:

* A group that is absent from `data` has no workspace override at all. The workspace inherits the organization-level limits for that group (it is not unlimited).
* Within a group that is present, a limiter type that is absent from `limits[]` has no workspace override for that limiter. The workspace inherits the organization value for it.
* For each limiter that is present, `org_limit` is the organization-level value for the same limiter, or `null` if the organization has no configured limit for that limiter type, and `source` is `{"type": "workspace"}`.

For complete parameter details and response schemas, see the [Workspace Rate Limits API reference](https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/list).

<Tip>
  To retrieve your organization's workspace IDs, use the [List Workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) endpoint, or find them in the [Claude Console](https://platform.claude.com/settings/workspaces). The default workspace cannot have rate limit overrides, and this endpoint returns a 404 error for it, with or without `include_inherited`; use the organization endpoint to read its limits.
</Tip>

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:workspaces:rate-limits list \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.workspaces.rate_limits.list(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.workspaces.rateLimits.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Organization.Workspaces.RateLimits.List(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.Workspaces.RateLimits.ListAutoPaging(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.OrganizationWorkspaceRateLimitListParams{},
  )

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.organization().workspaces().rateLimits()
      .list("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ");

  for (var entry : rateLimits.autoPager()) {
      var models = entry.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(entry.group().type().asString() + models);
      for (var limit : entry.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->organization->workspaces->rateLimits->list(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
  );

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  rate_limits = client.organization.workspaces.rate_limits.list(workspace_id)

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

```text wrap
{
  "data": [
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Hq7YkP3mZ9dTwRx4cVbN2s",
        "display_name": "Claude Opus 5.5"
      },
      "models": ["claude-opus-5-5"],
      "limits": [
        {
          "type": "requests_per_minute",
          "value": 1000,
          "org_limit": 4000,
          "source": { "type": "workspace" }
        },
        {
          "type": "input_tokens_per_minute",
          "value": 500000,
          "org_limit": 10000000,
          "source": { "type": "workspace" }
        }
      ]
    },
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Kd5wMv8nSq2LcXy6tRfJ4b",
        "display_name": "Claude Opus 4.x"
      },
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        {
          "type": "requests_per_minute",
          "value": 1000,
          "org_limit": 4000,
          "source": { "type": "workspace" }
        },
        {
          "type": "input_tokens_per_minute",
          "value": 500000,
          "org_limit": 10000000,
          "source": { "type": "workspace" }
        }
      ]
    }
  ],
  "next_page": null
}
```

### Include inherited values

To read a workspace's applicable limits in one request, add the optional `include_inherited` query parameter. It defaults to `false`; a value that isn't a Boolean returns a 400 error. With `include_inherited=true`:

* `data` has one entry for each group that applies to the workspace and has an organization-level value, even if the workspace overrides none of it. A model group applies when the workspace can access at least one of its models.
* Each entry's `limits[]` lists every limiter type the organization has a value for on that group, plus any type the workspace overrides. Each type appears once, with the workspace's override where one is stored and the organization's value otherwise, so one entry can mix the two.
* Each value's `source` tells them apart: `{"type": "workspace"}` is a stored override, and `{"type": "organization"}` is an inherited value, where `value` equals `org_limit`.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/rate_limits?include_inherited=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:workspaces:rate-limits list \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --include-inherited
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.workspaces.rate_limits.list(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      include_inherited=True,
  )

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value} ({limit.source.type})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.workspaces.rateLimits.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    { include_inherited: true }
  );

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value} (${limit.source.type})`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Organization.Workspaces.RateLimits.List(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      new() { IncludeInherited = true }
  );

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value} ({limit.Source.Type.GetString()})");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.Workspaces.RateLimits.ListAutoPaging(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.OrganizationWorkspaceRateLimitListParams{
  		IncludeInherited: anthropic.Bool(true),
  	},
  )

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d (%s)\n", limit.Type, limit.Value, limit.Source.Type)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.organization.workspaces.ratelimits.RateLimitListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RateLimitListParams.builder()
          .includeInherited(true)
          .build();
      var rateLimits = client.organization().workspaces().rateLimits()
          .list("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", params);

      for (var entry : rateLimits.autoPager()) {
          var models = entry.models()
              .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
              .orElse("");
          IO.println(entry.group().type().asString() + models);
          for (var limit : entry.limits()) {
              IO.println("  " + limit.type() + ": " + limit.value()
                  + " (" + limit.source().type().asString() + ")");
          }
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->organization->workspaces->rateLimits->list(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      includeInherited: true,
  );

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value} ({$limit->source->type})\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  rate_limits = client.organization.workspaces.rate_limits.list(workspace_id, include_inherited: true)

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value} (#{limit.source.type})"
    end
  end
  ```
</CodeGroup>

```text wrap
{
  "data": [
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Hq7YkP3mZ9dTwRx4cVbN2s",
        "display_name": "Claude Opus 5.5"
      },
      "models": ["claude-opus-5-5"],
      "limits": [
        {
          "type": "requests_per_minute",
          "value": 1000,
          "org_limit": 4000,
          "source": { "type": "workspace" }
        },
        {
          "type": "input_tokens_per_minute",
          "value": 500000,
          "org_limit": 10000000,
          "source": { "type": "workspace" }
        },
        {
          "type": "output_tokens_per_minute",
          "value": 800000,
          "org_limit": 800000,
          "source": { "type": "organization" }
        }
      ]
    },
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "group": {
        "type": "model_group",
        "id": "rlg_01Kd5wMv8nSq2LcXy6tRfJ4b",
        "display_name": "Claude Opus 4.x"
      },
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        {
          "type": "requests_per_minute",
          "value": 1000,
          "org_limit": 4000,
          "source": { "type": "workspace" }
        },
        {
          "type": "input_tokens_per_minute",
          "value": 500000,
          "org_limit": 10000000,
          "source": { "type": "workspace" }
        },
        {
          "type": "output_tokens_per_minute",
          "value": 800000,
          "org_limit": 800000,
          "source": { "type": "organization" }
        }
      ]
    },
    {
      "type": "workspace_rate_limit",
      "group_type": "batch",
      "group": { "type": "batch", "id": "rlg_01Wn3pBz6kCg9vHtQ7mLxD5a" },
      "models": null,
      "limits": [
        {
          "type": "enqueued_batch_requests",
          "value": 500000,
          "org_limit": 500000,
          "source": { "type": "organization" }
        }
      ]
    }
  ],
  "next_page": null
}
```

## Filtering by group type

Both endpoints accept an optional `group_type` query parameter that restricts the response to a single category:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits?group_type=batch" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:rate-limits list --group-type batch
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.organization.rate_limits.list(group_type="batch")

  for entry in rate_limits:
      models = f" ({', '.join(entry.models)})" if entry.models else ""
      print(f"{entry.group.type}{models}")
      for limit in entry.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.organization.rateLimits.list({ group_type: "batch" });

  for await (const entry of rateLimits) {
    const models = entry.models ? ` (${entry.models.join(", ")})` : "";
    console.log(`${entry.group.type}${models}`);
    for (const limit of entry.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Organization.RateLimits;

  AnthropicClient client = new();

  var rateLimits = await client.Organization.RateLimits.List(new()
  {
      GroupType = GroupType.Batch
  });

  await foreach (var entry in rateLimits.Paginate())
  {
      var models = entry.Models is null ? "" : $" ({string.Join(", ", entry.Models)})";
      Console.WriteLine($"{entry.Group.Type.GetString()}{models}");
      foreach (var limit in entry.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.OrganizationRateLimitListParams{
  	GroupType: anthropic.OrganizationRateLimitListParamsGroupTypeBatch,
  })

  for rateLimits.Next() {
  	entry := rateLimits.Current()
  	models := ""
  	if len(entry.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(entry.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", entry.Group.Type, models)
  	for _, limit := range entry.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.organization.ratelimits.RateLimitListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RateLimitListParams.builder()
          .groupType(RateLimitListParams.GroupType.BATCH)
          .build();
      var rateLimits = client.organization().rateLimits().list(params);

      for (var entry : rateLimits.autoPager()) {
          var models = entry.models()
              .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
              .orElse("");
          IO.println(entry.group().type().asString() + models);
          for (var limit : entry.limits()) {
              IO.println("  " + limit.type() + ": " + limit.value());
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Organization\RateLimits\RateLimitListParams\GroupType;
  // ...

  $client = new Client();

  $rateLimits = $client->organization->rateLimits->list(
      groupType: GroupType::BATCH,
  );

  foreach ($rateLimits->data as $entry) {
      $models = $entry->models ? ' (' . implode(', ', $entry->models) . ')' : '';
      echo "{$entry->group->type}{$models}\n";
      foreach ($entry->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.organization.rate_limits.list(group_type: :batch)

  rate_limits.data.each do |entry|
    models = entry.models ? " (#{entry.models.join(", ")})" : ""
    puts "#{entry.group.type}#{models}"
    entry.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

Valid values are `model_group`, `batch`, `token_count`, `files`, `skills`, and `web_search`.

## Pagination

Both endpoints accept a `page` query parameter and return a `next_page` field. Responses are currently always a single page, so `next_page` is `null`. Loop on `next_page` so your client paginates correctly without changes when the response grows.

## Frequently asked questions

### Which model strings appear in the `models` list?

Every model ID and alias that counts against the group, including dated IDs (such as `claude-sonnet-4-5-20250929`) and undated aliases (such as `claude-sonnet-4-5`). Look up any model string you pass to the Messages API and you'll find it in exactly one `model_group` entry.

### What does it mean if a group is missing from the workspace response?

By default, the workspace response lists only overrides, so a missing group has no workspace override and inherits the organization-level limit. Pass `include_inherited=true` to see inherited values on the workspace endpoint, or query the organization endpoint. With `include_inherited=true`, a group is missing only when it doesn't apply to the workspace or the organization has no limit set for it.

### Can I update rate limits with this API?

No. To set workspace rate limits, go to the [Rate limits](https://platform.claude.com/usage/limits) page in the Claude Console, select the workspace from the **Workspace** dropdown menu, and click **Edit** next to a model.

## See also

* [Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
* [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)
* [Admin API reference](https://platform.claude.com/docs/en/api/organization)
* [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces)
* [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
