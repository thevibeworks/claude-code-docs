---
title: List Bundle Targets
url: https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles/targets/list
---

# List Bundle Targets

**GET** `/v1/organizations/claude_tag/bundles/{bundle_id}/targets`

List the Slack channels and Slack workspaces a Bundle is attached to, newest first by `created_at`. Only channels and workspaces the organization owns are listed; a Bundle that is attached to anything else has no Bundle Target for it.

## Path parameters

- `bundle_id: string`

  The Bundle's identifier, starting with `capp_`.

## Query parameters

- `limit: optional number`

  Number of items to return per page, between 1 and 100. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `experimental-claude-tag-2026-10-21` in this header.

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

## Returns

- `data: array of BetaClaudeTagBundleTarget`

  Bundle Targets on this page, newest first.

  - `BetaClaudeTagSlackChannelBundleTarget object`

    One Bundle attached to one Slack channel. The Bundle can be used in that channel only.

    - `type: "slack_channel"`

    - `id: string`

      The Bundle Target's identifier. Starts with `btgt_`. No two Bundle Targets have the same one, and the same Bundle and target always give the same one, also after a detach and a new attach. It is opaque.

    - `created_at: string`

      Time the Bundle was attached.

      format: date-time

    - `slack_channel_id: string`

      The identifier of the Slack channel the Bundle is attached to, starting with `slch_`. It is the channel object's `id`, not Slack's `channel_id`.

  - `BetaClaudeTagSlackWorkspaceBundleTarget object`

    One Bundle attached to one Slack workspace. The Bundle can be used in the workspace and in every channel in it.

    - `type: "slack_workspace"`

    - `id: string`

      The Bundle Target's identifier. Starts with `btgt_`. No two Bundle Targets have the same one, and the same Bundle and target always give the same one, also after a detach and a new attach. It is opaque.

    - `created_at: string`

      Time the Bundle was attached.

      format: date-time

    - `slack_workspace_id: string`

      The identifier of the Slack workspace the Bundle is attached to, starting with `slws_`.

- `next_page: string or null`

  Cursor for the next page. Null on the last page.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/bundles/$BUNDLE_ID/targets \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    }
  ],
  "next_page": "next_page"
}
```
