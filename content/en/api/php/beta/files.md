# Files

## Upload File

`$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): BetaFileMetadata`

**POST** `/v1/files`

Upload File

### Parameters

- `file: string`

  The file to upload

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaFileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaFileMetadata = $client->beta->files->upload(
  file: FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaFileMetadata);
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
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## List Files

`$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<BetaFileMetadata>`

**GET** `/v1/files`

List Files

### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20

- `scopeID?:optional string`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaFileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->files->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  scopeID: 'scope_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($page);
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
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

## Download File

`$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download`

**GET** `/v1/files/{file_id}/content`

Download File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `mixed`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->files->download(
  'file_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($response);
```

## Get File Metadata

`$client->beta->files->retrieveMetadata(string fileID, ?list<AnthropicBeta> betas): BetaFileMetadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaFileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaFileMetadata = $client->beta->files->retrieveMetadata(
  'file_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaFileMetadata);
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
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

## Delete File

`$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

### Parameters

- `fileID: string`

  ID of the File.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaDeletedFile`

  - `string id`

    ID of the deleted file.

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedFile = $client->beta->files->delete(
  'file_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaDeletedFile);
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

- `BetaDeletedFile`

  - `string id`

    ID of the deleted file.

  - `?Type type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Beta File Metadata

- `BetaFileMetadata`

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing when the file was created.

  - `string filename`

    Original filename of the uploaded file.

  - `string mimeType`

    MIME type of the file.

  - `int sizeBytes`

    Size of the file in bytes.

  - `"file" type`

    Object type.

    For files, this is always `"file"`.

  - `?bool downloadable`

    Whether the file can be downloaded.

  - `?BetaFileScope scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

### Beta File Scope

- `BetaFileScope`

  - `string id`

    The ID of the scoping resource (e.g., the session ID).

  - `"session" type`

    The type of scope (e.g., `"session"`).
