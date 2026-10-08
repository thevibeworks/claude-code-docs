---
title: List Spend Limits
url: https://platform.claude.com/docs/en/api/beta/organization/spend_limits/list
---

# List Spend Limits

**GET** `/v1/organizations/spend_limits`

List the organization's spend limits.

A Claude Console organization's limits come in an order that is stable across
pages. A Claude Enterprise organization's are grouped by scope type,
in the order `organization`, `seat_tier`, `rbac_group`,
`organization_service`, `user`; within a type they come in a fixed order that
is not creation order.

## Query parameters

- `limit: optional number`

  Maximum number of limits per page. Defaults to `20`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `scope_type: optional array of "organization" or "organization_service" or "rbac_group" or 3 more`

  Return only limits with these scope types. A Claude Console organization has `organization` and `workspace` limits; a Claude Enterprise organization has `organization`, `seat_tier`, `rbac_group`, `organization_service` and `user` limits. Omit for all.

  maxItems: 100

  - `"organization"`

  - `"organization_service"`

  - `"rbac_group"`

  - `"seat_tier"`

  - `"user"`

  - `"workspace"`

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `spend-limit-reads-2026-09-26` in this header.

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

- `data: array of BetaSpendLimit`

  - `type: "spend_limit"`

    Object type. Always `spend_limit`.

    default: spend_limit

  - `id: string`

    Unique tagged ID of the spend limit (`spl_...`).

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `is_enabled: boolean`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: BetaSpendLimitUserScope or BetaSpendLimitSeatTierScope or BetaSpendLimitRBACGroupScope or 3 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `BetaSpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `BetaSpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `BetaSpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `BetaSpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `BetaSpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `BetaSpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

- `next_page: string or null`

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: spend-limit-reads-2026-09-26' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "amount": "50000",
      "created_at": "2019-12-27T18:11:19.117Z",
      "currency": "USD",
      "is_enabled": true,
      "period": "daily",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "type": "spend_limit",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```
