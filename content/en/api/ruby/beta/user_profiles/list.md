---
title: List User Profiles
url: https://platform.claude.com/docs/en/api/ruby/beta/user_profiles/list
---

# List User Profiles

`beta.user_profiles.list(**kwargs) -> PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

## Parameters

- `limit: optional Integer` (query parameter)

  The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

  format: int32

- `order: optional :asc | :desc` (query parameter)

  The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.

  - `:asc`

    Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

  - `:desc`

    Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.

- `order_by: optional :created_at | :name` (query parameter)

  The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.

  - `:created_at`

    Sort by when each user profile was created. This is the default.

  - `:name`

    Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.

- `page: optional String` (query parameter)

  The cursor for the page to return, taken from `next_page` in a previous response.

  Leave it out to get the first page.

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaUserProfile`

  A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

  A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    When this user profile was created, in RFC 3339 format.

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `name: String | nil`

    Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `updated_at: Time`

    When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

    format: date-time

  - `access_type: optional :application | :passthrough`

    How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

    - `:application`

      The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

    - `:passthrough`

      The user profile represents a company that the platform resells Claude access to.

  - `external_id: optional String | nil`

    Platform's own identifier for this user. Not enforced unique. Legacy field, present only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, the value is `external_user_details.reference_id`.

  - `external_user_details: optional BetaUserProfileExternalUserDetails`

    Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.

    - `account_status: :active | :suspended | :blocked | nil`

      The status of the entity's account on the platform: `active`, `suspended` or `blocked`. `null` until the platform supplies one.

      - `:active`

        The platform has neither restricted nor barred the account of the entity that the user profile represents.

      - `:suspended`

        The platform has restricted the account of the entity that the user profile represents and may restore it.

      - `:blocked`

        The platform has barred the account of the entity that the user profile represents.

    - `country: String | nil`

      The country the platform associates with the entity, as an ISO 3166-1 alpha-2 code. `null` until the platform supplies one.

    - `email_hash: String | nil`

      The platform-computed hash of the entity's email address. `null` until the platform supplies one.

    - `entity_type: :individual | :business | :non_profit | :government | nil`

      What kind of entity the profile represents: `individual`, `business`, `non_profit` or `government`. `null` until the platform supplies one.

      - `:individual`

      - `:business`

      - `:non_profit`

      - `:government`

    - `name_hash: String | nil`

      The platform-computed hash of the entity's name. `null` until the platform supplies one.

    - `onboarded_at: Time | nil`

      When the entity opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one.

      format: date-time

    - `reference_id: String | nil`

      The platform's own reference for the entity. `null` until the platform supplies one.

  - `external_user_onboarded_at: optional Time | nil`

    When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Legacy field, present only under the `user-profiles-2026-08-18` beta header; without a legacy header, the value is `external_user_details.onboarded_at`.

    format: date-time

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.user_profiles.list

puts(page)
```

### Response (200)

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
