---
title: Remove a Telemetry Destination Workspace
url: https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/workspaces/remove
---

# Remove a Telemetry Destination Workspace

**DELETE** `/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}`

Remove one workspace from a destination's workspace list.

Under `include` the workspace's spans stop going to the destination. Under `exclude` they start. An archived workspace can be removed too.

The API returns 404 when the workspace isn't on the list. A destination whose `workspaces.type` is `all` doesn't have a list, so the API returns 400.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-workspaces-for-a-destination) to learn more about choosing the workspaces of a destination.

## Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

- `workspace_id: string`

  ID of the workspace to remove (`wrkspc_...`).

## Headers

- `"anthropic-version": optional string`

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

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

## Returns

- `BetaDeletedTelemetryDestinationWorkspace object`

  Confirmation that a workspace was removed from a destination's list.

  - `type: "telemetry_destination_workspace_deleted"`

  - `telemetry_destination_id: string`

    ID of the telemetry destination (`tdst_...`).

  - `workspace_id: string`

    ID of the workspace that was removed (`wrkspc_...`).

## Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "telemetry_destination_id": "telemetry_destination_id",
  "type": "telemetry_destination_workspace_deleted",
  "workspace_id": "workspace_id"
}
```
