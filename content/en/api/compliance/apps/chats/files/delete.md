---
title: Delete file
url: https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete
---

# Delete file

**DELETE** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

## Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

## Headers

- `"x-api-key": optional string`

## Returns

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  default: claude_file_deleted

- `id: string`

  The ID of the file that was deleted

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```
