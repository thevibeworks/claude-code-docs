---
title: Slack Workspaces
url: https://platform.claude.com/docs/en/api/beta/organization/claude_tag/slack_workspaces
---

# Slack Workspaces

## List Slack Workspaces

**GET** `/v1/organizations/claude_tag/slack_workspaces`

List the set-up Slack workspaces the organization owns, newest first by `created_at`. Pass `slack_workspace_id` to look one workspace up by its Slack identifier: `data` then holds that workspace, or is empty when it is not set up. A workspace of a Slack Enterprise Grid the organization has connected returns 404 until it is set up. With `include_inherited=true` each workspace's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

### Query parameters

- `include_inherited: optional boolean`

  When `true`, `settings` holds what applies in each workspace once the organization's Slack defaults are taken into account, and every member of `sources` names the level a value comes from. When `false` or left out, `settings` holds what each workspace itself stores.

- `limit: optional number`

  Number of items to return per page, between 1 and 100. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `slack_workspace_id: optional string`

  Slack's identifier for one workspace, as in the workspace object's `slack.workspace_id`, not its `id`. With it `data` holds that workspace alone, or nothing when it is not set up.

### Headers

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

### Returns

- `data: array of BetaClaudeTagSlackWorkspace`

  Workspaces on this page, newest first.

  - `type: "slack_workspace"`

  - `id: string`

    The workspace's identifier. Starts with `slws_`. It does not change for as long as the workspace is set up. A workspace that is removed and set up again has a new one, and the old one keeps returning 404; look the workspace up by its Slack identifier for the new one.

  - `created_at: string`

    Time the workspace was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the workspace itself stores or, with `include_inherited`, what applies in it. `sources` says which.

    - `enabled: boolean or null`

      Whether Claude is on. The nearest settings level that sets it decides.

    - `environment_id: string or null`

      The environment Claude's sessions run in, starting with `env_`, or the identifier of a self-hosted runner pool, starting with `ccpool_`. The nearest settings level that sets it decides.

    - `guest_policy: BetaClaudeTagGuestPolicy or null`

      What Claude does in a channel while a Slack guest is in it. The nearest settings level that sets it decides.

      - `BetaClaudeTagGuestPolicyAllow object`

        Claude answers in the channel.

        - `type: "allow"`

      - `BetaClaudeTagGuestPolicyRestrict object`

        Claude does not answer in the channel.

        - `type: "restrict"`

      - `BetaClaudeTagGuestPolicyChannelOnly object`

        Claude answers with only the Bundles attached to the channel itself.

        - `type: "channel_only"`

    - `instructions: string or null`

      Instructions for Claude. Instructions add up: the text of every settings level that sets it is joined, broadest first.

    - `model: string or null`

      The model Claude uses: a model identifier or the name of a model line. The nearest settings level that sets it decides. When none does, Claude uses the product's default model.

  - `slack: BetaClaudeTagSlackWorkspaceIdentifiers`

    Slack's own identifier for the workspace.

    - `workspace_id: string`

      Slack's identifier for the workspace, starting with `T`, such as `T0123ABCD`.

  - `sources: BetaClaudeTagSettingSources`

    For each setting, the settings level its value in `settings` comes from.

    - `enabled: BetaClaudeTagSettingSource or null`

      The settings level `enabled` comes from.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

        - `type: "slack_channel"`

        - `slack_channel_id: string`

          The channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

        - `type: "slack_workspace"`

        - `slack_workspace_id: string`

          The workspace's identifier, starting with `slws_`.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

        - `type: "slack_parent_channel"`

        - `slack_channel_id: string`

          The parent channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

        - `type: "slack_default"`

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

        - `type: "default"`

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

        - `type: "slack_grid_channel"`

        - `slack: BetaClaudeTagSlackChannelIdentifiers`

          Slack's own identifiers for the channel under that other workspace.

          - `channel_id: string`

            Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

            minLength: 2, maxLength: 32

          - `workspace_id: string`

            Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

            minLength: 2, maxLength: 32

    - `environment_id: BetaClaudeTagSettingSource or null`

      The settings level `environment_id` comes from.

    - `guest_policy: BetaClaudeTagSettingSource or null`

      The settings level `guest_policy` comes from.

    - `instructions: array of BetaClaudeTagSettingSource`

      Every settings level that contributes text to `instructions`, broadest first, in the order their text is joined. Empty when none does.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

    - `model: BetaClaudeTagSettingSource or null`

      The settings level `model` comes from.

  - `updated_at: string`

    Time Claude Tag's record of the workspace last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the workspace again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

- `next_page: string or null`

  Cursor for the next page. Null on the last page.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "settings": {
        "enabled": true,
        "environment_id": "environment_id",
        "guest_policy": {
          "type": "allow"
        },
        "instructions": "instructions",
        "model": "model"
      },
      "slack": {
        "workspace_id": "workspace_id"
      },
      "sources": {
        "enabled": {
          "slack_channel_id": "slack_channel_id",
          "type": "slack_channel"
        },
        "environment_id": {
          "slack_channel_id": "slack_channel_id",
          "type": "slack_channel"
        },
        "guest_policy": {
          "slack_channel_id": "slack_channel_id",
          "type": "slack_channel"
        },
        "instructions": [
          {
            "slack_channel_id": "slack_channel_id",
            "type": "slack_channel"
          }
        ],
        "model": {
          "slack_channel_id": "slack_channel_id",
          "type": "slack_channel"
        }
      },
      "type": "slack_workspace",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

## Get Slack Workspace

**GET** `/v1/organizations/claude_tag/slack_workspaces/{id}`

Get one Slack workspace and its settings. By default `settings` holds what the workspace itself stores: a setting that is null there is not set on the workspace and is inherited. With `include_inherited=true`, `settings` holds what applies in the workspace once the organization's Slack defaults are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from.

### Path parameters

- `id: string`

  The workspace's identifier, starting with `slws_`.

### Query parameters

- `include_inherited: optional boolean`

  When `true`, `settings` holds what applies in the workspace once the organization's Slack defaults are taken into account, and every member of `sources` names the level a value comes from. When `false` or left out, `settings` holds what the workspace itself stores.

### Headers

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

### Returns

- `BetaClaudeTagSlackWorkspace object`

  A Slack workspace the organization has connected, itself or through its Slack Enterprise Grid, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_workspace"`

  - `id: string`

    The workspace's identifier. Starts with `slws_`. It does not change for as long as the workspace is set up. A workspace that is removed and set up again has a new one, and the old one keeps returning 404; look the workspace up by its Slack identifier for the new one.

  - `created_at: string`

    Time the workspace was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the workspace itself stores or, with `include_inherited`, what applies in it. `sources` says which.

    - `enabled: boolean or null`

      Whether Claude is on. The nearest settings level that sets it decides.

    - `environment_id: string or null`

      The environment Claude's sessions run in, starting with `env_`, or the identifier of a self-hosted runner pool, starting with `ccpool_`. The nearest settings level that sets it decides.

    - `guest_policy: BetaClaudeTagGuestPolicy or null`

      What Claude does in a channel while a Slack guest is in it. The nearest settings level that sets it decides.

      - `BetaClaudeTagGuestPolicyAllow object`

        Claude answers in the channel.

        - `type: "allow"`

      - `BetaClaudeTagGuestPolicyRestrict object`

        Claude does not answer in the channel.

        - `type: "restrict"`

      - `BetaClaudeTagGuestPolicyChannelOnly object`

        Claude answers with only the Bundles attached to the channel itself.

        - `type: "channel_only"`

    - `instructions: string or null`

      Instructions for Claude. Instructions add up: the text of every settings level that sets it is joined, broadest first.

    - `model: string or null`

      The model Claude uses: a model identifier or the name of a model line. The nearest settings level that sets it decides. When none does, Claude uses the product's default model.

  - `slack: BetaClaudeTagSlackWorkspaceIdentifiers`

    Slack's own identifier for the workspace.

    - `workspace_id: string`

      Slack's identifier for the workspace, starting with `T`, such as `T0123ABCD`.

  - `sources: BetaClaudeTagSettingSources`

    For each setting, the settings level its value in `settings` comes from.

    - `enabled: BetaClaudeTagSettingSource or null`

      The settings level `enabled` comes from.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

        - `type: "slack_channel"`

        - `slack_channel_id: string`

          The channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

        - `type: "slack_workspace"`

        - `slack_workspace_id: string`

          The workspace's identifier, starting with `slws_`.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

        - `type: "slack_parent_channel"`

        - `slack_channel_id: string`

          The parent channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

        - `type: "slack_default"`

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

        - `type: "default"`

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

        - `type: "slack_grid_channel"`

        - `slack: BetaClaudeTagSlackChannelIdentifiers`

          Slack's own identifiers for the channel under that other workspace.

          - `channel_id: string`

            Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

            minLength: 2, maxLength: 32

          - `workspace_id: string`

            Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

            minLength: 2, maxLength: 32

    - `environment_id: BetaClaudeTagSettingSource or null`

      The settings level `environment_id` comes from.

    - `guest_policy: BetaClaudeTagSettingSource or null`

      The settings level `guest_policy` comes from.

    - `instructions: array of BetaClaudeTagSettingSource`

      Every settings level that contributes text to `instructions`, broadest first, in the order their text is joined. Empty when none does.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

    - `model: BetaClaudeTagSettingSource or null`

      The settings level `model` comes from.

  - `updated_at: string`

    Time Claude Tag's record of the workspace last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the workspace again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces/$ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "settings": {
    "enabled": true,
    "environment_id": "environment_id",
    "guest_policy": {
      "type": "allow"
    },
    "instructions": "instructions",
    "model": "model"
  },
  "slack": {
    "workspace_id": "workspace_id"
  },
  "sources": {
    "enabled": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "environment_id": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "guest_policy": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "instructions": [
      {
        "slack_channel_id": "slack_channel_id",
        "type": "slack_channel"
      }
    ],
    "model": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    }
  },
  "type": "slack_workspace",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Slack Workspace

**POST** `/v1/organizations/claude_tag/slack_workspaces/{id}`

Change the settings a Slack workspace stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the workspace inherits it. If any value is refused, no setting in the request is stored.

### Path parameters

- `id: string`

  The workspace's identifier, starting with `slws_`.

### Headers

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

### Body parameters

- `settings: BetaClaudeTagSettingsUpdate`

  The settings to change.

  - `enabled: optional boolean or null`

    Whether Claude is on. `true` on a channel turns Claude on in it even when its workspace stores `false`. Null clears it.

  - `environment_id: optional string or null`

    The environment Claude's sessions run in: the identifier of an active environment of the organization, starting with `env_`. Null clears it.

    minLength: 1, maxLength: 64

  - `guest_policy: optional BetaClaudeTagGuestPolicy or null`

    What Claude does in a channel while a Slack guest is in it. Null clears it.

    - `BetaClaudeTagGuestPolicyAllow object`

      Claude answers in the channel.

      - `type: "allow"`

    - `BetaClaudeTagGuestPolicyRestrict object`

      Claude does not answer in the channel.

      - `type: "restrict"`

    - `BetaClaudeTagGuestPolicyChannelOnly object`

      Claude answers with only the Bundles attached to the channel itself.

      - `type: "channel_only"`

  - `instructions: optional string or null`

    Instructions for Claude, up to 8,192 characters after leading and trailing white space is trimmed. Null or blank text clears them.

  - `model: optional string or null`

    The model Claude uses: the identifier of a model, or the name of a model line, that the organization is entitled to for Claude Tag. Null clears it.

    minLength: 1, maxLength: 128

### Returns

- `BetaClaudeTagSlackWorkspace object`

  A Slack workspace the organization has connected, itself or through its Slack Enterprise Grid, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_workspace"`

  - `id: string`

    The workspace's identifier. Starts with `slws_`. It does not change for as long as the workspace is set up. A workspace that is removed and set up again has a new one, and the old one keeps returning 404; look the workspace up by its Slack identifier for the new one.

  - `created_at: string`

    Time the workspace was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the workspace itself stores or, with `include_inherited`, what applies in it. `sources` says which.

    - `enabled: boolean or null`

      Whether Claude is on. The nearest settings level that sets it decides.

    - `environment_id: string or null`

      The environment Claude's sessions run in, starting with `env_`, or the identifier of a self-hosted runner pool, starting with `ccpool_`. The nearest settings level that sets it decides.

    - `guest_policy: BetaClaudeTagGuestPolicy or null`

      What Claude does in a channel while a Slack guest is in it. The nearest settings level that sets it decides.

      - `BetaClaudeTagGuestPolicyAllow object`

        Claude answers in the channel.

        - `type: "allow"`

      - `BetaClaudeTagGuestPolicyRestrict object`

        Claude does not answer in the channel.

        - `type: "restrict"`

      - `BetaClaudeTagGuestPolicyChannelOnly object`

        Claude answers with only the Bundles attached to the channel itself.

        - `type: "channel_only"`

    - `instructions: string or null`

      Instructions for Claude. Instructions add up: the text of every settings level that sets it is joined, broadest first.

    - `model: string or null`

      The model Claude uses: a model identifier or the name of a model line. The nearest settings level that sets it decides. When none does, Claude uses the product's default model.

  - `slack: BetaClaudeTagSlackWorkspaceIdentifiers`

    Slack's own identifier for the workspace.

    - `workspace_id: string`

      Slack's identifier for the workspace, starting with `T`, such as `T0123ABCD`.

  - `sources: BetaClaudeTagSettingSources`

    For each setting, the settings level its value in `settings` comes from.

    - `enabled: BetaClaudeTagSettingSource or null`

      The settings level `enabled` comes from.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

        - `type: "slack_channel"`

        - `slack_channel_id: string`

          The channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

        - `type: "slack_workspace"`

        - `slack_workspace_id: string`

          The workspace's identifier, starting with `slws_`.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

        - `type: "slack_parent_channel"`

        - `slack_channel_id: string`

          The parent channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

        - `type: "slack_default"`

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

        - `type: "default"`

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

        - `type: "slack_grid_channel"`

        - `slack: BetaClaudeTagSlackChannelIdentifiers`

          Slack's own identifiers for the channel under that other workspace.

          - `channel_id: string`

            Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

            minLength: 2, maxLength: 32

          - `workspace_id: string`

            Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

            minLength: 2, maxLength: 32

    - `environment_id: BetaClaudeTagSettingSource or null`

      The settings level `environment_id` comes from.

    - `guest_policy: BetaClaudeTagSettingSource or null`

      The settings level `guest_policy` comes from.

    - `instructions: array of BetaClaudeTagSettingSource`

      Every settings level that contributes text to `instructions`, broadest first, in the order their text is joined. Empty when none does.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

    - `model: BetaClaudeTagSettingSource or null`

      The settings level `model` comes from.

  - `updated_at: string`

    Time Claude Tag's record of the workspace last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the workspace again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_workspaces/$ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "settings": {}
        }'
```

#### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "settings": {
    "enabled": true,
    "environment_id": "environment_id",
    "guest_policy": {
      "type": "allow"
    },
    "instructions": "instructions",
    "model": "model"
  },
  "slack": {
    "workspace_id": "workspace_id"
  },
  "sources": {
    "enabled": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "environment_id": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "guest_policy": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    },
    "instructions": [
      {
        "slack_channel_id": "slack_channel_id",
        "type": "slack_channel"
      }
    ],
    "model": {
      "slack_channel_id": "slack_channel_id",
      "type": "slack_channel"
    }
  },
  "type": "slack_workspace",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain types

### Beta Claude Tag Slack Workspace

- `BetaClaudeTagSlackWorkspace object`

  A Slack workspace the organization has connected, itself or through its Slack Enterprise Grid, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_workspace"`

  - `id: string`

    The workspace's identifier. Starts with `slws_`. It does not change for as long as the workspace is set up. A workspace that is removed and set up again has a new one, and the old one keeps returning 404; look the workspace up by its Slack identifier for the new one.

  - `created_at: string`

    Time the workspace was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the workspace itself stores or, with `include_inherited`, what applies in it. `sources` says which.

    - `enabled: boolean or null`

      Whether Claude is on. The nearest settings level that sets it decides.

    - `environment_id: string or null`

      The environment Claude's sessions run in, starting with `env_`, or the identifier of a self-hosted runner pool, starting with `ccpool_`. The nearest settings level that sets it decides.

    - `guest_policy: BetaClaudeTagGuestPolicy or null`

      What Claude does in a channel while a Slack guest is in it. The nearest settings level that sets it decides.

      - `BetaClaudeTagGuestPolicyAllow object`

        Claude answers in the channel.

        - `type: "allow"`

      - `BetaClaudeTagGuestPolicyRestrict object`

        Claude does not answer in the channel.

        - `type: "restrict"`

      - `BetaClaudeTagGuestPolicyChannelOnly object`

        Claude answers with only the Bundles attached to the channel itself.

        - `type: "channel_only"`

    - `instructions: string or null`

      Instructions for Claude. Instructions add up: the text of every settings level that sets it is joined, broadest first.

    - `model: string or null`

      The model Claude uses: a model identifier or the name of a model line. The nearest settings level that sets it decides. When none does, Claude uses the product's default model.

  - `slack: BetaClaudeTagSlackWorkspaceIdentifiers`

    Slack's own identifier for the workspace.

    - `workspace_id: string`

      Slack's identifier for the workspace, starting with `T`, such as `T0123ABCD`.

  - `sources: BetaClaudeTagSettingSources`

    For each setting, the settings level its value in `settings` comes from.

    - `enabled: BetaClaudeTagSettingSource or null`

      The settings level `enabled` comes from.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

        - `type: "slack_channel"`

        - `slack_channel_id: string`

          The channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

        - `type: "slack_workspace"`

        - `slack_workspace_id: string`

          The workspace's identifier, starting with `slws_`.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

        - `type: "slack_parent_channel"`

        - `slack_channel_id: string`

          The parent channel's identifier, starting with `slch_`.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

        - `type: "slack_default"`

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

        - `type: "default"`

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

        - `type: "slack_grid_channel"`

        - `slack: BetaClaudeTagSlackChannelIdentifiers`

          Slack's own identifiers for the channel under that other workspace.

          - `channel_id: string`

            Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

            minLength: 2, maxLength: 32

          - `workspace_id: string`

            Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

            minLength: 2, maxLength: 32

    - `environment_id: BetaClaudeTagSettingSource or null`

      The settings level `environment_id` comes from.

    - `guest_policy: BetaClaudeTagSettingSource or null`

      The settings level `guest_policy` comes from.

    - `instructions: array of BetaClaudeTagSettingSource`

      Every settings level that contributes text to `instructions`, broadest first, in the order their text is joined. Empty when none does.

      - `BetaClaudeTagSlackChannelSettingSource object`

        The value comes from the addressed Slack channel itself.

      - `BetaClaudeTagSlackWorkspaceSettingSource object`

        The value comes from a Slack workspace of the organization.

      - `BetaClaudeTagSlackParentChannelSettingSource object`

        The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

      - `BetaClaudeTagSlackDefaultSettingSource object`

        The value comes from the organization's Slack defaults, which have no identifier.

      - `BetaClaudeTagDefaultSettingSource object`

        No settings level sets a value, and the built-in default applies.

      - `BetaClaudeTagSlackGridChannelSettingSource object`

        The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

    - `model: BetaClaudeTagSettingSource or null`

      The settings level `model` comes from.

  - `updated_at: string`

    Time Claude Tag's record of the workspace last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the workspace again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time
