---
title: Configuration
url: https://platform.claude.com/docs/en/api/beta/organization/claude_code/managed_settings/configuration
---

# Configuration

## Get Claude Code Managed Settings Configuration

**GET** `/v1/organizations/claude_code/managed_settings/configuration`

Retrieve the organization's Claude Code managed settings mode and RBAC Group order.

**Accepted credentials:** an organization-level Admin API key with the `read:claude_code_managed_settings` scope.

Every request must include the beta header `anthropic-beta: ce-claude-code-managed-settings-2026-10-06`. A request without it, or from an organization not enabled for this beta, returns `404`. The Claude Code Managed Settings API is in beta and is available to Claude Enterprise organizations only.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-claude-code-managed-settings-2026-10-06` in this header.

  - `string`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"output-128k-2025-02-19"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

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

  - `"admin-user-sign-out-2026-10-08"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

  - `"ce-claude-code-managed-settings-2026-10-06"`

  - `"user-profiles-billing-2026-10-01"`

  - `"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

### Returns

- `BetaClaudeCodeManagedSettingsConfiguration object`

  - `type: "claude_code_managed_settings_configuration"`

    Always `claude_code_managed_settings_configuration`.

    default: claude_code_managed_settings_configuration

  - `mode: BetaClaudeCodeManagedSettingsMode`

    How the organization serves managed settings. In `organization` mode every member receives the organization settings, which are set in claude.ai. In `rbac_groups` mode each member receives the settings of the first RBAC Group in `rbac_group_order` that they belong to. A member in none of them receives the default settings, or no settings if no default is set.

    - `BetaClaudeCodeManagedSettingsOrganizationMode object`

      - `type: "organization"`

        Always `organization`.

        default: organization

    - `BetaClaudeCodeManagedSettingsRBACGroupsMode object`

      - `type: "rbac_groups"`

        Always `rbac_groups`.

        default: rbac_groups

  - `mode_updated_at: string or null`

    When the mode last changed, in RFC 3339 format, or `null` if it never has.

    format: date-time

  - `rbac_group_order: array of string`

    The ID of every RBAC Group with settings, deleted groups included, highest precedence first.

  - `rbac_group_order_version: string`

    An opaque version of `rbac_group_order`, which changes whenever the order does. Send it back with a new order.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_code/managed_settings/configuration \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-claude-code-managed-settings-2026-10-06' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "mode": {
    "type": "organization"
  },
  "mode_updated_at": "2019-12-27T18:11:19.117Z",
  "rbac_group_order": [
    "rbac_group_012rppKaSVsmTo6NqRDXQXNF"
  ],
  "rbac_group_order_version": "rbac_group_order_version",
  "type": "claude_code_managed_settings_configuration"
}
```

## Update Claude Code Managed Settings Configuration

**POST** `/v1/organizations/claude_code/managed_settings/configuration`

Change the organization's Claude Code managed settings mode, the RBAC Group order, or both, in one atomic write.

To change the order, send `rbac_group_order` with the `rbac_group_order_version` from the read the change is based on. If the order has changed since that read, the request returns `409`: read it again and retry. To switch modes only if the order has not changed, send the current `rbac_group_order` and `rbac_group_order_version` with the new `mode`.

A switch to `rbac_groups` mode with no RBAC Group settings and no default settings copies the organization settings into a new default, in the same write, so members keep the settings they had. The copy does not follow later changes to the organization settings. If the organization settings cannot be copied, the request returns `400` and changes nothing. If they cannot be read, are over 1 MiB or are not valid, setting the default settings first avoids the copy.

After a switch to `rbac_groups` mode, a member in no listed RBAC Group receives the default settings, or no settings if no default is set, not the organization settings.

**Accepted credentials:** an organization-level Admin API key with the `write:claude_code_managed_settings` scope.

Every request must include the beta header `anthropic-beta: ce-claude-code-managed-settings-2026-10-06`. A request without it, or from an organization not enabled for this beta, returns `404`. The Claude Code Managed Settings API is in beta and is available to Claude Enterprise organizations only.

A write that returns `503` may have applied. Retrying it is safe.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-claude-code-managed-settings-2026-10-06` in this header.

  - `string`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"output-128k-2025-02-19"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

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

  - `"admin-user-sign-out-2026-10-08"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

  - `"ce-claude-code-managed-settings-2026-10-06"`

  - `"user-profiles-billing-2026-10-01"`

  - `"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

### Body parameters

- `mode: optional BetaClaudeCodeManagedSettingsModeParam`

  The new mode, as an object such as `{"type": "rbac_groups"}`.

  - `BetaClaudeCodeManagedSettingsOrganizationModeParam object`

    - `type: "organization"`

  - `BetaClaudeCodeManagedSettingsRBACGroupsModeParam object`

    - `type: "rbac_groups"`

- `rbac_group_order: optional array of string`

  Every RBAC Group that has settings, each listed once, in the new order, highest precedence first. Requires `rbac_group_order_version`.

- `rbac_group_order_version: optional string`

  The `rbac_group_order_version` from the read this change is based on. Requires `rbac_group_order`.

### Returns

- `BetaClaudeCodeManagedSettingsConfiguration object`

  - `type: "claude_code_managed_settings_configuration"`

    Always `claude_code_managed_settings_configuration`.

    default: claude_code_managed_settings_configuration

  - `mode: BetaClaudeCodeManagedSettingsMode`

    How the organization serves managed settings. In `organization` mode every member receives the organization settings, which are set in claude.ai. In `rbac_groups` mode each member receives the settings of the first RBAC Group in `rbac_group_order` that they belong to. A member in none of them receives the default settings, or no settings if no default is set.

    - `BetaClaudeCodeManagedSettingsOrganizationMode object`

      - `type: "organization"`

        Always `organization`.

        default: organization

    - `BetaClaudeCodeManagedSettingsRBACGroupsMode object`

      - `type: "rbac_groups"`

        Always `rbac_groups`.

        default: rbac_groups

  - `mode_updated_at: string or null`

    When the mode last changed, in RFC 3339 format, or `null` if it never has.

    format: date-time

  - `rbac_group_order: array of string`

    The ID of every RBAC Group with settings, deleted groups included, highest precedence first.

  - `rbac_group_order_version: string`

    An opaque version of `rbac_group_order`, which changes whenever the order does. Send it back with a new order.

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=http).

Each code below is the value of `error.details.error_code` in the response body.

- `cmek_key_disabled` (HTTP status 400)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `request_body_timeout` (HTTP status 400)

  The request body did not finish arriving in time, so nothing was done. Send a smaller body, or send it over a faster connection.

- `settings_document_limit_exceeded` (HTTP status 400)

  The organization has reached its limit of settings documents, counting unused ones. An owner can remove unused documents in claude.ai. Deleting a group's settings or clearing the default settings also frees a document, if nothing else uses it. None of these works once the organization has also reached its settings history limit.

- `settings_history_limit_exceeded` (HTTP status 400)

  The organization has reached its settings history limit, a cap on stored versions of its settings documents. Nothing in the API or claude.ai lowers the count, so contact support. Creating or deleting group settings, creating or clearing the default settings, and reordering are refused. Changing the mode still works, unless it would copy the organization settings into a new default.

- `sandbox_egress_restricted` (HTTP status 403)

  The request came from a Claude sandbox with restricted network access, which is not allowed to make this request. Send it from outside the sandbox, or from a sandbox with unrestricted network access.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_code/managed_settings/configuration \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-claude-code-managed-settings-2026-10-06' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

```json
{
  "mode": {
    "type": "organization"
  },
  "mode_updated_at": "2019-12-27T18:11:19.117Z",
  "rbac_group_order": [
    "rbac_group_012rppKaSVsmTo6NqRDXQXNF"
  ],
  "rbac_group_order_version": "rbac_group_order_version",
  "type": "claude_code_managed_settings_configuration"
}
```

## Domain types

### Beta Claude Code Managed Settings Configuration

- `BetaClaudeCodeManagedSettingsConfiguration object`

  - `type: "claude_code_managed_settings_configuration"`

    Always `claude_code_managed_settings_configuration`.

    default: claude_code_managed_settings_configuration

  - `mode: BetaClaudeCodeManagedSettingsMode`

    How the organization serves managed settings. In `organization` mode every member receives the organization settings, which are set in claude.ai. In `rbac_groups` mode each member receives the settings of the first RBAC Group in `rbac_group_order` that they belong to. A member in none of them receives the default settings, or no settings if no default is set.

    - `BetaClaudeCodeManagedSettingsOrganizationMode object`

      - `type: "organization"`

        Always `organization`.

        default: organization

    - `BetaClaudeCodeManagedSettingsRBACGroupsMode object`

      - `type: "rbac_groups"`

        Always `rbac_groups`.

        default: rbac_groups

  - `mode_updated_at: string or null`

    When the mode last changed, in RFC 3339 format, or `null` if it never has.

    format: date-time

  - `rbac_group_order: array of string`

    The ID of every RBAC Group with settings, deleted groups included, highest precedence first.

  - `rbac_group_order_version: string`

    An opaque version of `rbac_group_order`, which changes whenever the order does. Send it back with a new order.

### Beta Claude Code Managed Settings Mode

- `BetaClaudeCodeManagedSettingsMode = BetaClaudeCodeManagedSettingsOrganizationMode or BetaClaudeCodeManagedSettingsRBACGroupsMode`

  - `BetaClaudeCodeManagedSettingsOrganizationMode object`

    - `type: "organization"`

      Always `organization`.

      default: organization

  - `BetaClaudeCodeManagedSettingsRBACGroupsMode object`

    - `type: "rbac_groups"`

      Always `rbac_groups`.

      default: rbac_groups

### Beta Claude Code Managed Settings Mode Param

- `BetaClaudeCodeManagedSettingsModeParam = BetaClaudeCodeManagedSettingsOrganizationModeParam or BetaClaudeCodeManagedSettingsRBACGroupsModeParam`

  - `BetaClaudeCodeManagedSettingsOrganizationModeParam object`

    - `type: "organization"`

  - `BetaClaudeCodeManagedSettingsRBACGroupsModeParam object`

    - `type: "rbac_groups"`

### Beta Claude Code Managed Settings Organization Mode

- `BetaClaudeCodeManagedSettingsOrganizationMode object`

  - `type: "organization"`

    Always `organization`.

    default: organization

### Beta Claude Code Managed Settings Organization Mode Param

- `BetaClaudeCodeManagedSettingsOrganizationModeParam object`

  - `type: "organization"`

### Beta Claude Code Managed Settings RBAC Groups Mode

- `BetaClaudeCodeManagedSettingsRBACGroupsMode object`

  - `type: "rbac_groups"`

    Always `rbac_groups`.

    default: rbac_groups

### Beta Claude Code Managed Settings RBAC Groups Mode Param

- `BetaClaudeCodeManagedSettingsRBACGroupsModeParam object`

  - `type: "rbac_groups"`
