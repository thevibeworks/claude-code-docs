---
title: User Profiles
url: https://platform.claude.com/docs/en/api/cli/beta/user_profiles
---

# User Profiles

## Create User Profile

`$ ant beta:user-profiles create`

**POST** `/v1/user_profiles`

Create User Profile

### Parameters

- `--access-type: optional "application" or "passthrough"`

  Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `--external-id: optional string`

  Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

  minLength: 1, maxLength: 255

- `--external-user-details: optional object`

  Body param: Details about the entity this profile represents, as the platform states them. Every field is optional. Accepted under the `user-profiles-2026-09-04` beta header only.

- `--external-user-onboarded-at: optional string`

  Body param: A timestamp in RFC 3339 format

  format: date-time

- `--metadata: optional map[string]`

  Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `--name: optional string`

  Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object`

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

### Example

```bash
ant beta:user-profiles create \
  --api-key my-anthropic-api-key
```

#### Response (200)

```json
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
```

## List User Profiles

`$ ant beta:user-profiles list`

**GET** `/v1/user_profiles`

List User Profiles

### Parameters

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

### Returns

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

### Example

```bash
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
```

#### Response (200)

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

## Get User Profile

`$ ant beta:user-profiles retrieve`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object`

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

### Example

```bash
ant beta:user-profiles retrieve \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

#### Response (200)

```json
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
```

## Update User Profile

`$ ant beta:user-profiles update`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `--user-profile-id: string`

  Path param: Path parameter user_profile_id

- `--access-type: optional "application" or "passthrough"`

  Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `--external-id: optional string`

  Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

  minLength: 1, maxLength: 255

- `--external-user-details: optional object`

  Body param: Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Accepted under the `user-profiles-2026-09-04` beta header only.

- `--external-user-onboarded-at: optional string`

  Body param: A timestamp in RFC 3339 format

  format: date-time

- `--metadata: optional map[string]`

  Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `--name: optional string`

  Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object`

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

### Example

```bash
ant beta:user-profiles update \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

#### Response (200)

```json
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
```

## Create Enrollment URL

`$ ant beta:user-profiles create-enrollment-url`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile_enrollment_url: object`

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```bash
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

#### Response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Domain types

### Beta User Profile

- `beta_user_profile: object`

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

### Beta User Profile Enrollment URL

- `beta_user_profile_enrollment_url: object`

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile External User Details

- `beta_user_profile_external_user_details: object`

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

### Beta User Profile External User Details Params

- `beta_user_profile_external_user_details_params: object`

  - `account_status: optional "active" or "suspended" or "blocked"`

    The status of the entity's account on the platform, as the platform states it: `active`; `suspended`, when the platform has restricted the account and may restore it; or `blocked`, when the platform has barred it. It records the platform's decision only; the statuses in `trust_grants` are Anthropic's and do not follow it.

    - `"active"`

    - `"suspended"`

    - `"blocked"`

  - `country: optional string`

    The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

  - `email_hash: optional string`

    A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `entity_type: optional "individual" or "business" or "non_profit" or "government"`

    What kind of entity the profile represents, as the platform states it: `individual`, `business`, `non_profit` or `government`.

    - `"individual"`

    - `"business"`

    - `"non_profit"`

    - `"government"`

  - `name_hash: optional string`

    A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `onboarded_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `reference_id: optional string`

    The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

    minLength: 1, maxLength: 255

### Beta User Profile Trust Grant

- `beta_user_profile_trust_grant: object`

  - `status: "active" or "pending" or "rejected"`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`
