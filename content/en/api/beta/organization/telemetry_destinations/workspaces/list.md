---
title: List Telemetry Destination Workspaces
url: https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/workspaces/list
---

# List Telemetry Destination Workspaces

**GET** `/v1/organizations/telemetry_destinations/{destination_id}/workspaces`

List the workspaces on a destination's workspace list, newest entry first.

A destination whose `workspaces.type` is `all` doesn't have a list, so its page is empty. The list includes archived workspaces.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-workspaces-for-a-destination) to learn more about choosing the workspaces of a destination.

## Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

## Query parameters

- `limit: optional number`

  Number of entries to return per page, between 1 and 1,000. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`. Leave it out to get the first page.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `telemetry-destinations-2026-08-11` in this header.

  - `string`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

## Returns

- `data: array of BetaTelemetryDestinationWorkspace`

  Entries on this page, newest first.

  - `type: "telemetry_destination_workspace"`

  - `created_at: string`

    Time the workspace was added to the list.

    format: date-time

  - `telemetry_destination_id: string`

    ID of the telemetry destination (`tdst_...`).

  - `workspace_id: string`

    ID of the workspace (`wrkspc_...`).

- `next_page: string or null`

  Cursor for the next page. Null on the last page.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/workspaces \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "created_at": "2019-12-27T18:11:19.117Z",
      "telemetry_destination_id": "telemetry_destination_id",
      "type": "telemetry_destination_workspace",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```
