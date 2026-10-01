---
title: Plugins
url: https://platform.claude.com/docs/en/api/beta/organization/plugins
---

# Plugins

## Create Plugin

**POST** `/v1/organizations/plugins`

Create an organization-owned Plugin and its first version by uploading the
version's files.

The upload is `multipart/form-data`: the version's files (`files`, each part sent
as `files[]`), with an optional `marketplace_id` and `release_notes`. The manifest's `name` becomes the
Plugin's `name`, and `display_name`, `description` and `manifest_version` come
from the manifest too.

`name` may contain lowercase letters (from any alphabet), digits, and hyphens, up
to 64 characters. Uppercase letters, spaces, underscores, and other punctuation are
rejected.

The `name` must be unique within the marketplace: a name already taken
returns a 409 with `error_code` `plugin_name_taken` and, when a Plugin holds it,
that Plugin's ID in `details.plugin_id`. A Plugin going into the organization's
library marketplace is also refused with a 409 when one of its skills has the name of
an organization skill (a skill an administrator uploaded for the whole organization
in claude.ai): `error_code` `skill_name_taken`, with that name in
`details.skill_name`; rename the skill, or remove the organization skill in
claude.ai. A 503 with `error_code`
`registration_pending` means the Plugin and its version were stored (their IDs are
in `details`) but are not yet usable in claude.ai: do not retry the create (the
retry would return `plugin_name_taken`); create a version on the stored Plugin
instead, which completes it.

For a worked example, see [Create a plugin](/docs/en/manage-claude/plugins-api#create-a-plugin)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

### Body parameters (form-data)

- `files: array of string`

  The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `marketplace_id: optional string`

  ID of the organization-owned plugin marketplace to create the Plugin in (prefixed `marketplace_`). It must be a `manual` marketplace, one whose Plugins are uploaded rather than synchronized from a repository. When omitted, the Plugin is created in the organization's library marketplace, an organization-owned `manual` marketplace created on first use.

- `release_notes: optional string`

  Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

### Returns

- `BetaPlugin object`

  - `type: "plugin"`

    Always `plugin`.

    default: plugin

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent or null`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who created the Plugin; null when no creator is recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The served version's description.

  - `display_name: string or null`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string or null`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required" or null`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean or null`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `BetaPluginOwnerOrganization object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `BetaPluginOwnerUser object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F 'files[]=@/path/to/file'
```

#### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

## Get Plugin

**GET** `/v1/organizations/plugins/{plugin_id}`

Retrieve a Plugin by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

### Query parameters

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

### Returns

- `BetaPlugin object`

  - `type: "plugin"`

    Always `plugin`.

    default: plugin

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent or null`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who created the Plugin; null when no creator is recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The served version's description.

  - `display_name: string or null`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string or null`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required" or null`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean or null`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `BetaPluginOwnerOrganization object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `BetaPluginOwnerUser object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

## Update Plugin

**POST** `/v1/organizations/plugins/{plugin_id}`

Change which stored version of an organization-owned Plugin is served to members,
for example to roll back to an earlier one. This pins the served version: later
uploads are stored but no longer change what is served, and pinning cannot currently
be undone, here or in claude.ai.

Pass the version as `served_version_id`: an earlier one to roll back, a later one to
start serving a version that was stored without being served, or the one already
served to pin it without changing what is served. No new version is created.

When the organization has content scanning enabled, a version whose scan is still
running is refused with a 409 (`error_code` `scan_pending`; retry once the scan
finishes) and one whose scan failed, errored or reached no verdict with a 400
(`scan_failed`; a `warn` is accepted). When the Plugin is in the organization's
library marketplace, a version other than the one served is also refused with a 409
when one of its skills has a name that an organization skill (one an administrator
uploaded for the whole organization in claude.ai) has since taken: `error_code`
`skill_name_taken`, with that name in `details.skill_name`. A member-owned Plugin
cannot be updated here (403).

This endpoint does not write installation settings; they are written at
`/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

### Body parameters

- `served_version_id: string`

  Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

### Returns

- `BetaPlugin object`

  - `type: "plugin"`

    Always `plugin`.

    default: plugin

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent or null`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who created the Plugin; null when no creator is recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The served version's description.

  - `display_name: string or null`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string or null`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required" or null`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean or null`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `BetaPluginOwnerOrganization object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `BetaPluginOwnerUser object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "served_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8"
        }'
```

#### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

## List Plugins

**GET** `/v1/organizations/plugins`

List the Plugins created under the organization, newest first: those in the
organization's own plugin marketplaces and those in members' personal plugin
marketplaces.

Plugins in members' personal marketplaces are listed with the same detail as the
organization's own, and their files can be downloaded through the version archive
endpoint, which records each such download on the Compliance API activity feed.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

### Query parameters

- `"created_at[gt]": optional string`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `"created_at[gte]": optional string`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `"created_at[lt]": optional string`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `"created_at[lte]": optional string`

  RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  default: 20, minimum: 1, maximum: 100

- `marketplace_id: optional string`

  Only Plugins in this plugin marketplace (prefixed `marketplace_`).

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `owner_type: optional "organization" or "user"`

  `organization` for Plugins in the organization's plugin marketplaces, `user` for Plugins in members' personal plugin marketplaces.

  - `"organization"`

  - `"user"`

- `owner_user_id: optional string`

  Only Plugins in this member's personal plugin marketplaces (prefixed `user_`); a removed member's ID is accepted.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

### Returns

- `data: array of BetaPlugin`

  - `type: "plugin"`

    Always `plugin`.

    default: plugin

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent or null`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who created the Plugin; null when no creator is recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The served version's description.

  - `display_name: string or null`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string or null`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required" or null`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean or null`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `BetaPluginOwnerOrganization object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `BetaPluginOwnerUser object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data. A page may hold fewer than `limit` Plugins, even none, while this is set; keep following it until it is null.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "manifest_version": "1.2.0",
      "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
      "name": "code-review-helper",
      "organization_installation_preference": "available",
      "organization_installation_preference_inherited": true,
      "owner": {
        "type": "organization"
      },
      "reach": "contained",
      "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
      "served_version_pinned": true,
      "type": "plugin",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

## Delete Plugin

**DELETE** `/v1/organizations/plugins/{plugin_id}`

Permanently delete a Plugin and every version it holds, exactly as when an
administrator deletes it in claude.ai. The Plugin may belong to the organization or
to a member, including a member who has since left the organization.

An organization-owned Plugin's installation settings go with it; a member-owned
Plugin's shares are withdrawn and its owner no longer has it.

To take an organization-owned Plugin out of use reversibly, set its
organization-wide installation setting to `not_available` instead (and
remove or change any group settings, which override it for their members). Only a
Plugin in a `manual` marketplace can be deleted here; one synchronized from a
repository is removed by removing it from the repository (400).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

### Returns

- `BetaDeletedPlugin object`

  - `type: "plugin_deleted"`

    Always `plugin_deleted`.

    default: plugin_deleted

  - `id: string`

    The deleted Plugin's ID.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "type": "plugin_deleted"
}
```

## Domain types

### Beta Deleted Plugin

- `BetaDeletedPlugin object`

  - `type: "plugin_deleted"`

    Always `plugin_deleted`.

    default: plugin_deleted

  - `id: string`

    The deleted Plugin's ID.

### Beta Plugin

- `BetaPlugin object`

  - `type: "plugin"`

    Always `plugin`.

    default: plugin

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent or null`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who created the Plugin; null when no creator is recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The served version's description.

  - `display_name: string or null`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string or null`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required" or null`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean or null`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `BetaPluginOwnerOrganization object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `BetaPluginOwnerUser object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

### Beta Plugin API Actor

- `BetaPluginAPIActor object`

  - `type: "api_actor"`

    An Admin API key, in the same form the Compliance API activity feed uses for it.

    default: api_actor

  - `api_key_id: string`

    The key's ID.

### Beta Plugin Component

- `BetaPluginComponent object`

  - `type: "agent" or "cli" or "command" or 3 more`

    The kind of component.

    - `"agent"`

    - `"cli"`

    - `"command"`

    - `"hook"`

    - `"mcp_server"`

    - `"skill"`

  - `description: string or null`

    What the component declares about itself; always null for MCP servers, hooks, and CLIs.

  - `name: string`

    The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

### Beta Plugin Content Scan

- `BetaPluginContentScan object`

  - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

    The scan's verdict; set only when `status` is `completed`.

    - `"fail"`

    - `"pass"`

    - `"unknown"`

    - `"warn"`

  - `reason: string or null`

    The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

  - `status: "completed" or "errored" or "processing"`

    `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

    - `"completed"`

    - `"errored"`

    - `"processing"`

### Beta Plugin Owner Organization

- `BetaPluginOwnerOrganization object`

  - `type: "organization"`

    The Plugin lives in a plugin marketplace the organization owns.

    default: organization

### Beta Plugin Owner User

- `BetaPluginOwnerUser object`

  - `type: "user"`

    The Plugin lives in one member's personal plugin marketplace.

    default: user

  - `user_id: string`

    The member's User ID.

### Beta Plugin Target Organization

- `BetaPluginTargetOrganization object`

  - `type: "organization"`

    Every member of the organization.

    default: organization

### Beta Plugin Target Organization Member

- `BetaPluginTargetOrganizationMember object`

  - `type: "organization_member"`

    One member of the organization.

    default: organization_member

  - `user_id: string`

    The member's User ID.

### Beta Plugin Target RBAC Group

- `BetaPluginTargetRBACGroup object`

  - `type: "rbac_group"`

    An RBAC Group.

    default: rbac_group

  - `rbac_group_id: string`

    The RBAC Group's ID.

### Beta Plugin User Actor

- `BetaPluginUserActor object`

  - `type: "user_actor"`

    A member of the organization.

    default: user_actor

  - `email_address: string or null`

    The member's email address; may be null, for example when they are no longer a member of the organization.

  - `user_id: string`

    The member's User ID.

## Plugins › Versions

### Create Plugin Version

**POST** `/v1/organizations/plugins/{plugin_id}/versions`

Add a version to an organization-owned Plugin by uploading the new version's
files; it becomes the version served to members unless the Plugin's served version
has been pinned.

The upload is the same `multipart/form-data` as creating a Plugin: the version's
files (`files`, each part sent as `files[]`) and optional `release_notes`. The uploaded manifest's `name`
must equal the Plugin's `name`. Returns the stored version; read the Plugin back to
see which version it serves.

Only a Plugin in a `manual` marketplace takes uploads; a Plugin synchronized from
a repository gets its versions from the repository. When the Plugin is in the
organization's library marketplace, a version that adds a skill with the name of an
organization skill (a skill an administrator uploaded for the whole organization in
claude.ai) is refused with a 409: `error_code` `skill_name_taken`, with that name in
`details.skill_name`. A 503 with `error_code`
`registration_pending` means the version was stored but is not yet usable; a later
version create on the Plugin completes it.

For a worked example, see [Create a version](/docs/en/manage-claude/plugins-api#create-a-version)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Body parameters (form-data)

- `files: array of string`

  The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `release_notes: optional string`

  Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

#### Returns

- `BetaPluginVersion object`

  - `type: "plugin_version"`

    Always `plugin_version`.

    default: plugin_version

  - `id: string`

    The version's ID.

  - `components: array of BetaPluginComponent or null`

    What the version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    This version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who uploaded this version; null when not recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The manifest's description; null when it declares none.

  - `display_name: string or null`

    The manifest's display name; null when it declares none.

  - `manifest_version: string or null`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: string`

    The Plugin's ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `release_notes: string or null`

    As supplied with the upload; null when none were supplied.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/versions \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F 'files[]=@/path/to/file'
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### List Plugin Versions

**GET** `/v1/organizations/plugins/{plugin_id}/versions`

List a Plugin's versions, newest first.

The first item of the first page is the version the Plugin's `latest_version_id`
refers to.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Returns

- `data: array of BetaPluginVersion`

  - `type: "plugin_version"`

    Always `plugin_version`.

    default: plugin_version

  - `id: string`

    The version's ID.

  - `components: array of BetaPluginComponent or null`

    What the version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    This version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who uploaded this version; null when not recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The manifest's description; null when it declares none.

  - `display_name: string or null`

    The manifest's display name; null when it declares none.

  - `manifest_version: string or null`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: string`

    The Plugin's ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `release_notes: string or null`

    As supplied with the upload; null when none were supplied.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "manifest_version": "1.2.0",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "reach": "contained",
      "release_notes": "Adds a review checklist for database migrations.",
      "type": "plugin_version"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Get Plugin Version

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}`

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

- `version: string`

  ID of the Plugin Version (prefixed `pluginver_`), or `latest` for the newest one.

#### Query parameters

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Returns

- `BetaPluginVersion object`

  - `type: "plugin_version"`

    Always `plugin_version`.

    default: plugin_version

  - `id: string`

    The version's ID.

  - `components: array of BetaPluginComponent or null`

    What the version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string or null`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: BetaPluginContentScan or null`

    This version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn" or null`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor or null`

    Who uploaded this version; null when not recorded.

    - `BetaPluginUserActor object`

      - `type: "user_actor"`

        A member of the organization.

        default: user_actor

      - `email_address: string or null`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `BetaPluginAPIActor object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `api_key_id: string`

        The key's ID.

  - `description: string or null`

    The manifest's description; null when it declares none.

  - `display_name: string or null`

    The manifest's display name; null when it declares none.

  - `manifest_version: string or null`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: string`

    The Plugin's ID.

  - `reach: "contained" or "privileged" or "remote" or null`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `release_notes: string or null`

    As supplied with the upload; null when none were supplied.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/versions/$VERSION \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### Download Plugin Version Archive

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}/content`

Download one version's `.zip` archive, exactly as stored. Each download of a
Plugin from a member's personal plugin marketplace is recorded on the Compliance API
activity feed.

The response body is the archive (`Content-Type: application/zip`), sent as an
attachment whose filename is derived from the Plugin's name; name saved files from
the IDs in the request path, since that filename is not unique.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every read scope above (`read:plugins`, `read:org_audit`, and
`read:compliance_org_data`) can download the files of plugins in members' personal
marketplaces, including files that claude.ai's admin settings do not show, and a
`read:org_audit` or `read:compliance_org_data` key created for all of your parent
organization's linked organizations can do this in any organization under it that has
access to this API, by passing `organization_id`. Each such download records a
`claude_plugin_archive_accessed` event on the Compliance API activity feed,
identifying the key, the plugin, the version, and the member. Downloads of
organization-owned plugins are not recorded.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

- `version: string`

  ID of the Plugin Version (prefixed `pluginver_`). `latest` is not accepted here.

#### Query parameters

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/versions/$VERSION/content \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

## Plugins › Installation Settings

### List Plugin Installation Settings

**GET** `/v1/organizations/plugins/{plugin_id}/installation_settings`

List an organization-owned Plugin's installation settings, which say which
members it is for, most recently created first.

The list holds the Plugin's own organization-wide setting (absent while the Plugin
inherits its marketplace's default) and each RBAC Group's own setting. A
member-owned Plugin has shares instead, so this path returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  default: 20, minimum: 1, maximum: 100

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `target_type: optional "organization" or "rbac_group"`

  Only settings for this kind of target: `organization` (the organization-wide setting) or `rbac_group` (an RBAC Group's).

  - `"organization"`

  - `"rbac_group"`

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Returns

- `data: array of BetaPluginInstallationSetting`

  - `type: "plugin_installation_setting"`

    Always `plugin_installation_setting`.

    default: plugin_installation_setting

  - `created_at: string`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `installation_preference: "auto_install" or "available" or "not_available" or "required"`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `BetaPluginTargetOrganization object`

      - `type: "organization"`

        Every member of the organization.

        default: organization

    - `BetaPluginTargetRBACGroup object`

      - `type: "rbac_group"`

        An RBAC Group.

        default: rbac_group

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `BetaPluginTargetOrganizationMember object`

      - `type: "organization_member"`

        One member of the organization.

        default: organization_member

      - `user_id: string`

        The member's User ID.

  - `updated_at: string`

    When its setting last changed.

    format: date-time

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/installation_settings \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2026-03-14T09:26:53.589793Z",
      "installation_preference": "required",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_installation_setting",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Set Plugin Installation Setting

**POST** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Set or change an organization-owned Plugin's installation setting for the whole
organization or for one RBAC Group.

Writing the value a target already holds of its own changes nothing.

A member-owned Plugin has shares instead of installation settings, so this path
returns 404 for one.

Send a Plugin's installation-setting writes one at a time. If several writes for the
same Plugin arrive at the same time, the server handles them one after another and
can answer some of them with `503` instead of applying them. That `503` carries
`x-should-retry: true`, and the write is safe to repeat: wait a second or two, then
send it again.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

- `target: string`

  The target whose setting is written: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Writing the `organization` target stops the Plugin from inheriting its marketplace's default, even when the value written equals that default.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Body parameters

- `installation_preference: "auto_install" or "available" or "not_available" or "required"`

  The installation setting the target is to hold for this Plugin: one of `required`, `auto_install`, `available`, `not_available`.

  - `"auto_install"`

  - `"available"`

  - `"not_available"`

  - `"required"`

#### Returns

- `BetaPluginInstallationSetting object`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `type: "plugin_installation_setting"`

    Always `plugin_installation_setting`.

    default: plugin_installation_setting

  - `created_at: string`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `installation_preference: "auto_install" or "available" or "not_available" or "required"`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `BetaPluginTargetOrganization object`

      - `type: "organization"`

        Every member of the organization.

        default: organization

    - `BetaPluginTargetRBACGroup object`

      - `type: "rbac_group"`

        An RBAC Group.

        default: rbac_group

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `BetaPluginTargetOrganizationMember object`

      - `type: "organization_member"`

        One member of the organization.

        default: organization_member

      - `user_id: string`

        The member's User ID.

  - `updated_at: string`

    When its setting last changed.

    format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/installation_settings/$TARGET \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "installation_preference": "required"
        }'
```

##### Response (200)

```json
{
  "created_at": "2026-03-14T09:26:53.589793Z",
  "installation_preference": "required",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "type": "organization"
  },
  "type": "plugin_installation_setting",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Remove Plugin Installation Setting

**DELETE** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Remove an organization-owned Plugin's own installation setting for the whole
organization or for one RBAC Group.

Removing the `organization` target returns the Plugin to its marketplace's default
installation setting and leaves the groups' settings in place. Removing a group's
setting makes the group's members fall back to the Plugin's organization-wide setting
or to the settings of their other groups.

A target that holds no setting of its own returns 404 (a Plugin that already inherits
its marketplace's default holds no `organization` setting), and so does a member-owned
Plugin.

A removal counts as one of the Plugin's installation-setting writes: send all of those
writes one at a time. If several arrive for the same Plugin at the same time, the server
handles them one after another and can answer some of them with `503` and
`x-should-retry: true` instead of applying them; wait a second or two and send the
removal again. A `404` on the repeat means the setting is already gone.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

- `target: string`

  The target whose own setting is removed: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Removing the `organization` setting returns the Plugin to its marketplace's default.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Returns

- `BetaDeletedPluginInstallationSetting object`

  Confirmation that one target's installation setting was removed, naming
  the Plugin and the target in place of an ID.

  - `type: "plugin_installation_setting_deleted"`

    Always `plugin_installation_setting_deleted`.

    default: plugin_installation_setting_deleted

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Whose setting was removed.

    - `BetaPluginTargetOrganization object`

      - `type: "organization"`

        Every member of the organization.

        default: organization

    - `BetaPluginTargetRBACGroup object`

      - `type: "rbac_group"`

        An RBAC Group.

        default: rbac_group

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `BetaPluginTargetOrganizationMember object`

      - `type: "organization_member"`

        One member of the organization.

        default: organization_member

      - `user_id: string`

        The member's User ID.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/installation_settings/$TARGET \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
    "type": "rbac_group"
  },
  "type": "plugin_installation_setting_deleted"
}
```

## Plugins › Shares

### List Plugin Shares

**GET** `/v1/organizations/plugins/{plugin_id}/shares`

List the shares the owner of a member-owned Plugin has given — to every member of
the organization, to an RBAC Group, or to one member — most recently granted first.

Shares are read-only in this API: members give and withdraw them in claude.ai, and
who gave a share is recorded on the Compliance API activity feed rather than on the
share. An organization-owned Plugin has installation settings instead, so this path
returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

#### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  default: 20, minimum: 1, maximum: 100

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `target_type: optional "organization" or "organization_member" or "rbac_group"`

  Only shares with this kind of target: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

  - `"organization"`

  - `"organization_member"`

  - `"rbac_group"`

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

#### Returns

- `data: array of BetaPluginShare`

  - `type: "plugin_share"`

    Always `plugin_share`.

    default: plugin_share

  - `granted_at: string`

    When the share was given; a share whose role is later changed in claude.ai is re-granted and carries the time of that change.

    format: date-time

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Who the Plugin is shared with: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

    - `BetaPluginTargetOrganization object`

      - `type: "organization"`

        Every member of the organization.

        default: organization

    - `BetaPluginTargetRBACGroup object`

      - `type: "rbac_group"`

        An RBAC Group.

        default: rbac_group

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `BetaPluginTargetOrganizationMember object`

      - `type: "organization_member"`

        One member of the organization.

        default: organization_member

      - `user_id: string`

        The member's User ID.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/shares \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2026-03-14T09:26:53.589793Z",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_share"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```
