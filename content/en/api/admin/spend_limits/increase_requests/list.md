# List Spend Limit Increase Requests

**GET** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

## Query parameters

- `actor_ids: optional array of string`

  Filter by requester, as `user_...` tagged IDs.

- `limit: optional number`

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `status: optional array of "approved" or "denied" or "pending"`

  Filter by status. Omit to return all.

  - `"approved"`

  - `"denied"`

  - `"pending"`

## Returns

- `data: array of SpendLimitIncreaseRequest`

  - `id: string`

  - `actor: object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `deleted: boolean`

      True only when the underlying account has been deleted.

      default: false

    - `email_address: string or null`

      The user's email address. Null when the account is unavailable or has been deleted.

    - `name: string or null`

      The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

    - `type: "user_actor"`

      Actor type. Always `user_actor`.

      default: user_actor

    - `user_id: string`

      Tagged ID of the user.

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

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `user_id: string`

        Tagged ID of the user.

    - `ScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `scoped_api_key_id: string`

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `user_id: string`

        Tagged ID of the user.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: "daily" or "monthly" or "weekly"`

      Period this row's effective limit and spend are reported for.

      - `"daily"`

      - `"monthly"`

      - `"weekly"`

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `source: object or object or object or 2 more`

      Scope selecting a single member of the organization.

      - `User object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

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

- `next_page: string or null`

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "monthly",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```
