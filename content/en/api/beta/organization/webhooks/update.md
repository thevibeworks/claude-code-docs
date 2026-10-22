---
title: Update Organization Webhook Endpoint
url: https://platform.claude.com/docs/en/api/beta/organization/webhooks/update
---

# Update Organization Webhook Endpoint

**POST** `/v1/organizations/webhooks/{webhook_endpoint_id}`

Update an organization webhook endpoint. Only the fields you send are changed.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

## Path parameters

- `webhook_endpoint_id: string`

  ID of the webhook endpoint.

  maxLength: 2048

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `webhooks-2026-10-07` in this header.

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

## Body parameters

- `description: optional string`

  Notes about the endpoint.

- `enabled_events: optional array of "user_profile.enforcement_action_opened" or "user_profile.enforcement_action_resolved"`

  The event types to deliver to the endpoint. Replaces the whole set; an empty list leaves it unchanged.

  - `"user_profile.enforcement_action_opened"`

  - `"user_profile.enforcement_action_resolved"`

- `name: optional string`

  A short label for the endpoint.

- `state: optional "disabled" or "enabled"`

  `disabled` stops deliveries. `enabled` resumes them and clears `disabled_reason`. Events that happen while the endpoint is disabled are never delivered.

  - `"disabled"`

  - `"enabled"`

- `url: optional string`

  The HTTPS URL that deliveries are sent to.

  minLength: 1

## Returns

- `BetaOrganizationWebhookEndpoint object`

  A webhook endpoint that belongs to the organization rather than to one of
  its workspaces.

  - `id: string`

    ID of the webhook endpoint.

  - `created_at: string`

    When the endpoint was created, in RFC 3339 format.

    format: date-time

  - `description: string`

    Notes about the endpoint. An empty string when none were given.

  - `disabled_reason: string`

    Why Anthropic disabled the endpoint automatically. An empty string when the endpoint is enabled, or when you disabled it.

  - `enabled_events: array of "user_profile.enforcement_action_opened" or "user_profile.enforcement_action_resolved"`

    The event types delivered to the endpoint.

    - `"user_profile.enforcement_action_opened"`

    - `"user_profile.enforcement_action_resolved"`

  - `name: string`

    A short label for the endpoint. An empty string when none was given.

  - `state: BetaOrganizationWebhookEndpointState`

    Whether deliveries are sent to the endpoint.

    - `"disabled"`

    - `"enabled"`

  - `updated_at: string`

    When the endpoint was last changed, in RFC 3339 format.

    format: date-time

  - `url: string`

    The HTTPS URL that deliveries are sent to.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks/$WEBHOOK_ENDPOINT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "disabled_reason": "disabled_reason",
  "enabled_events": [
    "user_profile.enforcement_action_opened"
  ],
  "name": "name",
  "state": "disabled",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "url": "url"
}
```
