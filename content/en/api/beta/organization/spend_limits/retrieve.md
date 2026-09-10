---
title: Get Spend Limit
url: https://platform.claude.com/docs/en/api/beta/organization/spend_limits/retrieve
---

# Get Spend Limit

**GET** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

## Path parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

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

  - `scope: object or object or object or 2 more`

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

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
