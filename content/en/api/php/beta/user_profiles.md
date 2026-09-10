---
title: User Profiles
url: https://platform.claude.com/docs/en/api/php/beta/user_profiles
---

# User Profiles

## Create User Profile

`$client->beta->userProfiles->create(?AccessType accessType, ?string externalID, ?BetaUserProfileExternalUserDetailsParams externalUserDetails, ?\Datetime externalUserOnboardedAt, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): BetaUserProfile`

**POST** `/v1/user_profiles`

Create User Profile

### Parameters

- `accessType?:optional AccessType`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `externalID?:optional string`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

- `externalUserDetails?:optional BetaUserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Every field is optional. Accepted under the `user-profiles-2026-09-04` beta header only.

- `externalUserOnboardedAt?:optional \Datetime`

  A timestamp in RFC 3339 format

- `metadata?:optional array<string,string>`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name?:optional string`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->create(
  accessType: 'application',
  externalID: 'user_12345',
  externalUserDetails: [
    'accountStatus' => 'active',
    'country' => 'country',
    'emailHash' => 'x',
    'entityType' => 'individual',
    'nameHash' => 'x',
    'onboardedAt' => new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
    'referenceID' => 'x',
  ],
  externalUserOnboardedAt: new \DateTimeImmutable('2024-11-02T08:15:00Z'),
  metadata: [],
  name: 'x',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaUserProfile);
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

`$client->beta->userProfiles->list(?int limit, ?Order order, ?OrderBy orderBy, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

### Parameters

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

### Returns

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

### Example

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

`$client->beta->userProfiles->retrieve(string userProfileID, ?list<AnthropicBeta> betas): BetaUserProfile`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->retrieve(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaUserProfile);
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

`$client->beta->userProfiles->update(string userProfileID, ?AccessType accessType, ?string externalID, ?BetaUserProfileExternalUserDetailsParams externalUserDetails, ?\Datetime externalUserOnboardedAt, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID: string`

- `accessType?:optional AccessType`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

- `externalID?:optional string`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

- `externalUserDetails?:optional BetaUserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Accepted under the `user-profiles-2026-09-04` beta header only.

- `externalUserOnboardedAt?:optional \Datetime`

  A timestamp in RFC 3339 format

- `metadata?:optional array<string,string>`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name?:optional string`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->update(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  accessType: 'application',
  externalID: 'user_12345',
  externalUserDetails: [
    'accountStatus' => 'active',
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
);

var_dump($betaUserProfile);
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

`$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): BetaUserProfileEnrollmentURL`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaUserProfileEnrollmentURL`

  - `Type type`

    Object type. Always `enrollment_url`.

  - `\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfileEnrollmentURL = $client
  ->beta
  ->userProfiles
  ->createEnrollmentURL(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaUserProfileEnrollmentURL);
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

### Beta User Profile Enrollment URL

- `BetaUserProfileEnrollmentURL`

  - `Type type`

    Object type. Always `enrollment_url`.

  - `\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile External User Details

- `BetaUserProfileExternalUserDetails`

  - `?AccountStatus accountStatus`

    The status of the entity's account on the platform, as the platform states it: `active`; `suspended`, when the platform has restricted the account and may restore it; or `blocked`, when the platform has barred it. It records the platform's decision only; the statuses in `trust_grants` are Anthropic's and do not follow it.

  - `?string country`

    The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

  - `?string emailHash`

    The platform-computed hash of the entity's email address. `null` until the platform supplies one.

  - `?EntityType entityType`

    What kind of entity the profile represents, as the platform states it: `individual`, `business`, `non_profit` or `government`.

  - `?string nameHash`

    The platform-computed hash of the entity's name. `null` until the platform supplies one.

  - `?\Datetime onboardedAt`

    A timestamp in RFC 3339 format

  - `?string referenceID`

    The platform's own reference for the entity. `null` until the platform supplies one.

### Beta User Profile External User Details Params

- `BetaUserProfileExternalUserDetailsParams`

  - `?AccountStatus accountStatus`

    The status of the entity's account on the platform, as the platform states it: `active`; `suspended`, when the platform has restricted the account and may restore it; or `blocked`, when the platform has barred it. It records the platform's decision only; the statuses in `trust_grants` are Anthropic's and do not follow it.

  - `?string country`

    The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

  - `?string emailHash`

    A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

  - `?EntityType entityType`

    What kind of entity the profile represents, as the platform states it: `individual`, `business`, `non_profit` or `government`.

  - `?string nameHash`

    A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

  - `?\Datetime onboardedAt`

    A timestamp in RFC 3339 format

  - `?string referenceID`

    The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

### Beta User Profile Trust Grant

- `BetaUserProfileTrustGrant`

  - `Status status`

    Status of the trust grant.
