---
title: Create Enrollment URL
url: https://platform.claude.com/docs/en/api/cli/beta/user_profiles/create_enrollment_url
---

# Create Enrollment URL

`$ ant beta:user-profiles create-enrollment-url`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

## Parameters

- `--user-profile-id: string`

  The ID of the user profile to create an enrollment URL for (`uprof_...`).

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_user_profile_enrollment_url: object`

  A URL to give to the entity that a user profile represents, so that the entity can enroll for a trust grant.

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

  - `expires_at: string`

    When this enrollment URL expires, in RFC 3339 format.

    format: date-time

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

## Example

```bash
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

### Response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```
