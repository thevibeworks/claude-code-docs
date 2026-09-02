# Update User Profile

`$client->beta->userProfiles->update(string userProfileID, ?AccessType accessType, ?string externalID, ?\Datetime externalUserOnboardedAt, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

## Parameters

- `userProfileID: string`

- `accessType?:optional AccessType`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `externalID?:optional string`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `externalUserOnboardedAt?:optional \Datetime`

  A timestamp in RFC 3339 format

- `metadata?:optional array<string,string>`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name?:optional string`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaUserProfile`

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `Type type`

    Object type. Always `user_profile`.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `?AccessType accessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique.

  - `?\Datetime externalUserOnboardedAt`

    A timestamp in RFC 3339 format

  - `?string name`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->update(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  accessType: 'application',
  externalID: 'user_12345',
  externalUserOnboardedAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  metadata: ['foo' => 'string'],
  name: 'x',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaUserProfile);
```

### Response (200)

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
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```
