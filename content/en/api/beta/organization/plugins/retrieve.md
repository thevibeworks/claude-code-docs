---
title: Get Plugin
url: https://platform.claude.com/docs/en/api/beta/organization/plugins/retrieve
---

# Get Plugin

**GET** `/v1/organizations/plugins/{plugin_id}`

Retrieve a Plugin by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

## Path parameters

- `plugin_id: string`

  ID of the Plugin (prefixed `plugin_`).

## Query parameters

- `organization_id: optional string`

  For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

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

## Example

```bash
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
