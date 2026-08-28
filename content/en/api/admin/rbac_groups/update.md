# Update RBAC Group

**POST** `/v1/organizations/rbac_groups/{group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is available to Claude Enterprise organizations only.

## Path parameters

- `group_id: string`

  ID of the RBAC Group.

## Body parameters

- `name: optional string or null`

  Name of the RBAC Group. Not uniqueness-enforced.

  maxLength: 255, minLength: 1

## Returns

- `RbacGroup object`

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `roles: array of string or null`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "name": "Engineering"
        }'
```

### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
