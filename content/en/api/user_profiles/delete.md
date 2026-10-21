---
title: Delete User Profile
url: https://platform.claude.com/docs/en/api/user_profiles/delete
---

# Delete User Profile

**DELETE** `/v1/user_profiles/{user_profile_id}`

Delete User Profile

## Path parameters

- `user_profile_id: string`

  The ID of the user profile to delete (`uprof_...`).

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `DeletedUserProfile object`

  - `type: "user_profile_deleted"`

    Object type. Always `user_profile_deleted`.

  - `id: string`

    Identifier of the deleted user profile, prefixed `uprof_`.

## Example

```bash
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "type": "user_profile_deleted"
}
```
