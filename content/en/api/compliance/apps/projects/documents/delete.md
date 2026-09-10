---
title: Delete project document
url: https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/delete
---

# Delete project document

**DELETE** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

## Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

- `"x-api-key": optional string`

## Returns

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  default: claude_project_document_deleted

- `id: string`

  The ID of the project document that was deleted

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```
