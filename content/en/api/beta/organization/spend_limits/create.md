---
title: Set Spend Limit
url: https://platform.claude.com/docs/en/api/beta/organization/spend_limits/create
---

# Set Spend Limit

**POST** `/v1/organizations/spend_limits`

Set a spend limit.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. A Claude Enterprise organization sets `user`
limits. Its seat-tier, group, and organization-level defaults are configured
in claude.ai. A Claude Console organization sets `organization` and
`workspace` limits, which are monthly and always carry an amount. Setting those
limits is in an early access preview. To request access, contact your
Anthropic account team.

## Body parameters

- `amount: string or null`

  Limit amount as a non-negative integer decimal string in the minor unit of the organization's billing currency (cents for USD): "50000" is $500.00. `null` sets an explicit no-limit override for this scope and `period` only — each period resolves independently, so caps for other periods still apply.

- `scope: User or Organization or Workspace`

  What the limit applies to. Claude Enterprise organizations set `user` limits. Claude Console organizations set `organization` and `workspace` limits. Any other combination returns 400. Setting `organization` and `workspace` limits through the API is in an early access preview. To request access, contact your Anthropic account team.

  - `User object`

    Scope selecting a single member of the organization.

    - `type: "user"`

      Scope type. Always `user` for this scope.

      default: user

    - `user_id: string`

      Tagged ID of the member the spend limit applies to.

  - `Organization object`

    - `type: "organization"`

      default: organization

  - `Workspace object`

    Scope selecting one workspace of a Claude Console organization.

    - `type: "workspace"`

      Scope type. Always `workspace` for this scope.

      default: workspace

    - `workspace_id: string`

      Tagged ID of the workspace the spend limit applies to.

- `period: optional "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

## Returns

- `BetaSpendLimit object`

  A configured spend limit: a cap on metered spend for one scope and period.

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

  - `period: "daily" or "monthly" or "weekly"`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: User or SeatTier or RBACGroup or 3 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `User object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SeatTier object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `RBACGroup object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `OrganizationService object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `Organization object`

      - `type: "organization"`

        default: organization

    - `Workspace object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "amount": "50000",
          "scope": {
            "type": "user",
            "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
          },
          "period": "monthly"
        }'
```

### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```
