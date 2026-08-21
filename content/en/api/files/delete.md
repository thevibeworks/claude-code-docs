---
title: Delete File
url: https://platform.claude.com/docs/en/api/files/delete
---

## Delete File

**delete** `/v1/files/{file_id}`

Delete File

### Path Parameters

- `file_id: string`

  ID of the File.

### Returns

- `DeletedFile object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/files/$FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
