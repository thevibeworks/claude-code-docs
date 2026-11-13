---
title: Get RBAC Role
url: https://platform.claude.com/docs/en/api/beta/organization/rbac_roles/retrieve
---

# Get RBAC Role

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

## Path parameters

- `rbac_role_id: string`

  ID of the RBAC Role.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

## Returns

- `BetaRBACRole object`

  - `type: "rbac_role"`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    default: rbac_role

  - `id: string`

    ID of the RBAC Role.

  - `created_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `display_name: string`

    Name of the RBAC Role. For a built-in role, this is Anthropic's name for the access that the role grants. Anthropic may change this name, so to keep a lasting reference to a role, store its `id`.

  - `source: BetaRBACRoleSource`

    Whether the RBAC Role is built-in or custom. More values of `type` may be added, so do not treat every role that is not `built_in` as `custom`.

    - `BetaRBACRoleSourceBuiltIn object`

      - `type: "built_in"`

        Anthropic provisions the RBAC Role, and the organization's administrators cannot change or delete it.

        default: built_in

    - `BetaRBACRoleSourceCustom object`

      - `type: "custom"`

        The organization's administrators can change and delete the RBAC Role.

        default: custom

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_roles/$RBAC_ROLE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "source": {
    "type": "built_in"
  },
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
