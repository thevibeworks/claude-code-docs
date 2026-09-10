---
title: List Tunnels
url: https://platform.claude.com/docs/en/api/beta/organization/mcp_tunnels/list
---

# List Tunnels

**GET** `/v1/organizations/tunnels`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the organization's tunnels.

Results span the caller's organization, ordered by creation time
(newest first). Use `workspace_id` to filter to a single workspace;
archived tunnels are excluded unless `include_archived` is set.

## Query parameters

- `include_archived: optional boolean`

  Include archived tunnels in the results. Archived tunnels are excluded by
  default.

  default: false

- `limit: optional number`

  Maximum number of tunnels to return in a single page.

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  Opaque pagination cursor from a previous response's `next_page`. Omit to
  fetch the first page.

- `workspace_id: optional string`

  Return only tunnels in this Workspace. Accepts a `wrkspc_`-prefixed
  Workspace ID; omit to list tunnels across all Workspaces.

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

- `data: array of BetaOrganizationTunnel`

  - `type: "tunnel"`

    Object type. Always `tunnel` for Tunnels.

    default: tunnel

  - `id: string`

    ID of the Tunnel.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the Tunnel was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the Tunnel was created.

    format: date-time

  - `display_name: string or null`

    Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

  - `domain: string`

    Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
    subdomain of this value are routed through the Tunnel. Globally unique and
    never reused, even after the Tunnel is archived.

  - `workspace_id: string or null`

    ID of the Workspace this Tunnel belongs to, or `null` for the default
    Workspace. Immutable after creation.

- `next_page: string or null`

  Opaque cursor for the next page, or `null` if there are no more results.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
