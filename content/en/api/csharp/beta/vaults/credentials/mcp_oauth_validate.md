# Validate Credential

`BetaManagedAgentsCredentialValidation Beta.Vaults.Credentials.McpOAuthValidate(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

## Parameters

- `CredentialMcpOAuthValidateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

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

## Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required bool HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    The failing step of an MCP validation probe.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required bool BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required int StatusCode`

        HTTP status code.

        format: int32

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

    - `required Status Status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `Succeeded`

      - `Failed`

      - `ConnectError`

      - `NoRefreshToken`

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of a credential validation probe.

    - `Valid`

    - `Invalid`

    - `Unknown`

  - `required Type Type`

  - `required DateTimeOffset ValidatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault containing the credential.

## Example

```csharp
CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
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
