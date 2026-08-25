# Delete project

**DELETE** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

## Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

## Headers

- `"x-api-key": optional string`

## Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  default: claude_project_deleted

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```
