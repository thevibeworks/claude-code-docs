---
title: Update Plugin
url: https://platform.claude.com/docs/en/api/beta/organization/plugins/update
---

# Update Plugin

**POST** `/v1/organizations/plugins/{plugin_id}`

Change which stored version of an organization-owned Plugin is served to members,
for example to roll back to an earlier one. This pins the served version: later
uploads are stored but no longer change what is served, and pinning cannot currently
be undone, here or in claude.ai.

Pass the version as `served_version_id`: an earlier one to roll back, a later one to
start serving a version that was stored without being served, or the one already
served to pin it without changing what is served. No new version is created.

When the organization has content scanning enabled, a version whose
`content_scan.status` is `processing` is refused with a 409 (`error_code`
`scan_pending`; retry once the scan finishes). A version whose `content_scan.status`
is `errored`, or whose `content_scan.assessment` is `fail` or `unknown`, is refused
with a 400 (`error_code` `scan_failed`); a `warn` is accepted. If the scan outcome
cannot be read at that moment, the request fails with a retryable 503 instead.
When the Plugin is in the organization's
library marketplace, a version other than the one served is also refused with a 409
when one of its skills has a name that an organization skill (one an administrator
uploaded for the whole organization in claude.ai) has since taken: `error_code`
`skill_name_taken`, with that name in `details.skill_name`. A member-owned Plugin
cannot be updated here (403).

This endpoint does not write installation settings; they are written at
`/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

## Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

## Headers

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

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

## Body parameters

- `served_version_id: string`

  Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

## Returns

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

      The scan's verdict; set only when `status` is `completed`. A `warn` can mean a `fail` that was allowed in claude.ai.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string or null`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run. Once a scan of the version has completed, `content_scan` describes the newest completed scan, even while a later scan runs. While the scan outcome cannot be read, `status` is `errored` instead.

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

    The served version's manifest `version`, normalized for display, or `null` (the Plugin Version's `manifest_version` says how and when).

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

    How far the served version reaches, or `null` if it is not classified.

    `remote` means it declares an MCP server or a CLI. `privileged` means it declares no MCP server or CLI, but declares a hook, monitor, language server, or settings, or has a skill, command, or other Markdown file whose frontmatter pre-approves tools (`allowed-tools` with any value other than an empty one or one that names only `AskUserQuestion`, `TodoWrite`, and `ToolSearch`). Otherwise it is `contained`.

    If the frontmatter of a skill, command, or other Markdown file that could change the value could not be read, or was past a size limit, the version is `null` or `privileged` (or `remote`, if it declares an MCP server or a CLI), not `contained`. The value is normally worked out when a version is stored, under the rules of that time, so an older version can be `null`, or `contained` where the same files stored today would be `privileged` or `null`.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    True once the served version has been pinned, through Update Plugin or in claude.ai. While false, a new version normally becomes the served version when it is stored. While the newest version is not the served version, as when a version saved in claude.ai is waiting for its content scan, `served_version_id` differs from `latest_version_id`.

  - `updated_at: string`

    RFC 3339. Moves on a served-version change (including pinning an unpinned Plugin to the version it already serves) and, normally, on a new version. A version saved in claude.ai that waits for its content scan moves it when it becomes the served version, and not necessarily when it is stored. A change to the Plugin's installation settings or shares does not move it.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "served_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8"
        }'
```

### Response (200)

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
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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
