# Files

## Upload File

`BetaFileMetadata Beta.Files.Upload(parameters, cancellationToken = default)`

**POST** `/v1/files`

Upload File

### Parameters

- `FileUploadParams parameters`

  - `required string file`

    Body param: The file to upload

    format: binary

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileUploadParams parameters = new()
{
    File = Encoding.UTF8.GetBytes("Example data")
};

var betaFileMetadata = await client.Beta.Files.Upload(parameters);

Console.WriteLine(betaFileMetadata);
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

`FileListPageResponse Beta.Files.List(parameters, cancellationToken = default)`

**GET** `/v1/files`

List Files

### Parameters

- `FileListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `string scopeID`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

### Returns

- `class FileListPageResponse:`

  - `required IReadOnlyList<BetaFileMetadata> Data`

    List of file metadata objects.

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing when the file was created.

      format: date-time

    - `required string Filename`

      Original filename of the uploaded file.

      maxLength: 500, minLength: 1

    - `required string MimeType`

      MIME type of the file.

      maxLength: 255, minLength: 1

    - `required long SizeBytes`

      Size of the file in bytes.

      minimum: 0

    - `JsonElement Type constant`

      Object type.

      For files, this is always `"file"`.

    - `bool Downloadable`

      Whether the file can be downloaded.

    - `BetaFileScope? Scope`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `required string ID`

        The ID of the scoping resource (e.g., the session ID).

      - `JsonElement Type constant`

        The type of scope (e.g., `"session"`).

  - `string? FirstID`

    ID of the first file in this page of results.

  - `bool HasMore`

    Whether there are more results available.

  - `string? LastID`

    ID of the last file in this page of results.

### Example

```csharp
FileListParams parameters = new();

var page = await client.Beta.Files.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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

`HttpResponse Beta.Files.Download(parameters, cancellationToken = default)`

**GET** `/v1/files/{file_id}/content`

Download File

### Parameters

- `FileDownloadParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

### Example

```csharp
FileDownloadParams parameters = new() { FileID = "file_id" };

var response = await client.Beta.Files.Download(parameters);

Console.WriteLine(response);
```

## Get File Metadata

`BetaFileMetadata Beta.Files.RetrieveMetadata(parameters, cancellationToken = default)`

**GET** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `FileRetrieveMetadataParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

### Example

```csharp
FileRetrieveMetadataParams parameters = new() { FileID = "file_id" };

var betaFileMetadata = await client.Beta.Files.RetrieveMetadata(parameters);

Console.WriteLine(betaFileMetadata);
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

`BetaDeletedFile Beta.Files.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/files/{file_id}`

Delete File

### Parameters

- `FileDeleteParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

### Returns

- `class BetaDeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Example

```csharp
FileDeleteParams parameters = new() { FileID = "file_id" };

var betaDeletedFile = await client.Beta.Files.Delete(parameters);

Console.WriteLine(betaDeletedFile);
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

- `class BetaDeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

### Beta File Metadata

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

### Beta File Scope

- `class BetaFileScope:`

  - `required string ID`

    The ID of the scoping resource (e.g., the session ID).

  - `JsonElement Type constant`

    The type of scope (e.g., `"session"`).
