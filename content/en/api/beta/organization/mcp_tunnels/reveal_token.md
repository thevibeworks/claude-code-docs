---
title: Reveal Tunnel Token
url: https://platform.claude.com/docs/en/api/beta/organization/mcp_tunnels/reveal_token
---

# Reveal Tunnel Token

**POST** `/v1/organizations/tunnels/{tunnel_id}/reveal_token`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Return the tunnel's current connection token.

The value is fetched live on each call; Anthropic does not store it.
Repeated calls return the same value until the token is rotated.
Exposed as `POST` so the token does not appear in intermediary
access logs.

## Path parameters

- `tunnel_id: string`

  ID of the Tunnel.

## Headers

- `"anthropic-beta": array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 42 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"user-profiles-2026-09-04"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

## Returns

- `BetaOrganizationTunnelToken object`

  - `type: "tunnel_token"`

    Object type. Always `tunnel_token` for Tunnel Tokens.

    default: tunnel_token

  - `id: string`

    Stable identifier for the current token value. Changes when the token is
    rotated.

  - `tunnel_token: string`

    The tunnel's connection token.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/reveal_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```
