---
title: Admin API
url: https://platform.claude.com/docs/en/manage-claude/admin-api
description: Manage organization members, workspaces, invites, and API keys programmatically with the Admin API, using an Admin API key or an `org:admin` OAuth token.
---

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>

The [Admin API](https://platform.claude.com/docs/en/api/admin) lets you manage your organization's members, workspaces, invites, and API keys programmatically instead of by hand in the [Claude Console](https://platform.claude.com/).

<Check>
  **The Admin API requires special access**

  The Admin API accepts two credentials:

  * An **Admin API key** (starting with `sk-ant-admin...`) sent in the `x-api-key` header. Only organization members with the admin role can provision one. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys).
  * An **OAuth bearer token** with the `org:admin` scope sent in the `authorization: Bearer` header. Only members with the admin, owner, or primary owner role can obtain one. See [Obtain an OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token).
</Check>

<Note>
  **Claude Enterprise:** Claude Enterprise (claude.ai) organizations call the Admin API with a scoped API key created in claude.ai. From this page, only the members and invites endpoints apply to them. They also get Enterprise-only endpoints: group and custom-role reads, and [spend limits](https://platform.claude.com/docs/en/manage-claude/spend-limits-api). See [User management](https://platform.claude.com/docs/en/manage-claude/user-management).
</Note>

<Note>
  **Claude Platform on AWS:** Only the workspace endpoints (create, get, list, update, and archive on `/v1/organizations/workspaces`) are available on Claude Platform on AWS. Organization members, workspace members, invites, API keys, and the usage, cost, and rate limit reports aren't. See [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).
</Note>

## Authentication

Authenticate with either credential. An Admin API key covers most endpoints. The service-account, federation-issuer, and federation-rule endpoints accept only an `org:admin` OAuth token. The following examples call the [organization info endpoint](https://platform.claude.com/docs/en/manage-claude/admin-api#accessing-organization-info) both ways.

The Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs expose the Admin API under `client.beta.organization`, and the `ant` CLI under `ant beta:organization`. The examples on this page use the default client, which reads an Admin API key from `ANTHROPIC_API_KEY` or an OAuth bearer token from `ANTHROPIC_AUTH_TOKEN`. SDK list methods in Python, TypeScript, C#, Go, and Java return an iterator that fetches more pages on demand, so `limit` sets the page size, not the total. The PHP, Ruby, and curl examples return one page. In the CLI, `--limit` caps the results on the member, invite, workspace, workspace-member, and API-key lists. For each endpoint's parameters and responses, see the [Admin API reference](https://platform.claude.com/docs/en/api/admin).

### OAuth bearer token

Log in with the [`ant` CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) under a dedicated profile with the `org:admin` scope (see [Admin access](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication#admin-access)), then export the bearer token. `--profile admin` stores the `org:admin` credential under its own profile and makes it the CLI's active profile. The exported variable applies to every SDK and CLI call in that shell. Use a shell you reserve for administration, unset the variable when you're done, and switch the CLI back with `ant profile activate default`:

```bash CLI
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Interactive tokens are short-lived. If requests start returning 401, re-run the `export` command to refresh the token.

The SDKs and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically. Leave `ANTHROPIC_API_KEY` unset in the same shell so they send the bearer token. Automated workloads skip the login: they authenticate through workload identity federation, and the SDKs and CLI perform the token exchange from the federation environment variables. See [Bootstrap a workload to manage WIF](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#bootstrap-a-workload-to-manage-wif).

Call the Admin API with the exported token:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/me" \
    -H "authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization retrieve
  ```

  ```python Python
  client = anthropic.Anthropic()

  organization = client.beta.organization.retrieve()

  print(f"id: {organization.id}")
  print(f"name: {organization.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const organization = await client.beta.organization.retrieve();

  console.log(`id: ${organization.id}`);
  console.log(`name: ${organization.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var organization = await client.Beta.Organization.Retrieve();

  Console.WriteLine($"id: {organization.ID}");
  Console.WriteLine($"name: {organization.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  organization, err := client.Beta.Organization.Get(context.Background())
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", organization.ID)
  fmt.Printf("name: %s\n", organization.Name)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var organization = client.beta().organization().retrieve();

  IO.println("id: " + organization.id());
  IO.println("name: " + organization.name());
  ```

  ```php PHP
  $client = new Client();

  $organization = $client->beta->organization->retrieve();

  echo "id: {$organization->id}\n";
  echo "name: {$organization->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  organization = client.beta.organization.retrieve

  puts "id: #{organization.id}"
  puts "name: #{organization.name}"
  ```
</CodeGroup>

An `org:admin` token grants access to the whole organization, regardless of the workspace the underlying profile or [federation rule](https://platform.claude.com/docs/en/manage-claude/admin-api#federation-rules) is bound to.

For CI and other non-interactive workloads, mint the token with Workload Identity Federation instead of logging in interactively. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#workload-ci-and-automation).

### Admin API key

To create an Admin API key for your organization type, see [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys).

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS "https://api.anthropic.com/v1/organizations/me" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization retrieve
  ```

  ```python Python
  client = anthropic.Anthropic()

  organization = client.beta.organization.retrieve()

  print(f"id: {organization.id}")
  print(f"name: {organization.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const organization = await client.beta.organization.retrieve();

  console.log(`id: ${organization.id}`);
  console.log(`name: ${organization.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var organization = await client.Beta.Organization.Retrieve();

  Console.WriteLine($"id: {organization.ID}");
  Console.WriteLine($"name: {organization.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  organization, err := client.Beta.Organization.Get(context.Background())
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", organization.ID)
  fmt.Printf("name: %s\n", organization.Name)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var organization = client.beta().organization().retrieve();

  IO.println("id: " + organization.id());
  IO.println("name: " + organization.name());
  ```

  ```php PHP
  $client = new Client();

  $organization = $client->beta->organization->retrieve();

  echo "id: {$organization->id}\n";
  echo "name: {$organization->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  organization = client.beta.organization.retrieve

  puts "id: #{organization.id}"
  puts "name: #{organization.name}"
  ```
</CodeGroup>

## How the Admin API works

Authenticate with either credential from [Authentication](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication), then manage the following resources:

* Organization members and their roles
* Organization invites
* Workspaces and their members
* API keys
* Service accounts, federation issuers, and federation rules (`org:admin` OAuth token only)

Common uses include automating onboarding and offboarding, managing workspace access, and auditing API keys.

## Organization roles and permissions

There are five organization-level roles. For details, see [API Console roles and permissions](https://support.claude.com/en/articles/10186004-api-console-roles-and-permissions).

| Role               | Permissions                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| user               | Can use playground                                                             |
| claude\_code\_user | Can use playground and [Claude Code](https://code.claude.com/docs/en/overview) |
| developer          | Can use playground and manage API keys                                         |
| billing            | Can use playground and manage billing details                                  |
| admin              | Can do all of the preceding, plus manage users                                 |

Organization owners and primary owners have all admin permissions and can also manage admins. All references to the admin role on this page also apply to owners and primary owners.

## Key concepts

### Organization members

List [organization members](https://platform.claude.com/docs/en/api/admin-api/users/get-user), update their roles, and remove them.

List the members of your organization:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/users?limit=10" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:users list --limit 10
  ```

  ```python Python
  client = anthropic.Anthropic()

  users = client.beta.organization.users.list(limit=10)

  # Automatically fetches more pages as needed.
  for user in users:
      print(f"{user.id}: {user.email} ({user.role})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const users = await client.beta.organization.users.list({ limit: 10 });

  for await (const user of users) {
    console.log(`${user.id}: ${user.email} (${user.role})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Users.List(new() { Limit = 10 });

  await foreach (var user in page.Paginate())
  {
      Console.WriteLine($"{user.ID}: {user.Email} ({user.Role.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  users := client.Beta.Organization.Users.ListAutoPaging(context.Background(), anthropic.BetaOrganizationUserListParams{
  	Limit: anthropic.Int(10),
  })

  for users.Next() {
  	user := users.Current()
  	fmt.Printf("%s: %s (%s)\n", user.ID, user.Email, user.Role)
  }
  if err := users.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.users.UserListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserListParams.builder()
          .limit(10)
          .build();
      var users = client.beta().organization().users().list(params);

      for (var user : users.autoPager()) {
          IO.println(user.id() + ": " + user.email() + " (" + user.role().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $users = $client->beta->organization->users->list(limit: 10);

  foreach ($users->getItems() as $user) {
      echo "{$user->id}: {$user->email} ({$user->role})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  users = client.beta.organization.users.list(limit: 10)

  users.data.each do |user|
    puts "#{user.id}: #{user.email} (#{user.role})"
  end
  ```
</CodeGroup>

Update a member's role:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/users/user_01XyDMpzjS89pFZXqSFUBDr6" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{"role": "developer"}'
  ```

  ```bash CLI
  ant beta:organization:users update \
    --user-id user_01XyDMpzjS89pFZXqSFUBDr6 \
    --role developer
  ```

  ```python Python
  client = anthropic.Anthropic()

  user = client.beta.organization.users.update(
      "user_01XyDMpzjS89pFZXqSFUBDr6", role="developer"
  )

  print(f"id: {user.id}")
  print(f"role: {user.role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const user = await client.beta.organization.users.update("user_01XyDMpzjS89pFZXqSFUBDr6", {
    role: "developer"
  });

  console.log(`id: ${user.id}`);
  console.log(`role: ${user.role}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Users;
  // ...

  AnthropicClient client = new();

  var user = await client.Beta.Organization.Users.Update(
      "user_01XyDMpzjS89pFZXqSFUBDr6",
      new() { Role = Role.Developer }
  );

  Console.WriteLine($"id: {user.ID}");
  Console.WriteLine($"role: {user.Role.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  user, err := client.Beta.Organization.Users.Update(
  	context.Background(),
  	"user_01XyDMpzjS89pFZXqSFUBDr6",
  	anthropic.BetaOrganizationUserUpdateParams{
  		Role: anthropic.BetaOrganizationUserUpdateParamsRoleDeveloper,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", user.ID)
  fmt.Printf("role: %s\n", user.Role)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.users.UserUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserUpdateParams.builder()
          .role(UserUpdateParams.Role.DEVELOPER)
          .build();
      var user = client.beta().organization().users()
          .update("user_01XyDMpzjS89pFZXqSFUBDr6", params);

      IO.println("id: " + user.id());
      IO.println("role: " + user.role().asString());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Users\UserUpdateParams\Role;
  // ...

  $client = new Client();

  $user = $client->beta->organization->users->update(
      userID: 'user_01XyDMpzjS89pFZXqSFUBDr6',
      role: Role::DEVELOPER,
  );

  echo "id: {$user->id}\n";
  echo "role: {$user->role}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01XyDMpzjS89pFZXqSFUBDr6"
  user = client.beta.organization.users.update(user_id, role: :developer)

  puts "id: #{user.id}"
  puts "role: #{user.role}"
  ```
</CodeGroup>

Remove a member from the organization:

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/users/user_01XyDMpzjS89pFZXqSFUBDr6" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:users remove --user-id user_01XyDMpzjS89pFZXqSFUBDr6
  ```

  ```python Python
  client = anthropic.Anthropic()

  removed_user = client.beta.organization.users.remove("user_01XyDMpzjS89pFZXqSFUBDr6")

  print(f"id: {removed_user.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const removedUser = await client.beta.organization.users.remove(
    "user_01XyDMpzjS89pFZXqSFUBDr6"
  );

  console.log(`id: ${removedUser.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var removedUser = await client.Beta.Organization.Users.Remove("user_01XyDMpzjS89pFZXqSFUBDr6");

  Console.WriteLine($"id: {removedUser.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  removedUser, err := client.Beta.Organization.Users.Remove(context.Background(), "user_01XyDMpzjS89pFZXqSFUBDr6")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", removedUser.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var removedUser = client.beta().organization().users()
      .remove("user_01XyDMpzjS89pFZXqSFUBDr6");

  IO.println("id: " + removedUser.id());
  ```

  ```php PHP
  $client = new Client();

  $removedUser = $client->beta->organization->users->remove(
      userID: 'user_01XyDMpzjS89pFZXqSFUBDr6',
  );

  echo "id: {$removedUser->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01XyDMpzjS89pFZXqSFUBDr6"
  removed_user = client.beta.organization.users.remove(user_id)

  puts "id: #{removed_user.id}"
  ```
</CodeGroup>

### Organization invites

Invite users to your organization and manage pending [invites](https://platform.claude.com/docs/en/api/admin-api/invites/get-invite).

Invite a user to your organization:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/invites" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "email": "user@example.com",
      "role": "developer"
    }'
  ```

  ```bash CLI
  ant beta:organization:invites create --email user@example.com --role developer
  ```

  ```python Python
  client = anthropic.Anthropic()

  invite = client.beta.organization.invites.create(
      email="user@example.com", role="developer"
  )

  print(f"id: {invite.id}")
  print(f"email: {invite.email}")
  print(f"status: {invite.status}")
  print(f"expires_at: {invite.expires_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const invite = await client.beta.organization.invites.create({
    email: "user@example.com",
    role: "developer"
  });

  console.log(`id: ${invite.id}`);
  console.log(`email: ${invite.email}`);
  console.log(`status: ${invite.status}`);
  console.log(`expires_at: ${invite.expires_at}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Invites;
  // ...

  AnthropicClient client = new();

  var invite = await client.Beta.Organization.Invites.Create(new()
  {
      Email = "user@example.com",
      Role = Role.Developer
  });

  Console.WriteLine($"id: {invite.ID}");
  Console.WriteLine($"email: {invite.Email}");
  Console.WriteLine($"status: {invite.Status.Raw()}");
  Console.WriteLine($"expires_at: {invite.ExpiresAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  invite, err := client.Beta.Organization.Invites.New(context.Background(), anthropic.BetaOrganizationInviteNewParams{
  	Email: "user@example.com",
  	Role:  anthropic.BetaOrganizationInviteNewParamsRoleDeveloper,
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", invite.ID)
  fmt.Printf("email: %s\n", invite.Email)
  fmt.Printf("status: %s\n", invite.Status)
  fmt.Printf("expires_at: %s\n", invite.ExpiresAt.Format(time.RFC3339))
  ```

  ```java Java
  import com.anthropic.models.beta.organization.invites.InviteCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InviteCreateParams.builder()
          .email("user@example.com")
          .role(InviteCreateParams.Role.DEVELOPER)
          .build();
      var invite = client.beta().organization().invites().create(params);

      IO.println("id: " + invite.id());
      IO.println("email: " + invite.email());
      IO.println("status: " + invite.status().asString());
      IO.println("expires_at: " + invite.expiresAt());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Invites\InviteCreateParams\Role;
  // ...

  $client = new Client();

  $invite = $client->beta->organization->invites->create(
      email: 'user@example.com',
      role: Role::DEVELOPER,
  );

  echo "id: {$invite->id}\n";
  echo "email: {$invite->email}\n";
  echo "status: {$invite->status}\n";
  echo "expires_at: {$invite->expiresAt->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invite = client.beta.organization.invites.create(email: "user@example.com", role: :developer)

  puts "id: #{invite.id}"
  puts "email: #{invite.email}"
  puts "status: #{invite.status}"
  puts "expires_at: #{invite.expires_at.iso8601}"
  ```
</CodeGroup>

List pending invites:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/invites?limit=10" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:invites list --limit 10
  ```

  ```python Python
  client = anthropic.Anthropic()

  invites = client.beta.organization.invites.list(limit=10)

  # Automatically fetches more pages as needed.
  for invite in invites:
      print(f"{invite.id}: {invite.email} ({invite.status})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const invites = await client.beta.organization.invites.list({ limit: 10 });

  for await (const invite of invites) {
    console.log(`${invite.id}: ${invite.email} (${invite.status})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Invites.List(new() { Limit = 10 });

  await foreach (var invite in page.Paginate())
  {
      Console.WriteLine($"{invite.ID}: {invite.Email} ({invite.Status.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  invites := client.Beta.Organization.Invites.ListAutoPaging(context.Background(), anthropic.BetaOrganizationInviteListParams{
  	Limit: anthropic.Int(10),
  })

  for invites.Next() {
  	invite := invites.Current()
  	fmt.Printf("%s: %s (%s)\n", invite.ID, invite.Email, invite.Status)
  }
  if err := invites.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.invites.InviteListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InviteListParams.builder()
          .limit(10)
          .build();
      var invites = client.beta().organization().invites().list(params);

      for (var invite : invites.autoPager()) {
          IO.println(invite.id() + ": " + invite.email() + " (" + invite.status().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $invites = $client->beta->organization->invites->list(limit: 10);

  foreach ($invites->getItems() as $invite) {
      echo "{$invite->id}: {$invite->email} ({$invite->status})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invites = client.beta.organization.invites.list(limit: 10)

  invites.data.each do |invite|
    puts "#{invite.id}: #{invite.email} (#{invite.status})"
  end
  ```
</CodeGroup>

Delete an invite:

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/invites/invite_015gWxHNr6h6TdRPZTmuCGnn" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:invites delete --invite-id invite_015gWxHNr6h6TdRPZTmuCGnn
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_invite = client.beta.organization.invites.delete(
      "invite_015gWxHNr6h6TdRPZTmuCGnn"
  )

  print(f"id: {deleted_invite.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedInvite = await client.beta.organization.invites.delete(
    "invite_015gWxHNr6h6TdRPZTmuCGnn"
  );

  console.log(`id: ${deletedInvite.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedInvite = await client.Beta.Organization.Invites.Delete(
      "invite_015gWxHNr6h6TdRPZTmuCGnn"
  );

  Console.WriteLine($"id: {deletedInvite.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedInvite, err := client.Beta.Organization.Invites.Delete(context.Background(), "invite_015gWxHNr6h6TdRPZTmuCGnn")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deletedInvite.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedInvite = client.beta().organization().invites()
      .delete("invite_015gWxHNr6h6TdRPZTmuCGnn");

  IO.println("id: " + deletedInvite.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedInvite = $client->beta->organization->invites->delete(
      inviteID: 'invite_015gWxHNr6h6TdRPZTmuCGnn',
  );

  echo "id: {$deletedInvite->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invite_id = "invite_015gWxHNr6h6TdRPZTmuCGnn"
  deleted_invite = client.beta.organization.invites.delete(invite_id)

  puts "id: #{deleted_invite.id}"
  ```
</CodeGroup>

### Workspaces

See [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces) for Console and API examples.

### Workspace members

Manage [user access to specific workspaces](https://platform.claude.com/docs/en/api/admin-api/workspace_members/get-workspace-member):

Add a member to a workspace:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "user_id": "user_01XyDMpzjS89pFZXqSFUBDr6",
      "workspace_role": "workspace_developer"
    }'
  ```

  ```bash CLI
  ant beta:organization:workspaces:members add \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --user-id user_01XyDMpzjS89pFZXqSFUBDr6 \
    --workspace-role workspace_developer
  ```

  ```python Python
  client = anthropic.Anthropic()

  member = client.beta.organization.workspaces.members.add(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      user_id="user_01XyDMpzjS89pFZXqSFUBDr6",
      workspace_role="workspace_developer",
  )

  print(f"user_id: {member.user_id}")
  print(f"workspace_role: {member.workspace_role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const member = await client.beta.organization.workspaces.members.add(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    {
      user_id: "user_01XyDMpzjS89pFZXqSFUBDr6",
      workspace_role: "workspace_developer"
    }
  );

  console.log(`user_id: ${member.user_id}`);
  console.log(`workspace_role: ${member.workspace_role}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Workspaces;

  AnthropicClient client = new();

  var member = await client.Beta.Organization.Workspaces.Members.Add(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      new()
      {
          UserID = "user_01XyDMpzjS89pFZXqSFUBDr6",
          WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceDeveloper
      }
  );

  Console.WriteLine($"user_id: {member.UserID}");
  Console.WriteLine($"workspace_role: {member.WorkspaceRole.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  member, err := client.Beta.Organization.Workspaces.Members.Add(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.BetaOrganizationWorkspaceMemberAddParams{
  		UserID:        "user_01XyDMpzjS89pFZXqSFUBDr6",
  		WorkspaceRole: anthropic.BetaNoBillingWorkspaceRoleWorkspaceDeveloper,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("user_id: %s\n", member.UserID)
  fmt.Printf("workspace_role: %s\n", member.WorkspaceRole)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.BetaNoBillingWorkspaceRole;
  import com.anthropic.models.beta.organization.workspaces.members.MemberAddParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberAddParams.builder()
          .userId("user_01XyDMpzjS89pFZXqSFUBDr6")
          .workspaceRole(BetaNoBillingWorkspaceRole.WORKSPACE_DEVELOPER)
          .build();
      var member = client.beta().organization().workspaces().members()
          .add("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", params);

      IO.println("user_id: " + member.userId());
      IO.println("workspace_role: " + member.workspaceRole().asString());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Workspaces\NoBillingWorkspaceRole;
  // ...

  $client = new Client();

  $member = $client->beta->organization->workspaces->members->add(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      userID: 'user_01XyDMpzjS89pFZXqSFUBDr6',
      workspaceRole: NoBillingWorkspaceRole::WORKSPACE_DEVELOPER,
  );

  echo "user_id: {$member->userID}\n";
  echo "workspace_role: {$member->workspaceRole}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  member = client.beta.organization.workspaces.members.add(
    workspace_id,
    user_id: "user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_role: :workspace_developer
  )

  puts "user_id: #{member.user_id}"
  puts "workspace_role: #{member.workspace_role}"
  ```
</CodeGroup>

List the members of a workspace:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members?limit=10" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:workspaces:members list \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --limit 10
  ```

  ```python Python
  client = anthropic.Anthropic()

  members = client.beta.organization.workspaces.members.list(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", limit=10
  )

  # Automatically fetches more pages as needed.
  for member in members:
      print(f"{member.user_id}: {member.workspace_role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const members = await client.beta.organization.workspaces.members.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    { limit: 10 }
  );

  for await (const member of members) {
    console.log(`${member.user_id}: ${member.workspace_role}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Workspaces.Members.List(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      new() { Limit = 10 }
  );

  await foreach (var member in page.Paginate())
  {
      Console.WriteLine($"{member.UserID}: {member.WorkspaceRole.Raw()}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  members := client.Beta.Organization.Workspaces.Members.ListAutoPaging(
  	context.Background(),
  	"wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	anthropic.BetaOrganizationWorkspaceMemberListParams{
  		Limit: anthropic.Int(10),
  	},
  )

  for members.Next() {
  	member := members.Current()
  	fmt.Printf("%s: %s\n", member.UserID, member.WorkspaceRole)
  }
  if err := members.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.members.MemberListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberListParams.builder()
          .limit(10)
          .build();
      var members = client.beta().organization().workspaces().members()
          .list("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", params);

      for (var member : members.autoPager()) {
          IO.println(member.userId() + ": " + member.workspaceRole().asString());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $members = $client->beta->organization->workspaces->members->list(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      limit: 10,
  );

  foreach ($members->getItems() as $member) {
      echo "{$member->userID}: {$member->workspaceRole}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  members = client.beta.organization.workspaces.members.list(workspace_id, limit: 10)

  members.data.each do |member|
    puts "#{member.user_id}: #{member.workspace_role}"
  end
  ```
</CodeGroup>

Update a workspace member's role:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members/user_01XyDMpzjS89pFZXqSFUBDr6" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{"workspace_role": "workspace_admin"}'
  ```

  ```bash CLI
  ant beta:organization:workspaces:members update \
    --user-id user_01XyDMpzjS89pFZXqSFUBDr6 \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ \
    --workspace-role workspace_admin
  ```

  ```python Python
  client = anthropic.Anthropic()

  member = client.beta.organization.workspaces.members.update(
      "user_01XyDMpzjS89pFZXqSFUBDr6",
      workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      workspace_role="workspace_admin",
  )

  print(f"user_id: {member.user_id}")
  print(f"workspace_role: {member.workspace_role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const member = await client.beta.organization.workspaces.members.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    {
      workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      workspace_role: "workspace_admin"
    }
  );

  console.log(`user_id: ${member.user_id}`);
  console.log(`workspace_role: ${member.workspace_role}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Workspaces;

  AnthropicClient client = new();

  var member = await client.Beta.Organization.Workspaces.Members.Update(
      "user_01XyDMpzjS89pFZXqSFUBDr6",
      new()
      {
          WorkspaceID = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
          WorkspaceRole = BetaWorkspaceRole.WorkspaceAdmin
      }
  );

  Console.WriteLine($"user_id: {member.UserID}");
  Console.WriteLine($"workspace_role: {member.WorkspaceRole.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  member, err := client.Beta.Organization.Workspaces.Members.Update(
  	context.Background(),
  	"user_01XyDMpzjS89pFZXqSFUBDr6",
  	anthropic.BetaOrganizationWorkspaceMemberUpdateParams{
  		WorkspaceID:   "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  		WorkspaceRole: anthropic.BetaWorkspaceRoleWorkspaceAdmin,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("user_id: %s\n", member.UserID)
  fmt.Printf("workspace_role: %s\n", member.WorkspaceRole)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.BetaWorkspaceRole;
  import com.anthropic.models.beta.organization.workspaces.members.MemberUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberUpdateParams.builder()
          .workspaceId("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
          .workspaceRole(BetaWorkspaceRole.WORKSPACE_ADMIN)
          .build();
      var member = client.beta().organization().workspaces().members()
          .update("user_01XyDMpzjS89pFZXqSFUBDr6", params);

      IO.println("user_id: " + member.userId());
      IO.println("workspace_role: " + member.workspaceRole().asString());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Workspaces\WorkspaceRole;
  // ...

  $client = new Client();

  $member = $client->beta->organization->workspaces->members->update(
      userID: 'user_01XyDMpzjS89pFZXqSFUBDr6',
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
      workspaceRole: WorkspaceRole::WORKSPACE_ADMIN,
  );

  echo "user_id: {$member->userID}\n";
  echo "workspace_role: {$member->workspaceRole}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01XyDMpzjS89pFZXqSFUBDr6"
  member = client.beta.organization.workspaces.members.update(
    user_id,
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    workspace_role: :workspace_admin
  )

  puts "user_id: #{member.user_id}"
  puts "workspace_role: #{member.workspace_role}"
  ```
</CodeGroup>

Remove a member from a workspace:

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members/user_01XyDMpzjS89pFZXqSFUBDr6" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:workspaces:members remove \
    --user-id user_01XyDMpzjS89pFZXqSFUBDr6 \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  ```

  ```python Python
  client = anthropic.Anthropic()

  removed_member = client.beta.organization.workspaces.members.remove(
      "user_01XyDMpzjS89pFZXqSFUBDr6", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  print(f"user_id: {removed_member.user_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const removedMember = await client.beta.organization.workspaces.members.remove(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    { workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" }
  );

  console.log(`user_id: ${removedMember.user_id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var removedMember = await client.Beta.Organization.Workspaces.Members.Remove(
      "user_01XyDMpzjS89pFZXqSFUBDr6",
      new() { WorkspaceID = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" }
  );

  Console.WriteLine($"user_id: {removedMember.UserID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  removedMember, err := client.Beta.Organization.Workspaces.Members.Remove(
  	context.Background(),
  	"user_01XyDMpzjS89pFZXqSFUBDr6",
  	anthropic.BetaOrganizationWorkspaceMemberRemoveParams{
  		WorkspaceID: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("user_id: %s\n", removedMember.UserID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.members.MemberRemoveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberRemoveParams.builder()
          .workspaceId("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
          .build();
      var removedMember = client.beta().organization().workspaces().members()
          .remove("user_01XyDMpzjS89pFZXqSFUBDr6", params);

      IO.println("user_id: " + removedMember.userId());
  }
  ```

  ```php PHP
  $client = new Client();

  $removedMember = $client->beta->organization->workspaces->members->remove(
      userID: 'user_01XyDMpzjS89pFZXqSFUBDr6',
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
  );

  echo "user_id: {$removedMember->userID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01XyDMpzjS89pFZXqSFUBDr6"
  removed_member = client.beta.organization.workspaces.members.remove(
    user_id,
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  puts "user_id: #{removed_member.user_id}"
  ```
</CodeGroup>

### API keys

Monitor and manage [API keys](https://platform.claude.com/docs/en/api/admin/api_keys/list). Each key in the response includes its `expires_at` timestamp (`null` for keys without an [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration)):

List the active API keys in a workspace:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/api_keys?limit=10&status=active&workspace_id=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:api-keys list \
    --limit 10 \
    --status active \
    --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  ```

  ```python Python
  client = anthropic.Anthropic()

  api_keys = client.beta.organization.api_keys.list(
      limit=10, status="active", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  # Automatically fetches more pages as needed.
  for api_key in api_keys:
      print(f"{api_key.id}: {api_key.name} ({api_key.status})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const apiKeys = await client.beta.organization.apiKeys.list({
    limit: 10,
    status: "active",
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  });

  for await (const apiKey of apiKeys) {
    console.log(`${apiKey.id}: ${apiKey.name} (${apiKey.status})`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ApiKeys;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.ApiKeys.List(new()
  {
      Limit = 10,
      Status = ApiKeyListParamsStatus.Active,
      WorkspaceID = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  });

  await foreach (var apiKey in page.Paginate())
  {
      Console.WriteLine($"{apiKey.ID}: {apiKey.Name} ({apiKey.Status.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  apiKeys := client.Beta.Organization.APIKeys.ListAutoPaging(context.Background(), anthropic.BetaOrganizationAPIKeyListParams{
  	Limit:       anthropic.Int(10),
  	Status:      anthropic.BetaOrganizationAPIKeyListParamsStatusActive,
  	WorkspaceID: anthropic.String("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"),
  })

  for apiKeys.Next() {
  	apiKey := apiKeys.Current()
  	fmt.Printf("%s: %s (%s)\n", apiKey.ID, apiKey.Name, apiKey.Status)
  }
  if err := apiKeys.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.apikeys.ApiKeyListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = ApiKeyListParams.builder()
          .limit(10)
          .status(ApiKeyListParams.Status.ACTIVE)
          .workspaceId("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
          .build();
      var apiKeys = client.beta().organization().apiKeys().list(params);

      for (var apiKey : apiKeys.autoPager()) {
          IO.println(apiKey.id() + ": " + apiKey.name() + " (" + apiKey.status().asString() + ")");
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\APIKeys\APIKeyListParams\Status;
  // ...

  $client = new Client();

  $apiKeys = $client->beta->organization->apiKeys->list(
      limit: 10,
      status: Status::ACTIVE,
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
  );

  foreach ($apiKeys->getItems() as $apiKey) {
      echo "{$apiKey->id}: {$apiKey->name} ({$apiKey->status})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  api_keys = client.beta.organization.api_keys.list(
    limit: 10,
    status: :active,
    workspace_id: "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  api_keys.data.each do |api_key|
    puts "#{api_key.id}: #{api_key.name} (#{api_key.status})"
  end
  ```
</CodeGroup>

Rename or deactivate an API key:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/api_keys/apikey_01Rj2N8SVvo6BePZj99NhmiT" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "status": "inactive",
      "name": "New Key Name"
    }'
  ```

  ```bash CLI
  ant beta:organization:api-keys update \
    --api-key-id apikey_01Rj2N8SVvo6BePZj99NhmiT \
    --status inactive \
    --name "New Key Name"
  ```

  ```python Python
  client = anthropic.Anthropic()

  api_key = client.beta.organization.api_keys.update(
      "apikey_01Rj2N8SVvo6BePZj99NhmiT", status="inactive", name="New Key Name"
  )

  print(f"id: {api_key.id}")
  print(f"name: {api_key.name}")
  print(f"status: {api_key.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const apiKey = await client.beta.organization.apiKeys.update(
    "apikey_01Rj2N8SVvo6BePZj99NhmiT",
    {
      status: "inactive",
      name: "New Key Name"
    }
  );

  console.log(`id: ${apiKey.id}`);
  console.log(`name: ${apiKey.name}`);
  console.log(`status: ${apiKey.status}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ApiKeys;

  AnthropicClient client = new();

  var apiKey = await client.Beta.Organization.ApiKeys.Update(
      "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      new()
      {
          Status = Status.Inactive,
          Name = "New Key Name"
      }
  );

  Console.WriteLine($"id: {apiKey.ID}");
  Console.WriteLine($"name: {apiKey.Name}");
  Console.WriteLine($"status: {apiKey.Status.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  apiKey, err := client.Beta.Organization.APIKeys.Update(
  	context.Background(),
  	"apikey_01Rj2N8SVvo6BePZj99NhmiT",
  	anthropic.BetaOrganizationAPIKeyUpdateParams{
  		Status: anthropic.BetaOrganizationAPIKeyUpdateParamsStatusInactive,
  		Name:   anthropic.String("New Key Name"),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", apiKey.ID)
  fmt.Printf("name: %s\n", apiKey.Name)
  fmt.Printf("status: %s\n", apiKey.Status)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.apikeys.ApiKeyUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = ApiKeyUpdateParams.builder()
          .status(ApiKeyUpdateParams.Status.INACTIVE)
          .name("New Key Name")
          .build();
      var apiKey = client.beta().organization().apiKeys()
          .update("apikey_01Rj2N8SVvo6BePZj99NhmiT", params);

      IO.println("id: " + apiKey.id());
      IO.println("name: " + apiKey.name());
      IO.println("status: " + apiKey.status().asString());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\APIKeys\APIKeyUpdateParams\Status;
  // ...

  $client = new Client();

  $apiKey = $client->beta->organization->apiKeys->update(
      apiKeyID: 'apikey_01Rj2N8SVvo6BePZj99NhmiT',
      status: Status::INACTIVE,
      name: 'New Key Name',
  );

  echo "id: {$apiKey->id}\n";
  echo "name: {$apiKey->name}\n";
  echo "status: {$apiKey->status}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  api_key_id = "apikey_01Rj2N8SVvo6BePZj99NhmiT"
  api_key = client.beta.organization.api_keys.update(
    api_key_id,
    status: :inactive,
    name: "New Key Name"
  )

  puts "id: #{api_key.id}"
  puts "name: #{api_key.name}"
  puts "status: #{api_key.status}"
  ```
</CodeGroup>

### Service accounts

Create and manage service accounts (`svac_...`), the non-human identities that [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) tokens act as. These endpoints, like the federation-issuer and federation-rule endpoints, require an `org:admin` OAuth token. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#service-accounts).

### Federation issuers

Register the OIDC identity providers (`fdis_...`) whose tokens may assert workload identity for your organization. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#federation-issuers).

### Federation rules

Manage the rules (`fdrl_...`) that map issuer tokens to service accounts and scopes. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api#federation-rules).

## Accessing organization info

The `/v1/organizations/me` endpoint returns the organization that your credential belongs to:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/me" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization retrieve
  ```

  ```python Python
  client = anthropic.Anthropic()

  organization = client.beta.organization.retrieve()

  print(f"id: {organization.id}")
  print(f"name: {organization.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const organization = await client.beta.organization.retrieve();

  console.log(`id: ${organization.id}`);
  console.log(`name: ${organization.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var organization = await client.Beta.Organization.Retrieve();

  Console.WriteLine($"id: {organization.ID}");
  Console.WriteLine($"name: {organization.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  organization, err := client.Beta.Organization.Get(context.Background())
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", organization.ID)
  fmt.Printf("name: %s\n", organization.Name)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var organization = client.beta().organization().retrieve();

  IO.println("id: " + organization.id());
  IO.println("name: " + organization.name());
  ```

  ```php PHP
  $client = new Client();

  $organization = $client->beta->organization->retrieve();

  echo "id: {$organization->id}\n";
  echo "name: {$organization->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  organization = client.beta.organization.retrieve

  puts "id: #{organization.id}"
  puts "name: #{organization.name}"
  ```
</CodeGroup>

```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "type": "organization",
  "name": "Organization Name"
}
```

For parameter details and response schemas, see the [Organization Info API reference](https://platform.claude.com/docs/en/api/admin-api/organization/get-me).

## Usage and cost reports

Track your organization's usage and costs with the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api).

## Claude Code analytics

Monitor developer productivity and Claude Code adoption with the [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api).

## Rate limits

Read the rate limits configured for your organization and its workspaces with the [Rate Limits API](https://platform.claude.com/docs/en/manage-claude/rate-limits-api).

## Compliance API

Retrieve audit and activity data for your organization with the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api). Admin API keys can read only the Activity Feed. For full access, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).

## Best practices

* Use meaningful names and descriptions for workspaces and API keys
* Handle errors from failed operations
* Regularly audit member roles and permissions
* Clean up unused workspaces and expired invites
* Monitor API key usage, audit each key's [`expires_at`](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration), and rotate keys periodically

## FAQ

<AccordionGroup>
  <Accordion title="What permissions are needed to use the Admin API?">
    The Admin API accepts either an Admin API key (starting with `sk-ant-admin`) or an OAuth bearer token with the `org:admin` scope. Only organization members with the admin role can provision Admin API keys, and only members with the admin, owner, or primary owner role can obtain `org:admin` tokens. See [Authentication](https://platform.claude.com/docs/en/manage-claude/admin-api#authentication).
  </Accordion>

  <Accordion title="Can I create new API keys through the Admin API?">
    No. You create API keys in the Claude Console. The Admin API can only read, rename, and change the status of existing keys.
  </Accordion>

  <Accordion title="What happens to API keys when removing a user?">
    They're unaffected. API keys belong to the organization, not to individual users.
  </Accordion>

  <Accordion title="Can organization admins be removed through the API?">
    No. The API can't remove members with the admin role.
  </Accordion>

  <Accordion title="How long do organization invites last?">
    Invites expire after 21 days. The expiration period isn't configurable.
  </Accordion>
</AccordionGroup>

For workspace-specific questions, see the [Workspaces FAQ](https://platform.claude.com/docs/en/manage-claude/workspaces#faq).
