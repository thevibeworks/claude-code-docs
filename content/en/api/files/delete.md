---
title: Delete File
url: https://platform.claude.com/docs/en/api/files/delete
---

# Delete File

**DELETE** `/v1/files/{file_id}`

Delete File

## Path parameters

- `file_id: string`

  ID of the File.

## Headers

- `"anthropic-workspace-id": optional string`

## Returns

- `DeletedFile object`

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    default: file_deleted

  - `id: string`

    ID of the deleted file.

## Example

```bash
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
