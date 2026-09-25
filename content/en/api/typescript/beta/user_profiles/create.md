---
title: Create User Profile
url: https://platform.claude.com/docs/en/api/typescript/beta/user_profiles/create
---

# Create User Profile

`client.beta.userProfiles.create(params, options?): BetaUserProfile`

**POST** `/v1/user_profiles`

Create User Profile

## Parameters

- `params: UserProfileCreateParams`

  - `access_type?: "application" | "passthrough"`

    Body param: How the platform uses the API for this entity. `application` (default): the profile represents an individual end-user of the platform's product. `passthrough`: the profile identifies a company the platform resells Claude access to.

    - `"application"`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `"passthrough"`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id?: string | null`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters. Accepted under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` send `external_user_details.reference_id` instead.

    minLength: 1, maxLength: 255

  - `external_user_details?: BetaUserProfileExternalUserDetailsParams`

    Body param: Details about the entity this profile represents, as the platform states them. Every field is optional. Accepted under the `user-profiles-2026-09-04` beta header only.

    - `account_status?: "active" | "suspended" | "blocked" | null`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`.

      - `"active"`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `"suspended"`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `"blocked"`

        The platform has barred the account of the entity that the user profile represents.

    - `country?: string | null`

      The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked.

    - `email_hash?: string | null`

      A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

      minLength: 1, maxLength: 255

    - `entity_type?: "individual" | "business" | "non_profit" | "government" | null`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`.

      - `"individual"`

      - `"business"`

      - `"non_profit"`

      - `"government"`

    - `name_hash?: string | null`

      A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters.

      minLength: 1, maxLength: 255

    - `onboarded_at?: string`

      When the entity opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future.

      format: date-time

    - `reference_id?: string | null`

      The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters.

      minLength: 1, maxLength: 255

  - `external_user_onboarded_at?: string`

    Body param: When the entity this profile represents opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future. Optional. Accepted under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` send `external_user_details.onboarded_at` instead.

    format: date-time

  - `metadata?: Record<string, string>`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `name?: string | null`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 45 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"user-profiles-2026-09-04"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

      - `"compact-2026-01-12"`

      - `"computer-use-2025-11-24"`

      - `"mcp-tunnels-2026-06-22"`

      - `"structured-outputs-2025-11-13"`

      - `"task-budgets-2026-03-13"`

      - `"thinking-display-updates-2026-08-18"`

      - `"ce-user-management-2026-07-13"`

      - `"mid-conversation-output-config-2026-07-01"`

      - `"thinking-binding-controls-2026-08-01"`

      - `"mid-conversation-system-clear-at-2026-08-21"`

      - `"compact-2026-09-04"`

      - `"inline-tools-2026-09-15"`

      - `"mcp-client-2026-09-15"`

  - `workspace_id?: string`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `interface BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Record<string, BetaUserProfileTrustGrant>`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" | "pending" | "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `updated_at: string`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `"application"`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `"passthrough"`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details?: BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: "active" | "suspended" | "blocked" | null`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `"active"`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `"suspended"`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `"blocked"`

        The platform has barred the account of the entity that the user profile represents.

    - `country: string | null`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: string | null`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: "individual" | "business" | "non_profit" | "government" | null`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `"individual"`

      - `"business"`

      - `"non_profit"`

      - `"government"`

    - `name_hash: string | null`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: string | null`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: string | null`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at?: string | null`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.create();

console.log(betaUserProfile.id);
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
