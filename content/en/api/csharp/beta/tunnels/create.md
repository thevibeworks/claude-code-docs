---
title: Create Tunnel
url: https://platform.claude.com/docs/en/api/csharp/beta/tunnels/create
---

## Create Tunnel

`BetaTunnel Beta.Tunnels.Create(TunnelCreateParams?parameters, CancellationTokencancellationToken = default)`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `TunnelCreateParams parameters`

  - `string? displayName`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

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

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type "tunnel"constant`

### Example

```csharp
TunnelCreateParams parameters = new();

var betaTunnel = await client.Beta.Tunnels.Create(parameters);

Console.WriteLine(betaTunnel);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```
