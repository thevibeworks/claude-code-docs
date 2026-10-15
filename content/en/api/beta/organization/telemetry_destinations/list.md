---
title: List Telemetry Destinations
url: https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/list
---

# List Telemetry Destinations

**GET** `/v1/organizations/telemetry_destinations`

List the organization's destinations, newest first, optionally only those that cover given workspaces.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#set-up-api-tracing) to learn more about destinations.

## Query parameters

- `limit: optional number`

  Number of destinations to return per page, between 1 and 1,000. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`. Leave it out to get the first page.

- `workspace_ids: optional array of string`

  Return only the destinations that cover at least one of these workspaces (`wrkspc_...`).

  Send at most 100 IDs, as `workspace_ids[]`. A destination covers a workspace when its `workspaces.type` is `all`, when its `include` list has the workspace, or when its `exclude` list doesn't have it. Destinations in either state can match. An ID that isn't the ID of one of the organization's workspaces doesn't match any destination, not even one whose type is `all`.

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

- `data: array of BetaTelemetryDestination`

  Destinations on this page, newest first.

  - `type: "telemetry_destination"`

  - `id: string`

    The unique ID of the destination (`tdst_...`).

  - `created_at: string`

    Time the destination was created.

    format: date-time

  - `delivery_health: BetaTelemetryDestinationDeliveryHealth`

    The most recent delivery results for this destination.

    - `last_error: string or null`

      A message that describes the most recent failed delivery to the destination, or `null` if no delivery has failed yet.

      Examples are `temporary DNS failure`, `TLS failure`, `timeout`, `connection failure`, `invalid address`, `HTTP error (status 503)`, and `redirect (status 301)`. The message is `invalid address` both for a hostname that doesn't exist and for an address that isn't publicly routable. It never contains the endpoint's response body, a header value, a network address, or TLS details.

      `last_error` and `last_error_at` always change together. A later successful delivery doesn't clear them. If `last_success_at` is later than `last_error_at`, a delivery has succeeded since this failure.

      See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-errors) to learn the likely cause of each error.

    - `last_error_at: string or null`

      Time of the failure that `last_error` describes. Changes together with `last_error`. Null until a delivery first fails.

      format: date-time

    - `last_success_at: string or null`

      Time of the most recent successful delivery to the destination, or `null` if no delivery has succeeded yet.

      format: date-time

  - `display_name: string or null`

    Human-readable name for the destination. Null when none was set.

  - `endpoint_url: string`

    The base URL of the destination's OTLP/HTTP endpoint, exactly as registered.

    The API appends the per-signal path, such as `/v1/traces`, on delivery, unless `traces.endpoint_url` is set.

  - `header_names: array of string`

    Names of the registered request headers. Header values are write-only and are never returned.

  - `state: BetaTelemetryDestinationState`

    Whether the destination receives deliveries.

    - `BetaTelemetryDestinationStateEnabled object`

      The telemetry destination receives the spans of the workspaces that it covers.

      - `type: "enabled"`

    - `BetaTelemetryDestinationStateDisabled object`

      The API doesn't deliver anything to the telemetry destination.

      Spans produced while it is disabled aren't delivered later.

      - `type: "disabled"`

      - `reason: BetaTelemetryDestinationDisabledReason`

        Whether a caller or the API disabled the destination and, when the API did, why. Read-only.

        - `BetaTelemetryDestinationDisabledReasonCaller object`

          A caller disabled the destination with an update that set `state` to `disabled`.

          - `type: "caller"`

        - `BetaTelemetryDestinationDisabledReasonSustainedFailure object`

          The API disabled the destination because deliveries to it failed, with no successful delivery in between, for longer than a threshold that Anthropic configures and that is not part of this contract. The reason is `invalid_address` instead when the most recent failed delivery failed with an invalid address.

          - `type: "sustained_failure"`

        - `BetaTelemetryDestinationDisabledReasonInvalidAddress object`

          The API disabled the destination because deliveries to it failed for longer than the same threshold as for `sustained_failure`, and the most recent failed delivery failed with an invalid address: the DNS answer says that the endpoint's hostname doesn't exist or doesn't have an address, or the address that the API would connect to isn't publicly routable or is reserved, for example a loopback, link-local, private-network, or cloud-metadata address. The API doesn't connect to such an address, and retries the delivery a bounded number of times as it does after a timeout. A timeout or a server failure of the DNS lookup is a temporary DNS failure instead, not an invalid address.

          - `type: "invalid_address"`

        - `BetaTelemetryDestinationDisabledReasonRedirect object`

          The API disabled the destination because the endpoint answered a delivery with a 3xx status. Redirects are never followed, and one such answer disables the destination at once.

          - `type: "redirect"`

  - `traces: BetaTelemetryDestinationTraces`

    The destination's settings for the traces it receives.

    - `content_mode: BetaTelemetryDestinationContentMode`

      What the exported spans contain.

      - `"metadata_only"`

        The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.

      - `"content"`

        The spans contain the same metadata as `metadata_only`, plus message and tool content.

        An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.

    - `enabled: boolean`

      Whether the destination receives traces. A destination whose `enabled` is false keeps its other settings.

    - `endpoint_url: string or null`

      The full URL that the API posts traces to, exactly as registered, or `null` if the destination doesn't have one.

      When it is `null`, the API posts traces to `endpoint_url` with `/v1/traces` appended.

    - `max_content_bytes: number or null`

      The most bytes of content that one exported span can contain, or `null` if only the API's maximum applies.

      Content means model prompts and responses, and tool inputs and outputs. The API shortens longer content to this size before it delivers the span. A destination whose `content_mode` is `metadata_only` keeps this value. It applies once `content_mode` is `content`.

      format: int32

  - `updated_at: string`

    Time of the last change to the destination's configuration or state. Changes to `delivery_health` don't change it.

    An update that sets a header value always changes it, even when the value is the same as before. Adding or removing a single workspace on the destination's list doesn't change it. An update that changes the list does.

    format: date-time

  - `workspaces: BetaTelemetryDestinationWorkspaces`

    Which of the organization's workspaces the destination covers.

    - `BetaTelemetryDestinationWorkspacesAll object`

      The destination covers every workspace of the organization, including the default workspace, archived workspaces, and workspaces created later. It doesn't have a list.

      - `type: "all"`

    - `BetaTelemetryDestinationWorkspacesInclude object`

      The destination covers the workspaces on its list, and no others.

      - `type: "include"`

    - `BetaTelemetryDestinationWorkspacesExclude object`

      The destination covers every workspace of the organization except the workspaces on its list. A workspace created later is covered until it is added to the list.

      - `type: "exclude"`

- `next_page: string or null`

  Cursor for the next page. Null on the last page.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "delivery_health": {
        "last_error": "last_error",
        "last_error_at": "2019-12-27T18:11:19.117Z",
        "last_success_at": "2019-12-27T18:11:19.117Z"
      },
      "display_name": "display_name",
      "endpoint_url": "endpoint_url",
      "header_names": [
        "string"
      ],
      "state": {
        "type": "enabled"
      },
      "traces": {
        "content_mode": "metadata_only",
        "enabled": true,
        "endpoint_url": "endpoint_url",
        "max_content_bytes": 0
      },
      "type": "telemetry_destination",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "workspaces": {
        "type": "all"
      }
    }
  ],
  "next_page": "next_page"
}
```
