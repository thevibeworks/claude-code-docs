---
title: Update User Profile
url: https://platform.claude.com/docs/en/api/python/beta/user_profiles/update
---

## Update User Profile

`beta.user_profiles.update(struser_profile_id, UserProfileUpdateParams**kwargs)  -> BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `user_profile_id: str`

- `access_type: Optional[Literal["application", "passthrough"]]`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `"application"`

  - `"passthrough"`

- `external_id: Optional[str]`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: Optional[str]`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship: Optional[Literal["external", "resold", "internal"]]`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.update(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile.id)
```

#### Response

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
  "name": "Example User",
  "relationship": "external"
}
```
