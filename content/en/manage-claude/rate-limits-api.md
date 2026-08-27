---
title: Rate Limits API
url: https://platform.claude.com/docs/en/manage-claude/rate-limits-api
description: Programmatically query your organization's API rate limits with the Rate Limits API.
---

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The Rate Limits API provides programmatic access to the rate limits configured for your organization and its workspaces. This is the same information shown on the [Rate limits](https://platform.claude.com/settings/limits) page in the Claude Console.

Use this API to:

* **Keep gateways and proxies in sync:** Read your current limits at startup and on a schedule instead of hardcoding values that drift when Anthropic adjusts them.
* **Power internal alerting:** Compare usage data from the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) against your configured limits.
* **Audit workspace configuration:** Verify that workspace overrides match what your provisioning automation expects.

<Check>
  **Admin API key required.** These endpoints require an Admin API key, which is different from a standard Claude API key. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) to find where to create one for your organization type and which scopes to select.
</Check>

The SDK and CLI examples on this page construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable. The SDKs expose these endpoints as `client.beta.organization.rate_limits` and `client.beta.organization.workspaces.rate_limits`; the Python, TypeScript, C#, Go, and Java list methods return an iterator that follows `next_page` for you, while the PHP, Ruby, and curl examples read one page.

## Quick start

List the rate limits configured for your organization:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rate-limits list
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.beta.organization.rate_limits.list()

  for group in rate_limits:
      models = f" ({', '.join(group.models)})" if group.models else ""
      print(f"{group.group_type}{models}")
      for limit in group.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.beta.organization.rateLimits.list();

  for await (const group of rateLimits) {
    const models = group.models ? ` (${group.models.join(", ")})` : "";
    console.log(`${group.group_type}${models}`);
    for (const limit of group.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Beta.Organization.RateLimits.List();

  await foreach (var group in rateLimits.Paginate())
  {
      var models = group.Models is null ? "" : $" ({string.Join(", ", group.Models)})";
      Console.WriteLine($"{group.GroupType.Raw()}{models}");
      foreach (var limit in group.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Beta.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRateLimitListParams{})

  for rateLimits.Next() {
  	group := rateLimits.Current()
  	models := ""
  	if len(group.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(group.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", group.GroupType, models)
  	for _, limit := range group.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.beta().organization().rateLimits().list();

  for (var group : rateLimits.autoPager()) {
      var models = group.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(group.groupType().asString() + models);
      for (var limit : group.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->beta->organization->rateLimits->list();

  foreach ($rateLimits->data as $group) {
      $models = $group->models ? ' (' . implode(', ', $group->models) . ')' : '';
      echo "{$group->groupType}{$models}\n";
      foreach ($group->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.beta.organization.rate_limits.list

  rate_limits.data.each do |group|
    models = group.models ? " (#{group.models.join(", ")})" : ""
    puts "#{group.group_type}#{models}"
    group.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

## Organization rate limits

The `/v1/organizations/rate_limits` endpoint returns the rate limits applied at the organization level for the Messages API and its supporting resources. Limits for other products, such as [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), are not included.

### Key concepts

* **Rate limit groups:** Each entry in the response represents one rate limit group. Model rate limits are grouped so that several model versions share a single set of limits, and other groups cover resources such as the Message Batches API, the Files API, the Token Counting API, agent skills, and the web search tool.
* **`group_type`:** Identifies which category of limits the entry covers. See [Filtering by group type](https://platform.claude.com/docs/en/manage-claude/rate-limits-api#filtering-by-group-type) for the list of values.
* **`models` list:** For `model_group` entries, the `models` field lists every model ID and alias that counts against that group's limits. Use this list to look up which group any model string falls under. For other group types, `models` is `null`.
* **`limits` list:** Each group carries a list of `{type, value}` pairs. The `type` field identifies the limiter (such as `requests_per_minute`, `input_tokens_per_minute`, or `output_tokens_per_minute`) and `value` is the configured limit. See [Rate limits](https://platform.claude.com/docs/en/api/rate-limits) for how each limiter is measured and enforced.

For complete parameter details and response schemas, see the [Organization Rate Limits API reference](https://platform.claude.com/docs/en/api/admin/rate_limits/list).

### List all organization rate limits

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rate-limits list
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.beta.organization.rate_limits.list()

  for group in rate_limits:
      models = f" ({', '.join(group.models)})" if group.models else ""
      print(f"{group.group_type}{models}")
      for limit in group.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.beta.organization.rateLimits.list();

  for await (const group of rateLimits) {
    const models = group.models ? ` (${group.models.join(", ")})` : "";
    console.log(`${group.group_type}${models}`);
    for (const limit of group.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Beta.Organization.RateLimits.List();

  await foreach (var group in rateLimits.Paginate())
  {
      var models = group.Models is null ? "" : $" ({string.Join(", ", group.Models)})";
      Console.WriteLine($"{group.GroupType.Raw()}{models}");
      foreach (var limit in group.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Beta.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRateLimitListParams{})

  for rateLimits.Next() {
  	group := rateLimits.Current()
  	models := ""
  	if len(group.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(group.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", group.GroupType, models)
  	for _, limit := range group.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.beta().organization().rateLimits().list();

  for (var group : rateLimits.autoPager()) {
      var models = group.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(group.groupType().asString() + models);
      for (var limit : group.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->beta->organization->rateLimits->list();

  foreach ($rateLimits->data as $group) {
      $models = $group->models ? ' (' . implode(', ', $group->models) . ')' : '';
      echo "{$group->groupType}{$models}\n";
      foreach ($group->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.beta.organization.rate_limits.list

  rate_limits.data.each do |group|
    models = group.models ? " (#{group.models.join(", ")})" : ""
    puts "#{group.group_type}#{models}"
    group.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "rate_limit",
      "group_type": "model_group",
      "models": ["claude-opus-5"],
      "limits": [
        { "type": "requests_per_minute", "value": 4000 },
        { "type": "input_tokens_per_minute", "value": 10000000 },
        { "type": "output_tokens_per_minute", "value": 800000 }
      ]
    },
    {
      "type": "rate_limit",
      "group_type": "model_group",
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
  ant beta:organization:rate-limits list --model claude-opus-5
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.beta.organization.rate_limits.list(model="claude-opus-5")

  for group in rate_limits:
      models = f" ({', '.join(group.models)})" if group.models else ""
      print(f"{group.group_type}{models}")
      for limit in group.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.beta.organization.rateLimits.list({ model: "claude-opus-5" });

  for await (const group of rateLimits) {
    const models = group.models ? ` (${group.models.join(", ")})` : "";
    console.log(`${group.group_type}${models}`);
    for (const limit of group.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Beta.Organization.RateLimits.List(new()
  {
      Model = "claude-opus-5"
  });

  await foreach (var group in rateLimits.Paginate())
  {
      var models = group.Models is null ? "" : $" ({string.Join(", ", group.Models)})";
      Console.WriteLine($"{group.GroupType.Raw()}{models}");
      foreach (var limit in group.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Beta.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRateLimitListParams{
  	Model: anthropic.String(anthropic.ModelClaudeOpus5),
  })

  for rateLimits.Next() {
  	group := rateLimits.Current()
  	models := ""
  	if len(group.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(group.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", group.GroupType, models)
  	for _, limit := range group.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.ratelimits.RateLimitListParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RateLimitListParams.builder()
          .model(Model.CLAUDE_OPUS_5.asString())
          .build();
      var rateLimits = client.beta().organization().rateLimits().list(params);

      for (var group : rateLimits.autoPager()) {
          var models = group.models()
              .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
              .orElse("");
          IO.println(group.groupType().asString() + models);
          for (var limit : group.limits()) {
              IO.println("  " + limit.type() + ": " + limit.value());
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Messages\Model;

  $client = new Client();

  $rateLimits = $client->beta->organization->rateLimits->list(
      model: Model::CLAUDE_OPUS_5->value,
  );

  foreach ($rateLimits->data as $group) {
      $models = $group->models ? ' (' . implode(', ', $group->models) . ')' : '';
      echo "{$group->groupType}{$models}\n";
      foreach ($group->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.beta.organization.rate_limits.list(model: Anthropic::Model::CLAUDE_OPUS_5)

  rate_limits.data.each do |group|
    models = group.models ? " (#{group.models.join(", ")})" : ""
    puts "#{group.group_type}#{models}"
    group.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

If the model string doesn't match any group, the endpoint returns a 404 error. The `model` parameter is supported on the organization endpoint only; the workspace endpoint doesn't accept it.

## Workspace rate limits

The `/v1/organizations/workspaces/{workspace_id}/rate_limits` endpoint returns the rate limit overrides configured for a single workspace.

The response only includes overrides, so anything missing from it is inherited from the organization:

* A group that is absent from `data` has no workspace override at all. The workspace inherits the organization-level limits for that group (it is not unlimited).
* Within a group that is present, a limiter type that is absent from `limits[]` has no workspace override for that limiter. The workspace inherits the organization value for it.
* For each limiter that is present, `org_limit` is the organization-level value for the same limiter, or `null` if the organization has no configured limit for that limiter type.

For complete parameter details and response schemas, see the [Workspace Rate Limits API reference](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list).

<Tip>
  To retrieve your organization's workspace IDs, use the [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) endpoint, or find them in the [Claude Console](https://platform.claude.com/settings/workspaces). The default workspace cannot have rate limit overrides, so it has no entry on this endpoint; use the organization endpoint to read its limits.
</Tip>

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/rate_limits" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:workspaces:rate-limits list \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.beta.organization.workspaces.rate_limits.list(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  for group in rate_limits:
      models = f" ({', '.join(group.models)})" if group.models else ""
      print(f"{group.group_type}{models}")
      for limit in group.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.beta.organization.workspaces.rateLimits.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  for await (const group of rateLimits) {
    const models = group.models ? ` (${group.models.join(", ")})` : "";
    console.log(`${group.group_type}${models}`);
    for (const limit of group.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rateLimits = await client.Beta.Organization.Workspaces.RateLimits.List(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  await foreach (var group in rateLimits.Paginate())
  {
      var models = group.Models is null ? "" : $" ({string.Join(", ", group.Models)})";
      Console.WriteLine($"{group.GroupType.Raw()}{models}");
      foreach (var limit in group.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Beta.Organization.Workspaces.RateLimits.ListAutoPaging(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.BetaOrganizationWorkspaceRateLimitListParams{},
  )

  for rateLimits.Next() {
  	group := rateLimits.Current()
  	models := ""
  	if len(group.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(group.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", group.GroupType, models)
  	for _, limit := range group.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rateLimits = client.beta().organization().workspaces().rateLimits()
      .list("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ");

  for (var group : rateLimits.autoPager()) {
      var models = group.models()
          .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
          .orElse("");
      IO.println(group.groupType().asString() + models);
      for (var limit : group.limits()) {
          IO.println("  " + limit.type() + ": " + limit.value());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rateLimits = $client->beta->organization->workspaces->rateLimits->list(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
  );

  foreach ($rateLimits->data as $group) {
      $models = $group->models ? ' (' . implode(', ', $group->models) . ')' : '';
      echo "{$group->groupType}{$models}\n";
      foreach ($group->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  rate_limits = client.beta.organization.workspaces.rate_limits.list(workspace_id)

  rate_limits.data.each do |group|
    models = group.models ? " (#{group.models.join(", ")})" : ""
    puts "#{group.group_type}#{models}"
    group.limits.each do |limit|
      puts "  #{limit.type}: #{limit.value}"
    end
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "models": ["claude-opus-5"],
      "limits": [
        { "type": "requests_per_minute", "value": 1000, "org_limit": 4000 },
        { "type": "input_tokens_per_minute", "value": 500000, "org_limit": 10000000 }
      ]
    },
    {
      "type": "workspace_rate_limit",
      "group_type": "model_group",
      "models": [
        "claude-opus-4-5",
        "claude-opus-4-5-20251101",
        "claude-opus-4-6",
        "claude-opus-4-7",
        "claude-opus-4-8"
      ],
      "limits": [
        { "type": "requests_per_minute", "value": 1000, "org_limit": 4000 },
        { "type": "input_tokens_per_minute", "value": 500000, "org_limit": 10000000 }
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
  ant beta:organization:rate-limits list --group-type batch
  ```

  ```python Python
  client = anthropic.Anthropic()

  rate_limits = client.beta.organization.rate_limits.list(group_type="batch")

  for group in rate_limits:
      models = f" ({', '.join(group.models)})" if group.models else ""
      print(f"{group.group_type}{models}")
      for limit in group.limits:
          print(f"  {limit.type}: {limit.value}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rateLimits = await client.beta.organization.rateLimits.list({ group_type: "batch" });

  for await (const group of rateLimits) {
    const models = group.models ? ` (${group.models.join(", ")})` : "";
    console.log(`${group.group_type}${models}`);
    for (const limit of group.limits) {
      console.log(`  ${limit.type}: ${limit.value}`);
    }
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.RateLimits;

  AnthropicClient client = new();

  var rateLimits = await client.Beta.Organization.RateLimits.List(new()
  {
      GroupType = GroupType.Batch
  });

  await foreach (var group in rateLimits.Paginate())
  {
      var models = group.Models is null ? "" : $" ({string.Join(", ", group.Models)})";
      Console.WriteLine($"{group.GroupType.Raw()}{models}");
      foreach (var limit in group.Limits)
      {
          Console.WriteLine($"  {limit.Type}: {limit.Value}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rateLimits := client.Beta.Organization.RateLimits.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRateLimitListParams{
  	GroupType: anthropic.BetaOrganizationRateLimitListParamsGroupTypeBatch,
  })

  for rateLimits.Next() {
  	group := rateLimits.Current()
  	models := ""
  	if len(group.Models) > 0 {
  		models = fmt.Sprintf(" (%s)", strings.Join(group.Models, ", "))
  	}
  	fmt.Printf("%s%s\n", group.GroupType, models)
  	for _, limit := range group.Limits {
  		fmt.Printf("  %s: %d\n", limit.Type, limit.Value)
  	}
  }
  if err := rateLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.ratelimits.RateLimitListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RateLimitListParams.builder()
          .groupType(RateLimitListParams.GroupType.BATCH)
          .build();
      var rateLimits = client.beta().organization().rateLimits().list(params);

      for (var group : rateLimits.autoPager()) {
          var models = group.models()
              .map(modelIds -> " (" + String.join(", ", modelIds) + ")")
              .orElse("");
          IO.println(group.groupType().asString() + models);
          for (var limit : group.limits()) {
              IO.println("  " + limit.type() + ": " + limit.value());
          }
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\RateLimits\RateLimitListParams\GroupType;
  // ...

  $client = new Client();

  $rateLimits = $client->beta->organization->rateLimits->list(
      groupType: GroupType::BATCH,
  );

  foreach ($rateLimits->data as $group) {
      $models = $group->models ? ' (' . implode(', ', $group->models) . ')' : '';
      echo "{$group->groupType}{$models}\n";
      foreach ($group->limits as $limit) {
          echo "  {$limit->type}: {$limit->value}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rate_limits = client.beta.organization.rate_limits.list(group_type: :batch)

  rate_limits.data.each do |group|
    models = group.models ? " (#{group.models.join(", ")})" : ""
    puts "#{group.group_type}#{models}"
    group.limits.each do |limit|
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

The workspace has no override for that group and inherits the organization-level limit. Query the organization endpoint to see the inherited values.

### Can I update rate limits with this API?

No. To set workspace rate limits, open the workspace in the [Claude Console](https://platform.claude.com/settings/workspaces) and use the **Rate limits** tab.

## See also

* [Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
* [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)
* [Admin API reference](https://platform.claude.com/docs/en/api/admin)
* [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces)
* [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
