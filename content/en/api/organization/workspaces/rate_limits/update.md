---
title: Set Workspace Rate Limits
url: https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/update
---

# Set Workspace Rate Limits

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

## Path parameters

- `workspace_id: string`

  The ID of the workspace.

- `rate_limit_id: string`

  The `id` of the organization's rate-limit entry to set overrides for.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

## Body parameters

- `limits: array of WorkspaceRateLimitUpdateValue`

  Limits to set or clear. Unspecified limit types are unchanged.

  minItems: 1, maxItems: 16

  - `type: WorkspaceRateLimitType`

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

## Returns

- `WorkspaceRateLimit object`

  - `type: "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group: OrganizationRateLimitModelGroup or OrganizationRateLimitBatchGroup or OrganizationRateLimitTokenCountGroup or 3 more`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `OrganizationRateLimitModelGroup object`

      - `type: "model_group"`

        Always `model_group`: a family of models.

        default: model_group

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `display_name: string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `OrganizationRateLimitBatchGroup object`

      - `type: "batch"`

        Always `batch`: the Message Batches API.

        default: batch

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitTokenCountGroup object`

      - `type: "token_count"`

        Always `token_count`: the Token Count API.

        default: token_count

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitFilesGroup object`

      - `type: "files"`

        Always `files`: the Files API.

        default: files

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitSkillsGroup object`

      - `type: "skills"`

        Always `skills`: the Skills API.

        default: skills

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `OrganizationRateLimitWebSearchGroup object`

      - `type: "web_search"`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `id: string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `limits: array of WorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `type: string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: number or null`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `source: WorkspaceRateLimitWorkspaceSource or WorkspaceRateLimitOrganizationSource`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `WorkspaceRateLimitWorkspaceSource object`

        - `type: "workspace"`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `WorkspaceRateLimitOrganizationSource object`

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

## Example

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

### Response (200)

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
