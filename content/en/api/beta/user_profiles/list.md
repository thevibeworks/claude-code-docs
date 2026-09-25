---
title: List User Profiles
url: https://platform.claude.com/docs/en/api/beta/user_profiles/list
---

# List User Profiles

**GET** `/v1/user_profiles`

List User Profiles

## Query parameters

- `limit: optional number`

  The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

  format: int32

- `order: optional "asc" or "desc"`

  The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.

  - `"asc"`

    Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

  - `"desc"`

    Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.

- `order_by: optional "created_at" or "name"`

  The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.

  - `"created_at"`

    Sort by when each user profile was created. This is the default.

  - `"name"`

    Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.

- `page: optional string`

  The cursor for the page to return, taken from `next_page` in a previous response.

  Leave it out to get the first page.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more`

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

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `data: array of BetaUserProfile`

  User profiles on this page.

  - `type: "user_profile"`

    Object type. Always `user_profile`.

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    When this user profile was created, in RFC 3339 format.

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

  - `updated_at: string`

    When this user profile was last modified, in RFC 3339 format. Trust-grant status changes also bump this timestamp.

    format: date-time

  - `access_type: optional "application" or "passthrough"`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Present under the `user-profiles-2026-08-18` and later beta headers.

    - `"application"`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `"passthrough"`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: optional string or null`

    Platform's own identifier for this user. Not enforced unique. Present under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; under `user-profiles-2026-09-04` the value is `external_user_details.reference_id`.

  - `external_user_details: optional BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Present under the `user-profiles-2026-09-04` beta header, with every field present and `null` until the platform supplies a value; the earlier beta headers serve `reference_id` as the top-level `external_id`, and `user-profiles-2026-08-18` serves `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: "active" or "suspended" or "blocked" or null`

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

    - `entity_type: "individual" or "business" or "non_profit" or "government" or null`

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

  - `external_user_onboarded_at: optional string or null`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Present under the `user-profiles-2026-08-18` beta header; under `user-profiles-2026-09-04` the value is `external_user_details.onboarded_at`.

    format: date-time

  - `name: optional string or null`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name.

- `next_page: string or null`

  Cursor for the next page, or `null` when there are no more results.

## Example

```bash
curl https://api.anthropic.com/v1/user_profiles \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-08-18' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
