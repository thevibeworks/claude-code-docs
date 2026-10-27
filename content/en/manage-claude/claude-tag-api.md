---
title: Claude Tag API
url: https://platform.claude.com/docs/en/manage-claude/claude-tag-api
description: "Manage Claude Tag in Slack for your Claude Enterprise organization from your own systems: read and change settings on Slack channels and workspaces, see which settings apply and why, and attach Access bundles."
---

[Claude Tag](https://claude.com/docs/claude-tag/overview) is Claude working as a teammate in Slack: someone mentions Claude in a channel and Claude answers in the thread. The Claude Tag API lets you read and change, from your own systems, the Claude Tag settings that an organization owner otherwise sets by hand in [claude.ai > Organization settings > Claude Tag](https://claude.ai/admin-settings/claude-tag). Use it to turn Claude on channel by channel from an approval workflow, keep your configuration in version control, or audit what applies in every channel.

Claude Tag is a claude.ai product. This API manages it for a Claude Enterprise organization and has nothing to do with Claude Platform workspaces, API usage, or the Claude Console.

<Check>
  **Scoped Admin API key required**

  These endpoints require an Admin API key with the `read:claude_tag` scope (for `GET` endpoints) or the `write:claude_tag` scope (for `POST` and `DELETE` endpoints); see [Scopes](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#scopes). See [Create an Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization) for where your primary owner creates one.
</Check>

<Note>
  The Claude Tag API is in **beta** and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations.

  Every request must include the [beta header](https://platform.claude.com/docs/en/api/beta-headers) `anthropic-beta: experimental-claude-tag-2026-10-21` (the SDK and the `ant` CLI send it for you). A request without it returns `404`, exactly as if the endpoint did not exist.
</Note>

## Endpoints

The API exposes 14 endpoints across four resources:

| Resource                                                                                                                                      | Endpoints                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Slack channels:** set a channel up, list the channels of a workspace or find one by its Slack IDs, read one, change its settings, remove it | `POST /v1/organizations/claude_tag/slack_channels`<br />`GET /v1/organizations/claude_tag/slack_channels`<br />`GET /v1/organizations/claude_tag/slack_channels/{id}`<br />`POST /v1/organizations/claude_tag/slack_channels/{id}`<br />`DELETE /v1/organizations/claude_tag/slack_channels/{id}`      |
| **Slack workspaces:** list your workspaces or find one by its Slack ID, read one, change its settings                                         | `GET /v1/organizations/claude_tag/slack_workspaces`<br />`GET /v1/organizations/claude_tag/slack_workspaces/{id}`<br />`POST /v1/organizations/claude_tag/slack_workspaces/{id}`                                                                                                                       |
| **Bundles:** list your organization's Access bundles, read one (read-only)                                                                    | `GET /v1/organizations/claude_tag/bundles`<br />`GET /v1/organizations/claude_tag/bundles/{bundle_id}`                                                                                                                                                                                                 |
| **Bundle targets:** list where a Bundle is attached, attach it to a channel or workspace, read one attachment, detach it                      | `GET /v1/organizations/claude_tag/bundles/{bundle_id}/targets`<br />`POST /v1/organizations/claude_tag/bundles/{bundle_id}/targets`<br />`GET /v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}`<br />`DELETE /v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}` |

This release covers Slack. Connecting and disconnecting a Slack workspace or Enterprise Grid, your organization's Slack defaults, creating and editing Access bundles, spend limits, and every Claude Tag setting other than the five in [Settings](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#settings) stay in claude.ai.

## Prerequisites

* Your organization must be on a Claude Enterprise plan, with [Claude Tag set up](https://claude.com/docs/claude-tag/admins/setup-overview) and at least one Slack workspace or Enterprise Grid connected.
* Your primary owner creates an Admin API key with the `read:claude_tag` scope, the `write:claude_tag` scope, or both in [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access). See [Create a key for a Claude Enterprise organization](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-enterprise-organization).
* Every request carries three headers: `x-api-key`, `anthropic-version: 2023-06-01` (see [API versions](https://platform.claude.com/docs/en/api/versioning)), and `anthropic-beta: experimental-claude-tag-2026-10-21`.

In Python, TypeScript, C#, Go, Java, PHP, and Ruby, the SDK exposes these endpoints under `client.beta.organization.claude_tag` (typescript: `client.beta.organization.claudeTag`; csharp, go: `client.Beta.Organization.ClaudeTag`; java: `client.beta().organization().claudeTag()`; php: `$client->beta->organization->claudeTag`), and the [`ant` CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart) under `ant beta:organization:claude-tag`; they send the `anthropic-version` and `anthropic-beta` headers for you. The examples on this page read the Admin API key from the `ANTHROPIC_API_KEY` environment variable. Where an SDK or the CLI fetches more pages for you, `limit` sets the page size, not the total (see [Pagination](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#pagination)).

API keys belong to the organization and keep working after the person who created them leaves. Do not share them or check them into source control.

## Quick start

List your organization's Slack workspaces in Claude Tag:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-workspaces list
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspaces = client.beta.organization.claude_tag.slack_workspaces.list()

  # Automatically fetches more pages as needed.
  for workspace in workspaces:
      print(f"{workspace.id}: {workspace.slack.workspace_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspaces = await client.beta.organization.claudeTag.slackWorkspaces.list();

  for await (const workspace of workspaces) {
    console.log(`${workspace.id}: ${workspace.slack.workspace_id}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ClaudeTag.SlackWorkspaces.List();

  await foreach (var workspace in page.Paginate())
  {
      Console.WriteLine($"{workspace.ID}: {workspace.Slack.WorkspaceID}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  workspaces := client.Beta.Organization.ClaudeTag.SlackWorkspaces.ListAutoPaging(
  	context.Background(),
  	anthropic.BetaOrganizationClaudeTagSlackWorkspaceListParams{},
  )

  for workspaces.Next() {
  	workspace := workspaces.Current()
  	fmt.Printf("%s: %s\n", workspace.ID, workspace.Slack.WorkspaceID)
  }
  if err := workspaces.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var workspaces = client.beta().organization().claudeTag().slackWorkspaces().list();

  for (var workspace : workspaces.autoPager()) {
      IO.println(workspace.id() + ": " + workspace.slack().workspaceId());
  }
  ```

  ```php PHP
  $client = new Client();

  $workspaces = $client->beta->organization->claudeTag->slackWorkspaces->list();

  // Only this page; for the next, call list() again with page: $workspaces->nextPage.
  foreach ($workspaces->getItems() as $workspace) {
      echo "{$workspace->id}: {$workspace->slack->workspaceID}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.claude_tag.slack_workspaces.list

  page.auto_paging_each do |workspace|
    puts "#{workspace.id}: #{workspace.slack.workspace_id}"
  end
  ```
</CodeGroup>

```json Response
{
  "data": [
    {
      "type": "slack_workspace",
      "id": "slws_011CZkZnWa7xPc3uJfZe5LgT",
      "slack": {
        "workspace_id": "T01ABCD2EFG"
      },
      "settings": {
        "enabled": null,
        "instructions": "Answer in English unless asked otherwise.",
        "model": null,
        "environment_id": null,
        "guest_policy": null
      },
      "sources": {
        "enabled": null,
        "instructions": [
          {
            "type": "slack_workspace",
            "slack_workspace_id": "slws_011CZkZnWa7xPc3uJfZe5LgT"
          }
        ],
        "model": null,
        "environment_id": null,
        "guest_policy": null
      },
      "created_at": "2026-09-02T17:04:11Z",
      "updated_at": "2026-10-06T09:41:53Z"
    }
  ],
  "next_page": null
}
```

A setting that is `null` in `settings` is not set on this workspace, so the workspace inherits it and has no source for it. To read what applies instead, see [Stored and inherited values](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#stored-and-inherited-values).

## Scopes

| Scope              | Grants                                                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `read:claude_tag`  | Every `GET` endpoint on this page.                                                                                                      |
| `write:claude_tag` | Every `POST` and `DELETE` endpoint on this page. It does not grant reads, although the response to a change holds the changed resource. |

A key can carry both scopes. An integration that looks a channel up and then changes it needs both. No other scope grants access to these endpoints, and a key created in the Claude Console does not work here.

The key must belong to the organization as a whole. The organization is always the one the key belongs to, and no request names one. The `anthropic-workspace-id` header is ignored, because nothing here belongs to a Claude Platform workspace.

## Key concepts

### Names on this page and in claude.ai

| This API         | claude.ai and Slack                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Slack workspace  | A Slack workspace. Slack's own API calls it a team, so Slack's own workspace ID on this page is the team ID there. It is unrelated to a Claude Platform workspace, whose IDs start with `wrkspc_`. |
| Slack defaults   | **Default Slack access**: the settings that apply to every workspace and channel. An organization owner changes them in claude.ai; this API shows where a channel or workspace inherits from them. |
| Settings level   | A [scope](https://claude.com/docs/claude-tag/admins/customize): a channel, a workspace, or the Slack defaults                                                                                      |
| Bundle           | An Access bundle ([Claude Tag glossary](https://claude.com/docs/claude-tag/concepts/glossary#access-bundle))                                                                                       |
| `enabled`        | The **Enable Claude Tag in Slack** toggle                                                                                                                                                          |
| `instructions`   | **Custom instructions**                                                                                                                                                                            |
| `model`          | **Model**                                                                                                                                                                                          |
| `environment_id` | **Environment**                                                                                                                                                                                    |
| `guest_policy`   | **How should Claude work in channels with guests**: `restrict` is **Restrict**, `channel_only` is **Channel only**, and `allow` is **Full access**                                                 |

### Set-up channels and workspaces

A channel or workspace is **set up** when Claude Tag holds a settings record for it. Only a set-up channel or workspace has an `id`, and only those are listed: Slack, not this API, holds the full list of a workspace's channels.

* A **workspace** is set up when an organization owner connects it in claude.ai. When an owner connects a Slack Enterprise Grid, the Grid's workspaces are set up shortly afterward. Claude's first use in a workspace, or the first channel you [set up](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel) in it, sets up any that was not. No other endpoint sets up a workspace, and none removes one.
* A **channel** is set up in claude.ai, by Claude's first use in it, or with [Set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel).

Your organization owns a workspace while its connection to that workspace is active, and owns the channels in it. A Slack Enterprise Grid groups several workspaces under one company. While your organization's connection to a Grid is active, it also owns every workspace in the Grid that no other organization has connected. Such a workspace is a workspace like any other: once it is set up, it has an `id`, is listed, and can be read, changed, and given Bundles, and its channels can be listed. The Grid itself is not a resource of this API and has no `id`. A channel or workspace you do not own returns the same `404` as one that does not exist.

A workspace your organization owns only through a Grid returns that `404` until it is set up, wherever a request names it by Slack's own ID: when you find the workspace, list its channels, or look up a channel in it that is not set up. You can still [set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel) in it, which also sets the workspace up, with no settings stored.

A channel that is shared with a whole Grid can be stored under the Grid's own Slack ID, which starts with `E`, in place of a workspace's. That ID is then the channel's `slack.workspace_id`, and [listing channels](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-channels) with it as `slack_workspace_id` returns those channels. No workspace object has it: if an owner stored settings on the Grid itself in claude.ai, `sources` can name them as a `slack_workspace` whose `id` returns `404` when you read it.

### IDs

You know a channel by the IDs Slack shows you. Look its `id` up once with [Find a channel by its Slack IDs](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#find-a-channel-by-its-slack-ids), then store and use the `id`.

| ID                       | Prefix                                                                                                                                                                  | Where it appears                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Slack channel resource   | `slch_`                                                                                                                                                                 | `id` on a channel; `slack_channel_id` in request bodies and responses     |
| Slack workspace resource | `slws_`                                                                                                                                                                 | `id` on a workspace; `slack_workspace_id` in request bodies and responses |
| Bundle                   | `capp_`                                                                                                                                                                 | `id` on a Bundle; `{bundle_id}` in paths                                  |
| Bundle target            | `btgt_`                                                                                                                                                                 | `id` on a Bundle target; `{target_id}` in paths                           |
| Slack's own workspace ID | `T`, or `E` for a Grid's own ID (see [Set-up channels and workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-channels-and-workspaces)) | `slack.workspace_id`; the `slack_workspace_id` query parameter            |
| Slack's own channel ID   | `C` or `G`                                                                                                                                                              | `slack.channel_id`; the `slack_channel_id` query parameter                |

<Warning>
  `slack_channel_id` and `slack_workspace_id` each mean two things. In a **query parameter** each is Slack's own ID (`C05HJKL6MNP`, `T01ABCD2EFG`). In a **request body or a response** each is the `id` this API issues (`slch_...`, `slws_...`). Slack's own IDs in a body or a response are always under `slack`.
</Warning>

A Slack channel ID in a query parameter or a request body that does not start with `C` or `G` returns `400`, and so does any Slack ID that has anything but capital letters and digits after its first letter or is longer than 32 characters.

An `id` does not change while the channel or workspace is set up, whatever you change on it, with one exception described in [Read-only mode](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-only-mode). A channel or workspace that is removed and set up again has a new `id`, and the old one keeps returning `404`. When a stored `id` returns `404` with no `error_code`, [list your workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-workspaces) with the same key and headers. That request names no channel or workspace, so if it returns `200`, the `id` is gone: find the channel or workspace again by its Slack IDs. Any other status says nothing about the `id`: keep your stored `id` values and see [Error responses](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#error-responses).

### Settings

Each settings level stores the same five settings, all optional:

| Setting          | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`        | boolean | Whether Claude is on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `instructions`   | string  | Standing guidance Claude reads in every session. At most 8,192 characters after leading and trailing white space is trimmed. Blank text clears the setting.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `model`          | string  | The model new sessions start on: a [model ID](https://platform.claude.com/docs/en/models/overview) your organization can use with Claude Tag. At most 128 characters.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `environment_id` | string  | The cloud environment sessions run in, prefixed `env_`. It must be active and belong to your organization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `guest_policy`   | object  | What Claude does in a channel while a Slack guest is in it, for everyone in the channel: `{"type": "allow"}` (Claude answers), `{"type": "restrict"}` (Claude does not answer), or `{"type": "channel_only"}` (Claude answers with only the Bundles attached to the channel itself; if `channel_only` is not available to your organization, a request that sets it returns `400`). See [Restrict guest channels](https://claude.com/docs/claude-tag/admins/restrict-access#restrict-guest-channels) for what it means in channels shared through Slack Connect or across an Enterprise Grid. |

`model` and `environment_id` are checked when you write them and not again: if the model or environment later changes, responses keep returning the stored value.

If an organization owner has put a settings level on a self-hosted runner pool in claude.ai, its `environment_id` returns the pool's ID, which starts with `ccpool_`. This API cannot set a runner pool, and returns `400` for a request that changes or clears `environment_id` on a settings level that stores one.

### Stored and inherited values

Settings exist at three levels: the channel, the workspace the channel is in, and your organization's Slack defaults, which an organization owner sets in claude.ai. Each level stores only what was set on it. The `settings` of a channel or workspace object can hold either of two things:

* **What it stores.** This is what a response holds unless you ask otherwise. A setting that is not set on the channel or workspace is `null`. Use it to compare against configuration you keep elsewhere.
* **What applies in it**, once every level is taken into account. To get this, add the query parameter `include_inherited=true` to any `GET` request that returns a channel or a workspace, the two lists included. Use it to audit, or to find out why Claude behaves as it does in one channel. The parameter defaults to `false`, and a value that is not a Boolean returns `400`. A request that sets a channel up or changes settings does not take the parameter and returns `400` if you send it; its response holds what is stored.

In both cases `sources` names, for each setting, the level that the value in `settings` comes from. Without `include_inherited`, the source of a setting that the channel or workspace stores names the channel or workspace itself, and a setting it does not store has no source: `null`, or an empty list for `instructions`. With `include_inherited=true`, every setting except `instructions` has a source, and a setting that no level sets has the source `{"type": "default"}`; when no level sets `instructions`, it is `null` and its source list is empty. So to tell a value the channel or workspace sets itself from one it inherits, look at its source, not at whether the value is `null`.

Each setting is resolved on its own:

| Setting          | Rule                                                                                                                                      | When no level sets it                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `enabled`        | The nearest level that sets it determines the value, so `true` on a channel turns Claude on there even when its workspace stores `false`. | `true`                                          |
| `instructions`   | Additive. The text of every level that sets it is joined, broadest first, with a blank line between.                                      | `null`                                          |
| `model`          | The nearest level that sets it determines the value.                                                                                      | `null`: Claude uses the product's default model |
| `environment_id` | The nearest level that sets it determines the value.                                                                                      | `null`                                          |
| `guest_policy`   | The nearest level that sets it determines the value.                                                                                      | `restrict`                                      |

For example, an organization stores instructions on its Slack defaults, turns Claude off on a workspace, and sets a model on one channel of that workspace. Read with `include_inherited=true`, the channel shows the three values and where each comes from:

```json
{
  "type": "slack_channel",
  "id": "slch_011CZkZmRt4vNq8sHbYw2KdX",
  "slack": {
    "workspace_id": "T01ABCD2EFG",
    "channel_id": "C05HJKL6MNP"
  },
  "settings": {
    "enabled": false,
    "instructions": "Be brief.",
    "model": "claude-opus-5-5",
    "environment_id": null,
    "guest_policy": { "type": "restrict" }
  },
  "sources": {
    "enabled": {
      "type": "slack_workspace",
      "slack_workspace_id": "slws_011CZkZnWa7xPc3uJfZe5LgT"
    },
    "instructions": [{ "type": "slack_default" }],
    "model": {
      "type": "slack_channel",
      "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX"
    },
    "environment_id": { "type": "default" },
    "guest_policy": { "type": "default" }
  },
  "created_at": "2026-10-19T16:20:05Z",
  "updated_at": "2026-10-19T16:24:38Z"
}
```

Read without the parameter, the same channel has its `model` and four `null` settings in `settings`; in `sources`, `model` names the channel, `instructions` is an empty list, and the other three are `null`.

A source is one of:

| `type`                 | Meaning                                                                                                                                                                                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slack_channel`        | The channel, named in `slack_channel_id`.                                                                                                                                                                                                                                                             |
| `slack_workspace`      | The workspace, named in `slack_workspace_id`.                                                                                                                                                                                                                                                         |
| `slack_parent_channel` | The parent of a code channel, named in `slack_channel_id`. A code channel is one that was started from another channel. While the parent is a public channel in the same workspace, it sits between the channel and the workspace and contributes `instructions` and `environment_id` only.           |
| `slack_grid_channel`   | The same Slack channel as set up under another workspace of its Slack Enterprise Grid, named by Slack's own IDs under `slack`. It contributes `enabled` only: when neither the channel nor its workspace sets `enabled`, a `true` stored for the channel under another workspace of the Grid applies. |
| `slack_default`        | Your organization's Slack defaults, which have no ID.                                                                                                                                                                                                                                                 |
| `default`              | No level sets a value, so the built-in default applies.                                                                                                                                                                                                                                               |

`sources.instructions` lists every level that contributes text, broadest first, which is the order of their text in `settings.instructions`, and is empty when none does. It says whose text comes first, not where one level's text ends: to get one level's own text, read that channel or workspace without `include_inherited`, or, for the Slack defaults, look in claude.ai. A source that names a channel or workspace always carries its ID, which is never `null`: an `id` of this API in `slack_channel_id` or `slack_workspace_id`, or, on `slack_grid_channel`, Slack's own IDs under `slack` as on a channel object.

With `include_inherited=true`, a request fails with `503` if a level cannot be read, rather than answer without it.

### Changing settings

The two update endpoints and [Set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel) take a `settings` object under the same rules:

* **A setting you leave out is unchanged.** `{"settings": {"enabled": false}}` turns Claude off and leaves the other four settings as they are.
* **A setting you send as `null` is cleared**, so the level inherits it again.
* **All or nothing.** If any value in a request is refused, no setting in the request is stored.
* **Safe to repeat.** Every change leaves the resource as the first identical request left it, so no endpoint takes an `Idempotency-Key`. A request that alters nothing writes nothing and records no Activity Feed event.
* **Last write wins.** No request takes a precondition. Two callers that each read a resource and then change the same setting overwrite one another. A `409` is returned only when another change overlaps your request while it runs; nothing your request asked to change or delete was done, except that a setup request might already have set the channel up, so read the resource again and resend the change if it is still needed.

A change to `guest_policy` on a channel can end sessions that are running in that channel. They end in the background, and the response does not wait for it.

### Read-only mode

**API / Terraform read-only mode** is a setting that an organization owner turns on and off in claude.ai's Claude Tag settings. The name describes claude.ai and Slack: while the mode is on, they refuse a person's changes to what this API manages, so only keys make those changes. They also refuse a few related changes that no key makes, such as changing a setting on the Slack defaults, so nobody makes those until an owner turns the mode off. It does not make this API read-only. Every endpoint on this page answers the same whether the mode is on or off, and no endpoint reads or changes it.

While the mode is off, people and keys change the same settings and attach and detach the same Bundles, and each change replaces what is stored. Turn it on if your pipeline should be the only source of changes.

While the mode is on, claude.ai and Slack refuse:

* Changing any of the five settings on a channel, a workspace, or the Slack defaults (which no key changes either)
* Setting a channel up, removing a channel, adding a workspace of a connected Enterprise Grid, or disconnecting a workspace or a Grid in claude.ai
* Attaching a Bundle to a channel or workspace, detaching one, or deleting a Bundle that is attached to one

Some things stay possible either way: an owner can still connect a new workspace or Grid, create and edit Bundles, and change Claude Tag settings this API does not manage. Claude's first use still sets up a channel, or a Grid workspace that was not set up, deleting a channel in Slack still removes it, and uninstalling Claude's Slack app still disconnects that workspace or Grid.

While the mode is off, setting up in claude.ai a channel that is already set up can replace the channel's record, but only a channel that holds nothing yet: one that Claude's first use set up, or that this API set up with no `settings`, and on which nobody has since stored a setting or attached a Bundle. The channel then has a new `id`, and the old one returns `404`. Any other channel keeps its `id` until it is removed.

### Group direct messages

A Slack group direct message has an ID in a channel's form, so Claude's use in one sets it up like a channel: it has an `id`, is listed, and can be read. Setting one up through this API, changing a setting on one, attaching a Bundle to one, and removing one each return `400`, except that a setup request that omits `settings` for one that is already set up returns it with `200`, as a read does. Detaching a Bundle from one is allowed.

## Example workflows

### Turn Claude on only in approved channels

Any member can invite Claude to a public channel. To keep Claude on only where you have approved it:

1. Ask an organization owner to turn Claude off everywhere in claude.ai, with the **Enable Claude Tag in Slack** toggle under **Default Slack access**, which stores `enabled` as `false` on your organization's Slack defaults. [Read-only mode](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-only-mode) must be off while they do.
2. When your approval system approves a channel, [set the channel up](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel) with `"settings": {"enabled": true}`. The request takes Slack's own IDs and returns the channel even if it was already set up, so it is safe to repeat.
3. In the same run, [attach](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#attach-a-bundle) the Bundles the team was approved for, so the channel's first session already has its tools.

### Keep configuration in version control

1. Key your configuration by the IDs Slack shows for each channel, and [find each channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#find-a-channel-by-its-slack-ids) by them.
2. Read each channel without `include_inherited` and compare its `settings` with what your repository declares. With the parameter, inherited values would be mixed in.
3. Send only the settings that differ, and send `null` for a setting your repository no longer declares.
4. Ask an organization owner to turn on [read-only mode](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-only-mode), so that nobody changes the same settings by hand.

### Audit what applies everywhere

1. [List your workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-workspaces), then [list each workspace's channels](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-channels), both with `include_inherited=true` so that each item holds what applies in it. If your organization connected an Enterprise Grid, also list the channels stored under the Grid's own Slack ID. See [Set-up channels and workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-channels-and-workspaces).
2. Flag what your policy forbids, such as a channel where `enabled` is `true` without an approval on file, or where `guest_policy` is `allow`.
3. [List your Bundles](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-bundles), then [each Bundle's targets](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-a-bundles-targets), to see where access to sensitive systems is attached.

## Slack channels

The channel object describes one Slack channel:

| Field        | Description                                                                                                                                                                                                                                                                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`       | `slack_channel`.                                                                                                                                                                                                                                                                                                                                                            |
| `id`         | Prefixed `slch_`. See [IDs](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#ids).                                                                                                                                                                                                                                                                          |
| `slack`      | Slack's own IDs: `workspace_id` for the workspace the channel is in, and `channel_id` for the channel.                                                                                                                                                                                                                                                                      |
| `settings`   | What the channel itself stores, or, with `include_inherited=true`, what applies in it. Always present, with all five [settings](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#settings); one that is not set is `null`. See [Stored and inherited values](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#stored-and-inherited-values). |
| `sources`    | For each setting, the level that the value in `settings` comes from. Always present.                                                                                                                                                                                                                                                                                        |
| `created_at` | When the channel was set up.                                                                                                                                                                                                                                                                                                                                                |
| `updated_at` | When Claude Tag's record of the channel last changed. It moves on every change to a setting, here, in claude.ai, or in Slack, and can also move for a change that no response here shows. Treat a later value as a reason to read the channel again, not as proof that a setting changed. Attaching or detaching a Bundle does not by itself move it.                       |

An `id` that is not a valid `slch_` identifier returns `400`. A valid one that names no channel of your organization returns `404`.

### Set up a channel

`POST /v1/organizations/claude_tag/slack_channels` sets a Slack channel up and returns it. `slack.workspace_id` and `slack.channel_id` are required and are Slack's own IDs. `settings` is optional and follows [Changing settings](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#changing-settings). If the channel is already set up, the request returns the existing channel and applies `settings`; the response is `200` in both cases. Requires the `write:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{
      "slack": {"workspace_id": "T01ABCD2EFG", "channel_id": "C05HJKL6MNP"},
      "settings": {"instructions": "Answer in the language of the question."}
    }'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels create \
    --slack '{workspace_id: T01ABCD2EFG, channel_id: C05HJKL6MNP}' \
    --settings '{instructions: "Answer in the language of the question."}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  channel = client.beta.organization.claude_tag.slack_channels.create(
      slack={"workspace_id": "T01ABCD2EFG", "channel_id": "C05HJKL6MNP"},
      settings={"instructions": "Answer in the language of the question."},
  )

  print(channel.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channel = await client.beta.organization.claudeTag.slackChannels.create({
    slack: { workspace_id: "T01ABCD2EFG", channel_id: "C05HJKL6MNP" },
    settings: { instructions: "Answer in the language of the question." }
  });

  console.log(channel.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var channel = await client.Beta.Organization.ClaudeTag.SlackChannels.Create(
      new()
      {
          Slack = new() { WorkspaceID = "T01ABCD2EFG", ChannelID = "C05HJKL6MNP" },
          Settings = new() { Instructions = "Answer in the language of the question." },
      }
  );

  Console.WriteLine(channel.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  channel, err := client.Beta.Organization.ClaudeTag.SlackChannels.New(
  	context.Background(),
  	anthropic.BetaOrganizationClaudeTagSlackChannelNewParams{
  		Slack: anthropic.BetaClaudeTagSlackChannelIdentifiersParam{
  			WorkspaceID: "T01ABCD2EFG",
  			ChannelID:   "C05HJKL6MNP",
  		},
  		Settings: anthropic.BetaClaudeTagSettingsCreateParam{
  			Instructions: anthropic.String("Answer in the language of the question."),
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(channel.ID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagSettingsCreate;
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagSlackChannelIdentifiers;
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelCreateParams.builder()
          .slack(BetaClaudeTagSlackChannelIdentifiers.builder()
              .workspaceId("T01ABCD2EFG")
              .channelId("C05HJKL6MNP")
              .build())
          .settings(BetaClaudeTagSettingsCreate.builder()
              .instructions("Answer in the language of the question.")
              .build())
          .build();
      var channel = client.beta().organization().claudeTag().slackChannels().create(params);

      IO.println(channel.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $channel = $client->beta->organization->claudeTag->slackChannels->create(
      slack: ['workspaceID' => 'T01ABCD2EFG', 'channelID' => 'C05HJKL6MNP'],
      settings: ['instructions' => 'Answer in the language of the question.'],
  );

  echo "{$channel->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel = client.beta.organization.claude_tag.slack_channels.create(
    slack: {workspace_id: "T01ABCD2EFG", channel_id: "C05HJKL6MNP"},
    settings: {instructions: "Answer in the language of the question."}
  )

  puts channel.id
  ```
</CodeGroup>

```json Response
{
  "type": "slack_channel",
  "id": "slch_011CZkZmRt4vNq8sHbYw2KdX",
  "slack": {
    "workspace_id": "T01ABCD2EFG",
    "channel_id": "C05HJKL6MNP"
  },
  "settings": {
    "enabled": null,
    "instructions": "Answer in the language of the question.",
    "model": null,
    "environment_id": null,
    "guest_policy": null
  },
  "sources": {
    "enabled": null,
    "instructions": [
      {
        "type": "slack_channel",
        "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX"
      }
    ],
    "model": null,
    "environment_id": null,
    "guest_policy": null
  },
  "created_at": "2026-10-19T16:20:05Z",
  "updated_at": "2026-10-19T16:20:05Z"
}
```

Before a channel is set up, Claude's Slack app confirms with Slack that the channel is in the workspace, is not archived, and is visible to the app. A channel that fails that check returns `404`, as does a workspace that does not have Claude's Slack app installed. For a workspace your organization owns through an Enterprise Grid, the app must be installed on the Grid.

Setting the channel up and applying `settings` are two steps. When this request sets the channel up and `settings` is then refused with a `400`, `404`, or `409`, the response is the refusal and the channel stays set up with nothing stored (after a `409`, unless the overlapping change removed or replaced it). That refusal carries an `error_code` that starts with `slack_channel_set_up_` and the new channel's `id` in `error.details.slack_channel_id` (see [Error responses](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#error-responses)). Correct `settings` and send it in an [update](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#update-a-channel) to that `id`, or send the setup request again. If the channel was already set up, a refused `settings` returns the same error as an [update](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#update-a-channel) would, and the channel keeps what it stored. A `500` or `503` in either case carries no `error_code` and does not say whether the channel was set up or `settings` stored: send the setup request again.

### List channels

`GET /v1/organizations/claude_tag/slack_channels` lists the set-up channels of one workspace, newest first by `created_at`. `slack_workspace_id` is required and is Slack's own ID for the workspace. Add `include_inherited=true` to have each channel hold what applies in it (see [Stored and inherited values](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#stored-and-inherited-values)). A page can hold fewer than `limit` channels, or none, while `next_page` is still set, so keep requesting pages until `next_page` is `null` (see [Pagination](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#pagination)). Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels?slack_workspace_id=T01ABCD2EFG" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels list --slack-workspace-id T01ABCD2EFG
  ```

  ```python Python
  client = anthropic.Anthropic()

  channels = client.beta.organization.claude_tag.slack_channels.list(
      slack_workspace_id="T01ABCD2EFG"
  )

  # Automatically fetches more pages as needed.
  for channel in channels:
      print(f"{channel.id}: {channel.slack.channel_id}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channels = await client.beta.organization.claudeTag.slackChannels.list({
    slack_workspace_id: "T01ABCD2EFG"
  });

  for await (const channel of channels) {
    console.log(`${channel.id}: ${channel.slack.channel_id}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ClaudeTag.SlackChannels.List(
      new() { SlackWorkspaceID = "T01ABCD2EFG" }
  );

  await foreach (var channel in page.Paginate())
  {
      Console.WriteLine($"{channel.ID}: {channel.Slack.ChannelID}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  channels := client.Beta.Organization.ClaudeTag.SlackChannels.ListAutoPaging(
  	context.Background(),
  	anthropic.BetaOrganizationClaudeTagSlackChannelListParams{
  		SlackWorkspaceID: "T01ABCD2EFG",
  	},
  )

  for channels.Next() {
  	channel := channels.Current()
  	fmt.Printf("%s: %s\n", channel.ID, channel.Slack.ChannelID)
  }
  if err := channels.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelListParams.builder()
          .slackWorkspaceId("T01ABCD2EFG")
          .build();
      var channels = client.beta().organization().claudeTag().slackChannels().list(params);

      for (var channel : channels.autoPager()) {
          IO.println(channel.id() + ": " + channel.slack().channelId());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $channels = $client->beta->organization->claudeTag->slackChannels->list(
      slackWorkspaceID: 'T01ABCD2EFG',
  );

  // Only this page; for the next, call list() again with page: $channels->nextPage.
  foreach ($channels->getItems() as $channel) {
      echo "{$channel->id}: {$channel->slack->channelID}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.claude_tag.slack_channels.list(slack_workspace_id: "T01ABCD2EFG")

  page.auto_paging_each do |channel|
    puts "#{channel.id}: #{channel.slack.channel_id}"
  end
  ```
</CodeGroup>

The response is `{"data": [...], "next_page": ...}`, where each item is a channel object. A `slack_workspace_id` that names a workspace your organization does not own returns `404`, and so does one it owns only through an Enterprise Grid until that workspace is set up (see [Set-up channels and workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-channels-and-workspaces)).

### Find a channel by its Slack IDs

Add `slack_channel_id`, Slack's own ID for the channel, to look one channel up. `data` holds that channel, or is empty when the channel is not set up. In a workspace that is not set up and that your organization owns only through an Enterprise Grid, a channel that is not set up returns `404` instead. A lookup does not page: it ignores `page` and any `limit` from 1 to 100 (a `limit` outside that range still returns `400`), and its `next_page` is `null`. This is how you find a channel's `id`.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels?slack_workspace_id=T01ABCD2EFG&slack_channel_id=C05HJKL6MNP" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels list \
    --slack-workspace-id T01ABCD2EFG \
    --slack-channel-id C05HJKL6MNP
  ```

  ```python Python
  client = anthropic.Anthropic()

  page = client.beta.organization.claude_tag.slack_channels.list(
      slack_workspace_id="T01ABCD2EFG",
      slack_channel_id="C05HJKL6MNP",
  )

  for channel in page.data:
      print(channel.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const page = await client.beta.organization.claudeTag.slackChannels.list({
    slack_workspace_id: "T01ABCD2EFG",
    slack_channel_id: "C05HJKL6MNP"
  });

  for (const channel of page.data) {
    console.log(channel.id);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ClaudeTag.SlackChannels.List(
      new() { SlackWorkspaceID = "T01ABCD2EFG", SlackChannelID = "C05HJKL6MNP" }
  );

  foreach (var channel in page.Items)
  {
      Console.WriteLine(channel.ID);
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  page, err := client.Beta.Organization.ClaudeTag.SlackChannels.List(
  	context.Background(),
  	anthropic.BetaOrganizationClaudeTagSlackChannelListParams{
  		SlackWorkspaceID: "T01ABCD2EFG",
  		SlackChannelID:   anthropic.String("C05HJKL6MNP"),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  for _, channel := range page.Data {
  	fmt.Println(channel.ID)
  }
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelListParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelListParams.builder()
          .slackWorkspaceId("T01ABCD2EFG")
          .slackChannelId("C05HJKL6MNP")
          .build();
      var page = client.beta().organization().claudeTag().slackChannels().list(params);

      for (var channel : page.items()) {
          IO.println(channel.id());
      }
  }
  ```

  ```php PHP
  $client = new Client();

  $channels = $client->beta->organization->claudeTag->slackChannels->list(
      slackWorkspaceID: 'T01ABCD2EFG',
      slackChannelID: 'C05HJKL6MNP',
  );

  foreach ($channels->getItems() as $channel) {
      echo "{$channel->id}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.claude_tag.slack_channels.list(
    slack_workspace_id: "T01ABCD2EFG",
    slack_channel_id: "C05HJKL6MNP"
  )

  page.data&.each do |channel|
    puts channel.id
  end
  ```
</CodeGroup>

Passing a `slch_` ID as `slack_channel_id` returns `400`.

### Get a channel

`GET /v1/organizations/claude_tag/slack_channels/{id}` returns the channel object, holding what the channel stores. To read what applies in it instead, see [Read what applies in a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-what-applies-in-a-channel). Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/slch_011CZkZmRt4vNq8sHbYw2KdX" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels retrieve \
    --id slch_011CZkZmRt4vNq8sHbYw2KdX
  ```

  ```python Python
  client = anthropic.Anthropic()

  channel = client.beta.organization.claude_tag.slack_channels.retrieve(
      "slch_011CZkZmRt4vNq8sHbYw2KdX"
  )

  print(channel.settings.enabled)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channel = await client.beta.organization.claudeTag.slackChannels.retrieve(
    "slch_011CZkZmRt4vNq8sHbYw2KdX"
  );

  console.log(channel.settings.enabled);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var channel = await client.Beta.Organization.ClaudeTag.SlackChannels.Retrieve(
      "slch_011CZkZmRt4vNq8sHbYw2KdX"
  );

  Console.WriteLine(channel.Settings.Enabled);
  ```

  ```go Go
  client := anthropic.NewClient()

  channel, err := client.Beta.Organization.ClaudeTag.SlackChannels.Get(
  	context.Background(),
  	"slch_011CZkZmRt4vNq8sHbYw2KdX",
  	anthropic.BetaOrganizationClaudeTagSlackChannelGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(channel.Settings.Enabled)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var channel = client.beta().organization().claudeTag().slackChannels()
      .retrieve("slch_011CZkZmRt4vNq8sHbYw2KdX");

  IO.println(channel.settings().enabled().orElse(null));
  ```

  ```php PHP
  $client = new Client();

  $channel = $client->beta->organization->claudeTag->slackChannels->retrieve(
      id: 'slch_011CZkZmRt4vNq8sHbYw2KdX',
  );

  echo json_encode($channel->settings->enabled) . "\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel_id = "slch_011CZkZmRt4vNq8sHbYw2KdX"
  channel = client.beta.organization.claude_tag.slack_channels.retrieve(channel_id)

  puts channel.settings.enabled
  ```
</CodeGroup>

### Read what applies in a channel

The same request with `include_inherited=true` returns the channel object with `settings` holding what applies in the channel, and `sources` saying where each value comes from. [Stored and inherited values](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#stored-and-inherited-values) shows a complete response; `enabled` and `guest_policy` are never `null` in it. If a level cannot be read, the request fails with `503` rather than answer without it. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/slch_011CZkZmRt4vNq8sHbYw2KdX?include_inherited=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels retrieve \
    --id slch_011CZkZmRt4vNq8sHbYw2KdX \
    --include-inherited
  ```

  ```python Python
  client = anthropic.Anthropic()

  channel = client.beta.organization.claude_tag.slack_channels.retrieve(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      include_inherited=True,
  )

  print(channel.settings.instructions)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channel = await client.beta.organization.claudeTag.slackChannels.retrieve(
    "slch_011CZkZmRt4vNq8sHbYw2KdX",
    { include_inherited: true }
  );

  console.log(channel.settings.instructions);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var channel = await client.Beta.Organization.ClaudeTag.SlackChannels.Retrieve(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      new() { IncludeInherited = true }
  );

  Console.WriteLine(channel.Settings.Instructions);
  ```

  ```go Go
  client := anthropic.NewClient()

  channel, err := client.Beta.Organization.ClaudeTag.SlackChannels.Get(
  	context.Background(),
  	"slch_011CZkZmRt4vNq8sHbYw2KdX",
  	anthropic.BetaOrganizationClaudeTagSlackChannelGetParams{
  		IncludeInherited: anthropic.Bool(true),
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(channel.Settings.Instructions)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelRetrieveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelRetrieveParams.builder()
          .includeInherited(true)
          .build();
      var channel = client.beta().organization().claudeTag().slackChannels()
          .retrieve("slch_011CZkZmRt4vNq8sHbYw2KdX", params);

      IO.println(channel.settings().instructions().orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $channel = $client->beta->organization->claudeTag->slackChannels->retrieve(
      id: 'slch_011CZkZmRt4vNq8sHbYw2KdX',
      includeInherited: true,
  );

  echo "{$channel->settings->instructions}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel_id = "slch_011CZkZmRt4vNq8sHbYw2KdX"
  channel = client.beta.organization.claude_tag.slack_channels.retrieve(channel_id, include_inherited: true)

  puts channel.settings.instructions
  ```
</CodeGroup>

### Update a channel

`POST /v1/organizations/claude_tag/slack_channels/{id}` changes the channel's settings and returns the channel object. `settings` is required and follows [Changing settings](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#changing-settings). Requires the `write:claude_tag` scope.

Turn Claude off in one channel and leave its other settings as they are:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/slch_011CZkZmRt4vNq8sHbYw2KdX" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{"settings": {"enabled": false}}'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels update \
    --id slch_011CZkZmRt4vNq8sHbYw2KdX \
    --settings '{enabled: false}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  channel = client.beta.organization.claude_tag.slack_channels.update(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      settings={"enabled": False},
  )

  print(channel.settings.enabled)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channel = await client.beta.organization.claudeTag.slackChannels.update(
    "slch_011CZkZmRt4vNq8sHbYw2KdX",
    { settings: { enabled: false } }
  );

  console.log(channel.settings.enabled);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var channel = await client.Beta.Organization.ClaudeTag.SlackChannels.Update(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      new() { Settings = new() { Enabled = false } }
  );

  Console.WriteLine(channel.Settings.Enabled);
  ```

  ```go Go
  client := anthropic.NewClient()

  channel, err := client.Beta.Organization.ClaudeTag.SlackChannels.Update(
  	context.Background(),
  	"slch_011CZkZmRt4vNq8sHbYw2KdX",
  	anthropic.BetaOrganizationClaudeTagSlackChannelUpdateParams{
  		Settings: anthropic.BetaClaudeTagSettingsUpdateParam{
  			Enabled: anthropic.Bool(false),
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(channel.Settings.Enabled)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagSettingsUpdate;
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelUpdateParams.builder()
          .settings(BetaClaudeTagSettingsUpdate.builder()
              .enabled(false)
              .build())
          .build();
      var channel = client.beta().organization().claudeTag().slackChannels()
          .update("slch_011CZkZmRt4vNq8sHbYw2KdX", params);

      IO.println(channel.settings().enabled().orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $channel = $client->beta->organization->claudeTag->slackChannels->update(
      id: 'slch_011CZkZmRt4vNq8sHbYw2KdX',
      settings: ['enabled' => false],
  );

  echo json_encode($channel->settings->enabled) . "\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel_id = "slch_011CZkZmRt4vNq8sHbYw2KdX"
  channel = client.beta.organization.claude_tag.slack_channels.update(
    channel_id,
    settings: {enabled: false}
  )

  puts channel.settings.enabled
  ```
</CodeGroup>

Clear the channel's instructions, so that only the inherited ones apply:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/slch_011CZkZmRt4vNq8sHbYw2KdX" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{"settings": {"instructions": null}}'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels update \
    --id slch_011CZkZmRt4vNq8sHbYw2KdX \
    --settings '{instructions: null}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  channel = client.beta.organization.claude_tag.slack_channels.update(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      settings={"instructions": None},
  )

  print(channel.settings.instructions)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const channel = await client.beta.organization.claudeTag.slackChannels.update(
    "slch_011CZkZmRt4vNq8sHbYw2KdX",
    { settings: { instructions: null } }
  );

  console.log(channel.settings.instructions);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var channel = await client.Beta.Organization.ClaudeTag.SlackChannels.Update(
      "slch_011CZkZmRt4vNq8sHbYw2KdX",
      new() { Settings = new() { Instructions = null } }
  );

  Console.WriteLine(channel.Settings.Instructions);
  ```

  ```go Go
  client := anthropic.NewClient()

  channel, err := client.Beta.Organization.ClaudeTag.SlackChannels.Update(
  	context.Background(),
  	"slch_011CZkZmRt4vNq8sHbYw2KdX",
  	anthropic.BetaOrganizationClaudeTagSlackChannelUpdateParams{
  		Settings: anthropic.BetaClaudeTagSettingsUpdateParam{
  			Instructions: param.Null[string](),
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(channel.Settings.Instructions)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagSettingsUpdate;
  import com.anthropic.models.beta.organization.claudetag.slackchannels.SlackChannelUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackChannelUpdateParams.builder()
          .settings(BetaClaudeTagSettingsUpdate.builder()
              .instructions(Optional.empty())
              .build())
          .build();
      var channel = client.beta().organization().claudeTag().slackChannels()
          .update("slch_011CZkZmRt4vNq8sHbYw2KdX", params);

      IO.println(channel.settings().instructions().orElse(null));
  }
  ```

  ```php PHP
  use Anthropic\Beta\Organization\ClaudeTag\ClaudeTagSettingsUpdate;
  // ...

  $client = new Client();

  // update() drops nulls inside arrays, so build the settings object to send null.
  $channel = $client->beta->organization->claudeTag->slackChannels->update(
      id: 'slch_011CZkZmRt4vNq8sHbYw2KdX',
      settings: (new ClaudeTagSettingsUpdate())->withInstructions(null),
  );

  echo "{$channel->settings->instructions}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel_id = "slch_011CZkZmRt4vNq8sHbYw2KdX"
  channel = client.beta.organization.claude_tag.slack_channels.update(
    channel_id,
    settings: {instructions: nil}
  )

  puts channel.settings.instructions
  ```
</CodeGroup>

### Remove a channel

`DELETE /v1/organizations/claude_tag/slack_channels/{id}` removes a channel from Claude Tag. It is the removal an organization owner makes in claude.ai, with the same effect. It does not delete, archive, or change the channel in Slack, or any message in it. Requires the `write:claude_tag` scope.

<Warning>
  Removal cannot be undone. It deletes what Claude Tag holds for the channel:

  * its stored settings and its Bundle targets
  * its sessions and their transcripts, including sessions that are running
  * its memory, which is what Claude keeps about the channel from one session to the next
  * its routines and the artifacts published from it
</Warning>

**A channel can be removed only while Claude is off in it.** While `enabled` resolves to `true` for the channel, as [Read what applies in a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-what-applies-in-a-channel) returns it, the request returns `400` with `error_code: "slack_channel_enabled"`. Set `enabled` to `false` on the channel first, then send the request again. The one exception is an organization with a [restricted compliance configuration](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#error-responses): it cannot make that change, so its request removes the channel whether or not Claude is on in it. If a level that this check needs cannot be read, the request returns `503` and removes nothing.

The check guards against mistakenly removing a channel that is in use. It does not keep Claude out of the channel afterward. Removal deletes the channel's own settings, including an `enabled` of `false`, so from then on only what the channel inherits determines whether Claude is on there. If that turns Claude on, Claude answers in the channel again on its next mention, and that use sets the channel up anew: a new `id`, no settings of its own, and none of the removed channel's memory.

* To keep Claude out of a channel, keep it set up with `enabled` set to `false` rather than remove it, or make sure that what it would inherit, which removal does not touch, keeps Claude off.
* To have a channel store nothing and keep its sessions and memory, clear each setting and detach each Bundle instead.

Two kinds of channel cannot be removed here at all, whether Claude is on or off in them, and return `400` with no `error_code`: a [group direct message](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#group-direct-messages), and a channel that holds configuration this API does not manage, such as a runner pool or a setting that only claude.ai has. These are checked before `enabled` is, so turning Claude off does not help; an organization owner removes the second kind in claude.ai.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/slch_011CZkZmRt4vNq8sHbYw2KdX" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-channels delete \
    --id slch_011CZkZmRt4vNq8sHbYw2KdX
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_channel = client.beta.organization.claude_tag.slack_channels.delete(
      "slch_011CZkZmRt4vNq8sHbYw2KdX"
  )

  print(deleted_channel.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedChannel = await client.beta.organization.claudeTag.slackChannels.delete(
    "slch_011CZkZmRt4vNq8sHbYw2KdX"
  );

  console.log(deletedChannel.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedChannel = await client.Beta.Organization.ClaudeTag.SlackChannels.Delete(
      "slch_011CZkZmRt4vNq8sHbYw2KdX"
  );

  Console.WriteLine(deletedChannel.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedChannel, err := client.Beta.Organization.ClaudeTag.SlackChannels.Delete(
  	context.Background(),
  	"slch_011CZkZmRt4vNq8sHbYw2KdX",
  	anthropic.BetaOrganizationClaudeTagSlackChannelDeleteParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(deletedChannel.ID)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var deletedChannel = client.beta().organization().claudeTag().slackChannels()
      .delete("slch_011CZkZmRt4vNq8sHbYw2KdX");

  IO.println(deletedChannel.id());
  ```

  ```php PHP
  $client = new Client();

  $deletedChannel = $client->beta->organization->claudeTag->slackChannels->delete(
      id: 'slch_011CZkZmRt4vNq8sHbYw2KdX',
  );

  echo "{$deletedChannel->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  channel_id = "slch_011CZkZmRt4vNq8sHbYw2KdX"
  deleted_channel = client.beta.organization.claude_tag.slack_channels.delete(channel_id)

  puts deleted_channel.id
  ```
</CodeGroup>

```json Response
{
  "type": "slack_channel_deleted",
  "id": "slch_011CZkZmRt4vNq8sHbYw2KdX"
}
```

The `id` returns `404` as soon as the request returns, and the rest is deleted in the background. A repeated removal returns `404`, so if you resend a removal after a `503`, a `404` then means the channel is already gone.

## Slack workspaces

The workspace object describes one Slack workspace. It has the same fields as the [channel object](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#slack-channels), except that `type` is `slack_workspace`, `id` is prefixed `slws_`, and `slack` holds `workspace_id` only. The [Quick start](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#quick-start) response shows a complete one. Read with `include_inherited=true`, a workspace shows each setting as the workspace and the Slack defaults resolve it, which is what a channel of the workspace inherits unless a nearer level sets that setting.

An `id` that is not a valid `slws_` identifier returns `400`. A valid one that names no workspace of your organization returns `404`.

### List workspaces

`GET /v1/organizations/claude_tag/slack_workspaces` lists the set-up workspaces your organization owns, newest first by `created_at`. The [Quick start](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#quick-start) shows the request and the response. To find one workspace by Slack's own ID, add `slack_workspace_id`: `data` holds that workspace, or is empty when it is not set up, and a workspace your organization does not own returns `404`. A workspace it owns only through an Enterprise Grid also returns `404` until it is set up. Add `include_inherited=true` to have each workspace hold what applies in it (see [Stored and inherited values](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#stored-and-inherited-values)). Requires the `read:claude_tag` scope.

### Get a workspace

`GET /v1/organizations/claude_tag/slack_workspaces/{id}` returns the workspace object, holding what the workspace stores, or, with `include_inherited=true` in the query as in [Read what applies in a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#read-what-applies-in-a-channel), what applies in it. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces/slws_011CZkZnWa7xPc3uJfZe5LgT" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-workspaces retrieve \
    --id slws_011CZkZnWa7xPc3uJfZe5LgT
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.claude_tag.slack_workspaces.retrieve(
      "slws_011CZkZnWa7xPc3uJfZe5LgT"
  )

  print(workspace.settings.instructions)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspace = await client.beta.organization.claudeTag.slackWorkspaces.retrieve(
    "slws_011CZkZnWa7xPc3uJfZe5LgT"
  );

  console.log(workspace.settings.instructions);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var workspace = await client.Beta.Organization.ClaudeTag.SlackWorkspaces.Retrieve(
      "slws_011CZkZnWa7xPc3uJfZe5LgT"
  );

  Console.WriteLine(workspace.Settings.Instructions);
  ```

  ```go Go
  client := anthropic.NewClient()

  workspace, err := client.Beta.Organization.ClaudeTag.SlackWorkspaces.Get(
  	context.Background(),
  	"slws_011CZkZnWa7xPc3uJfZe5LgT",
  	anthropic.BetaOrganizationClaudeTagSlackWorkspaceGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(workspace.Settings.Instructions)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var workspace = client.beta().organization().claudeTag().slackWorkspaces()
      .retrieve("slws_011CZkZnWa7xPc3uJfZe5LgT");

  IO.println(workspace.settings().instructions().orElse(null));
  ```

  ```php PHP
  $client = new Client();

  $workspace = $client->beta->organization->claudeTag->slackWorkspaces->retrieve(
      id: 'slws_011CZkZnWa7xPc3uJfZe5LgT',
  );

  echo "{$workspace->settings->instructions}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "slws_011CZkZnWa7xPc3uJfZe5LgT"
  workspace = client.beta.organization.claude_tag.slack_workspaces.retrieve(workspace_id)

  puts workspace.settings.instructions
  ```
</CodeGroup>

### Update a workspace

`POST /v1/organizations/claude_tag/slack_workspaces/{id}` changes the workspace's settings and returns the workspace object. `settings` is required and follows [Changing settings](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#changing-settings). What you set here applies in every channel of the workspace that does not set its own value, except `instructions`, which every channel adds its own to rather than replaces. Requires the `write:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces/slws_011CZkZnWa7xPc3uJfZe5LgT" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{"settings": {"guest_policy": {"type": "restrict"}}}'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:slack-workspaces update \
    --id slws_011CZkZnWa7xPc3uJfZe5LgT \
    --settings '{guest_policy: {type: restrict}}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  workspace = client.beta.organization.claude_tag.slack_workspaces.update(
      "slws_011CZkZnWa7xPc3uJfZe5LgT",
      settings={"guest_policy": {"type": "restrict"}},
  )

  print(workspace.settings.guest_policy)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const workspace = await client.beta.organization.claudeTag.slackWorkspaces.update(
    "slws_011CZkZnWa7xPc3uJfZe5LgT",
    { settings: { guest_policy: { type: "restrict" } } }
  );

  console.log(workspace.settings.guest_policy?.type);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ClaudeTag;

  AnthropicClient client = new();

  var workspace = await client.Beta.Organization.ClaudeTag.SlackWorkspaces.Update(
      "slws_011CZkZnWa7xPc3uJfZe5LgT",
      new() { Settings = new() { GuestPolicy = new BetaClaudeTagGuestPolicyRestrict() } }
  );

  Console.WriteLine(workspace.Settings.GuestPolicy?.Type.Raw());
  ```

  ```go Go
  client := anthropic.NewClient()

  workspace, err := client.Beta.Organization.ClaudeTag.SlackWorkspaces.Update(
  	context.Background(),
  	"slws_011CZkZnWa7xPc3uJfZe5LgT",
  	anthropic.BetaOrganizationClaudeTagSlackWorkspaceUpdateParams{
  		Settings: anthropic.BetaClaudeTagSettingsUpdateParam{
  			GuestPolicy: anthropic.BetaClaudeTagGuestPolicyUnionParam{
  				OfRestrict: &anthropic.BetaClaudeTagGuestPolicyRestrictParam{},
  			},
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(workspace.Settings.GuestPolicy.Type)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagGuestPolicyRestrict;
  import com.anthropic.models.beta.organization.claudetag.BetaClaudeTagSettingsUpdate;
  import com.anthropic.models.beta.organization.claudetag.slackworkspaces.SlackWorkspaceUpdateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = SlackWorkspaceUpdateParams.builder()
          .settings(BetaClaudeTagSettingsUpdate.builder()
              .guestPolicy(BetaClaudeTagGuestPolicyRestrict.builder().build())
              .build())
          .build();
      var workspace = client.beta().organization().claudeTag().slackWorkspaces()
          .update("slws_011CZkZnWa7xPc3uJfZe5LgT", params);

      IO.println(workspace.settings().guestPolicy().map(policy -> policy.type().asString()).orElse(null));
  }
  ```

  ```php PHP
  $client = new Client();

  $workspace = $client->beta->organization->claudeTag->slackWorkspaces->update(
      id: 'slws_011CZkZnWa7xPc3uJfZe5LgT',
      settings: ['guestPolicy' => ['type' => 'restrict']],
  );

  echo "{$workspace->settings->guestPolicy?->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  workspace_id = "slws_011CZkZnWa7xPc3uJfZe5LgT"
  workspace = client.beta.organization.claude_tag.slack_workspaces.update(
    workspace_id,
    settings: {guest_policy: {type: :restrict}}
  )

  puts workspace.settings.guest_policy&.type
  ```
</CodeGroup>

## Bundles

A Bundle is what claude.ai calls an [Access bundle](https://claude.com/docs/claude-tag/admins/add-connections): a named set of access, such as connectors, repositories, and credentials, that Claude can use in a channel or workspace. Organization owners create, edit, and delete Bundles in claude.ai. This API lists them and attaches them. It returns a Bundle's name and description and never what the Bundle grants.

| Field                      | Description                                      |
| -------------------------- | ------------------------------------------------ |
| `type`                     | `bundle`.                                        |
| `id`                       | Prefixed `capp_`.                                |
| `display_name`             | The Bundle's name.                               |
| `description`              | What the Bundle is for. `null` when it has none. |
| `created_at`, `updated_at` | When the Bundle was created and last changed.    |

A `bundle_id` that is not a valid `capp_` identifier returns `400`. A valid one that does not exist or belongs to another organization returns `404`, whatever else the request holds. Bundles that Claude Tag manages for itself are not listed and return `404`.

### List Bundles

`GET /v1/organizations/claude_tag/bundles` lists your organization's Bundles, newest first by `created_at`. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/bundles" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles list
  ```

  ```python Python
  client = anthropic.Anthropic()

  bundles = client.beta.organization.claude_tag.bundles.list()

  # Automatically fetches more pages as needed.
  for bundle in bundles:
      print(f"{bundle.id}: {bundle.display_name}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const bundles = await client.beta.organization.claudeTag.bundles.list();

  for await (const bundle of bundles) {
    console.log(`${bundle.id}: ${bundle.display_name}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ClaudeTag.Bundles.List();

  await foreach (var bundle in page.Paginate())
  {
      Console.WriteLine($"{bundle.ID}: {bundle.DisplayName}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  bundles := client.Beta.Organization.ClaudeTag.Bundles.ListAutoPaging(
  	context.Background(),
  	anthropic.BetaOrganizationClaudeTagBundleListParams{},
  )

  for bundles.Next() {
  	bundle := bundles.Current()
  	fmt.Printf("%s: %s\n", bundle.ID, bundle.DisplayName)
  }
  if err := bundles.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var bundles = client.beta().organization().claudeTag().bundles().list();

  for (var bundle : bundles.autoPager()) {
      IO.println(bundle.id() + ": " + bundle.displayName());
  }
  ```

  ```php PHP
  $client = new Client();

  $bundles = $client->beta->organization->claudeTag->bundles->list();

  // Only this page; for the next, call list() again with page: $bundles->nextPage.
  foreach ($bundles->getItems() as $bundle) {
      echo "{$bundle->id}: {$bundle->displayName}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  page = client.beta.organization.claude_tag.bundles.list

  page.auto_paging_each do |bundle|
    puts "#{bundle.id}: #{bundle.display_name}"
  end
  ```
</CodeGroup>

```json Response
{
  "data": [
    {
      "type": "bundle",
      "id": "capp_011CZkZjLP1cWxj5EtMmdgbq",
      "display_name": "Support tools",
      "description": "Issue tracker and the support runbooks repository.",
      "created_at": "2026-09-12T08:15:30Z",
      "updated_at": "2026-09-30T13:02:47Z"
    }
  ],
  "next_page": null
}
```

### Get a Bundle

`GET /v1/organizations/claude_tag/bundles/{bundle_id}` returns the Bundle object. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles retrieve \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq
  ```

  ```python Python
  client = anthropic.Anthropic()

  bundle = client.beta.organization.claude_tag.bundles.retrieve(
      "capp_011CZkZjLP1cWxj5EtMmdgbq"
  )

  print(bundle.display_name)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const bundle = await client.beta.organization.claudeTag.bundles.retrieve(
    "capp_011CZkZjLP1cWxj5EtMmdgbq"
  );

  console.log(bundle.display_name);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var bundle = await client.Beta.Organization.ClaudeTag.Bundles.Retrieve(
      "capp_011CZkZjLP1cWxj5EtMmdgbq"
  );

  Console.WriteLine(bundle.DisplayName);
  ```

  ```go Go
  client := anthropic.NewClient()

  bundle, err := client.Beta.Organization.ClaudeTag.Bundles.Get(
  	context.Background(),
  	"capp_011CZkZjLP1cWxj5EtMmdgbq",
  	anthropic.BetaOrganizationClaudeTagBundleGetParams{},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(bundle.DisplayName)
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var bundle = client.beta().organization().claudeTag().bundles()
      .retrieve("capp_011CZkZjLP1cWxj5EtMmdgbq");

  IO.println(bundle.displayName());
  ```

  ```php PHP
  $client = new Client();

  $bundle = $client->beta->organization->claudeTag->bundles->retrieve(
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
  );

  echo "{$bundle->displayName}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  bundle = client.beta.organization.claude_tag.bundles.retrieve(bundle_id)

  puts bundle.display_name
  ```
</CodeGroup>

## Bundle targets

A Bundle target is the record of one Bundle attached to one channel or one workspace. A Bundle attached to a workspace can be used in the workspace and in every channel in it. A Bundle attached to a channel can be used in that channel only.

| Field                | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| `type`               | `slack_channel` or `slack_workspace`.                                                                   |
| `id`                 | Prefixed `btgt_`. It is the `{target_id}` in paths, and is never the channel's or workspace's own `id`. |
| `slack_channel_id`   | On a `slack_channel` target: the channel's `id`, prefixed `slch_`.                                      |
| `slack_workspace_id` | On a `slack_workspace` target: the workspace's `id`, prefixed `slws_`.                                  |
| `created_at`         | When the Bundle was attached.                                                                           |

A Bundle is attached to a channel or workspace at most once, and the same pair always has the same `id`, also after a detach and a new attach. The `id` is opaque: get it from the response to an attach or from the list. A Bundle target does not hold its Bundle's `id`, which its paths also need, so keep the two together.

Attaching or detaching changes no stored setting. Sessions that are running in the channel or workspace are told that its access changed.

The Bundle that claude.ai attaches as part of an on-call setup is listed and can be read, but cannot be attached or detached here, and nothing can be attached to or detached from a channel or workspace that an on-call setup manages. Each of those requests returns `400`.

### List a Bundle's targets

`GET /v1/organizations/claude_tag/bundles/{bundle_id}/targets` lists the channels and workspaces the Bundle is attached to, newest first by `created_at`. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq/targets" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles:targets list \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq
  ```

  ```python Python
  client = anthropic.Anthropic()

  targets = client.beta.organization.claude_tag.bundles.targets.list(
      "capp_011CZkZjLP1cWxj5EtMmdgbq"
  )

  # Automatically fetches more pages as needed.
  for target in targets:
      print(f"{target.id}: {target.type}")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const targets = await client.beta.organization.claudeTag.bundles.targets.list(
    "capp_011CZkZjLP1cWxj5EtMmdgbq"
  );

  for await (const target of targets) {
    console.log(`${target.id}: ${target.type}`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.ClaudeTag.Bundles.Targets.List(
      "capp_011CZkZjLP1cWxj5EtMmdgbq"
  );

  await foreach (var target in page.Paginate())
  {
      Console.WriteLine($"{target.ID}: {target.Type.Raw()}");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  targets := client.Beta.Organization.ClaudeTag.Bundles.Targets.ListAutoPaging(
  	context.Background(),
  	"capp_011CZkZjLP1cWxj5EtMmdgbq",
  	anthropic.BetaOrganizationClaudeTagBundleTargetListParams{},
  )

  for targets.Next() {
  	target := targets.Current()
  	fmt.Printf("%s: %s\n", target.ID, target.Type)
  }
  if err := targets.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var targets = client.beta().organization().claudeTag().bundles().targets()
      .list("capp_011CZkZjLP1cWxj5EtMmdgbq");

  for (var target : targets.autoPager()) {
      IO.println(target.id() + ": " + target.type().asString());
  }
  ```

  ```php PHP
  $client = new Client();

  $targets = $client->beta->organization->claudeTag->bundles->targets->list(
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
  );

  // Only this page; for the next, call list() again with page: $targets->nextPage.
  foreach ($targets->getItems() as $target) {
      echo "{$target->id}: {$target->type}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  page = client.beta.organization.claude_tag.bundles.targets.list(bundle_id)

  page.auto_paging_each do |target|
    puts "#{target.id}: #{target.type}"
  end
  ```
</CodeGroup>

```json Response
{
  "data": [
    {
      "type": "slack_channel",
      "id": "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
      "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX",
      "created_at": "2026-10-19T16:21:44Z"
    },
    {
      "type": "slack_workspace",
      "id": "btgt_011CZkZuMc3dVk7xQpGw9StZ1CZkZxRe6gTk9uNyVs4adJ",
      "slack_workspace_id": "slws_011CZkZnWa7xPc3uJfZe5LgT",
      "created_at": "2026-09-12T08:17:02Z"
    }
  ],
  "next_page": null
}
```

Only attachments to channels and workspaces are listed. A Bundle that is attached in claude.ai to anything else, such as **Default Slack access**, has no Bundle target for it, and neither does a rule that applies a Bundle in many channels at once. So the Bundles Claude can use in a channel can be more than the targets that name it. No endpoint lists the Bundles attached to one channel or workspace.

### Attach a Bundle

`POST /v1/organizations/claude_tag/bundles/{bundle_id}/targets` attaches the Bundle and returns the Bundle target. The body names the `type` and the matching `id`. The channel or workspace must already be set up: attaching never sets a channel up. Attaching a pair that is already attached returns `200` with the existing Bundle target. Requires the `write:claude_tag` scope.

Attach a Bundle to a channel:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq/targets" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{
      "type": "slack_channel",
      "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX"
    }'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles:targets create \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq \
    --target '{type: slack_channel, slack_channel_id: slch_011CZkZmRt4vNq8sHbYw2KdX}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  target = client.beta.organization.claude_tag.bundles.targets.create(
      "capp_011CZkZjLP1cWxj5EtMmdgbq",
      target={
          "type": "slack_channel",
          "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX",
      },
  )

  print(target.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const target = await client.beta.organization.claudeTag.bundles.targets.create(
    "capp_011CZkZjLP1cWxj5EtMmdgbq",
    { target: { type: "slack_channel", slack_channel_id: "slch_011CZkZmRt4vNq8sHbYw2KdX" } }
  );

  console.log(target.id);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ClaudeTag.Bundles.Targets;

  AnthropicClient client = new();

  var target = await client.Beta.Organization.ClaudeTag.Bundles.Targets.Create(
      "capp_011CZkZjLP1cWxj5EtMmdgbq",
      new()
      {
          Target = new BetaClaudeTagSlackChannelBundleTargetCreate
          {
              SlackChannelID = "slch_011CZkZmRt4vNq8sHbYw2KdX",
          },
      }
  );

  Console.WriteLine(target.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  target, err := client.Beta.Organization.ClaudeTag.Bundles.Targets.New(
  	context.Background(),
  	"capp_011CZkZjLP1cWxj5EtMmdgbq",
  	anthropic.BetaOrganizationClaudeTagBundleTargetNewParams{
  		Target: anthropic.BetaClaudeTagBundleTargetCreateUnionParam{
  			OfSlackChannel: &anthropic.BetaClaudeTagSlackChannelBundleTargetCreateParam{
  				SlackChannelID: "slch_011CZkZmRt4vNq8sHbYw2KdX",
  			},
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(target.ID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.bundles.targets.TargetCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = TargetCreateParams.builder()
          .slackChannelTarget("slch_011CZkZmRt4vNq8sHbYw2KdX")
          .build();
      var target = client.beta().organization().claudeTag().bundles().targets()
          .create("capp_011CZkZjLP1cWxj5EtMmdgbq", params);

      IO.println(target.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $target = $client->beta->organization->claudeTag->bundles->targets->create(
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
      target: [
          'type' => 'slack_channel',
          'slackChannelID' => 'slch_011CZkZmRt4vNq8sHbYw2KdX',
      ],
  );

  echo "{$target->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  target = client.beta.organization.claude_tag.bundles.targets.create(
    bundle_id,
    target: {
      type: :slack_channel,
      slack_channel_id: "slch_011CZkZmRt4vNq8sHbYw2KdX"
    }
  )

  puts target.id
  ```
</CodeGroup>

```json Response
{
  "type": "slack_channel",
  "id": "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
  "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX",
  "created_at": "2026-10-19T16:21:44Z"
}
```

Attach a Bundle to a workspace:

<CodeGroup>
  ```bash cURL
  curl -X POST "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq/targets" \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21" \
    -d '{
      "type": "slack_workspace",
      "slack_workspace_id": "slws_011CZkZnWa7xPc3uJfZe5LgT"
    }'
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles:targets create \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq \
    --target '{type: slack_workspace, slack_workspace_id: slws_011CZkZnWa7xPc3uJfZe5LgT}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  target = client.beta.organization.claude_tag.bundles.targets.create(
      "capp_011CZkZjLP1cWxj5EtMmdgbq",
      target={
          "type": "slack_workspace",
          "slack_workspace_id": "slws_011CZkZnWa7xPc3uJfZe5LgT",
      },
  )

  print(target.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const target = await client.beta.organization.claudeTag.bundles.targets.create(
    "capp_011CZkZjLP1cWxj5EtMmdgbq",
    { target: { type: "slack_workspace", slack_workspace_id: "slws_011CZkZnWa7xPc3uJfZe5LgT" } }
  );

  console.log(target.id);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.ClaudeTag.Bundles.Targets;

  AnthropicClient client = new();

  var target = await client.Beta.Organization.ClaudeTag.Bundles.Targets.Create(
      "capp_011CZkZjLP1cWxj5EtMmdgbq",
      new()
      {
          Target = new BetaClaudeTagSlackWorkspaceBundleTargetCreate
          {
              SlackWorkspaceID = "slws_011CZkZnWa7xPc3uJfZe5LgT",
          },
      }
  );

  Console.WriteLine(target.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  target, err := client.Beta.Organization.ClaudeTag.Bundles.Targets.New(
  	context.Background(),
  	"capp_011CZkZjLP1cWxj5EtMmdgbq",
  	anthropic.BetaOrganizationClaudeTagBundleTargetNewParams{
  		Target: anthropic.BetaClaudeTagBundleTargetCreateUnionParam{
  			OfSlackWorkspace: &anthropic.BetaClaudeTagSlackWorkspaceBundleTargetCreateParam{
  				SlackWorkspaceID: "slws_011CZkZnWa7xPc3uJfZe5LgT",
  			},
  		},
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(target.ID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.bundles.targets.TargetCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = TargetCreateParams.builder()
          .slackWorkspaceTarget("slws_011CZkZnWa7xPc3uJfZe5LgT")
          .build();
      var target = client.beta().organization().claudeTag().bundles().targets()
          .create("capp_011CZkZjLP1cWxj5EtMmdgbq", params);

      IO.println(target.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $target = $client->beta->organization->claudeTag->bundles->targets->create(
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
      target: [
          'type' => 'slack_workspace',
          'slackWorkspaceID' => 'slws_011CZkZnWa7xPc3uJfZe5LgT',
      ],
  );

  echo "{$target->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  target = client.beta.organization.claude_tag.bundles.targets.create(
    bundle_id,
    target: {
      type: :slack_workspace,
      slack_workspace_id: "slws_011CZkZnWa7xPc3uJfZe5LgT"
    }
  )

  puts target.id
  ```
</CodeGroup>

An attachment to a channel has conditions under which it applies, such as only while no Slack guest is in the channel. Conditions are set in claude.ai and are not returned here. Attaching through this API uses the default conditions, and attaching a pair that is already attached leaves its conditions unchanged.

### Get a Bundle target

`GET /v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}` returns the Bundle target. A `target_id` that is not a valid `btgt_` identifier returns `400`. A valid one that belongs to another Bundle, was detached, or names a channel or workspace that is no longer set up returns `404`. Requires the `read:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq/targets/btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles:targets retrieve \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq \
    --target-id btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH
  ```

  ```python Python
  client = anthropic.Anthropic()

  target = client.beta.organization.claude_tag.bundles.targets.retrieve(
      "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
      bundle_id="capp_011CZkZjLP1cWxj5EtMmdgbq",
  )

  print(target.type)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const target = await client.beta.organization.claudeTag.bundles.targets.retrieve(
    "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
    { bundle_id: "capp_011CZkZjLP1cWxj5EtMmdgbq" }
  );

  console.log(target.type);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var target = await client.Beta.Organization.ClaudeTag.Bundles.Targets.Retrieve(
      "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
      new() { BundleID = "capp_011CZkZjLP1cWxj5EtMmdgbq" }
  );

  Console.WriteLine(target.Type.Raw());
  ```

  ```go Go
  client := anthropic.NewClient()

  target, err := client.Beta.Organization.ClaudeTag.Bundles.Targets.Get(
  	context.Background(),
  	"btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
  	anthropic.BetaOrganizationClaudeTagBundleTargetGetParams{
  		BundleID: "capp_011CZkZjLP1cWxj5EtMmdgbq",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(target.Type)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.bundles.targets.TargetRetrieveParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = TargetRetrieveParams.builder()
          .bundleId("capp_011CZkZjLP1cWxj5EtMmdgbq")
          .build();
      var target = client.beta().organization().claudeTag().bundles().targets()
          .retrieve("btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH", params);

      IO.println(target.type().asString());
  }
  ```

  ```php PHP
  $client = new Client();

  $target = $client->beta->organization->claudeTag->bundles->targets->retrieve(
      targetID: 'btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH',
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
  );

  echo "{$target->type}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  target_id = "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH"
  target = client.beta.organization.claude_tag.bundles.targets.retrieve(
    target_id,
    bundle_id: bundle_id
  )

  puts target.type
  ```
</CodeGroup>

### Detach a Bundle

`DELETE /v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}` detaches the Bundle. A repeated detach returns `404`, so after a `503`, a resent detach that returns `404` means the Bundle target is already gone. Requires the `write:claude_tag` scope.

<CodeGroup>
  ```bash cURL
  curl -X DELETE "https://api.anthropic.com/v1/organizations/claude_tag/bundles/capp_011CZkZjLP1cWxj5EtMmdgbq/targets/btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: experimental-claude-tag-2026-10-21"
  ```

  ```bash CLI
  ant beta:organization:claude-tag:bundles:targets delete \
    --bundle-id capp_011CZkZjLP1cWxj5EtMmdgbq \
    --target-id btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH
  ```

  ```python Python
  client = anthropic.Anthropic()

  deleted_target = client.beta.organization.claude_tag.bundles.targets.delete(
      "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
      bundle_id="capp_011CZkZjLP1cWxj5EtMmdgbq",
  )

  print(deleted_target.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const deletedTarget = await client.beta.organization.claudeTag.bundles.targets.delete(
    "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
    { bundle_id: "capp_011CZkZjLP1cWxj5EtMmdgbq" }
  );

  console.log(deletedTarget.id);
  ```

  ```csharp C#
  AnthropicClient client = new();

  var deletedTarget = await client.Beta.Organization.ClaudeTag.Bundles.Targets.Delete(
      "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
      new() { BundleID = "capp_011CZkZjLP1cWxj5EtMmdgbq" }
  );

  Console.WriteLine(deletedTarget.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  deletedTarget, err := client.Beta.Organization.ClaudeTag.Bundles.Targets.Delete(
  	context.Background(),
  	"btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH",
  	anthropic.BetaOrganizationClaudeTagBundleTargetDeleteParams{
  		BundleID: "capp_011CZkZjLP1cWxj5EtMmdgbq",
  	},
  )
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(deletedTarget.ID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.claudetag.bundles.targets.TargetDeleteParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = TargetDeleteParams.builder()
          .bundleId("capp_011CZkZjLP1cWxj5EtMmdgbq")
          .build();
      var deletedTarget = client.beta().organization().claudeTag().bundles().targets()
          .delete("btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH", params);

      IO.println(deletedTarget.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $deletedTarget = $client->beta->organization->claudeTag->bundles->targets->delete(
      targetID: 'btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH',
      bundleID: 'capp_011CZkZjLP1cWxj5EtMmdgbq',
  );

  echo "{$deletedTarget->id}\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  bundle_id = "capp_011CZkZjLP1cWxj5EtMmdgbq"
  target_id = "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH"
  deleted_target = client.beta.organization.claude_tag.bundles.targets.delete(
    target_id,
    bundle_id: bundle_id
  )

  puts deleted_target.id
  ```
</CodeGroup>

```json Response
{
  "type": "bundle_target_deleted",
  "id": "btgt_011CZkZpBv9yQd6wKhAr8MnU1CZkZwPd5fSj8tMxUr3ZcH"
}
```

## Unrecognized values

`guest_policy.type`, a source's `type`, a Bundle target's `type`, and error codes may gain new values at any time. Treat a value you do not recognize as you would any unknown string rather than failing.

## Rate limiting

Requests are limited for each organization, in two budgets that all of your organization's keys share and that are separate from your organization's other Admin API limits. Each budget allows a burst and then refills at a steady rate:

| Budget  | Requests                  | Burst | Refill       |
| ------- | ------------------------- | ----- | ------------ |
| Reads   | Every `GET`               | 120   | 2 per second |
| Changes | Every `POST` and `DELETE` | 60    | 1 per second |

Requests over a budget return **429 Too Many Requests** with a `retry-after` header: wait that many seconds, then send the request again. A request that got as far as its budget, whatever its outcome, gets the `anthropic-ratelimit-requests-limit`, `anthropic-ratelimit-requests-remaining`, and `anthropic-ratelimit-requests-reset` headers for that budget; a request refused before that, such as for its key, scope, or headers, or because the API, changes, or new storage are not enabled for your organization, gets none.

## Pagination

List endpoints use an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor; pass the cursor unchanged as the `page` parameter on the next request, with the other query parameters unchanged, and repeat until `next_page` is `null`. A cursor sent with the other value of `include_inherited` than the request that returned it returns `400`. Treat the cursor string as opaque: don't parse, modify, or construct it yourself. [List channels](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-channels) can return a page with fewer than `limit` channels, or none, while `next_page` is still set, so keep requesting pages until `next_page` is `null`. The Python, TypeScript, C#, Go, Java, and Ruby SDKs' list iterators and the CLI (except with `--format raw`) do that for you. In PHP and curl, request each page yourself and pass its `next_page` as `page`.

`limit` defaults to 20, with a minimum of 1 and a maximum of 100; a value outside that range returns `400` on every list. Every list is ordered newest first by `created_at`, and takes no other order.

## Error responses

Error responses follow the standard shape documented in [Claude API errors](https://platform.claude.com/docs/en/api/errors). Quote the `request_id` from the response body when contacting support.

| Status | Meaning                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400    | Invalid input, or the operation does not apply to this channel, workspace, or Bundle (see each endpoint's section).                                                                                                                                                                                                                                                                                       |
| 401    | Missing `x-api-key` header, or the key is not recognized.                                                                                                                                                                                                                                                                                                                                                 |
| 403    | The key is not an organization-level scoped key, is missing the required scope, or your organization cannot make this change.                                                                                                                                                                                                                                                                             |
| 404    | Resource not found, or not your organization's. Also returned when the request omits the `anthropic-beta` value, or the API is not enabled for your organization, so that the endpoints read as nonexistent.                                                                                                                                                                                              |
| 409    | Something else changed or removed the resource while the request ran. Nothing the request asked for was done: no setting stored, nothing attached, detached, or removed. The one exception is a setup request, which can have set the channel up before its `settings` met the conflict (`slack_channel_set_up_settings_conflict`). Read the resource again and resend the request if it is still needed. |
| 429    | Rate limit exceeded. See [Rate limiting](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#rate-limiting).                                                                                                                                                                                                                                                                                 |
| 500    | Internal error.                                                                                                                                                                                                                                                                                                                                                                                           |
| 503    | Temporary. On a change, it does not say whether the change was stored. Every change is safe to repeat, so send the request again unchanged. If a resent `DELETE` then returns `404`, the channel or Bundle target is already gone.                                                                                                                                                                        |

When one status has several causes that you would handle differently, the error also carries `error.details.error_code`:

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "...",
    "details": {
      "error_code": "slack_channel_set_up_settings_refused",
      "slack_channel_id": "slch_011CZkZmRt4vNq8sHbYw2KdX"
    }
  },
  "request_id": "req_018EeWyXxfu5pfWkrYcMdjWG"
}
```

| `error_code`                                 | Status | Meaning and what to do                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_level_scoped_api_key_required` | 403    | The credential is not a scoped Admin API key that belongs to the organization as a whole. Ask your primary owner for one.                                                                                                                                                                                                                                                                                                                       |
| `api_key_scope_missing`                      | 403    | The key lacks `read:claude_tag` or `write:claude_tag`, whichever the endpoint requires.                                                                                                                                                                                                                                                                                                                                                         |
| `claude_tag_writes_not_enabled`              | 403    | Your organization can read through this API but is not enabled for changes.                                                                                                                                                                                                                                                                                                                                                                     |
| `compliance_configuration_restricted`        | 403    | Your organization has a compliance configuration under which Claude Tag stores nothing new, such as zero data retention. Setting a channel up, updating settings (even to clear them), and attaching a Bundle are refused. Detaching a Bundle and removing a channel are not, and such an organization can [remove](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#remove-a-channel) a channel even while Claude is on in it. |
| `environment_not_found`                      | 404    | `environment_id` names no environment your organization can use here. The `id` in the path is fine.                                                                                                                                                                                                                                                                                                                                             |
| `environment_archived`                       | 400    | `environment_id` names an archived environment.                                                                                                                                                                                                                                                                                                                                                                                                 |
| `slack_channel_set_up_settings_refused`      | 400    | The request set the channel up, then `settings` was refused. `details.slack_channel_id` is the channel. See [Set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel).                                                                                                                                                                                                                              |
| `slack_channel_set_up_environment_not_found` | 404    | The request set the channel up, then `environment_id` was not found. `details.slack_channel_id` is the channel. See [Set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel).                                                                                                                                                                                                                      |
| `slack_channel_set_up_settings_conflict`     | 409    | The request set the channel up, then another change overlapped `settings`. Nothing of `settings` was stored. `details.slack_channel_id` is the channel. See [Set up a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#set-up-a-channel).                                                                                                                                                                              |
| `slack_channel_enabled`                      | 400    | Claude is on in the channel (`enabled` resolves to `true`), so it cannot be removed. Set `enabled` to `false` first. See [Remove a channel](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#remove-a-channel).                                                                                                                                                                                                                 |

New codes may be added. Treat a code you do not recognize the way you treat its status. A `404` with no `error_code` has one of two causes. Either something the request names was not found (an `id` in the path, or a Slack channel or workspace in the body or the query), or every endpoint reads as nonexistent because the request omits the `anthropic-beta` value or the API is not enabled for your organization. To tell them apart, [list your workspaces](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#list-workspaces) with the same key and headers: that request names nothing, so it returns `404` only in the second case.

## Activity Feed events

Every change through this API is recorded on your organization's [Compliance API Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed), attributed to the API key as an `api_actor` carrying its `apikey_` ID. The events are the ones the feed records when the same change is made in claude.ai, so one query finds a change whichever way it was made.

| Event                             | Emitted when                                                                        |
| --------------------------------- | ----------------------------------------------------------------------------------- |
| `ccr_agent_created`               | A channel is set up.                                                                |
| `ccr_agent_updated`               | A setting changes on a channel or a workspace.                                      |
| `ccr_agent_deleted`               | A channel is removed. Its Bundle targets go with it and emit no event of their own. |
| `ccr_agent_proxy_profile_bound`   | A Bundle is attached.                                                               |
| `ccr_agent_proxy_profile_unbound` | A Bundle is detached.                                                               |

The events name a channel or workspace by an identifier of the feed's own, `agent_id` (prefixed `cagt_`), which no response of this API holds, so you cannot yet match an event to a channel's or workspace's `id`. The two Bundle events name the Bundle in `profile_id` and the channel or workspace, by the same `agent_id`, in `scope_id`.

A `ccr_agent_updated` event lists what changed in `updated_fields`, under the feed's own names:

| Setting          | Name in `updated_fields` |
| ---------------- | ------------------------ |
| `enabled`        | `slackbot_version`       |
| `instructions`   | `system_prompt_addendum` |
| `model`          | `default_model`          |
| `environment_id` | `default_environment_id` |
| `guest_policy`   | `guest_policy`           |

`updated_fields` can also hold `is_virtual`, which names no setting. It appears beside the names of the changed settings in the event for a change through this API that is the first thing anyone stores on the channel or workspace: a channel that Claude's first use set up, or that this API set up with no `settings`, or a workspace in which Claude was never used, and on which nobody has yet stored a setting or attached a Bundle, here or in claude.ai. The `model` a code channel starts with does not count as stored. Attaching a Bundle records only `ccr_agent_proxy_profile_bound`.

Reads, requests that change nothing, and requests that are refused before anything is stored record nothing. A setup request that sets a channel up and whose `settings` is then refused records `ccr_agent_created`.

## See also

<CardGroup cols={2}>
  <Card title="Create an Admin API key" href="https://platform.claude.com/docs/en/manage-claude/admin-api-keys">
    Where your primary owner creates a scoped key.
  </Card>

  <Card title="Claude Tag documentation" href="https://claude.com/docs/claude-tag/overview">
    What Claude Tag is, how to set it up, and what each setting does in Slack.
  </Card>

  <Card title="Compliance API Activity Feed" href="https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed">
    The audit trail of every change made here and in claude.ai.
  </Card>

  <Card title="Plugins API" href="https://platform.claude.com/docs/en/manage-claude/plugins-api">
    Manage the plugins in your Claude Enterprise organization.
  </Card>
</CardGroup>
