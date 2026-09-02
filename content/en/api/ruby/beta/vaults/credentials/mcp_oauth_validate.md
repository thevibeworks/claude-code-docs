# Validate Credential

`beta.vaults.credentials.mcp_oauth_validate(credential_id, **kwargs) -> BetaManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

## Parameters

- `vault_id: String`

- `credential_id: String`

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

## Returns

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: String`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: String`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: String`

        Value of the `Content-Type` response header.

      - `status_code: Integer`

        HTTP status code.

        format: int32

    - `method_: String`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `:succeeded`

      - `:failed`

      - `:connect_error`

      - `:no_refresh_token`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `:valid`

    - `:invalid`

    - `:unknown`

  - `type: :vault_credential_validation`

  - `validated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault containing the credential.

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential_validation = anthropic.beta.vaults.credentials.mcp_oauth_validate(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential_validation)
```

### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```
