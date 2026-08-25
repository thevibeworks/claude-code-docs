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

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaListUserProfilesResponse: object`

  - `data: array of BetaUserProfile`

    User profiles on this page.

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

    - `type: "user_profile"`

      Object type. Always `user_profile`.

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

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
      "name": "Example User",
      "relationship": "external"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
