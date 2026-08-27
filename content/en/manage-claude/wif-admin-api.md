---
title: Manage WIF with the Admin API
url: https://platform.claude.com/docs/en/manage-claude/wif-admin-api
description: Create and manage Workload Identity Federation service accounts, issuers, and rules programmatically for infrastructure-as-code and CI workflows.
---

The Admin API lets you create and manage [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) resources programmatically: service accounts, federation issuers, and federation rules. Use it to keep your federation configuration in infrastructure as code, provision it from CI, and reproduce it across organizations instead of clicking through the Claude Console. These endpoints share the `/v1/organizations` path prefix with the rest of the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api).

## Prerequisites

Every request on this page authenticates with an OAuth bearer token that carries the `org:admin` scope. The scope is granted only to organization members with the admin, owner, or primary owner role, and it grants access to the whole organization: any workspace binding is ignored. There are two ways to obtain a token, and they carry different permissions: a token from your own login acts as a user, whereas a federated token acts as a service account and cannot perform every operation on this page.

### Interactive (your terminal)

Log in with the [`ant` CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) under a dedicated profile, requesting the `org:admin` scope (see [Admin access](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication#admin-access)), then export the bearer token. Logging in with `--profile admin` stores the `org:admin` credential under its own profile name and also makes it the CLI's active profile, and the exported variable applies to every SDK and CLI call in that shell; so use a shell you reserve for administration, unset the variable when you are done, and switch the CLI back with `ant profile activate default`:

```bash CLI
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Interactive tokens are short-lived; if requests start returning 401, re-run the export command (it refreshes the token automatically).

The SDKs and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically; leave `ANTHROPIC_API_KEY` unset in the same shell, because these endpoints reject API keys and some clients prefer the key when both are set.

### Workload (CI and automation)

Create a federation rule with `oauth_scope: org:admin` that targets a service account whose `organization_role` is `admin`. The rule itself must be created in the Claude Console: granting a workload organization-admin access is a deliberate human action, not something automation can bootstrap for itself. The next section walks through this once-per-organization setup.

## Bootstrap a workload to manage WIF

One Console-created rule is enough to put the rest of your federation configuration under infrastructure as code: grant a single trusted workload the `org:admin` scope, and let that workload manage federation issuers and every workspace-scoped federation rule through this API.

<Steps>
  <Step title="Create the org:admin rule in the Console">
    In the Claude Console, go to **Settings → Workload identity** and select **Connect workload** to create one federation rule for your automation workload, for example a GitHub Actions workflow in your infrastructure repository. Under **Advanced rule options**, set the rule's OAuth scope to `org:admin`: the wizard then creates the new service account with the Admin organization role (or asks you to pick an existing admin service account as the target).

    <Warning>
      Match the rule to one exact workload identity, not a broad pattern. `subject_prefix` is an exact match unless it ends in `*`. For GitHub Actions, pin the subject to a protected branch, such as `repo:my-org/my-repo:ref:refs/heads/main`. A trailing wildcard such as `repo:my-org/my-repo:*` also matches `pull_request` runs, including runs triggered from forks, so anyone who could open a pull request against the repository could mint an `org:admin` token. See [Restrict which workflows can authenticate](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#restrict-which-workflows-can-authenticate).
    </Warning>
  </Step>

  <Step title="Exchange the workload's identity token">
    A workload that uses one of the SDKs or the `ant` CLI does not perform the exchange itself. Point the client at the rule with the federation environment variables and construct it with no arguments, exactly as for inference in [Construct the SDK client](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#construct-the-sdk-client); the client exchanges the identity token on the first request and, before the resulting access token expires, re-reads the identity token and exchanges it again:

    ```bash
    export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...        # the org:admin rule from step 1
    export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
    export ANTHROPIC_SERVICE_ACCOUNT_ID=svac_...       # the rule's target service account
    export ANTHROPIC_IDENTITY_TOKEN_FILE=/path/to/jwt  # or ANTHROPIC_IDENTITY_TOKEN
    # ANTHROPIC_WORKSPACE_ID is required only if the rule is enabled for all
    # workspaces or more than one; the org:admin endpoints ignore the binding.
    unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN       # both take precedence over federation
    ```

    The `ant` CLI reads the same variables, or takes `--federation-rule`, `--organization-id`, `--service-account-id`, and `--identity-token-file` flags. For a workload that runs more than one `ant` command, use a [federation profile](https://platform.claude.com/docs/en/manage-claude/wif-reference#profile-configuration-file) rather than flags or environment variables: with flags or variables the CLI exchanges the identity token again in every process, and identity tokens that carry a `jti` claim (GitHub Actions tokens do) are accepted only once, so a second command would be rejected; a profile is also the only way to give the CLI a `workspace_id` for the exchange when the rule is enabled for all workspaces or more than one, because unlike the SDKs the CLI does not pass `ANTHROPIC_WORKSPACE_ID` or `--workspace-id` into the exchange. Every SDK also accepts the same settings as explicit constructor arguments, shown per language in [Construct the SDK client](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#construct-the-sdk-client). See [Environment variables](https://platform.claude.com/docs/en/manage-claude/wif-reference#environment-variables) and [Credential precedence](https://platform.claude.com/docs/en/manage-claude/wif-reference#credential-precedence) for the full list and ordering.

    A workload that calls the API with curl exchanges the JWT for a short-lived `org:admin` bearer token itself, using the same [token exchange](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#authenticate-from-your-workload) as any other federated workload, and sends it in the `authorization: Bearer` header.
  </Step>

  <Step title="Manage issuers and workspace-scoped rules through the API">
    With the client configured (or, for curl, the minted token in `ANTHROPIC_AUTH_TOKEN`), the workload creates and manages your federation configuration using the endpoints on this page.
  </Step>
</Steps>

For the operations a workload-minted token can and cannot perform, see [Permissions and constraints](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#permissions-and-constraints). If you already created issuers, service accounts, or rules with the **Connect workload** wizard, list them with the following endpoints and import them into your infrastructure-as-code state instead of recreating them.

## Authentication

All endpoints live under `https://api.anthropic.com/v1/organizations/`. Every request to the federation and service-account endpoints needs the API version header and the bearer token:

In the SDKs these endpoints are `client.beta.organization.service_accounts`, `client.beta.organization.federation.issuers`, and `client.beta.organization.federation.rules` (`ant beta:organization:service-accounts`, `federation:issuers`, and `federation:rules` in the CLI). The SDK and CLI examples construct the default client, which sends the bearer token from `ANTHROPIC_AUTH_TOKEN`, or, in an automated workload, performs the federation exchange itself as described in [Bootstrap a workload to manage WIF](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#bootstrap-a-workload-to-manage-wif). SDK list methods fetch further pages on demand, so `limit` sets the page size; the PHP and Ruby examples read one page.

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/service_accounts" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:service-accounts list
  ```

  ```python Python
  client = anthropic.Anthropic()

  service_accounts = client.beta.organization.service_accounts.list()

  for service_account in service_accounts:
      print(f"{service_account.id}: {service_account.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  for await (const serviceAccount of client.beta.organization.serviceAccounts.list()) {
    console.log(`${serviceAccount.id}: ${serviceAccount.name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ServiceAccounts.List();

  await foreach (var serviceAccount in page.Paginate())
  {
      Console.WriteLine($"{serviceAccount.ID}: {serviceAccount.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  serviceAccounts := client.Beta.Organization.ServiceAccounts.ListAutoPaging(context.Background(), anthropic.BetaOrganizationServiceAccountListParams{})

  for serviceAccounts.Next() {
  	serviceAccount := serviceAccounts.Current()
  	fmt.Printf("%s: %s\n", serviceAccount.ID, serviceAccount.Name)
  }
  if err := serviceAccounts.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var serviceAccounts = client.beta().organization().serviceAccounts().list();

  for (var serviceAccount : serviceAccounts.autoPager()) {
      IO.println(serviceAccount.id() + ": " + serviceAccount.name());
  }
  ```

  ```php PHP
  $client = new Client();

  $serviceAccounts = $client->beta->organization->serviceAccounts->list();

  foreach ($serviceAccounts->getItems() as $serviceAccount) {
      echo "{$serviceAccount->id}: {$serviceAccount->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  service_accounts = client.beta.organization.service_accounts.list

  service_accounts.data.each do |service_account|
    puts "#{service_account.id}: #{service_account.name}"
  end
  ```
</CodeGroup>

Admin API keys are not accepted on these endpoints; the Admin API page's `x-api-key` examples do not apply here.

## Service accounts

A [service account](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#service-accounts) (`svac_...`) is the non-human identity that a federated token acts as. Set `organization_role` to `developer`.

Create a service account:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/service_accounts" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "inference-worker",
      "organization_role": "developer"
    }'
  ```

  ```bash CLI
  ant beta:organization:service-accounts create \
    --name inference-worker \
    --organization-role developer
  ```

  ```python Python
  client = anthropic.Anthropic()

  service_account = client.beta.organization.service_accounts.create(
      name="inference-worker", organization_role="developer"
  )

  print(f"id: {service_account.id}")
  print(f"name: {service_account.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const serviceAccount = await client.beta.organization.serviceAccounts.create({
    name: "inference-worker",
    organization_role: "developer"
  });

  console.log(`id: ${serviceAccount.id}`);
  console.log(`name: ${serviceAccount.name}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ServiceAccounts;

  AnthropicClient client = new();

  var serviceAccount = await client.Beta.Organization.ServiceAccounts.Create(new()
  {
      Name = "inference-worker",
      OrganizationRole = OrganizationRole.Developer
  });

  Console.WriteLine($"id: {serviceAccount.ID}");
  Console.WriteLine($"name: {serviceAccount.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  serviceAccount, err := client.Beta.Organization.ServiceAccounts.New(context.Background(), anthropic.BetaOrganizationServiceAccountNewParams{
  	Name:             "inference-worker",
  	OrganizationRole: anthropic.BetaOrganizationServiceAccountNewParamsOrganizationRoleDeveloper,
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", serviceAccount.ID)
  fmt.Printf("name: %s\n", serviceAccount.Name)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = ServiceAccountCreateParams.builder()
          .name("inference-worker")
          .organizationRole(ServiceAccountCreateParams.OrganizationRole.DEVELOPER)
          .build();
      var serviceAccount = client.beta().organization().serviceAccounts().create(params);

      IO.println("id: " + serviceAccount.id());
      IO.println("name: " + serviceAccount.name());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\ServiceAccounts\ServiceAccountCreateParams\OrganizationRole;
  // ...

  $client = new Client();

  $serviceAccount = $client->beta->organization->serviceAccounts->create(
      name: 'inference-worker',
      organizationRole: OrganizationRole::DEVELOPER,
  );

  echo "id: {$serviceAccount->id}\n";
  echo "name: {$serviceAccount->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  service_account = client.beta.organization.service_accounts.create(
    name: "inference-worker",
    organization_role: :developer
  )

  puts "id: #{service_account.id}"
  puts "name: #{service_account.name}"
  ```
</CodeGroup>

List service accounts:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/service_accounts?limit=20" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:service-accounts list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  service_accounts = client.beta.organization.service_accounts.list(limit=20)

  for service_account in service_accounts:
      print(f"{service_account.id}: {service_account.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  for await (const serviceAccount of client.beta.organization.serviceAccounts.list({
    limit: 20
  })) {
    console.log(`${serviceAccount.id}: ${serviceAccount.name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ServiceAccounts.List(new() { Limit = 20 });

  await foreach (var serviceAccount in page.Paginate())
  {
      Console.WriteLine($"{serviceAccount.ID}: {serviceAccount.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  serviceAccounts := client.Beta.Organization.ServiceAccounts.ListAutoPaging(context.Background(), anthropic.BetaOrganizationServiceAccountListParams{
  	Limit: anthropic.Int(20),
  })

  for serviceAccounts.Next() {
  	serviceAccount := serviceAccounts.Current()
  	fmt.Printf("%s: %s\n", serviceAccount.ID, serviceAccount.Name)
  }
  if err := serviceAccounts.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = ServiceAccountListParams.builder()
          .limit(20)
          .build();
      var serviceAccounts = client.beta().organization().serviceAccounts().list(params);

      for (var serviceAccount : serviceAccounts.autoPager()) {
          IO.println(serviceAccount.id() + ": " + serviceAccount.name());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $serviceAccounts = $client->beta->organization->serviceAccounts->list(limit: 20);

  foreach ($serviceAccounts->getItems() as $serviceAccount) {
      echo "{$serviceAccount->id}: {$serviceAccount->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  service_accounts = client.beta.organization.service_accounts.list(limit: 20)

  service_accounts.data.each do |service_account|
    puts "#{service_account.id}: #{service_account.name}"
  end
  ```
</CodeGroup>

Archive a service account:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS -X POST "https://api.anthropic.com/v1/organizations/service_accounts/svac_01ABCDEFabcdef0123456789XY/archive" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:service-accounts archive svac_01ABCDEFabcdef0123456789XY
  ```

  ```python Python
  client = anthropic.Anthropic()

  service_account = client.beta.organization.service_accounts.archive(
      "svac_01ABCDEFabcdef0123456789XY"
  )

  print(f"id: {service_account.id}")
  print(f"archived_at: {service_account.archived_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const serviceAccount = await client.beta.organization.serviceAccounts.archive(
    "svac_01ABCDEFabcdef0123456789XY"
  );

  console.log(`id: ${serviceAccount.id}`);
  console.log(`archived_at: ${serviceAccount.archived_at}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var serviceAccount = await client.Beta.Organization.ServiceAccounts.Archive(
      "svac_01ABCDEFabcdef0123456789XY"
  );

  Console.WriteLine($"id: {serviceAccount.ID}");
  Console.WriteLine($"archived_at: {serviceAccount.ArchivedAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  serviceAccount, err := client.Beta.Organization.ServiceAccounts.Archive(
  	context.Background(),
  	"svac_01ABCDEFabcdef0123456789XY",
  	anthropic.BetaOrganizationServiceAccountArchiveParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", serviceAccount.ID)
  fmt.Printf("archived_at: %s\n", serviceAccount.ArchivedAt)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var serviceAccount = client.beta().organization().serviceAccounts()
      .archive("svac_01ABCDEFabcdef0123456789XY");

  IO.println("id: " + serviceAccount.id());
  IO.println("archived_at: " + serviceAccount.archivedAt().orElseThrow());
  ```

  ```php PHP
  $client = new Client();

  $serviceAccount = $client->beta->organization->serviceAccounts->archive(
      serviceAccountID: 'svac_01ABCDEFabcdef0123456789XY',
  );

  echo "id: {$serviceAccount->id}\n";
  echo "archived_at: {$serviceAccount->archivedAt?->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  service_account_id = "svac_01ABCDEFabcdef0123456789XY"
  service_account = client.beta.organization.service_accounts.archive(service_account_id)

  puts "id: #{service_account.id}"
  puts "archived_at: #{service_account.archived_at}"
  ```
</CodeGroup>

The create endpoint returns the new service account:

```json
{
  "id": "svac_...",
  "name": "inference-worker",
  "organization_role": "developer",
  "created_at": "...",
  "type": "service_account",
  "...": "..."
}
```

To read or update a single service account, use `GET` and `POST` on `/v1/organizations/service_accounts/{service_account_id}`. A service account must be a member of a workspace before federated tokens can act in it. Every service account has an implicit membership in your organization's default workspace; add explicit memberships for other workspaces with `GET`, `POST`, and `DELETE` on `/v1/organizations/service_accounts/{service_account_id}/workspaces`, where `DELETE` targets `.../workspaces/{workspace_id}`.

For complete parameter details and response schemas, see the [Service accounts API reference](https://platform.claude.com/docs/en/api/admin/service_accounts).

## Federation issuers

A [federation issuer](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#federation-issuers) (`fdis_...`) registers an OIDC identity provider with your organization. The `jwks` field is a discriminated union that controls how Anthropic fetches the provider's signing keys:

| `jwks` value                             | When to use                                                                       |
| ---------------------------------------- | --------------------------------------------------------------------------------- |
| `{"type": "discovery"}`                  | The provider serves `/.well-known/openid-configuration` at the issuer URL.        |
| `{"type": "explicit_url", "url": "..."}` | Point at a JWKS endpoint directly.                                                |
| `{"type": "inline", "keys": [...]}`      | Upload the key set for providers that are not reachable from the public internet. |

Register an issuer. This example registers GitHub Actions with JWKS discovery:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/federation_issuers" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "github-actions",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {"type": "discovery"}
    }'
  ```

  ```bash CLI
  ant beta:organization:federation:issuers create \
    --name github-actions \
    --issuer-url https://token.actions.githubusercontent.com \
    --jwks '{type: discovery}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  issuer = client.beta.organization.federation.issuers.create(
      name="github-actions",
      issuer_url="https://token.actions.githubusercontent.com",
      jwks={"type": "discovery"},
  )

  print(f"id: {issuer.id}")
  print(f"name: {issuer.name}")
  print(f"issuer_url: {issuer.issuer_url}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const issuer = await client.beta.organization.federation.issuers.create({
    name: "github-actions",
    issuer_url: "https://token.actions.githubusercontent.com",
    jwks: { type: "discovery" }
  });

  console.log(`id: ${issuer.id}`);
  console.log(`name: ${issuer.name}`);
  console.log(`issuer_url: ${issuer.issuer_url}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Federation.Issuers;

  AnthropicClient client = new();

  var issuer = await client.Beta.Organization.Federation.Issuers.Create(new()
  {
      Name = "github-actions",
      IssuerUrl = "https://token.actions.githubusercontent.com",
      Jwks = new BetaJwksDiscovery()
  });

  Console.WriteLine($"id: {issuer.ID}");
  Console.WriteLine($"name: {issuer.Name}");
  Console.WriteLine($"issuer_url: {issuer.IssuerUrl}");
  ```

  ```go Go
  client := anthropic.NewClient()

  issuer, err := client.Beta.Organization.Federation.Issuers.New(context.Background(), anthropic.BetaOrganizationFederationIssuerNewParams{
  	Name:      "github-actions",
  	IssuerURL: "https://token.actions.githubusercontent.com",
  	JWKS: anthropic.BetaOrganizationFederationIssuerNewParamsJWKSUnion{
  		OfDiscovery: &anthropic.BetaJWKSDiscoveryParam{},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", issuer.ID)
  fmt.Printf("name: %s\n", issuer.Name)
  fmt.Printf("issuer_url: %s\n", issuer.IssuerURL)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.federation.issuers.BetaJwksDiscovery;
  import com.anthropic.models.beta.organization.federation.issuers.IssuerCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = IssuerCreateParams.builder()
          .name("github-actions")
          .issuerUrl("https://token.actions.githubusercontent.com")
          .jwks(BetaJwksDiscovery.builder().build())
          .build();
      var issuer = client.beta().organization().federation().issuers().create(params);

      IO.println("id: " + issuer.id());
      IO.println("name: " + issuer.name());
      IO.println("issuer_url: " + issuer.issuerUrl());
  }
  ```

  ```php PHP
  $client = new Client();

  $issuer = $client->beta->organization->federation->issuers->create(
      name: 'github-actions',
      issuerURL: 'https://token.actions.githubusercontent.com',
      jwks: ['type' => 'discovery'],
  );

  echo "id: {$issuer->id}\n";
  echo "name: {$issuer->name}\n";
  echo "issuer_url: {$issuer->issuerURL}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  issuer = client.beta.organization.federation.issuers.create(
    name: "github-actions",
    issuer_url: "https://token.actions.githubusercontent.com",
    jwks: {type: :discovery}
  )

  puts "id: #{issuer.id}"
  puts "name: #{issuer.name}"
  puts "issuer_url: #{issuer.issuer_url}"
  ```
</CodeGroup>

List issuers:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/federation_issuers?limit=20" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:federation:issuers list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  issuers = client.beta.organization.federation.issuers.list(limit=20)

  for issuer in issuers:
      print(f"{issuer.id}: {issuer.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  for await (const issuer of client.beta.organization.federation.issuers.list({ limit: 20 })) {
    console.log(`${issuer.id}: ${issuer.name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Federation.Issuers.List(new() { Limit = 20 });

  await foreach (var issuer in page.Paginate())
  {
      Console.WriteLine($"{issuer.ID}: {issuer.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  issuers := client.Beta.Organization.Federation.Issuers.ListAutoPaging(context.Background(), anthropic.BetaOrganizationFederationIssuerListParams{
  	Limit: anthropic.Int(20),
  })

  for issuers.Next() {
  	issuer := issuers.Current()
  	fmt.Printf("%s: %s\n", issuer.ID, issuer.Name)
  }
  if err := issuers.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.federation.issuers.IssuerListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = IssuerListParams.builder()
          .limit(20)
          .build();
      var issuers = client.beta().organization().federation().issuers().list(params);

      for (var issuer : issuers.autoPager()) {
          IO.println(issuer.id() + ": " + issuer.name());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $issuers = $client->beta->organization->federation->issuers->list(limit: 20);

  foreach ($issuers->getItems() as $issuer) {
      echo "{$issuer->id}: {$issuer->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  issuers = client.beta.organization.federation.issuers.list(limit: 20)

  issuers.data.each do |issuer|
    puts "#{issuer.id}: #{issuer.name}"
  end
  ```
</CodeGroup>

Archive an issuer:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS -X POST "https://api.anthropic.com/v1/organizations/federation_issuers/fdis_01ABCDEFabcdef0123456789XY/archive" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:federation:issuers archive \
    --federation-issuer-id fdis_01ABCDEFabcdef0123456789XY
  ```

  ```python Python
  client = anthropic.Anthropic()

  issuer = client.beta.organization.federation.issuers.archive(
      "fdis_01ABCDEFabcdef0123456789XY"
  )

  print(f"id: {issuer.id}")
  print(f"archived_at: {issuer.archived_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const issuer = await client.beta.organization.federation.issuers.archive(
    "fdis_01ABCDEFabcdef0123456789XY"
  );

  console.log(`id: ${issuer.id}`);
  console.log(`archived_at: ${issuer.archived_at}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var issuer = await client.Beta.Organization.Federation.Issuers.Archive(
      "fdis_01ABCDEFabcdef0123456789XY"
  );

  Console.WriteLine($"id: {issuer.ID}");
  Console.WriteLine($"archived_at: {issuer.ArchivedAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  issuer, err := client.Beta.Organization.Federation.Issuers.Archive(
  	context.Background(),
  	"fdis_01ABCDEFabcdef0123456789XY",
  	anthropic.BetaOrganizationFederationIssuerArchiveParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", issuer.ID)
  fmt.Printf("archived_at: %s\n", issuer.ArchivedAt)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var issuer = client.beta().organization().federation().issuers()
      .archive("fdis_01ABCDEFabcdef0123456789XY");

  IO.println("id: " + issuer.id());
  IO.println("archived_at: " + issuer.archivedAt().orElseThrow());
  ```

  ```php PHP
  $client = new Client();

  $issuer = $client->beta->organization->federation->issuers->archive(
      federationIssuerID: 'fdis_01ABCDEFabcdef0123456789XY',
  );

  echo "id: {$issuer->id}\n";
  echo "archived_at: {$issuer->archivedAt?->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  issuer_id = "fdis_01ABCDEFabcdef0123456789XY"
  issuer = client.beta.organization.federation.issuers.archive(issuer_id)

  puts "id: #{issuer.id}"
  puts "archived_at: #{issuer.archived_at}"
  ```
</CodeGroup>

To read or update a single issuer, use `GET` and `POST` on `/v1/organizations/federation_issuers/{issuer_id}`. An OAuth caller cannot update an issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference`; see [Permissions and constraints](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#permissions-and-constraints).

For complete parameter details and response schemas, see the [Federation issuers API reference](https://platform.claude.com/docs/en/api/admin/federation_issuers).

## Federation rules

A [federation rule](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#federation-rules) (`fdrl_...`) binds an issuer to a service account: JWTs from the issuer that satisfy the rule's match conditions can mint tokens that act as the rule's target. The `workspace_id` in the create request enables the rule in that workspace at creation; add more workspaces later through the `/federation_rules/{rule_id}/workspaces` sub-resource. Either `workspace_id` or `applies_to_all_workspaces: true` is required on create.

Create a rule. This example lets GitHub Actions deploys from the main branch act as the service account:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/federation_rules" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "gha-deploy",
      "issuer_id": "fdis_01ABCDEFabcdef0123456789XY",
      "match": {
        "subject_prefix": "repo:my-org/my-repo:ref:refs/heads/main",
        "claims": {"repository_owner": "my-org"}
      },
      "target": {
        "type": "service_account",
        "service_account_id": "svac_01ABCDEFabcdef0123456789XY"
      },
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "oauth_scope": "workspace:developer",
      "token_lifetime_seconds": 600
    }'
  ```

  ```bash CLI
  ant beta:organization:federation:rules create <<'YAML'
  name: gha-deploy
  issuer_id: fdis_01ABCDEFabcdef0123456789XY
  match:
    subject_prefix: "repo:my-org/my-repo:ref:refs/heads/main"
    claims:
      repository_owner: my-org
  target:
    type: service_account
    service_account_id: svac_01ABCDEFabcdef0123456789XY
  workspace_id: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  oauth_scope: "workspace:developer"
  token_lifetime_seconds: 600
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  rule = client.beta.organization.federation.rules.create(
      name="gha-deploy",
      issuer_id="fdis_01ABCDEFabcdef0123456789XY",
      match={
          "subject_prefix": "repo:my-org/my-repo:ref:refs/heads/main",
          "claims": {"repository_owner": "my-org"},
      },
      target={
          "type": "service_account",
          "service_account_id": "svac_01ABCDEFabcdef0123456789XY",
      },
      workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      oauth_scope="workspace:developer",
      token_lifetime_seconds=600,
  )

  print(f"id: {rule.id}")
  print(f"name: {rule.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rule = await client.beta.organization.federation.rules.create({
    name: "gha-deploy",
    issuer_id: "fdis_01ABCDEFabcdef0123456789XY",
    match: {
      subject_prefix: "repo:my-org/my-repo:ref:refs/heads/main",
      claims: { repository_owner: "my-org" }
    },
    target: {
      type: "service_account",
      service_account_id: "svac_01ABCDEFabcdef0123456789XY"
    },
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    oauth_scope: "workspace:developer",
    token_lifetime_seconds: 600
  });

  console.log(`id: ${rule.id}`);
  console.log(`name: ${rule.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rule = await client.Beta.Organization.Federation.Rules.Create(new()
  {
      Name = "gha-deploy",
      IssuerID = "fdis_01ABCDEFabcdef0123456789XY",
      Match = new()
      {
          SubjectPrefix = "repo:my-org/my-repo:ref:refs/heads/main",
          Claims = new Dictionary<string, string> { ["repository_owner"] = "my-org" }
      },
      Target = new() { ServiceAccountID = "svac_01ABCDEFabcdef0123456789XY" },
      WorkspaceID = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      OAuthScope = "workspace:developer",
      TokenLifetimeSeconds = 600
  });

  Console.WriteLine($"id: {rule.ID}");
  Console.WriteLine($"name: {rule.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  rule, err := client.Beta.Organization.Federation.Rules.New(context.Background(), anthropic.BetaOrganizationFederationRuleNewParams{
  	Name:     "gha-deploy",
  	IssuerID: "fdis_01ABCDEFabcdef0123456789XY",
  	Match: anthropic.BetaFederationRuleMatchParam{
  		SubjectPrefix: anthropic.String("repo:my-org/my-repo:ref:refs/heads/main"),
  		Claims:        map[string]string{"repository_owner": "my-org"},
  	},
  	Target: anthropic.BetaServiceAccountTargetParam{
  		ServiceAccountID: "svac_01ABCDEFabcdef0123456789XY",
  	},
  	WorkspaceID:          anthropic.String("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"),
  	OAuthScope:           "workspace:developer",
  	TokenLifetimeSeconds: anthropic.Int(600),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", rule.ID)
  fmt.Printf("name: %s\n", rule.Name)
  ```

  ```java Java
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.organization.federation.rules.BetaFederationRuleMatch;
  import com.anthropic.models.beta.organization.federation.rules.BetaServiceAccountTarget;
  import com.anthropic.models.beta.organization.federation.rules.RuleCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var match = BetaFederationRuleMatch.builder()
          .subjectPrefix("repo:my-org/my-repo:ref:refs/heads/main")
          .claims(BetaFederationRuleMatch.Claims.builder()
              .putAdditionalProperty("repository_owner", JsonValue.from("my-org"))
              .build())
          .build();
      var params = RuleCreateParams.builder()
          .name("gha-deploy")
          .issuerId("fdis_01ABCDEFabcdef0123456789XY")
          .match(match)
          .target(BetaServiceAccountTarget.of("svac_01ABCDEFabcdef0123456789XY"))
          .workspaceId("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
          .oauthScope("workspace:developer")
          .tokenLifetimeSeconds(600)
          .build();
      var rule = client.beta().organization().federation().rules().create(params);

      IO.println("id: " + rule.id());
      IO.println("name: " + rule.name());
  }
  ```

  ```php PHP
  $client = new Client();

  $rule = $client->beta->organization->federation->rules->create(
      name: 'gha-deploy',
      issuerID: 'fdis_01ABCDEFabcdef0123456789XY',
      match: [
          'subjectPrefix' => 'repo:my-org/my-repo:ref:refs/heads/main',
          'claims' => ['repository_owner' => 'my-org'],
      ],
      target: [
          'type' => 'service_account',
          'serviceAccountID' => 'svac_01ABCDEFabcdef0123456789XY',
      ],
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      oauthScope: 'workspace:developer',
      tokenLifetimeSeconds: 600,
  );

  echo "id: {$rule->id}\n";
  echo "name: {$rule->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rule = client.beta.organization.federation.rules.create(
    name: "gha-deploy",
    issuer_id: "fdis_01ABCDEFabcdef0123456789XY",
    match: {
      subject_prefix: "repo:my-org/my-repo:ref:refs/heads/main",
      claims: {repository_owner: "my-org"}
    },
    target: {
      type: :service_account,
      service_account_id: "svac_01ABCDEFabcdef0123456789XY"
    },
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    oauth_scope: "workspace:developer",
    token_lifetime_seconds: 600
  )

  puts "id: #{rule.id}"
  puts "name: #{rule.name}"
  ```
</CodeGroup>

List rules, optionally filtered by issuer:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/federation_rules?issuer_id=fdis_01ABCDEFabcdef0123456789XY" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:federation:rules list \
    --issuer-id fdis_01ABCDEFabcdef0123456789XY
  ```

  ```python Python
  client = anthropic.Anthropic()

  rules = client.beta.organization.federation.rules.list(
      issuer_id="fdis_01ABCDEFabcdef0123456789XY"
  )

  for rule in rules:
      print(f"{rule.id}: {rule.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  for await (const rule of client.beta.organization.federation.rules.list({
    issuer_id: "fdis_01ABCDEFabcdef0123456789XY"
  })) {
    console.log(`${rule.id}: ${rule.name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Federation.Rules.List(new()
  {
      IssuerID = "fdis_01ABCDEFabcdef0123456789XY"
  });

  await foreach (var rule in page.Paginate())
  {
      Console.WriteLine($"{rule.ID}: {rule.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  rules := client.Beta.Organization.Federation.Rules.ListAutoPaging(context.Background(), anthropic.BetaOrganizationFederationRuleListParams{
  	IssuerID: anthropic.String("fdis_01ABCDEFabcdef0123456789XY"),
  })

  for rules.Next() {
  	rule := rules.Current()
  	fmt.Printf("%s: %s\n", rule.ID, rule.Name)
  }
  if err := rules.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.federation.rules.RuleListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RuleListParams.builder()
          .issuerId("fdis_01ABCDEFabcdef0123456789XY")
          .build();
      var rules = client.beta().organization().federation().rules().list(params);

      for (var rule : rules.autoPager()) {
          IO.println(rule.id() + ": " + rule.name());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $rules = $client->beta->organization->federation->rules->list(
      issuerID: 'fdis_01ABCDEFabcdef0123456789XY',
  );

  foreach ($rules->getItems() as $rule) {
      echo "{$rule->id}: {$rule->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rules = client.beta.organization.federation.rules.list(
    issuer_id: "fdis_01ABCDEFabcdef0123456789XY"
  )

  rules.data.each do |rule|
    puts "#{rule.id}: #{rule.name}"
  end
  ```
</CodeGroup>

Archive a rule:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS -X POST "https://api.anthropic.com/v1/organizations/federation_rules/fdrl_01ABCDEFabcdef0123456789XY/archive" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:federation:rules archive \
    --federation-rule-id fdrl_01ABCDEFabcdef0123456789XY
  ```

  ```python Python
  client = anthropic.Anthropic()

  rule = client.beta.organization.federation.rules.archive(
      "fdrl_01ABCDEFabcdef0123456789XY"
  )

  print(f"id: {rule.id}")
  print(f"archived_at: {rule.archived_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const rule = await client.beta.organization.federation.rules.archive(
    "fdrl_01ABCDEFabcdef0123456789XY"
  );

  console.log(`id: ${rule.id}`);
  console.log(`archived_at: ${rule.archived_at}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var rule = await client.Beta.Organization.Federation.Rules.Archive(
      "fdrl_01ABCDEFabcdef0123456789XY"
  );

  Console.WriteLine($"id: {rule.ID}");
  Console.WriteLine($"archived_at: {rule.ArchivedAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  rule, err := client.Beta.Organization.Federation.Rules.Archive(
  	context.Background(),
  	"fdrl_01ABCDEFabcdef0123456789XY",
  	anthropic.BetaOrganizationFederationRuleArchiveParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", rule.ID)
  fmt.Printf("archived_at: %s\n", rule.ArchivedAt)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var rule = client.beta().organization().federation().rules()
      .archive("fdrl_01ABCDEFabcdef0123456789XY");

  IO.println("id: " + rule.id());
  IO.println("archived_at: " + rule.archivedAt().orElseThrow());
  ```

  ```php PHP
  $client = new Client();

  $rule = $client->beta->organization->federation->rules->archive(
      federationRuleID: 'fdrl_01ABCDEFabcdef0123456789XY',
  );

  echo "id: {$rule->id}\n";
  echo "archived_at: {$rule->archivedAt?->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rule_id = "fdrl_01ABCDEFabcdef0123456789XY"
  rule = client.beta.organization.federation.rules.archive(rule_id)

  puts "id: #{rule.id}"
  puts "archived_at: #{rule.archived_at}"
  ```
</CodeGroup>

The list endpoint returns a page of rules and the cursor for the next page:

```json
{
  "data": [{ "id": "fdrl_...", "name": "gha-deploy", "...": "..." }],
  "next_page": "..."
}
```

To read or update a single rule, use `GET` and `POST` on `/v1/organizations/federation_rules/{rule_id}`. To manage the workspaces a rule can mint tokens in, use `GET` and `POST` on `/v1/organizations/federation_rules/{rule_id}/workspaces`, and `DELETE` on `/v1/organizations/federation_rules/{rule_id}/workspaces/{workspace_id}`.

For complete parameter details and response schemas, see the [Federation rules API reference](https://platform.claude.com/docs/en/api/admin/federation_rules).

## Permissions and constraints

<Note>
  * OAuth-authenticated callers can only create or modify rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`. To create or modify a rule with any other scope (such as `org:admin` or `workspace:manage_tunnels`), use the Console.
  * An OAuth caller cannot update a federation issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference` (such as `org:admin` or `workspace:manage_tunnels`). Consider registering a dedicated issuer for the bootstrap rule so the issuers behind workspace-scoped rules stay updatable through the API.
  * Admin API keys are not accepted on these endpoints, for reads or writes; use an `org:admin` OAuth token.
</Note>

A rule with `oauth_scope: org:admin` must target a service account whose `organization_role` is `admin`. Resource names must match `^[a-z0-9-]+$`, be 1 to 255 characters, and be unique within an organization for each resource type; for the full field-level constraints, see [Validation rules](https://platform.claude.com/docs/en/manage-claude/wif-reference#validation-rules).

## Pagination and archiving

The service-account, federation-issuer, and federation-rule list endpoints accept `limit` (1 to 100, default 20) and a `page` cursor taken from the previous response. Pass the response's `next_page` value as the `page` query parameter on the next request. The rule-workspaces sub-resource list returns the full set without pagination. Archived resources are hidden from lists by default; pass `include_archived=true` to include them.

Archiving is a soft delete and is idempotent: archiving an already-archived resource succeeds. Archiving an issuer or a service account returns `400` while a live federation rule still references it; archive the rule first.

## See also

* [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): concepts and the Console setup walkthrough
* [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference): environment variables, validation rules, OAuth scopes, and error codes
* [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api): the rest of the organization management surface
* [Admin API reference](https://platform.claude.com/docs/en/api/admin): generated request and response schemas for every Admin API endpoint
