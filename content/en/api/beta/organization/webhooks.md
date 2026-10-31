---
title: Webhooks
url: https://platform.claude.com/docs/en/api/beta/organization/webhooks
---

# Webhooks

## Create Organization Webhook Endpoint

**POST** `/v1/organizations/webhooks`

Create an organization webhook endpoint.

An organization webhook endpoint belongs to the organization rather than to one of its workspaces. An organization can have at most 32 organization
webhook endpoints, enabled or disabled.

The response includes the endpoint's signing secret. No read returns it, so store
it when you receive it.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Body parameters

- `enabled_events: array of "user_profile.enforcement_action_opened" or "user_profile.enforcement_action_resolved"`

  The event types to deliver to the endpoint. Must list at least one.

  - `"user_profile.enforcement_action_opened"`

  - `"user_profile.enforcement_action_resolved"`

- `url: string`

  The HTTPS URL that deliveries are sent to.

  minLength: 1

- `description: optional string`

  Notes about the endpoint.

- `name: optional string`

  A short label for the endpoint.

### Returns

- `BetaNewOrganizationWebhookEndpoint object`

  A new organization webhook endpoint, with its signing secret.

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

  - `signing_secret: string`

    The secret Anthropic signs deliveries to the endpoint with (prefix `whsec_`). No other response returns it, so store it now. To replace it, regenerate the signing secret.

  - `state: BetaOrganizationWebhookEndpointState`

    Whether deliveries are sent to the endpoint.

    - `"disabled"`

    - `"enabled"`

  - `updated_at: string`

    When the endpoint was last changed, in RFC 3339 format.

    format: date-time

  - `url: string`

    The HTTPS URL that deliveries are sent to.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "enabled_events": [
            "user_profile.enforcement_action_opened"
          ],
          "url": "x"
        }'
```

#### Response (200)

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
  "signing_secret": "signing_secret",
  "state": "disabled",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "url": "url"
}
```

## List Organization Webhook Endpoints

**GET** `/v1/organizations/webhooks`

List the organization's webhook endpoints.

An organization webhook endpoint belongs to the organization rather than to one of its workspaces. The list does not include webhook endpoints that
belong to a workspace.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of a webhook endpoint to use as a cursor. Returns the first `limit` endpoints that come before it in list order, not the `limit` endpoints just before it.

- `limit: optional number`

  Number of items to return per page, up to `100`. The default, `0`, means `20`.

  default: 0, minimum: 0, maximum: 100

- `order: optional "asc" or "desc"`

  Sort order by `created_at`. Defaults to `desc`, newest first.

  - `"asc"`

  - `"desc"`

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Returns

- `data: array of BetaOrganizationWebhookEndpoint`

  The organization webhook endpoints on this page.

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

- `has_more: boolean`

  Whether more endpoints follow this page in list order. With `before_id`, only endpoints before the cursor count.

- `first_id: optional string or null`

  First ID in the `data` list.

- `last_id: optional string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
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
  ],
  "has_more": true,
  "first_id": "first_id",
  "last_id": "last_id"
}
```

## Get Organization Webhook Endpoint

**GET** `/v1/organizations/webhooks/{webhook_endpoint_id}`

Retrieve an organization webhook endpoint by ID.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Path parameters

- `webhook_endpoint_id: string`

  ID of the webhook endpoint.

  maxLength: 2048

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks/$WEBHOOK_ENDPOINT_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Update Organization Webhook Endpoint

**POST** `/v1/organizations/webhooks/{webhook_endpoint_id}`

Update an organization webhook endpoint. Only the fields you send are changed.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Path parameters

- `webhook_endpoint_id: string`

  ID of the webhook endpoint.

  maxLength: 2048

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Body parameters

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

### Returns

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

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks/$WEBHOOK_ENDPOINT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

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

## Delete Organization Webhook Endpoint

**DELETE** `/v1/organizations/webhooks/{webhook_endpoint_id}`

Delete an organization webhook endpoint.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Path parameters

- `webhook_endpoint_id: string`

  ID of the webhook endpoint.

  maxLength: 2048

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Returns

- `BetaDeletedOrganizationWebhookEndpoint object`

  A deleted organization webhook endpoint.

  - `type: "webhook_endpoint_deleted"`

    Always `webhook_endpoint_deleted`.

    default: webhook_endpoint_deleted

  - `id: string`

    ID of the deleted webhook endpoint.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks/$WEBHOOK_ENDPOINT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "webhook_endpoint_deleted"
}
```

## Regenerate Organization Webhook Endpoint Signing Secret

**POST** `/v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret`

Replace an organization webhook endpoint's signing secret. The old secret stops
working immediately. The new secret is returned only in this response.

Every request must include the beta header `anthropic-beta: webhooks-2026-10-07`. A request without it returns `404`, exactly as if this API did not exist. Anthropic turns organization webhook endpoints on for each organization; until yours is on, requests also return `404`. Organization webhook endpoints are in beta and are not available to organizations with HIPAA readiness enabled.

### Path parameters

- `webhook_endpoint_id: string`

  ID of the webhook endpoint.

  maxLength: 2048

### Headers

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

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Returns

- `BetaOrganizationWebhookEndpointSigningSecret object`

  An organization webhook endpoint's new signing secret.

  - `signing_secret: string`

    The new signing secret. Deliveries are signed with it from now on, and no other response returns it.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/webhooks/$WEBHOOK_ENDPOINT_ID/regenerate_signing_secret \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: webhooks-2026-10-07' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "signing_secret": "signing_secret"
}
```

## Domain types

### Beta Deleted Organization Webhook Endpoint

- `BetaDeletedOrganizationWebhookEndpoint object`

  A deleted organization webhook endpoint.

  - `type: "webhook_endpoint_deleted"`

    Always `webhook_endpoint_deleted`.

    default: webhook_endpoint_deleted

  - `id: string`

    ID of the deleted webhook endpoint.

### Beta New Organization Webhook Endpoint

- `BetaNewOrganizationWebhookEndpoint object`

  A new organization webhook endpoint, with its signing secret.

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

  - `signing_secret: string`

    The secret Anthropic signs deliveries to the endpoint with (prefix `whsec_`). No other response returns it, so store it now. To replace it, regenerate the signing secret.

  - `state: BetaOrganizationWebhookEndpointState`

    Whether deliveries are sent to the endpoint.

    - `"disabled"`

    - `"enabled"`

  - `updated_at: string`

    When the endpoint was last changed, in RFC 3339 format.

    format: date-time

  - `url: string`

    The HTTPS URL that deliveries are sent to.

### Beta Organization Webhook Endpoint

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

### Beta Organization Webhook Endpoint Signing Secret

- `BetaOrganizationWebhookEndpointSigningSecret object`

  An organization webhook endpoint's new signing secret.

  - `signing_secret: string`

    The new signing secret. Deliveries are signed with it from now on, and no other response returns it.

### Beta Organization Webhook Endpoint State

- `BetaOrganizationWebhookEndpointState = "disabled" or "enabled"`

  Whether deliveries are sent to an organization webhook endpoint.

  - `"disabled"`

  - `"enabled"`
