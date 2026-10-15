---
title: Telemetry Destinations
url: https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations
---

# Telemetry Destinations

## Create a Telemetry Destination

**POST** `/v1/organizations/telemetry_destinations`

Register an OpenTelemetry destination for the organization.

The destination starts in state `enabled`. An organization can have at most 10 destinations, including disabled ones.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#add-a-destination) to learn more about adding a destination.

### Headers

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

### Body parameters

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

### Returns

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

### Example

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

#### Response (200)

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

## List Telemetry Destinations

**GET** `/v1/organizations/telemetry_destinations`

List the organization's destinations, newest first, optionally only those that cover given workspaces.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#set-up-api-tracing) to learn more about destinations.

### Query parameters

- `limit: optional number`

  Number of destinations to return per page, between 1 and 1,000. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`. Leave it out to get the first page.

- `workspace_ids: optional array of string`

  Return only the destinations that cover at least one of these workspaces (`wrkspc_...`).

  Send at most 100 IDs, as `workspace_ids[]`. A destination covers a workspace when its `workspaces.type` is `all`, when its `include` list has the workspace, or when its `exclude` list doesn't have it. Destinations in either state can match. An ID that isn't the ID of one of the organization's workspaces doesn't match any destination, not even one whose type is `all`.

### Headers

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

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Retrieve a Telemetry Destination

**GET** `/v1/organizations/telemetry_destinations/{destination_id}`

Read a destination's configuration, state, and most recent delivery results.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-and-health) to learn how the API delivers spans and when it disables a destination.

### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

### Headers

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

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Update a Telemetry Destination

**POST** `/v1/organizations/telemetry_destinations/{destination_id}`

Change a telemetry destination's settings, its state, or which workspaces it covers.

Send at least one field. Omitted fields keep their stored values, except the registered headers, which a change of the endpoint's hostname or port removes. Only `display_name`, `traces`, `traces.endpoint_url`, `traces.content_mode`, `traces.max_content_bytes`, and individual `headers` values accept `null`.

If another request changes the destination while the update runs, the API returns a 409 `conflict_error`. Read the destination again, then retry the update.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-and-health) to learn more about changing a destination.

### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

### Headers

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

### Body parameters

- `display_name: optional string or null`

  New human-readable name, 1 to 255 characters. Null clears it.

- `endpoint_url: optional string`

  The new base URL of the destination's OTLP/HTTP endpoint. The same rules as on create apply.

  A change of hostname or port first removes every registered header, so send the headers for the new endpoint in the same request. When the destination has a `traces.endpoint_url`, such a change must also set `traces.endpoint_url` to a URL with the new hostname and port, or to `null`. A change of the path alone keeps the headers.

  maxLength: 2048

- `headers: optional map[string] or null`

  Headers to set or remove. The API merges them into the destination's headers by name.

  Names compare case-insensitively. A string value sets or replaces that header. A `null` value removes it. Headers that you omit don't change. The field itself can't be `null`.

  A request that sets a header value must also include `endpoint_url`. The current URL is accepted.

  The resulting set must stay within the same limits as on create. When the request sets a value, each stored value that it doesn't set counts as 4,096 bytes toward the 16,384-byte limit, because you can't read its real length. So to change one header of a destination that has four or more other headers, send the values of the others again in the same request.

- `state: optional BetaTelemetryDestinationStateParams`

  Whether the destination receives deliveries after the update. The field can't be `null`.

  - `BetaTelemetryDestinationStateEnabledParams object`

    Start deliveries to the telemetry destination again.

    This doesn't reset `delivery_health`.

    - `type: "enabled"`

  - `BetaTelemetryDestinationStateDisabledParams object`

    Stop deliveries to the telemetry destination.

    Spans produced while it is disabled aren't delivered later. A destination that is already disabled keeps its `reason`.

    - `type: "disabled"`

- `traces: optional BetaTelemetryDestinationTracesParams or null`

  The traces settings to change. Omitted settings keep their stored values.

  `null` sets every traces setting to its create default.

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

- `workspaces: optional BetaTelemetryDestinationWorkspacesParams`

  The new workspace scope, in the same form as on create. The field can't be `null`.

  The API refuses an update that changes the type or sends `workspace_ids` while the destination's list has more than 750 workspaces. Remove workspaces one at a time until 750 or fewer remain, then send the update again.

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

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

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

## Delete a Telemetry Destination

**DELETE** `/v1/organizations/telemetry_destinations/{destination_id}`

Delete a destination and its workspace list.

The API stops sending spans to the destination. The spans of the workspaces it covered still go to the other destinations that cover them. A deleted destination can't be read, listed, or restored.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-and-health) to learn more about managing a destination.

### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

### Headers

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

### Returns

- `BetaDeletedTelemetryDestination object`

  Confirmation that a destination was deleted.

  - `type: "telemetry_destination_deleted"`

  - `id: string`

    ID of the deleted destination (`tdst_...`).

### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "telemetry_destination_deleted"
}
```

## Test a Telemetry Destination

**POST** `/v1/organizations/telemetry_destinations/{destination_id}/test`

Send one test span, named `anthropic.test`, to the destination with its registered headers, once and without retries, and report the destination's answer. The response is 200 whether or not the destination answered with a 2xx status: its `result` has the type `success`, or the type `failure` and the reason in `error`. The destination's configuration, `state` and `delivery_health` do not change. A disabled destination can be tested too. Wait 10 seconds between tests of one destination; a request that comes sooner may be answered with status 429.

### Path parameters

- `destination_id: string`

  ID of the destination to test (starts with `tdst_`).

### Headers

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

### Returns

- `BetaTelemetryDestinationTestResponse object`

  The result of one test span sent to a destination.

  - `type: "telemetry_destination_test"`

  - `result: BetaTelemetryDestinationTestResult`

    How the test went: `success` when the destination answered with a 2xx status, else `failure` with the reason.

    - `BetaTelemetryDestinationTestSuccess object`

      The destination answered the test span with a 2xx status.

      - `type: "success"`

    - `BetaTelemetryDestinationTestFailure object`

      The test span was not delivered.

      - `type: "failure"`

      - `error: string`

        A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/test \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "result": {
    "type": "success"
  },
  "type": "telemetry_destination_test"
}
```

## Domain types

### Beta Deleted Telemetry Destination

- `BetaDeletedTelemetryDestination object`

  Confirmation that a destination was deleted.

  - `type: "telemetry_destination_deleted"`

  - `id: string`

    ID of the deleted destination (`tdst_...`).

### Beta Telemetry Destination

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

### Beta Telemetry Destination Content Mode

- `BetaTelemetryDestinationContentMode = "metadata_only" or "content"`

  What the spans that the API exports to a telemetry destination contain.

  See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-a-content-mode) to learn what the spans contain in each content mode.

  - `"metadata_only"`

    The spans contain identifiers, timing, status, token counts, and similar metadata. They don't contain prompt text, completion text, or tool inputs and outputs.

  - `"content"`

    The spans contain the same metadata as `metadata_only`, plus message and tool content.

    An organization with a data-handling restriction, such as under HIPAA, can't choose this mode. The API exports only metadata for such an organization, even to a destination that already has `content`.

### Beta Telemetry Destination Delivery Health

- `BetaTelemetryDestinationDeliveryHealth object`

  The most recent delivery results that the API records for a telemetry destination.

  Changes to the destination's configuration or state don't reset these fields. Changes to these fields don't change `updated_at`. The values can lag behind the latest deliveries.

  See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-and-health) to learn how the API delivers spans and when it disables a destination.

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

### Beta Telemetry Destination Disabled Reason

- `BetaTelemetryDestinationDisabledReason = BetaTelemetryDestinationDisabledReasonCaller or BetaTelemetryDestinationDisabledReasonSustainedFailure or BetaTelemetryDestinationDisabledReasonInvalidAddress or BetaTelemetryDestinationDisabledReasonRedirect`

  Why the destination is disabled: `caller` when a caller disabled it, or the reason the API disabled it automatically (`sustained_failure`, `invalid_address`, or `redirect`). Every automatic disable is reversible with an update that sets `state` to `enabled`. An update that sets `disabled` on a destination that is already disabled keeps its reason.

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

### Beta Telemetry Destination Disabled Reason Caller

- `BetaTelemetryDestinationDisabledReasonCaller object`

  A caller disabled the destination with an update that set `state` to `disabled`.

  - `type: "caller"`

### Beta Telemetry Destination Disabled Reason Invalid Address

- `BetaTelemetryDestinationDisabledReasonInvalidAddress object`

  The API disabled the destination because deliveries to it failed for longer than the same threshold as for `sustained_failure`, and the most recent failed delivery failed with an invalid address: the DNS answer says that the endpoint's hostname doesn't exist or doesn't have an address, or the address that the API would connect to isn't publicly routable or is reserved, for example a loopback, link-local, private-network, or cloud-metadata address. The API doesn't connect to such an address, and retries the delivery a bounded number of times as it does after a timeout. A timeout or a server failure of the DNS lookup is a temporary DNS failure instead, not an invalid address.

  - `type: "invalid_address"`

### Beta Telemetry Destination Disabled Reason Redirect

- `BetaTelemetryDestinationDisabledReasonRedirect object`

  The API disabled the destination because the endpoint answered a delivery with a 3xx status. Redirects are never followed, and one such answer disables the destination at once.

  - `type: "redirect"`

### Beta Telemetry Destination Disabled Reason Sustained Failure

- `BetaTelemetryDestinationDisabledReasonSustainedFailure object`

  The API disabled the destination because deliveries to it failed, with no successful delivery in between, for longer than a threshold that Anthropic configures and that is not part of this contract. The reason is `invalid_address` instead when the most recent failed delivery failed with an invalid address.

  - `type: "sustained_failure"`

### Beta Telemetry Destination State

- `BetaTelemetryDestinationState = BetaTelemetryDestinationStateEnabled or BetaTelemetryDestinationStateDisabled`

  Whether a telemetry destination receives deliveries.

  A caller can set either state. The API also disables an enabled destination on its own in some cases. The `reason` of the disabled state says whether a caller or the API disabled the destination and, when the API did, why.

  See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#delivery-and-health) to learn when the API disables a destination.

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

### Beta Telemetry Destination State Disabled

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

### Beta Telemetry Destination State Disabled Params

- `BetaTelemetryDestinationStateDisabledParams object`

  Stop deliveries to the telemetry destination.

  Spans produced while it is disabled aren't delivered later. A destination that is already disabled keeps its `reason`.

  - `type: "disabled"`

### Beta Telemetry Destination State Enabled

- `BetaTelemetryDestinationStateEnabled object`

  The telemetry destination receives the spans of the workspaces that it covers.

  - `type: "enabled"`

### Beta Telemetry Destination State Enabled Params

- `BetaTelemetryDestinationStateEnabledParams object`

  Start deliveries to the telemetry destination again.

  This doesn't reset `delivery_health`.

  - `type: "enabled"`

### Beta Telemetry Destination State Params

- `BetaTelemetryDestinationStateParams = BetaTelemetryDestinationStateEnabledParams or BetaTelemetryDestinationStateDisabledParams`

  The state to set on a telemetry destination, by `type` alone.

  A caller can't set the `reason` of a disabled state. Only the API sets it.

  - `BetaTelemetryDestinationStateEnabledParams object`

    Start deliveries to the telemetry destination again.

    This doesn't reset `delivery_health`.

    - `type: "enabled"`

  - `BetaTelemetryDestinationStateDisabledParams object`

    Stop deliveries to the telemetry destination.

    Spans produced while it is disabled aren't delivered later. A destination that is already disabled keeps its `reason`.

    - `type: "disabled"`

### Beta Telemetry Destination Test Failure

- `BetaTelemetryDestinationTestFailure object`

  The test span was not delivered.

  - `type: "failure"`

  - `error: string`

    A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.

### Beta Telemetry Destination Test Response

- `BetaTelemetryDestinationTestResponse object`

  The result of one test span sent to a destination.

  - `type: "telemetry_destination_test"`

  - `result: BetaTelemetryDestinationTestResult`

    How the test went: `success` when the destination answered with a 2xx status, else `failure` with the reason.

    - `BetaTelemetryDestinationTestSuccess object`

      The destination answered the test span with a 2xx status.

      - `type: "success"`

    - `BetaTelemetryDestinationTestFailure object`

      The test span was not delivered.

      - `type: "failure"`

      - `error: string`

        A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.

### Beta Telemetry Destination Test Result

- `BetaTelemetryDestinationTestResult = BetaTelemetryDestinationTestSuccess or BetaTelemetryDestinationTestFailure`

  The outcome of a test: `success`, or `failure` with the reason.

  - `BetaTelemetryDestinationTestSuccess object`

    The destination answered the test span with a 2xx status.

    - `type: "success"`

  - `BetaTelemetryDestinationTestFailure object`

    The test span was not delivered.

    - `type: "failure"`

    - `error: string`

      A message that describes why the test span was not delivered, including the HTTP status code when the destination returned one. Examples: `HTTP error (status 403)`, `timeout`, `TLS failure`. It has the same form as the destination's `delivery_health.last_error` and never contains the destination's response body, any header value, a network address, or TLS details.

### Beta Telemetry Destination Test Success

- `BetaTelemetryDestinationTestSuccess object`

  The destination answered the test span with a 2xx status.

  - `type: "success"`

### Beta Telemetry Destination Traces

- `BetaTelemetryDestinationTraces object`

  A telemetry destination's settings for the traces it receives.

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

### Beta Telemetry Destination Traces Params

- `BetaTelemetryDestinationTracesParams object`

  The settings for the traces that a telemetry destination receives, as a create or update request sets them. An omitted field takes its default on create and keeps its stored value on update.

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

### Beta Telemetry Destination Workspaces

- `BetaTelemetryDestinationWorkspaces = BetaTelemetryDestinationWorkspacesAll or BetaTelemetryDestinationWorkspacesInclude or BetaTelemetryDestinationWorkspacesExclude`

  Which of the organization's workspaces a telemetry destination covers.

  Several destinations can cover the same workspace. Each of them receives the workspace's spans while it is enabled.

  The workspace list of an `include` or `exclude` destination isn't part of the destination object. List the destination's workspaces to read it. Add or remove one workspace at a time, or replace the whole list with an update. A list holds at most 1,000 workspaces.

  - `BetaTelemetryDestinationWorkspacesAll object`

    The destination covers every workspace of the organization, including the default workspace, archived workspaces, and workspaces created later. It doesn't have a list.

    - `type: "all"`

  - `BetaTelemetryDestinationWorkspacesInclude object`

    The destination covers the workspaces on its list, and no others.

    - `type: "include"`

  - `BetaTelemetryDestinationWorkspacesExclude object`

    The destination covers every workspace of the organization except the workspaces on its list. A workspace created later is covered until it is added to the list.

    - `type: "exclude"`

### Beta Telemetry Destination Workspaces All

- `BetaTelemetryDestinationWorkspacesAll object`

  The destination covers every workspace of the organization, including the default workspace, archived workspaces, and workspaces created later. It doesn't have a list.

  - `type: "all"`

### Beta Telemetry Destination Workspaces All Params

- `BetaTelemetryDestinationWorkspacesAllParams object`

  Cover every workspace of the organization. Doesn't take `workspace_ids`.

  An update that sets `all` empties the destination's workspace list.

  - `type: "all"`

### Beta Telemetry Destination Workspaces Exclude

- `BetaTelemetryDestinationWorkspacesExclude object`

  The destination covers every workspace of the organization except the workspaces on its list. A workspace created later is covered until it is added to the list.

  - `type: "exclude"`

### Beta Telemetry Destination Workspaces Exclude Params

- `BetaTelemetryDestinationWorkspacesExcludeParams object`

  Cover every workspace of the organization except the workspaces on the list.

  - `type: "exclude"`

  - `workspace_ids: optional array of string`

    The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

    On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

    On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

    An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.

### Beta Telemetry Destination Workspaces Include

- `BetaTelemetryDestinationWorkspacesInclude object`

  The destination covers the workspaces on its list, and no others.

  - `type: "include"`

### Beta Telemetry Destination Workspaces Include Params

- `BetaTelemetryDestinationWorkspacesIncludeParams object`

  Cover only the workspaces on the list.

  - `type: "include"`

  - `workspace_ids: optional array of string`

    The IDs of the workspaces on the destination's list (`wrkspc_...`). At most 100 per request.

    On create, these workspaces become the destination's list. If you leave `workspace_ids` out, the list starts empty. If the API refuses one of the IDs, it doesn't create the destination.

    On update, `workspace_ids` replaces the whole list. A workspace that stays on the list keeps its entry and its `created_at`. An empty array empties the list. If you leave `workspace_ids` out and the type stays the same, the list doesn't change. If you leave it out and the type changes, the new list starts empty. After a change to `include` without `workspace_ids`, the destination doesn't cover any workspace until one is added. After a change to `exclude` without `workspace_ids`, it covers every workspace.

    An ID sent more than once is added once. An archived workspace can't be added to a list. An update can keep an archived workspace that is already on the list.

### Beta Telemetry Destination Workspaces Params

- `BetaTelemetryDestinationWorkspacesParams = BetaTelemetryDestinationWorkspacesAllParams or BetaTelemetryDestinationWorkspacesIncludeParams or BetaTelemetryDestinationWorkspacesExcludeParams`

  Which of the organization's workspaces a telemetry destination covers, as a create or update request sets it.

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

## Telemetry Destinations › Workspaces

### List Telemetry Destination Workspaces

**GET** `/v1/organizations/telemetry_destinations/{destination_id}/workspaces`

List the workspaces on a destination's workspace list, newest entry first.

A destination whose `workspaces.type` is `all` doesn't have a list, so its page is empty. The list includes archived workspaces.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-workspaces-for-a-destination) to learn more about choosing the workspaces of a destination.

#### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

#### Query parameters

- `limit: optional number`

  Number of entries to return per page, between 1 and 1,000. Defaults to 20.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's `next_page`. Leave it out to get the first page.

#### Headers

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

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

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

### Add a Telemetry Destination Workspace

**POST** `/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}`

Add one workspace to a destination's workspace list.

Under `include` the workspace's spans start going to the destination. Under `exclude` they stop. A list holds at most 1,000 workspaces.

Adding a workspace that is already on the list changes nothing and returns the existing entry. An archived workspace that isn't on the list yet can't be added. A destination whose `workspaces.type` is `all` doesn't have a list, so the API returns 400. To change which workspaces such a destination covers, update its `workspaces`.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-workspaces-for-a-destination) to learn more about choosing the workspaces of a destination.

#### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

- `workspace_id: string`

  ID of the workspace to add (`wrkspc_...`).

#### Headers

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

#### Returns

- `BetaTelemetryDestinationWorkspace object`

  A workspace on a telemetry destination's workspace list.

  Under `include`, the destination covers the workspace. Under `exclude`, the destination covers every workspace except this one. The entry doesn't have an `id`. Its `telemetry_destination_id` and `workspace_id` together identify it.

  - `type: "telemetry_destination_workspace"`

  - `created_at: string`

    Time the workspace was added to the list.

    format: date-time

  - `telemetry_destination_id: string`

    ID of the telemetry destination (`tdst_...`).

  - `workspace_id: string`

    ID of the workspace (`wrkspc_...`).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/workspaces/$WORKSPACE_ID \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "created_at": "2019-12-27T18:11:19.117Z",
  "telemetry_destination_id": "telemetry_destination_id",
  "type": "telemetry_destination_workspace",
  "workspace_id": "workspace_id"
}
```

### Remove a Telemetry Destination Workspace

**DELETE** `/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}`

Remove one workspace from a destination's workspace list.

Under `include` the workspace's spans stop going to the destination. Under `exclude` they start. An archived workspace can be removed too.

The API returns 404 when the workspace isn't on the list. A destination whose `workspaces.type` is `all` doesn't have a list, so the API returns 400.

See the [OpenTelemetry export guide](https://platform.claude.com/docs/en/manage-claude/opentelemetry?sdk_languages=http#choose-workspaces-for-a-destination) to learn more about choosing the workspaces of a destination.

#### Path parameters

- `destination_id: string`

  ID of the destination (`tdst_...`).

- `workspace_id: string`

  ID of the workspace to remove (`wrkspc_...`).

#### Headers

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

#### Returns

- `BetaDeletedTelemetryDestinationWorkspace object`

  Confirmation that a workspace was removed from a destination's list.

  - `type: "telemetry_destination_workspace_deleted"`

  - `telemetry_destination_id: string`

    ID of the telemetry destination (`tdst_...`).

  - `workspace_id: string`

    ID of the workspace that was removed (`wrkspc_...`).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/telemetry_destinations/$DESTINATION_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: telemetry-destinations-2026-08-11' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "telemetry_destination_id": "telemetry_destination_id",
  "type": "telemetry_destination_workspace_deleted",
  "workspace_id": "workspace_id"
}
```
