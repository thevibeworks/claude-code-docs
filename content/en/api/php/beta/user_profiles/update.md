---
title: Update User Profile
url: https://platform.claude.com/docs/en/api/php/beta/user_profiles/update
---

# Update User Profile

`$client->beta->userProfiles->update(string userProfileID, ?AccessType accessType, ?string externalID, ?BetaUserProfileExternalUserDetailsParams externalUserDetails, ?\Datetime externalUserOnboardedAt, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas, ?string workspaceID): BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

## Parameters

- `userProfileID: string` (path parameter)

  The ID of the user profile to update (`uprof_...`).

- `accessType?:optional AccessType`

  If present, replaces the stored access type. Omit to leave unchanged.

- `externalID?:optional string`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters. Legacy field, accepted only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, send `external_user_details.reference_id`.

- `externalUserDetails?:optional BetaUserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Not accepted under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers.

- `externalUserOnboardedAt?:optional \Datetime`

  If present, replaces the stored account creation time. Omit to leave unchanged; once set, the value cannot be cleared and `null` is rejected. Must be a complete RFC 3339 timestamp no more than 1 minute in the future. Legacy field, accepted only under the `user-profiles-2026-08-18` beta header; without a legacy header, send `external_user_details.onboarded_at`.

- `metadata?:optional array<string,string>`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name?:optional string`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaUserProfile`

  - `"user_profile" type`

    Object type. Always `user_profile`.

  - `string id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `\Datetime createdAt`

    When this user profile was created, in RFC 3339 format.

  - `array<string,string> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `?string name`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.

  - `array<string,BetaUserProfileTrustGrant> trustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

  - `\Datetime updatedAt`

    When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

  - `?AccessType accessType`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

  - `?string externalID`

    Platform's own identifier for this user. Not enforced unique. Legacy field, present only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, the value is `external_user_details.reference_id`.

  - `?BetaUserProfileExternalUserDetails externalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.

  - `?\Datetime externalUserOnboardedAt`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Legacy field, present only under the `user-profiles-2026-08-18` beta header; without a legacy header, the value is `external_user_details.onboarded_at`.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->update(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  accessType: 'application',
  externalID: 'x',
  externalUserDetails: [
    'accountStatus' => 'suspended',
    'country' => 'country',
    'emailHash' => 'x',
    'entityType' => 'individual',
    'nameHash' => 'x',
    'onboardedAt' => new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
    'referenceID' => 'x',
  ],
  externalUserOnboardedAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  metadata: ['foo' => 'string'],
  name: 'x',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaUserProfile);
```

### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "name": "Example User",
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
    "country": "US",
    "email_hash": null,
    "entity_type": "business",
    "name_hash": null,
    "onboarded_at": "2024-11-02T08:15:00Z",
    "reference_id": "user_12345"
  },
  "external_user_onboarded_at": "2024-11-02T08:15:00Z"
}
```
