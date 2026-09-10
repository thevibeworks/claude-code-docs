---
title: List User Profiles
url: https://platform.claude.com/docs/en/api/php/beta/user_profiles/list
---

# List User Profiles

`$client->beta->userProfiles->list(?int limit, ?Order order, ?OrderBy orderBy, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

## Parameters

- `limit?:optional int`

  Query parameter for limit

- `order?:optional Order`

  Query parameter for order

- `orderBy?:optional OrderBy`

  Query parameter for order_by

- `page?:optional string`

  Query parameter for page

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaUserProfile`

  - `Type type`

    Object type. Always `user_profile`.

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?AccessType accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `?BetaUserProfileExternalUserDetails externalUserDetails`

    Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value.

  - `?\Datetime externalUserOnboardedAt`

    A timestamp in RFC 3339 format

  - `?string name`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->userProfiles->list(
  limit: 0,
  order: 'asc',
  orderBy: 'created_at',
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($page);
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
