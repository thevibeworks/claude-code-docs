# List Effective Spend Limits

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

## Query parameters

- `limit: optional number`

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

- `period: optional array of string`

  maxItems: 3

- `user_ids: optional array of string`

  maxItems: 100

## Returns

- `data: array of SpendSummary`

  - `actor: object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

      default: false

    - `email_address: string or null`

    - `name: string or null`

    - `type: "user_actor"`

      default: user_actor

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

  - `scope: object`

    - `type: "user"`

      default: user

    - `user_id: string`

  - `source: object or object or object or 2 more`

    - `User object`

      - `type: "user"`

        default: user

      - `user_id: string`

    - `SeatTier object`

      - `seat_tier: string`

      - `type: "seat_tier"`

        default: seat_tier

    - `RbacGroup object`

      - `rbac_group_id: string`

      - `type: "rbac_group"`

        default: rbac_group

    - `OrganizationService object`

      - `service: string`

      - `type: "organization_service"`

        default: organization_service

    - `Organization object`

      - `type: "organization"`

        default: organization

  - `spend_limit_id: string`

- `next_page: string or null`

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

### Response (200)

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
