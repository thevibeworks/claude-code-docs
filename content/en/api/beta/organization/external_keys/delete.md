---
title: Delete External Key
url: https://platform.claude.com/docs/en/api/beta/organization/external_keys/delete
---

# Delete External Key

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

## Path parameters

- `external_key_id: string`

  ID of the External Key.

  maxLength: 2048

## Returns

- `type: "external_key_deleted"`

  default: external_key_deleted

- `id: string`

  ID of the deleted External Key.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```
