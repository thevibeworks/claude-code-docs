# Upload File

**POST** `/v1/files`

Upload File

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

## Body parameters (form-data)

- `file: string`

  The file to upload

  format: binary

- `expires_in_seconds: optional number`

  Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

## Returns

- `BetaFileMetadata object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: string`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: string`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: number`

    Size of the file in bytes.

    minimum: 0

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

    default: false

  - `expires_at: optional string or null`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional BetaFileScope or null`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

## Example

```bash
curl https://api.anthropic.com/v1/files \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F 'file=@/path/to/file'
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z",
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```
