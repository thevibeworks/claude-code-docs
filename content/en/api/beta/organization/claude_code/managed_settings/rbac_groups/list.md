---
title: List RBAC Group Claude Code Managed Settings
url: https://platform.claude.com/docs/en/api/beta/organization/claude_code/managed_settings/rbac_groups/list
---

# List RBAC Group Claude Code Managed Settings

**GET** `/v1/organizations/claude_code/managed_settings/rbac_groups`

List the RBAC Groups that have Claude Code managed settings, highest precedence first.

Each entry gives the group's status and timestamps, not its settings. The list includes deleted groups that still have settings, and leaves out the default settings. If the order changes between pages, the request returns `409`: list again from the first page.

**Accepted credentials:** an organization-level Admin API key with the `read:claude_code_managed_settings` scope.

Every request must include the beta header `anthropic-beta: ce-claude-code-managed-settings-2026-10-06`. A request without it, or from an organization not enabled for this beta, returns `404`. The Claude Code Managed Settings API is in beta and is available to Claude Enterprise organizations only.

## Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

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

## Returns

- `data: array of BetaClaudeCodeRBACGroupManagedSettingsSummary`

  The RBAC Groups with settings on this page, highest precedence first.

  - `type: "claude_code_rbac_group_managed_settings_summary"`

    Always `claude_code_rbac_group_managed_settings_summary`.

    default: claude_code_rbac_group_managed_settings_summary

  - `created_at: string`

    When the settings document this group uses was first stored, in RFC 3339 format. This can be earlier than when the group got its settings, and it changes if the group gets a different document.

    format: date-time

  - `rbac_group_id: string`

    The RBAC Group's ID, prefixed `rbac_group_`.

  - `rbac_group_status: BetaClaudeCodeRBACGroupStatus`

    Whether the group is still one of the organization's RBAC Groups. Its `type` is `active` if it is, `deleted` if it is not, and `unknown` if that cannot be checked right now. A deleted group's settings stay in `rbac_group_order` but match no member.

    - `BetaClaudeCodeRBACGroupStatusActive object`

      - `type: "active"`

        Always `active`.

        default: active

    - `BetaClaudeCodeRBACGroupStatusDeleted object`

      - `type: "deleted"`

        Always `deleted`.

        default: deleted

    - `BetaClaudeCodeRBACGroupStatusUnknown object`

      - `type: "unknown"`

        Always `unknown`.

        default: unknown

  - `updated_at: string`

    When this group's settings or its position in the order last changed, in RFC 3339 format. Its position changes whenever the number of groups ahead of it changes.

    format: date-time

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_code/managed_settings/rbac_groups \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-claude-code-managed-settings-2026-10-06' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "created_at": "2019-12-27T18:11:19.117Z",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "rbac_group_status": {
        "type": "active"
      },
      "type": "claude_code_rbac_group_managed_settings_summary",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```
