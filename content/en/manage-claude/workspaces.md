---
title: Workspaces
url: https://platform.claude.com/docs/en/manage-claude/workspaces
description: Organize API keys, manage team access, and control costs with workspaces.
---

Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.

## How workspaces work

Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.

Key characteristics:

* **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
* **Maximum 100 workspaces** per organization by default (archived workspaces don't count); contact your account team if you need more
* **Default Workspace** has a `wrkspc_` ID like any other workspace (returned in the [`anthropic-workspace-id` response header](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response) and accepted by [Get Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)), but it doesn't appear in [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) results, and API keys, usage reports, and cost reports show `null` for its `workspace_id`
* **API keys** are scoped to a single workspace and can only access resources within that workspace

### Claude Code workspace

When a member of your organization first signs in to [Claude Code](https://code.claude.com/docs/en/overview) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.

The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:

* Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
* A Claude Code key stops working if its owner is removed from the workspace or organization, unlike standard workspace keys.
* Claude Code usage is rate-limited separately, and admins can cap its share of the organization's limits under [Settings > Workspaces](https://platform.claude.com/settings/workspaces).
* It is the only workspace that supports per-user monthly spend limits.

<Warning>
  Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.
</Warning>

## Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

| Role                        | Permissions                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| Workspace User              | Use playground only                                                                             |
| Workspace Limited Developer | Create and manage API keys, use the API. Cannot access session tracing views or download files. |
| Workspace Developer         | Create and manage API keys, use the API                                                         |
| Workspace Admin             | Full control over workspace settings and members                                                |
| Workspace Billing           | View workspace billing information (inherited from organization billing role)                   |

### Role inheritance

* **Organization admins** automatically receive Workspace Admin access to all workspaces
* **Organization billing members** automatically receive Workspace Billing access to all workspaces
* **Organization users and developers** must be explicitly added to each workspace

<Note>
  The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.
</Note>

## Managing workspaces

<Note>
  Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.
</Note>

### Using the Console

Create and manage workspaces in the [Claude Console](https://platform.claude.com/settings/workspaces).

#### Create a workspace

<Steps>
  <Step title="Open workspace settings">
    In the Claude Console, go to **Settings > Workspaces**.
  </Step>

  <Step title="Create a workspace">
    Click **Create workspace**.
  </Step>

  <Step title="Configure the workspace">
    Enter a workspace name and select a color for visual identification.
  </Step>

  <Step title="Create the workspace">
    Click **Create** to finalize.
  </Step>
</Steps>

<Tip>
  To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.
</Tip>

#### Edit workspace details

To modify a workspace's name or color:

1. Select the workspace from the list.
2. Click the ellipsis menu (**...**) and choose **Edit details**.
3. Update the name or color and save your changes.

<Note>
  The Default Workspace cannot be renamed or deleted.
</Note>

#### Add members to a workspace

1. Navigate to the workspace's **Members** tab.
2. Click **Add to Workspace**.
3. Select an organization member and assign them a [workspace role](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions).
4. Confirm the addition.

To remove a member, click the trash icon next to their name.

<Note>
  Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.
</Note>

#### Set workspace limits

Each workspace's settings split these across two tabs:

* **Rate limits:** On the **Rate limits** tab, set limits per model tier for requests per minute, input tokens, or output tokens
* **Spend limits:** On the **Spend limits** tab, cap monthly spending and configure alerts when spending reaches certain thresholds

#### Archive a workspace

To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:

* Preserves historical data for reporting
* Deactivates the workspace and all associated API keys
* Cannot be undone

<Warning>
  Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone. If you archive the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.
</Warning>

### Using the Admin API

Programmatically manage workspaces using the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api).

<Note>
  Admin API endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys) for how to provision one.
</Note>

The following SDK and CLI examples construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable; the SDKs expose these endpoints under `client.beta.organization.workspaces`. SDK list methods fetch further pages on demand, so `limit` sets the page size; the PHP, Ruby, and curl examples return one page.

Create a workspace:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/workspaces" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{"name": "Production"}'
  ```

  ```bash CLI
  ant beta:organization:workspaces create --name Production
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.workspaces.create(name="Production")

  print(f"id: {workspace.id}")
  print(f"name: {workspace.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspace = await client.beta.organization.workspaces.create({ name: "Production" });

  console.log(`id: ${workspace.id}`);
  console.log(`name: ${workspace.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var workspace = await client.Beta.Organization.Workspaces.Create(new()
  {
      Name = "Production"
  });

  Console.WriteLine($"id: {workspace.ID}");
  Console.WriteLine($"name: {workspace.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  workspace, err := client.Beta.Organization.Workspaces.New(context.Background(), anthropic.BetaOrganizationWorkspaceNewParams{
  	Name: "Production",
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", workspace.ID)
  fmt.Printf("name: %s\n", workspace.Name)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.WorkspaceCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = WorkspaceCreateParams.builder()
          .name("Production")
          .build();
      var workspace = client.beta().organization().workspaces().create(params);

      IO.println("id: " + workspace.id());
      IO.println("name: " + workspace.name());
  }
  ```

  ```php PHP
  $client = new Client();

  $workspace = $client->beta->organization->workspaces->create(
      name: 'Production',
  );

  echo "id: {$workspace->id}\n";
  echo "name: {$workspace->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace = client.beta.organization.workspaces.create(name: "Production")

  puts "id: #{workspace.id}"
  puts "name: #{workspace.name}"
  ```
</CodeGroup>

List workspaces:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:workspaces list --limit 10 --include-archived=false
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspaces = client.beta.organization.workspaces.list(limit=10, include_archived=False)

  for workspace in workspaces:
      print(f"{workspace.id}: {workspace.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspaces = await client.beta.organization.workspaces.list({
    limit: 10,
    include_archived: false
  });

  for await (const workspace of workspaces) {
    console.log(`${workspace.id}: ${workspace.name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var workspaces = await client.Beta.Organization.Workspaces.List(new()
  {
      Limit = 10,
      IncludeArchived = false
  });

  await foreach (var workspace in workspaces.Paginate())
  {
      Console.WriteLine($"{workspace.ID}: {workspace.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  workspaces := client.Beta.Organization.Workspaces.ListAutoPaging(context.Background(), anthropic.BetaOrganizationWorkspaceListParams{
  	Limit:           anthropic.Int(10),
  	IncludeArchived: anthropic.Bool(false),
  })

  for workspaces.Next() {
  	workspace := workspaces.Current()
  	fmt.Printf("%s: %s\n", workspace.ID, workspace.Name)
  }
  if err := workspaces.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.workspaces.WorkspaceListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = WorkspaceListParams.builder()
          .limit(10)
          .includeArchived(false)
          .build();
      var workspaces = client.beta().organization().workspaces().list(params);

      for (var workspace : workspaces.autoPager()) {
          IO.println(workspace.id() + ": " + workspace.name());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $workspaces = $client->beta->organization->workspaces->list(
      limit: 10,
      includeArchived: false,
  );

  foreach ($workspaces->getItems() as $workspace) {
      echo "{$workspace->id}: {$workspace->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspaces = client.beta.organization.workspaces.list(limit: 10, include_archived: false)

  workspaces.data.each do |workspace|
    puts "#{workspace.id}: #{workspace.name}"
  end
  ```
</CodeGroup>

Archive a workspace:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/archive" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:organization:workspaces archive --workspace-id wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.workspaces.archive(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  )

  print(f"id: {workspace.id}")
  print(f"archived_at: {workspace.archived_at}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspace = await client.beta.organization.workspaces.archive(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  console.log(`id: ${workspace.id}`);
  console.log(`archived_at: ${workspace.archived_at}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var workspace = await client.Beta.Organization.Workspaces.Archive(
      "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  );

  Console.WriteLine($"id: {workspace.ID}");
  Console.WriteLine($"archived_at: {workspace.ArchivedAt:O}");
  ```

  ```go Go
  client := anthropic.NewClient()

  workspace, err := client.Beta.Organization.Workspaces.Archive(context.Background(), "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", workspace.ID)
  fmt.Printf("archived_at: %s\n", workspace.ArchivedAt)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var workspace = client.beta().organization().workspaces()
      .archive("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ");

  IO.println("id: " + workspace.id());
  IO.println("archived_at: " + workspace.archivedAt().orElseThrow());
  ```

  ```php PHP
  $client = new Client();

  $workspace = $client->beta->organization->workspaces->archive(
      workspaceID: 'wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ',
  );

  echo "id: {$workspace->id}\n";
  echo "archived_at: {$workspace->archivedAt?->format(DATE_ATOM)}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  workspace = client.beta.organization.workspaces.archive(workspace_id)

  puts "id: #{workspace.id}"
  puts "archived_at: #{workspace.archived_at}"
  ```
</CodeGroup>

For complete parameter details and response schemas, see the [Workspaces API reference](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve).

### Managing workspace members

Add a member to a workspace:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members" \
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

Update a member's role:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ/members/user_01XyDMpzjS89pFZXqSFUBDr6" \
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
      "user_01XyDMpzjS89pFZXqSFUBDr6",
      workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
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

For complete parameter details, see the [Workspace Members API reference](https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve).

## API keys and resource scoping

API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.

Resources scoped to workspaces include:

* **Files** created through the [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
* **Message Batches** created through the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
* **Skills** created through the [Skills API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)

Some resources cannot be managed with a workspace API key:

* **[MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)** are managed with a `workspace:manage_tunnels` OAuth token obtained through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation), not a workspace API key. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only; the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them.
* **Workspaces** themselves and **organization members** are managed at the organization level through the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api), which requires an Admin API key.

To look up your organization's workspace IDs, call the [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) endpoint or find them in the [Claude Console](https://platform.claude.com/settings/workspaces).

<Note>
  [Prompt caches](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) are also isolated per workspace on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). On Amazon Bedrock and Google Cloud, prompt caches are isolated per organization.
</Note>

## Identify the workspace behind an API response

Claude API responses include an `anthropic-workspace-id` header alongside the `request-id` and `anthropic-organization-id` [response headers](https://platform.claude.com/docs/en/api/overview#response-headers). Its value is the `wrkspc_`-prefixed ID of the workspace that the request's API key or access token resolved to, including when that workspace is the Default Workspace. For example, a successful response includes headers like these:

```http
HTTP/1.1 200 OK
request-id: req_018EeWyXxfu5pfWkrYcMdjWG
anthropic-organization-id: 0d0e7a3b-52f1-4c7e-9a51-3f6f2f7c1b9e
anthropic-workspace-id: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
```

The header is absent when the credential doesn't resolve to a workspace (for example, on Admin API requests) or when the request fails before authentication completes, such as a 401 error.

The following examples send a Messages API request and print the workspace ID from the response headers:

<CodeGroup>
  ```bash cURL
  # -D - prints the response headers; -o /dev/null discards the body
  curl -sS -D - -o /dev/null https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }' | grep -i '^anthropic-workspace-id'
  ```

  ```bash CLI
  # --debug prints the HTTP response, including the Anthropic-Workspace-Id
  # header, to stderr; > /dev/null hides the JSON body on stdout
  ant --debug messages create \
    --model claude-opus-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' > /dev/null
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.with_raw_response.create(
      model="claude-opus-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  workspace_id = response.headers.get("anthropic-workspace-id")
  print(f"Workspace ID: {workspace_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const { response } = await client.messages
    .create({
      model: "claude-opus-5",
      max_tokens: 1024,
      messages: [{ role: "user", content: "Hello, Claude" }]
    })
    .withResponse();
  console.log("Workspace ID:", response.headers.get("anthropic-workspace-id"));
  ```

  ```csharp C#
  AnthropicClient client = new();

  using var response = await client.WithRawResponse.Messages.Create(new()
  {
      Model = Model.ClaudeOpus5,
      MaxTokens = 1024,
      Messages = [new() { Role = Role.User, Content = "Hello, Claude" }]
  });
  var workspaceId = response.GetHeaderValues("anthropic-workspace-id").First();
  Console.WriteLine($"Workspace ID: {workspaceId}");
  ```

  ```go Go
  client := anthropic.NewClient()

  var response *http.Response
  _, err := client.Messages.New(
  	context.Background(),
  	anthropic.MessageNewParams{
  		Model:     anthropic.ModelClaudeOpus5,
  		MaxTokens: 1024,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  		},
  	},
  	option.WithResponseInto(&response),
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println("Workspace ID:", response.Header.Get("anthropic-workspace-id"))
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.http.HttpResponseFor;
  import com.anthropic.models.messages.Message;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      HttpResponseFor<Message> response = client.messages().withRawResponse().create(
          MessageCreateParams.builder()
              .model(Model.CLAUDE_OPUS_5)
              .maxTokens(1024)
              .addUserMessage("Hello, Claude")
              .build()
      );

      String workspaceId = response.headers().values("anthropic-workspace-id").getFirst();
      IO.println("Workspace ID: " + workspaceId);
  }
  ```

  ```php PHP
  $client = new Client();

  $response = $client->messages->raw->create([
      'model' => Model::CLAUDE_OPUS_5,
      'maxTokens' => 1024,
      'messages' => [['role' => 'user', 'content' => 'Hello, Claude']],
  ]);
  echo 'Workspace ID: ' . $response->getHeaderLine('anthropic-workspace-id') . "\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Read response headers in per-request middleware, which receives the
  # raw HTTP response before the SDK parses it
  workspace_id = nil
  read_workspace_id = lambda do |request, call_next|
    response = call_next.call(request)
    # Keys in response.headers are lowercase
    workspace_id = response.headers["anthropic-workspace-id"]
    response
  end

  client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }],
    request_options: { middleware: [read_workspace_id] }
  )
  puts "Workspace ID: #{workspace_id}"
  ```
</CodeGroup>

```text Output wrap
Workspace ID: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
```

The same accessors read the header from other Claude API endpoints too, including the [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) APIs. For example, read `anthropic-workspace-id` from the response that [creates a session](https://platform.claude.com/docs/en/managed-agents/sessions) to record which workspace the session belongs to.

With the workspace ID from a response, you can:

* Confirm which workspace's usage, cost, and [rate limits](https://platform.claude.com/docs/en/api/rate-limits) the request counted toward
* Match it against the `workspace_id` field in [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) reports and on [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) objects such as API keys (both report `null` for the Default Workspace)
* Check whether it's your Default Workspace's ID by passing it to [Get Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve) with an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys): the Default Workspace comes back with `"name": "Default"`, even though [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) omits it
* Open that workspace in the [Console](https://platform.claude.com/settings/workspaces) to find the request's resources, such as sessions, files, message batches, and skills

## Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.

### Setting workspace limits

You can set workspace limits lower than (but not higher than) your organization's limits:

* **Spend limits:** Cap monthly spending for a workspace. Set these on the workspace's **Spend limits** settings tab in the [Claude Console](https://platform.claude.com/settings/workspaces).
* **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute. Set these on the workspace's **Rate limits** settings tab in the [Claude Console](https://platform.claude.com/settings/workspaces).

<Note>
  - You cannot set limits on the Default Workspace
  - If not set, workspace limits match the organization's limits
  - Organization-wide limits always apply, even if workspace limits add up to more
</Note>

For detailed information on rate limits and how they work, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits). You can also read your current organization and workspace rate limits programmatically with the [Rate Limits API](https://platform.claude.com/docs/en/manage-claude/rate-limits-api).

## Usage and cost tracking

Track usage and costs by workspace using the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api):

```bash cURL
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

Usage and costs attributed to the Default Workspace have a `null` value for `workspace_id`.

## Common use cases

### Environment separation

Create separate workspaces for development, staging, and production:

| Workspace   | Purpose                                            |
| ----------- | -------------------------------------------------- |
| Development | Testing and experimentation with lower rate limits |
| Staging     | Pre-production testing with production-like limits |
| Production  | Live traffic with full rate limits and monitoring  |

### Team or department isolation

Assign workspaces to different teams for cost allocation and access control:

* **Engineering team** with developer access
* **Data science team** with their own API keys
* **Support team** with limited access for customer tools

### Project-based organization

Create workspaces for specific projects or products to track usage and costs separately.

## Best practices

<Steps>
  <Step title="Plan your workspace structure">
    Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.
  </Step>

  <Step title="Use meaningful names">
    Name workspaces clearly to indicate their purpose (for example, "Production - Customer Chatbot" or "Dev - Internal Tools").
  </Step>

  <Step title="Set appropriate limits">
    Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.
  </Step>

  <Step title="Audit access regularly">
    Review workspace membership periodically to ensure only appropriate users have access.
  </Step>

  <Step title="Monitor usage">
    Use the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) to track workspace-level consumption.
  </Step>
</Steps>

## FAQ

<AccordionGroup>
  <Accordion title="What's the Default Workspace?">
    Every organization has a "Default Workspace" that cannot be renamed, archived, or deleted. Like every workspace, it has a `wrkspc_` ID: the API returns it in the [`anthropic-workspace-id` response header](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response), and you can pass it to [Get Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve) and [Update Workspace](https://platform.claude.com/docs/en/api/admin/workspaces/update). It has no member list of its own, because access to it follows each member's organization role. It doesn't appear in [List Workspaces](https://platform.claude.com/docs/en/api/admin/workspaces/list) results, and API keys, usage reports, and cost reports that belong to it show `null` for `workspace_id`.
  </Accordion>

  <Accordion title="What's the Claude Code workspace?">
    Anthropic creates the Claude Code workspace automatically the first time a member of your organization signs in to Claude Code with their Console account. It isolates Claude Code's API keys, usage, and rate limits from your other workloads. See [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace) for details.
  </Accordion>

  <Accordion title="Are there limits on workspaces?">
    Yes. Each organization can have up to 100 workspaces by default, and archived workspaces don't count toward this limit. If you need more, contact your account team.
  </Accordion>

  <Accordion title="How do organization roles affect workspace access?">
    Organization admins automatically get the Workspace Admin role in all workspaces. Organization billing members automatically get the Workspace Billing role. Organization users and developers must be manually added to each workspace.
  </Accordion>

  <Accordion title="Which roles can be assigned in workspaces?">
    Organization users and developers can be assigned Workspace Admin, Workspace Developer, Workspace Limited Developer, or Workspace User roles. The Workspace Billing role cannot be manually assigned; it's inherited from having the organization `billing` role.
  </Accordion>

  <Accordion title="Can organization admin or billing members' workspace roles be changed?">
    Organization admins and billing members cannot have their workspace roles changed or be removed from workspaces while they hold those organization roles (with one exception: billing members can be upgraded to a Workspace Admin role). For everyone else covered by this constraint, change their organization role first to change their workspace access.
  </Accordion>

  <Accordion title="What happens to workspace access when organization roles change?">
    If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.
  </Accordion>

  <Accordion title="What happens to API keys when a user is removed from a workspace?">
    API keys persist in their current state as they are scoped to the organization and workspace, not to individual users. The exception is the [Claude Code workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#claude-code-workspace), where each key is bound to the member who created it and stops working when that member is removed.
  </Accordion>
</AccordionGroup>

## See also

* [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)
* [Admin API reference](https://platform.claude.com/docs/en/api/admin)
* [Rate limits](https://platform.claude.com/docs/en/api/rate-limits)
* [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)
