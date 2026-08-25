# Generated Files

## Get Claude-generated file metadata

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}`

Returns metadata for a file the assistant created via tool use.

Use the sibling `/content` endpoint to download the bytes.

### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Headers

- `"x-api-key": optional string`

### Returns

- `id: string`

  Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

- `claude_chat_id: string`

  The chat this generated file belongs to

- `created_at: string or null`

  File creation timestamp, when available

  format: date-time

- `filename: string`

  Display name of the generated file

- `md5: string or null`

  Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

- `mime_type: string or null`

  MIME type of the stored file, when available

- `size_bytes: number or null`

  Size in bytes of the stored file, when available

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

## Download a Claude-generated file

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Headers

- `"x-api-key": optional string`

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain types

### Generated File Retrieve Response

- `GeneratedFileRetrieveResponse object`

  Metadata for GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the bytes. The owning chat is included since the id is opaque; to find the
  specific message that produced the file, fetch
  `/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
  `generated_files[].id`.

  - `id: string`

    Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

  - `claude_chat_id: string`

    The chat this generated file belongs to

  - `created_at: string or null`

    File creation timestamp, when available

    format: date-time

  - `filename: string`

    Display name of the generated file

  - `md5: string or null`

    Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

  - `mime_type: string or null`

    MIME type of the stored file, when available

  - `size_bytes: number or null`

    Size in bytes of the stored file, when available
