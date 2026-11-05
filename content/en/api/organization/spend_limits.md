---
title: Spend Limits
url: https://platform.claude.com/docs/en/api/organization/spend_limits
---

# Spend Limits

## Domain types

### Spend Limit

- `SpendLimit object`

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

  - `is_enabled: boolean`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: SpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

### Spend Limit Organization Scope

- `SpendLimitOrganizationScope object`

  - `type: "organization"`

    default: organization

### Spend Limit Organization Service Scope

- `SpendLimitOrganizationServiceScope object`

  - `type: "organization_service"`

    default: organization_service

  - `service: string`

### Spend Limit Period

- `SpendLimitPeriod = "daily" or "monthly" or "weekly"`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

### Spend Limit RBAC Group Scope

- `SpendLimitRBACGroupScope object`

  - `type: "rbac_group"`

    default: rbac_group

  - `rbac_group_id: string`

### Spend Limit Scoped API Key Actor

- `SpendLimitScopedAPIKeyActor object`

  A scoped Admin API key acting on behalf of the organization.

  - `type: "scoped_api_key_actor"`

    default: scoped_api_key_actor

  - `scoped_api_key_id: string`

### Spend Limit Seat Tier Scope

- `SpendLimitSeatTierScope object`

  - `type: "seat_tier"`

    default: seat_tier

  - `seat_tier: string`

### Spend Limit Usage Tier Scope

- `SpendLimitUsageTierScope object`

  Scope of the monthly spend cap Anthropic sets for a Claude Console
  organization from its usage tier, or a higher cap Anthropic granted the
  organization. Read-only; its `created_at` and `updated_at` are the
  organization's creation time, so `amount` can change while `updated_at` stays
  the same.

  - `type: "usage_tier"`

    Scope type. Always `usage_tier` for this scope.

    default: usage_tier

### Spend Limit User Actor

- `SpendLimitUserActor object`

  A user within the organization. `name` and `email_address` are
  null when the underlying account is unavailable or has been deleted;
  `deleted` is true only for deleted accounts.

  - `type: "user_actor"`

    Actor type. Always `user_actor`.

    default: user_actor

  - `deleted: boolean`

    True only when the underlying account has been deleted.

    default: false

  - `email_address: string or null`

    The user's email address. Null when the account is unavailable or has been deleted.

  - `name: string or null`

    The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

  - `user_id: string`

    Tagged ID of the user.

### Spend Limit User Scope

- `SpendLimitUserScope object`

  Scope selecting a single member of the organization.

  - `type: "user"`

    Scope type. Always `user` for this scope.

    default: user

  - `user_id: string`

    Tagged ID of the member the spend limit applies to.

### Spend Limit Workspace Scope

- `SpendLimitWorkspaceScope object`

  Scope selecting one workspace of a Claude Console organization.

  - `type: "workspace"`

    Scope type. Always `workspace` for this scope.

    default: workspace

  - `workspace_id: string`

    Tagged ID of the workspace the spend limit applies to.

### Spend Summary

- `SpendSummary object`

  Per-member effective-limit report row (`GET /spend_limits/effective`).

  - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: SpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `spend_limit_id: string`

## Spend Limits › Effective

### List Effective Spend Limits

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.
Supported for Claude Enterprise organizations only, not for Claude Console
organizations.

#### Query parameters

- `limit: optional number`

  Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page` field.

- `period: optional array of SpendLimitPeriod`

  Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

  maxItems: 3

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `user_ids: optional array of string`

  Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

  maxItems: 100

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of SpendSummary`

  - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: SpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `spend_limit_id: string`

- `next_page: string or null`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/effective \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```

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

  default: 20, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

- `status: optional array of SpendLimitIncreaseRequestStatus`

  Filter by status. Omit to return all.

  - `"approved"`

  - `"denied"`

  - `"pending"`

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `data: array of SpendLimitIncreaseRequest`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

- `next_page: string or null`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "daily",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "daily",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Returns

- `SpendLimitIncreaseRequest object`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
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
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `amount: string`

  New per-user spend limit as a non-negative integer decimal string (minor units).

- `period: optional SpendLimitPeriod or null`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `suppress_notification: optional boolean`

#### Returns

- `type: "spend_limit_increase_request"`

  default: spend_limit_increase_request

- `id: string`

- `actor: SpendLimitIncreaseRequestActor`

  Who submitted the increase request.

  - `SpendLimitUserActor object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

    - `type: "user_actor"`

      Actor type. Always `user_actor`.

      default: user_actor

    - `deleted: boolean`

      True only when the underlying account has been deleted.

      default: false

    - `email_address: string or null`

      The user's email address. Null when the account is unavailable or has been deleted.

    - `name: string or null`

      The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

    - `user_id: string`

      Tagged ID of the user.

  - `SpendLimitScopedAPIKeyActor object`

    A scoped Admin API key acting on behalf of the organization.

    - `type: "scoped_api_key_actor"`

      default: scoped_api_key_actor

    - `scoped_api_key_id: string`

- `created_at: string`

  format: date-time

- `period: SpendLimitPeriod`

  - `"daily"`

  - `"monthly"`

  - `"weekly"`

- `resolved_at: string or null`

  format: date-time

- `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

  Who approved or denied the increase request.

  - `SpendLimitUserActor object`

    A user within the organization. `name` and `email_address` are
    null when the underlying account is unavailable or has been deleted;
    `deleted` is true only for deleted accounts.

  - `SpendLimitScopedAPIKeyActor object`

    A scoped Admin API key acting on behalf of the organization.

- `spend_limit: SpendLimit or null`

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

  - `is_enabled: boolean`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `period: SpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

      - `type: "user"`

        Scope type. Always `user` for this scope.

        default: user

      - `user_id: string`

        Tagged ID of the member the spend limit applies to.

    - `SpendLimitSeatTierScope object`

      - `type: "seat_tier"`

        default: seat_tier

      - `seat_tier: string`

    - `SpendLimitRBACGroupScope object`

      - `type: "rbac_group"`

        default: rbac_group

      - `rbac_group_id: string`

    - `SpendLimitOrganizationServiceScope object`

      - `type: "organization_service"`

        default: organization_service

      - `service: string`

    - `SpendLimitOrganizationScope object`

      - `type: "organization"`

        default: organization

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

      - `type: "workspace"`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `workspace_id: string`

        Tagged ID of the workspace the spend limit applies to.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

      - `type: "usage_tier"`

        Scope type. Always `usage_tier` for this scope.

        default: usage_tier

  - `updated_at: string`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

- `spend_summary: SpendSummary or null`

  Per-member effective-limit report row (`GET /spend_limits/effective`).

  - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `amount: string or null`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `currency: string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `period: SpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

  - `period_to_date_spend: string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

    - `SpendLimitUserScope object`

      Scope selecting a single member of the organization.

    - `SpendLimitSeatTierScope object`

    - `SpendLimitRBACGroupScope object`

    - `SpendLimitOrganizationServiceScope object`

    - `SpendLimitOrganizationScope object`

    - `SpendLimitWorkspaceScope object`

      Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitUsageTierScope object`

      Scope of the monthly spend cap Anthropic sets for a Claude Console
      organization from its usage tier, or a higher cap Anthropic granted the
      organization. Read-only; its `created_at` and `updated_at` are the
      organization's creation time, so `amount` can change while `updated_at` stays
      the same.

  - `spend_limit_id: string`

- `status: SpendLimitIncreaseRequestStatus`

  - `"approved"`

  - `"denied"`

  - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/approve \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
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

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

#### Body parameters

- `suppress_notification: optional boolean`

#### Returns

- `SpendLimitIncreaseRequest object`

  - `type: "spend_limit_increase_request"`

    default: spend_limit_increase_request

  - `id: string`

  - `actor: SpendLimitIncreaseRequestActor`

    Who submitted the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `type: "user_actor"`

        Actor type. Always `user_actor`.

        default: user_actor

      - `deleted: boolean`

        True only when the underlying account has been deleted.

        default: false

      - `email_address: string or null`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `name: string or null`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `user_id: string`

        Tagged ID of the user.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

      - `type: "scoped_api_key_actor"`

        default: scoped_api_key_actor

      - `scoped_api_key_id: string`

  - `created_at: string`

    format: date-time

  - `period: SpendLimitPeriod`

    - `"daily"`

    - `"monthly"`

    - `"weekly"`

  - `resolved_at: string or null`

    format: date-time

  - `resolved_by: SpendLimitIncreaseRequestResolvedBy or null`

    Who approved or denied the increase request.

    - `SpendLimitUserActor object`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `SpendLimitScopedAPIKeyActor object`

      A scoped Admin API key acting on behalf of the organization.

  - `spend_summary: SpendSummary or null`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `actor: SpendLimitUserActor or SpendLimitScopedAPIKeyActor`

      - `SpendLimitUserActor object`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `SpendLimitScopedAPIKeyActor object`

        A scoped Admin API key acting on behalf of the organization.

    - `amount: string or null`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `currency: string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `period: SpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `period_to_date_spend: string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `scope: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

        - `type: "user"`

          Scope type. Always `user` for this scope.

          default: user

        - `user_id: string`

          Tagged ID of the member the spend limit applies to.

      - `SpendLimitSeatTierScope object`

        - `type: "seat_tier"`

          default: seat_tier

        - `seat_tier: string`

      - `SpendLimitRBACGroupScope object`

        - `type: "rbac_group"`

          default: rbac_group

        - `rbac_group_id: string`

      - `SpendLimitOrganizationServiceScope object`

        - `type: "organization_service"`

          default: organization_service

        - `service: string`

      - `SpendLimitOrganizationScope object`

        - `type: "organization"`

          default: organization

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

        - `type: "workspace"`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `workspace_id: string`

          Tagged ID of the workspace the spend limit applies to.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

        - `type: "usage_tier"`

          Scope type. Always `usage_tier` for this scope.

          default: usage_tier

    - `source: SpendLimitUserScope or SpendLimitSeatTierScope or SpendLimitRBACGroupScope or 4 more`

      - `SpendLimitUserScope object`

        Scope selecting a single member of the organization.

      - `SpendLimitSeatTierScope object`

      - `SpendLimitRBACGroupScope object`

      - `SpendLimitOrganizationServiceScope object`

      - `SpendLimitOrganizationScope object`

      - `SpendLimitWorkspaceScope object`

        Scope selecting one workspace of a Claude Console organization.

      - `SpendLimitUsageTierScope object`

        Scope of the monthly spend cap Anthropic sets for a Claude Console
        organization from its usage tier, or a higher cap Anthropic granted the
        organization. Read-only; its `created_at` and `updated_at` are the
        organization's creation time, so `amount` can change while `updated_at` stays
        the same.

    - `spend_limit_id: string`

  - `status: SpendLimitIncreaseRequestStatus`

    - `"approved"`

    - `"denied"`

    - `"pending"`

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/$SPEND_LIMIT_INCREASE_REQUEST_ID/deny \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
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
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```
