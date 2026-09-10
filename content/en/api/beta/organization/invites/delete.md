---
title: Delete Invite
url: https://platform.claude.com/docs/en/api/beta/organization/invites/delete
---

# Delete Invite

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

## Path parameters

- `invite_id: string`

  ID of the Invite.

## Returns

- `type: "invite_deleted"`

  Deleted object type.

  For Invites, this is always `"invite_deleted"`.

  default: invite_deleted

- `id: string`

  ID of the Invite.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```
