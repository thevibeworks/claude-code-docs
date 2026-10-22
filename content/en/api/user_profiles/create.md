---
title: Create User Profile
url: https://platform.claude.com/docs/en/api/user_profiles/create
---

# Create User Profile

**POST** `/v1/user_profiles`

Create User Profile

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Body parameters

- `access_type: optional UserProfileAccessType`

  How the platform uses the API for this entity. `application` (default): the profile represents an individual end-user of the platform's product. `passthrough`: the profile identifies a company the platform resells Claude access to.

  - `"application"`

    The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

  - `"passthrough"`

    The user profile represents a company that the platform resells Claude access to.

- `external_user_details: optional UserProfileExternalUserDetailsParams`

  Details about the entity this profile represents, as the platform states them. Every field is optional. Not accepted under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which take the top-level `external_id` (and, under `user-profiles-2026-08-18`, `external_user_onboarded_at`) instead.

  - `account_status: optional UserProfileExternalUserAccountStatus or null`

    The status of the entity's account on the platform: `active`, `suspended` or `blocked`.

    - `"active"`

      The platform has neither restricted nor barred the account of the entity that the user profile represents.

    - `"suspended"`

      The platform has restricted the account of the entity that the user profile represents and may restore it.

    - `"blocked"`

      The platform has barred the account of the entity that the user profile represents.

  - `country: optional string or null`

    The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

  - `email_hash: optional string or null`

    A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `entity_type: optional UserProfileExternalUserEntityType or null`

    What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`.

    - `"individual"`

    - `"business"`

    - `"non_profit"`

    - `"government"`

  - `name_hash: optional string or null`

    A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

    minLength: 1, maxLength: 255

  - `onboarded_at: optional string`

    When the entity opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future.

    format: date-time

  - `reference_id: optional string or null`

    The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

    minLength: 1, maxLength: 255

- `metadata: optional map[string]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: optional string or null`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  minLength: 1, maxLength: 255

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

  - `enforcement_actions: array of UserProfileEnforcementAction`

    The enforcement actions open on this profile; empty when none is open. Absent under the `user-profiles-2026-09-04` and earlier beta headers.

    - `UserProfileEnforcementActionRestriction object`

      Anthropic has limited how it serves the end user until the action is resolved. The end user may still be served in part.

      - `type: "restriction"`

      - `id: string`

        The action's ID (`enac_...`), stable while the action is open.

      - `action: UserProfileEnforcementActionNextStep or null`

        The next step on the action: `verify` or `null`. `verify`: the end user can clear it now by passing an identity check. `null`: there is nothing the end user can do now to clear it, including while Anthropic reviews an identity check the end user submitted.

      - `expires_at: string or null`

        When the action ends on its own, in RFC 3339 format; it stops showing once this time has passed. `null` when it has no end date, and always `null` when `reason` is `account_compromise`.

        format: date-time

      - `opened_at: string`

        When Anthropic opened the action, in RFC 3339 format.

        format: date-time

      - `reason: UserProfileEnforcementActionReason`

        Why Anthropic placed the limit: `unsupported_region`, `fraud_or_abuse`, `high_harm`, `usage_policy_violation`, `account_compromise` or `unspecified`.

        - `"unsupported_region"`

        - `"fraud_or_abuse"`

        - `"high_harm"`

        - `"usage_policy_violation"`

        - `"account_compromise"`

        - `"unspecified"`

    - `UserProfileEnforcementActionBan object`

      Anthropic has stopped serving the end user where the ban applies and does not plan to serve them there again.

      - `type: "ban"`

      - `id: string`

        The action's ID (`enac_...`), stable while the action is open.

      - `action: UserProfileEnforcementActionNextStep or null`

        Always `null`: the end user cannot clear a ban.

      - `expires_at: string or null`

        Always `null`: a ban has no end date.

        format: date-time

      - `opened_at: string`

        When Anthropic opened the action, in RFC 3339 format.

        format: date-time

      - `reason: UserProfileEnforcementActionReason`

        Why Anthropic placed the limit: `unsupported_region`, `fraud_or_abuse`, `high_harm`, `usage_policy_violation`, `account_compromise` or `unspecified`.

  - `enforcement_status: UserProfileEnforcementStatus`

    Anthropic's enforcement status of this profile, from its open enforcement actions and any identity check under review, by the first rule that applies: `banned` while any open action is a `ban`; `pending` while a restriction that an identity check can clear is open, the end user has submitted that check, Anthropic's review of it has not ended, and no open action's `reason` is `account_compromise`; `restricted` while any action is open; `unrestricted` while none is. Absent under the `user-profiles-2026-09-04` and earlier beta headers.

    - `"unrestricted"`

    - `"pending"`

    - `"restricted"`

    - `"banned"`

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
curl https://api.anthropic.com/v1/user_profiles \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "external_user_details": {
            "account_status": "active",
            "country": "US",
            "entity_type": "business",
            "onboarded_at": "2024-11-02T08:15:00Z",
            "reference_id": "user_12345"
          },
          "metadata": {},
          "name": "Example User"
        }'
```

### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "access_type": "application",
  "created_at": "2026-03-15T10:00:00Z",
  "enforcement_actions": [
    {
      "id": "enac_011CZkZCu8hGbp5mYRQgUmz9",
      "action": "verify",
      "expires_at": null,
      "opened_at": "2026-10-02T19:30:00Z",
      "reason": "fraud_or_abuse",
      "type": "restriction"
    }
  ],
  "enforcement_status": "unrestricted",
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
