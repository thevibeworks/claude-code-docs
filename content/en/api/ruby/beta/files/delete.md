---
title: Delete File
url: https://platform.claude.com/docs/en/api/ruby/beta/files/delete
---

# Delete File

`beta.files.delete(file_id, **kwargs) -> BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

## Parameters

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

## Returns

- `class BetaDeletedFile`

  - `type: optional :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

  - `id: String`

    ID of the deleted file.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=ruby).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_file = anthropic.beta.files.delete("file_id")

puts(beta_deleted_file)
```

### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```
