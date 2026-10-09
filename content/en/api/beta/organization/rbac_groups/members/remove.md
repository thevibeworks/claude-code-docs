---
title: Remove RBAC Group Member
url: https://platform.claude.com/docs/en/api/beta/organization/rbac_groups/members/remove
---

# Remove RBAC Group Member

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

## Path parameters

- `rbac_group_id: string`

  ID of the RBAC Group.

- `user_id: string`

  ID of the User.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

## Returns

- `type: "rbac_group_member_deleted"`

  Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

  default: rbac_group_member_deleted

- `rbac_group_id: string`

  ID of the RBAC Group.

- `user_id: string`

  ID of the User.

- `group_id: string`

  **Deprecated**: Use `rbac_group_id` instead; `group_id` always has the same value.

  Deprecated: use `rbac_group_id` instead. ID of the RBAC Group; always the same value as `rbac_group_id`.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/rbac_groups/$RBAC_GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```
