---
title: Update Bundle
url: https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles/update
---

# Update Bundle

**POST** `/v1/organizations/claude_tag/bundles/{bundle_id}`

Change a Bundle's instructions. The update is partial: a field left out is unchanged, and `instructions` sent as null or as an empty string clears them. The later of two updates wins. Sessions that start after the change use the new instructions; sessions already running keep the ones they started with. Some Bundles are managed in claude.ai, and an update of one returns 400.

## Path parameters

- `bundle_id: string`

  The Bundle's identifier, starting with `capp_`.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `experimental-claude-tag-2026-10-21` in this header.

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

- `instructions: optional string or null`

  Instructions for Claude, up to 10,000 bytes (UTF-8), added to the instructions of every session that can use the Bundle. Null or an empty string clears them.

## Returns

- `BetaClaudeTagBundle object`

  A named set of access that Claude can use in a Slack channel or a Slack workspace: connectors, repositories and credentials. Created and edited in claude.ai; Update Bundle also changes its instructions.

  - `type: "bundle"`

  - `id: string`

    The Bundle's identifier. Starts with `capp_`.

  - `created_at: string`

    Time the Bundle was created.

    format: date-time

  - `description: string or null`

    What the Bundle is for. Null when it has none. Read-only.

  - `display_name: string`

    The Bundle's name. Always set. Read-only.

  - `instructions: string or null`

    Instructions for Claude, added to the instructions of every session that can use the Bundle. Null when it has none.

  - `updated_at: string`

    Time of the last change to the Bundle.

    format: date-time

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=http).

Each code below is the value of `error.details.error_code` in the response body.

- `bundle_attachment_not_supported` (HTTP status 400)

  The Bundle has an attachment this API does not support editing, so its instructions can be changed only in claude.ai.

- `bundle_on_call` (HTTP status 400)

  This Bundle's instructions are managed in claude.ai and can't be changed through the API.

- `api_key_scope_missing` (HTTP status 403)

  The API key lacks the scope the request needs: `read:claude_tag` for a read, `write:claude_tag` for a change.

- `claude_tag_writes_not_enabled` (HTTP status 403)

  Changes through the Claude Tag API are not enabled for the organization.

- `compliance_configuration_restricted` (HTTP status 403)

  The organization's compliance configuration does not let Claude Tag store anything new.

- `organization_level_scoped_api_key_required` (HTTP status 403)

  The credential is not a scoped API key that is bound at the organization level.

- `slack_channel_set_up_settings_conflict` (HTTP status 409)

  The request set the channel up, and something else then changed the channel or removed it. Nothing of `settings` was stored.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/bundles/$BUNDLE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "display_name": "display_name",
  "instructions": "instructions",
  "type": "bundle",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
