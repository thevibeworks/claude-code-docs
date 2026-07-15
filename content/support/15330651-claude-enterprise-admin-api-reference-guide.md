# Claude Enterprise Admin API reference guide

This guide covers **spend limits** and **spend limit increase requests** for your Claude Enterprise organization using the Claude Enterprise Admin API. Spend limits let you cap each member's usage credit spending over a recurring period, see where each member's limit is inherited from, and review or act on members' requests for a higher limit.

For per-user and time-bucketed usage and cost reporting, see the **[Analytics API reference guide](https://platform.claude.com/docs/en/api/admin/analytics)**.

Claude Enterprise Admin API is currently in public beta and available to organizations on Enterprise plans with usage credits enabled.

## Overview

There are eight endpoints across two resources:

| **Resource**                      | **Endpoints**                                                                                                                                                                                                                                                  | **Use for**                                                                                                 |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Spend limits**                  | `GET /v1/organizations/spend_limits/effective`<br>`GET /v1/organizations/spend_limits/{spend_limit_id}`<br>`POST /v1/organizations/spend_limits`<br>`DELETE /v1/organizations/spend_limits/{spend_limit_id}`                                                   | Read each member's effective limit and period-to-date spend; set or clear a per-user override.              |
| **Spend limit increase requests** | `GET /v1/organizations/spend_limit_increase_requests`<br>`GET /v1/organizations/spend_limit_increase_requests/{id}`<br>`POST /v1/organizations/spend_limit_increase_requests/{id}/approve`<br>`POST /v1/organizations/spend_limit_increase_requests/{id}/deny` | List members' requests for a higher limit, with the context needed to decide; approve or deny each request. |

Use the **spend limits** endpoints to answer, “What limit applies to each member, where does it come from, and how close are they to it?" and to set a per-user override. Use the **spend limit increase requests** endpoints to work the queue of member-submitted requests.

## Prerequisites and authentication

- Your organization must be on a Claude Enterprise plan.

- Usage credits must be enabled for your organization. Your Primary Owner can enable this under **Billing settings** in Claude.

- The Primary Owner needs to mint an Admin API key with one or both of the following scopes:

  - **`read:spend_limits`** (required for all `GET` endpoints)

  - **`write:spend_limits`** (required for `POST` and `DELETE` endpoints)

Pass the key in the **`x-api-key`** header on every request.

**Important:** Don't share API keys publicly or check them into source control.

## Create an Admin API key for your Claude Enterprise organization

1. **Sign in as the Primary Owner**—Only the Primary Owner of your Claude Enterprise parent organization can create these keys.

2. **Open API settings**—Go to **[Organization settings > API](https://claude.ai/admin-settings/api-access)** and find the **Keys** section.

3. **Click and create key**—Name the key and select the scopes you need from the **[scopes table](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#choose-scopes-for-a-claude-enterprise-key)**. You can combine scopes from different APIs (for example, `read:analytics` and `read:spend_limits`) on a single key.

4. **Copy and store the secret**—Copy the displayed secret (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is shown only once.

## Base URL

```
https://api.anthropic.com
```

## Rate limiting

All eight endpoints share a single per-organization limit of **60 requests per minute**. Requests over the limit return **429 Too Many Requests**.

## Pagination

`GET /v1/organizations/spend_limits/effective` and `GET /v1/organizations/spend_limit_increase_requests` are paginated with an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor. Pass that cursor unchanged as the `page` parameter on the next request, and repeat until `next_page` is `null`.

**Important:** Don’t change query parameters mid-sequence. Cursors are bound to the filters that issued them. If you change `user_ids[]`, `status[]`, or `actor_ids[]` and pass an old cursor, you'll get a 400 with "cursor does not match current query parameters". Start a new sequence from the first page instead.

Treat the cursor string as opaque: don't parse, modify, or construct it yourself.

## Serializing list parameters

List parameters use bracket notation: repeat the parameter name with `[]` for each value.

```
user_ids[]=user_01AbCdEfGh&user_ids[]=user_01JkLmNoPq
```

## Error responses

| **Status** | **Meaning**                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400        | Invalid input, unsupported parameter value, page cursor does not match current parameters, or a precondition is not met (see per-endpoint Validations). |
| 401        | Missing `x-api-key` header.                                                                                                                             |
| 403        | API key is missing the required scope (`read:spend_limits` or `write:spend_limits`).                                                                    |
| 404        | Resource not found, or API key is unknown, expired, or revoked.                                                                                         |
| 429        | Rate limit exceeded.                                                                                                                                    |
| 500        | Internal error.                                                                                                                                         |

Error bodies have the shape:

```
{"type": "error", "error": {"type": "<error_type>", "message": "..."}, "request_id": "req_..."}
```

`error.type` is a status-dependent discriminator: `invalid_request_error` (400), `authentication_error` (401), `permission_error` (403), `not_found_error` (404), `rate_limit_error` (429), `api_error` (500). `request_id` is always present and is the value to quote when contacting support. The Validations table under each endpoint lists the specific messages.

---

## Concepts

### The spend limit hierarchy

Each member's usage credit spending is capped by an **effective spend limit**, resolved from a hierarchy of scope levels. When a member has no per-user override, they inherit the limit configured for their seat tier, their group (if your organization uses group-based limits), or the organization-wide default.

Reading `GET /v1/organizations/spend_limits/effective` returns every current member with their resolved effective limit, where that limit was resolved from (`source`), and their period-to-date spend. Setting a per-user override via `POST /v1/organizations/spend_limits` pins a member to a specific limit regardless of what they would otherwise inherit. Deleting the override returns them to the inherited limit.

### Scope

A scope identifies the level a spend limit is written or resolved at:

| **Type**       | **Fields**      | **Meaning**                                                                                                                                                   |
| -------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user`         | `user_id`       | A specific member. `user_id` matches the IDs returned by the Admin API users endpoints.                                                                       |
| `seat_tier`    | `seat_tier`     | A seat tier default. `seat_tier` values are fully-qualified identifiers such as `enterprise_standard` or `enterprise_tier_1`; additional values may be added. |
| `rbac_group`   | `rbac_group_id` | A group default, when your organization manages limits by group.                                                                                              |
| `organization` | —               | The organization-wide default.                                                                                                                                |

`scope.type` is an open string. Clients should treat unknown values as opaque and fall through rather than fail. Additional scope types may be added in future.

### Period

`period` is the recurring window over which the limit is enforced and spend resets. The only value today is `"monthly"`.

`period` is an open string. Clients should treat unknown values as opaque and fall through rather than fail. Additional period values may be added in the future.

### Amounts and currency

All monetary values are strings in **minor units of the organization's billing currency** (cents, for USD). For example, `"50000"` represents 500.00 USD. Parse as a decimal and divide by 100 to display dollars. Avoid binary floating-point for large values.

`amount` is **nullable**: `null` means **unlimited** (no limit). `"0"` means usage credits are **disabled** for that member.

`period_to_date_spend` is the member's usage credit accrued since the start of the current `period`, in the same minor-unit format. It may include a fractional part (for example, `"41280.125"`).

### Increase request lifecycle

A **spend limit increase request** is created when a member clicks "request more usage" in claude.ai. Requests are not created via this API.

| **Status** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pending`  | Awaiting admin action. The request normally carries a live `spend_summary` so you can see the member's current effective limit and period-to-date spend while deciding. `spend_summary` may be `null` if it couldn’t be computed, so handle that case.                                                                                                                                                     |
| `approved` | The request was resolved with approval: either an admin approved it explicitly (writing a per-user spend limit at the admin-supplied amount), another admin action made usage credits available to the member (for example, raising a seat-tier limit or enabling usage credit billing for the organization), or Anthropic support raised a limit on the organization's behalf. `spend_summary` is `null`. |
| `denied`   | An admin declined. `spend_summary` is `null`. Claude.ai hides that member's request button for 30 days from `resolved_at`; an admin can still raise the member's limit directly at any time.                                                                                                                                                                                                               |

Both `approved` and `denied` are terminal. A member has at most one `pending` request at a time.

Approving via `POST …/approve` writes the same per-user spend limit row that `POST /v1/organizations/spend_limits` writes. Setting a spend limit directly does *not* transition a pending request. Use the approve endpoint to resolve a request.

By default, Anthropic emails the member when their request is approved or denied. Pass `suppress_notification: true` on approve or deny to suppress that email (for example, when your own system notifies the member).

---

## The SpendLimit object

A configured limit at one scope level.

```
{
  "type": "spend_limit",
  "id": "spl_01AbCdEfGhIjKlMnOpQrSt",
  "created_at": "2026-05-01T12:00:00Z",
  "updated_at": "2026-05-03T09:14:11Z",
  "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
  "amount": "50000",
  "currency": "USD",
  "period": "monthly"
}
```

| **Field**    | **Type**          | **Description**                                                                 |
| ------------ | ----------------- | ------------------------------------------------------------------------------- |
| `type`       | string            | Always `"spend_limit"`.                                                         |
| `id`         | string            | Prefixed `spl_`.                                                                |
| `created_at` | string (RFC 3339) | When this limit was first set.                                                  |
| `updated_at` | string (RFC 3339) | When this limit was last changed.                                               |
| `scope`      | Scope             | The level this limit is written at. See the "Scope" section.                    |
| `amount`     | string or null    | Limit for the `period`, in minor units. `null` means unlimited.                 |
| `currency`   | string            | ISO 4217. The organization's billing currency.                                  |
| `period`     | string            | The recurring window over which `amount` is enforced. See the "Period" section. |

## The SpendSummary object

A computed per-member report row: the member's effective limit, where it came from, and their period-to-date spend. Not an addressable resource (no `id`).

```
{
  "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
  "amount": "50000",
  "currency": "USD",
  "period": "monthly",
  "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
  "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
  "period_to_date_spend": "31402.5"
}
```

| **Field**              | **Type**               | **Description**                                                                                                        |
| ---------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `scope`                | Scope (`type: "user"`) | The member this row is for.                                                                                            |
| `amount`               | string or null         | The effective limit for the `period`, in minor units. `null` means unlimited; `"0"` means usage credits are disabled.  |
| `currency`             | string                 | ISO 4217.                                                                                                              |
| `period`               | string                 | The period of the spend limit that `source` resolved to. See the "Period" section.                                     |
| `source`               | Scope                  | Where `amount` was resolved from in the hierarchy. Equals `scope` when the member has a per-user override.             |
| `spend_limit_id`       | string                 | ID of the `SpendLimit` that `source` resolved to. Fetch it with `GET /v1/organizations/spend_limits/{spend_limit_id}`. |
| `period_to_date_spend` | string                 | The member's usage credits accrued since the start of the current `period`, in minor units.                            |

## The SpendLimitIncreaseRequest object

```
{
  "type": "spend_limit_increase_request",
  "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
  "created_at": "2026-05-04T16:22:09Z",
  "status": "pending",
  "resolved_at": null,
  "resolved_by": null,
  "actor": {
    "type": "user_actor",
    "user_id": "user_01AbCdEfGh",
    "name": "Jane Smith",
    "email_address": "jane@example.com"
  },
  "spend_summary": {
    "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
    "amount": "50000",
    "currency": "USD",
    "period": "monthly",
    "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
    "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
    "period_to_date_spend": "48900"
  }
}
```

| **Field**       | **Type**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`          | string                    | Always `"spend_limit_increase_request"`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `id`            | string                    | Prefixed `slir_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_at`    | string (RFC 3339)         | When the member submitted the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `status`        | string                    | `pending`, `approved`, or `denied`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `resolved_at`   | string (RFC 3339) or null | When the request was approved or denied. `null` while pending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `resolved_by`   | Actor or null             | Who approved or denied the request: either a `user_actor` (an admin acted in claude.ai) or a `scoped_api_key_actor` (resolved via this API). When a request is auto-resolved by an admin action in claude.ai (for example, raising a seat-tier limit, enabling usage credit billing for the organization, or raising the member's limit), `resolved_by` is the acting admin's `user_actor`. `null` while pending, when the resolving admin's account has since been deleted, or when the request was resolved by Anthropic support. A `scoped_api_key_actor` may reference a key that has since been deleted or revoked. Treat `scoped_api_key_id` as a historical reference and tolerate lookup failures. |
| `actor`         | Actor (`user_actor`)      | The member who submitted the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `spend_summary` | SpendSummary or null      | Live decision context for the requester: their effective limit and period-to-date spend. Present while `status` is pending (may be `null` if the summary couldn’t be computed); always `null` once resolved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Actor

| **Field**           | **Type**       | **Description**                                                                                                  |
| ------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------- |
| `type`              | string         | `user_actor` or `scoped_api_key_actor`.                                                                          |
| `user_id`           | string         | Present on `user_actor`. The user's ID; same value accepted by `actor_ids[]`.                                    |
| `name`              | string or null | Present on `user_actor`. The user's name; `null` if the account has been deleted or the user has not set a name. |
| `email_address`     | string or null | Present on `user_actor`. The user's email; `null` if the account has been deleted.                               |
| `scoped_api_key_id` | string         | Present on `scoped_api_key_actor`. Prefixed `apikey_`.                                                           |

---

## Spend limits

### 1. List effective spend limits

```
GET /v1/organizations/spend_limits/effective
```

Returns **every current member** of the organization with their resolved effective limit and period-to-date spend. Members without a per-user override appear with `source.type` of `seat_tier`, `rbac_group`, or `organization`. Ex-members aren’t listed.

Requires scope: `read:spend_limits.`

#### Query parameters

| **Field**    | **Type**                | **Required** | **Default** | **Description**                                                                                                           |
| ------------ | ----------------------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| `user_ids[]` | string, max 100 entries | No           | all members | Narrow to specific members. Accepts `user_...` IDs. An entry that isn’t a current member is silently omitted from `data`. |
| `limit`      | integer 1–1000          | No           | 20          | Rows per page.                                                                                                            |
| `page`       | opaque cursor string    | No           | —           | The `next_page` value from a previous response.                                                                           |

#### Response fields

| **Field**   | **Type**              | **Description**                                                                          |
| ----------- | --------------------- | ---------------------------------------------------------------------------------------- |
| `data`      | array of SpendSummary | One entry per member, ordered by when the member joined the organization (newest first). |
| `next_page` | string or null        | Opaque cursor for the next page; `null` when no more pages.                              |

#### Example request

```
curl "https://api.anthropic.com/v1/organizations/spend_limits/effective?limit=20" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Example response

```
{
  "data": [
    {
      "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly",
      "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
      "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
      "period_to_date_spend": "31402.5"
    }
  ],
  "next_page": "page_..."
}
```

#### Validations

| **Condition**                                     | **Status** | **Message**                                                 |
| ------------------------------------------------- | ---------- | ----------------------------------------------------------- |
| `user_ids[]` entry malformed                      | 400        | `user_ids[]: entry is not a valid user ID`                  |
| `user_ids[]` has more than 100 entries            | 400        |                                                             |
| `limit` outside 1–1000                            | 400        |                                                             |
| `page` cursor invalid                             | 400        | `page: invalid cursor`                                      |
| `page` cursor does not match current `user_ids[]` | 400        | `page: cursor does not match current query parameters`      |
| `page` cursor from a different API version        | 400        | `page: cursor was issued by a different API version`        |
| Organization is not on an Enterprise plan         | 400        | `this endpoint is not supported for this organization type` |
| Usage credit billing not enabled                  | 400        | `overage billing is not enabled for this organization`      |

---

### 2. Get a spend limit

```
GET /v1/organizations/spend_limits/{spend_limit_id}
```

Returns a single spend limit by ID. Use this to inspect the row that a `SpendSummary.spend_limit_id` or a `POST` response referenced.

Requires scope: `read:spend_limits`.

#### Path parameters

| **Field**        | **Type** | **Description**  |
| ---------------- | -------- | ---------------- |
| `spend_limit_id` | string   | Prefixed `spl_`. |

#### Response

A SpendLimit object.

#### Example request

```
curl "https://api.anthropic.com/v1/organizations/spend_limits/spl_01AbCdEfGhIjKlMnOpQrSt" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Validations

| **Condition**                                   | **Status** | **Message**                                                 |
| ----------------------------------------------- | ---------- | ----------------------------------------------------------- |
| `spend_limit_id` not found in this organization | 404        |                                                             |
| Organization is not on an Enterprise plan       | 400        | `this endpoint is not supported for this organization type` |
| Usage credit billing not enabled                | 400        | `overage billing is not enabled for this organization`      |

---

### 3. Set a spend limit

```
POST /v1/organizations/spend_limits
```

Sets a **per-user** spend limit override. Upsert: setting a limit for a user who already has one overwrites it in place.

Only `scope.type: "user"` is accepted. Seat-tier, group, and organization-level defaults are configured in claude.ai settings.

Setting a spend limit directly does *not* transition a member's pending increase request. Use the approve endpoint to resolve a request.

Requires scope: `write:spend_limits`.

#### Request body

| **Field** | **Type**       | **Required** | **Description**                                                                                                                                                         |
| --------- | -------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`   | object         | Yes          | `{ "type": "user", "user_id": "user_..." }`.                                                                                                                            |
| `amount`  | string or null | Yes          | New limit for the `period`, in minor units, as a non-negative integer decimal string. `"0"` disables usage credit for the member. `null` removes the limit (unlimited). |
| `period`  | string         | No           | Default `"monthly"`. See the "Period" section.                                                                                                                          |

#### Response

A SpendLimit object reflecting the written override.

#### Example request

```
curl -X POST "https://api.anthropic.com/v1/organizations/spend_limits" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "content-type: application/json" \
  -d '{"scope": {"type": "user", "user_id": "user_01AbCdEfGh"}, "amount": "75000"}'
```

#### Example response

```
{
  "type": "spend_limit",
  "id": "spl_01RsTuVwXyZaBcDeFgHiJk",
  "created_at": "2026-05-11T10:02:44Z",
  "updated_at": "2026-05-11T10:02:44Z",
  "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
  "amount": "75000",
  "currency": "USD",
  "period": "monthly"
}
```

#### Validations

| **Condition**                                                | **Status** | **Message**                                                 |
| ------------------------------------------------------------ | ---------- | ----------------------------------------------------------- |
| `scope.type` is not `"user"`                                 | 400        | `scope.type: not yet supported`                             |
| `scope.user_id` malformed                                    | 400        | `scope.user_id: malformed`                                  |
| `scope.user_id` not a member of this organization            | 400        | `scope.user_id: not a member of this organization`          |
| `amount` negative, fractional, or not a valid decimal string | 400        |                                                             |
| `period` is not `"monthly"`                                  | 400        | `period: not yet supported`                                 |
| Organization is not on an Enterprise plan                    | 400        | `this endpoint is not supported for this organization type` |
| Usage credit billing not enabled                             | 400        | `overage billing is not enabled for this organization`      |

---

### 4. Remove a spend limit

```
DELETE /v1/organizations/spend_limits/{spend_limit_id}
```

Removes a **per-user** override so the member falls back to the inherited limit (seat tier, group, or organization default). Seat-tier, group, and organization-level rows can’t be deleted via this endpoint.

Requires scope: `write:spend_limits`.

#### Path parameters

| **Field**        | **Type** | **Description**                                         |
| ---------------- | -------- | ------------------------------------------------------- |
| `spend_limit_id` | string   | Prefixed `spl_`. Must be the ID of a per-user override. |

#### Response

```
{ "type": "spend_limit_deleted", "id": "spl_01RsTuVwXyZaBcDeFgHiJk" }
```

#### Example request

```
curl -X DELETE "https://api.anthropic.com/v1/organizations/spend_limits/spl_01RsTuVwXyZaBcDeFgHiJk" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Validations

| **Condition**                                               | **Status** | **Message**                                                    |
| ----------------------------------------------------------- | ---------- | -------------------------------------------------------------- |
| `spend_limit_id` not found in this organization             | 404        |                                                                |
| `spend_limit_id` is a seat-tier, group, or organization row | 400        | `Only per-user spend limits can be deleted via this endpoint.` |
| Organization is not on an Enterprise plan                   | 400        | `this endpoint is not supported for this organization type`    |
| Usage credit billing not enabled                            | 400        | `overage billing is not enabled for this organization`         |

---

## Spend limit increase requests

### 5. List increase requests

```
GET /v1/organizations/spend_limit_increase_requests
```

Lists increase requests, most recent first. Requests whose requester is no longer a member of the organization are excluded.

Requires scope: `read:spend_limits`.

#### Query parameters

| **Field**     | **Type**                                       | **Required** | **Default** | **Description**                                             |
| ------------- | ---------------------------------------------- | ------------ | ----------- | ----------------------------------------------------------- |
| `status[]`    | one or more of `pending`, `approved`, `denied` | No           | all         | Filter by status. Repeat the parameter for multiple values. |
| `actor_ids[]` | string                                         | No           | all         | Filter by requester. Accepts `user_...` IDs.                |
| `limit`       | integer 1–1000                                 | No           | 20          | Rows per page.                                              |
| `page`        | opaque cursor string                           | No           | —           | The `next_page` value from a previous response.             |

#### Response fields

| **Field**   | **Type**                           | **Description**                                             |
| ----------- | ---------------------------------- | ----------------------------------------------------------- |
| `data`      | array of SpendLimitIncreaseRequest | Ordered by `created_at` descending.                         |
| `next_page` | string or null                     | Opaque cursor for the next page; `null` when no more pages. |

#### Example request

```
curl "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests?status[]=pending&limit=50" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Example response

```
{
  "data": [
    {
      "type": "spend_limit_increase_request",
      "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
      "created_at": "2026-05-04T16:22:09Z",
      "status": "pending",
      "resolved_at": null,
      "resolved_by": null,
      "actor": {
        "type": "user_actor",
        "user_id": "user_01AbCdEfGh",
        "name": "Jane Smith",
        "email_address": "jane@example.com"
      },
      "spend_summary": {
        "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
        "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
        "period_to_date_spend": "48900"
      }
    }
  ],
  "next_page": null
}
```

#### Validations

| **Condition**                                                    | **Status** | **Message**                                                             |
| ---------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------- |
| `actor_ids[]` entry malformed                                    | 400        | `actor_ids[]: invalid tagged user ID`                                   |
| `limit` outside 1–1000                                           | 400        |                                                                         |
| `page` cursor malformed                                          | 400        | `invalid page cursor format` or `invalid page cursor`                   |
| `page` cursor does not match current `status[]` or `actor_ids[]` | 400        | `page cursor does not match current query parameters`                   |
| `page` cursor from a different API version                       | 400        | `page cursor was issued by a different API version; restart pagination` |
| Organization is not on an Enterprise plan                        | 400        | `this endpoint is not supported for this organization type`             |
| Usage credit billing not enabled                                 | 400        | `overage billing is not enabled for this organization`                  |

---

### 6. Get an increase request

```
GET /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}
```

Returns a single increase request.

Requires scope: `read:spend_limits`.

#### Path parameters

| **Field**                         | **Type** | **Description**   |
| --------------------------------- | -------- | ----------------- |
| `spend_limit_increase_request_id` | string   | Prefixed `slir_`. |

#### Response

A SpendLimitIncreaseRequest object.

#### Example request

```
curl "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

#### Validations

| **Condition**                                        | **Status** | **Message**                                                 |
| ---------------------------------------------------- | ---------- | ----------------------------------------------------------- |
| Request not found in this organization               | 404        |                                                             |
| Requester is no longer a member of this organization | 404        |                                                             |
| Organization is not on an Enterprise plan            | 400        | `this endpoint is not supported for this organization type` |
| Usage credit billing not enabled                     | 400        | `overage billing is not enabled for this organization`      |

---

### 7. Approve an increase request

```
POST /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve
```

Approves a pending request. Writes a **per-user spend limit** at `amount` for the requester and transitions the request to `approved`. The request doesn’t carry a requested amount, the admin supplies the new limit on approval.

Requires scope: `write:spend_limits`.

#### Path parameters

| **Field**                         | **Type** | **Description**   |
| --------------------------------- | -------- | ----------------- |
| `spend_limit_increase_request_id` | string   | Prefixed `slir_`. |

#### Request body

| **Field**               | **Type** | **Required** | **Default** | **Description**                                                                                |
| ----------------------- | -------- | ------------ | ----------- | ---------------------------------------------------------------------------------------------- |
| `amount`                | string   | Yes          | —           | New per-user limit for the `period`, in minor units, as a non-negative integer decimal string. |
| `period`                | string   | No           | `"monthly"` | See the "Period" section.                                                                      |
| `suppress_notification` | boolean  | No           | `false`     | If `true`, Anthropic doesn’t email the member that their request was approved.                 |

#### Response

The SpendLimitIncreaseRequest in status `approved`, with an additional `spend_limit` field containing the SpendLimit that was written.

#### Example request

```
curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/approve" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "content-type: application/json" \
  -d '{"amount": "75000", "suppress_notification": true}'
```

#### Example response

```
{
  "type": "spend_limit_increase_request",
  "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
  "created_at": "2026-05-04T16:22:09Z",
  "status": "approved",
  "resolved_at": "2026-05-11T10:05:02Z",
  "resolved_by": {
    "type": "scoped_api_key_actor",
    "scoped_api_key_id": "apikey_01ZyXwVuTsRqPoNmLkJiHg"
  },
  "actor": {
    "type": "user_actor",
    "user_id": "user_01AbCdEfGh",
    "name": "Jane Smith",
    "email_address": "jane@example.com"
  },
  "spend_summary": null,
  "spend_limit": {
    "type": "spend_limit",
    "id": "spl_01RsTuVwXyZaBcDeFgHiJk",
    "created_at": "2026-05-11T10:05:02Z",
    "updated_at": "2026-05-11T10:05:02Z",
    "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
    "amount": "75000",
    "currency": "USD",
    "period": "monthly"
  }
}
```

#### Validations

| **Condition**                                                | **Status** | **Message**                                                 |
| ------------------------------------------------------------ | ---------- | ----------------------------------------------------------- |
| Request not found in this organization                       | 404        |                                                             |
| Requester is no longer a member of this organization         | 404        |                                                             |
| Request already `approved` or `denied`                       | 400        | `spend limit increase request is already resolved`          |
| `amount` negative, fractional, or not a valid decimal string | 400        |                                                             |
| `period` is not `"monthly"`                                  | 400        | `period: not yet supported`                                 |
| Organization is not on an Enterprise plan                    | 400        | `this endpoint is not supported for this organization type` |
| Usage credit billing not enabled                             | 400        | `overage billing is not enabled for this organization`      |

---

### 8. Deny an increase request

```
POST /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny
```

Denies a pending request. Idempotent on `denied`: denying an already-denied request returns 200 with the existing resource. Denying an already-approved request is rejected so automation can distinguish a retry from a conflicting decision.

Requires scope: `write:spend_limits`.

#### Path parameters

| **Field**                         | **Type** | **Description**   |
| --------------------------------- | -------- | ----------------- |
| `spend_limit_increase_request_id` | string   | Prefixed `slir_`. |

#### Request body

| **Field**               | **Type** | **Required** | **Default** | **Description**                                                              |
| ----------------------- | -------- | ------------ | ----------- | ---------------------------------------------------------------------------- |
| `suppress_notification` | boolean  | No           | `false`     | If `true`, Anthropic doesn’t email the member that their request was denied. |

#### Response

A SpendLimitIncreaseRequest in status denied.

#### Example request

```
curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/deny" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "content-type: application/json" \
  -d '{"suppress_notification": true}'
```

#### Validations

| **Condition**                                        | **Status**          | **Message**                                                 |
| ---------------------------------------------------- | ------------------- | ----------------------------------------------------------- |
| Request not found in this organization               | 404                 |                                                             |
| Requester is no longer a member of this organization | 404                 |                                                             |
| Request already `approved`                           | 400                 | `spend limit increase request is already approved`          |
| Request already `denied`                             | — (200, idempotent) |                                                             |
| Organization is not on an Enterprise plan            | 400                 | `this endpoint is not supported for this organization type` |
| Usage credits not enabled                            | 400                 | `overage billing is not enabled for this organization`      |