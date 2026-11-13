---
title: User Profiles
url: https://platform.claude.com/docs/en/api/typescript/beta/user_profiles
---

# User Profiles

## Create User Profile

- Signature: `client.beta.userProfiles.create(params: UserProfileCreateParams, options?: RequestOptions): BetaUserProfile`
- Endpoint: `POST /v1/user_profiles`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.create({});

console.log(betaUserProfile.id);
```

### Example response (200)

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

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

interface UserProfileCreateParams {
  /**
   * How the platform uses the API for this entity. `application` (default): the profile represents an individual end-user of the platform's product. `passthrough`: the profile identifies a company the platform resells Claude access to.
   * - `"application"`: The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.
   * - `"passthrough"`: The user profile represents a company that the platform resells Claude access to.
   */
  access_type?: "application" | "passthrough";
  /** Platform's own identifier for this user. Not enforced unique. Maximum 255 characters. Legacy field, accepted only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, send `external_user_details.reference_id`. */
  external_id?: string | null; // minLength: 1, maxLength: 255, beta header: user-profiles-2026-03-24 or user-profiles-2026-08-18
  /** Details about the entity this profile represents, as the platform states them. Every field is optional. Not accepted under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which take the top-level `external_id` (and, under `user-profiles-2026-08-18`, `external_user_onboarded_at`) instead. */
  external_user_details?: BetaUserProfileExternalUserDetailsParams;
  /** When the entity this profile represents opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future. Optional. Legacy field, accepted only under the `user-profiles-2026-08-18` beta header; without a legacy header, send `external_user_details.onboarded_at`. */
  external_user_onboarded_at?: string; // format: date-time, beta header: user-profiles-2026-08-18
  /** Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings. */
  metadata?: Record<string, string>;
  /** Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters. */
  name?: string | null; // minLength: 1, maxLength: 255
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to. A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity. */
interface BetaUserProfile {
  /** Object type. Always `user_profile`. */
  type: "user_profile";
  /** Unique identifier for this user profile, prefixed `uprof_`. */
  id: string;
  /** When this user profile was created, in RFC 3339 format. */
  created_at: string; // format: date-time
  /** Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars. */
  metadata: Record<string, string>;
  /** Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one. */
  name: string | null;
  /** Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight. */
  trust_grants: Record<string, BetaUserProfileTrustGrant>; // beta header: user-profiles-2026-03-24 or user-profiles-2026-08-18 or user-profiles-2026-09-04
  /** When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp. */
  updated_at: string; // format: date-time
  /**
   * How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.
   * - `"application"`: The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.
   * - `"passthrough"`: The user profile represents a company that the platform resells Claude access to.
   */
  access_type?: "application" | "passthrough";
  /** Platform's own identifier for this user. Not enforced unique. Legacy field, present only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, the value is `external_user_details.reference_id`. */
  external_id?: string | null; // beta header: user-profiles-2026-03-24 or user-profiles-2026-08-18
  /** Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`. */
  external_user_details?: BetaUserProfileExternalUserDetails;
  /** When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Legacy field, present only under the `user-profiles-2026-08-18` beta header; without a legacy header, the value is `external_user_details.onboarded_at`. */
  external_user_onboarded_at?: string | null; // format: date-time, beta header: user-profiles-2026-08-18
}
```

### Types

```ts
interface BetaUserProfileExternalUserDetailsParams {
  /**
   * The status of the entity's account on the platform: `active`, `suspended` or `blocked`.
   * - `"active"`: The platform has neither restricted nor barred the account of the entity that the user profile represents.
   * - `"suspended"`: The platform has restricted the account of the entity that the user profile represents and may restore it.
   * - `"blocked"`: The platform has barred the account of the entity that the user profile represents.
   */
  account_status?: "active" | "suspended" | "blocked" | null;
  /** The country of the entity (not of the platform), as the platform determines it: an ISO 3166-1 alpha-2 code in upper case, for example `US`. Only the form, two uppercase ASCII letters, is checked. */
  country?: string | null; // pattern: ^[A-Z]{2}$
  /** A hash of the entity's email address, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters. */
  email_hash?: string | null; // minLength: 1, maxLength: 255
  /** What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. */
  entity_type?: "individual" | "business" | "non_profit" | "government" | null;
  /** A hash of the entity's name, computed by the platform. Anthropic treats it as an opaque string and does not prescribe the hash function. 1 to 255 characters. */
  name_hash?: string | null; // minLength: 1, maxLength: 255
  /** When the entity opened its account with the platform, in RFC 3339 format: for an `application` profile, when the end-user signed up; for a `passthrough` profile, when the company became the platform's customer. Must be a complete timestamp no more than 1 minute in the future. */
  onboarded_at?: string; // format: date-time
  /** The platform's own reference for the entity, for example the key of the end-user's row in the platform's database. Not interpreted by Anthropic and not enforced unique. 1 to 255 characters. */
  reference_id?: string | null; // minLength: 1, maxLength: 255
}

type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

/** The status of one trust grant on a user profile, listed in the profile's `trust_grants` map under the grant's name. */
interface BetaUserProfileTrustGrant {
  /** Status of the trust grant. */
  status: "active" | "pending" | "rejected";
}

/** Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value. */
interface BetaUserProfileExternalUserDetails {
  /**
   * The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.
   * - `"active"`: The platform has neither restricted nor barred the account of the entity that the user profile represents.
   * - `"suspended"`: The platform has restricted the account of the entity that the user profile represents and may restore it.
   * - `"blocked"`: The platform has barred the account of the entity that the user profile represents.
   */
  account_status: "active" | "suspended" | "blocked" | null;
  /** The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one. */
  country: string | null;
  /** The platform-computed hash of the entity's email address. `null` until the platform supplies one. */
  email_hash: string | null;
  /** What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one. */
  entity_type: "individual" | "business" | "non_profit" | "government" | null;
  /** The platform-computed hash of the entity's name. `null` until the platform supplies one. */
  name_hash: string | null;
  /** When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. */
  onboarded_at: string | null; // format: date-time
  /** The platform's own reference for the entity. `null` until the platform supplies one. */
  reference_id: string | null;
}
```

## List User Profiles

- Signature: `client.beta.userProfiles.list(params?: UserProfileListParams, options?: RequestOptions): PageCursor<BetaUserProfile>`
- Endpoint: `GET /v1/user_profiles`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaUserProfile of client.beta.userProfiles.list()) {
  console.log(betaUserProfile.id);
}
```

### Example response (200)

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Parameters

```ts
interface UserProfileListParams {
  /** The maximum number of user profiles to return, from 1 to 100. Defaults to 20. */
  limit?: number; // query parameter, format: int32
  /**
   * The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.
   * - `"asc"`: Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.
   * - `"desc"`: Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.
   */
  order?: "asc" | "desc"; // query parameter
  /**
   * The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.
   * - `"created_at"`: Sort by when each user profile was created. This is the default.
   * - `"name"`: Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.
   */
  order_by?: "created_at" | "name"; // query parameter
  /** The cursor for the page to return, taken from `next_page` in a previous response. Leave it out to get the first page. */
  page?: string; // query parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Get User Profile

- Signature: `client.beta.userProfiles.retrieve(userProfileID: string, params?: UserProfileRetrieveParams, options?: RequestOptions): BetaUserProfile`
- Endpoint: `GET /v1/user_profiles/{user_profile_id}`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.retrieve(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfile.id);
```

### Example response (200)

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

### Parameters

```ts
/** The ID of the user profile to get (`uprof_...`). */
userProfileID: string; // path parameter

interface UserProfileRetrieveParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Update User Profile

- Signature: `client.beta.userProfiles.update(userProfileID: string, params: UserProfileUpdateParams, options?: RequestOptions): BetaUserProfile`
- Endpoint: `POST /v1/user_profiles/{user_profile_id}`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.update(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  {}
);

console.log(betaUserProfile.id);
```

### Example response (200)

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

### Parameters

```ts
/** The ID of the user profile to update (`uprof_...`). */
userProfileID: string; // path parameter

interface UserProfileUpdateParams {
  /**
   * If present, replaces the stored access type. Omit to leave unchanged.
   * - `"application"`: The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.
   * - `"passthrough"`: The user profile represents a company that the platform resells Claude access to.
   */
  access_type?: "application" | "passthrough" | null;
  /** If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters. Legacy field, accepted only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, send `external_user_details.reference_id`. */
  external_id?: string | null; // minLength: 1, maxLength: 255, beta header: user-profiles-2026-03-24 or user-profiles-2026-08-18
  /** Details about the entity this profile represents, as the platform states them. Each field sent replaces the stored value; omit a field to leave it unchanged. Once set, a value cannot be cleared and `null` is rejected. Not accepted under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers. */
  external_user_details?: BetaUserProfileExternalUserDetailsParams;
  /** If present, replaces the stored account creation time. Omit to leave unchanged; once set, the value cannot be cleared and `null` is rejected. Must be a complete RFC 3339 timestamp no more than 1 minute in the future. Legacy field, accepted only under the `user-profiles-2026-08-18` beta header; without a legacy header, send `external_user_details.onboarded_at`. */
  external_user_onboarded_at?: string; // format: date-time, beta header: user-profiles-2026-08-18
  /** Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. */
  metadata?: Record<string, string>;
  /** If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters. */
  name?: string | null; // minLength: 1, maxLength: 255
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Delete User Profile

- Signature: `client.beta.userProfiles.delete(userProfileID: string, params?: UserProfileDeleteParams, options?: RequestOptions): BetaDeletedUserProfile`
- Endpoint: `DELETE /v1/user_profiles/{user_profile_id}`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaDeletedUserProfile = await client.beta.userProfiles.delete(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaDeletedUserProfile.id);
```

### Example response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "type": "user_profile_deleted"
}
```

### Parameters

```ts
/** The ID of the user profile to delete (`uprof_...`). */
userProfileID: string; // path parameter

interface UserProfileDeleteParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
interface BetaDeletedUserProfile {
  /** Object type. Always `user_profile_deleted`. */
  type: "user_profile_deleted";
  /** Identifier of the deleted user profile, prefixed `uprof_`. */
  id: string;
}
```

## Create Enrollment URL

- Signature: `client.beta.userProfiles.createEnrollmentURL(userProfileID: string, params?: UserProfileCreateEnrollmentURLParams, options?: RequestOptions): BetaUserProfileEnrollmentURL`
- Endpoint: `POST /v1/user_profiles/{user_profile_id}/enrollment_url`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfileEnrollmentURL = await client.beta.userProfiles.createEnrollmentURL(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfileEnrollmentURL.expires_at);
```

### Example response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

### Parameters

```ts
/** The ID of the user profile to create an enrollment URL for (`uprof_...`). */
userProfileID: string; // path parameter

interface UserProfileCreateEnrollmentURLParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A URL to give to the entity that a user profile represents, so that the entity can enroll in a program. */
interface BetaUserProfileEnrollmentURL {
  /** Object type. Always `enrollment_url`. */
  type: "enrollment_url";
  /** When this enrollment URL expires, in RFC 3339 format. */
  expires_at: string; // format: date-time
  /** Enrollment URL to send to the end user. Valid until `expires_at`. */
  url: string;
}
```

## User Profiles › Action URLs

### Create Action URL

- Signature: `client.beta.userProfiles.actionURLs.create(userProfileID: string, params: ActionURLCreateParams, options?: RequestOptions): BetaUserProfileActionURL`
- Endpoint: `POST /v1/user_profiles/{user_profile_id}/action_urls`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfileActionURL = await client.beta.userProfiles.actionURLs.create(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  { action: { type: "enroll_end_user" } }
);

console.log(betaUserProfileActionURL.expires_at);
```

#### Example response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "user_profile_action_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

#### Parameters

```ts
/** The ID of the user profile the action is for (`uprof_...`). */
userProfileID: string; // path parameter

interface ActionURLCreateParams {
  /** The action that the person who opens the URL takes. */
  action: BetaUserProfileEnrollEndUserAction;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** A URL to give to the person who takes the requested action. */
interface BetaUserProfileActionURL {
  /** Object type. Always `user_profile_action_url`. */
  type: "user_profile_action_url";
  /** When the URL stops working, in RFC 3339 format. */
  expires_at: string; // format: date-time
  /** The URL to give to the person who takes the action. Anyone who holds it can open it until `expires_at`. */
  url: string;
}
```

#### Types

```ts
interface BetaUserProfileEnrollEndUserAction {
  type: "enroll_end_user";
}
```
