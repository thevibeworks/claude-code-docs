---
title: List Effective Spend Limits
url: https://platform.claude.com/docs/en/api/admin/spend_limits/list_effective
---

## List Effective Spend Limits

**get** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

### Query Parameters

- `limit: optional number`

- `page: optional string`

- `period: optional array of string`

- `user_ids: optional array of string`

### Returns

- `data: array of SpendSummary`

  - `actor: object { deleted, email_address, name, 2 more }`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

    - `email_address: string or null`

    - `name: string or null`

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: object { type, user_id }`

    - `type: "user"`

      - `"user"`

    - `user_id: string`

  - `source: object { type, user_id }  or object { seat_tier, type }  or object { rbac_group_id, type }  or 2 more`

    - `User object { type, user_id }`

      - `type: "user"`

        - `"user"`

      - `user_id: string`

    - `SeatTier object { seat_tier, type }`

      - `seat_tier: string`

      - `type: "seat_tier"`

        - `"seat_tier"`

    - `RbacGroup object { rbac_group_id, type }`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        - `"rbac_group"`

    - `OrganizationService object { service, type }`

      - `service: string`

      - `type: "organization_service"`

        - `"organization_service"`

    - `Organization object { type }`

      - `type: "organization"`

        - `"organization"`

  - `spend_limit_id: string`

- `next_page: string or null`

### Example

```http
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_id"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_id"
      },
      "source": {
        "type": "user",
        "user_id": "user_id"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```
