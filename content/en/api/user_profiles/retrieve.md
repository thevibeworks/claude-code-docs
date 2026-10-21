---
title: Get User Profile
url: https://platform.claude.com/docs/en/api/user_profiles/retrieve
---

# Get User Profile

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

## Path parameters

- `user_profile_id: string`

  The ID of the user profile to get (`uprof_...`).

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `UserProfile object`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `access_type: UserProfileAccessType`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

    - `"application"`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `"passthrough"`

      The user profile represents a company that the platform resells Claude access to.

  - `created_at: string`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `external_user_details: UserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: UserProfileExternalUserAccountStatus or null`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `"active"`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `"suspended"`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `"blocked"`

        The platform has barred the account of the entity that the user profile represents.

    - `country: string or null`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: string or null`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: UserProfileExternalUserEntityType or null`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `"individual"`

      - `"business"`

      - `"non_profit"`

      - `"government"`

    - `name_hash: string or null`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: string or null`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: string or null`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `name: string or null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.

  - `programs: UserProfilePrograms`

    The profile's standing in each Anthropic program, such as the Cyber Verification Program. Present when the request sends no user-profiles beta header; absent under the `user-profiles-2026-09-04` and earlier beta headers, which serve `trust_grants` instead.

    - `cyber: UserProfileCyberProgram or null`

      The profile's standing in the Cyber Verification Program. `null` when the profile has no status in it. Only retrieving the profile gives the full answer: a list or update response can show `null`, or a status other than `active`, for a profile that reads `active` when retrieved.

      - `requirements: UserProfileCyberRequirements or null`

        What a request that names the profile must allow to get the relaxed safeguards of every `active` tier. `null` when no tier is `active`, and wherever `tiers` is `{}`.

        - `data_retention: boolean`

          Whether Anthropic must be able to retain the request's inference data.

        - `human_review: boolean`

          Whether Anthropic personnel must be allowed to review the data retained from the request.

      - `status: UserProfileProgramStatus`

        `active` when at least one tier is `active`, or when the profile has the program's access to earlier models. That access is not a tier: a profile that has it alone reads `active` with every tier `inactive`, or with `tiers` `{}` on a response that does not report tiers. When nothing is `active`, `pending` means that an application or enrollment is under review, or that what Anthropic approved does not yet apply to this profile, and `rejected` means that the application or enrollment was declined.

        - `"active"`

          The profile is in the program.

        - `"pending"`

          The profile is not in the program yet, and something is still awaited.

        - `"rejected"`

          The profile is not in the program and nothing is awaited: Anthropic has declined, or has withdrawn an earlier approval.

      - `tiers: map[UserProfileCyberTier]`

        The program's tiers, keyed by tier: `a` (Specialized Access), `b` (Red Team Access) and `c` (Defense Access). A response reports either every tier or none. When it reports them, as retrieving the profile normally does, every tier has a key, whether or not it applies to the profile. When it does not, as in the list of user profiles, `tiers` is `{}`, which does not mean that the tiers are inactive. No tier implies another, so read the tier you need. Anthropic may add tiers; ignore a key you do not recognize.

        - `status: "active" or "inactive"`

          `active` when the tier applies to the profile, otherwise `inactive`. The response does not say why a tier is `inactive`: it can be in review, declined, withdrawn, never applied for, or approved but not applied to this profile.

          - `"active"`

          - `"inactive"`

    - `efs: UserProfileEfsProgram or null`

      The profile's standing in Enterprise Frontier Safeguards. `null` unless the platform's attestation for the program is in place on this profile, or the entity it represents has applied to the program. A list of user profiles does not report this program: there it reads `null` for every profile, so retrieve the profile to read it.

      - `features: map[UserProfileEfsFeature]`

        The program's features, keyed by feature: `data_retention_exemption` (use of models that normally require data retention, without the data being retained), `cmek` (customer-managed encryption keys) and `storage` (customer-owned storage). Every feature that the caller's organization may read has a key, whether or not it is approved; a missing key does not mean that the feature is inactive. Anthropic may add features; ignore a key you do not recognize.

        - `status: "active" or "inactive"`

          `active` when Anthropic has approved the entity the profile represents to use the feature, otherwise `inactive`. `active` does not mean that the feature is set up or switched on, which is a separate step.

          - `"active"`

          - `"inactive"`

      - `status: UserProfileProgramStatus`

        Anthropic's decision on the entity the profile represents: `pending` while it is awaited, `active` once Anthropic has approved the entity for the program, or `rejected` once Anthropic has declined or has removed the entity from the program. `active` does not mean that any one feature is approved: read the feature you need in `features`.

  - `updated_at: string`

    When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "access_type": "application",
  "created_at": "2026-03-15T10:00:00Z",
  "external_user_details": {
    "account_status": "active",
    "country": "US",
    "email_hash": null,
    "entity_type": "business",
    "name_hash": null,
    "onboarded_at": "2024-11-02T08:15:00Z",
    "reference_id": "user_12345"
  },
  "metadata": {},
  "name": "Example User",
  "programs": {
    "cyber": {
      "requirements": {
        "data_retention": true,
        "human_review": true
      },
      "status": "active",
      "tiers": {
        "a": {
          "status": "inactive"
        },
        "b": {
          "status": "inactive"
        },
        "c": {
          "status": "inactive"
        }
      }
    },
    "efs": {
      "features": {
        "data_retention_exemption": {
          "status": "inactive"
        },
        "cmek": {
          "status": "active"
        },
        "storage": {
          "status": "inactive"
        }
      },
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z"
}
```
