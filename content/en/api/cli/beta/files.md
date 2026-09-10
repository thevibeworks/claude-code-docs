---
title: Files
url: https://platform.claude.com/docs/en/api/cli/beta/files
---

# Files

## Upload File

`$ ant beta:files upload`

**POST** `/v1/files`

Upload File

### Parameters

- `--file: string`

  Body param: The file to upload. Only the final path component of the part's `filename` is kept; an absent or empty `filename` is replaced with `unnamed` plus the extension for the file's stored `mime_type`, when known.

  format: binary

- `--expires-in-seconds: optional number`

  Body param: Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_file_metadata: object`

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `expires_at: optional string`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional object`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

### Example

```bash
ant beta:files upload \
  --api-key my-anthropic-api-key \
  --file 'Example data'
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

`$ ant beta:files list`

**GET** `/v1/files`

List Files

### Parameters

- `--id: optional array of string`

  Query param: Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--page: optional string`

  Query param: Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

- `--scope-id: optional string`

  Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaFileListResponse: object`

  - `data: array of BetaFileMetadata`

    List of file metadata objects.

    - `type: "file"`

      Object type.

      For files, this is always `"file"`.

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

    - `downloadable: optional boolean`

      Whether the file can be downloaded.

    - `expires_at: optional string`

      RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

      format: date-time

    - `scope: optional object`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `type: "session"`

        The type of scope (e.g., `"session"`).

      - `id: string`

        The ID of the scoping resource (e.g., the session ID).

  - `next_page: optional string`

    Opaque cursor for the next page. Supply as `?page=` to fetch the next page; null when there are no more results.

### Example

```bash
ant beta:files list \
  --api-key my-anthropic-api-key
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

`$ ant beta:files download`

**GET** `/v1/files/{file_id}/content`

Download File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `unnamed_schema_1: file path`

### Example

```bash
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

## Get File Metadata

`$ ant beta:files retrieve-metadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_file_metadata: object`

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `expires_at: optional string`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional object`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

### Example

```bash
ant beta:files retrieve-metadata \
  --api-key my-anthropic-api-key \
  --file-id file_id
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

`$ ant beta:files delete`

**DELETE** `/v1/files/{file_id}`

Delete File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_deleted_file: object`

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: string`

    ID of the deleted file.

### Example

```bash
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
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

- `beta_deleted_file: object`

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: string`

    ID of the deleted file.

### Beta File Metadata

- `beta_file_metadata: object`

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

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

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `expires_at: optional string`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional object`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

### Beta File Scope

- `beta_file_scope: object`

  - `type: "session"`

    The type of scope (e.g., `"session"`).

  - `id: string`

    The ID of the scoping resource (e.g., the session ID).
