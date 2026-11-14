---
title: Files
url: https://platform.claude.com/docs/en/api/ruby/beta/files
---

# Files

## Upload File

`beta.files.upload(**kwargs) -> BetaFileMetadata`

**POST** `/v1/files`

Upload File

### Parameters

- `file: FileInput`

  The file to upload. Only the final path component of the part's `filename` is kept; an absent or empty `filename` is replaced with `unnamed` plus the extension for the file's stored `mime_type`, when known.

  format: binary

- `expires_in_seconds: optional Integer`

  Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

  minimum: 3600, maximum: 7776000

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: optional bool`

    Whether the file can be downloaded.

  - `expires_at: optional Time | nil`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional BetaFileScope | nil`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `StorageQuotaExceededError` (HTTP status 400, error code `storage_quota_exceeded`)

  The organization's file storage quota is exhausted. Delete files to free up space, then retry the upload.

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

- `ids: optional Array[String] | nil` (query parameter)

  Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

- `limit: optional Integer` (query parameter)

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `page: optional String | nil` (query parameter)

  Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

- `scope_id: optional String` (query parameter)

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: optional bool`

    Whether the file can be downloaded.

  - `expires_at: optional Time | nil`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional BetaFileScope | nil`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

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

- `file_id: String` (path parameter)

  ID of the File.

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `StringIO`

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `FileNotDownloadableError` (HTTP status 400, error code `file_not_downloadable`)

  The file has `downloadable: false`. Only files generated by a tool, such as the code execution tool, can be downloaded.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `FileExpiredError` (HTTP status 404, error code `file_expired`)

  The file's `expires_at` has passed, so its content is no longer available.

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

- `file_id: String` (path parameter)

  ID of the File.

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: optional bool`

    Whether the file can be downloaded.

  - `expires_at: optional Time | nil`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional BetaFileScope | nil`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

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

- `file_id: String` (path parameter)

  ID of the File.

- `betas: optional Array[AnthropicBeta]` (header parameter)

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaDeletedFile`

  - `type: optional :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: String`

    ID of the deleted file.

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

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

  - `type: optional :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: String`

    ID of the deleted file.

### Beta File Metadata

- `class BetaFileMetadata`

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    minLength: 1, maxLength: 500

  - `mime_type: String`

    MIME type of the file.

    minLength: 1, maxLength: 255

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `downloadable: optional bool`

    Whether the file can be downloaded.

  - `expires_at: optional Time | nil`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `scope: optional BetaFileScope | nil`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `type: :session`

      The type of scope (e.g., `"session"`).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

### Beta File Scope

- `class BetaFileScope`

  - `type: :session`

    The type of scope (e.g., `"session"`).

  - `id: String`

    The ID of the scoping resource (e.g., the session ID).
