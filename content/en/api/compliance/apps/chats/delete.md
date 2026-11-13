---
title: Delete chat
url: https://platform.claude.com/docs/en/api/compliance/apps/chats/delete
---

# Delete chat

**DELETE** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

A chat's remote sessions are deleted first. If that deletion cannot be
confirmed, the request returns a 503 with error code
`chat_delete_remote_sessions_unconfirmed` and leaves the chat unchanged.
You can retry the request.

## Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Returns

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  default: claude_chat_deleted

- `id: string`

  The ID of the Claude chat that was deleted

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```
