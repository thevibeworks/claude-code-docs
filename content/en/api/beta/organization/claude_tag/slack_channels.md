---
title: Slack Channels
url: https://platform.claude.com/docs/en/api/beta/organization/claude_tag/slack_channels
---

# Slack Channels

## Set Up Slack Channel

**POST** `/v1/organizations/claude_tag/slack_channels`

Set a Slack channel up for Claude Tag and return it with its identifier. If the channel is already set up, whether in claude.ai, by Claude's first use in it or by an earlier request, the existing channel is returned, so the request can be repeated. `settings`, when sent, is applied as an update applies it. Before a channel is set up, Claude's Slack app confirms with Slack that the channel is in the workspace, is not archived and is visible to the app; a channel that fails the confirmation returns 404. Setting the channel up and applying `settings` are two steps: when the second is refused, the response is the refusal, the channel stays set up with every setting unset, and the error's `details.slack_channel_id` holds the channel's identifier.

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

- `slack: BetaClaudeTagSlackChannelIdentifiers`

  Slack's own identifiers for the channel to set up. The organization must own the workspace.

  - `channel_id: string`

    Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

    minLength: 2, maxLength: 32

  - `workspace_id: string`

    Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

    minLength: 2, maxLength: 32

- `settings: optional BetaClaudeTagSettingsCreate`

  Settings to store on the channel, applied as Update Slack Channel applies them.

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

- `BetaClaudeTagSlackChannel object`

  A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_channel"`

  - `id: string`

    The channel's identifier. Starts with `slch_`. It does not change for as long as the channel is set up, with one exception: a channel that is not configured gets a new one when claude.ai replaces its record, which happens only while the organization's read-only mode is off. A channel that is removed and set up again also has a new one. The old one keeps returning 404; look the channel up by its Slack identifiers for the new one.

  - `created_at: string`

    Time the channel was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the channel itself stores or, with `include_inherited`, what applies in it. `sources` says which.

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

  - `slack: BetaClaudeTagSlackChannelIdentifiers`

    Slack's own identifiers for the channel.

    - `channel_id: string`

      Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

      minLength: 2, maxLength: 32

    - `workspace_id: string`

      Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

      minLength: 2, maxLength: 32

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

    Time Claude Tag's record of the channel last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the channel again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "slack": {
            "channel_id": "xx",
            "workspace_id": "xx"
          }
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
    "channel_id": "xx",
    "workspace_id": "xx"
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
  "type": "slack_channel",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Slack Channels

**GET** `/v1/organizations/claude_tag/slack_channels`

List the set-up Slack channels of one Slack workspace, newest first by `created_at`. A channel that is not set up is not listed: Slack holds the full list of a workspace's channels. Pass `slack_channel_id` as well to look one channel up by its Slack identifiers: `data` then holds that channel, or is empty when it is not set up, and `limit` and `page` are ignored. A workspace that the organization owns only through a Slack Enterprise Grid returns 404 until it is set up. With `include_inherited=true` each channel's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

### Query parameters

- `slack_workspace_id: string`

  The Slack workspace whose channels to list: Slack's identifier for it, as in the channel object's `slack.workspace_id`, not the workspace object's `id`.

- `include_inherited: optional boolean`

  When `true`, `settings` holds what applies in each channel once the settings levels above it are taken into account, and every member of `sources` names the level a value comes from. When `false` or left out, `settings` holds what each channel itself stores.

- `limit: optional number`

  Number of items to return per page, between 1 and 100. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `slack_channel_id: optional string`

  Slack's identifier for one channel of that workspace, as in the channel object's `slack.channel_id`. It is not the channel object's `id`. With it `data` holds that channel alone, or nothing when the channel is not set up.

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

- `data: array of BetaClaudeTagSlackChannel`

  Channels on this page, newest first.

  - `type: "slack_channel"`

  - `id: string`

    The channel's identifier. Starts with `slch_`. It does not change for as long as the channel is set up, with one exception: a channel that is not configured gets a new one when claude.ai replaces its record, which happens only while the organization's read-only mode is off. A channel that is removed and set up again also has a new one. The old one keeps returning 404; look the channel up by its Slack identifiers for the new one.

  - `created_at: string`

    Time the channel was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the channel itself stores or, with `include_inherited`, what applies in it. `sources` says which.

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

  - `slack: BetaClaudeTagSlackChannelIdentifiers`

    Slack's own identifiers for the channel.

    - `channel_id: string`

      Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

      minLength: 2, maxLength: 32

    - `workspace_id: string`

      Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

      minLength: 2, maxLength: 32

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

    Time Claude Tag's record of the channel last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the channel again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

- `next_page: string or null`

  Cursor for the next page. Null on the last page.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels \
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
        "channel_id": "xx",
        "workspace_id": "xx"
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
      "type": "slack_channel",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

## Get Slack Channel

**GET** `/v1/organizations/claude_tag/slack_channels/{id}`

Get one Slack channel and its settings. By default `settings` holds what the channel itself stores: a setting that is null there is not set on the channel and is inherited. With `include_inherited=true`, `settings` holds what applies in the channel once the settings levels above it are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from, so a caller tells the channel's own value from an inherited one by its source, not by whether it is null.

### Path parameters

- `id: string`

  The channel's identifier, starting with `slch_`.

### Query parameters

- `include_inherited: optional boolean`

  When `true`, `settings` holds what applies in the channel once the settings levels above it are taken into account, and every member of `sources` names the level a value comes from. When `false` or left out, `settings` holds what the channel itself stores.

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

- `BetaClaudeTagSlackChannel object`

  A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_channel"`

  - `id: string`

    The channel's identifier. Starts with `slch_`. It does not change for as long as the channel is set up, with one exception: a channel that is not configured gets a new one when claude.ai replaces its record, which happens only while the organization's read-only mode is off. A channel that is removed and set up again also has a new one. The old one keeps returning 404; look the channel up by its Slack identifiers for the new one.

  - `created_at: string`

    Time the channel was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the channel itself stores or, with `include_inherited`, what applies in it. `sources` says which.

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

  - `slack: BetaClaudeTagSlackChannelIdentifiers`

    Slack's own identifiers for the channel.

    - `channel_id: string`

      Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

      minLength: 2, maxLength: 32

    - `workspace_id: string`

      Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

      minLength: 2, maxLength: 32

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

    Time Claude Tag's record of the channel last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the channel again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/$ID \
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
    "channel_id": "xx",
    "workspace_id": "xx"
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
  "type": "slack_channel",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Slack Channel

**POST** `/v1/organizations/claude_tag/slack_channels/{id}`

Change the settings a Slack channel stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the channel inherits it. If any value is refused, no setting in the request is stored. A group direct message takes no settings and returns 400.

### Path parameters

- `id: string`

  The channel's identifier, starting with `slch_`.

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

- `BetaClaudeTagSlackChannel object`

  A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_channel"`

  - `id: string`

    The channel's identifier. Starts with `slch_`. It does not change for as long as the channel is set up, with one exception: a channel that is not configured gets a new one when claude.ai replaces its record, which happens only while the organization's read-only mode is off. A channel that is removed and set up again also has a new one. The old one keeps returning 404; look the channel up by its Slack identifiers for the new one.

  - `created_at: string`

    Time the channel was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the channel itself stores or, with `include_inherited`, what applies in it. `sources` says which.

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

  - `slack: BetaClaudeTagSlackChannelIdentifiers`

    Slack's own identifiers for the channel.

    - `channel_id: string`

      Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

      minLength: 2, maxLength: 32

    - `workspace_id: string`

      Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

      minLength: 2, maxLength: 32

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

    Time Claude Tag's record of the channel last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the channel again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/$ID \
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
    "channel_id": "xx",
    "workspace_id": "xx"
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
  "type": "slack_channel",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Remove Slack Channel

**DELETE** `/v1/organizations/claude_tag/slack_channels/{id}`

Remove a Slack channel from Claude Tag. This deletes the channel's stored settings and its Bundle Targets at once, and then, in the background, the channel's sessions and their transcripts, its memory, its routines and the artifacts published from it. None of it can be restored. The channel in Slack and its messages are unchanged. The request is refused with 400 and `error.details.error_code` `slack_channel_enabled` while `enabled` resolves to `true` for the channel, as a read with `include_inherited=true` returns it: set `enabled` to `false` on the channel first. This guards against removing a channel in use by mistake; it is not a way to keep Claude out, because the removal deletes the channel's own `enabled: false` with its other settings, after which the channel inherits again and Claude's next use of it can set it up anew with a new identifier. The identifier returns 404 as soon as the request returns, so a repeated removal returns 404. A group direct message returns 400, and so does a channel that holds configuration this API does not manage.

### Path parameters

- `id: string`

  The channel's identifier, starting with `slch_`.

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

- `BetaClaudeTagDeletedSlackChannel object`

  Confirms that a Slack channel was removed from Claude Tag.

  - `type: "slack_channel_deleted"`

  - `id: string`

    The removed channel's identifier.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/claude_tag/slack_channels/$ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "slack_channel_deleted"
}
```

## Domain types

### Beta Claude Tag Deleted Slack Channel

- `BetaClaudeTagDeletedSlackChannel object`

  Confirms that a Slack channel was removed from Claude Tag.

  - `type: "slack_channel_deleted"`

  - `id: string`

    The removed channel's identifier.

### Beta Claude Tag Slack Channel

- `BetaClaudeTagSlackChannel object`

  A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.

  - `type: "slack_channel"`

  - `id: string`

    The channel's identifier. Starts with `slch_`. It does not change for as long as the channel is set up, with one exception: a channel that is not configured gets a new one when claude.ai replaces its record, which happens only while the organization's read-only mode is off. A channel that is removed and set up again also has a new one. The old one keeps returning 404; look the channel up by its Slack identifiers for the new one.

  - `created_at: string`

    Time the channel was set up, by whichever route. It does not change for as long as `id` does not.

    format: date-time

  - `settings: BetaClaudeTagSettings`

    What the channel itself stores or, with `include_inherited`, what applies in it. `sources` says which.

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

  - `slack: BetaClaudeTagSlackChannelIdentifiers`

    Slack's own identifiers for the channel.

    - `channel_id: string`

      Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

      minLength: 2, maxLength: 32

    - `workspace_id: string`

      Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

      minLength: 2, maxLength: 32

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

    Time Claude Tag's record of the channel last changed. It moves on every change to a setting, and can also move when something no response holds changes, so a later value says to read the channel again, not that a setting changed. Attaching or detaching a Bundle does not by itself move it.

    format: date-time
