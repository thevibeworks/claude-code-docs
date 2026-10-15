---
title: Spend Limits API
url: https://platform.claude.com/docs/en/manage-claude/spend-limits-api
description: Set a spend limit on each Claude Enterprise member, see where each member's spend limit is inherited from, and review or act on members' requests for a higher limit.
---

The Spend Limits API lets you set a spend limit on each Claude Enterprise member, see where each member's spend limit is inherited from, and review or act on members' requests for a higher limit.

For per-user and time-bucketed usage and cost *reporting*, see [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api).

<Check>
  **Scoped Admin API key required**

  These endpoints require an Admin API key with the `read:spend_limits` scope (for `GET` endpoints) or the `write:spend_limits` scope (for `POST` and `DELETE` endpoints). See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization) for where your primary owner creates one and which scopes to select. Pass the key in the `x-api-key` header on every request, together with the [`anthropic-version`](https://platform.claude.com/docs/en/api/versioning) header.
</Check>

<Note>
  The Spend Limits API is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations.
</Note>

## Overview

The API exposes eight endpoints across two resources:

| Resource                          | Endpoints                                                                                                                                                                                                                                                            | Use for                                                                                                           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Spend limits**                  | `GET /v1/organizations/spend_limits/effective`<br />`GET /v1/organizations/spend_limits/{spend_limit_id}`<br />`POST /v1/organizations/spend_limits`<br />`DELETE /v1/organizations/spend_limits/{spend_limit_id}`                                                   | Read each member's effective spend limit and period-to-date spend; set or clear a per-user override.              |
| **Spend limit increase requests** | `GET /v1/organizations/spend_limit_increase_requests`<br />`GET /v1/organizations/spend_limit_increase_requests/{id}`<br />`POST /v1/organizations/spend_limit_increase_requests/{id}/approve`<br />`POST /v1/organizations/spend_limit_increase_requests/{id}/deny` | List members' requests for a higher spend limit, with the context needed to decide; approve or deny each request. |

Use the **spend limits** endpoints to answer "what spend limit applies to each member, where does it come from, and how close are they to it?" and to set a per-user override. Use the **spend limit increase requests** endpoints to work the queue of member-submitted requests.

## Prerequisites

* Your organization must be on a Claude Enterprise plan.
* Usage credits must be turned on for your organization. Your primary owner can turn them on in claude.ai billing settings.

The SDK exposes these endpoints under `client.beta.organization.spend_limits` (typescript: `client.beta.organization.spendLimits`; csharp, go: `client.Beta.Organization.SpendLimits`; java: `client.beta().organization().spendLimits()`; php: `$client->beta->organization->spendLimits`), and the `ant` CLI under `ant beta:organization:spend-limits`. Both send the `anthropic-version` header for you. The examples read the Admin API key from the `ANTHROPIC_API_KEY` environment variable. The SDK and the CLI fetch more pages for you as you go through the results, so `limit` sets the page size, not the total (see [Pagination](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#pagination)).

## Quick start

List every member's effective monthly spend limit and period-to-date spend:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/spend_limits/effective?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits:effective list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  effective_limits = client.beta.organization.spend_limits.effective.list(limit=20)

  for effective_limit in effective_limits:
      scope = effective_limit.scope
      if scope.type == "user":
          amount = effective_limit.amount or "unlimited"
          print(f"{scope.user_id}: {effective_limit.period_to_date_spend} of {amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const effectiveLimits = await client.beta.organization.spendLimits.effective.list({
    limit: 20
  });

  for await (const effectiveLimit of effectiveLimits) {
    const { scope } = effectiveLimit;
    if (scope.type === "user") {
      const amount = effectiveLimit.amount ?? "unlimited";
      console.log(`${scope.user_id}: ${effectiveLimit.period_to_date_spend} of ${amount}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.SpendLimits.Effective.List(
      new() { Limit = 20 }
  );

  await foreach (var effectiveLimit in page.Paginate())
  {
      if (effectiveLimit.Scope.TryPickBetaSpendLimitUser(out var userScope))
      {
          var amount = effectiveLimit.Amount ?? "unlimited";
          Console.WriteLine($"{userScope.UserID}: {effectiveLimit.PeriodToDateSpend} of {amount}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  effectiveLimits := client.Beta.Organization.SpendLimits.Effective.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitEffectiveListParams{
  	Limit: anthropic.Int(20),
  })

  for effectiveLimits.Next() {
  	effectiveLimit := effectiveLimits.Current()
  	if userScope, ok := effectiveLimit.Scope.AsAny().(anthropic.BetaSpendLimitUserScope); ok {
  		amount := effectiveLimit.Amount
  		if !effectiveLimit.JSON.Amount.Valid() {
  			amount = "unlimited"
  		}
  		fmt.Printf("%s: %s of %s\n", userScope.UserID, effectiveLimit.PeriodToDateSpend, amount)
  	}
  }
  if err := effectiveLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.effective.EffectiveListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = EffectiveListParams.builder()
          .limit(20)
          .build();
      var effectiveLimits = client.beta().organization().spendLimits().effective().list(params);

      for (var effectiveLimit : effectiveLimits.autoPager()) {
          var amount = effectiveLimit.amount().orElse("unlimited");
          effectiveLimit.scope().user().ifPresent(userScope ->
              IO.println(userScope.userId() + ": " + effectiveLimit.periodToDateSpend() + " of " + amount)
          );
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
  // ...

  $client = new Client();

  $effectiveLimits = $client->beta->organization->spendLimits->effective->list(limit: 20);

  foreach ($effectiveLimits->pagingEachItem() as $effectiveLimit) {
      $scope = $effectiveLimit->scope;
      if ($scope instanceof SpendLimitUserScope) {
          $amount = $effectiveLimit->amount ?? 'unlimited';
          echo "{$scope->userID}: {$effectiveLimit->periodToDateSpend} of {$amount}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.spend_limits.effective.list(limit: 20)

  page.auto_paging_each do |effective_limit|
    scope = effective_limit.scope
    if scope.is_a?(Anthropic::Models::Beta::Organization::BetaSpendLimitUserScope)
      amount = effective_limit.amount || "unlimited"
      puts "#{scope.user_id}: #{effective_limit.period_to_date_spend} of #{amount}"
    end
  end
  ```
</CodeGroup>

## Key concepts

### The spend limit hierarchy

An **effective spend limit** applies to each member's spend, resolved from a hierarchy of scope levels. When a member has no per-user override, they inherit the spend limit configured for their group (if your organization uses group-based limits), their seat tier, or the organization-wide default. A group spend limit is a per-member default: each member inheriting it is gated against their own spend, not a pooled group budget.

Reading `GET /v1/organizations/spend_limits/effective` returns every current member with their resolved effective spend limit, where that limit was resolved from (`source`), and their period-to-date spend. Setting a per-user override with `POST /v1/organizations/spend_limits` pins a member to a specific spend limit regardless of what they would otherwise inherit. Deleting the override returns them to the inherited spend limit (or leaves them unlimited if none exists).

The `source` field on each member's row tells you which level their spend limit resolved from: `user` (a per-user override), `seat_tier`, `rbac_group`, or `organization`. Treat scope types as an open set; fall through on unknown values rather than failing.

### Period

`period` is the recurring window over which the spend limit is enforced and spend resets. A spend limit is identified by its `(scope, period)` pair. Currently `monthly` is the only supported period; monthly spend resets at 00:00 UTC on the first of each calendar month. Treat `period` as an open set.

### Amounts and currency

All monetary values are strings in **minor units of the organization's billing currency** (cents, for USD). For example, `"50000"` represents 500.00 USD. Parse as a decimal and divide by 100 to display dollars; avoid binary floating-point for large values.

`amount` is **nullable**. In a member's effective row, `null` means **unlimited** (no spend limit) and `"0"` means the member cannot use Claude beyond their plan's included usage. On a configured spend-limit row (as returned by `GET /v1/organizations/spend_limits/{id}`), `null` only means no numeric spend limit is set; read the member's effective row to distinguish unlimited from included-usage-only.

`period_to_date_spend` is the member's spend accrued since the start of the current `period`, in the same minor-unit format; it may include a fractional part (for example, `"41280.125"`). It may read as `"0"` if the spend reading is temporarily unavailable; treat it as informational, not transactional.

### Increase request lifecycle

A **spend limit increase request** is created when a member clicks **Request more usage** in claude.ai. Requests are not created through this API. A request's `status` is one of:

| Status     | Meaning                                                                                                                                                                                                                                  |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pending`  | Awaiting admin action. The request normally carries a live `spend_summary` so you can see the member's current effective spend limit and period-to-date spend while deciding; `spend_summary` may be `null` if it could not be computed. |
| `approved` | The request was resolved with approval: either an admin approved it explicitly, another admin action raised the member's spend limit, or Anthropic support raised a spend limit on the organization's behalf. `spend_summary` is `null`. |
| `denied`   | An admin declined. `spend_summary` is `null`. The member can send a new request right away; only a `pending` request blocks a new one. An admin can still raise the member's spend limit directly at any time.                           |

Both `approved` and `denied` are terminal. A member has at most one `pending` request at a time.

Approving with `POST /v1/organizations/spend_limit_increase_requests/{id}/approve` writes the same per-user spend limit row that `POST /v1/organizations/spend_limits` writes. Setting a spend limit directly does **not** transition a pending request; use the approve endpoint to resolve a request.

By default, Anthropic emails the member when their request is approved or denied. Pass `suppress_notification: true` on approve or deny to suppress that email (for example, when your own system notifies the member).

## Versioning

Send the `anthropic-version` header on every request; see [API versions](https://platform.claude.com/docs/en/api/versioning) for the available versions.

## Rate limiting

All eight endpoints share a single per-organization limit of **60 requests per minute**. Requests over the limit return **429 Too Many Requests**.

## Pagination

`GET /v1/organizations/spend_limits/effective` and `GET /v1/organizations/spend_limit_increase_requests` are paginated with an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor; pass that cursor unchanged as the `page` parameter on the next request, and repeat until `next_page` is `null`.

**Do not change query parameters mid-sequence.** Cursors are bound to the filters that issued them. If you change `user_ids[]`, `period[]`, `status[]`, or `actor_ids[]` and pass an old cursor, you'll get a 400 with *"cursor does not match current query parameters"*. Start a new sequence from the first page instead.

## Serializing list parameters

List parameters use bracket notation: repeat the parameter name with `[]` for each value.

```text wrap
user_ids[]=user_01AbCdEfGh&user_ids[]=user_01JkLmNoPq
```

## Error responses

Error responses follow the standard shape documented in [Errors](https://platform.claude.com/docs/en/api/errors). Quote the `request_id` from the response body when contacting support.

## Spend limits

### List each member's effective spend limit

`GET /v1/organizations/spend_limits/effective` returns one row per current member, reflecting each member's effective spend limit, its `source` in the scope hierarchy, and their `period_to_date_spend`. Requires the `read:spend_limits` scope.

For complete parameter details and response schemas, see [List effective spend limits](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/effective/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/spend_limits/effective?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits:effective list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  effective_limits = client.beta.organization.spend_limits.effective.list(limit=20)

  for effective_limit in effective_limits:
      scope = effective_limit.scope
      if scope.type == "user":
          amount = effective_limit.amount or "unlimited"
          print(f"{scope.user_id}: {effective_limit.period_to_date_spend} of {amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const effectiveLimits = await client.beta.organization.spendLimits.effective.list({
    limit: 20
  });

  for await (const effectiveLimit of effectiveLimits) {
    const { scope } = effectiveLimit;
    if (scope.type === "user") {
      const amount = effectiveLimit.amount ?? "unlimited";
      console.log(`${scope.user_id}: ${effectiveLimit.period_to_date_spend} of ${amount}`);
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.SpendLimits.Effective.List(
      new() { Limit = 20 }
  );

  await foreach (var effectiveLimit in page.Paginate())
  {
      if (effectiveLimit.Scope.TryPickBetaSpendLimitUser(out var userScope))
      {
          var amount = effectiveLimit.Amount ?? "unlimited";
          Console.WriteLine($"{userScope.UserID}: {effectiveLimit.PeriodToDateSpend} of {amount}");
      }
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  effectiveLimits := client.Beta.Organization.SpendLimits.Effective.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitEffectiveListParams{
  	Limit: anthropic.Int(20),
  })

  for effectiveLimits.Next() {
  	effectiveLimit := effectiveLimits.Current()
  	if userScope, ok := effectiveLimit.Scope.AsAny().(anthropic.BetaSpendLimitUserScope); ok {
  		amount := effectiveLimit.Amount
  		if !effectiveLimit.JSON.Amount.Valid() {
  			amount = "unlimited"
  		}
  		fmt.Printf("%s: %s of %s\n", userScope.UserID, effectiveLimit.PeriodToDateSpend, amount)
  	}
  }
  if err := effectiveLimits.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.effective.EffectiveListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = EffectiveListParams.builder()
          .limit(20)
          .build();
      var effectiveLimits = client.beta().organization().spendLimits().effective().list(params);

      for (var effectiveLimit : effectiveLimits.autoPager()) {
          var amount = effectiveLimit.amount().orElse("unlimited");
          effectiveLimit.scope().user().ifPresent(userScope ->
              IO.println(userScope.userId() + ": " + effectiveLimit.periodToDateSpend() + " of " + amount)
          );
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
  // ...

  $client = new Client();

  $effectiveLimits = $client->beta->organization->spendLimits->effective->list(limit: 20);

  foreach ($effectiveLimits->pagingEachItem() as $effectiveLimit) {
      $scope = $effectiveLimit->scope;
      if ($scope instanceof SpendLimitUserScope) {
          $amount = $effectiveLimit->amount ?? 'unlimited';
          echo "{$scope->userID}: {$effectiveLimit->periodToDateSpend} of {$amount}\n";
      }
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.spend_limits.effective.list(limit: 20)

  page.auto_paging_each do |effective_limit|
    scope = effective_limit.scope
    if scope.is_a?(Anthropic::Models::Beta::Organization::BetaSpendLimitUserScope)
      amount = effective_limit.amount || "unlimited"
      puts "#{scope.user_id}: #{effective_limit.period_to_date_spend} of #{amount}"
    end
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
      "actor": {
        "type": "user_actor",
        "user_id": "user_01AbCdEfGh",
        "name": "Jane Smith",
        "email_address": "jane@example.com",
        "deleted": false
      },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly",
      "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
      "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
      "period_to_date_spend": "31402.5"
    }
  ],
  "next_page": "page_..."
}
```

### Get a single spend limit

`GET /v1/organizations/spend_limits/{spend_limit_id}` returns one configured spend limit by ID. Use it to inspect the row that a `spend_limit_id` field referenced. Requires the `read:spend_limits` scope.

For complete parameter details and response schemas, see [Retrieve a spend limit](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/spend_limits/spl_01AbCdEfGhIjKlMnOpQrSt" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits retrieve \
    --spend-limit-id spl_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  spend_limit = client.beta.organization.spend_limits.retrieve(
      "spl_01AbCdEfGhIjKlMnOpQrSt"
  )

  amount = spend_limit.amount or "none"
  print(f"id: {spend_limit.id}")
  print(f"amount: {amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const spendLimit = await client.beta.organization.spendLimits.retrieve(
    "spl_01AbCdEfGhIjKlMnOpQrSt"
  );

  const amount = spendLimit.amount ?? "none";
  console.log(`id: ${spendLimit.id}`);
  console.log(`amount: ${amount}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var spendLimit = await client.Beta.Organization.SpendLimits.Retrieve(
      "spl_01AbCdEfGhIjKlMnOpQrSt"
  );

  var amount = spendLimit.Amount ?? "none";
  Console.WriteLine($"id: {spendLimit.ID}");
  Console.WriteLine($"amount: {amount}");
  ```

  ```go Go
  client := anthropic.NewClient()

  spendLimit, err := client.Beta.Organization.SpendLimits.Get(context.Background(), "spl_01AbCdEfGhIjKlMnOpQrSt")
  if err != nil {
  	log.Fatal(err)
  }

  amount := spendLimit.Amount
  if !spendLimit.JSON.Amount.Valid() {
  	amount = "none"
  }

  fmt.Printf("id: %s\n", spendLimit.ID)
  fmt.Printf("amount: %s\n", amount)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var spendLimit = client.beta().organization().spendLimits()
      .retrieve("spl_01AbCdEfGhIjKlMnOpQrSt");

  var amount = spendLimit.amount().orElse("none");
  IO.println("id: " + spendLimit.id());
  IO.println("amount: " + amount);
  ```

  ```php PHP
  $client = new Client();

  $spendLimit = $client->beta->organization->spendLimits->retrieve('spl_01AbCdEfGhIjKlMnOpQrSt');

  $amount = $spendLimit->amount ?? 'none';
  echo "id: {$spendLimit->id}\n";
  echo "amount: {$amount}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  spend_limit = client.beta.organization.spend_limits.retrieve("spl_01AbCdEfGhIjKlMnOpQrSt")

  amount = spend_limit.amount || "none"
  puts "id: #{spend_limit.id}"
  puts "amount: #{amount}"
  ```
</CodeGroup>

### Set a per-user override

`POST /v1/organizations/spend_limits` sets a per-user spend limit override. This is an upsert keyed on `(scope, period)`: setting a limit for a user and period that already has one overwrites it in place. This endpoint accepts only `scope.type: "user"`; seat-tier, group, and organization-level defaults are configured in claude.ai settings. Requires the `write:spend_limits` scope.

For complete parameter details and response schemas, see [Create a spend limit](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/set) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/spend_limits" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"scope": {"type": "user", "user_id": "user_01AbCdEfGh"}, "amount": "75000"}'
  ```

  ```bash CLI
  ant beta:organization:spend-limits set \
    --scope '{type: user, user_id: user_01AbCdEfGh}' \
    --amount 75000
  ```

  ```python Python
  client = anthropic.Anthropic()

  spend_limit = client.beta.organization.spend_limits.set(
      scope={"type": "user", "user_id": "user_01AbCdEfGh"}, amount="75000"
  )

  print(f"id: {spend_limit.id}")
  print(f"amount: {spend_limit.amount}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const spendLimit = await client.beta.organization.spendLimits.set({
    scope: { type: "user", user_id: "user_01AbCdEfGh" },
    amount: "75000"
  });

  console.log(`id: ${spendLimit.id}`);
  console.log(`amount: ${spendLimit.amount}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.SpendLimits;

  AnthropicClient client = new();

  var spendLimit = await client.Beta.Organization.SpendLimits.Set(
      new()
      {
          Scope = new BetaSpendLimitUserScope("user_01AbCdEfGh"),
          Amount = "75000",
      }
  );

  Console.WriteLine($"id: {spendLimit.ID}");
  Console.WriteLine($"amount: {spendLimit.Amount}");
  ```

  ```go Go
  client := anthropic.NewClient()

  spendLimit, err := client.Beta.Organization.SpendLimits.Set(context.Background(), anthropic.BetaOrganizationSpendLimitSetParams{
  	Scope: anthropic.BetaOrganizationSpendLimitSetParamsScopeUnion{
  		OfUser: &anthropic.BetaSpendLimitUserScopeParam{UserID: "user_01AbCdEfGh"},
  	},
  	Amount: anthropic.String("75000"),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", spendLimit.ID)
  fmt.Printf("amount: %s\n", spendLimit.Amount)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.SpendLimitSetParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SpendLimitSetParams.builder()
          .userScope("user_01AbCdEfGh")
          .amount("75000")
          .build();
      var spendLimit = client.beta().organization().spendLimits().set(params);

      IO.println("id: " + spendLimit.id());
      IO.println("amount: " + spendLimit.amount().orElseThrow());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
  // ...

  $client = new Client();

  $spendLimit = $client->beta->organization->spendLimits->set(
      scope: SpendLimitUserScope::with(userID: 'user_01AbCdEfGh'),
      amount: '75000',
  );

  echo "id: {$spendLimit->id}\n";
  echo "amount: {$spendLimit->amount}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  spend_limit = client.beta.organization.spend_limits.set(
    scope: { type: :user, user_id: "user_01AbCdEfGh" },
    amount: "75000"
  )

  puts "id: #{spend_limit.id}"
  puts "amount: #{spend_limit.amount}"
  ```
</CodeGroup>

```json
{
  "type": "spend_limit",
  "id": "spl_01RsTuVwXyZaBcDeFgHiJk",
  "created_at": "2026-05-11T10:02:44Z",
  "updated_at": "2026-05-11T10:02:44Z",
  "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
  "amount": "75000",
  "currency": "USD",
  "period": "monthly"
}
```

### Remove a per-user override

`DELETE /v1/organizations/spend_limits/{spend_limit_id}` removes a per-user override, after which the member falls back to any inherited seat-tier, group, or organization default. Seat-tier, group, and organization-level rows cannot be deleted through this endpoint. Requires the `write:spend_limits` scope.

For complete parameter details and response schemas, see [Delete a spend limit](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/delete) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/spend_limits/spl_01RsTuVwXyZaBcDeFgHiJk" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits delete \
    --spend-limit-id spl_01RsTuVwXyZaBcDeFgHiJk
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_spend_limit = client.beta.organization.spend_limits.delete(
      "spl_01RsTuVwXyZaBcDeFgHiJk"
  )

  print(f"id: {deleted_spend_limit.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedSpendLimit = await client.beta.organization.spendLimits.delete(
    "spl_01RsTuVwXyZaBcDeFgHiJk"
  );

  console.log(`id: ${deletedSpendLimit.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedSpendLimit = await client.Beta.Organization.SpendLimits.Delete(
      "spl_01RsTuVwXyZaBcDeFgHiJk"
  );

  Console.WriteLine($"id: {deletedSpendLimit.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedSpendLimit, err := client.Beta.Organization.SpendLimits.Delete(context.Background(), "spl_01RsTuVwXyZaBcDeFgHiJk")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deletedSpendLimit.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedSpendLimit = client.beta().organization().spendLimits()
      .delete("spl_01RsTuVwXyZaBcDeFgHiJk");

  IO.println("id: " + deletedSpendLimit.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedSpendLimit = $client->beta->organization->spendLimits->delete('spl_01RsTuVwXyZaBcDeFgHiJk');

  echo "id: {$deletedSpendLimit->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  deleted_spend_limit = client.beta.organization.spend_limits.delete("spl_01RsTuVwXyZaBcDeFgHiJk")

  puts "id: #{deleted_spend_limit.id}"
  ```
</CodeGroup>

## Spend limit increase requests

### List increase requests

`GET /v1/organizations/spend_limit_increase_requests` lists requests, most recent first. Filter by `status[]` (`pending`, `approved`, `denied`) and `actor_ids[]`. The list excludes requests whose requester is no longer a member of the organization. Requires the `read:spend_limits` scope.

For complete parameter details and response schemas, see [List spend limit increase requests](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -g "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests?status[]=pending&limit=50" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits:increase-requests list \
    --status pending \
    --limit 50
  ```

  ```python Python
  client = anthropic.Anthropic()

  increase_requests = client.beta.organization.spend_limits.increase_requests.list(
      status=["pending"], limit=50
  )

  for increase_request in increase_requests:
      print(f"{increase_request.id}: {increase_request.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const increaseRequests = await client.beta.organization.spendLimits.increaseRequests.list({
    status: ["pending"],
    limit: 50
  });

  for await (const increaseRequest of increaseRequests) {
    console.log(`${increaseRequest.id}: ${increaseRequest.status}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.SpendLimits.IncreaseRequests;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.SpendLimits.IncreaseRequests.List(
      new() { Status = [BetaSpendLimitIncreaseRequestStatus.Pending], Limit = 50 }
  );

  await foreach (var increaseRequest in page.Paginate())
  {
      Console.WriteLine($"{increaseRequest.ID}: {increaseRequest.Status.Raw()}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  increaseRequests := client.Beta.Organization.SpendLimits.IncreaseRequests.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitIncreaseRequestListParams{
  	Status: []anthropic.BetaSpendLimitIncreaseRequestStatus{anthropic.BetaSpendLimitIncreaseRequestStatusPending},
  	Limit:  anthropic.Int(50),
  })

  for increaseRequests.Next() {
  	increaseRequest := increaseRequests.Current()
  	fmt.Printf("%s: %s\n", increaseRequest.ID, increaseRequest.Status)
  }
  if err := increaseRequests.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.increaserequests.BetaSpendLimitIncreaseRequestStatus;
  import com.anthropic.models.beta.organization.spendlimits.increaserequests.IncreaseRequestListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = IncreaseRequestListParams.builder()
          .addStatus(BetaSpendLimitIncreaseRequestStatus.PENDING)
          .limit(50)
          .build();
      var increaseRequests = client.beta().organization().spendLimits().increaseRequests().list(params);

      for (var increaseRequest : increaseRequests.autoPager()) {
          IO.println(increaseRequest.id() + ": " + increaseRequest.status().asString());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $increaseRequests = $client->beta->organization->spendLimits->increaseRequests->list(
      status: ['pending'],
      limit: 50,
  );

  foreach ($increaseRequests->pagingEachItem() as $increaseRequest) {
      echo "{$increaseRequest->id}: {$increaseRequest->status}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.spend_limits.increase_requests.list(status: [:pending], limit: 50)

  page.auto_paging_each do |increase_request|
    puts "#{increase_request.id}: #{increase_request.status}"
  end
  ```
</CodeGroup>

Each pending request carries a live `spend_summary` showing the requester's current effective spend limit and period-to-date spend, enough to decide without a separate lookup.

### Get a single increase request

`GET /v1/organizations/spend_limit_increase_requests/{id}` returns one request by ID. Requires the `read:spend_limits` scope.

For complete parameter details and response schemas, see [Retrieve a spend limit increase request](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:spend-limits:increase-requests retrieve \
    --spend-limit-increase-request-id slir_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  increase_request = client.beta.organization.spend_limits.increase_requests.retrieve(
      "slir_01AbCdEfGhIjKlMnOpQrSt"
  )

  print(f"id: {increase_request.id}")
  print(f"status: {increase_request.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const increaseRequest = await client.beta.organization.spendLimits.increaseRequests.retrieve(
    "slir_01AbCdEfGhIjKlMnOpQrSt"
  );

  console.log(`id: ${increaseRequest.id}`);
  console.log(`status: ${increaseRequest.status}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var increaseRequest = await client.Beta.Organization.SpendLimits.IncreaseRequests.Retrieve(
      "slir_01AbCdEfGhIjKlMnOpQrSt"
  );

  Console.WriteLine($"id: {increaseRequest.ID}");
  Console.WriteLine($"status: {increaseRequest.Status.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  increaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Get(context.Background(), "slir_01AbCdEfGhIjKlMnOpQrSt")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", increaseRequest.ID)
  fmt.Printf("status: %s\n", increaseRequest.Status)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var increaseRequest = client.beta().organization().spendLimits().increaseRequests()
      .retrieve("slir_01AbCdEfGhIjKlMnOpQrSt");

  IO.println("id: " + increaseRequest.id());
  IO.println("status: " + increaseRequest.status().asString());
  ```

  ```php PHP
  $client = new Client();

  $increaseRequest = $client->beta->organization->spendLimits->increaseRequests->retrieve(
      'slir_01AbCdEfGhIjKlMnOpQrSt',
  );

  echo "id: {$increaseRequest->id}\n";
  echo "status: {$increaseRequest->status}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  increase_request = client.beta.organization.spend_limits.increase_requests.retrieve(
    "slir_01AbCdEfGhIjKlMnOpQrSt"
  )

  puts "id: #{increase_request.id}"
  puts "status: #{increase_request.status}"
  ```
</CodeGroup>

### Approve an increase request

`POST /v1/organizations/spend_limit_increase_requests/{id}/approve` approves a pending request: it writes a per-user spend limit at the admin-supplied `amount` for the requester and transitions the request to `approved`. The request does not carry a requested amount; you supply the new spend limit on approval. Requires the `write:spend_limits` scope.

For complete parameter details and response schemas, see [Approve a spend limit increase request](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/approve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/approve" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"amount": "75000", "suppress_notification": true}'
  ```

  ```bash CLI
  ant beta:organization:spend-limits:increase-requests approve \
    --spend-limit-increase-request-id slir_01AbCdEfGhIjKlMnOpQrSt \
    --amount 75000 \
    --suppress-notification
  ```

  ```python Python
  client = anthropic.Anthropic()

  increase_request = client.beta.organization.spend_limits.increase_requests.approve(
      "slir_01AbCdEfGhIjKlMnOpQrSt", amount="75000", suppress_notification=True
  )

  print(f"id: {increase_request.id}")
  print(f"status: {increase_request.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const increaseRequest = await client.beta.organization.spendLimits.increaseRequests.approve(
    "slir_01AbCdEfGhIjKlMnOpQrSt",
    {
      amount: "75000",
      suppress_notification: true
    }
  );

  console.log(`id: ${increaseRequest.id}`);
  console.log(`status: ${increaseRequest.status}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var increaseRequest = await client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(
      "slir_01AbCdEfGhIjKlMnOpQrSt",
      new() { Amount = "75000", SuppressNotification = true }
  );

  Console.WriteLine($"id: {increaseRequest.ID}");
  Console.WriteLine($"status: {increaseRequest.Status.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  increaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(
  	context.Background(),
  	"slir_01AbCdEfGhIjKlMnOpQrSt",
  	anthropic.BetaOrganizationSpendLimitIncreaseRequestApproveParams{
  		Amount:               "75000",
  		SuppressNotification: anthropic.Bool(true),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", increaseRequest.ID)
  fmt.Printf("status: %s\n", increaseRequest.Status)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.increaserequests.IncreaseRequestApproveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = IncreaseRequestApproveParams.builder()
          .amount("75000")
          .suppressNotification(true)
          .build();
      var increaseRequest = client.beta().organization().spendLimits().increaseRequests()
          .approve("slir_01AbCdEfGhIjKlMnOpQrSt", params);

      IO.println("id: " + increaseRequest.id());
      IO.println("status: " + increaseRequest.status().asString());
  }
  ```

  ```php PHP
  $client = new Client();

  $increaseRequest = $client->beta->organization->spendLimits->increaseRequests->approve(
      'slir_01AbCdEfGhIjKlMnOpQrSt',
      amount: '75000',
      suppressNotification: true,
  );

  echo "id: {$increaseRequest->id}\n";
  echo "status: {$increaseRequest->status}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  increase_request = client.beta.organization.spend_limits.increase_requests.approve(
    "slir_01AbCdEfGhIjKlMnOpQrSt",
    amount: "75000",
    suppress_notification: true
  )

  puts "id: #{increase_request.id}"
  puts "status: #{increase_request.status}"
  ```
</CodeGroup>

### Deny an increase request

`POST /v1/organizations/spend_limit_increase_requests/{id}/deny` denies a pending request. Idempotent on `denied`: denying an already-denied request returns 200 with the existing resource. The endpoint rejects an attempt to deny an already-approved request so automation can distinguish a retry from a conflicting decision. Requires the `write:spend_limits` scope.

For complete parameter details and response schemas, see [Deny a spend limit increase request](https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests/deny) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/deny" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"suppress_notification": true}'
  ```

  ```bash CLI
  ant beta:organization:spend-limits:increase-requests deny \
    --spend-limit-increase-request-id slir_01AbCdEfGhIjKlMnOpQrSt \
    --suppress-notification
  ```

  ```python Python
  client = anthropic.Anthropic()

  increase_request = client.beta.organization.spend_limits.increase_requests.deny(
      "slir_01AbCdEfGhIjKlMnOpQrSt", suppress_notification=True
  )

  print(f"id: {increase_request.id}")
  print(f"status: {increase_request.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const increaseRequest = await client.beta.organization.spendLimits.increaseRequests.deny(
    "slir_01AbCdEfGhIjKlMnOpQrSt",
    {
      suppress_notification: true
    }
  );

  console.log(`id: ${increaseRequest.id}`);
  console.log(`status: ${increaseRequest.status}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var increaseRequest = await client.Beta.Organization.SpendLimits.IncreaseRequests.Deny(
      "slir_01AbCdEfGhIjKlMnOpQrSt",
      new() { SuppressNotification = true }
  );

  Console.WriteLine($"id: {increaseRequest.ID}");
  Console.WriteLine($"status: {increaseRequest.Status.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  increaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Deny(
  	context.Background(),
  	"slir_01AbCdEfGhIjKlMnOpQrSt",
  	anthropic.BetaOrganizationSpendLimitIncreaseRequestDenyParams{
  		SuppressNotification: anthropic.Bool(true),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", increaseRequest.ID)
  fmt.Printf("status: %s\n", increaseRequest.Status)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.spendlimits.increaserequests.IncreaseRequestDenyParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = IncreaseRequestDenyParams.builder()
          .suppressNotification(true)
          .build();
      var increaseRequest = client.beta().organization().spendLimits().increaseRequests()
          .deny("slir_01AbCdEfGhIjKlMnOpQrSt", params);

      IO.println("id: " + increaseRequest.id());
      IO.println("status: " + increaseRequest.status().asString());
  }
  ```

  ```php PHP
  $client = new Client();

  $increaseRequest = $client->beta->organization->spendLimits->increaseRequests->deny(
      'slir_01AbCdEfGhIjKlMnOpQrSt',
      suppressNotification: true,
  );

  echo "id: {$increaseRequest->id}\n";
  echo "status: {$increaseRequest->status}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  increase_request = client.beta.organization.spend_limits.increase_requests.deny(
    "slir_01AbCdEfGhIjKlMnOpQrSt",
    suppress_notification: true
  )

  puts "id: #{increase_request.id}"
  puts "status: #{increase_request.status}"
  ```
</CodeGroup>

## Example workflows

Some of these workflows combine the Spend Limits API with the [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api) cost endpoints. The Analytics cost endpoints are designed for organization-wide spend reporting across a date range. `GET /spend_limits/effective` returns the cap that currently applies to each member. Start a sweep with Analytics to discover which members to look at, then read their current caps with `/effective`.

Spend Limits endpoints require the `spend_limits` scopes and Analytics cost endpoints require `read:analytics`; see [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api) for how to provision access. The examples use one Admin API key that has the scopes of every API they call. A primary owner [selects these scopes when creating the key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#choose-scopes-for-a-claude-enterprise-key). All monetary values on both are decimal strings in minor units (cents). Both APIs paginate with an opaque cursor. Set an explicit `limit` and page through `next_page` until it's `null` to cover the whole organization.

### Automate the increase-request review flow

Run a scheduled job that fetches pending requests, applies your organization's approval policy, and resolves each one.

1. List pending requests:

   <CodeGroup>
     ```bash cURL
     curl -g "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests?status[]=pending&limit=100" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant beta:organization:spend-limits:increase-requests list \
       --status pending \
       --limit 100
     ```

     ```python Python
     client = anthropic.Anthropic()

     increase_requests = client.beta.organization.spend_limits.increase_requests.list(
         status=["pending"], limit=100
     )

     for increase_request in increase_requests:
         print(f"{increase_request.id}: {increase_request.status}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const increaseRequests = await client.beta.organization.spendLimits.increaseRequests.list({
       status: ["pending"],
       limit: 100
     });

     for await (const increaseRequest of increaseRequests) {
       console.log(`${increaseRequest.id}: ${increaseRequest.status}`);
     }
     ```

     ```csharp C#
     using Anthropic.Models.Beta.Organization.SpendLimits.IncreaseRequests;

     AnthropicClient client = new();

     var page = await client.Beta.Organization.SpendLimits.IncreaseRequests.List(
         new() { Status = [BetaSpendLimitIncreaseRequestStatus.Pending], Limit = 100 }
     );

     await foreach (var increaseRequest in page.Paginate())
     {
         Console.WriteLine($"{increaseRequest.ID}: {increaseRequest.Status.Raw()}");
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     increaseRequests := client.Beta.Organization.SpendLimits.IncreaseRequests.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitIncreaseRequestListParams{
     	Status: []anthropic.BetaSpendLimitIncreaseRequestStatus{anthropic.BetaSpendLimitIncreaseRequestStatusPending},
     	Limit:  anthropic.Int(100),
     })

     for increaseRequests.Next() {
     	increaseRequest := increaseRequests.Current()
     	fmt.Printf("%s: %s\n", increaseRequest.ID, increaseRequest.Status)
     }
     if err := increaseRequests.Err(); err != nil {
     	log.Fatal(err)
     }
     ```

     ```java Java
     import com.anthropic.models.beta.organization.spendlimits.increaserequests.BetaSpendLimitIncreaseRequestStatus;
     import com.anthropic.models.beta.organization.spendlimits.increaserequests.IncreaseRequestListParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = IncreaseRequestListParams.builder()
             .addStatus(BetaSpendLimitIncreaseRequestStatus.PENDING)
             .limit(100)
             .build();
         var increaseRequests = client.beta().organization().spendLimits().increaseRequests().list(params);

         for (var increaseRequest : increaseRequests.autoPager()) {
             IO.println(increaseRequest.id() + ": " + increaseRequest.status().asString());
         }
     }
     ```

     ```php PHP
     $client = new Client();

     $increaseRequests = $client->beta->organization->spendLimits->increaseRequests->list(
         status: ['pending'],
         limit: 100,
     );

     foreach ($increaseRequests->pagingEachItem() as $increaseRequest) {
         echo "{$increaseRequest->id}: {$increaseRequest->status}\n";
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     page = client.beta.organization.spend_limits.increase_requests.list(status: [:pending], limit: 100)

     page.auto_paging_each do |increase_request|
       puts "#{increase_request.id}: #{increase_request.status}"
     end
     ```
   </CodeGroup>

   Each request carries the requester's `actor.user_id` and a live `spend_summary` with their current effective `amount` and `period_to_date_spend`, enough to decide without a separate lookup.

2. Apply your policy. For example, auto-approve when the member's current `amount` is below a threshold, and route larger caps for manual review.

3. Resolve each request. To approve, supply the new cap:

   <CodeGroup>
     ```bash cURL
     curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/approve" \
       -H "content-type: application/json" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01" \
       -d '{"amount": "75000", "suppress_notification": true}'
     ```

     ```bash CLI
     ant beta:organization:spend-limits:increase-requests approve \
       --spend-limit-increase-request-id slir_01AbCdEfGhIjKlMnOpQrSt \
       --amount 75000 \
       --suppress-notification
     ```

     ```python Python
     client = anthropic.Anthropic()

     increase_request = client.beta.organization.spend_limits.increase_requests.approve(
         "slir_01AbCdEfGhIjKlMnOpQrSt", amount="75000", suppress_notification=True
     )

     print(f"id: {increase_request.id}")
     print(f"status: {increase_request.status}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const increaseRequest = await client.beta.organization.spendLimits.increaseRequests.approve(
       "slir_01AbCdEfGhIjKlMnOpQrSt",
       {
         amount: "75000",
         suppress_notification: true
       }
     );

     console.log(`id: ${increaseRequest.id}`);
     console.log(`status: ${increaseRequest.status}`);
     ```

     ```csharp C#
     AnthropicClient client = new();

     var increaseRequest = await client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(
         "slir_01AbCdEfGhIjKlMnOpQrSt",
         new() { Amount = "75000", SuppressNotification = true }
     );

     Console.WriteLine($"id: {increaseRequest.ID}");
     Console.WriteLine($"status: {increaseRequest.Status.Raw()}");
     ```

     ```go Go
     client := anthropic.NewClient()

     increaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(
     	context.Background(),
     	"slir_01AbCdEfGhIjKlMnOpQrSt",
     	anthropic.BetaOrganizationSpendLimitIncreaseRequestApproveParams{
     		Amount:               "75000",
     		SuppressNotification: anthropic.Bool(true),
     	},
     )
     if err != nil {
     	log.Fatal(err)
     }

     fmt.Printf("id: %s\n", increaseRequest.ID)
     fmt.Printf("status: %s\n", increaseRequest.Status)
     ```

     ```java Java
     import com.anthropic.models.beta.organization.spendlimits.increaserequests.IncreaseRequestApproveParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = IncreaseRequestApproveParams.builder()
             .amount("75000")
             .suppressNotification(true)
             .build();
         var increaseRequest = client.beta().organization().spendLimits().increaseRequests()
             .approve("slir_01AbCdEfGhIjKlMnOpQrSt", params);

         IO.println("id: " + increaseRequest.id());
         IO.println("status: " + increaseRequest.status().asString());
     }
     ```

     ```php PHP
     $client = new Client();

     $increaseRequest = $client->beta->organization->spendLimits->increaseRequests->approve(
         'slir_01AbCdEfGhIjKlMnOpQrSt',
         amount: '75000',
         suppressNotification: true,
     );

     echo "id: {$increaseRequest->id}\n";
     echo "status: {$increaseRequest->status}\n";
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     increase_request = client.beta.organization.spend_limits.increase_requests.approve(
       "slir_01AbCdEfGhIjKlMnOpQrSt",
       amount: "75000",
       suppress_notification: true
     )

     puts "id: #{increase_request.id}"
     puts "status: #{increase_request.status}"
     ```
   </CodeGroup>

   To deny, call the [deny endpoint](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#deny-an-increase-request) with the same ID instead. Pass `suppress_notification: true` when your own system notifies the requester.

### Identify members close to their spend limit

Find members approaching their cap so you can raise it before they're blocked.

1. Pull each member's month-to-date spend from the Analytics API (one row per member, highest spend first by default):

   <CodeGroup>
     ```bash cURL
     curl "https://api.anthropic.com/v1/organizations/analytics/user_cost_report?starting_at=2026-06-01T00:00:00Z&limit=1000" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant beta:organization:analytics:user-cost-report list \
       --starting-at 2026-06-01T00:00:00Z \
       --limit 1000
     ```

     ```python Python
     client = anthropic.Anthropic()

     cost_rows = client.beta.organization.analytics.user_cost_report.list(
         starting_at="2026-06-01T00:00:00Z", limit=1000
     )

     for cost_row in cost_rows:
         print(f"{cost_row.actor.user_id}: {cost_row.amount}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const costRows = await client.beta.organization.analytics.userCostReport.list({
       starting_at: "2026-06-01T00:00:00Z",
       limit: 1000
     });

     for await (const costRow of costRows) {
       console.log(`${costRow.actor.user_id}: ${costRow.amount}`);
     }
     ```

     ```csharp C#
     AnthropicClient client = new();

     var page = await client.Beta.Organization.Analytics.UserCostReport.List(
         new()
         {
             StartingAt = DateTimeOffset.Parse("2026-06-01T00:00:00Z"),
             Limit = 1000,
         }
     );

     await foreach (var costRow in page.Paginate())
     {
         Console.WriteLine($"{costRow.Actor.UserID}: {costRow.Amount}");
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     costRows := client.Beta.Organization.Analytics.UserCostReport.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUserCostReportListParams{
     	StartingAt: time.Date(2026, time.June, 1, 0, 0, 0, 0, time.UTC),
     	Limit:      anthropic.Int(1000),
     })

     for costRows.Next() {
     	costRow := costRows.Current()
     	fmt.Printf("%s: %s\n", costRow.Actor.UserID, costRow.Amount)
     }
     if err := costRows.Err(); err != nil {
     	log.Fatal(err)
     }
     ```

     ```java Java
     import com.anthropic.models.beta.organization.analytics.usercostreport.UserCostReportListParams;
     import java.time.OffsetDateTime;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = UserCostReportListParams.builder()
             .startingAt(OffsetDateTime.parse("2026-06-01T00:00:00Z"))
             .limit(1000)
             .build();
         var costRows = client.beta().organization().analytics().userCostReport().list(params);

         for (var costRow : costRows.autoPager()) {
             IO.println(costRow.actor().userId() + ": " + costRow.amount());
         }
     }
     ```

     ```php PHP
     $client = new Client();

     $costRows = $client->beta->organization->analytics->userCostReport->list(
         startingAt: new \DateTimeImmutable('2026-06-01T00:00:00Z'),
         limit: 1000,
     );

     foreach ($costRows->pagingEachItem() as $costRow) {
         echo "{$costRow->actor->userID}: {$costRow->amount}\n";
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     page = client.beta.organization.analytics.user_cost_report.list(
       starting_at: Time.utc(2026, 6, 1),
       limit: 1000
     )

     page.auto_paging_each do |cost_row|
       puts "#{cost_row.actor.user_id}: #{cost_row.amount}"
     end
     ```
   </CodeGroup>

   Each row contains `actor.user_id`, `actor.email_address`, and `amount` (the member's spend in cents). Page through `next_page` to cover the whole organization.

2. For the top spenders (or everyone above a dollar threshold), fetch effective caps in batches:

   <CodeGroup>
     ```bash cURL
     curl -g "https://api.anthropic.com/v1/organizations/spend_limits/effective?user_ids[]=user_01AbCdEfGh&user_ids[]=user_01JkLmNoPq&limit=100" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant beta:organization:spend-limits:effective list \
       --user-id user_01AbCdEfGh \
       --user-id user_01JkLmNoPq \
       --limit 100
     ```

     ```python Python
     client = anthropic.Anthropic()

     effective_limits = client.beta.organization.spend_limits.effective.list(
         user_ids=["user_01AbCdEfGh", "user_01JkLmNoPq"], limit=100
     )

     for effective_limit in effective_limits:
         scope = effective_limit.scope
         if scope.type == "user":
             amount = effective_limit.amount or "unlimited"
             print(f"{scope.user_id}: {effective_limit.period_to_date_spend} of {amount}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const effectiveLimits = await client.beta.organization.spendLimits.effective.list({
       user_ids: ["user_01AbCdEfGh", "user_01JkLmNoPq"],
       limit: 100
     });

     for await (const effectiveLimit of effectiveLimits) {
       const { scope } = effectiveLimit;
       if (scope.type === "user") {
         const amount = effectiveLimit.amount ?? "unlimited";
         console.log(`${scope.user_id}: ${effectiveLimit.period_to_date_spend} of ${amount}`);
       }
     }
     ```

     ```csharp C#
     AnthropicClient client = new();

     var page = await client.Beta.Organization.SpendLimits.Effective.List(
         new() { UserIds = ["user_01AbCdEfGh", "user_01JkLmNoPq"], Limit = 100 }
     );

     await foreach (var effectiveLimit in page.Paginate())
     {
         if (effectiveLimit.Scope.TryPickBetaSpendLimitUser(out var userScope))
         {
             var amount = effectiveLimit.Amount ?? "unlimited";
             Console.WriteLine($"{userScope.UserID}: {effectiveLimit.PeriodToDateSpend} of {amount}");
         }
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     effectiveLimits := client.Beta.Organization.SpendLimits.Effective.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitEffectiveListParams{
     	UserIDs: []string{"user_01AbCdEfGh", "user_01JkLmNoPq"},
     	Limit:   anthropic.Int(100),
     })

     for effectiveLimits.Next() {
     	effectiveLimit := effectiveLimits.Current()
     	if userScope, ok := effectiveLimit.Scope.AsAny().(anthropic.BetaSpendLimitUserScope); ok {
     		amount := effectiveLimit.Amount
     		if !effectiveLimit.JSON.Amount.Valid() {
     			amount = "unlimited"
     		}
     		fmt.Printf("%s: %s of %s\n", userScope.UserID, effectiveLimit.PeriodToDateSpend, amount)
     	}
     }
     if err := effectiveLimits.Err(); err != nil {
     	log.Fatal(err)
     }
     ```

     ```java Java
     import com.anthropic.models.beta.organization.spendlimits.effective.EffectiveListParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = EffectiveListParams.builder()
             .addUserId("user_01AbCdEfGh")
             .addUserId("user_01JkLmNoPq")
             .limit(100)
             .build();
         var effectiveLimits = client.beta().organization().spendLimits().effective().list(params);

         for (var effectiveLimit : effectiveLimits.autoPager()) {
             var amount = effectiveLimit.amount().orElse("unlimited");
             effectiveLimit.scope().user().ifPresent(userScope ->
                 IO.println(userScope.userId() + ": " + effectiveLimit.periodToDateSpend() + " of " + amount)
             );
         }
     }
     ```

     ```php PHP
     use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
     // ...

     $client = new Client();

     $effectiveLimits = $client->beta->organization->spendLimits->effective->list(
         userIDs: ['user_01AbCdEfGh', 'user_01JkLmNoPq'],
         limit: 100,
     );

     foreach ($effectiveLimits->pagingEachItem() as $effectiveLimit) {
         $scope = $effectiveLimit->scope;
         if ($scope instanceof SpendLimitUserScope) {
             $amount = $effectiveLimit->amount ?? 'unlimited';
             echo "{$scope->userID}: {$effectiveLimit->periodToDateSpend} of {$amount}\n";
         }
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     page = client.beta.organization.spend_limits.effective.list(
       user_ids: ["user_01AbCdEfGh", "user_01JkLmNoPq"],
       limit: 100
     )

     page.auto_paging_each do |effective_limit|
       scope = effective_limit.scope
       if scope.is_a?(Anthropic::Models::Beta::Organization::BetaSpendLimitUserScope)
         amount = effective_limit.amount || "unlimited"
         puts "#{scope.user_id}: #{effective_limit.period_to_date_spend} of #{amount}"
       end
     end
     ```
   </CodeGroup>

   Each row returns the cap as `amount` (`null` = unlimited, `"0"` = included usage only) alongside `period_to_date_spend`.

3. For each member with a positive cap, compute `period_to_date_spend / amount` and flag those at or above your threshold (for example, 80 percent). Treat a `"0"` cap as already at-limit. There is no server-side filter for this ratio.

4. Act on flagged members: raise the cap with `POST /v1/organizations/spend_limits`, approve a pending increase request if one exists, or reach out to the member.

### Find members with rapidly changing usage

Surface members whose spend has jumped week over week.

1. Pull per-member daily cost for the trailing two weeks from the Analytics API:

   <CodeGroup>
     ```bash cURL
     curl "https://api.anthropic.com/v1/organizations/analytics/user_cost_report?starting_at=2026-06-09T00:00:00Z&ending_at=2026-06-23T00:00:00Z&bucket_width=1d&limit=1000" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant beta:organization:analytics:user-cost-report list \
       --starting-at 2026-06-09T00:00:00Z \
       --ending-at 2026-06-23T00:00:00Z \
       --bucket-width 1d \
       --limit 1000
     ```

     ```python Python
     client = anthropic.Anthropic()

     cost_rows = client.beta.organization.analytics.user_cost_report.list(
         starting_at="2026-06-09T00:00:00Z",
         ending_at="2026-06-23T00:00:00Z",
         bucket_width="1d",
         limit=1000,
     )

     for cost_row in cost_rows:
         print(f"{cost_row.actor.user_id} {cost_row.starting_at}: {cost_row.amount}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const costRows = await client.beta.organization.analytics.userCostReport.list({
       starting_at: "2026-06-09T00:00:00Z",
       ending_at: "2026-06-23T00:00:00Z",
       bucket_width: "1d",
       limit: 1000
     });

     for await (const costRow of costRows) {
       console.log(`${costRow.actor.user_id} ${costRow.starting_at}: ${costRow.amount}`);
     }
     ```

     ```csharp C#
     using Anthropic.Models.Beta.Organization.Analytics.UserCostReport;

     AnthropicClient client = new();

     var page = await client.Beta.Organization.Analytics.UserCostReport.List(
         new()
         {
             StartingAt = DateTimeOffset.Parse("2026-06-09T00:00:00Z"),
             EndingAt = DateTimeOffset.Parse("2026-06-23T00:00:00Z"),
             BucketWidth = BucketWidth.Day,
             Limit = 1000,
         }
     );

     await foreach (var costRow in page.Paginate())
     {
         Console.WriteLine($"{costRow.Actor.UserID} {costRow.StartingAt}: {costRow.Amount}");
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     costRows := client.Beta.Organization.Analytics.UserCostReport.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAnalyticsUserCostReportListParams{
     	StartingAt:  time.Date(2026, time.June, 9, 0, 0, 0, 0, time.UTC),
     	EndingAt:    anthropic.Time(time.Date(2026, time.June, 23, 0, 0, 0, 0, time.UTC)),
     	BucketWidth: anthropic.BetaOrganizationAnalyticsUserCostReportListParamsBucketWidthDay,
     	Limit:       anthropic.Int(1000),
     })

     for costRows.Next() {
     	costRow := costRows.Current()
     	fmt.Printf("%s %s: %s\n", costRow.Actor.UserID, costRow.StartingAt, costRow.Amount)
     }
     if err := costRows.Err(); err != nil {
     	log.Fatal(err)
     }
     ```

     ```java Java
     import com.anthropic.models.beta.organization.analytics.usercostreport.UserCostReportListParams;
     import java.time.OffsetDateTime;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = UserCostReportListParams.builder()
             .startingAt(OffsetDateTime.parse("2026-06-09T00:00:00Z"))
             .endingAt(OffsetDateTime.parse("2026-06-23T00:00:00Z"))
             .bucketWidth(UserCostReportListParams.BucketWidth.DAY)
             .limit(1000)
             .build();
         var costRows = client.beta().organization().analytics().userCostReport().list(params);

         for (var costRow : costRows.autoPager()) {
             IO.println(costRow.actor().userId() + " " + costRow.startingAt().orElseThrow() + ": " + costRow.amount());
         }
     }
     ```

     ```php PHP
     $client = new Client();

     $costRows = $client->beta->organization->analytics->userCostReport->list(
         startingAt: new \DateTimeImmutable('2026-06-09T00:00:00Z'),
         endingAt: new \DateTimeImmutable('2026-06-23T00:00:00Z'),
         bucketWidth: '1d',
         limit: 1000,
     );

     foreach ($costRows->pagingEachItem() as $costRow) {
         $startingAt = $costRow->startingAt?->format(\DateTimeInterface::ATOM);
         echo "{$costRow->actor->userID} {$startingAt}: {$costRow->amount}\n";
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     page = client.beta.organization.analytics.user_cost_report.list(
       starting_at: Time.utc(2026, 6, 9),
       ending_at: Time.utc(2026, 6, 23),
       bucket_width: :"1d",
       limit: 1000
     )

     page.auto_paging_each do |cost_row|
       puts "#{cost_row.actor.user_id} #{cost_row.starting_at}: #{cost_row.amount}"
     end
     ```
   </CodeGroup>

   With `bucket_width` set, each member spans one row per day with usage. Page through `next_page` to collect every member's full series.

2. Group rows by `actor.user_id`. For each member, sum the most recent seven days and the prior seven days. Flag members whose recent week exceeds the prior week by your chosen multiple (for example, three). Recent-day cost is provisional and can be revised upward; for repeatable comparisons, set `ending_at` at or before a previously returned `data_refreshed_at` (see [Data availability and freshness](https://platform.claude.com/docs/en/manage-claude/analytics-api#data-availability-and-freshness)).

3. Act on flagged members: adjust the cap with `POST /v1/organizations/spend_limits`, or reach out.

### Temporarily raise a member's spend limit during an incident

Give an incident responder room to work while an incident is open: raise their spend cap when the incident starts, and roll it back after the incident closes. Gate the raise on your incident management system, for example by requiring a live incident ID with the member assigned to it.

1. Read the member's current cap, and record it for the rollback:

   <CodeGroup>
     ```bash cURL
     curl -g "https://api.anthropic.com/v1/organizations/spend_limits/effective?user_ids[]=user_01AbCdEfGh&period[]=monthly" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant beta:organization:spend-limits:effective list \
       --user-id user_01AbCdEfGh \
       --period monthly
     ```

     ```python Python
     client = anthropic.Anthropic()

     effective_limits = client.beta.organization.spend_limits.effective.list(
         user_ids=["user_01AbCdEfGh"], period=["monthly"]
     )

     for effective_limit in effective_limits:
         scope = effective_limit.scope
         if scope.type == "user":
             amount = effective_limit.amount or "unlimited"
             print(f"{scope.user_id}: {effective_limit.period_to_date_spend} of {amount}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const effectiveLimits = await client.beta.organization.spendLimits.effective.list({
       user_ids: ["user_01AbCdEfGh"],
       period: ["monthly"]
     });

     for await (const effectiveLimit of effectiveLimits) {
       const { scope } = effectiveLimit;
       if (scope.type === "user") {
         const amount = effectiveLimit.amount ?? "unlimited";
         console.log(`${scope.user_id}: ${effectiveLimit.period_to_date_spend} of ${amount}`);
       }
     }
     ```

     ```csharp C#
     using Anthropic.Models.Beta.Organization.SpendLimits.Effective;

     AnthropicClient client = new();

     var page = await client.Beta.Organization.SpendLimits.Effective.List(
         new() { UserIds = ["user_01AbCdEfGh"], Period = [Period.Monthly] }
     );

     await foreach (var effectiveLimit in page.Paginate())
     {
         if (effectiveLimit.Scope.TryPickBetaSpendLimitUser(out var userScope))
         {
             var amount = effectiveLimit.Amount ?? "unlimited";
             Console.WriteLine($"{userScope.UserID}: {effectiveLimit.PeriodToDateSpend} of {amount}");
         }
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     effectiveLimits := client.Beta.Organization.SpendLimits.Effective.ListAutoPaging(context.Background(), anthropic.BetaOrganizationSpendLimitEffectiveListParams{
     	UserIDs: []string{"user_01AbCdEfGh"},
     	Period:  []string{"monthly"},
     })

     for effectiveLimits.Next() {
     	effectiveLimit := effectiveLimits.Current()
     	if userScope, ok := effectiveLimit.Scope.AsAny().(anthropic.BetaSpendLimitUserScope); ok {
     		amount := effectiveLimit.Amount
     		if !effectiveLimit.JSON.Amount.Valid() {
     			amount = "unlimited"
     		}
     		fmt.Printf("%s: %s of %s\n", userScope.UserID, effectiveLimit.PeriodToDateSpend, amount)
     	}
     }
     if err := effectiveLimits.Err(); err != nil {
     	log.Fatal(err)
     }
     ```

     ```java Java
     import com.anthropic.models.beta.organization.spendlimits.effective.EffectiveListParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = EffectiveListParams.builder()
             .addUserId("user_01AbCdEfGh")
             .addPeriod(EffectiveListParams.Period.MONTHLY)
             .build();
         var effectiveLimits = client.beta().organization().spendLimits().effective().list(params);

         for (var effectiveLimit : effectiveLimits.autoPager()) {
             var amount = effectiveLimit.amount().orElse("unlimited");
             effectiveLimit.scope().user().ifPresent(userScope ->
                 IO.println(userScope.userId() + ": " + effectiveLimit.periodToDateSpend() + " of " + amount)
             );
         }
     }
     ```

     ```php PHP
     use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
     // ...

     $client = new Client();

     $effectiveLimits = $client->beta->organization->spendLimits->effective->list(
         userIDs: ['user_01AbCdEfGh'],
         period: ['monthly'],
     );

     foreach ($effectiveLimits->pagingEachItem() as $effectiveLimit) {
         $scope = $effectiveLimit->scope;
         if ($scope instanceof SpendLimitUserScope) {
             $amount = $effectiveLimit->amount ?? 'unlimited';
             echo "{$scope->userID}: {$effectiveLimit->periodToDateSpend} of {$amount}\n";
         }
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     page = client.beta.organization.spend_limits.effective.list(
       user_ids: ["user_01AbCdEfGh"],
       period: [:monthly]
     )

     page.auto_paging_each do |effective_limit|
       scope = effective_limit.scope
       if scope.is_a?(Anthropic::Models::Beta::Organization::BetaSpendLimitUserScope)
         amount = effective_limit.amount || "unlimited"
         puts "#{scope.user_id}: #{effective_limit.period_to_date_spend} of #{amount}"
       end
     end
     ```
   </CodeGroup>

2. Raise the cap:

   <CodeGroup>
     ```bash cURL
     curl -X POST "https://api.anthropic.com/v1/organizations/spend_limits" \
       -H "content-type: application/json" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01" \
       -d '{"scope": {"type": "user", "user_id": "user_01AbCdEfGh"}, "amount": "500000", "period": "monthly"}'
     ```

     ```bash CLI
     ant beta:organization:spend-limits set \
       --scope '{type: user, user_id: user_01AbCdEfGh}' \
       --amount 500000 \
       --period monthly
     ```

     ```python Python
     client = anthropic.Anthropic()

     spend_limit = client.beta.organization.spend_limits.set(
         scope={"type": "user", "user_id": "user_01AbCdEfGh"},
         amount="500000",
         period="monthly",
     )

     print(f"id: {spend_limit.id}")
     print(f"amount: {spend_limit.amount}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const spendLimit = await client.beta.organization.spendLimits.set({
       scope: { type: "user", user_id: "user_01AbCdEfGh" },
       amount: "500000",
       period: "monthly"
     });

     console.log(`id: ${spendLimit.id}`);
     console.log(`amount: ${spendLimit.amount}`);
     ```

     ```csharp C#
     using Anthropic.Models.Beta.Organization.SpendLimits;

     AnthropicClient client = new();

     var spendLimit = await client.Beta.Organization.SpendLimits.Set(
         new()
         {
             Scope = new BetaSpendLimitUserScope("user_01AbCdEfGh"),
             Amount = "500000",
             Period = BetaSpendLimitPeriod.Monthly,
         }
     );

     Console.WriteLine($"id: {spendLimit.ID}");
     Console.WriteLine($"amount: {spendLimit.Amount}");
     ```

     ```go Go
     client := anthropic.NewClient()

     spendLimit, err := client.Beta.Organization.SpendLimits.Set(context.Background(), anthropic.BetaOrganizationSpendLimitSetParams{
     	Scope: anthropic.BetaOrganizationSpendLimitSetParamsScopeUnion{
     		OfUser: &anthropic.BetaSpendLimitUserScopeParam{UserID: "user_01AbCdEfGh"},
     	},
     	Amount: anthropic.String("500000"),
     	Period: anthropic.BetaSpendLimitPeriodMonthly,
     })
     if err != nil {
     	log.Fatal(err)
     }

     fmt.Printf("id: %s\n", spendLimit.ID)
     fmt.Printf("amount: %s\n", spendLimit.Amount)
     ```

     ```java Java
     import com.anthropic.models.beta.organization.spendlimits.BetaSpendLimitPeriod;
     import com.anthropic.models.beta.organization.spendlimits.SpendLimitSetParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = SpendLimitSetParams.builder()
             .userScope("user_01AbCdEfGh")
             .amount("500000")
             .period(BetaSpendLimitPeriod.MONTHLY)
             .build();
         var spendLimit = client.beta().organization().spendLimits().set(params);

         IO.println("id: " + spendLimit.id());
         IO.println("amount: " + spendLimit.amount().orElseThrow());
     }
     ```

     ```php PHP
     use Anthropic\Beta\Organization\SpendLimits\SpendLimitUserScope;
     // ...

     $client = new Client();

     $spendLimit = $client->beta->organization->spendLimits->set(
         scope: SpendLimitUserScope::with(userID: 'user_01AbCdEfGh'),
         amount: '500000',
         period: 'monthly',
     );

     echo "id: {$spendLimit->id}\n";
     echo "amount: {$spendLimit->amount}\n";
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     spend_limit = client.beta.organization.spend_limits.set(
       scope: { type: :user, user_id: "user_01AbCdEfGh" },
       amount: "500000",
       period: :monthly
     )

     puts "id: #{spend_limit.id}"
     puts "amount: #{spend_limit.amount}"
     ```
   </CodeGroup>

3. If responders need broader access during an incident, pre-provision an incident-responders group whose [custom role](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles) grants it, and add the member for the duration:

   <CodeGroup>
     ```bash cURL
     curl -X POST "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn/members" \
       -H "content-type: application/json" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01" \
       -d '{"user_id": "user_01AbCdEfGh"}'
     ```

     ```bash CLI
     ant beta:organization:rbac-groups:members add \
       --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn \
       --user-id user_01AbCdEfGh
     ```

     ```python Python
     client = anthropic.Anthropic()

     member = client.beta.organization.rbac_groups.members.add(
         "rbac_group_01UvWxYzAbCdEfGhIjKlMn", user_id="user_01AbCdEfGh"
     )

     print(f"user_id: {member.user_id}")
     print(f"rbac_group_id: {member.rbac_group_id}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const member = await client.beta.organization.rbacGroups.members.add(
       "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
       {
         user_id: "user_01AbCdEfGh"
       }
     );

     console.log(`user_id: ${member.user_id}`);
     console.log(`rbac_group_id: ${member.rbac_group_id}`);
     ```

     ```csharp C#
     AnthropicClient client = new();

     var member = await client.Beta.Organization.RbacGroups.Members.Add(
         "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
         new() { UserID = "user_01AbCdEfGh" }
     );

     Console.WriteLine($"user_id: {member.UserID}");
     Console.WriteLine($"rbac_group_id: {member.RbacGroupID}");
     ```

     ```go Go
     client := anthropic.NewClient()

     member, err := client.Beta.Organization.RBACGroups.Members.Add(
     	context.Background(),
     	"rbac_group_01UvWxYzAbCdEfGhIjKlMn",
     	anthropic.BetaOrganizationRBACGroupMemberAddParams{
     		UserID: "user_01AbCdEfGh",
     	},
     )
     if err != nil {
     	log.Fatal(err)
     }

     fmt.Printf("user_id: %s\n", member.UserID)
     fmt.Printf("rbac_group_id: %s\n", member.RBACGroupID)
     ```

     ```java Java
     import com.anthropic.models.beta.organization.rbacgroups.members.MemberAddParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = MemberAddParams.builder()
             .userId("user_01AbCdEfGh")
             .build();
         var member = client.beta().organization().rbacGroups().members()
             .add("rbac_group_01UvWxYzAbCdEfGhIjKlMn", params);

         IO.println("user_id: " + member.userId());
         IO.println("rbac_group_id: " + member.rbacGroupId());
     }
     ```

     ```php PHP
     $client = new Client();

     $member = $client->beta->organization->rbacGroups->members->add(
         'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
         userID: 'user_01AbCdEfGh',
     );

     echo "user_id: {$member->userID}\n";
     echo "rbac_group_id: {$member->rbacGroupID}\n";
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     member = client.beta.organization.rbac_groups.members.add(
       "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
       user_id: "user_01AbCdEfGh"
     )

     puts "user_id: #{member.user_id}"
     puts "rbac_group_id: #{member.rbac_group_id}"
     ```
   </CodeGroup>

   See [User management](https://platform.claude.com/docs/en/manage-claude/user-management#groups) for the group endpoints.

4. When your incident system marks the incident closed, roll both changes back: restore the spend limit you recorded in step 1 (or delete the override with `DELETE /v1/organizations/spend_limits/{spend_limit_id}` if the member had none), and remove the member from the group with `DELETE /v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`.

## Frequently asked questions

### Does setting a spend limit directly resolve a member's pending increase request?

No. `POST /v1/organizations/spend_limits` writes the override but leaves the pending request untouched. Use `POST /v1/organizations/spend_limit_increase_requests/{id}/approve` to resolve the request and write the override in one call.

### What happens when I delete a per-user override?

The member falls back to whatever they'd inherit from the hierarchy: their group, seat-tier, or organization default. If no default exists at any level, the member is unlimited.

### Can I set a seat-tier or organization-wide default through this API?

No. Only per-user overrides can be written through this API. Seat-tier, group, and organization-level defaults are configured in claude.ai Organization settings.

### Why does `period_to_date_spend` sometimes read as `"0"` for an active member?

The spend reading can be temporarily unavailable, in which case the field reads `"0"` rather than erroring. Treat it as informational.

## See also

<CardGroup cols={2}>
  <Card title="Spend Limits API reference" href="https://platform.claude.com/docs/en/api/beta/organization/spend_limits">
    Generated request and response schemas for every Spend Limits API endpoint.
  </Card>

  <Card title="Spend Limit Increase Requests API reference" href="https://platform.claude.com/docs/en/api/beta/organization/spend_limits/increase_requests">
    Generated request and response schemas for the increase-request endpoints.
  </Card>

  <Card title="Analytics APIs" href="https://platform.claude.com/docs/en/manage-claude/analytics-api">
    Per-user and time-bucketed usage and cost reporting for Claude Enterprise.
  </Card>
</CardGroup>
