# Members

## List RBAC Group Members

**GET** `/v1/organizations/rbac_groups/{group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

### Path parameters

- `group_id: string`

  ID of the RBAC Group.

### Query parameters

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  Optionally set to the `next_page` token from the previous response.

### Returns

- `data: array of RbacGroupMember`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `user_id: string`

    ID of the User.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `next_page: string or null`

  Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

#### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

## Add RBAC Group Member

**POST** `/v1/organizations/rbac_groups/{group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

### Path parameters

- `group_id: string`

  ID of the RBAC Group.

### Body parameters

- `user_id: string`

  ID of the User.

### Returns

- `RbacGroupMember object`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `user_id: string`

    ID of the User.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        }'
```

#### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Remove RBAC Group Member

**DELETE** `/v1/organizations/rbac_groups/{group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

### Path parameters

- `group_id: string`

  ID of the RBAC Group.

- `user_id: string`

  ID of the User.

### Returns

- `RbacGroupMemberDeleted object`

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    default: rbac_group_member_deleted

  - `user_id: string`

    ID of the User.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
```

#### Response (200)

```json
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Domain types

### Rbac Group Member

- `RbacGroupMember object`

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `user_id: string`

    ID of the User.

### Rbac Group Member Deleted

- `RbacGroupMemberDeleted object`

  - `group_id: string`

    ID of the RBAC Group.

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    default: rbac_group_member_deleted

  - `user_id: string`

    ID of the User.
