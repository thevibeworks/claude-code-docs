# Spend Limits

## Set Spend Limit

**POST** `/v1/organizations/spend_limits`

Set a per-user spend limit override.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. Only `scope.type: "user"` is accepted; seat-tier,
group, and organization-level defaults are configured in claude.ai.

### Body parameters

- `amount: string or null`

  Limit amount as a non-negative integer decimal string in the minor unit of the organization's billing currency (cents for USD): "50000" is $500.00. `null` sets an explicit no-limit override for this scope and `period` only — each period resolves independently, so caps for other periods still apply.

- `scope: object`

  - `type: "user"`

    default: user

  - `user_id: string`

- `period: optional "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

### Returns

- `SpendLimit object`

  - `id: string`

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object or object or object or 2 more`

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

  - `type: "spend_limit"`

    default: spend_limit

  - `updated_at: string`

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "scope": {
            "type": "user",
            "user_id": "user_id"
          },
          "period": "monthly"
        }'
```

#### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Get Spend Limit

**GET** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

### Path parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

### Returns

- `SpendLimit object`

  - `id: string`

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object or object or object or 2 more`

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

  - `type: "spend_limit"`

    default: spend_limit

  - `updated_at: string`

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "period": "monthly",
  "scope": {
    "type": "user",
    "user_id": "user_id"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Spend Limit

**DELETE** `/v1/organizations/spend_limits/{spend_limit_id}`

Delete a per-user spend limit override.

The member falls back to any inherited spend limit at that period.
Seat-tier, group, and organization-level rows cannot be deleted via
this endpoint.

### Path parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

### Returns

- `id: string`

- `type: "spend_limit_deleted"`

  default: spend_limit_deleted

### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

## List Effective Spend Limits

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

### Query parameters

- `limit: optional number`

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

- `period: optional array of string`

  maxItems: 3

- `user_ids: optional array of string`

  maxItems: 100

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

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

## Domain types

### Spend Limit

- `SpendLimit object`

  - `id: string`

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object or object or object or 2 more`

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

  - `type: "spend_limit"`

    default: spend_limit

  - `updated_at: string`

    format: date-time

### Spend Summary

- `SpendSummary object`

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

### Spend Limit Delete Response

- `SpendLimitDeleteResponse object`

  - `id: string`

  - `type: "spend_limit_deleted"`

    default: spend_limit_deleted

## Spend Limits › Increase Requests

### List Spend Limit Increase Requests

**GET** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

#### Query parameters

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

#### Returns

- `data: array of SpendLimitIncreaseRequest`

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

- `next_page: string or null`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

##### Response (200)

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
  ],
  "next_page": "next_page"
}
```

### Get Spend Limit Increase Request

**GET** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}`

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the
requester at the request's period.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

##### Response (200)

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

### Approve Spend Limit Increase Request

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Body parameters

- `amount: string`

  New per-user spend limit as a non-negative integer decimal string (minor units).

- `period: optional "daily" or "monthly" or "weekly" or null`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `suppress_notification: optional boolean`

#### Returns

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

- `spend_limit: SpendLimit`

  - `id: string`

  - `amount: string or null`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `created_at: string`

    format: date-time

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `period: "daily" or "monthly" or "weekly"`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: object or object or object or 2 more`

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

  - `type: "spend_limit"`

    default: spend_limit

  - `updated_at: string`

    format: date-time

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "amount": "50000",
          "period": "monthly"
        }'
```

##### Response (200)

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
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "period": "monthly",
    "scope": {
      "type": "user",
      "user_id": "user_id"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
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

### Deny Spend Limit Increase Request

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

#### Path parameters

- `spend_limit_increase_request_id: string`

  ID of the spend limit increase request.

#### Body parameters

- `suppress_notification: optional boolean`

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/deny \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

##### Response (200)

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
