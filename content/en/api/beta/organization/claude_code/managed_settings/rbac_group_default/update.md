---
title: Update RBAC Group Default Claude Code Managed Settings
url: https://platform.claude.com/docs/en/api/beta/organization/claude_code/managed_settings/rbac_group_default/update
---

# Update RBAC Group Default Claude Code Managed Settings

**POST** `/v1/organizations/claude_code/managed_settings/rbac_group_default`

Set or replace the default Claude Code managed settings, or clear them with `null`.

**Accepted credentials:** an organization-level Admin API key with the `write:claude_code_managed_settings` scope.

Every request must include the beta header `anthropic-beta: ce-claude-code-managed-settings-2026-10-06`. A request without it, or from an organization not enabled for this beta, returns `404`. The Claude Code Managed Settings API is in beta and is available to Claude Enterprise organizations only.

A write that returns `503` may have applied. Retrying it is safe.

## Headers

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

  - `"efs-2026-10-01"`

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

## Body parameters

- `settings: map[unknown] or null`

  The whole settings document, a JSON object of Claude Code managed settings. It replaces any stored document, or `null` clears the default settings. At most 1 MiB as the server stores it, which can be larger than the request body.

## Returns

- `BetaClaudeCodeRBACGroupDefaultManagedSettings object`

  - `type: "claude_code_rbac_group_default_managed_settings"`

    Always `claude_code_rbac_group_default_managed_settings`.

    default: claude_code_rbac_group_default_managed_settings

  - `settings: map[unknown] or null`

    The default settings document, or `null` if none are set or the stored document is damaged and can no longer be read. To tell these apart, `updated_at` is `null` only when none are set. Replacing a damaged document fixes this.

  - `updated_at: string or null`

    When the default settings last changed, in RFC 3339 format, or `null` if none are set.

    format: date-time

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=http).

Each code below is the value of `error.details.error_code` in the response body.

- `cmek_feature_unsupported` (HTTP status 400)

  This stored settings document currently cannot be read or replaced. Contact support, or, if you no longer need these settings, delete the group's settings or clear the default.

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

## Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_code/managed_settings/rbac_group_default \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-claude-code-managed-settings-2026-10-06' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "settings": {
            "foo": "bar"
          }
        }'
```

### Response (200)

```json
{
  "settings": {
    "foo": "bar"
  },
  "type": "claude_code_rbac_group_default_managed_settings",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
