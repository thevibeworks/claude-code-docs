# User Profiles

## Create User Profile

`client.beta.userProfiles.create(params, options?): BetaUserProfile`

**POST** `/v1/user_profiles`

Create User Profile

### Parameters

- `params: UserProfileCreateParams`

  - `access_type?: "application" | "passthrough"`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `external_user_onboarded_at?: string`

    Body param: A timestamp in RFC 3339 format

    format: date-time

  - `metadata?: Record<string, string>`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `name?: string | null`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a company the platform resells Claude access to (`access_type` `passthrough`), that company's name where known. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

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

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `external_user_onboarded_at?: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.create();

console.log(betaUserProfile.id);
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
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

## List User Profiles

`client.beta.userProfiles.list(params?, options?): PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

### Parameters

- `params: UserProfileListParams`

  - `limit?: number`

    Query param: Query parameter for limit

    format: int32

  - `order?: "asc" | "desc"`

    Query param: Query parameter for order

    - `"asc"`

    - `"desc"`

  - `order_by?: "created_at" | "name"`

    Query param: Query parameter for order_by

    - `"created_at"`

    - `"name"`

  - `page?: string`

    Query param: Query parameter for page

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

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

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `external_user_onboarded_at?: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaUserProfile of client.beta.userProfiles.list()) {
  console.log(betaUserProfile.id);
}
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
      "external_user_onboarded_at": "2024-11-02T08:15:00Z",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`client.beta.userProfiles.retrieve(userProfileID, params?, options?): BetaUserProfile`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID: string`

- `params: UserProfileRetrieveParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

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

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `external_user_onboarded_at?: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.retrieve(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfile.id);
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
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

## Update User Profile

`client.beta.userProfiles.update(userProfileID, params, options?): BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID: string`

- `params: UserProfileUpdateParams`

  - `access_type?: "application" | "passthrough" | null`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `external_user_onboarded_at?: string`

    Body param: A timestamp in RFC 3339 format

    format: date-time

  - `metadata?: Record<string, string>`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `name?: string | null`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

### Returns

- `BetaUserProfile`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

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

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `external_user_onboarded_at?: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.update(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfile.id);
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
  "external_user_onboarded_at": "2024-11-02T08:15:00Z",
  "name": "Example User"
}
```

## Create Enrollment URL

`client.beta.userProfiles.createEnrollmentURL(userProfileID, params?, options?): BetaUserProfileEnrollmentURL`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID: string`

- `params: UserProfileCreateEnrollmentURLParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

### Returns

- `BetaUserProfileEnrollmentURL`

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaUserProfileEnrollmentURL = await client.beta.userProfiles.createEnrollmentURL(
  "uprof_011CZkZCu8hGbp5mYRQgUmz9"
);

console.log(betaUserProfileEnrollmentURL.expires_at);
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

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

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

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type?: "application" | "passthrough"`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id?: string | null`

    Platform's own identifier for this user. Not enforced unique.

  - `external_user_onboarded_at?: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `name?: string | null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

### Beta User Profile Enrollment URL

- `BetaUserProfileEnrollmentURL`

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `BetaUserProfileTrustGrant`

  - `status: "active" | "pending" | "rejected"`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`
