---
title: Certificates
url: https://platform.claude.com/docs/en/api/csharp/beta/tunnels/certificates
---

# Certificates

## Create Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Create(CertificateCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `CertificateCreateParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string caCertificatePem`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateCreateParams parameters = new()
{
    TunnelID = "tunnel_id",
    CaCertificatePem = "ca_certificate_pem",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Create(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Retrieve(CertificateRetrieveParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `CertificateRetrieveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateRetrieveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Retrieve(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

`CertificateListPageResponse Beta.Tunnels.Certificates.List(CertificateListParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `CertificateListParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `Boolean includeArchived`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `Int limit`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class CertificateListPageResponse:`

  The tunnel's certificates.

  - `required IReadOnlyList<BetaTunnelCertificate> Data`

    List of certificates, ordered by created_at descending.

    - `required string ID`

      Unique identifier for the certificate, prefixed with `tcrt_`.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

    - `required DateTimeOffset? ExpiresAt`

      A timestamp in RFC 3339 format

    - `required string Fingerprint`

      Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

    - `required string TunnelID`

      ID of the tunnel the certificate is registered against.

    - `JsonElement Type "tunnel_certificate"constant`

  - `required string? NextPage`

    Pagination cursor for the next page, or null if no more results.

### Example

```csharp
CertificateListParams parameters = new() { TunnelID = "tunnel_id" };

var page = await client.Beta.Tunnels.Certificates.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Archive(CertificateArchiveParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `CertificateArchiveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`

### Example

```csharp
CertificateArchiveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Archive(parameters);

Console.WriteLine(betaTunnelCertificate);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Domain Types

### Beta Tunnel Certificate

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type "tunnel_certificate"constant`
