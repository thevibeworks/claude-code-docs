---
title: Update User Profile
url: https://platform.claude.com/docs/en/api/cli/beta/user_profiles/update
---

## Update User Profile

`$ ant beta:user-profiles update`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `--user-profile-id: string`

  Path param: Path parameter user_profile_id

- `--access-type: optional "application" or "passthrough"`

  Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `--external-id: optional string`

  Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `--metadata: optional map[string]`

  Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `--name: optional string`

  Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `--relationship: optional "external" or "resold" or "internal"`

  Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object { id, created_at, metadata, 7 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `access_type: optional "application" or "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: optional "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```cli
ant beta:user-profiles update \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

#### Response

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
  "name": "Example User",
  "relationship": "external"
}
```
