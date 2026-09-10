---
title: List User Profiles
url: https://platform.claude.com/docs/en/api/cli/beta/user_profiles/list
---

# List User Profiles

`$ ant beta:user-profiles list`

**GET** `/v1/user_profiles`

List User Profiles

## Parameters

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--order: optional "asc" or "desc"`

  Query param: Query parameter for order

- `--order-by: optional "created_at" or "name"`

  Query param: Query parameter for order_by

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaListUserProfilesResponse: object`

  - `data: array of BetaUserProfile`

    User profiles on this page.

    - `type: "user_profile"`

      Object type. Always `user_profile`.

    - `id: string`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `trust_grants: map[BetaUserProfileTrustGrant]`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `status: "active" or "pending" or "rejected"`

        Status of the trust grant.

        - `"active"`

        - `"pending"`

        - `"rejected"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `access_type: optional "application" or "passthrough"`

      How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

      - `"application"`

      - `"passthrough"`

    - `external_id: optional string`

      Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

    - `external_user_details: optional object`

      Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value.

      - `account_status: "active" or "suspended" or "blocked"`

        The status of the entity's account on the platform, as the platform states it: `active`; `suspended`, when the platform has restricted the account and may restore it; or `blocked`, when the platform has barred it. It records the platform's decision only; the statuses in `trust_grants` are Anthropic's and do not follow it.

        - `"active"`

        - `"suspended"`

        - `"blocked"`

      - `country: string`

        The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

      - `email_hash: string`

        The platform-computed hash of the entity's email address. `null` until the platform supplies one.

      - `entity_type: "individual" or "business" or "non_profit" or "government"`

        What kind of entity the profile represents, as the platform states it: `individual`, `business`, `non_profit` or `government`.

        - `"individual"`

        - `"business"`

        - `"non_profit"`

        - `"government"`

      - `name_hash: string`

        The platform-computed hash of the entity's name. `null` until the platform supplies one.

      - `onboarded_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `reference_id: string`

        The platform's own reference for the entity. `null` until the platform supplies one.

    - `external_user_onboarded_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `name: optional string`

      Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

  - `next_page: string`

    Cursor for the next page, or `null` when there are no more results.

## Example

```bash
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
```

### Response (200)

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "external_user_details": {
        "account_status": "active",
        "country": "country",
        "email_hash": "email_hash",
        "entity_type": "individual",
        "name_hash": "name_hash",
        "onboarded_at": "2019-12-27T18:11:19.117Z",
        "reference_id": "reference_id"
      },
      "external_user_onboarded_at": "2024-11-02T08:15:00Z",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
