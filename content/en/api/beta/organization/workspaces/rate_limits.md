---
title: Rate Limits
url: https://platform.claude.com/docs/en/api/beta/organization/workspaces/rate_limits
---

# Rate Limits

## List Workspace Rate Limits

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List a workspace's rate limits.

By default, returns only the groups and limiter types that have a
workspace-level override. With `include_inherited=true`, returns every
group with organization-level limits the workspace can see, listing for
each the values it inherits from the organization as well as its own
overrides. Each value's `source` says which it is.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

### Path parameters

- `workspace_id: string`

  The ID of the workspace.

### Query parameters

- `group_type: optional "batch" or "files" or "model_group" or 3 more`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `include_inherited: optional boolean`

  Also list the limiter values the workspace inherits from the organization, including groups with no workspace-level override.

  default: false

- `limit: optional number`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Returns

- `data: array of BetaWorkspaceRateLimit`

  Rate-limit entries for the workspace: one per group with at least one override, or, with `include_inherited` set to `true`, one per group the workspace can see that has organization-level limits.

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: BetaOrganizationRateLimitModelGroup or BetaOrganizationRateLimitBatchGroup or BetaOrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `BetaOrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `BetaOrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of BetaWorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: BetaWorkspaceRateLimitWorkspaceSource or BetaWorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `BetaWorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `BetaWorkspaceRateLimitOrganizationSource object`

        - `type: "organization"`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `value: number`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: string`

    ID of the Workspace this entry applies to.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

- `next_page: string or null`

  Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "source": {
            "type": "workspace"
          },
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

## Set Workspace Rate Limits

**POST** `/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}`

Set or clear rate-limit overrides for one rate-limit group in a workspace.

Only the limiter types named in `limits` change: an integer `value` sets
that type's override and `null` clears it. Types not named keep their
current value. A value above the organization's own limit is stored, but
the organization limit still applies, so the lower of the two is
enforced.

Returns the targeted group's entry with this request applied, in the shape
`GET /v1/organizations/workspaces/{workspace_id}/rate_limits` returns.
Changes take effect within about an hour.

### Path parameters

- `workspace_id: string`

  The ID of the workspace.

- `rate_limit_id: string`

  The `id` of the organization's rate-limit entry to set overrides for.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Body parameters

- `limits: array of BetaWorkspaceRateLimitUpdateValue`

  Limits to set or clear. Unspecified limit types are unchanged.

  minItems: 1, maxItems: 16

  - `type: BetaWorkspaceRateLimitType`

    Rate limiter type.

    - `"fast_itpmca"`

    - `"fast_otpm"`

    - `"input_tokens_per_minute"`

    - `"input_tokens_per_minute_cache_aware"`

    - `"output_tokens_per_minute"`

    - `"requests_per_minute"`

    - `"tokens_per_day"`

    - `"tokens_per_minute"`

    - `"tool_uses_per_second"`

  - `value: number or null`

    New limit value. Set to null to clear the workspace override and fall back to the organization limit.

    minimum: 0, maximum: 9007199254740991

### Returns

- `BetaWorkspaceRateLimit object`

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: BetaOrganizationRateLimitModelGroup or BetaOrganizationRateLimitBatchGroup or BetaOrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `BetaOrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `BetaOrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of BetaWorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: BetaWorkspaceRateLimitWorkspaceSource or BetaWorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `BetaWorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `BetaWorkspaceRateLimitOrganizationSource object`

        - `type: "organization"`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `value: number`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: string`

    ID of the Workspace this entry applies to.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

### Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits/$RATE_LIMIT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "limits": [
            {
              "type": "fast_itpmca",
              "value": 0
            }
          ]
        }'
```

#### Response (200)

```json
{
  "group": {
    "id": "id",
    "display_name": "display_name",
    "type": "model_group"
  },
  "group_type": "batch",
  "limits": [
    {
      "org_limit": 0,
      "source": {
        "type": "workspace"
      },
      "type": "type",
      "value": 0
    }
  ],
  "models": [
    "string"
  ],
  "rate_limit_id": "rate_limit_id",
  "type": "workspace_rate_limit",
  "workspace_id": "workspace_id"
}
```

## Domain types

### Beta Workspace Rate Limit

- `BetaWorkspaceRateLimit object`

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: BetaOrganizationRateLimitModelGroup or BetaOrganizationRateLimitBatchGroup or BetaOrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `BetaOrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `BetaOrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `BetaOrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of BetaWorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: BetaWorkspaceRateLimitWorkspaceSource or BetaWorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `BetaWorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `BetaWorkspaceRateLimitOrganizationSource object`

        - `type: "organization"`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `value: number`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `models: array of string or null`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `workspace_id: string`

    ID of the Workspace this entry applies to.

  - `group_type: "batch" or "files" or "model_group" or 3 more`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

### Beta Workspace Rate Limit Organization Source

- `BetaWorkspaceRateLimitOrganizationSource object`

  - `type: "organization"`

    Always `organization`: no workspace-level override is stored, so the organization's value applies.

    default: organization

### Beta Workspace Rate Limit Type

- `BetaWorkspaceRateLimitType = "fast_itpmca" or "fast_otpm" or "input_tokens_per_minute" or 6 more`

  Rate limiter type.

  - `"fast_itpmca"`

  - `"fast_otpm"`

  - `"input_tokens_per_minute"`

  - `"input_tokens_per_minute_cache_aware"`

  - `"output_tokens_per_minute"`

  - `"requests_per_minute"`

  - `"tokens_per_day"`

  - `"tokens_per_minute"`

  - `"tool_uses_per_second"`

### Beta Workspace Rate Limit Update Value

- `BetaWorkspaceRateLimitUpdateValue object`

  - `type: BetaWorkspaceRateLimitType`

    Rate limiter type.

    - `"fast_itpmca"`

    - `"fast_otpm"`

    - `"input_tokens_per_minute"`

    - `"input_tokens_per_minute_cache_aware"`

    - `"output_tokens_per_minute"`

    - `"requests_per_minute"`

    - `"tokens_per_day"`

    - `"tokens_per_minute"`

    - `"tool_uses_per_second"`

  - `value: number or null`

    New limit value. Set to null to clear the workspace override and fall back to the organization limit.

    minimum: 0, maximum: 9007199254740991

### Beta Workspace Rate Limit Value

- `BetaWorkspaceRateLimitValue object`

  - `type: string`

    The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

  - `org_limit: number or null`

    The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

  - `source: BetaWorkspaceRateLimitWorkspaceSource or BetaWorkspaceRateLimitOrganizationSource`

    Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

    - `BetaWorkspaceRateLimitWorkspaceSource object`

      - `type: "workspace"`

        Always `workspace`: a workspace-level override is stored.

        default: workspace

    - `BetaWorkspaceRateLimitOrganizationSource object`

      - `type: "organization"`

        Always `organization`: no workspace-level override is stored, so the organization's value applies.

        default: organization

  - `value: number`

    The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

### Beta Workspace Rate Limit Workspace Source

- `BetaWorkspaceRateLimitWorkspaceSource object`

  - `type: "workspace"`

    Always `workspace`: a workspace-level override is stored.

    default: workspace
