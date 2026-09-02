# Files

## Upload File

`beta.files.upload(**kwargs) -> BetaFileMetadata`

**POST** `/v1/files`

Upload File

### Parameters

- `file: String`

  The file to upload

  format: binary

- `expires_in_seconds: Integer`

  Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 41 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.upload(file: StringIO.new("Example data"))

puts(beta_file_metadata)
```

#### Response (200)

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

## List Files

`beta.files.list(**kwargs) -> PageCursor<BetaFileMetadata>`

**GET** `/v1/files`

List Files

### Parameters

- `ids: Array[String]`

  Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `page: String`

  Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

- `scope_id: String`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 41 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.files.list

puts(page)
```

#### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Download File

`beta.files.download(file_id, **kwargs) -> StringIO`

**GET** `/v1/files/{file_id}/content`

Download File

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 41 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `StringIO`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.files.download("file_id")

puts(response)
```

## Get File Metadata

`beta.files.retrieve_metadata(file_id, **kwargs) -> BetaFileMetadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 41 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(beta_file_metadata)
```

#### Response (200)

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

## Delete File

`beta.files.delete(file_id, **kwargs) -> BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 41 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `class BetaDeletedFile`

  - `id: String`

    ID of the deleted file.

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_file = anthropic.beta.files.delete("file_id")

puts(beta_deleted_file)
```

#### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Domain types

### Beta Deleted File

- `class BetaDeletedFile`

  - `id: String`

    ID of the deleted file.

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Beta File Metadata

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `expires_at: Time`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

### Beta File Scope

- `class BetaFileScope`

  - `id: String`

    The ID of the scoping resource (e.g., the session ID).

  - `type: :session`

    The type of scope (e.g., `"session"`).
