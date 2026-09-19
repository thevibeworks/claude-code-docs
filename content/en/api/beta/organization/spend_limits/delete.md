---
title: Delete Spend Limit
url: https://platform.claude.com/docs/en/api/beta/organization/spend_limits/delete
---

# Delete Spend Limit

**DELETE** `/v1/organizations/spend_limits/{spend_limit_id}`

Delete a spend limit.

For a Claude Enterprise organization, this deletes a per-user override, and
the member falls back to any inherited spend limit at that period. Its
seat-tier, group, and organization-level rows cannot be deleted via this
endpoint. A Claude Console organization deletes its organization and
workspace limits. Deleting them through the API is in an early access preview.

## Path parameters

- `spend_limit_id: string`

  ID of the Spend Limit.

## Returns

- `type: "spend_limit_deleted"`

  default: spend_limit_deleted

- `id: string`

## Example

```bash
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```
