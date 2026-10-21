---
title: User management
url: https://platform.claude.com/docs/en/manage-claude/user-management
description: "Manage the people in your Claude Enterprise organization with the Admin API: list members and change roles, send and withdraw invites, manage groups, and read custom roles."
---

This page covers managing the people in your **Claude Enterprise** (claude.ai) organization programmatically, using the [Admin API](https://platform.claude.com/docs/en/api/beta/organization): list members and look them up by email address, change a member's role, remove members, send and withdraw invites, manage your enterprise's groups and their membership, and read your organization's custom roles. For Claude Console (Claude Platform) organizations, see the [Admin API guide for Claude Console](https://platform.claude.com/docs/en/manage-claude/admin-api).

<Note>
  Group and custom-role requests don't require the `anthropic-beta: ce-user-management-2026-07-13` [beta header](https://platform.claude.com/docs/en/api/beta-headers). Requests that still send it are accepted and behave identically.
</Note>

## Which endpoints can your organization use?

The Admin API is a single set of endpoints under `https://api.anthropic.com/v1/organizations/`. Claude Console and Claude Enterprise organizations authenticate with different [Admin API keys](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) and each have access to a different subset of the endpoints:

| Endpoints                                                                                                                                                                                                                                                                                                                                                     | Claude Console (Claude Platform)                                                                          | Claude Enterprise (claude.ai)                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Members](https://platform.claude.com/docs/en/manage-claude/user-management#members) and [invites](https://platform.claude.com/docs/en/manage-claude/user-management#invites)                                                                                                                                                                                 | Available; see the [Admin API guide](https://platform.claude.com/docs/en/manage-claude/admin-api)         | Available (this page)                                                                                                                                                      |
| [Groups](https://platform.claude.com/docs/en/manage-claude/user-management#groups)                                                                                                                                                                                                                                                                            | Not available                                                                                             | Available (this page)                                                                                                                                                      |
| [Custom roles](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles)                                                                                                                                                                                                                                                                | Not available                                                                                             | Available, read-only (this page)                                                                                                                                           |
| [Plugins](https://platform.claude.com/docs/en/manage-claude/plugins-api)                                                                                                                                                                                                                                                                                      | Not available                                                                                             | Available in beta                                                                                                                                                          |
| [Spend limits](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)                                                                                                                                                                                                                                                                            | Not available                                                                                             | Available                                                                                                                                                                  |
| Usage and cost reports                                                                                                                                                                                                                                                                                                                                        | Available; see the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) | Available through the [Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api#get-access-to-the-claude-enterprise-analytics-api) |
| [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces), [API keys](https://platform.claude.com/docs/en/manage-claude/admin-api#api-keys), [rate limits](https://platform.claude.com/docs/en/manage-claude/rate-limits-api), and the other endpoints in the [Admin API guide](https://platform.claude.com/docs/en/manage-claude/admin-api) | Available                                                                                                 | Not available                                                                                                                                                              |

Members and invites are the same endpoints for both organization types; this page documents their Claude Enterprise behavior, including the Claude Enterprise [organization roles](https://platform.claude.com/docs/en/manage-claude/user-management#organization-roles). The group and custom-role endpoints exist only for Claude Enterprise.

<Check>
  **Scoped Admin API key required**

  These endpoints require an Admin API key with the `read:members` scope (member and invite `GET` endpoints, and all custom-role endpoints; there is no separate role scope), the `write:members` scope (member and invite `POST` and `DELETE` endpoints), the `read:rbac_groups` scope (group `GET` endpoints), or the `write:rbac_groups` scope (group `POST` and `DELETE` endpoints). Assigning the `managed` role, or groups on an invite, requires `write:rbac_groups` in addition to `write:members`. A key carrying the `read:org_audit` scope (a read-only scope for security-audit integrations) can also call every `GET` endpoint on this page and the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) read endpoints. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization) for where your primary owner creates one and which scopes to select. Pass the key in the `x-api-key` header on every request, together with the [`anthropic-version`](https://platform.claude.com/docs/en/api/versioning) header.
</Check>

## Overview

This page covers five resources:

| Resource          | Endpoints                                                                                                                                                                                                                                                    | Use for                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Members**       | `GET /v1/organizations/users`<br />`GET /v1/organizations/users/{user_id}`<br />`POST /v1/organizations/users/{user_id}`<br />`DELETE /v1/organizations/users/{user_id}`                                                                                     | List the organization's members or look one up by email; change a member's role; remove a member.          |
| **Invites**       | `POST /v1/organizations/invites`<br />`GET /v1/organizations/invites`<br />`GET /v1/organizations/invites/{invite_id}`<br />`DELETE /v1/organizations/invites/{invite_id}`                                                                                   | Invite a person to the organization, track the invitation's status, and withdraw it before it is accepted. |
| **Groups**        | `GET /v1/organizations/rbac_groups`<br />`GET /v1/organizations/rbac_groups/{rbac_group_id}`<br />`POST /v1/organizations/rbac_groups`<br />`POST /v1/organizations/rbac_groups/{rbac_group_id}`<br />`DELETE /v1/organizations/rbac_groups/{rbac_group_id}` | Read your enterprise's groups and the custom roles attached to each; create, rename, and delete groups.    |
| **Group members** | `GET /v1/organizations/rbac_groups/{rbac_group_id}/members`<br />`POST /v1/organizations/rbac_groups/{rbac_group_id}/members`<br />`DELETE /v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`                                                  | Read a group's members; add and remove members.                                                            |
| **Custom roles**  | `GET /v1/organizations/rbac_roles`<br />`GET /v1/organizations/rbac_roles/{rbac_role_id}`<br />`GET /v1/organizations/rbac_roles/{rbac_role_id}/permissions`                                                                                                 | Read your organization's custom roles and the permissions each role grants.                                |

Custom roles and their group attachments are managed in [claude.ai organization settings](https://claude.ai/admin-settings); the API reads them but cannot change them.

## Quick start

Set the `ANTHROPIC_API_KEY` environment variable to your Admin API key. The examples on this page read the key from it. The SDK and the `ant` CLI send the `Authorization` and `anthropic-version` headers for you.

List the organization's members, newest first:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/users?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:users list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  users = client.organization.users.list(limit=20)

  for user in users:
      print(f"{user.id}: {user.email} ({user.role})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const users = await client.organization.users.list({ limit: 20 });

  for await (const user of users) {
    console.log(`${user.id}: ${user.email} (${user.role})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Organization.Users.List(new() { Limit = 20 });

  await foreach (var user in page.Paginate())
  {
      Console.WriteLine($"{user.ID}: {user.Email} ({user.Role.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  users := client.Organization.Users.ListAutoPaging(context.Background(), anthropic.OrganizationUserListParams{
  	Limit: anthropic.Int(20),
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
  import com.anthropic.models.organization.users.UserListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserListParams.builder()
          .limit(20)
          .build();
      var users = client.organization().users().list(params);

      for (var user : users.autoPager()) {
          IO.println(user.id() + ": " + user.email() + " (" + user.role().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $users = $client->organization->users->list(limit: 20);

  foreach ($users->pagingEachItem() as $user) {
      echo "{$user->id}: {$user->email} ({$user->role})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  users = client.organization.users.list(limit: 20)

  users.auto_paging_each do |user|
    puts "#{user.id}: #{user.email} (#{user.role})"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "user",
      "id": "user_01AbCdEfGhIjKlMnOpQrSt",
      "email": "jane@example.com",
      "name": "Jane Smith",
      "role": "user",
      "added_at": "2026-06-12T09:14:03Z"
    }
  ],
  "has_more": false,
  "first_id": "user_01AbCdEfGhIjKlMnOpQrSt",
  "last_id": "user_01AbCdEfGhIjKlMnOpQrSt"
}
```

## Key concepts

### Organization roles

Every member has exactly one organization role. Reads return the member's role as one of five values:

| Role               | Meaning                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `user`             | A standard member.                                                                        |
| `managed`          | A member whose permissions are granted through the custom roles attached to their groups. |
| `owner`            | An organization owner.                                                                    |
| `membership_admin` | A member who can manage the organization's members.                                       |
| `primary_owner`    | The organization's primary owner. There is exactly one.                                   |

The API can assign only the `user` and `managed` roles, on invite creation and on role updates. Assigning `managed` requires the `write:rbac_groups` scope in addition to `write:members`, because a managed member's permissions come from the custom roles attached to their groups. The administrative roles (`owner`, `membership_admin`, and `primary_owner`) are assigned in claude.ai organization settings, and members holding them cannot be modified or removed through this API.

### Members and invites

A person becomes a member by accepting an invite (or through your organization's single sign-on, where configured). Creating an invite sends an invitation email; the invite then reads as `pending` until the recipient accepts (`accepted`) or its server-assigned `expires_at` passes (`expired`). Only a `pending` invite can be withdrawn. To change a pending invitation's email address or role, withdraw it and create a new one.

If your organization's plan draws members from a finite pool of purchased seats, a pending invite consumes a seat. The create-invite endpoint does not take a seat or tier parameter: the seat is assigned automatically from the lowest tier that has availability. Creating an invite when no seat is free fails with a 400 error rather than purchasing a seat. Withdrawing the invite, letting it expire, or removing the member later returns the seat to the pool.

### Groups and roles

Groups connect members to custom roles (role-based access control, the `rbac` in the endpoint paths and scope names). Groups are owned by your enterprise as a whole (the parent organization together with every organization under it) rather than by a single organization, so the group scopes (`read:rbac_groups` and `write:rbac_groups`) require a key created for all linked organizations. Each group carries a `source_type`: `direct` for groups created in claude.ai, `scim` for groups provisioned by your identity provider. A group's `role_ids` field lists the IDs of the custom roles attached to it; resolve them to names and permissions with the [custom role endpoints](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles), noting that the role catalog is per-organization whereas groups are enterprise-wide, so fetching a role that belongs to a different organization of your enterprise returns 404 for your key. The field is `null` (rather than `[]`) when role data was temporarily unavailable, so retry to distinguish a degraded read from a group with no roles.

## Versioning

Send the `anthropic-version` header on every request; see [API versions](https://platform.claude.com/docs/en/api/versioning) for the available versions.

## Rate limits

Admin API endpoints share a per-organization limit of **100 requests per minute**; invite creation has its own limit of **1,200 requests per hour** instead. Requests over a limit return **429 Too Many Requests**.

## Pagination

Member and invite lists use ID-based pagination: pass `limit` (default 20, max 1000) plus at most one of `before_id` or `after_id`, and page using the `first_id` and `last_id` fields of each response until `has_more` is `false`. Group and custom-role lists use an **opaque cursor** instead: pass the response's `next_page` value unchanged as the `page` parameter on the next request, until `next_page` is `null`.

When you iterate over the results, the SDK fetches more pages for you, so `limit` sets the page size, not the total. In the CLI, `--limit` sets the total number of results for member and invite lists. For group and role lists, it sets the page size.

## Error responses

Error responses follow the standard shape documented in [Claude API errors](https://platform.claude.com/docs/en/api/errors).

## Members

### List members

`GET /v1/organizations/users` returns the organization's members, most recently added first. Filter by `email` to look up a specific member; the match is case-insensitive and tolerates common variants of the same address (for example, `jane+hiring@example.com` matches `jane@example.com`). Requires the `read:members` scope.

For complete parameter details and response schemas, see [List users](https://platform.claude.com/docs/en/api/organization/users/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/users?email=jane@example.com" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:users list --email jane@example.com
  ```

  ```python Python
  client = anthropic.Anthropic()

  users = client.organization.users.list(email="jane@example.com")

  for user in users:
      print(f"{user.id}: {user.email} ({user.role})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const users = await client.organization.users.list({ email: "jane@example.com" });

  for await (const user of users) {
    console.log(`${user.id}: ${user.email} (${user.role})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Organization.Users.List(new() { Email = "jane@example.com" });

  await foreach (var user in page.Paginate())
  {
      Console.WriteLine($"{user.ID}: {user.Email} ({user.Role.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  users := client.Organization.Users.ListAutoPaging(context.Background(), anthropic.OrganizationUserListParams{
  	Email: anthropic.String("jane@example.com"),
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
  import com.anthropic.models.organization.users.UserListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserListParams.builder()
          .email("jane@example.com")
          .build();
      var users = client.organization().users().list(params);

      for (var user : users.autoPager()) {
          IO.println(user.id() + ": " + user.email() + " (" + user.role().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $users = $client->organization->users->list(email: 'jane@example.com');

  foreach ($users->pagingEachItem() as $user) {
      echo "{$user->id}: {$user->email} ({$user->role})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  users = client.organization.users.list(email: "jane@example.com")

  users.auto_paging_each do |user|
    puts "#{user.id}: #{user.email} (#{user.role})"
  end
  ```
</CodeGroup>

### Get a member

`GET /v1/organizations/users/{user_id}` returns one member by ID. Requires the `read:members` scope.

For complete parameter details and response schemas, see [Get user](https://platform.claude.com/docs/en/api/organization/users/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/users/user_01AbCdEfGhIjKlMnOpQrSt" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:users retrieve --user-id user_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  user = client.organization.users.retrieve("user_01AbCdEfGhIjKlMnOpQrSt")

  print(f"id: {user.id}")
  print(f"email: {user.email}")
  print(f"role: {user.role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const user = await client.organization.users.retrieve("user_01AbCdEfGhIjKlMnOpQrSt");

  console.log(`id: ${user.id}`);
  console.log(`email: ${user.email}`);
  console.log(`role: ${user.role}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var user = await client.Organization.Users.Retrieve("user_01AbCdEfGhIjKlMnOpQrSt");

  Console.WriteLine($"id: {user.ID}");
  Console.WriteLine($"email: {user.Email}");
  Console.WriteLine($"role: {user.Role.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  user, err := client.Organization.Users.Get(context.Background(), "user_01AbCdEfGhIjKlMnOpQrSt")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", user.ID)
  fmt.Printf("email: %s\n", user.Email)
  fmt.Printf("role: %s\n", user.Role)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var user = client.organization().users()
      .retrieve("user_01AbCdEfGhIjKlMnOpQrSt");

  IO.println("id: " + user.id());
  IO.println("email: " + user.email());
  IO.println("role: " + user.role().asString());
  ```

  ```php PHP
  $client = new Client();

  $user = $client->organization->users->retrieve(
      userID: 'user_01AbCdEfGhIjKlMnOpQrSt',
  );

  echo "id: {$user->id}\n";
  echo "email: {$user->email}\n";
  echo "role: {$user->role}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user = client.organization.users.retrieve("user_01AbCdEfGhIjKlMnOpQrSt")

  puts "id: #{user.id}"
  puts "email: #{user.email}"
  puts "role: #{user.role}"
  ```
</CodeGroup>

### Change a member's role

`POST /v1/organizations/users/{user_id}` sets the member's role to `user` or `managed`. Members holding an administrative role (`owner`, `membership_admin`, or `primary_owner`) cannot be changed through this endpoint, and administrative roles cannot be assigned; both return 400 and are managed in claude.ai organization settings. If your organization's identity provider manages roles (advanced SSO or advanced SCIM provisioning), role updates return 400. Requires the `write:members` scope, plus `write:rbac_groups` when changing the role to `managed`.

For complete parameter details and response schemas, see [Update user](https://platform.claude.com/docs/en/api/organization/users/update) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/users/user_01AbCdEfGhIjKlMnOpQrSt" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"role": "managed"}'
  ```

  ```bash CLI
  ant organization:users update \
    --user-id user_01AbCdEfGhIjKlMnOpQrSt \
    --role managed
  ```

  ```python Python
  client = anthropic.Anthropic()

  user = client.organization.users.update("user_01AbCdEfGhIjKlMnOpQrSt", role="managed")

  print(f"id: {user.id}")
  print(f"role: {user.role}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const user = await client.organization.users.update("user_01AbCdEfGhIjKlMnOpQrSt", {
    role: "managed"
  });

  console.log(`id: ${user.id}`);
  console.log(`role: ${user.role}`);
  ```

  ```csharp C#
  using Anthropic.Models.Organization.Users;
  // ...

  AnthropicClient client = new();

  var user = await client.Organization.Users.Update(
      "user_01AbCdEfGhIjKlMnOpQrSt",
      new() { Role = Role.Managed }
  );

  Console.WriteLine($"id: {user.ID}");
  Console.WriteLine($"role: {user.Role.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  user, err := client.Organization.Users.Update(
  	context.Background(),
  	"user_01AbCdEfGhIjKlMnOpQrSt",
  	anthropic.OrganizationUserUpdateParams{
  		Role: anthropic.OrganizationUserUpdateParamsRoleManaged,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", user.ID)
  fmt.Printf("role: %s\n", user.Role)
  ```

  ```java Java
  import com.anthropic.models.organization.users.UserUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = UserUpdateParams.builder()
          .role(UserUpdateParams.Role.MANAGED)
          .build();
      var user = client.organization().users()
          .update("user_01AbCdEfGhIjKlMnOpQrSt", params);

      IO.println("id: " + user.id());
      IO.println("role: " + user.role().asString());
  }
  ```

  ```php PHP
  use Anthropic\Organization\Users\UserUpdateParams\Role;
  // ...

  $client = new Client();

  $user = $client->organization->users->update(
      userID: 'user_01AbCdEfGhIjKlMnOpQrSt',
      role: Role::MANAGED,
  );

  echo "id: {$user->id}\n";
  echo "role: {$user->role}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01AbCdEfGhIjKlMnOpQrSt"
  user = client.organization.users.update(user_id, role: :managed)

  puts "id: #{user.id}"
  puts "role: #{user.role}"
  ```
</CodeGroup>

### Remove a member

`DELETE /v1/organizations/users/{user_id}` removes the member from the organization, returning any purchased seat they occupied to the organization's pool. Members holding an administrative role cannot be removed through this endpoint, and if your identity provider manages membership (SCIM), removals return 400. Requires the `write:members` scope.

For complete parameter details and response schemas, see [Remove user](https://platform.claude.com/docs/en/api/organization/users/remove) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/users/user_01AbCdEfGhIjKlMnOpQrSt" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:users remove --user-id user_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  removed_user = client.organization.users.remove("user_01AbCdEfGhIjKlMnOpQrSt")

  print(f"id: {removed_user.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const removedUser = await client.organization.users.remove("user_01AbCdEfGhIjKlMnOpQrSt");

  console.log(`id: ${removedUser.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var removedUser = await client.Organization.Users.Remove("user_01AbCdEfGhIjKlMnOpQrSt");

  Console.WriteLine($"id: {removedUser.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  removedUser, err := client.Organization.Users.Remove(context.Background(), "user_01AbCdEfGhIjKlMnOpQrSt")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", removedUser.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var removedUser = client.organization().users()
      .remove("user_01AbCdEfGhIjKlMnOpQrSt");

  IO.println("id: " + removedUser.id());
  ```

  ```php PHP
  $client = new Client();

  $removedUser = $client->organization->users->remove(
      userID: 'user_01AbCdEfGhIjKlMnOpQrSt',
  );

  echo "id: {$removedUser->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  user_id = "user_01AbCdEfGhIjKlMnOpQrSt"
  removed_user = client.organization.users.remove(user_id)

  puts "id: #{removed_user.id}"
  ```
</CodeGroup>

```json
{
  "type": "user_deleted",
  "id": "user_01AbCdEfGhIjKlMnOpQrSt"
}
```

## Invites

### Create an invite

`POST /v1/organizations/invites` sends an invitation email and returns the invite with a server-assigned `expires_at`. `role` must be `user` or `managed`. If a pending invite already exists for the email address, or the address already belongs to a member, the request returns 400 naming the existing resource. Organizations whose identity provider provisions users automatically (JIT or SCIM) cannot create invites through the API. Requires the `write:members` scope, plus `write:rbac_groups` when `role` is `managed`.

On plans that draw members from a finite seat pool, the invite automatically takes a seat from the lowest tier that has availability. The API does not take a tier parameter. If no seat is free, the request fails with a 400 error rather than purchasing a seat. Add seats through the organization's plan management and retry.

The optional `rbac_group_ids` field lists groups (by `rbac_group_`-prefixed ID) to assign to the member when they accept. Passing a non-empty `rbac_group_ids` additionally requires the key to carry the `write:rbac_groups` scope, because group assignment can grant the permissions attached to the group's roles.

For complete parameter details and response schemas, see [Create invite](https://platform.claude.com/docs/en/api/organization/invites/create) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/invites" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "email": "newhire@example.com",
      "role": "managed",
      "rbac_group_ids": ["rbac_group_01UvWxYzAbCdEfGhIjKlMn"]
    }'
  ```

  ```bash CLI
  ant organization:invites create \
    --email newhire@example.com \
    --role managed \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn
  ```

  ```python Python
  client = anthropic.Anthropic()

  invite = client.organization.invites.create(
      email="newhire@example.com",
      role="managed",
      rbac_group_ids=["rbac_group_01UvWxYzAbCdEfGhIjKlMn"],
  )

  print(f"id: {invite.id}")
  print(f"email: {invite.email}")
  print(f"status: {invite.status}")
  print(f"expires_at: {invite.expires_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const invite = await client.organization.invites.create({
    email: "newhire@example.com",
    role: "managed",
    rbac_group_ids: ["rbac_group_01UvWxYzAbCdEfGhIjKlMn"]
  });

  console.log(`id: ${invite.id}`);
  console.log(`email: ${invite.email}`);
  console.log(`status: ${invite.status}`);
  console.log(`expires_at: ${invite.expires_at}`);
  ```

  ```csharp C#
  using Anthropic.Models.Organization.Invites;
  // ...

  AnthropicClient client = new();

  var invite = await client.Organization.Invites.Create(new()
  {
      Email = "newhire@example.com",
      Role = Role.Managed,
      RbacGroupIds = ["rbac_group_01UvWxYzAbCdEfGhIjKlMn"]
  });

  Console.WriteLine($"id: {invite.ID}");
  Console.WriteLine($"email: {invite.Email}");
  Console.WriteLine($"status: {invite.Status.Raw()}");
  Console.WriteLine($"expires_at: {invite.ExpiresAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  invite, err := client.Organization.Invites.New(context.Background(), anthropic.OrganizationInviteNewParams{
  	Email:        "newhire@example.com",
  	Role:         anthropic.OrganizationInviteNewParamsRoleManaged,
  	RBACGroupIDs: []string{"rbac_group_01UvWxYzAbCdEfGhIjKlMn"},
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
  import com.anthropic.models.organization.invites.InviteCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InviteCreateParams.builder()
          .email("newhire@example.com")
          .role(InviteCreateParams.Role.MANAGED)
          .addRbacGroupId("rbac_group_01UvWxYzAbCdEfGhIjKlMn")
          .build();
      var invite = client.organization().invites().create(params);

      IO.println("id: " + invite.id());
      IO.println("email: " + invite.email());
      IO.println("status: " + invite.status().asString());
      IO.println("expires_at: " + invite.expiresAt());
  }
  ```

  ```php PHP
  use Anthropic\Organization\Invites\InviteCreateParams\Role;
  // ...

  $client = new Client();

  $invite = $client->organization->invites->create(
      email: 'newhire@example.com',
      role: Role::MANAGED,
      rbacGroupIDs: ['rbac_group_01UvWxYzAbCdEfGhIjKlMn'],
  );

  echo "id: {$invite->id}\n";
  echo "email: {$invite->email}\n";
  echo "status: {$invite->status}\n";
  echo "expires_at: {$invite->expiresAt->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invite = client.organization.invites.create(
    email: "newhire@example.com",
    role: :managed,
    rbac_group_ids: ["rbac_group_01UvWxYzAbCdEfGhIjKlMn"]
  )

  puts "id: #{invite.id}"
  puts "email: #{invite.email}"
  puts "status: #{invite.status}"
  puts "expires_at: #{invite.expires_at.iso8601}"
  ```
</CodeGroup>

```json
{
  "type": "invite",
  "id": "invite_01QrStUvWxYzAbCdEfGhIj",
  "email": "newhire@example.com",
  "role": "managed",
  "invited_at": "2026-07-06T16:20:11Z",
  "expires_at": "2026-07-27T16:20:11Z",
  "accepted_at": null,
  "status": "pending",
  "rbac_group_ids": ["rbac_group_01UvWxYzAbCdEfGhIjKlMn"]
}
```

### List invites

`GET /v1/organizations/invites` returns the organization's invites, most recent first, across the `pending`, `accepted`, and `expired` states; there is no status filter. Requires the `read:members` scope.

For complete parameter details and response schemas, see [List invites](https://platform.claude.com/docs/en/api/organization/invites/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/invites?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:invites list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  invites = client.organization.invites.list(limit=20)

  for invite in invites:
      print(f"{invite.id}: {invite.email} ({invite.status})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const invites = await client.organization.invites.list({ limit: 20 });

  for await (const invite of invites) {
    console.log(`${invite.id}: ${invite.email} (${invite.status})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Organization.Invites.List(new() { Limit = 20 });

  await foreach (var invite in page.Paginate())
  {
      Console.WriteLine($"{invite.ID}: {invite.Email} ({invite.Status.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  invites := client.Organization.Invites.ListAutoPaging(context.Background(), anthropic.OrganizationInviteListParams{
  	Limit: anthropic.Int(20),
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
  import com.anthropic.models.organization.invites.InviteListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InviteListParams.builder()
          .limit(20)
          .build();
      var invites = client.organization().invites().list(params);

      for (var invite : invites.autoPager()) {
          IO.println(invite.id() + ": " + invite.email() + " (" + invite.status().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $invites = $client->organization->invites->list(limit: 20);

  foreach ($invites->pagingEachItem() as $invite) {
      echo "{$invite->id}: {$invite->email} ({$invite->status})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invites = client.organization.invites.list(limit: 20)

  invites.auto_paging_each do |invite|
    puts "#{invite.id}: #{invite.email} (#{invite.status})"
  end
  ```
</CodeGroup>

### Get an invite

`GET /v1/organizations/invites/{invite_id}` returns one invite by ID. Requires the `read:members` scope.

For complete parameter details and response schemas, see [Get invite](https://platform.claude.com/docs/en/api/organization/invites/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/invites/invite_01QrStUvWxYzAbCdEfGhIj" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:invites retrieve --invite-id invite_01QrStUvWxYzAbCdEfGhIj
  ```

  ```python Python
  client = anthropic.Anthropic()

  invite = client.organization.invites.retrieve("invite_01QrStUvWxYzAbCdEfGhIj")

  print(f"id: {invite.id}")
  print(f"email: {invite.email}")
  print(f"status: {invite.status}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const invite = await client.organization.invites.retrieve("invite_01QrStUvWxYzAbCdEfGhIj");

  console.log(`id: ${invite.id}`);
  console.log(`email: ${invite.email}`);
  console.log(`status: ${invite.status}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var invite = await client.Organization.Invites.Retrieve("invite_01QrStUvWxYzAbCdEfGhIj");

  Console.WriteLine($"id: {invite.ID}");
  Console.WriteLine($"email: {invite.Email}");
  Console.WriteLine($"status: {invite.Status.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  invite, err := client.Organization.Invites.Get(context.Background(), "invite_01QrStUvWxYzAbCdEfGhIj")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", invite.ID)
  fmt.Printf("email: %s\n", invite.Email)
  fmt.Printf("status: %s\n", invite.Status)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var invite = client.organization().invites()
      .retrieve("invite_01QrStUvWxYzAbCdEfGhIj");

  IO.println("id: " + invite.id());
  IO.println("email: " + invite.email());
  IO.println("status: " + invite.status().asString());
  ```

  ```php PHP
  $client = new Client();

  $invite = $client->organization->invites->retrieve(
      inviteID: 'invite_01QrStUvWxYzAbCdEfGhIj',
  );

  echo "id: {$invite->id}\n";
  echo "email: {$invite->email}\n";
  echo "status: {$invite->status}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invite = client.organization.invites.retrieve("invite_01QrStUvWxYzAbCdEfGhIj")

  puts "id: #{invite.id}"
  puts "email: #{invite.email}"
  puts "status: #{invite.status}"
  ```
</CodeGroup>

### Withdraw an invite

`DELETE /v1/organizations/invites/{invite_id}` withdraws a `pending` invite, deactivating the link in the invitation email. Withdrawing an `accepted` invite returns 400 (remove the member instead); withdrawing an `expired` invite returns 400. Requires the `write:members` scope.

For complete parameter details and response schemas, see [Delete invite](https://platform.claude.com/docs/en/api/organization/invites/delete) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/invites/invite_01QrStUvWxYzAbCdEfGhIj" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant organization:invites delete --invite-id invite_01QrStUvWxYzAbCdEfGhIj
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_invite = client.organization.invites.delete("invite_01QrStUvWxYzAbCdEfGhIj")

  print(f"id: {deleted_invite.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedInvite = await client.organization.invites.delete(
    "invite_01QrStUvWxYzAbCdEfGhIj"
  );

  console.log(`id: ${deletedInvite.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedInvite = await client.Organization.Invites.Delete("invite_01QrStUvWxYzAbCdEfGhIj");

  Console.WriteLine($"id: {deletedInvite.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedInvite, err := client.Organization.Invites.Delete(context.Background(), "invite_01QrStUvWxYzAbCdEfGhIj")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deletedInvite.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedInvite = client.organization().invites()
      .delete("invite_01QrStUvWxYzAbCdEfGhIj");

  IO.println("id: " + deletedInvite.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedInvite = $client->organization->invites->delete(
      inviteID: 'invite_01QrStUvWxYzAbCdEfGhIj',
  );

  echo "id: {$deletedInvite->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  invite_id = "invite_01QrStUvWxYzAbCdEfGhIj"
  deleted_invite = client.organization.invites.delete(invite_id)

  puts "id: #{deleted_invite.id}"
  ```
</CodeGroup>

## Groups

Groups your enterprise creates directly, in [claude.ai organization settings](https://claude.ai/admin-settings) or through this API (`source_type: "direct"`), support every endpoint in this section. Groups provisioned by your identity provider (`source_type: "scim"`) can be read but not modified: renaming or deleting a SCIM group, or changing its membership, returns 400, because your identity provider owns it.

### List groups

`GET /v1/organizations/rbac_groups` returns your enterprise's groups, including identity-provider-managed (`scim`) groups. Requires the `read:rbac_groups` scope.

For complete parameter details and response schemas, see [List groups](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_groups?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-groups list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  groups = client.beta.organization.rbac_groups.list(limit=20)

  for group in groups:
      print(f"{group.id}: {group.name} ({group.source_type})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const groups = await client.beta.organization.rbacGroups.list({ limit: 20 });

  for await (const group of groups) {
    console.log(`${group.id}: ${group.name} (${group.source_type})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.RbacGroups.List(new() { Limit = 20 });

  await foreach (var group in page.Paginate())
  {
      Console.WriteLine($"{group.ID}: {group.Name} ({group.SourceType.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  groups := client.Beta.Organization.RBACGroups.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRBACGroupListParams{
  	Limit: anthropic.Int(20),
  })

  for groups.Next() {
  	group := groups.Current()
  	fmt.Printf("%s: %s (%s)\n", group.ID, group.Name, group.SourceType)
  }
  if err := groups.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.RbacGroupListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RbacGroupListParams.builder()
          .limit(20)
          .build();
      var groups = client.beta().organization().rbacGroups().list(params);

      for (var group : groups.autoPager()) {
          IO.println(group.id() + ": " + group.name() + " (" + group.sourceType().asString() + ")");
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $groups = $client->beta->organization->rbacGroups->list(limit: 20);

  foreach ($groups->pagingEachItem() as $group) {
      echo "{$group->id}: {$group->name} ({$group->sourceType})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  groups = client.beta.organization.rbac_groups.list(limit: 20)

  groups.auto_paging_each do |group|
    puts "#{group.id}: #{group.name} (#{group.source_type})"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "rbac_group",
      "id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      "name": "Engineering",
      "source_type": "direct",
      "role_ids": ["rbac_role_01CdEfGhIjKlMnOpQrStUv"],
      "roles": ["rbac_role_01CdEfGhIjKlMnOpQrStUv"],
      "created_at": "2026-03-18T10:01:42Z",
      "updated_at": "2026-05-02T08:55:09Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

### Get a group

`GET /v1/organizations/rbac_groups/{rbac_group_id}` returns one group by ID. Requires the `read:rbac_groups` scope.

For complete parameter details and response schemas, see [Get group](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-groups retrieve \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn
  ```

  ```python Python
  client = anthropic.Anthropic()

  group = client.beta.organization.rbac_groups.retrieve(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  )

  print(f"id: {group.id}")
  print(f"name: {group.name}")
  print(f"source_type: {group.source_type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const group = await client.beta.organization.rbacGroups.retrieve(
    "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  );

  console.log(`id: ${group.id}`);
  console.log(`name: ${group.name}`);
  console.log(`source_type: ${group.source_type}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var group = await client.Beta.Organization.RbacGroups.Retrieve("rbac_group_01UvWxYzAbCdEfGhIjKlMn");

  Console.WriteLine($"id: {group.ID}");
  Console.WriteLine($"name: {group.Name}");
  Console.WriteLine($"source_type: {group.SourceType.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  group, err := client.Beta.Organization.RBACGroups.Get(context.Background(), "rbac_group_01UvWxYzAbCdEfGhIjKlMn")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", group.ID)
  fmt.Printf("name: %s\n", group.Name)
  fmt.Printf("source_type: %s\n", group.SourceType)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var group = client.beta().organization().rbacGroups()
      .retrieve("rbac_group_01UvWxYzAbCdEfGhIjKlMn");

  IO.println("id: " + group.id());
  IO.println("name: " + group.name());
  IO.println("source_type: " + group.sourceType().asString());
  ```

  ```php PHP
  $client = new Client();

  $group = $client->beta->organization->rbacGroups->retrieve(
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
  );

  echo "id: {$group->id}\n";
  echo "name: {$group->name}\n";
  echo "source_type: {$group->sourceType}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  group = client.beta.organization.rbac_groups.retrieve(rbac_group_id)

  puts "id: #{group.id}"
  puts "name: #{group.name}"
  puts "source_type: #{group.source_type}"
  ```
</CodeGroup>

### Create a group

`POST /v1/organizations/rbac_groups` creates a group with the given `name` (1–255 characters) and no roles or members. Requires the `write:rbac_groups` scope.

For complete parameter details and response schemas, see [Create group](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/create) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/rbac_groups" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"name": "Engineering"}'
  ```

  ```bash CLI
  ant beta:organization:rbac-groups create --name Engineering
  ```

  ```python Python
  client = anthropic.Anthropic()

  group = client.beta.organization.rbac_groups.create(name="Engineering")

  print(f"id: {group.id}")
  print(f"name: {group.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const group = await client.beta.organization.rbacGroups.create({ name: "Engineering" });

  console.log(`id: ${group.id}`);
  console.log(`name: ${group.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var group = await client.Beta.Organization.RbacGroups.Create(new()
  {
      Name = "Engineering"
  });

  Console.WriteLine($"id: {group.ID}");
  Console.WriteLine($"name: {group.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  group, err := client.Beta.Organization.RBACGroups.New(context.Background(), anthropic.BetaOrganizationRBACGroupNewParams{
  	Name: "Engineering",
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", group.ID)
  fmt.Printf("name: %s\n", group.Name)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.RbacGroupCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RbacGroupCreateParams.builder()
          .name("Engineering")
          .build();
      var group = client.beta().organization().rbacGroups().create(params);

      IO.println("id: " + group.id());
      IO.println("name: " + group.name());
  }
  ```

  ```php PHP
  $client = new Client();

  $group = $client->beta->organization->rbacGroups->create(
      name: 'Engineering',
  );

  echo "id: {$group->id}\n";
  echo "name: {$group->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  group = client.beta.organization.rbac_groups.create(name: "Engineering")

  puts "id: #{group.id}"
  puts "name: #{group.name}"
  ```
</CodeGroup>

```json
{
  "type": "rbac_group",
  "id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "name": "Engineering",
  "source_type": "direct",
  "role_ids": [],
  "roles": [],
  "created_at": "2026-07-09T18:00:00Z",
  "updated_at": "2026-07-09T18:00:00Z"
}
```

### Rename a group

`POST /v1/organizations/rbac_groups/{rbac_group_id}` updates the group. `name` is the only field this endpoint can change. Requires the `write:rbac_groups` scope.

For complete parameter details and response schemas, see [Update group](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/update) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"name": "Platform Engineering"}'
  ```

  ```bash CLI
  ant beta:organization:rbac-groups update \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn \
    --name "Platform Engineering"
  ```

  ```python Python
  client = anthropic.Anthropic()

  group = client.beta.organization.rbac_groups.update(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn", name="Platform Engineering"
  )

  print(f"id: {group.id}")
  print(f"name: {group.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const group = await client.beta.organization.rbacGroups.update(
    "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
    { name: "Platform Engineering" }
  );

  console.log(`id: ${group.id}`);
  console.log(`name: ${group.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var group = await client.Beta.Organization.RbacGroups.Update(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      new() { Name = "Platform Engineering" }
  );

  Console.WriteLine($"id: {group.ID}");
  Console.WriteLine($"name: {group.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  group, err := client.Beta.Organization.RBACGroups.Update(
  	context.Background(),
  	"rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  	anthropic.BetaOrganizationRBACGroupUpdateParams{
  		Name: anthropic.String("Platform Engineering"),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", group.ID)
  fmt.Printf("name: %s\n", group.Name)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.RbacGroupUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RbacGroupUpdateParams.builder()
          .name("Platform Engineering")
          .build();
      var group = client.beta().organization().rbacGroups()
          .update("rbac_group_01UvWxYzAbCdEfGhIjKlMn", params);

      IO.println("id: " + group.id());
      IO.println("name: " + group.name());
  }
  ```

  ```php PHP
  $client = new Client();

  $group = $client->beta->organization->rbacGroups->update(
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
      name: 'Platform Engineering',
  );

  echo "id: {$group->id}\n";
  echo "name: {$group->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  group = client.beta.organization.rbac_groups.update(rbac_group_id, name: "Platform Engineering")

  puts "id: #{group.id}"
  puts "name: #{group.name}"
  ```
</CodeGroup>

### Delete a group

`DELETE /v1/organizations/rbac_groups/{rbac_group_id}` deletes the group. Its members remain members of their organizations, but they lose the permissions of its attached roles, and a group [spend limit](https://platform.claude.com/docs/en/manage-claude/spend-limits-api), if one existed, stops applying to them. Requires the `write:rbac_groups` scope.

For complete parameter details and response schemas, see [Delete group](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/delete) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-groups delete \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_group = client.beta.organization.rbac_groups.delete(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  )

  print(f"id: {deleted_group.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedGroup = await client.beta.organization.rbacGroups.delete(
    "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  );

  console.log(`id: ${deletedGroup.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedGroup = await client.Beta.Organization.RbacGroups.Delete(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  );

  Console.WriteLine($"id: {deletedGroup.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedGroup, err := client.Beta.Organization.RBACGroups.Delete(context.Background(), "rbac_group_01UvWxYzAbCdEfGhIjKlMn")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deletedGroup.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedGroup = client.beta().organization().rbacGroups()
      .delete("rbac_group_01UvWxYzAbCdEfGhIjKlMn");

  IO.println("id: " + deletedGroup.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedGroup = $client->beta->organization->rbacGroups->delete(
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
  );

  echo "id: {$deletedGroup->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  deleted_group = client.beta.organization.rbac_groups.delete(rbac_group_id)

  puts "id: #{deleted_group.id}"
  ```
</CodeGroup>

```json
{
  "id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "type": "rbac_group_deleted"
}
```

### List a group's members

`GET /v1/organizations/rbac_groups/{rbac_group_id}/members` returns the group's members (each with their `user_id` and email), oldest first. Only current members of your enterprise's organizations are returned, so a page might contain fewer than `limit` entries while `has_more` is `true`. Requires the `read:rbac_groups` scope.

For complete parameter details and response schemas, see [List group members](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn/members?limit=100" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-groups:members list \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn \
    --limit 100
  ```

  ```python Python
  client = anthropic.Anthropic()

  members = client.beta.organization.rbac_groups.members.list(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn", limit=100
  )

  for member in members:
      print(f"{member.user_id}: {member.email}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const members = await client.beta.organization.rbacGroups.members.list(
    "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
    { limit: 100 }
  );

  for await (const member of members) {
    console.log(`${member.user_id}: ${member.email}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.RbacGroups.Members.List(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      new() { Limit = 100 }
  );

  await foreach (var member in page.Paginate())
  {
      Console.WriteLine($"{member.UserID}: {member.Email}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  members := client.Beta.Organization.RBACGroups.Members.ListAutoPaging(
  	context.Background(),
  	"rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  	anthropic.BetaOrganizationRBACGroupMemberListParams{
  		Limit: anthropic.Int(100),
  	},
  )

  for members.Next() {
  	member := members.Current()
  	fmt.Printf("%s: %s\n", member.UserID, member.Email)
  }
  if err := members.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.members.MemberListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberListParams.builder()
          .limit(100)
          .build();
      var members = client.beta().organization().rbacGroups().members()
          .list("rbac_group_01UvWxYzAbCdEfGhIjKlMn", params);

      for (var member : members.autoPager()) {
          IO.println(member.userId() + ": " + member.email());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $members = $client->beta->organization->rbacGroups->members->list(
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
      limit: 100,
  );

  foreach ($members->pagingEachItem() as $member) {
      echo "{$member->userID}: {$member->email}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  members = client.beta.organization.rbac_groups.members.list(rbac_group_id, limit: 100)

  members.auto_paging_each do |member|
    puts "#{member.user_id}: #{member.email}"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "rbac_group_member",
      "rbac_group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      "group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
      "email": "jane@example.com",
      "created_at": "2026-04-07T12:30:00Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

### Add a member to a group

`POST /v1/organizations/rbac_groups/{rbac_group_id}/members` adds an organization member to the group by `user_id`. The user must already be a member of one of your enterprise's organizations (the request returns 404 otherwise), and adding someone who is already in the group returns 400. For `scim` groups, membership is managed in your identity provider and this request returns 400. To assign groups to a person who has not joined yet, use `rbac_group_ids` on [invite creation](https://platform.claude.com/docs/en/manage-claude/user-management#create-an-invite) instead. Requires the `write:rbac_groups` scope.

For complete parameter details and response schemas, see [Add group member](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/add) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn/members" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"user_id": "user_01AbCdEfGhIjKlMnOpQrSt"}'
  ```

  ```bash CLI
  ant beta:organization:rbac-groups:members add \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn \
    --user-id user_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  member = client.beta.organization.rbac_groups.members.add(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn", user_id="user_01AbCdEfGhIjKlMnOpQrSt"
  )

  print(f"user_id: {member.user_id}")
  print(f"email: {member.email}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const member = await client.beta.organization.rbacGroups.members.add(
    "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
    { user_id: "user_01AbCdEfGhIjKlMnOpQrSt" }
  );

  console.log(`user_id: ${member.user_id}`);
  console.log(`email: ${member.email}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var member = await client.Beta.Organization.RbacGroups.Members.Add(
      "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
      new() { UserID = "user_01AbCdEfGhIjKlMnOpQrSt" }
  );

  Console.WriteLine($"user_id: {member.UserID}");
  Console.WriteLine($"email: {member.Email}");
  ```

  ```go Go
  client := anthropic.NewClient()

  member, err := client.Beta.Organization.RBACGroups.Members.Add(
  	context.Background(),
  	"rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  	anthropic.BetaOrganizationRBACGroupMemberAddParams{
  		UserID: "user_01AbCdEfGhIjKlMnOpQrSt",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("user_id: %s\n", member.UserID)
  fmt.Printf("email: %s\n", member.Email)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.members.MemberAddParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberAddParams.builder()
          .userId("user_01AbCdEfGhIjKlMnOpQrSt")
          .build();
      var member = client.beta().organization().rbacGroups().members()
          .add("rbac_group_01UvWxYzAbCdEfGhIjKlMn", params);

      IO.println("user_id: " + member.userId());
      IO.println("email: " + member.email());
  }
  ```

  ```php PHP
  $client = new Client();

  $member = $client->beta->organization->rbacGroups->members->add(
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
      userID: 'user_01AbCdEfGhIjKlMnOpQrSt',
  );

  echo "user_id: {$member->userID}\n";
  echo "email: {$member->email}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  member = client.beta.organization.rbac_groups.members.add(
    rbac_group_id,
    user_id: "user_01AbCdEfGhIjKlMnOpQrSt"
  )

  puts "user_id: #{member.user_id}"
  puts "email: #{member.email}"
  ```
</CodeGroup>

```json
{
  "type": "rbac_group_member",
  "rbac_group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
  "email": "jane@example.com",
  "created_at": "2026-07-09T18:00:00Z"
}
```

### Remove a member from a group

`DELETE /v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}` removes the member from the group; they remain a member of their organization. The request returns 404 if the user is not a member of the group, and 400 for `scim` groups, whose membership is managed in your identity provider. Requires the `write:rbac_groups` scope.

For complete parameter details and response schemas, see [Remove group member](https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/remove) in the API reference.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/rbac_groups/rbac_group_01UvWxYzAbCdEfGhIjKlMn/members/user_01AbCdEfGhIjKlMnOpQrSt" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-groups:members remove \
    --rbac-group-id rbac_group_01UvWxYzAbCdEfGhIjKlMn \
    --user-id user_01AbCdEfGhIjKlMnOpQrSt
  ```

  ```python Python
  client = anthropic.Anthropic()

  removed_member = client.beta.organization.rbac_groups.members.remove(
      "user_01AbCdEfGhIjKlMnOpQrSt", rbac_group_id="rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  )

  print(f"user_id: {removed_member.user_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const removedMember = await client.beta.organization.rbacGroups.members.remove(
    "user_01AbCdEfGhIjKlMnOpQrSt",
    { rbac_group_id: "rbac_group_01UvWxYzAbCdEfGhIjKlMn" }
  );

  console.log(`user_id: ${removedMember.user_id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var removedMember = await client.Beta.Organization.RbacGroups.Members.Remove(
      "user_01AbCdEfGhIjKlMnOpQrSt",
      new() { RbacGroupID = "rbac_group_01UvWxYzAbCdEfGhIjKlMn" }
  );

  Console.WriteLine($"user_id: {removedMember.UserID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  removedMember, err := client.Beta.Organization.RBACGroups.Members.Remove(
  	context.Background(),
  	"user_01AbCdEfGhIjKlMnOpQrSt",
  	anthropic.BetaOrganizationRBACGroupMemberRemoveParams{
  		RBACGroupID: "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("user_id: %s\n", removedMember.UserID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacgroups.members.MemberRemoveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = MemberRemoveParams.builder()
          .rbacGroupId("rbac_group_01UvWxYzAbCdEfGhIjKlMn")
          .build();
      var removedMember = client.beta().organization().rbacGroups().members()
          .remove("user_01AbCdEfGhIjKlMnOpQrSt", params);

      IO.println("user_id: " + removedMember.userId());
  }
  ```

  ```php PHP
  $client = new Client();

  $removedMember = $client->beta->organization->rbacGroups->members->remove(
      userID: 'user_01AbCdEfGhIjKlMnOpQrSt',
      rbacGroupID: 'rbac_group_01UvWxYzAbCdEfGhIjKlMn',
  );

  echo "user_id: {$removedMember->userID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_group_id = "rbac_group_01UvWxYzAbCdEfGhIjKlMn"
  removed_member = client.beta.organization.rbac_groups.members.remove(
    "user_01AbCdEfGhIjKlMnOpQrSt",
    rbac_group_id: rbac_group_id
  )

  puts "user_id: #{removed_member.user_id}"
  ```
</CodeGroup>

```json
{
  "rbac_group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "group_id": "rbac_group_01UvWxYzAbCdEfGhIjKlMn",
  "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
  "type": "rbac_group_member_deleted"
}
```

## Custom roles

Custom roles are read-only through the API: these endpoints catalog your organization's custom roles (defined in [claude.ai organization settings](https://claude.ai/admin-settings) or provisioned by Anthropic) and the permissions each role grants. Custom-role reads use the `read:members` scope (there is no separate role scope) and work with an organization-level key: unlike the group endpoints, they do not require a key created for all linked organizations, and the catalog returned is your organization's own.

Read a role's name from its `display_name` field. For a role provisioned by Anthropic, `display_name` can differ from the label claude.ai shows, and Anthropic might change the name. To keep a lasting reference to a role, store its `id`.

### List roles

`GET /v1/organizations/rbac_roles` returns your organization's custom roles. Requires the `read:members` scope.

For complete parameter details and response schemas, see [List roles](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_roles?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-roles list --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  roles = client.beta.organization.rbac_roles.list(limit=20)

  for role in roles:
      print(f"{role.id}: {role.display_name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const roles = await client.beta.organization.rbacRoles.list({ limit: 20 });

  for await (const role of roles) {
    console.log(`${role.id}: ${role.display_name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.RbacRoles.List(new() { Limit = 20 });

  await foreach (var role in page.Paginate())
  {
      Console.WriteLine($"{role.ID}: {role.DisplayName}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  roles := client.Beta.Organization.RBACRoles.ListAutoPaging(context.Background(), anthropic.BetaOrganizationRBACRoleListParams{
  	Limit: anthropic.Int(20),
  })

  for roles.Next() {
  	role := roles.Current()
  	fmt.Printf("%s: %s\n", role.ID, role.DisplayName)
  }
  if err := roles.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacroles.RbacRoleListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = RbacRoleListParams.builder()
          .limit(20)
          .build();
      var roles = client.beta().organization().rbacRoles().list(params);

      for (var role : roles.autoPager()) {
          IO.println(role.id() + ": " + role.displayName());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $roles = $client->beta->organization->rbacRoles->list(limit: 20);

  foreach ($roles->pagingEachItem() as $role) {
      echo "{$role->id}: {$role->displayName}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  roles = client.beta.organization.rbac_roles.list(limit: 20)

  roles.auto_paging_each do |role|
    puts "#{role.id}: #{role.display_name}"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "rbac_role",
      "id": "rbac_role_01CdEfGhIjKlMnOpQrStUv",
      "display_name": "Engineering base",
      "name": "Engineering base",
      "created_at": "2026-03-18T10:01:42Z",
      "updated_at": "2026-05-02T08:55:09Z"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

### Get a role

`GET /v1/organizations/rbac_roles/{rbac_role_id}` returns one role by ID. Requires the `read:members` scope.

For complete parameter details and response schemas, see [Get role](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/retrieve) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_roles/rbac_role_01CdEfGhIjKlMnOpQrStUv" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-roles retrieve \
    --rbac-role-id rbac_role_01CdEfGhIjKlMnOpQrStUv
  ```

  ```python Python
  client = anthropic.Anthropic()

  role = client.beta.organization.rbac_roles.retrieve("rbac_role_01CdEfGhIjKlMnOpQrStUv")

  print(f"id: {role.id}")
  print(f"display_name: {role.display_name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const role = await client.beta.organization.rbacRoles.retrieve(
    "rbac_role_01CdEfGhIjKlMnOpQrStUv"
  );

  console.log(`id: ${role.id}`);
  console.log(`display_name: ${role.display_name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var role = await client.Beta.Organization.RbacRoles.Retrieve("rbac_role_01CdEfGhIjKlMnOpQrStUv");

  Console.WriteLine($"id: {role.ID}");
  Console.WriteLine($"display_name: {role.DisplayName}");
  ```

  ```go Go
  client := anthropic.NewClient()

  role, err := client.Beta.Organization.RBACRoles.Get(context.Background(), "rbac_role_01CdEfGhIjKlMnOpQrStUv")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", role.ID)
  fmt.Printf("display_name: %s\n", role.DisplayName)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var role = client.beta().organization().rbacRoles()
      .retrieve("rbac_role_01CdEfGhIjKlMnOpQrStUv");

  IO.println("id: " + role.id());
  IO.println("display_name: " + role.displayName());
  ```

  ```php PHP
  $client = new Client();

  $role = $client->beta->organization->rbacRoles->retrieve(
      rbacRoleID: 'rbac_role_01CdEfGhIjKlMnOpQrStUv',
  );

  echo "id: {$role->id}\n";
  echo "display_name: {$role->displayName}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_role_id = "rbac_role_01CdEfGhIjKlMnOpQrStUv"
  role = client.beta.organization.rbac_roles.retrieve(rbac_role_id)

  puts "id: #{role.id}"
  puts "display_name: #{role.display_name}"
  ```
</CodeGroup>

### List a role's permissions

`GET /v1/organizations/rbac_roles/{rbac_role_id}/permissions` returns the role's permissions. Each permission pairs a `resource` (what it applies to: the organization's product features, a connector tool, a connector OAuth scope, one connector, or every connector) with an `action` (what it grants on that resource). Rows for features not enabled for your organization are omitted, so a page might contain fewer than `limit` rows while `has_more` is `true`. Requires the `read:members` scope.

Two `action` values need special care: an `organization` permission whose action is `capability_access_all` (every product feature) or `capability_access_all_ga` (every stable product feature, that is, every feature not labeled beta or research preview) is a blanket grant (one that covers neither model access nor the `permission_`-prefixed admin-panel permissions) and is listed as that single row rather than expanded. When you tally what a role grants, treat a blanket row as covering everything its variant describes, not just the features named in other rows.

For complete parameter details and response schemas, see [List role permissions](https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/permissions/list) in the API reference.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/rbac_roles/rbac_role_01CdEfGhIjKlMnOpQrStUv/permissions?limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:rbac-roles:permissions list \
    --rbac-role-id rbac_role_01CdEfGhIjKlMnOpQrStUv \
    --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  permissions = client.beta.organization.rbac_roles.permissions.list(
      "rbac_role_01CdEfGhIjKlMnOpQrStUv", limit=20
  )

  for permission in permissions:
      print(permission.action)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const permissions = await client.beta.organization.rbacRoles.permissions.list(
    "rbac_role_01CdEfGhIjKlMnOpQrStUv",
    { limit: 20 }
  );

  for await (const permission of permissions) {
    console.log(permission.action);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.RbacRoles.Permissions.List(
      "rbac_role_01CdEfGhIjKlMnOpQrStUv",
      new() { Limit = 20 }
  );

  await foreach (var permission in page.Paginate())
  {
      Console.WriteLine(permission.Action);
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  permissions := client.Beta.Organization.RBACRoles.Permissions.ListAutoPaging(
  	context.Background(),
  	"rbac_role_01CdEfGhIjKlMnOpQrStUv",
  	anthropic.BetaOrganizationRBACRolePermissionListParams{
  		Limit: anthropic.Int(20),
  	},
  )

  for permissions.Next() {
  	permission := permissions.Current()
  	fmt.Println(permission.Action)
  }
  if err := permissions.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.rbacroles.permissions.PermissionListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PermissionListParams.builder()
          .limit(20)
          .build();
      var permissions = client.beta().organization().rbacRoles().permissions()
          .list("rbac_role_01CdEfGhIjKlMnOpQrStUv", params);

      for (var permission : permissions.autoPager()) {
          IO.println(permission.action());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $permissions = $client->beta->organization->rbacRoles->permissions->list(
      rbacRoleID: 'rbac_role_01CdEfGhIjKlMnOpQrStUv',
      limit: 20,
  );

  foreach ($permissions->pagingEachItem() as $permission) {
      echo "{$permission->action}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  rbac_role_id = "rbac_role_01CdEfGhIjKlMnOpQrStUv"
  permissions = client.beta.organization.rbac_roles.permissions.list(rbac_role_id, limit: 20)

  permissions.auto_paging_each do |permission|
    puts permission.action
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "rbac_role_permission",
      "resource": {
        "type": "organization",
        "organization_id": "12345678-1234-5678-1234-567812345678"
      },
      "action": "capability_access_all_ga"
    },
    {
      "type": "rbac_role_permission",
      "resource": {
        "type": "connector_tool",
        "connector_id": "mcpsrv_01WxYzAbCdEfGhIjKlMnOp",
        "tool_name": "search_tickets"
      },
      "action": "use"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

## Example workflows

### Offboard a departing employee

1. Look up the member by email:

   <CodeGroup>
     ```bash cURL
     curl "https://api.anthropic.com/v1/organizations/users?email=departing@example.com" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2023-06-01"
     ```

     ```bash CLI
     ant organization:users list --email departing@example.com
     ```

     ```python Python
     client = anthropic.Anthropic()

     users = client.organization.users.list(email="departing@example.com")

     for user in users:
         print(f"{user.id}: {user.email} ({user.role})")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const users = await client.organization.users.list({ email: "departing@example.com" });

     for await (const user of users) {
       console.log(`${user.id}: ${user.email} (${user.role})`);
     }
     ```

     ```csharp C#
     AnthropicClient client = new();

     var page = await client.Organization.Users.List(new() { Email = "departing@example.com" });

     await foreach (var user in page.Paginate())
     {
         Console.WriteLine($"{user.ID}: {user.Email} ({user.Role.Raw()})");
     }
     ```

     ```go Go
     client := anthropic.NewClient()

     users := client.Organization.Users.ListAutoPaging(context.Background(), anthropic.OrganizationUserListParams{
     	Email: anthropic.String("departing@example.com"),
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
     import com.anthropic.models.organization.users.UserListParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = UserListParams.builder()
             .email("departing@example.com")
             .build();
         var users = client.organization().users().list(params);

         for (var user : users.autoPager()) {
             IO.println(user.id() + ": " + user.email() + " (" + user.role().asString() + ")");
         }
     }
     ```

     ```php PHP
     $client = new Client();

     $users = $client->organization->users->list(email: 'departing@example.com');

     foreach ($users->pagingEachItem() as $user) {
         echo "{$user->id}: {$user->email} ({$user->role})\n";
     }
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     users = client.organization.users.list(email: "departing@example.com")

     users.auto_paging_each do |user|
       puts "#{user.id}: #{user.email} (#{user.role})"
     end
     ```
   </CodeGroup>

2. Remove them with `DELETE /v1/organizations/users/{user_id}`, using the `id` from the response. Their seat, if any, returns to the pool.

3. If the person had not yet joined, the lookup returns no member; list invites and withdraw their `pending` invite instead.

### Audit group membership

1. List groups and record each group's `id`, `name`, and `role_ids`.

2. For each group that carries sensitive roles, page through `GET /v1/organizations/rbac_groups/{rbac_group_id}/members` and compare the member emails against your identity provider's roster.

3. Remove members who should no longer be in the group with `DELETE /v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`. For `scim` groups, make the change in your identity provider instead.

For a workflow that combines group membership with a temporary spend limit raise, see [Temporarily raise a member's spend limit during an incident](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#temporarily-raise-a-members-spend-limit-during-an-incident) on the Spend Limits API page.

## Frequently asked questions

### Is this a different API from the Admin API?

No. The member and invite endpoints are the same `/v1/organizations/` endpoints that Claude Console organizations use; this page documents their Claude Enterprise behavior. The group and custom-role endpoints are part of the same API and exist only for Claude Enterprise organizations. The [availability table](https://platform.claude.com/docs/en/manage-claude/user-management#which-endpoints-can-your-organization-use) shows which endpoints each organization type can call.

### Can I assign the owner or membership admin role through the API?

No. The API assigns only `user` and `managed`, on invite creation and role updates. Administrative roles are assigned in claude.ai organization settings, and members holding them cannot be modified or removed through the API.

### Can I create or modify groups through the API?

Yes, with the `write:rbac_groups` scope: create, rename, and delete groups, and add or remove their members. Two things the API cannot change: groups provisioned by your identity provider (`source_type: "scim"`), whose name and membership are owned by the identity provider, and custom roles, which are managed in claude.ai organization settings (the API [reads them](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles)).

### Does an unaccepted invite consume a seat?

On plans with a finite seat pool, yes: a `pending` invite holds a seat. Withdrawing the invite or letting it expire frees the seat. On plans without a seat pool, invites consume nothing.

### My organization uses single sign-on. Which operations work?

If your identity provider provisions users automatically (JIT or SCIM), invite creation returns 400. If it manages roles (advanced SSO or advanced SCIM provisioning), role updates return 400. If it manages membership (SCIM provisioning), member removals return 400. Reads work regardless.

### What happens to an Admin API key when the person who created it leaves?

The key keeps working. Admin API keys are scoped to the organization, not to individual users, and a key created in claude.ai does not expire. Removing the creator from the organization or deprovisioning them through your identity provider ends their own access, but not the keys they created. Downgrading their role does not change the keys either: each key stays active with its original scopes. When you offboard someone who created Admin API keys, delete those keys in the **Keys** section of [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access) and create replacements.

## See also

<CardGroup cols={2}>
  <Card title="Create an Admin API key" href="https://platform.claude.com/docs/en/manage-claude/admin-api-keys">
    Where your primary owner creates a scoped key and which scopes to select.
  </Card>

  <Card title="Compliance API" href="https://platform.claude.com/docs/en/manage-claude/compliance-api">
    Audit activity and retrieve or delete user content across your organization.
  </Card>

  <Card title="Analytics APIs" href="https://platform.claude.com/docs/en/manage-claude/analytics-api">
    Per-user and time-bucketed usage and cost reporting for Claude Enterprise.
  </Card>

  <Card title="Spend Limits API" href="https://platform.claude.com/docs/en/manage-claude/spend-limits-api">
    Set per-member spend limits and review increase requests.
  </Card>
</CardGroup>
