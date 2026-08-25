# Deny Spend Limit Increase Request

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

## Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

## Body parameters

- `suppress_notification: optional boolean`

## Returns

- `SpendLimitIncreaseRequest object`

  - `id: string`

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

  - `created_at: string`

    format: date-time

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: object or object or null`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `UserActor object`

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

    - `ScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (GET /spend_limits/effective).

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

  - `status: "approved" or "denied" or "pending"`

    - `"approved"`

    - `"denied"`

    - `"pending"`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/deny \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "monthly",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_id"
  },
  "spend_summary": {
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
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```
