---
title: Create a Telemetry Destination
url: https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/create
---

# Create a Telemetry Destination

**POST** `/v1/organizations/telemetry_destinations`

Register an OpenTelemetry destination for the organization.

The destination starts in state `enabled`. An organization can have at most 10 destinations, including disabled ones.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#add-a-destination) to learn more about adding a destination.

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

## Body parameters

- `endpoint_url: string`

  The base URL of your collector's OTLP/HTTP endpoint, for example `https://gateway.example.com`.

  The URL must use `https` and a hostname, not an IP address. The port, if given, must be 443. The URL must not contain a query string, a fragment, or a username and password. At most 2,048 characters.

  A path prefix, such as `/otlp`, is allowed. Don't include the per-signal path (`/v1/traces`), because the API appends it on delivery. If your collector takes traces on another path, also set `traces.endpoint_url`.

  minLength: 1, maxLength: 2048

- `workspaces: BetaTelemetryDestinationWorkspacesParams`

  Which of the organization's workspaces the destination covers.

  - `BetaTelemetryDestinationWorkspacesAllParams object`

    Cover every workspace of the organization. Doesn't take `workspace_ids`.

    An update that sets `all` empties the destination's workspace list.

    - `type: "all"`

  - `BetaTelemetryDestinationWorkspacesIncludeParams object`

    Cover only the workspaces on the list.

    - `type: "include"`

    - `workspace_ids: optional array of string`

      The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

      On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

      On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

      An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.

  - `BetaTelemetryDestinationWorkspacesExcludeParams object`

    Cover every workspace of the organization except the workspaces on the list.

    - `type: "exclude"`

    - `workspace_ids: optional array of string`

      The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

      On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

      On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

      An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.

- `display_name: optional string or null`

  Human-readable name for the destination. Optional. 1 to 255 characters.

- `headers: optional map[string]`

  Request headers that the API sends with every delivery, typically your collector's authentication header (for example `authorization`).

  The API stores the values encrypted and never returns them. Reads show only `header_names`.

  At most 20 headers. Names are at most 128 characters. Two names can't differ only in case. Values are printable ASCII, at most 4,096 characters, and can't begin or end with a space. Names and values together are at most 16,384 bytes.

  Reserved names are rejected, for example `host`, `cookie`, `user-agent`, and names that start with `content-`, `proxy-`, `x-forwarded-`, or `anthropic-`. For this check, `_` in a name counts as `-`.

- `traces: optional BetaTelemetryDestinationTracesParams`

  The settings for the traces that the destination receives. If you leave it out, every setting takes its default.

  - `content_mode: optional BetaTelemetryDestinationContentMode or null`

    What the exported spans contain. Defaults to `metadata_only` on create.

    On update, `null` sets `metadata_only`.

    - `"metadata_only"`

      The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.

    - `"content"`

      The spans contain the same metadata as `metadata_only`, plus message and tool content.

      An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.

  - `enabled: optional boolean`

    Whether the destination receives traces. Defaults to true on create. It cannot be null.

  - `endpoint_url: optional string or null`

    The full URL of your collector's traces endpoint, for a collector that takes traces on a path other than `/v1/traces`. The API posts traces to it exactly as given and appends nothing.

    The same rules as for `endpoint_url` apply, except that any path is allowed. It must have the same scheme, host, and port as `endpoint_url`. At most 2,048 characters.

    On create, `null` is the same as leaving it out. On update, `null` removes it. The API then posts traces to `endpoint_url` with `/v1/traces` appended. A change of this URL alone keeps the registered headers.

    maxLength: 2048

  - `max_content_bytes: optional number or null`

    The most bytes of content that one exported span can contain, from 1 up to the API's maximum. `null` sets no bound, so only the API's maximum applies.

    On create, leaving it out is the same as `null`. The error for a value above the maximum states the maximum.

    format: int32

## Returns

- `BetaTelemetryDestination object`

  An OpenTelemetry destination: an OTLP/HTTP endpoint, the request headers sent with every delivery to it, what the exported spans contain, and which workspaces it covers. A destination belongs to an organization. A workspace's spans go to every enabled destination that covers it.

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

## Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "endpoint_url": "x",
          "workspaces": {
            "type": "all"
          }
        }'
```

### Response (200)

```json
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
```
