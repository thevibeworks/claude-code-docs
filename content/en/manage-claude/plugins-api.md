---
title: Plugins API
url: https://platform.claude.com/docs/en/manage-claude/plugins-api
description: "Inventory and manage the plugins in your Claude Enterprise organization: upload plugins and versions, choose the version members are served, control who can use each plugin, download plugin files for review, and validate a marketplace before you connect it."
---

The Plugins API lets you do the following:

* Inventory the plugins in your Claude Enterprise organization
* Publish plugins and new versions from your own pipelines
* Choose which version members are served
* Control who can use each plugin
* Download plugin files for review
* Check a Git marketplace before you connect it

For plugin *usage* reporting (which plugins and skills members use, and how often), see [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api).

<Check>
  **Scoped Admin API key required**

  These endpoints require an Admin API key with the `read:plugins` scope (for `GET` endpoints, including archive downloads) or the `write:plugins` scope (for `POST` and `DELETE` endpoints, except marketplace validation, which either scope allows); [Scopes](https://platform.claude.com/docs/en/manage-claude/plugins-api#scopes) has the details, including two other read scopes that also work. See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization) for where your primary owner creates one. Pass the key in the `x-api-key` header on every request, together with the [`anthropic-version`](https://platform.claude.com/docs/en/api/versioning) header and the beta header shown in the following note.
</Check>

<Note>
  The Plugins API is in **beta** and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

  Every request must include the [beta header](https://platform.claude.com/docs/en/api/beta-headers) `anthropic-beta: ce-plugins-2026-09-01` (the SDK and the `ant` CLI send it for you). A request without it returns `404`, exactly as if the endpoint did not exist.
</Note>

## Endpoints

The API exposes 18 endpoints across five resources:

| Resource | Endpoints |
| ----- | ----- |
| **Plugins:** list the plugins in the organization, upload a new one, look one up, choose the version members are served (roll back or promote), delete one | `GET /v1/organizations/plugins`<br />`POST /v1/organizations/plugins`<br />`GET /v1/organizations/plugins/{plugin_id}`<br />`POST /v1/organizations/plugins/{plugin_id}`<br />`DELETE /v1/organizations/plugins/{plugin_id}` |
| **Plugin versions:** list a plugin’s version history, upload a new version, look one up, download a version’s files | `GET /v1/organizations/plugins/{plugin_id}/versions`<br />`POST /v1/organizations/plugins/{plugin_id}/versions`<br />`GET /v1/organizations/plugins/{plugin_id}/versions/{version}`<br />`GET /v1/organizations/plugins/{plugin_id}/versions/{version}/content` |
| **Installation settings:** read who can use an organization-owned plugin, set it for the whole organization or for one group, remove either setting | `GET /v1/organizations/plugins/{plugin_id}/installation_settings`<br />`POST /v1/organizations/plugins/{plugin_id}/installation_settings/{target}`<br />`DELETE /v1/organizations/plugins/{plugin_id}/installation_settings/{target}` |
| **Shares:** read who a member has shared their own plugin with (read-only) | `GET /v1/organizations/plugins/{plugin_id}/shares` |
| **Plugin marketplaces:** find a marketplace’s ID, look one up, set the default installation setting for its plugins, check marketplace content before connecting it | `GET /v1/organizations/plugin_marketplaces`<br />`GET /v1/organizations/plugin_marketplaces/{marketplace_id}`<br />`POST /v1/organizations/plugin_marketplaces/{marketplace_id}`<br />`POST /v1/organizations/plugin_marketplaces/validate_repository`<br />`POST /v1/organizations/plugin_marketplaces/validate_archive` |

Plugins that Anthropic publishes are not inventoried; their usage is reported by the [Analytics APIs](https://platform.claude.com/docs/en/manage-claude/analytics-api). Marketplaces are created, connected to repositories, and deleted in claude.ai, not through this API.

Members and administrators can add plugins in claude.ai, so the inventory might list plugins that none of your pipelines created.

## Prerequisites

* Your organization must be on a Claude Enterprise plan.
* Your primary owner creates an Admin API key with the `read:plugins` scope, the `write:plugins` scope, or both in [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access). See [Create a key for a Claude Enterprise organization](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization).
* Every request carries three headers: `x-api-key`, `anthropic-version: 2026-10-21`, and `anthropic-beta: ce-plugins-2026-09-01`.

In Python, TypeScript, C#, Go, Java, PHP, and Ruby, the SDK exposes these endpoints under `client.beta.organization` (csharp, go: `client.Beta.Organization`; java: `client.beta().organization()`; php: `$client->beta->organization`), and the [`ant` CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) under `ant beta:organization`; they send the `anthropic-version` and `anthropic-beta` headers for you. The examples on this page read the Admin API key from the `ANTHROPIC_API_KEY` environment variable. Where an SDK or the CLI fetches more pages for you, `limit` sets the page size, not the total (see [Pagination](https://platform.claude.com/docs/en/manage-claude/plugins-api#pagination)).

API keys belong to the organization and keep working after the person who created them leaves. Do not share them or check them into source control.

## Quick start

List the plugins in your organization’s own marketplaces, newest first:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins?owner_type=organization&limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins list --owner-type organization --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  plugins = client.beta.organization.plugins.list(owner_type="organization", limit=20)

  # Automatically fetches more pages as needed.
  for plugin in plugins:
      print(f"{plugin.id}: {plugin.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const plugins = await client.beta.organization.plugins.list({
    owner_type: "organization",
    limit: 20
  });

  for await (const plugin of plugins) {
    console.log(`${plugin.id}: ${plugin.name}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Plugins;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Plugins.List(
      new() { OwnerType = OwnerType.Organization, Limit = 20 }
  );

  await foreach (var plugin in page.Paginate())
  {
      Console.WriteLine($"{plugin.ID}: {plugin.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  plugins := client.Beta.Organization.Plugins.ListAutoPaging(context.Background(), anthropic.BetaOrganizationPluginListParams{
  	OwnerType: anthropic.BetaOrganizationPluginListParamsOwnerTypeOrganization,
  	Limit:     anthropic.Int(20),
  })

  for plugins.Next() {
  	plugin := plugins.Current()
  	fmt.Printf("%s: %s\n", plugin.ID, plugin.Name)
  }
  if err := plugins.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.PluginListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginListParams.builder()
          .ownerType(PluginListParams.OwnerType.ORGANIZATION)
          .limit(20)
          .build();
      var plugins = client.beta().organization().plugins().list(params);

      for (var plugin : plugins.autoPager()) {
          IO.println(plugin.id() + ": " + plugin.name());
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Plugins\PluginListParams\OwnerType;
  // ...

  $client = new Client();

  $plugins = $client->beta->organization->plugins->list(
      limit: 20,
      ownerType: OwnerType::ORGANIZATION,
  );

  // Only this page; for the next, call list() again with page: $plugins->nextPage.
  foreach ($plugins->getItems() as $plugin) {
      echo "{$plugin->id}: {$plugin->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.plugins.list(owner_type: :organization, limit: 20)

  page.auto_paging_each do |plugin|
    puts "#{plugin.id}: #{plugin.name}"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "plugin",
      "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      "name": "sales-toolkit",
      "display_name": "Sales Toolkit",
      "description": "Account research and call prep for the sales team.",
      "served_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
      "served_version_pinned": true,
      "latest_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
      "manifest_version": "1.4.0",
      "owner": { "type": "organization" },
      "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
      "organization_installation_preference": "available",
      "organization_installation_preference_inherited": true,
      "content_scan": { "status": "completed", "assessment": "pass", "reason": null },
      "components": [
        {
          "type": "skill",
          "name": "account-research",
          "description": "Researches a customer account before a call."
        },
        { "type": "mcp_server", "name": "crm", "description": null }
      ],
      "reach": "remote",
      "created_at": "2026-09-01T17:04:11Z",
      "updated_at": "2026-09-15T14:12:30Z"
    }
  ],
  "next_page": "page_xK9f2LqT7vNw3pRzBd8sHy"
}
```

In this example the plugin is pinned to an earlier version: a newer version (`latest_version_id`) is stored but not served.

## Scopes

| Scope | Grants |
| ----- | ----- |
| `read:plugins` | Every `GET` endpoint on this page, including archive downloads, plus marketplace validation. |
| `write:plugins` | Every `POST` and `DELETE` endpoint on this page: create a plugin, create a version, change the served version, delete a plugin, set and remove installation settings, and set a marketplace’s default, plus marketplace validation. It does not grant reads. |
| `read:org_audit` | A read-only scope for security-audit integrations: every `GET` endpoint on this page, including archive downloads, plus the [user management](https://platform.claude.com/docs/en/manage-claude/user-management) and [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) read endpoints. It does not grant marketplace validation or any write. |
| `read:compliance_org_data` | The Compliance API’s scope for organization metadata (names, types, roles, and groups) and effective settings. Grants every `GET` endpoint on this page, exactly as `read:org_audit` does, so a Compliance Access Key can read plugins without a second key. It does not grant marketplace validation or any write. |

A key can carry several scopes. An integration that uploads a plugin and then reads it back needs both `read:plugins` and `write:plugins`. Wherever this page says an endpoint requires the `read:plugins` scope, a key with `read:org_audit` or `read:compliance_org_data` works too.

### Access to members’ plugin files

Each of these read scopes can download the files of plugins in members’ personal marketplaces: `read:plugins`, `read:org_audit`, and `read:compliance_org_data`. That includes files that claude.ai’s admin settings do not show. A `read:org_audit` or `read:compliance_org_data` key bound to your parent organization can do this in any organization under it that has access to this API. To do so, pass `organization_id` (see [Reading another organization under the same parent](https://platform.claude.com/docs/en/manage-claude/plugins-api#reading-another-organization-under-the-same-parent)). Each download of a member-owned plugin’s files through this API records a `claude_plugin_archive_accessed` event on the Compliance API Activity Feed (see [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)). The event identifies the key, the plugin, the version, and the member (see [Activity Feed events](https://platform.claude.com/docs/en/manage-claude/plugins-api#activity-feed-events)). Downloads of organization-owned plugins are not recorded.

### Reading another organization under the same parent

`read:plugins` and `write:plugins` keys read and write only the organization they were created in. Some companies have several Claude organizations linked under one parent organization. A `read:org_audit` or `read:compliance_org_data` [key created for all linked organizations](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization) can also read any linked organization that has access to this API. To read one, pass its ID in the `organization_id` query parameter on any `GET` endpoint on this page. The ID is the organization UUID shown in claude.ai’s settings (its `org_`-prefixed form is accepted too). Without the parameter, the key reads the organization it was created in. A key with no organization of its own must always pass `organization_id`. A `404` means the named organization is not under the key’s parent or the API is not available to it; a value that is not a UUID or `org_` ID returns `400`. Any other key that names an organization other than its own gets `404`. Writes do not accept `organization_id`.

## Key concepts

### Plugins and components

A **plugin** is a package that extends Claude for your organization’s members. It contains any combination of these components:

| Component | What it is |
| ----- | ----- |
| Skill | Instructions and files that Claude loads when a task calls for it. |
| Command | A saved prompt a member runs by typing `/` followed by the command’s name. |
| Agent | A helper assistant with its own instructions, to which Claude can hand part of a task. |
| Hook | An action that runs automatically when an event occurs in a session, such as before Claude uses a tool. |
| MCP server | A connection from Claude to tools and data in another system (Model Context Protocol). |
| CLI | A command-line program that the plugin lets Claude run. |

Every plugin has a manifest at `.claude-plugin/plugin.json`. The manifest’s `name` becomes the plugin’s `name`: a lowercase identifier that is unique within its marketplace.

### Marketplaces

A **marketplace** is a container of plugins. Each marketplace has an owner and a source.

* **Owner.** The organization owns its marketplaces. Each member can also have personal marketplaces.
* **Source.** `manual` means plugins are uploaded, in claude.ai or, for an organization marketplace, through this API. `github`, `gitlab`, and `public_git` mean plugins are synchronized from a Git repository the owner connected. Nothing can be uploaded to a synchronized marketplace, and this API cannot delete its plugins, because the next synchronization would undo either change. Change the repository instead.

Your organization’s **library marketplace** is the organization-owned `manual` marketplace that uploads go to when you do not name a marketplace. It is created the first time something is uploaded to it.

### Organization-owned and member-owned plugins

A plugin’s `owner.type` says whose marketplace it lives in:

* `organization`: you can manage it through this API, except that a plugin in a marketplace synchronized from Git cannot receive uploads or be deleted here.
* `user`: it lives in one member’s personal marketplace. You can read its details and download its files, and delete it if its marketplace is `manual`. Uploading versions and choosing the served version return `403`. Sharing is managed only by the member, in claude.ai.

Removing a member from the organization does not remove their plugins. They stay in the inventory under the member’s `user_id`, and the `owner_user_id` filter still finds them, so you can review and remove a departed member’s content. They are removed from the inventory when the member’s account is deleted.

### Versions and the served version

Every upload creates a new, immutable **version**, whether it comes from this API, from claude.ai, or from a Git synchronization. A plugin has two pointers to its versions:

* `latest_version_id`: the newest version
* `served_version_id`: the version members are served

By default `served_version_pinned` is `false`: the served version normally follows the newest one. When content scanning is on, a version saved in claude.ai might **wait** for its content scan: it is stored but not served at once. This page uses “wait” only for a version saved in claude.ai, not for one that a member or an administrator publishes into a plugin. While scanning is on, a waiting version is served only when its `content_scan` reads `completed` with `pass` or `warn`. While a version waits, `served_version_id` names an earlier version than `latest_version_id`. Do not poll until the two IDs match: they might stay different, for example when the scan fails.

The rules in this section describe organization-owned plugins. A member-owned plugin’s served version is controlled by its owner in claude.ai.

#### Pins

A plugin becomes **pinned** to a version (`served_version_pinned: true`) in any of these ways:

* You choose the version with `POST /v1/organizations/plugins/{plugin_id}`.
* An administrator chooses the version in claude.ai.
* A member or an administrator publishes the version into the plugin, and the publish goes through.

A plugin stays pinned permanently: it cannot be unpinned. Any of these actions can pin it again later, to the same version or to another one.

While a plugin is pinned, a new version from this API or from a Git synchronization is stored and advances `latest_version_id`. It is not served until someone chooses it.

The table shows what happens to a version that an administrator saves in claude.ai. The result depends on where the pin was last set and on the plugin’s newest version before the save.

| Where the pin was last set | The plugin’s newest version before the save | The version saved in claude.ai |
| ----- | ----- | ----- |
| Through this API | Any version | Is stored and is not served until someone chooses it. |
| In claude.ai | The served version or a waiting version | Might become the served version without anyone choosing it. `served_version_pinned` stays `true`. |
| In claude.ai | Another version (for example, an upload of yours that is not served yet) | Is stored and is not served until someone chooses it. |

Treat a pin that was set through this API before November 8, 2026, as set in claude.ai. To replace it, use this API to set the version you want served.

No field shows where the pin was last set. If your pipeline should determine what is served, [set the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#change-the-served-version) through this API on every run. Send the request with the version you want served, even if that version is already served. Do the same to replace a pin set through this API before November 8, 2026.

Each successful request also has two effects:

* **It sets the pin through this API again.** The pin stays set through this API until someone chooses a version in claude.ai or until a publish into the plugin goes through. After that, the plugin is still pinned. However, until your next run, saves in claude.ai might change the served version again.
* **It cancels any wait.** A version that was waiting for its content scan stays stored. It is served only if someone chooses it.

A pin lets a release pipeline upload each build, test it, and then promote it. To have your pipeline determine when each build is served, pin the plugin. [Set `served_version_id`](https://platform.claude.com/docs/en/manage-claude/plugins-api#change-the-served-version) to the version you want served, even if that version is already served. From then on, promote each build you want served. With content scanning on, the request that pins the plugin returns `409 scan_pending` while the version’s `content_scan` reads `processing`. It returns `400 scan_failed` if the scan reads `fail`, `unknown`, or `errored` (`warn` is accepted). Any later request that changes the served version gets the same checks (see [Content scanning](https://platform.claude.com/docs/en/manage-claude/plugins-api#content-scanning)).

To roll back, set `served_version_id` to an earlier version. Roll forward the same way.

### Installation settings

**Installation settings** determine who can use an organization-owned plugin. Each setting has one of four values, carried in the fields named `installation_preference` (and, on the plugin and marketplace objects, `organization_installation_preference` and `default_installation_preference`):

| Value | Members see |
| ----- | ----- |
| `required` | The plugin is installed and cannot be removed. |
| `auto_install` | The plugin is installed and can be removed. |
| `available` | The plugin can be installed on request. |
| `not_available` | The plugin is hidden. |

A plugin can hold an organization-wide setting and one setting for each group (the role-based access control [groups managed in User management](https://platform.claude.com/docs/en/manage-claude/user-management#groups)). A member gets a value by these rules:

1. The organization-wide value is the plugin’s own organization-wide setting if it has one, otherwise its marketplace’s default, otherwise `not_available`. The plugin reports this value in `organization_installation_preference`, with `organization_installation_preference_inherited: true` while it comes from the marketplace default.
2. A member who belongs to no group holding a setting for the plugin gets the organization-wide value.
3. A member who belongs to one or more groups holding a setting gets the most permissive of those groups’ settings instead, ranked `required`, `auto_install`, `available`, `not_available`.

A group’s setting replaces the organization-wide value for its members; it does not add to it. For example, if the organization-wide value is `required` and the Pilot group holds `available`, Pilot members get `available`. When you move a plugin from a pilot group to the whole organization, set the organization-wide value and then remove the group’s setting. Setting the organization-wide value stops the plugin from inheriting its marketplace default; [removing the organization-wide setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#remove-an-installation-setting) returns the plugin to that default.

A plugin created through this API starts with no settings of its own, so it inherits its marketplace’s default: `not_available` unless someone has set a default. Deleting a group removes its settings from every plugin.

### Shares

**Shares** determine who can use a member-owned plugin. The owner shares it in claude.ai with every member, with a group, or with named members. This API lists shares but cannot change them.

If your organization has turned off a kind of sharing in its claude.ai settings, shares of that kind still appear in the list but give no one access while that setting is off; the list itself does not show whether it is.

### Content scanning

Content scanning is an organization setting in claude.ai. When it is on, newly stored versions are scanned (claude.ai exempts some) and the result is reported in `content_scan`. A version that was not scanned has `content_scan: null`. For example, it might have been stored before scanning was turned on. Scanning is not offered to organizations that use customer-managed encryption keys or zero data retention.

While scanning is on, members are served a plugin only when its served version’s scan is `completed` with `pass` or `warn`. While the scan is `processing` or `errored`, or reads `fail` or `unknown`, the plugin is withheld from members, and an earlier version is not served in its place. A version that was never scanned (`content_scan: null`) is served normally.

A version you upload through this API never waits for its content scan. When it becomes the served version, members lose the plugin until its `content_scan` reads `completed` with `pass` or `warn`. If members should keep the current version while a new one is scanned, pin the plugin first (see [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)).

While a version saved in claude.ai waits for its scan, the served version does not change. When your API upload becomes the served version, any wait ends: the waiting version is served only if someone chooses it. To see a waiting version’s scan, read the version (see [List a plugin’s versions](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-a-plugins-versions)).

After an upload, `content_scan.status` is `processing` and the verdict arrives asynchronously. Read the version to see it; the plugin object shows only its served version’s scan. While scanning is on, changing the served version to a version whose `content_scan` reads `processing` returns `409 scan_pending`, and changing it to one whose scan reads `fail`, `unknown`, or `errored` returns `400 scan_failed`.

#### Failed scans allowed in claude.ai

In claude.ai, organization owners can allow a version whose scan failed. So can members whose [custom role](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles) can manage **Libraries**. This API can then report that scan as `completed` with `warn` and the failed scan’s `reason`. While it does, the rules for `warn` apply: the version can be served to members, and you can make it the served version. Nothing in the response shows that it was allowed, so a `warn` is either a warning or a failed scan that was allowed. Allowing a version whose scan reads `warn` does not change its `content_scan`. When a version stops being allowed, this API reports the verdict of its newest completed scan. A served version whose scan then reads `fail` or `unknown` is withheld from members.

### Reach

`reach` summarizes, in one value, how far a version reaches on members’ machines and beyond:

| Value | Meaning |
| ----- | ----- |
| `remote` | Declares an MCP server, a CLI, or something that counts as one, whatever else it declares. |
| `privileged` | Is not `remote` but meets at least one condition in the list after this table. |
| `contained` | Is neither `remote` nor `privileged` (typically, a plugin that holds only skills, commands, and agents, and none of them has `allowed-tools`). |

A `privileged` version meets at least one of these conditions:

* It declares a hook of any type, even one that posts to a URL (see the [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)).
* It declares a monitor (a background command that keeps running during a session).
* It declares an LSP (Language Server Protocol) server.
* It declares a workflow (a script that Claude Code can run). Any file in a `workflows/` folder at the plugin’s root counts as one.
* It declares settings that the plugin applies to the member’s app.
* It contains a Markdown file whose frontmatter pre-approves tools (`allowed-tools`). The file can be a skill, a command, or any other Markdown file. An `allowed-tools` value does not count if it is empty or if it lists one or more of `AskUserQuestion`, `TodoWrite`, and `ToolSearch` and nothing else.

All of these run or take effect on the member’s own computer. From there, some can still send data elsewhere, as a hook that posts to a URL does.

`reach` counts everything that the version declares. That includes monitors, LSP servers, workflows, and app settings, which `components` does not list. A version with an empty `components` list can therefore still be `privileged`. Such a version can also be `remote` if something else it declares makes it `remote`.

`reach` can be `null` for these versions:

* A version stored before components were recorded
* A version whose reach could not be determined because one of its skills’ `SKILL.md` or one of its command files could not be read

A version that declares an MCP server or a CLI is `remote` even if a `SKILL.md` or command file could not be read. Under today’s rules, a version with an unreadable `SKILL.md` or command file is never `contained`: if it is not `remote`, it is `null` or `privileged`. Treat `null` as unclassified, not as `contained`.

The server normally works out the value when a version is stored, under the rules of that time. An older version can therefore have a different value from the one that the same files would get today:

* An older version can be `contained` where the same files, stored today, would be `privileged`, `remote`, or `null`.
* An older version can be `privileged` where the same files, stored today, would be `remote`.

### Upload requirements

Uploads through this API follow these rules:

* The upload is either one `.zip` or `.plugin` archive, or a set of individual files. An archive may wrap everything in one top-level folder.
* It must contain exactly one manifest, at `.claude-plugin/plugin.json`, which must declare a `name`. A bare `SKILL.md` without a manifest is rejected.
* A top-level `SKILL.md` whose frontmatter declares plugin components is merged into the manifest; `plugin.json` wins wherever both set a value. A `description` that the manifest takes from that `SKILL.md` is cut to its first 500 characters.
* `name` may contain lowercase letters (from any alphabet), digits, and hyphens, up to 64 characters. Uppercase letters, spaces, underscores, and other punctuation are rejected.
* `displayName` is at most 64 characters and `description` at most 500.
* Every `SKILL.md` needs valid YAML frontmatter with a `name` and `description`, neither containing XML tags such as `<example>`. Two skills, or two commands, cannot share a name.
* No file may be under a top-level `bin/` directory.
* No nested `.zip` files. Packaged MCP servers (`.mcpb`, `.dxt`) are allowed.
* File paths must be relative, contain no `..`, and use only letters, digits, spaces, and `_ . - / ( ) ,`.
* The request body and the uncompressed archive are each at most 200 MB; a request body over the limit returns `413` (`request_too_large`) rather than `400`. An upload has at most 5,000 files, a path depth of 12, paths of 472 characters, and file or folder names of 255 characters.
* ZIP archives must use DEFLATE or STORE compression, and cannot be encrypted or contain symbolic links.
* An upload that creates a plugin returns `400` once the marketplace holds 1,000 plugins. Plugins that this API does not list also count, so the limit can be reached while [List plugins](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-plugins) shows fewer than 1,000 in that marketplace. Anthropic can raise the 5,000-file limit.

## Example workflows

### Publish each build from a release pipeline

Upload every tagged build from CI and let the pipeline determine when a build is served. The key needs the `read:plugins` and `write:plugins` scopes.

This workflow has a one-time setup and then steps for each new build. Where you start depends on the plugin:

* **A new plugin:** Start at step 1 of the setup.
* **An existing plugin, pinned or not:** Decide on the version you want served (see [List a plugin’s versions](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-a-plugins-versions)) and keep its ID. Then start at step 3 of the setup.

Set up the plugin once:

<Steps>
  <Step title="Find the marketplace">
    Find the marketplace to upload into with `GET /v1/organizations/plugin_marketplaces?owner_type=organization&source=manual`. Pass its ID as `marketplace_id` in step 2. To use the library marketplace, omit `marketplace_id`.
  </Step>

  <Step title="Create the plugin">
    [Create the plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-plugin) from your first build with `POST /v1/organizations/plugins`. Your first build becomes the served version. It is the version you want served, so keep its ID. The response’s `latest_version_id` is that ID. If the response is lost, see [Retrying uploads](https://platform.claude.com/docs/en/manage-claude/plugins-api#retrying-uploads) before you send the request again.
  </Step>

  <Step title="Check the scan of the version you want served">
    When content scanning is on, poll `GET /v1/organizations/plugins/{plugin_id}/versions/{version}` until the `content_scan.status` of the version you want served is no longer `processing`. Then act on the result:

    * **`content_scan` is `null`:** The version has no scan to check. Go on to step 4.
    * **`completed` with `pass` or `warn`:** Go on to step 4.
    * **`errored`:** Read it again after a few minutes, because a later read might report the result.
    * **`fail`, `unknown`, or still `errored`:** Decide on another version and repeat this step for it. If no other version is suitable, [upload a new version](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-version). That new version is now the version you want served, so repeat this step for it. If the plugin is not pinned (`served_version_pinned: false`), the upload is normally served at once. In that case, members cannot get the plugin until that version’s scan reads `completed` with `pass` or `warn`.

    When content scanning is off, go on to step 4.
  </Step>

  <Step title="Pin the plugin">
    To keep members on one version while each new build is checked, pin the plugin. [Set `served_version_id`](https://platform.claude.com/docs/en/manage-claude/plugins-api#change-the-served-version) to the version you want served, even if that version is already served. Keep that version’s ID. If the plugin is already pinned, this request sets the pin through this API, no matter how it was set before (see [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)). After the pin is set, each upload is stored without being served. A plugin cannot be unpinned, so every later build you want served must be promoted.
  </Step>
</Steps>

Then follow these steps for each new build:

<Steps>
  <Step title="Upload the build">
    Record the plugin’s `latest_version_id`. Then [upload a version](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-version) with `POST /v1/organizations/plugins/{plugin_id}/versions`. If the upload’s response is lost, read the plugin and retry only if `latest_version_id` is unchanged (see [Retrying uploads](https://platform.claude.com/docs/en/manage-claude/plugins-api#retrying-uploads)).
  </Step>

  <Step title="Check the new version’s scan">
    When content scanning is on, poll `GET /v1/organizations/plugins/{plugin_id}/versions/{version}` until `content_scan.status` is no longer `processing`. If `content_scan` is `null`, there is no scan to check, so you can promote the build. Otherwise, promote it only when the scan is `completed` with `pass` or `warn`. If the scan reads `errored`, read it again after a few minutes, because a later read might report the result. Go on to the next step even if you will not promote the build.
  </Step>

  <Step title="Set the served version">
    To [promote the build](https://platform.claude.com/docs/en/manage-claude/plugins-api#change-the-served-version), send `POST /v1/organizations/plugins/{plugin_id}` with `{"served_version_id": "<the new version's ID>"}`. To roll back, send an earlier version’s ID the same way. If a run promotes no build, still send the request. Send it with the version you want served, even if that version is already served. Keep the ID of each version you set. Your pipeline needs it when a run promotes no build. Do not take that ID from `served_version_id`, which might name a version saved in claude.ai. Each successful request sets the pin through this API again and cancels any wait (see [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)).
  </Step>
</Steps>

The pin always holds back your own uploads. It does not always hold back a version that an administrator saves in claude.ai. [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins) explains when such a version can become the served version and what to do about it.

Serving a version does not make the plugin available to members. A plugin created through this API inherits its marketplace’s default, which is `not_available` unless someone has set one (see [Installation settings](https://platform.claude.com/docs/en/manage-claude/plugins-api#installation-settings)).

### Roll a plugin out to a pilot group, then to everyone

1. Look up the pilot group’s ID with `GET /v1/organizations/rbac_groups`. That call needs the `read:rbac_groups` scope (see [Groups and roles in User management](https://platform.claude.com/docs/en/manage-claude/user-management#groups-and-roles)). The next steps need `write:plugins`, which acts only on the organization its key was created in, so in an enterprise with several linked organizations, create one key in the organization that holds the plugin and give it both scopes, or use a second key created there for those steps.

2. [Give the group its own setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#set-an-installation-setting), for example `auto_install`, with `POST /v1/organizations/plugins/{plugin_id}/installation_settings/{target}`, where `{target}` is the group’s `rbac_group_` ID, while the organization-wide value stays `not_available`. Only the group’s members get the plugin.

3. When the pilot ends, set the organization-wide value with the following call, then remove the group’s setting so the group follows the organization again. Setting the organization-wide value stops the plugin from inheriting its marketplace default; [removing the organization-wide setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#remove-an-installation-setting) later returns the plugin to that default.

   <CodeGroup>
     ```bash cURL
     curl -X POST "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/installation_settings/organization" \
       -H "content-type: application/json" \
       -H "x-api-key: $ANTHROPIC_API_KEY" \
       -H "anthropic-version: 2026-10-21" \
       -H "anthropic-beta: ce-plugins-2026-09-01" \
       -d '{"installation_preference": "required"}'
     ```

     ```bash CLI
     ant beta:organization:plugins:installation-settings set \
       --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
       --target organization \
       --installation-preference required
     ```

     ```python Python
     client = anthropic.Anthropic()

     setting = client.beta.organization.plugins.installation_settings.set(
         "organization",
         plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
         installation_preference="required",
     )

     print(f"plugin_id: {setting.plugin_id}")
     print(f"installation_preference: {setting.installation_preference}")
     ```

     ```typescript TypeScript
     const client = new Anthropic();

     const setting = await client.beta.organization.plugins.installationSettings.set(
       "organization",
       {
         plugin_id: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
         installation_preference: "required"
       }
     );

     console.log(`plugin_id: ${setting.plugin_id}`);
     console.log(`installation_preference: ${setting.installation_preference}`);
     ```

     ```csharp C#
     using Anthropic.Models.Beta.Organization.Plugins.InstallationSettings;

     AnthropicClient client = new();

     var setting = await client.Beta.Organization.Plugins.InstallationSettings.Set(
         "organization",
         new()
         {
             PluginID = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
             InstallationPreference = InstallationPreference.Required,
         }
     );

     Console.WriteLine($"plugin_id: {setting.PluginID}");
     Console.WriteLine($"installation_preference: {setting.InstallationPreference.Raw()}");
     ```

     ```go Go
     client := anthropic.NewClient()

     setting, err := client.Beta.Organization.Plugins.InstallationSettings.Set(
     	context.Background(),
     	"organization",
     	anthropic.BetaOrganizationPluginInstallationSettingSetParams{
     		PluginID:               "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
     		InstallationPreference: anthropic.BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceRequired,
     	},
     )
     if err != nil {
     	log.Fatal(err)
     }

     fmt.Printf("plugin_id: %s\n", setting.PluginID)
     fmt.Printf("installation_preference: %s\n", setting.InstallationPreference)
     ```

     ```java Java
     import com.anthropic.models.beta.organization.plugins.installationsettings.InstallationSettingSetParams;

     void main() {
         AnthropicClient client = AnthropicOkHttpClient.fromEnv();

         var params = InstallationSettingSetParams.builder()
             .pluginId("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")
             .installationPreference(InstallationSettingSetParams.InstallationPreference.REQUIRED)
             .build();
         var setting = client.beta().organization().plugins().installationSettings()
             .set("organization", params);

         IO.println("plugin_id: " + setting.pluginId());
         IO.println("installation_preference: " + setting.installationPreference().asString());
     }
     ```

     ```php PHP
     use Anthropic\Beta\Organization\Plugins\InstallationSettings\InstallationSettingSetParams\InstallationPreference;
     // ...

     $client = new Client();

     $setting = $client->beta->organization->plugins->installationSettings->set(
         target: 'organization',
         pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
         installationPreference: InstallationPreference::REQUIRED,
     );

     echo "plugin_id: {$setting->pluginID}\n";
     echo "installation_preference: {$setting->installationPreference}\n";
     ```

     ```ruby Ruby
     client = Anthropic::Client.new

     plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
     setting = client.beta.organization.plugins.installation_settings.set(
       "organization",
       plugin_id: plugin_id,
       installation_preference: :required
     )

     puts "plugin_id: #{setting.plugin_id}"
     puts "installation_preference: #{setting.installation_preference}"
     ```
   </CodeGroup>

   Then remove the group’s setting with `DELETE /v1/organizations/plugins/{plugin_id}/installation_settings/{target}`, where `{target}` is the group’s ID. A group’s setting replaces the organization-wide value for its members rather than adding to it, so a leftover group setting of `available` would keep those members on `available`.

### Keep a security inventory in sync

Run these steps as a nightly job:

<Steps>
  <Step title="List every plugin">
    Page through [`GET /v1/organizations/plugins?limit=100`](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-plugins) until `next_page` is `null` (see [Pagination](https://platform.claude.com/docs/en/manage-claude/plugins-api#pagination)). Read each plugin’s `reach` and `content_scan` from that list.

    Do this for every plugin on every run. `updated_at` normally tells you which plugins have new content or a new served version since the last run. It can miss these changes:

    * **A change to `content_scan` alone:** This change does not move `updated_at`. One example is a verdict that arrives later.
    * **A waiting version:** A waiting version (see [Versions and the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#versions-and-the-served-version)) moves `updated_at` when it becomes the served version. It does not necessarily move `updated_at` when it is stored. To notice one, compare `latest_version_id` with the value from your last run.
    * **A removed plugin:** A plugin disappears without an event when a Git synchronization or an account deletion removes it. The full list is what shows that it is gone.
  </Step>

  <Step title="Flag plugins for review">
    Flag each plugin that meets either of these tests:

    * Its `reach` is `remote`. For example, it declares an MCP server or a CLI.
    * Its `content_scan.assessment` is `warn`, `fail`, or `unknown`. A `warn` can also be a [failed scan that was allowed in claude.ai](https://platform.claude.com/docs/en/manage-claude/plugins-api#failed-scans-allowed-in-claude-ai). Leave `warn` out only if you accept every failed scan that is allowed there.

    For a stricter job, add one or both of these tests:

    * Its `reach` is anything other than `contained` (see [Reach](https://platform.claude.com/docs/en/manage-claude/plugins-api#reach)). This test adds `privileged`, `null` (unclassified), and any value added later.
    * Its `content_scan` or its `content_scan.assessment` is `null`, so no completed scan is reported. Where content scanning is off, this test can flag every plugin.

    The tests in this step have two limits:

    * The tests on `reach` read the stored value. For an older version, that value can understate its reach (see [Reach](https://platform.claude.com/docs/en/manage-claude/plugins-api#reach)).
    * `reach` and `content_scan` describe the served version. To also check a newer version that is not served, list the plugin’s versions when `latest_version_id` differs from `served_version_id` (see [List a plugin’s versions](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-a-plugins-versions)).
  </Step>

  <Step title="Download the flagged versions">
    For each flagged plugin, download the served version’s archive for review with `GET /v1/organizations/plugins/{plugin_id}/versions/{served_version_id}/content` (see [Download a version’s files](https://platform.claude.com/docs/en/manage-claude/plugins-api#download-a-versions-files)). Also download any unserved version that meets one of the tests you use in step 2. Use that version’s ID in place of `{served_version_id}`.

    A version’s files never change. You can skip a version that you have already reviewed unless its `content_scan` has changed since then.
  </Step>

  <Step title="Take a plugin away from members if you need to">
    To take a plugin away from members while you review it, see [Delete a plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#delete-a-plugin). That section has two options: a reversible one for organization-owned plugins and a permanent one.
  </Step>
</Steps>

## Plugins

The plugin object describes a plugin in one of your organization’s marketplaces or in a member’s personal marketplace (the [Quick start](https://platform.claude.com/docs/en/manage-claude/plugins-api#quick-start) response shows a complete one). Its `display_name`, `description`, `manifest_version`, `content_scan`, `components`, and `reach` describe its **served** version, so one list call shows what members are being served.

| Field | Description |
| ----- | ----- |
| `id` | Prefixed `plugin_`. |
| `name` | From the manifest. Unique within its marketplace, not across the organization. Fixed for an organization-owned plugin; changes if a member renames their own plugin in claude.ai. |
| `display_name`, `description`, `manifest_version` | The served version’s manifest `displayName`, `description`, and `version`; each is `null` when the manifest declares none. `description` might be a skill’s `description` rather than the manifest’s (described after this table). `manifest_version` is normalized for display: one leading `v` or `V` is dropped, so a manifest `version` of `"v1.4.0"` is returned as `"1.4.0"`. It is also `null` for a value that does not look like a version number, such as `"latest"`, and for a plugin version created before claude.ai started recording this field in August 2026. An upload is never refused because of its `version`, and `manifest_version` is not unique. |
| `served_version_id`, `latest_version_id` | Prefixed `pluginver_`: the version members are served, and the newest version. See [Versions and the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#versions-and-the-served-version). |
| `served_version_pinned` | `false` until the plugin is pinned (see [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)); `true` from then on. |
| `owner` | `{"type": "organization"}`, or `{"type": "user", "user_id": "user_..."}` for a member’s personal marketplace. |
| `marketplace_id` | Prefixed `marketplace_`. |
| `created_by` | Who created the plugin: `{"type": "user_actor", "user_id": "user_...", "email_address": "..."}` for a person in claude.ai (`email_address` might be `null`) or `{"type": "api_actor", "api_key_id": "apikey_..."}` for an API key. Other actor types might appear. `null` when no creator is recorded, such as for plugins synchronized from Git. |
| `organization_installation_preference`, `organization_installation_preference_inherited` | Organization-owned: the organization-wide value, and whether it comes from the marketplace’s default (see [Installation settings](https://platform.claude.com/docs/en/manage-claude/plugins-api#installation-settings)). Member-owned: both `null`. |
| `content_scan` | The served version’s scan result, an object with `status`, `assessment`, and `reason` (described after this table). `null` when it was never scanned. |
| `components` | The served version’s components, each `{"type", "name", "description"}` with `type` one of `skill`, `mcp_server`, `command`, `agent`, `hook`, or `cli`, listed in that type order and then by name. For an MCP server, `name` is its key in the manifest; for a hook, the event it runs on; for a CLI, the executable’s name. `description` is always `null` for MCP servers, hooks, and CLIs. `null` when not recorded. |
| `reach` | `contained`, `privileged`, `remote`, or `null`. See [Reach](https://platform.claude.com/docs/en/manage-claude/plugins-api#reach). |
| `updated_at` | Changes when the served version changes, when the plugin becomes pinned, and normally when a new version is stored. A waiting version (see [Versions and the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#versions-and-the-served-version)) changes it when it becomes the served version, not necessarily when it is stored. It does not change for installation settings, shares, or a change to `content_scan` alone. |

`description` is not always the manifest’s. A `description` that the manifest takes from a top-level `SKILL.md` is cut to its first 500 characters (see [Upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements)). If the manifest’s `description` is the first 500 characters of exactly one distinct skill `description` in `components`, the API returns that skill `description` instead. As a result:

* A `description` that you read might be longer than 500 characters, the limit on `description` in an uploaded manifest. An upload whose `plugin.json` sets such a `description` returns `400`.
* In the [files you download](https://platform.claude.com/docs/en/manage-claude/plugins-api#download-a-versions-files), `.claude-plugin/plugin.json` might have a different `description`, or none.

The `content_scan` object:

| Field | Description |
| ----- | ----- |
| `status` | `processing` while the scan runs, `completed` when it finished, or `errored` when it could not finish (or, occasionally, when its result could not be read for this response, in which case a later read might report it). The newest completed scan, if any, is reported. Members are not served a version whose `status` is `processing` or `errored`; uploading the content again as a new version gets a fresh scan. |
| `assessment` | Set when `status` is `completed`: `pass` (nothing found), `warn` (something found that does not block use, or a [failed scan that was allowed in claude.ai](https://platform.claude.com/docs/en/manage-claude/plugins-api#failed-scans-allowed-in-claude-ai)), `fail` (something found that blocks use), or `unknown` (no verdict). Otherwise `null`. |
| `reason` | For `warn` and `fail`, the main concern, from the following list. Otherwise `null`, and also `null` on an older scan that predates reason recording. |

<Accordion title="Content scan reason values">
  | `reason` | Meaning |
  | ----- | ----- |
  | `covert-usage-telemetry` | Tells Claude to send information about the member or their usage to an outside address without telling them. |
  | `undisclosed-data-destination` | Sends files, emails, documents, or other content to a fixed outside destination the member is not shown and does not control. |
  | `remote-code-instruction-loader` | Tells Claude to download and run, or follow instructions from, outside content that can change after the plugin is installed. |
  | `credential-exposure` | Contains live credentials, or collects credentials or tokens from the member’s environment. |
  | `guardrail-tampering` | Weakens the member’s safeguards, for example by pre-approving every permission prompt. |
  | `system-prompt-spoofing` | Imitates or attempts to replace Claude’s system instructions. |
  | `covert-record-tampering` | Quietly changes, hides, or deletes information the member would otherwise see. |
  | `covert-behavior-override` | Changes Claude’s behavior beyond the plugin’s purpose and hides the change from the member. |
  | `hidden-code-execution` | Runs bundled code while telling Claude not to reveal what it does. |
  | `undisclosed-promotion-injection` | Inserts undisclosed promotional content into Claude’s output. |
  | `hidden-identity-gate` | Changes or stops its behavior depending on which account runs it, without saying why. |
  | `destructive-persistence` | Can delete or corrupt the member’s files, or install programs that remain after the plugin. |
  | `unanalyzable-binary` | Includes a compiled or unreadable program, so the scan could not verify what it does. |
  | `other` | Any other concern, including one newer than this list. |
</Accordion>

A `plugin_id` that lacks the `plugin_` prefix returns `400`. A `plugin_id` that carries the prefix but is not in your organization’s inventory returns `404`.

### List plugins

`GET /v1/organizations/plugins` lists the plugins in your organization, in the organization’s marketplaces and in members’ personal marketplaces, ordered by `created_at` descending. Filter by `owner_type` (`organization` or `user`), `owner_user_id` (an ID prefixed `user_`, which finds a member’s plugins, including after the member leaves the organization), `marketplace_id`, and `created_at[gte]`, `created_at[gt]`, `created_at[lte]`, `created_at[lt]` (RFC 3339 timestamps). Filters combine with AND. A `marketplace_id` or `owner_user_id` that matches nothing in your organization returns an empty page, not an error. The response has the shape shown in [Quick start](https://platform.claude.com/docs/en/manage-claude/plugins-api#quick-start). Requires the `read:plugins` scope.

To find plugins that are new since you last listed them, compare the `id` values in the full list with those in the earlier list. Do not rely on `created_at[gt]` for this: a plugin might enter this list with a `created_at` earlier than the time of your last list.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins?owner_type=organization&limit=20" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins list --owner-type organization --limit 20
  ```

  ```python Python
  client = anthropic.Anthropic()

  plugins = client.beta.organization.plugins.list(owner_type="organization", limit=20)

  # Automatically fetches more pages as needed.
  for plugin in plugins:
      print(f"{plugin.id}: {plugin.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const plugins = await client.beta.organization.plugins.list({
    owner_type: "organization",
    limit: 20
  });

  for await (const plugin of plugins) {
    console.log(`${plugin.id}: ${plugin.name}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Plugins;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.Plugins.List(
      new() { OwnerType = OwnerType.Organization, Limit = 20 }
  );

  await foreach (var plugin in page.Paginate())
  {
      Console.WriteLine($"{plugin.ID}: {plugin.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  plugins := client.Beta.Organization.Plugins.ListAutoPaging(context.Background(), anthropic.BetaOrganizationPluginListParams{
  	OwnerType: anthropic.BetaOrganizationPluginListParamsOwnerTypeOrganization,
  	Limit:     anthropic.Int(20),
  })

  for plugins.Next() {
  	plugin := plugins.Current()
  	fmt.Printf("%s: %s\n", plugin.ID, plugin.Name)
  }
  if err := plugins.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.PluginListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginListParams.builder()
          .ownerType(PluginListParams.OwnerType.ORGANIZATION)
          .limit(20)
          .build();
      var plugins = client.beta().organization().plugins().list(params);

      for (var plugin : plugins.autoPager()) {
          IO.println(plugin.id() + ": " + plugin.name());
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Plugins\PluginListParams\OwnerType;
  // ...

  $client = new Client();

  $plugins = $client->beta->organization->plugins->list(
      limit: 20,
      ownerType: OwnerType::ORGANIZATION,
  );

  // Only this page; for the next, call list() again with page: $plugins->nextPage.
  foreach ($plugins->getItems() as $plugin) {
      echo "{$plugin->id}: {$plugin->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.plugins.list(owner_type: :organization, limit: 20)

  page.auto_paging_each do |plugin|
    puts "#{plugin.id}: #{plugin.name}"
  end
  ```
</CodeGroup>

### Create a plugin

`POST /v1/organizations/plugins` creates an organization-owned plugin and its first version in one call; the version becomes the served version. The body is `multipart/form-data`: `files[]` is either one `.zip` or `.plugin` archive, or one part for each file, where each part’s file name is the file’s path within the plugin (for example `.claude-plugin/plugin.json`). Optional fields are `marketplace_id` (an organization-owned `manual` marketplace, or by default your library marketplace, which is created on first use) and `release_notes` (up to 5,000 characters, shown in claude.ai’s version history and returned on the version). The plugin’s `name`, `display_name`, `description`, and `manifest_version` come from the uploaded files, and the upload must meet the [upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements). When content scanning is on, the response’s `content_scan.status` is `processing` and the verdict arrives asynchronously. Returns the plugin. Requires the `write:plugins` scope.

Upload an archive:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugins" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -F "files[]=@dist/sales-toolkit.zip" \
    -F "release_notes=First release"
  ```

  ```bash CLI
  ant beta:organization:plugins create \
    --file dist/sales-toolkit.zip \
    --release-notes "First release"
  ```

  ```python Python
  client = anthropic.Anthropic()

  with open("dist/sales-toolkit.zip", "rb") as archive:
      plugin = client.beta.organization.plugins.create(
          files=[archive],
          release_notes="First release",
      )

  print(f"id: {plugin.id}")
  print(f"served_version_id: {plugin.served_version_id}")
  ```

  ```typescript TypeScript
  import fs from "node:fs";

  const client = new Anthropic();

  const plugin = await client.beta.organization.plugins.create({
    files: [fs.createReadStream("dist/sales-toolkit.zip")],
    release_notes: "First release"
  });

  console.log(`id: ${plugin.id}`);
  console.log(`served_version_id: ${plugin.served_version_id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var plugin = await client.Beta.Organization.Plugins.Create(
      new()
      {
          Files = [File.OpenRead("dist/sales-toolkit.zip")],
          ReleaseNotes = "First release",
      }
  );

  Console.WriteLine($"id: {plugin.ID}");
  Console.WriteLine($"served_version_id: {plugin.ServedVersionID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  archive, err := os.Open("dist/sales-toolkit.zip")
  if err != nil {
  	log.Fatal(err)
  }
  defer archive.Close()

  plugin, err := client.Beta.Organization.Plugins.New(context.Background(), anthropic.BetaOrganizationPluginNewParams{
  	Files:        []io.Reader{archive},
  	ReleaseNotes: anthropic.String("First release"),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", plugin.ID)
  fmt.Printf("served_version_id: %s\n", plugin.ServedVersionID)
  ```

  ```java Java
  import com.anthropic.core.MultipartField;
  import com.anthropic.models.beta.organization.plugins.PluginCreateParams;

  void main() throws Exception {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      // Build the `files[]` part by hand so the archive is sent with its file name,
      // which the upload requires.
      var archive = MultipartField.<List<InputStream>>builder()
          .value(List.of(Files.newInputStream(Path.of("dist/sales-toolkit.zip"))))
          .filename("sales-toolkit.zip")
          .contentType("application/octet-stream")
          .build();
      var params = PluginCreateParams.builder()
          .files(archive)
          .releaseNotes("First release")
          .build();
      var plugin = client.beta().organization().plugins().create(params);

      IO.println("id: " + plugin.id());
      IO.println("served_version_id: " + plugin.servedVersionId());
  }
  ```

  ```php PHP
  use Anthropic\Core\FileParam;

  $client = new Client();

  $plugin = $client->beta->organization->plugins->create(
      files: [
          FileParam::fromResource(fopen('dist/sales-toolkit.zip', 'r')),
      ],
      releaseNotes: 'First release',
  );

  echo "id: {$plugin->id}\n";
  echo "served_version_id: {$plugin->servedVersionID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin = client.beta.organization.plugins.create(
    files: [Pathname("dist/sales-toolkit.zip")],
    release_notes: "First release"
  )

  puts "id: #{plugin.id}"
  puts "served_version_id: #{plugin.served_version_id}"
  ```
</CodeGroup>

```json
{
  "type": "plugin",
  "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "name": "sales-toolkit",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "served_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
  "served_version_pinned": false,
  "latest_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
  "manifest_version": "1.4.0",
  "owner": { "type": "organization" },
  "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "content_scan": { "status": "processing", "assessment": null, "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null }
  ],
  "reach": "remote",
  "created_at": "2026-09-01T17:04:11Z",
  "updated_at": "2026-09-01T17:04:11Z"
}
```

To upload individual files, attach each file under its path within the plugin. Each part’s file name sets that path. A manifest sent under its base name alone (`plugin.json`) is not found. Where a file’s path cannot be set, upload the plugin as one archive instead. Upload into a named marketplace:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugins" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -F "files[]=@.claude-plugin/plugin.json;filename=.claude-plugin/plugin.json" \
    -F "files[]=@skills/account-research/SKILL.md;filename=skills/account-research/SKILL.md" \
    -F "marketplace_id=marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  ```

  ```bash CLI
  # The CLI sends each file under its base name only,
  # so upload the plugin as one archive instead.
  ant beta:organization:plugins create \
    --file dist/sales-toolkit.zip \
    --marketplace-id marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r
  ```

  ```python Python
  client = anthropic.Anthropic()

  # A (filename, file) tuple keeps each file's path within the plugin;
  # a bare file object would be sent under its base name only.
  with (
      open(".claude-plugin/plugin.json", "rb") as manifest,
      open("skills/account-research/SKILL.md", "rb") as skill_md,
  ):
      plugin = client.beta.organization.plugins.create(
          files=[
              (".claude-plugin/plugin.json", manifest),
              ("skills/account-research/SKILL.md", skill_md),
          ],
          marketplace_id="marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      )

  print(f"id: {plugin.id}")
  print(f"served_version_id: {plugin.served_version_id}")
  ```

  ```typescript TypeScript
  import fs from "node:fs";

  const client = new Anthropic();

  // The TypeScript SDK sends each file under its base name,
  // so upload the plugin as one archive.
  const plugin = await client.beta.organization.plugins.create({
    files: [fs.createReadStream("dist/sales-toolkit.zip")],
    marketplace_id: "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  });

  console.log(`id: ${plugin.id}`);
  console.log(`served_version_id: ${plugin.served_version_id}`);
  ```

  ```csharp C#
  using Anthropic.Core;

  AnthropicClient client = new();

  // FileName keeps each file's path within the plugin; without it, a FileStream
  // is sent under its base name only.
  var plugin = await client.Beta.Organization.Plugins.Create(
      new()
      {
          Files =
          [
              new BinaryContent
              {
                  Stream = File.OpenRead(".claude-plugin/plugin.json"),
                  FileName = ".claude-plugin/plugin.json",
              },
              new BinaryContent
              {
                  Stream = File.OpenRead("skills/account-research/SKILL.md"),
                  FileName = "skills/account-research/SKILL.md",
              },
          ],
          MarketplaceID = "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      }
  );

  Console.WriteLine($"id: {plugin.ID}");
  Console.WriteLine($"served_version_id: {plugin.ServedVersionID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  manifest, err := os.Open(".claude-plugin/plugin.json")
  if err != nil {
  	log.Fatal(err)
  }
  defer manifest.Close()

  skillMd, err := os.Open("skills/account-research/SKILL.md")
  if err != nil {
  	log.Fatal(err)
  }
  defer skillMd.Close()

  // anthropic.File keeps each file's path within the plugin as the part's file name;
  // a bare *os.File would be sent under its base name and the manifest would not be found.
  plugin, err := client.Beta.Organization.Plugins.New(context.Background(), anthropic.BetaOrganizationPluginNewParams{
  	Files: []io.Reader{
  		anthropic.File(manifest, ".claude-plugin/plugin.json", "application/json"),
  		anthropic.File(skillMd, "skills/account-research/SKILL.md", "text/markdown"),
  	},
  	MarketplaceID: anthropic.String("marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"),
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", plugin.ID)
  fmt.Printf("served_version_id: %s\n", plugin.ServedVersionID)
  ```

  ```java Java
  import com.anthropic.core.MultipartField;
  import com.anthropic.models.beta.organization.plugins.PluginCreateParams;

  void main() throws Exception {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      // The `files` setters on PluginCreateParams take one file name for the whole
      // list, so upload the plugin as one archive instead: a single hand-built
      // part that carries the archive's file name, which the upload requires.
      var archive = MultipartField.<List<InputStream>>builder()
          .value(List.of(Files.newInputStream(Path.of("dist/sales-toolkit.zip"))))
          .filename("sales-toolkit.zip")
          .contentType("application/octet-stream")
          .build();
      var params = PluginCreateParams.builder()
          .files(archive)
          .marketplaceId("marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r")
          .build();
      var plugin = client.beta().organization().plugins().create(params);

      IO.println("id: " + plugin.id());
      IO.println("served_version_id: " + plugin.servedVersionId());
  }
  ```

  ```php PHP
  use Anthropic\Core\FileParam;

  $client = new Client();

  $plugin = $client->beta->organization->plugins->create(
      files: [
          FileParam::fromResource(
              fopen('.claude-plugin/plugin.json', 'r'),
              filename: '.claude-plugin/plugin.json',
          ),
          FileParam::fromResource(
              fopen('skills/account-research/SKILL.md', 'r'),
              filename: 'skills/account-research/SKILL.md',
          ),
      ],
      marketplaceID: 'marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r',
  );

  echo "id: {$plugin->id}\n";
  echo "served_version_id: {$plugin->servedVersionID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # A FilePart with filename: keeps each file's path within the plugin;
  # a bare Pathname would be sent under its base name only.
  plugin = client.beta.organization.plugins.create(
    files: [
      Anthropic::FilePart.new(
        Pathname(".claude-plugin/plugin.json"),
        filename: ".claude-plugin/plugin.json"
      ),
      Anthropic::FilePart.new(
        Pathname("skills/account-research/SKILL.md"),
        filename: "skills/account-research/SKILL.md"
      )
    ],
    marketplace_id: "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  )

  puts "id: #{plugin.id}"
  puts "served_version_id: #{plugin.served_version_id}"
  ```
</CodeGroup>

Besides a `400` for an upload that breaks the [upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements) (`413` for a request body over 200 MB) and the shared responses (a `403` when `marketplace_id` is a member’s personal marketplace; see [Error responses](https://platform.claude.com/docs/en/manage-claude/plugins-api#error-responses)), a create can fail with:

| Status | Cause | What to do |
| ----- | ----- | ----- |
| 404 | `marketplace_id` is not a marketplace of your organization. | Take the ID from [List marketplaces](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-marketplaces). |
| 400 | The marketplace is synchronized from Git, or already holds 1,000 plugins (see [Upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements)). | Upload to another `manual` marketplace, or change the repository instead. |
| 409 `plugin_name_taken` | The name is taken in that marketplace. | Upload a version to `details.plugin_id` only if it is the plugin you meant to update, because someone else might have made it. Otherwise, or when `details.plugin_id` is absent, upload under another name (change the manifest `name`). |
| 409 `skill_name_taken` | The plugin is going into the library marketplace and one of its skills has an organization skill’s name. | Rename the skill, or remove the organization skill in claude.ai. |
| 409 (no `error_code`) | Another upload with the same name to the same marketplace is in progress, or a plugin that this API does not list holds the name. | Retry with backoff. If the `409` persists for more than a few minutes, upload under another name (change the manifest `name`). |
| 503 `registration_pending` | The plugin was created but its registration did not complete. | Do not resend; upload the same files as a version of `details.plugin_id` (see [Retrying uploads](https://platform.claude.com/docs/en/manage-claude/plugins-api#retrying-uploads)). |

### Get a plugin

`GET /v1/organizations/plugins/{plugin_id}` returns one plugin. Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins retrieve \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL
  ```

  ```python Python
  client = anthropic.Anthropic()

  plugin = client.beta.organization.plugins.retrieve("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")

  print(f"id: {plugin.id}")
  print(f"name: {plugin.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const plugin = await client.beta.organization.plugins.retrieve(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  );

  console.log(`id: ${plugin.id}`);
  console.log(`name: ${plugin.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var plugin = await client.Beta.Organization.Plugins.Retrieve("plugin_01Hq3vX8kZcN2mB7pR4tY9wL");

  Console.WriteLine($"id: {plugin.ID}");
  Console.WriteLine($"name: {plugin.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  plugin, err := client.Beta.Organization.Plugins.Get(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", plugin.ID)
  fmt.Printf("name: %s\n", plugin.Name)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var plugin = client.beta().organization().plugins()
      .retrieve("plugin_01Hq3vX8kZcN2mB7pR4tY9wL");

  IO.println("id: " + plugin.id());
  IO.println("name: " + plugin.name());
  ```

  ```php PHP
  $client = new Client();

  $plugin = $client->beta->organization->plugins->retrieve(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
  );

  echo "id: {$plugin->id}\n";
  echo "name: {$plugin->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  plugin = client.beta.organization.plugins.retrieve(plugin_id)

  puts "id: #{plugin.id}"
  puts "name: #{plugin.name}"
  ```
</CodeGroup>

### Change the served version

`POST /v1/organizations/plugins/{plugin_id}` changes which version of an organization-owned plugin members are served. Pass an earlier version to roll back or a newer one to promote a build that was stored without being served. The only updatable field is `served_version_id`, and it is required. The change reaches members before the response returns and does not create a version. When content scanning is on, the version must be one members can be served (see [Content scanning](https://platform.claude.com/docs/en/manage-claude/plugins-api#content-scanning)). Returns the plugin. Requires the `write:plugins` scope.

Every successful request also has these effects:

* It pins the plugin to that version, and a pinned plugin cannot be unpinned here or in claude.ai. Passing the version already served pins an unpinned plugin, so later uploads stop being served automatically.
* It sets the pin through this API. From then on, saves in claude.ai do not change the served version until someone chooses a version in claude.ai or until a publish into the plugin goes through (see [Pins](https://platform.claude.com/docs/en/manage-claude/plugins-api#pins)). The plugin stays pinned either way.
* It cancels any wait (see [Versions and the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#versions-and-the-served-version)). A version that was waiting for its content scan stays stored. It is served only if someone chooses it.

If the plugin is already pinned and no version is waiting, passing the version already served changes no field and records no event. It still sets the pin through this API, which no field shows.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -d '{"served_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p"}'
  ```

  ```bash CLI
  ant beta:organization:plugins update \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --served-version-id pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p
  ```

  ```python Python
  client = anthropic.Anthropic()

  plugin = client.beta.organization.plugins.update(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      served_version_id="pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  )

  print(f"id: {plugin.id}")
  print(f"served_version_id: {plugin.served_version_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const plugin = await client.beta.organization.plugins.update(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
    { served_version_id: "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p" }
  );

  console.log(`id: ${plugin.id}`);
  console.log(`served_version_id: ${plugin.served_version_id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var plugin = await client.Beta.Organization.Plugins.Update(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      new() { ServedVersionID = "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p" }
  );

  Console.WriteLine($"id: {plugin.ID}");
  Console.WriteLine($"served_version_id: {plugin.ServedVersionID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  plugin, err := client.Beta.Organization.Plugins.Update(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginUpdateParams{
  		ServedVersionID: "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", plugin.ID)
  fmt.Printf("served_version_id: %s\n", plugin.ServedVersionID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.PluginUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginUpdateParams.builder()
          .servedVersionId("pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p")
          .build();
      var plugin = client.beta().organization().plugins()
          .update("plugin_01Hq3vX8kZcN2mB7pR4tY9wL", params);

      IO.println("id: " + plugin.id());
      IO.println("served_version_id: " + plugin.servedVersionId());
  }
  ```

  ```php PHP
  $client = new Client();

  $plugin = $client->beta->organization->plugins->update(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
      servedVersionID: 'pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p',
  );

  echo "id: {$plugin->id}\n";
  echo "served_version_id: {$plugin->servedVersionID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  plugin = client.beta.organization.plugins.update(
    plugin_id,
    served_version_id: "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p"
  )

  puts "id: #{plugin.id}"
  puts "served_version_id: #{plugin.served_version_id}"
  ```
</CodeGroup>

```json
{
  "type": "plugin",
  "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "name": "sales-toolkit",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "served_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "served_version_pinned": true,
  "latest_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "manifest_version": "1.5.0",
  "owner": { "type": "organization" },
  "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "content_scan": { "status": "completed", "assessment": "pass", "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null },
    {
      "type": "command",
      "name": "call-prep",
      "description": "Builds a one-page brief for an upcoming call."
    }
  ],
  "reach": "remote",
  "created_at": "2026-09-01T17:04:11Z",
  "updated_at": "2026-09-16T10:02:45Z"
}
```

Besides the shared responses (a `403` for a member-owned plugin, and `409 scan_pending` or `400 scan_failed` for a version members cannot be served; see [Error responses](https://platform.claude.com/docs/en/manage-claude/plugins-api#error-responses)), the request can fail with:

| Status | Cause | What to do |
| ----- | ----- | ----- |
| 400 | The body omits `served_version_id`, sets it to `null`, or contains any other field; or the value lacks the `pluginver_` prefix or is `latest`. | Send exactly `{"served_version_id": "pluginver_..."}`. |
| 404 | `served_version_id` is not a version of this plugin. | Take the ID from [List a plugin’s versions](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-a-plugins-versions). |
| 409 (no `error_code`) | An upload to this plugin or another served-version change is still in progress. | Retry shortly. |
| 409 `skill_name_taken` | The plugin is in the library marketplace and the version has a skill whose name an organization skill now uses. | Choose another version, upload one with the skill renamed, or remove the organization skill in claude.ai. |

### Delete a plugin

`DELETE /v1/organizations/plugins/{plugin_id}` permanently deletes a plugin and every version it holds, just as an administrator’s delete in claude.ai does. It works on any plugin in a `manual` marketplace, including a member’s plugin, even if that member has since left the organization. When the delete returns, the plugin, its versions, and their files are gone from every read, and members are no longer served it. An organization-owned plugin’s installation settings are removed with it; a member-owned plugin’s shares are withdrawn, and it disappears for its owner too. A plugin in a marketplace synchronized from Git returns `400`: remove it from the repository, or remove the marketplace in claude.ai. Requires the `write:plugins` scope.

Deletion cannot be undone, and there is no per-version delete. To withhold an organization-owned plugin reversibly instead, set its organization-wide installation setting to `not_available` (a plugin that was inheriting its marketplace’s default gets a setting of its own, and [removing that organization-wide setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#remove-an-installation-setting) later returns the plugin to the default), and remove (or set to `not_available`) every group setting that `GET /v1/organizations/plugins/{plugin_id}/installation_settings` lists, because a group’s setting overrides the organization-wide value for its members. Send these writes one after another, not in parallel (see [Set an installation setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#set-an-installation-setting)). A member-owned plugin cannot be withheld through this API except by deleting it, and only if its marketplace is `manual`.

Do not delete a plugin only because your pipeline did not create it: a member or an administrator might have added it in claude.ai. Before a script deletes a plugin because your pipeline created it, check that the plugin’s `created_by` is an `api_actor` with the `api_key_id` of one of your pipeline’s keys. With any other value, including `null`, do not assume that your pipeline created the plugin. A delete also removes any versions that other people added to the plugin. Make the same check on each version’s `created_by` and read every page of [List a plugin’s versions](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-a-plugins-versions). Do not delete the plugin automatically if any version fails the check, including one whose `created_by` is `null`.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins delete --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_plugin = client.beta.organization.plugins.delete(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  )

  print(f"id: {deleted_plugin.id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedPlugin = await client.beta.organization.plugins.delete(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  );

  console.log(`id: ${deletedPlugin.id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedPlugin = await client.Beta.Organization.Plugins.Delete(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  );

  Console.WriteLine($"id: {deletedPlugin.ID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedPlugin, err := client.Beta.Organization.Plugins.Delete(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginDeleteParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", deletedPlugin.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedPlugin = client.beta().organization().plugins()
      .delete("plugin_01Hq3vX8kZcN2mB7pR4tY9wL");

  IO.println("id: " + deletedPlugin.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedPlugin = $client->beta->organization->plugins->delete(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
  );

  echo "id: {$deletedPlugin->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  deleted_plugin = client.beta.organization.plugins.delete(plugin_id)

  puts "id: #{deleted_plugin.id}"
  ```
</CodeGroup>

```json
{ "type": "plugin_deleted", "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
```

## Plugin versions

A plugin version is an immutable snapshot of a plugin’s files from one upload (the [Create a version](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-version) response shows a complete object). Its fields mirror the plugin’s served-version fields (`display_name`, `description`, `manifest_version`, `content_scan`, `components`, `reach`) for this version, plus `release_notes` (as supplied with the upload and shown in claude.ai’s version history) and `created_by` (who uploaded it).

A `{version}` that lacks the `pluginver_` prefix returns `400` (except the literal `latest` where noted). One that carries the prefix but does not identify a version of that plugin returns `404`.

### List a plugin’s versions

`GET /v1/organizations/plugins/{plugin_id}/versions` lists a plugin’s versions, ordered by `created_at` descending; the first item is the version `latest_version_id` identifies. `limit` is 1 to 1,000. Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/versions?limit=50" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins:versions list \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --limit 50
  ```

  ```python Python
  client = anthropic.Anthropic()

  versions = client.beta.organization.plugins.versions.list(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL", limit=50
  )

  # Automatically fetches more pages as needed.
  for version in versions:
      print(f"{version.id}: {version.manifest_version}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const versions = await client.beta.organization.plugins.versions.list(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
    { limit: 50 }
  );

  for await (const version of versions) {
    console.log(`${version.id}: ${version.manifest_version}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Plugins.Versions.List(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      new() { Limit = 50 }
  );

  await foreach (var version in page.Paginate())
  {
      Console.WriteLine($"{version.ID}: {version.ManifestVersion}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  versions := client.Beta.Organization.Plugins.Versions.ListAutoPaging(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginVersionListParams{
  		Limit: anthropic.Int(50),
  	},
  )

  for versions.Next() {
  	version := versions.Current()
  	fmt.Printf("%s: %s\n", version.ID, version.ManifestVersion)
  }
  if err := versions.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.versions.VersionListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = VersionListParams.builder()
          .limit(50)
          .build();
      var versions = client.beta().organization().plugins().versions()
          .list("plugin_01Hq3vX8kZcN2mB7pR4tY9wL", params);

      for (var version : versions.autoPager()) {
          IO.println(version.id() + ": " + version.manifestVersion().orElse(null));
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $versions = $client->beta->organization->plugins->versions->list(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
      limit: 50,
  );

  // Only this page; for the next, call list() again with page: $versions->nextPage.
  foreach ($versions->getItems() as $version) {
      echo "{$version->id}: {$version->manifestVersion}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  page = client.beta.organization.plugins.versions.list(plugin_id, limit: 50)

  page.auto_paging_each do |version|
    puts "#{version.id}: #{version.manifest_version}"
  end
  ```
</CodeGroup>

### Create a version

`POST /v1/organizations/plugins/{plugin_id}/versions` adds a version to an organization-owned plugin in a `manual` marketplace. The body is `multipart/form-data`, with the same `files[]` and `release_notes` fields, [upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements), and file, manifest, archive, and size errors as [Create a plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-plugin). The uploaded name (the manifest’s `name`) must equal the plugin’s `name`. If the plugin is not pinned, the new version is normally served as soon as it is stored. In that case, when content scanning is on, members lose the plugin until that version’s `content_scan` reads `completed` with `pass` or `warn` (see [Content scanning](https://platform.claude.com/docs/en/manage-claude/plugins-api#content-scanning)). If the plugin is pinned, the version is stored but not served until someone chooses it (see [Change the served version](https://platform.claude.com/docs/en/manage-claude/plugins-api#change-the-served-version)). To check, compare the response’s `id` with the plugin’s `served_version_id`. Returns the version. Requires the `write:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/versions" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -F "files[]=@dist/sales-toolkit.zip" \
    -F "release_notes=Adds the call-prep command."
  ```

  ```bash CLI
  ant beta:organization:plugins:versions create \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --file dist/sales-toolkit.zip \
    --release-notes "Adds the call-prep command."
  ```

  ```python Python
  client = anthropic.Anthropic()

  with open("dist/sales-toolkit.zip", "rb") as archive:
      version = client.beta.organization.plugins.versions.create(
          "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
          files=[archive],
          release_notes="Adds the call-prep command.",
      )

  print(f"id: {version.id}")
  print(f"manifest_version: {version.manifest_version}")
  ```

  ```typescript TypeScript
  import fs from "node:fs";

  const client = new Anthropic();

  const version = await client.beta.organization.plugins.versions.create(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
    {
      files: [fs.createReadStream("dist/sales-toolkit.zip")],
      release_notes: "Adds the call-prep command."
    }
  );

  console.log(`id: ${version.id}`);
  console.log(`manifest_version: ${version.manifest_version}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var version = await client.Beta.Organization.Plugins.Versions.Create(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      new()
      {
          Files = [File.OpenRead("dist/sales-toolkit.zip")],
          ReleaseNotes = "Adds the call-prep command.",
      }
  );

  Console.WriteLine($"id: {version.ID}");
  Console.WriteLine($"manifest_version: {version.ManifestVersion}");
  ```

  ```go Go
  client := anthropic.NewClient()

  archive, err := os.Open("dist/sales-toolkit.zip")
  if err != nil {
  	log.Fatal(err)
  }
  defer archive.Close()

  version, err := client.Beta.Organization.Plugins.Versions.New(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginVersionNewParams{
  		Files:        []io.Reader{archive},
  		ReleaseNotes: anthropic.String("Adds the call-prep command."),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", version.ID)
  fmt.Printf("manifest_version: %s\n", version.ManifestVersion)
  ```

  ```java Java
  import com.anthropic.core.MultipartField;
  import com.anthropic.models.beta.organization.plugins.versions.VersionCreateParams;

  void main() throws Exception {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      // Build the `files[]` part by hand so the archive is sent with its file name,
      // which the upload requires.
      var archive = MultipartField.<List<InputStream>>builder()
          .value(List.of(Files.newInputStream(Path.of("dist/sales-toolkit.zip"))))
          .filename("sales-toolkit.zip")
          .contentType("application/octet-stream")
          .build();
      var params = VersionCreateParams.builder()
          .files(archive)
          .releaseNotes("Adds the call-prep command.")
          .build();
      var version = client.beta().organization().plugins().versions()
          .create("plugin_01Hq3vX8kZcN2mB7pR4tY9wL", params);

      IO.println("id: " + version.id());
      IO.println("manifest_version: " + version.manifestVersion().orElse(null));
  }
  ```

  ```php PHP
  use Anthropic\Core\FileParam;

  $client = new Client();

  $version = $client->beta->organization->plugins->versions->create(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
      files: [
          FileParam::fromResource(fopen('dist/sales-toolkit.zip', 'r')),
      ],
      releaseNotes: 'Adds the call-prep command.',
  );

  echo "id: {$version->id}\n";
  echo "manifest_version: {$version->manifestVersion}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  version = client.beta.organization.plugins.versions.create(
    plugin_id,
    files: [Pathname("dist/sales-toolkit.zip")],
    release_notes: "Adds the call-prep command."
  )

  puts "id: #{version.id}"
  puts "manifest_version: #{version.manifest_version}"
  ```
</CodeGroup>

```json
{
  "type": "plugin_version",
  "id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "manifest_version": "1.5.0",
  "release_notes": "Adds the call-prep command.",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "content_scan": { "status": "processing", "assessment": null, "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null },
    {
      "type": "command",
      "name": "call-prep",
      "description": "Builds a one-page brief for an upcoming call."
    }
  ],
  "reach": "remote",
  "created_at": "2026-09-15T14:12:30Z"
}
```

Besides a `400` for an upload that breaks the [upload requirements](https://platform.claude.com/docs/en/manage-claude/plugins-api#upload-requirements) (`413` for a request body over 200 MB) and the shared responses (a `403` for a member-owned plugin; see [Error responses](https://platform.claude.com/docs/en/manage-claude/plugins-api#error-responses)), the request can fail with:

| Status | Cause | What to do |
| ----- | ----- | ----- |
| 400 | The plugin is in a marketplace synchronized from Git, or the uploaded name differs from the plugin’s. | Change the repository instead, or fix the manifest `name`. |
| 409 (no `error_code`) | Another upload to this plugin, or a served-version change, is still in progress. | Retry shortly. |
| 409 `skill_name_taken` | The plugin is in the library marketplace and the version adds a skill with an organization skill’s name. | Rename the skill, or remove the organization skill in claude.ai. |
| 503 `registration_pending` | The version was stored but its registration did not complete. | Resend the same request when the response carries `x-should-retry: true` (see [Retrying uploads](https://platform.claude.com/docs/en/manage-claude/plugins-api#retrying-uploads)). |

### Get a version

`GET /v1/organizations/plugins/{plugin_id}/versions/{version}` returns one version. `{version}` is a version ID, or `latest` for the version `latest_version_id` identifies at the time of the request. Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/versions/latest" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins:versions retrieve \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --version latest
  ```

  ```python Python
  client = anthropic.Anthropic()

  version = client.beta.organization.plugins.versions.retrieve(
      "latest",
      plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  )

  print(f"id: {version.id}")
  print(f"manifest_version: {version.manifest_version}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const version = await client.beta.organization.plugins.versions.retrieve("latest", {
    plugin_id: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  });

  console.log(`id: ${version.id}`);
  console.log(`manifest_version: ${version.manifest_version}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var version = await client.Beta.Organization.Plugins.Versions.Retrieve(
      "latest",
      new() { PluginID = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
  );

  Console.WriteLine($"id: {version.ID}");
  Console.WriteLine($"manifest_version: {version.ManifestVersion}");
  ```

  ```go Go
  client := anthropic.NewClient()

  version, err := client.Beta.Organization.Plugins.Versions.Get(
  	context.Background(),
  	"latest",
  	anthropic.BetaOrganizationPluginVersionGetParams{
  		PluginID: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", version.ID)
  fmt.Printf("manifest_version: %s\n", version.ManifestVersion)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.versions.VersionRetrieveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = VersionRetrieveParams.builder()
          .pluginId("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")
          .build();
      var version = client.beta().organization().plugins().versions()
          .retrieve("latest", params);

      IO.println("id: " + version.id());
      IO.println("manifest_version: " + version.manifestVersion().orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $version = $client->beta->organization->plugins->versions->retrieve(
      version: 'latest',
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
  );

  echo "id: {$version->id}\n";
  echo "manifest_version: {$version->manifestVersion}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  version = client.beta.organization.plugins.versions.retrieve("latest", plugin_id: plugin_id)

  puts "id: #{version.id}"
  puts "manifest_version: #{version.manifest_version}"
  ```
</CodeGroup>

### Download a version’s files

`GET /v1/organizations/plugins/{plugin_id}/versions/{version}/content` downloads a version’s files as the stored `.zip` archive (`Content-Type: application/zip`). The archive is returned whatever its content-scan result, so you can inspect versions withheld from members. It is served exactly as stored, so for an organization-owned plugin in a `manual` marketplace you can re-upload it unchanged as a new version, provided it meets the current upload requirements. `{version}` must be a version ID, not `latest`: read the plugin’s `served_version_id` or `latest_version_id` first, or resolve `latest` with `GET /v1/organizations/plugins/{plugin_id}/versions/latest`. The `Content-Disposition` file name is derived from the plugin’s name and is not unique; name saved files by plugin and version ID. Requires the `read:plugins` scope.

Downloading a **member-owned** plugin’s archive records a `claude_plugin_archive_accessed` event on the Compliance API Activity Feed, identifying the key (as `api_actor`), the plugin and its marketplace, the version, and the owning member by ID; it carries no names. Downloading an organization-owned plugin’s archive records nothing.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/versions/pluginver_01Km7tL4pR9xF5sU2zV3jP6q/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -o plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip
  ```

  ```bash CLI
  ant beta:organization:plugins:versions download \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --version pluginver_01Km7tL4pR9xF5sU2zV3jP6q \
    --output plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip
  ```

  ```python Python
  client = anthropic.Anthropic()

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  version_id = "pluginver_01Km7tL4pR9xF5sU2zV3jP6q"

  with client.beta.organization.plugins.versions.with_streaming_response.download(
      version_id,
      plugin_id=plugin_id,
  ) as response:
      response.stream_to_file(f"{plugin_id}_{version_id}.zip")
  ```

  ```typescript TypeScript
  import { writeFile } from "node:fs/promises";

  const client = new Anthropic();

  const pluginId = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL";
  const versionId = "pluginver_01Km7tL4pR9xF5sU2zV3jP6q";

  const response = await client.beta.organization.plugins.versions.download(versionId, {
    plugin_id: pluginId
  });
  if (!response.body) {
    throw new Error("The download returned no body");
  }

  await writeFile(`${pluginId}_${versionId}.zip`, response.body);
  ```

  ```csharp C#
  AnthropicClient client = new();

  using var response = await client.Beta.Organization.Plugins.Versions.Download(
      "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
      new() { PluginID = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
  );

  using var content = await response.ReadAsStream();
  using var file = File.Create(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip"
  );
  await content.CopyToAsync(file);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Beta.Organization.Plugins.Versions.Download(
  	context.Background(),
  	"pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
  	anthropic.BetaOrganizationPluginVersionDownloadParams{
  		PluginID: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }
  defer response.Body.Close()

  out, err := os.Create("plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip")
  if err != nil {
  	log.Fatal(err)
  }
  defer out.Close()

  if _, err := io.Copy(out, response.Body); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.core.http.HttpResponse;
  import com.anthropic.models.beta.organization.plugins.versions.VersionDownloadParams;

  void main() throws Exception {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = VersionDownloadParams.builder()
          .pluginId("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")
          .build();
      try (HttpResponse response = client.beta().organization().plugins().versions()
              .download("pluginver_01Km7tL4pR9xF5sU2zV3jP6q", params)) {
          Files.copy(
              response.body(),
              Path.of("plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip"),
              StandardCopyOption.REPLACE_EXISTING);
      }
  }
  ```

  ```php PHP
  $client = new Client();

  // download() would return the whole archive as one string, so take the raw
  // response and copy its body to disk in chunks.
  $response = $client->beta->organization->plugins->versions->raw->download(
      version: 'pluginver_01Km7tL4pR9xF5sU2zV3jP6q',
      params: ['pluginID' => 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL'],
  );

  $archive = $response->getBody();
  $file = fopen('plugin_01Hq3vX8kZcN2mB7pR4tY9wL_pluginver_01Km7tL4pR9xF5sU2zV3jP6q.zip', 'wb');
  while (!$archive->eof()) {
      fwrite($file, $archive->read(1024 * 1024));
  }
  fclose($file);
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  version_id = "pluginver_01Km7tL4pR9xF5sU2zV3jP6q"
  archive = client.beta.organization.plugins.versions.download(version_id, plugin_id: plugin_id)

  # The SDK returns the archive already read into memory, as a StringIO.
  File.binwrite("#{plugin_id}_#{version_id}.zip", archive.string)
  ```
</CodeGroup>

## Plugin installation settings

These endpoints apply to organization-owned plugins. They return `404` for a member-owned plugin, which has shares instead (see [Plugin shares](https://platform.claude.com/docs/en/manage-claude/plugins-api#plugin-shares)). `{target}` is the literal `organization` for the plugin’s organization-wide setting, or a group’s `rbac_group_` ID for that group’s setting; any other value returns `400`. Group IDs come from `GET /v1/organizations/rbac_groups` (scope `read:rbac_groups`; see [Groups in User management](https://platform.claude.com/docs/en/manage-claude/user-management#groups)). A setting has no `id` of its own: it is addressed by `(plugin_id, target)`, and no actor is recorded on it (the actor is on its `plugin_installation_preference_updated` activity event).

### List a plugin’s installation settings

`GET /v1/organizations/plugins/{plugin_id}/installation_settings` lists the settings an organization-owned plugin holds, ordered by `created_at` descending: its own organization-wide setting (absent while it inherits its marketplace’s default) and each group’s setting. Filter by `target_type` (`organization` or `rbac_group`). Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/installation_settings" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins:installation-settings list \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL
  ```

  ```python Python
  client = anthropic.Anthropic()

  settings = client.beta.organization.plugins.installation_settings.list(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  )

  # Automatically fetches more pages as needed.
  for setting in settings:
      print(f"{setting.plugin_id}: {setting.installation_preference}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const settings = await client.beta.organization.plugins.installationSettings.list(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  );

  for await (const setting of settings) {
    console.log(`${setting.plugin_id}: ${setting.installation_preference}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Plugins.InstallationSettings.List(
      "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  );

  await foreach (var setting in page.Paginate())
  {
      Console.WriteLine($"{setting.PluginID}: {setting.InstallationPreference.Raw()}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  settings := client.Beta.Organization.Plugins.InstallationSettings.ListAutoPaging(
  	context.Background(),
  	"plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	anthropic.BetaOrganizationPluginInstallationSettingListParams{},
  )

  for settings.Next() {
  	setting := settings.Current()
  	fmt.Printf("%s: %s\n", setting.PluginID, setting.InstallationPreference)
  }
  if err := settings.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var settings = client.beta().organization().plugins().installationSettings()
      .list("plugin_01Hq3vX8kZcN2mB7pR4tY9wL");

  for (var setting : settings.autoPager()) {
      IO.println(setting.pluginId() + ": " + setting.installationPreference().asString());
  }
  ```

  ```php PHP
  $client = new Client();

  $settings = $client->beta->organization->plugins->installationSettings->list(
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
  );

  // Only this page; for the next, call list() again with page: $settings->nextPage.
  foreach ($settings->getItems() as $setting) {
      echo "{$setting->pluginID}: {$setting->installationPreference}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  page = client.beta.organization.plugins.installation_settings.list(plugin_id)

  page.auto_paging_each do |setting|
    puts "#{setting.plugin_id}: #{setting.installation_preference}"
  end
  ```
</CodeGroup>

### Set an installation setting

`POST /v1/organizations/plugins/{plugin_id}/installation_settings/{target}` sets one target’s installation setting for an organization-owned plugin, creating it or changing the value it already holds. The body’s only field is `installation_preference` (`required`, `auto_install`, `available`, or `not_available`), and it is required. Setting the value the target already holds changes nothing. Setting the `organization` target stops the plugin inheriting its marketplace’s default (`organization_installation_preference_inherited` becomes `false`), even when the value is the same as the default, so the plugin no longer follows later changes to the marketplace default. To return the plugin to its marketplace’s default, [remove the organization-wide setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#remove-an-installation-setting); group settings are unaffected. A group target must be a group your organization can see in `GET /v1/organizations/rbac_groups`, or the request returns `404`. The change does not alter the plugin’s `updated_at`; it is recorded on the Activity Feed. Returns the setting. Requires the `write:plugins` scope.

Send a plugin’s installation-setting writes one at a time. If several writes for the same plugin arrive at the same time, the server handles them one after another and can answer some of them with `503` instead of applying them. That `503` carries `x-should-retry: true`, and the write is safe to repeat: wait a second or two, then send it again.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/installation_settings/rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -d '{"installation_preference": "available"}'
  ```

  ```bash CLI
  ant beta:organization:plugins:installation-settings set \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --target rbac_group_01F3xQqQzXyWvUtSrQpOnMlK \
    --installation-preference available
  ```

  ```python Python
  client = anthropic.Anthropic()

  setting = client.beta.organization.plugins.installation_settings.set(
      "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
      plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      installation_preference="available",
  )

  print(f"plugin_id: {setting.plugin_id}")
  print(f"installation_preference: {setting.installation_preference}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const setting = await client.beta.organization.plugins.installationSettings.set(
    "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
    {
      plugin_id: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      installation_preference: "available"
    }
  );

  console.log(`plugin_id: ${setting.plugin_id}`);
  console.log(`installation_preference: ${setting.installation_preference}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Plugins.InstallationSettings;

  AnthropicClient client = new();

  var setting = await client.Beta.Organization.Plugins.InstallationSettings.Set(
      "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
      new()
      {
          PluginID = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
          InstallationPreference = InstallationPreference.Available,
      }
  );

  Console.WriteLine($"plugin_id: {setting.PluginID}");
  Console.WriteLine($"installation_preference: {setting.InstallationPreference.Raw()}");
  ```

  ```go Go
  client := anthropic.NewClient()

  setting, err := client.Beta.Organization.Plugins.InstallationSettings.Set(
  	context.Background(),
  	"rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
  	anthropic.BetaOrganizationPluginInstallationSettingSetParams{
  		PluginID:               "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  		InstallationPreference: anthropic.BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceAvailable,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("plugin_id: %s\n", setting.PluginID)
  fmt.Printf("installation_preference: %s\n", setting.InstallationPreference)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.installationsettings.InstallationSettingSetParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InstallationSettingSetParams.builder()
          .pluginId("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")
          .installationPreference(InstallationSettingSetParams.InstallationPreference.AVAILABLE)
          .build();
      var setting = client.beta().organization().plugins().installationSettings()
          .set("rbac_group_01F3xQqQzXyWvUtSrQpOnMlK", params);

      IO.println("plugin_id: " + setting.pluginId());
      IO.println("installation_preference: " + setting.installationPreference().asString());
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\Plugins\InstallationSettings\InstallationSettingSetParams\InstallationPreference;
  // ...

  $client = new Client();

  $setting = $client->beta->organization->plugins->installationSettings->set(
      target: 'rbac_group_01F3xQqQzXyWvUtSrQpOnMlK',
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
      installationPreference: InstallationPreference::AVAILABLE,
  );

  echo "plugin_id: {$setting->pluginID}\n";
  echo "installation_preference: {$setting->installationPreference}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  group_id = "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK"
  setting = client.beta.organization.plugins.installation_settings.set(
    group_id,
    plugin_id: plugin_id,
    installation_preference: :available
  )

  puts "plugin_id: #{setting.plugin_id}"
  puts "installation_preference: #{setting.installation_preference}"
  ```
</CodeGroup>

```json
{
  "type": "plugin_installation_setting",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "target": { "type": "rbac_group", "rbac_group_id": "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" },
  "installation_preference": "available",
  "created_at": "2026-09-02T10:00:00Z",
  "updated_at": "2026-09-02T10:00:00Z"
}
```

### Remove an installation setting

`DELETE /v1/organizations/plugins/{plugin_id}/installation_settings/{target}` removes one target’s installation setting for an organization-owned plugin. With `{target}` of `organization` it removes the plugin’s own organization-wide setting. The plugin then inherits its marketplace’s default again (`organization_installation_preference_inherited` becomes `true`) and follows later changes to that default; group settings are unaffected. With a group’s `rbac_group_` ID it removes that group’s setting: the group’s members fall back to the organization-wide value, or to another of their groups’ settings. A target that holds no setting of its own returns `404`; that includes the `organization` target of a plugin that already inherits its marketplace’s default. The change does not alter the plugin’s `updated_at`; it is recorded on the Activity Feed. The response carries the composite key in place of an `id`; for the `organization` target its `target` is `{"type": "organization"}`. Requires the `write:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/plugins/plugin_01Hq3vX8kZcN2mB7pR4tY9wL/installation_settings/rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins:installation-settings remove \
    --plugin-id plugin_01Hq3vX8kZcN2mB7pR4tY9wL \
    --target rbac_group_01F3xQqQzXyWvUtSrQpOnMlK
  ```

  ```python Python
  client = anthropic.Anthropic()

  removed_setting = client.beta.organization.plugins.installation_settings.remove(
      "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
      plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  )

  print(f"plugin_id: {removed_setting.plugin_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const removedSetting = await client.beta.organization.plugins.installationSettings.remove(
    "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
    { plugin_id: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
  );

  console.log(`plugin_id: ${removedSetting.plugin_id}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var removedSetting = await client.Beta.Organization.Plugins.InstallationSettings.Remove(
      "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
      new() { PluginID = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
  );

  Console.WriteLine($"plugin_id: {removedSetting.PluginID}");
  ```

  ```go Go
  client := anthropic.NewClient()

  removedSetting, err := client.Beta.Organization.Plugins.InstallationSettings.Remove(
  	context.Background(),
  	"rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
  	anthropic.BetaOrganizationPluginInstallationSettingRemoveParams{
  		PluginID: "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("plugin_id: %s\n", removedSetting.PluginID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.plugins.installationsettings.InstallationSettingRemoveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = InstallationSettingRemoveParams.builder()
          .pluginId("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")
          .build();
      var removedSetting = client.beta().organization().plugins().installationSettings()
          .remove("rbac_group_01F3xQqQzXyWvUtSrQpOnMlK", params);

      IO.println("plugin_id: " + removedSetting.pluginId());
  }
  ```

  ```php PHP
  $client = new Client();

  $removedSetting = $client->beta->organization->plugins->installationSettings->remove(
      target: 'rbac_group_01F3xQqQzXyWvUtSrQpOnMlK',
      pluginID: 'plugin_01Hq3vX8kZcN2mB7pR4tY9wL',
  );

  echo "plugin_id: {$removedSetting->pluginID}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
  group_id = "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK"
  removed_setting = client.beta.organization.plugins.installation_settings.remove(
    group_id,
    plugin_id: plugin_id
  )

  puts "plugin_id: #{removed_setting.plugin_id}"
  ```
</CodeGroup>

```json
{
  "type": "plugin_installation_setting_deleted",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "target": { "type": "rbac_group", "rbac_group_id": "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" }
}
```

## Plugin shares

Shares exist only on member-owned plugins and are read-only in this API (see [Shares](https://platform.claude.com/docs/en/manage-claude/plugins-api#shares)).

### List a plugin’s shares

`GET /v1/organizations/plugins/{plugin_id}/shares` lists who the owner of a member-owned plugin has shared it with, ordered by `granted_at` descending: every member (`organization`), a group (`rbac_group`), or a named member (`organization_member`). Filter by `target_type`. A plugin its owner has not shared returns an empty list; an organization-owned plugin returns `404`. Shares are read-only on this API, and a listed share gives access only while that kind of sharing is turned on for your organization in claude.ai (see [Shares](https://platform.claude.com/docs/en/manage-claude/plugins-api#shares)). `granted_at` is when the share was given; if the owner later changes the share in claude.ai, it is the time of that change. Requires the `read:plugins` scope.

An empty page is the whole list only if its `next_page` is `null` (see [Pagination](https://platform.claude.com/docs/en/manage-claude/plugins-api#pagination)).

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugins/plugin_01Mr2wP7sU3aJ8vX5cY6nS9t/shares" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugins:shares list \
    --plugin-id plugin_01Mr2wP7sU3aJ8vX5cY6nS9t
  ```

  ```python Python
  client = anthropic.Anthropic()

  shares = client.beta.organization.plugins.shares.list("plugin_01Mr2wP7sU3aJ8vX5cY6nS9t")

  # Automatically fetches more pages as needed.
  for share in shares:
      print(f"plugin_id: {share.plugin_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const shares = await client.beta.organization.plugins.shares.list(
    "plugin_01Mr2wP7sU3aJ8vX5cY6nS9t"
  );

  for await (const share of shares) {
    console.log(`plugin_id: ${share.plugin_id}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Plugins.Shares.List("plugin_01Mr2wP7sU3aJ8vX5cY6nS9t");

  await foreach (var share in page.Paginate())
  {
      Console.WriteLine($"plugin_id: {share.PluginID}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  shares := client.Beta.Organization.Plugins.Shares.ListAutoPaging(
  	context.Background(),
  	"plugin_01Mr2wP7sU3aJ8vX5cY6nS9t",
  	anthropic.BetaOrganizationPluginShareListParams{},
  )

  for shares.Next() {
  	share := shares.Current()
  	fmt.Printf("plugin_id: %s\n", share.PluginID)
  }
  if err := shares.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var shares = client.beta().organization().plugins().shares()
      .list("plugin_01Mr2wP7sU3aJ8vX5cY6nS9t");

  for (var share : shares.autoPager()) {
      IO.println("plugin_id: " + share.pluginId());
  }
  ```

  ```php PHP
  $client = new Client();

  $shares = $client->beta->organization->plugins->shares->list(
      pluginID: 'plugin_01Mr2wP7sU3aJ8vX5cY6nS9t',
  );

  // Only this page; for the next, call list() again with page: $shares->nextPage.
  foreach ($shares->getItems() as $share) {
      echo "plugin_id: {$share->pluginID}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  plugin_id = "plugin_01Mr2wP7sU3aJ8vX5cY6nS9t"
  page = client.beta.organization.plugins.shares.list(plugin_id)

  page.auto_paging_each do |share|
    puts "plugin_id: #{share.plugin_id}"
  end
  ```
</CodeGroup>

```json
{
  "data": [
    {
      "type": "plugin_share",
      "plugin_id": "plugin_01Mr2wP7sU3aJ8vX5cY6nS9t",
      "target": { "type": "organization_member", "user_id": "user_01WCz9BvGLdMYRUMmcAxMWvW" },
      "granted_at": "2026-08-20T15:12:00Z"
    }
  ],
  "next_page": null
}
```

## Plugin marketplaces

This API reads [marketplaces](https://platform.claude.com/docs/en/manage-claude/plugins-api#marketplaces) and sets an organization marketplace’s default installation setting; marketplaces themselves are created, connected to a repository, and deleted in claude.ai.

```json
{
  "type": "plugin_marketplace",
  "id": "marketplace_01VbNcMxZaSdFgHjKlQwErTy",
  "name": "engineering-tools",
  "owner": { "type": "organization" },
  "source": "github",
  "sync_status": "success",
  "last_sync_ended_at": "2026-09-10T22:15:03Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "default_installation_preference": "available",
  "created_at": "2026-06-12T08:45:00Z"
}
```

| Field | Description |
| ----- | ----- |
| `name` | The marketplace’s name. Fixed for its lifetime. |
| `owner` | Same shape as on the plugin. |
| `source` | `manual`, `github`, `gitlab`, or `public_git`. See [Marketplaces](https://platform.claude.com/docs/en/manage-claude/plugins-api#marketplaces). |
| `sync_status` | Outcome of the most recent synchronization: `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, or `failed_limits`. `null` until a synchronization is first attempted, which never occurs for a marketplace whose source is `manual`. |
| `last_sync_ended_at` | When the most recent synchronization attempt finished, whatever its outcome; for a connected repository that has not synchronized yet, when the marketplace was created. `null` for a marketplace that is not synchronized. |
| `last_sync_read_sha` | The commit the last synchronization read from the repository. Not necessarily the commit the served versions came from. `null` for a marketplace that is not synchronized. |
| `default_installation_preference` | Organization marketplaces: the organization-wide value for every plugin in it without its own setting (`not_available` if never set). Personal marketplaces: `null`. |

A `marketplace_id` that lacks the `marketplace_` prefix returns `400`. One that carries the prefix but does not resolve, or belongs to another organization, returns `404`.

### List marketplaces

`GET /v1/organizations/plugin_marketplaces` lists your organization’s marketplaces and members’ personal marketplaces, ordered by `created_at` descending. Use it to find a marketplace’s ID, to filter the plugin list by it or to upload into it, before it holds any plugin. The library marketplace appears once something has first been created in it, in claude.ai or through this API. Filter by `owner_type` (`organization` or `user`) and `source`. `limit` is 1 to 1,000. Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugin_marketplaces?owner_type=organization" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugin-marketplaces list --owner-type organization
  ```

  ```python Python
  client = anthropic.Anthropic()

  marketplaces = client.beta.organization.plugin_marketplaces.list(
      owner_type="organization"
  )

  # Automatically fetches more pages as needed.
  for marketplace in marketplaces:
      print(f"{marketplace.id}: {marketplace.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const marketplaces = await client.beta.organization.pluginMarketplaces.list({
    owner_type: "organization"
  });

  for await (const marketplace of marketplaces) {
    console.log(`${marketplace.id}: ${marketplace.name}`);
  }
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.PluginMarketplaces;

  AnthropicClient client = new();

  var page = await client.Beta.Organization.PluginMarketplaces.List(
      new() { OwnerType = OwnerType.Organization }
  );

  await foreach (var marketplace in page.Paginate())
  {
      Console.WriteLine($"{marketplace.ID}: {marketplace.Name}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  marketplaces := client.Beta.Organization.PluginMarketplaces.ListAutoPaging(
  	context.Background(),
  	anthropic.BetaOrganizationPluginMarketplaceListParams{
  		OwnerType: anthropic.BetaOrganizationPluginMarketplaceListParamsOwnerTypeOrganization,
  	},
  )

  for marketplaces.Next() {
  	marketplace := marketplaces.Current()
  	fmt.Printf("%s: %s\n", marketplace.ID, marketplace.Name)
  }
  if err := marketplaces.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.pluginmarketplaces.PluginMarketplaceListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginMarketplaceListParams.builder()
          .ownerType(PluginMarketplaceListParams.OwnerType.ORGANIZATION)
          .build();
      var marketplaces = client.beta().organization().pluginMarketplaces().list(params);

      for (var marketplace : marketplaces.autoPager()) {
          IO.println(marketplace.id() + ": " + marketplace.name());
      }
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\PluginMarketplaces\PluginMarketplaceListParams\OwnerType;
  // ...

  $client = new Client();

  $marketplaces = $client->beta->organization->pluginMarketplaces->list(
      ownerType: OwnerType::ORGANIZATION,
  );

  // Only this page; for the next, call list() again with page: $marketplaces->nextPage.
  foreach ($marketplaces->getItems() as $marketplace) {
      echo "{$marketplace->id}: {$marketplace->name}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.plugin_marketplaces.list(owner_type: :organization)

  page.auto_paging_each do |marketplace|
    puts "#{marketplace.id}: #{marketplace.name}"
  end
  ```
</CodeGroup>

### Get a marketplace

`GET /v1/organizations/plugin_marketplaces/{marketplace_id}` returns one marketplace. Requires the `read:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/plugin_marketplaces/marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01"
  ```

  ```bash CLI
  ant beta:organization:plugin-marketplaces retrieve \
    --marketplace-id marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r
  ```

  ```python Python
  client = anthropic.Anthropic()

  marketplace = client.beta.organization.plugin_marketplaces.retrieve(
      "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  )

  print(f"id: {marketplace.id}")
  print(f"name: {marketplace.name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const marketplace = await client.beta.organization.pluginMarketplaces.retrieve(
    "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  );

  console.log(`id: ${marketplace.id}`);
  console.log(`name: ${marketplace.name}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var marketplace = await client.Beta.Organization.PluginMarketplaces.Retrieve(
      "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  );

  Console.WriteLine($"id: {marketplace.ID}");
  Console.WriteLine($"name: {marketplace.Name}");
  ```

  ```go Go
  client := anthropic.NewClient()

  marketplace, err := client.Beta.Organization.PluginMarketplaces.Get(
  	context.Background(),
  	"marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  	anthropic.BetaOrganizationPluginMarketplaceGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", marketplace.ID)
  fmt.Printf("name: %s\n", marketplace.Name)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var marketplace = client.beta().organization().pluginMarketplaces()
      .retrieve("marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r");

  IO.println("id: " + marketplace.id());
  IO.println("name: " + marketplace.name());
  ```

  ```php PHP
  $client = new Client();

  $marketplace = $client->beta->organization->pluginMarketplaces->retrieve(
      marketplaceID: 'marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r',
  );

  echo "id: {$marketplace->id}\n";
  echo "name: {$marketplace->name}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  marketplace_id = "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  marketplace = client.beta.organization.plugin_marketplaces.retrieve(marketplace_id)

  puts "id: #{marketplace.id}"
  puts "name: #{marketplace.name}"
  ```
</CodeGroup>

### Set a marketplace’s default installation setting

`POST /v1/organizations/plugin_marketplaces/{marketplace_id}` sets the default installation setting of an organization-owned marketplace. Every plugin in the marketplace without its own organization-wide setting reports this default as its `organization_installation_preference`, including plugins added later. It works for `manual` and synchronized marketplaces; a member’s personal marketplace returns `403`. The only updatable field is `default_installation_preference`, and it is required. It cannot be set back to `null`: once a marketplace has a default, it keeps one, as in claude.ai. A change is recorded as one `marketplace_updated` event with no per-plugin events, and does not alter any plugin’s `updated_at`. Setting the value already set changes nothing, with one exception: a marketplace whose default was never set reports `not_available` but holds no setting, so its first write (even `not_available`) counts as a change. Returns the marketplace. Requires the `write:plugins` scope.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugin_marketplaces/marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -d '{"default_installation_preference": "available"}'
  ```

  ```bash CLI
  ant beta:organization:plugin-marketplaces update \
    --marketplace-id marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r \
    --default-installation-preference available
  ```

  ```python Python
  client = anthropic.Anthropic()

  marketplace = client.beta.organization.plugin_marketplaces.update(
      "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      default_installation_preference="available",
  )

  print(f"id: {marketplace.id}")
  print(f"default_installation_preference: {marketplace.default_installation_preference}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const marketplace = await client.beta.organization.pluginMarketplaces.update(
    "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
    { default_installation_preference: "available" }
  );

  console.log(`id: ${marketplace.id}`);
  console.log(`default_installation_preference: ${marketplace.default_installation_preference}`);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.PluginMarketplaces;

  AnthropicClient client = new();

  var marketplace = await client.Beta.Organization.PluginMarketplaces.Update(
      "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      new() { DefaultInstallationPreference = DefaultInstallationPreference.Available }
  );

  Console.WriteLine($"id: {marketplace.ID}");
  Console.WriteLine(
      $"default_installation_preference: {marketplace.DefaultInstallationPreference?.Raw()}"
  );
  ```

  ```go Go
  client := anthropic.NewClient()

  marketplace, err := client.Beta.Organization.PluginMarketplaces.Update(
  	context.Background(),
  	"marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  	anthropic.BetaOrganizationPluginMarketplaceUpdateParams{
  		DefaultInstallationPreference: anthropic.BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceAvailable,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("id: %s\n", marketplace.ID)
  fmt.Printf("default_installation_preference: %s\n", marketplace.DefaultInstallationPreference)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.pluginmarketplaces.PluginMarketplaceUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginMarketplaceUpdateParams.builder()
          .defaultInstallationPreference(PluginMarketplaceUpdateParams.DefaultInstallationPreference.AVAILABLE)
          .build();
      var marketplace = client.beta().organization().pluginMarketplaces()
          .update("marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r", params);

      IO.println("id: " + marketplace.id());
      IO.println("default_installation_preference: "
          + marketplace.defaultInstallationPreference().map(preference -> preference.asString()).orElse(null));
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\PluginMarketplaces\PluginMarketplaceUpdateParams\DefaultInstallationPreference;
  // ...

  $client = new Client();

  $marketplace = $client->beta->organization->pluginMarketplaces->update(
      marketplaceID: 'marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r',
      defaultInstallationPreference: DefaultInstallationPreference::AVAILABLE,
  );

  echo "id: {$marketplace->id}\n";
  echo "default_installation_preference: {$marketplace->defaultInstallationPreference}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  marketplace_id = "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
  marketplace = client.beta.organization.plugin_marketplaces.update(
    marketplace_id,
    default_installation_preference: :available
  )

  puts "id: #{marketplace.id}"
  puts "default_installation_preference: #{marketplace.default_installation_preference}"
  ```
</CodeGroup>

### Validate marketplace content

Two endpoints report what a synchronization of the given marketplace content would do, without connecting or storing anything: `POST /v1/organizations/plugin_marketplaces/validate_repository` reads a public GitHub repository, and `POST /v1/organizations/plugin_marketplaces/validate_archive` reads a `.zip` of the marketplace directory that you upload. Both return the same report: whether `marketplace.json` is well-formed, which plugins would be skipped and why, and which plugins would synchronize with some contents left out. The checks are the ones a real synchronization runs. Problems with the content come back in the report, not as HTTP errors: the request succeeds with `valid: false`, even when the repository or archive cannot be read at all. A validation counts as a read, and the two endpoints together are additionally limited to 10 validations a minute for each organization (see [Rate limiting](https://platform.claude.com/docs/en/manage-claude/plugins-api#rate-limiting)); they record nothing on the Activity Feed. A validation can take up to 120 seconds before it returns, so set your client’s timeout above that. Both endpoints require the `read:plugins` or `write:plugins` scope (`read:org_audit` and `read:compliance_org_data` do not grant them).

Validation reads the repository anonymously. It does the same for any plugin source that is on GitHub but outside the repository. As a result, validation reports a private repository or a private plugin source as not found or as needing a GitHub sign-in. When validation reports that a GitHub sign-in is needed, the report code is `marketplace_repo_sign_in_required`.

Validation does not fetch plugin sources on hosts other than GitHub. A plugin with such a source normally gets a `marketplace_validate_source_not_checked` warning and is checked when the marketplace actually synchronizes.

Validation applies stricter rules to a marketplace that Anthropic synchronizes into every organization. `validate_repository` applies them when the repository is such a marketplace. `validate_archive` applies them when the archive names such a marketplace. The stricter rules are as follows:

* Every plugin source outside the marketplace must be pinned to a full commit SHA.
* Validation reports unpinned sources and sources on unsupported hosts as plugin errors.
* For `validate_repository`, the branch that validation reads defaults to the branch that the marketplace synchronizes from.

`validate_repository` takes a JSON body with two fields: `repository_url`, the `https://` URL of a public repository on github.com (required), and `ref`, a branch name or a full 40-character commit SHA (optional). When `ref` is omitted or `null`, it defaults to the branch a synchronization would read, usually the repository’s default branch. `validate_archive` takes `multipart/form-data` with exactly one part, `archive`, sent as a file part with a file name. The file is a `.zip` of the marketplace directory, at most 32 MB, that uses DEFLATE or STORE compression only. The archive’s contents sit at the root or are wrapped in one folder (as a Git host’s download produces). No other form field is accepted.

Validate a public repository at a branch:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugin_marketplaces/validate_repository" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -d '{"repository_url": "https://github.com/example-org/claude-plugins", "ref": "release-candidate"}'
  ```

  ```bash CLI
  ant beta:organization:plugin-marketplaces validate-repository \
    --repository-url https://github.com/example-org/claude-plugins \
    --ref release-candidate
  ```

  ```python Python
  client = anthropic.Anthropic()

  report = client.beta.organization.plugin_marketplaces.validate_repository(
      repository_url="https://github.com/example-org/claude-plugins",
      ref="release-candidate",
  )

  print(f"valid: {str(report.valid).lower()}")
  print(f"total_plugin_count: {report.total_plugin_count}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const report = await client.beta.organization.pluginMarketplaces.validateRepository({
    repository_url: "https://github.com/example-org/claude-plugins",
    ref: "release-candidate"
  });

  console.log(`valid: ${report.valid}`);
  console.log(`total_plugin_count: ${report.total_plugin_count}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var report = await client.Beta.Organization.PluginMarketplaces.ValidateRepository(
      new()
      {
          RepositoryUrl = "https://github.com/example-org/claude-plugins",
          Ref = "release-candidate",
      }
  );

  Console.WriteLine($"valid: {report.Valid.ToString().ToLowerInvariant()}");
  Console.WriteLine($"total_plugin_count: {report.TotalPluginCount}");
  ```

  ```go Go
  client := anthropic.NewClient()

  report, err := client.Beta.Organization.PluginMarketplaces.ValidateRepository(
  	context.Background(),
  	anthropic.BetaOrganizationPluginMarketplaceValidateRepositoryParams{
  		RepositoryURL: "https://github.com/example-org/claude-plugins",
  		Ref:           anthropic.String("release-candidate"),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("valid: %t\n", report.Valid)
  fmt.Printf("total_plugin_count: %d\n", report.TotalPluginCount)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.pluginmarketplaces.PluginMarketplaceValidateRepositoryParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = PluginMarketplaceValidateRepositoryParams.builder()
          .repositoryUrl("https://github.com/example-org/claude-plugins")
          .ref("release-candidate")
          .build();
      var report = client.beta().organization().pluginMarketplaces().validateRepository(params);

      IO.println("valid: " + report.valid());
      IO.println("total_plugin_count: " + report.totalPluginCount());
  }
  ```

  ```php PHP
  $client = new Client();

  $report = $client->beta->organization->pluginMarketplaces->validateRepository(
      repositoryURL: 'https://github.com/example-org/claude-plugins',
      ref: 'release-candidate',
  );

  echo 'valid: ' . ($report->valid ? 'true' : 'false') . "\n";
  echo "total_plugin_count: {$report->totalPluginCount}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  report = client.beta.organization.plugin_marketplaces.validate_repository(
    repository_url: "https://github.com/example-org/claude-plugins",
    ref: "release-candidate"
  )

  puts "valid: #{report.valid}"
  puts "total_plugin_count: #{report.total_plugin_count}"
  ```
</CodeGroup>

```json
{
  "type": "plugin_marketplace_validation_report",
  "valid": false,
  "ref": "release-candidate",
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "total_plugin_count": 3,
  "manifest_error": null,
  "manifest_error_code": null,
  "plugin_errors": [
    {
      "name": "deploy-helper",
      "error": "The plugin has a top-level bin/ directory.",
      "error_code": "marketplace_sync_bin_directory_not_allowed"
    }
  ],
  "plugin_warnings": [
    {
      "name": "release-notes",
      "warnings": [
        {
          "message": "plugin.json has unrecognized top-level keys: owners",
          "error_code": "marketplace_sync_plugin_unrecognized_keys"
        }
      ]
    }
  ]
}
```

| Field | Description |
| ----- | ----- |
| `valid` | `true` when `marketplace.json` is well-formed and no plugin would be skipped. Warnings do not make it `false`. |
| `ref` | The branch that was read, by name; `null` when no branch was named and the default branch was read, for a commit SHA, or for an archive. |
| `commit_sha` | The commit that was validated. For an archive downloaded from a Git host, the commit the host recorded in the ZIP file’s comment field, if any (not verified). |
| `total_plugin_count` | How many plugins `marketplace.json` declares; `0` when it could not be read. |
| `manifest_error`, `manifest_error_code` | Set when nothing could be validated: the source could not be read, or `marketplace.json` is missing, malformed, or over a limit. Validation that did not complete within 120 seconds reports `manifest_error_code: "marketplace_validate_deadline_exceeded"`. |
| `plugin_errors` | One `{name, error, error_code}` per plugin a synchronization would skip. |
| `plugin_warnings` | One `{name, warnings: [{message, error_code}]}` per plugin that would synchronize with some contents left out. |

Validate a local copy of the marketplace directory instead, as a `.zip`; the response is the same report:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/plugin_marketplaces/validate_archive" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: ce-plugins-2026-09-01" \
    -F "archive=@marketplace.zip"
  ```

  ```bash CLI
  ant beta:organization:plugin-marketplaces validate-archive \
    --archive marketplace.zip
  ```

  ```python Python
  client = anthropic.Anthropic()

  with open("marketplace.zip", "rb") as archive:
      report = client.beta.organization.plugin_marketplaces.validate_archive(
          archive=archive
      )

  print(f"valid: {str(report.valid).lower()}")
  print(f"total_plugin_count: {report.total_plugin_count}")
  ```

  ```typescript TypeScript
  import fs from "node:fs";

  const client = new Anthropic();

  const report = await client.beta.organization.pluginMarketplaces.validateArchive({
    archive: fs.createReadStream("marketplace.zip")
  });

  console.log(`valid: ${report.valid}`);
  console.log(`total_plugin_count: ${report.total_plugin_count}`);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var report = await client.Beta.Organization.PluginMarketplaces.ValidateArchive(
      new() { Archive = File.OpenRead("marketplace.zip") }
  );

  Console.WriteLine($"valid: {report.Valid.ToString().ToLowerInvariant()}");
  Console.WriteLine($"total_plugin_count: {report.TotalPluginCount}");
  ```

  ```go Go
  client := anthropic.NewClient()

  archive, err := os.Open("marketplace.zip")
  if err != nil {
  	log.Fatal(err)
  }
  defer archive.Close()

  report, err := client.Beta.Organization.PluginMarketplaces.ValidateArchive(
  	context.Background(),
  	anthropic.BetaOrganizationPluginMarketplaceValidateArchiveParams{
  		Archive: archive,
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Printf("valid: %t\n", report.Valid)
  fmt.Printf("total_plugin_count: %d\n", report.TotalPluginCount)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.pluginmarketplaces.PluginMarketplaceValidateArchiveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      // Pass a Path so the `archive` part is sent with a file name, which this endpoint requires.
      var params = PluginMarketplaceValidateArchiveParams.builder()
          .archive(Path.of("marketplace.zip"))
          .build();
      var report = client.beta().organization().pluginMarketplaces().validateArchive(params);

      IO.println("valid: " + report.valid());
      IO.println("total_plugin_count: " + report.totalPluginCount());
  }
  ```

  ```php PHP
  use Anthropic\Core\FileParam;

  $client = new Client();

  $report = $client->beta->organization->pluginMarketplaces->validateArchive(
      archive: FileParam::fromResource(fopen('marketplace.zip', 'r')),
  );

  echo 'valid: ' . ($report->valid ? 'true' : 'false') . "\n";
  echo "total_plugin_count: {$report->totalPluginCount}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  report = client.beta.organization.plugin_marketplaces.validate_archive(
    archive: Pathname("marketplace.zip")
  )

  puts "valid: #{report.valid}"
  puts "total_plugin_count: #{report.total_plugin_count}"
  ```
</CodeGroup>

Problems with the content never fail the request. Apart from the responses every endpoint shares (a `403` for a key that has only `read:org_audit` or `read:compliance_org_data`; see [Error responses](https://platform.claude.com/docs/en/manage-claude/plugins-api#error-responses) and [Rate limiting](https://platform.claude.com/docs/en/manage-claude/plugins-api#rate-limiting)), the request itself can fail with:

| Status | Cause | What to do |
| ----- | ----- | ----- |
| 400 | On `validate_repository`: the body is not a JSON object; `repository_url` is missing, is longer than 2,048 characters, carries credentials, or is not of the form `https://github.com/{owner}/{repo}` (a `.git` suffix is accepted; another host, a longer path such as a branch page’s `/tree/main`, or a port other than 443 or 80 is not); `ref` is empty, is longer than 255 characters, contains `..`, or contains a character other than ASCII letters, digits, `.`, `_`, `-`, `+`, and `/`; or another field is present. A `ref` that passes these checks but names a branch the repository does not have is not refused: the request succeeds with `valid: false` and `manifest_error` says the branch was not found. On `validate_archive`: the body is not `multipart/form-data`, the `archive` part is missing, repeated, or not sent as a file part with a file name, or another form field is present. | Fix the request and resend. |
| 413 | On `validate_archive`: the `archive` part, or the request’s declared body length, exceeds 32 MB. | Validate the repository by URL instead, or trim the archive. |

#### Report codes

Each finding in a report has a stable code: `manifest_error_code` when nothing could be validated, `error_code` on each `plugin_errors` entry, and `error_code` on each warning. When a plugin has several problems, `error_code` is the first one’s and `error` joins their messages. New codes might be added. An unrecognized `manifest_error_code` still means that the content could not be validated. An unrecognized `error_code` on a `plugin_errors` entry still means that the plugin would be skipped. An unrecognized `error_code` on a warning still means that the plugin would synchronize. These codes indicate transient conditions, so the same request might succeed later: `marketplace_host_rate_limited`, `marketplace_host_server_error`, `marketplace_host_timeout`, `marketplace_host_unreachable`, `marketplace_repo_access_denied`, `marketplace_sync_transient_fetch_budget_exhausted`, `marketplace_validate_network_error`, and usually `marketplace_validate_deadline_exceeded`.

## Unrecognized values

Every string value on this page (component types, `reach`, scan fields, marketplace `source`, error codes) might gain new values at any time. Treat a value you do not recognize as you would any unknown string rather than failing.

## Rate limiting

Read requests (every `GET` endpoint on this page) share a limit of **300 requests per minute** for each organization. Write requests (creating a plugin or version, changing the served version, deleting, setting or removing an installation setting, and updating a marketplace) share a limit of **60 requests per minute** for each organization. A marketplace validation (either endpoint) counts as a read, and validations are additionally limited to 10 a minute for each organization across both endpoints; both limits are checked before the request body is read. These limits are counted across all of your organization’s keys and are separate from your organization’s other Admin API limits. A read that passes `organization_id` counts against the limit of the organization the key was created in, or of the parent organization if the key has no organization of its own. Requests over a limit return **429 Too Many Requests** with a `retry-after` header. Responses include `anthropic-ratelimit-requests-*` headers for the limit that applies (on marketplace validation, its 10-per-minute limit; on a `429`, whichever limit refused the request).

An upload, a served-version change, or a validation can also return `429` with `retry-after` when the service briefly has no capacity for another one, and an upload returns `429` when your organization has exceeded its content-scan rate. Handle all of these the same way: wait for `retry-after`, then retry. Separately from these limits, send installation-setting writes for the same plugin one at a time: when several arrive at the same time, some can be answered with `503` and `x-should-retry: true`, and those are safe to send again after a second or two (see [Set an installation setting](https://platform.claude.com/docs/en/manage-claude/plugins-api#set-an-installation-setting)).

## Pagination

List endpoints use an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor. Pass the cursor unchanged as the `page` parameter on the next request, and repeat until `next_page` is `null`. Treat the cursor string as opaque: don’t parse, modify, or construct it yourself. [List plugins](https://platform.claude.com/docs/en/manage-claude/plugins-api#list-plugins) might return a page with fewer than `limit` rows or with no rows while `next_page` is still set. A short or empty page is therefore not always the last one. The list iterators in the Python, TypeScript, C#, Go, Java, and Ruby SDKs allow for this. The CLI also allows for this, except with `--format raw`. Both request the next page while `next_page` is set. In PHP and cURL, request each page yourself and pass its `next_page` as `page`.

`limit` defaults to 20 and has a minimum of 1. The maximum is 100 for plugins, installation settings, and shares, and 1,000 for versions and marketplaces. Every list is ordered newest first.

## Error responses

Error responses follow the standard shape documented in [Claude API errors](https://platform.claude.com/docs/en/api/errors). Quote the `request_id` from the response body when contacting support.

| Status | Meaning |
| ----- | ----- |
| 400 | Invalid input, or the operation does not apply to this plugin or marketplace (see each endpoint’s section). Also returned for a query parameter the endpoint does not recognize, and for an organization that is not a Claude Enterprise organization (`this endpoint is not supported for this organization type`). |
| 401 | Missing `x-api-key` header, or the key is not recognized. |
| 403 | The key is missing the required scope, or the request uploads to, changes the served version of, or sets the default for a member’s plugin or personal marketplace. (Deleting a member’s plugin is allowed.) |
| 404 | Resource not found. Also returned when the request omits this API’s beta, or the API is not enabled for your organization, so that the endpoints read as nonexistent. |
| 409 | A name is taken, a version’s `content_scan` reads `processing`, or a conflicting upload is in progress. |
| 413 | The request body is over the size limit: 200 MB for an upload, 32 MB for marketplace validation. |
| 429 | Rate limit exceeded. See [Rate limiting](https://platform.claude.com/docs/en/manage-claude/plugins-api#rate-limiting). |
| 500 | Internal error. |
| 503 | Temporary. Also returned when several installation-setting writes for one plugin arrive at the same time; send those one at a time. Retry with backoff, except `registration_pending` (see the following table). |

When one status has several causes that you would handle differently, the error also carries `error.details.error_code`, and `error.details.plugin_id` or `error.details.plugin_version_id` when the cause involves one:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "...",
    "details": {
      "error_code": "plugin_name_taken",
      "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
    }
  },
  "request_id": "req_018EeWyXxfu5pfWkrYcMdjWG"
}
```

| `error_code` | Status | Meaning and what to do |
| ----- | ----- | ----- |
| `plugin_name_taken` | 409 | The marketplace already holds this name. `details.plugin_id` is the plugin that holds it, and someone else might have made it. To see who, [get the plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#get-a-plugin) and read its `created_by`, which is `null` when no creator is recorded. Upload versions to it only if it is the plugin you meant to update. Otherwise, or when `plugin_id` is absent, upload under another name. |
| `skill_name_taken` | 409 | The plugin is in the library marketplace and one of its skills has the name of an organization skill. `details.skill_name` names it. Retry with an upload or a version that has no skill of that name. You can also remove the organization skill in claude.ai. |
| `registration_pending` | 503 | The files were stored, but the plugin’s skills could not yet be made available to members. See [Retrying uploads](https://platform.claude.com/docs/en/manage-claude/plugins-api#retrying-uploads). |
| `scan_pending` | 409 | The version’s `content_scan` reads `processing`. Retry once the scan finishes. |
| `scan_failed` | 400 | The version’s `content_scan` reads `fail`, `unknown`, or `errored`, so it cannot be served. Choose another version. |
| `cmek_key_disabled`, `cmek_key_network_blocked` | 400 | Your organization’s customer-managed encryption key is unavailable. See [Customer-managed encryption keys](https://platform.claude.com/docs/en/manage-claude/plugins-api#customer-managed-encryption-keys). |
| `unsupported_charset` | 400 | On an upload or `validate_archive`, the request’s `Content-Type` header names a charset other than UTF-8, ISO-8859-1, or US-ASCII. Send the request with no charset, or with one of these. |

New codes might be added. Treat a code you do not recognize the way you treat its status.

### Retrying uploads

No endpoint accepts an `Idempotency-Key`. Changing the served version, setting an installation setting, and setting a marketplace default are safe to repeat. A repeated delete, or a repeated removal of an installation setting, returns `404`.

An upload that returns an error stored nothing, with one exception: `503` with `error_code: "registration_pending"`. After storing an upload’s files, the server registers the new version’s skills with claude.ai, which is what makes them usable by members; `registration_pending` means the files were stored but that last step did not complete. Uploading the same files once more completes it (and stores one more, identical version):

* On `POST /v1/organizations/plugins`, the plugin *was* created, and the response carries `x-should-retry: false`: do not resend the create (a resend returns `409 plugin_name_taken`); instead upload the same files as a version of `details.plugin_id`.
* On `POST /v1/organizations/plugins/{plugin_id}/versions`, the version *was* stored (`details.plugin_version_id`); resend the same request when the response carries `x-should-retry: true`, and do not when it carries `false`.

If a create’s response is lost, send the create again. A `409 plugin_name_taken` means either that the first attempt stored the plugin or that the name was already taken. Your lost create made the plugin in `details.plugin_id` only if its `created_by` is an `api_actor` with your key’s `api_key_id`. Check that before you upload to it (see `plugin_name_taken` in the preceding table). Retrying a version create whose response was lost stores a second, identical version. To avoid that, record the plugin’s `latest_version_id` before each upload; if a response is lost, read the plugin and retry only if `latest_version_id` is unchanged.

## Activity Feed events

Writes through this API are recorded on your organization’s Compliance API Activity Feed (see [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)), attributed to the API key as an `api_actor` carrying its `apikey_` ID. The same actor appears in `created_by` on the plugins and versions the key creates. A write that changes no field or setting records nothing.

| Event | Emitted when |
| ----- | ----- |
| `claude_plugin_created` | A plugin is created by an upload (here or in claude.ai) or by an accepted request to publish. A plugin created by a Git synchronization emits only `claude_plugin_version_created`. |
| `claude_plugin_version_created` | A version is stored. Versions stored by a Git synchronization are attributed to a `system_actor`. |
| `claude_plugin_updated` | A new version is uploaded to an existing plugin. |
| `claude_plugin_served_version_updated` | The served version changes. |
| `claude_plugin_deleted` | A plugin is deleted on its own, here or in claude.ai. |
| `plugin_installation_preference_updated` | An installation setting is set or removed. |
| `marketplace_created` | The first upload creates the library marketplace. |
| `marketplace_updated` | A marketplace’s default installation setting changes, or an administrator or owner starts a synchronization in claude.ai. |
| `marketplace_deleted` | A marketplace is deleted in claude.ai together with its plugins (no per-plugin events). |
| `claude_plugin_archive_accessed` | A member-owned plugin’s archive is downloaded. |
| `claude_plugin_security_scan_completed` | A content scan completes. |

The plugin, version, and marketplace IDs in these events are the same IDs this API returns. An event can also name a marketplace that this API does not list, such as a marketplace of plugins that Anthropic publishes. `plugin_installation_preference_updated` identifies the plugin by its `name` and `marketplace_id` rather than its `id`. In `claude_plugin_security_scan_completed`, `plugin_version` is not a version ID, and no field of a [plugin version](https://platform.claude.com/docs/en/manage-claude/plugins-api#plugin-versions) corresponds to it.

Changing a marketplace’s default installation setting records one `marketplace_updated` event. It records no per-plugin events, even though the organization-wide value of every plugin that inherits the default changes. Reads are not recorded, except downloads of a member-owned plugin’s archive.

Shares given or withdrawn in claude.ai appear on the feed as `role_assignment_granted` and `role_assignment_revoked` events. This API does not report deletions: a deleted plugin is absent from the next list. A plugin removed by a Git synchronization, by deleting its marketplace (one `marketplace_deleted` event), or by deleting a member’s account or the organization emits no per-plugin event, so re-list the full inventory periodically to catch removals.

## Customer-managed encryption keys

If your organization uses a [customer-managed encryption key](https://platform.claude.com/docs/en/manage-claude/cmek), a version’s `description`, `release_notes`, `components`, and files are encrypted with it. While the key is unavailable:

* Reads and lists still succeed, with `description`, `release_notes`, and `components` returned as `null`.
* Archive downloads, creates, version creates, and served-version changes return `400` with `cmek_key_disabled` or `cmek_key_network_blocked`.
* Deleting a plugin in the library marketplace returns `400 cmek_key_disabled` and deletes nothing, because its skills must first be withdrawn from claude.ai and that needs the key. Other deletes, installation settings, and marketplace defaults work normally.

Restoring the key clears all of these.

## See also

<CardGroup cols={2}>
  <Card title="Create an Admin API key" href="https://platform.claude.com/docs/en/manage-claude/admin-api-keys">
    Where your primary owner creates a scoped key.
  </Card>

  <Card title="User management" href="https://platform.claude.com/docs/en/manage-claude/user-management">
    The group endpoints that supply the `rbac_group_` IDs used in installation settings.
  </Card>

  <Card title="Compliance API Activity Feed" href="https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed">
    Where plugin writes and member-archive downloads are recorded.
  </Card>

  <Card title="Analytics APIs" href="https://platform.claude.com/docs/en/manage-claude/analytics-api">
    Plugin and skill usage reporting for Claude Enterprise.
  </Card>
</CardGroup>
