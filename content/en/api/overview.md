---
title: API overview
url: https://platform.claude.com/docs/en/api/overview
description: Understand the Claude API's available endpoints, authentication headers, client SDKs, pagination, rate limits, and cloud platform access options.
---

The Claude API is a RESTful API at `https://api.anthropic.com` that provides programmatic access to Claude models and Claude Managed Agents.

<Note>
  **New to Claude?** For direct model access, start with [Get started](https://platform.claude.com/docs/en/get-started) and [Working with Messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages). For managed agent infrastructure, see the [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).
</Note>

## Prerequisites

To use the Claude API, you'll need:

* A [Claude Console account](https://platform.claude.com)
* An [API key](https://platform.claude.com/settings/keys), or a configured [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rule

For step-by-step setup instructions, see [Get started](https://platform.claude.com/docs/en/get-started).

## Available APIs

The Claude API includes the following APIs:

**General Availability:**

* **[Messages API](https://platform.claude.com/docs/en/api/messages/create)**: Send messages to Claude for conversational interactions (`POST /v1/messages`)
* **[Message Batches API](https://platform.claude.com/docs/en/api/messages/batches/create)**: Process large volumes of Messages requests asynchronously with 50% cost reduction (`POST /v1/messages/batches`)
* **[Token Counting API](https://platform.claude.com/docs/en/api/messages-count-tokens)**: Count tokens in a message before sending to manage costs and rate limits (`POST /v1/messages/count_tokens`)
* **[Models API](https://platform.claude.com/docs/en/api/models/list)**: List available Claude models and their details (`GET /v1/models`)
* **[Files API](https://platform.claude.com/docs/en/api/beta/files/upload)**: Upload and manage files for use across multiple API calls (`POST /v1/files`, `GET /v1/files`)
* **[Skills API](https://platform.claude.com/docs/en/api/skills/create-skill)**: Create and manage custom agent skills (`POST /v1/skills`, `GET /v1/skills`)

**Beta:**

* **[Agents API](https://platform.claude.com/docs/en/managed-agents/agent-setup)**: Define reusable, versioned agent configurations for Claude Managed Agents (`POST /v1/agents`, `GET /v1/agents`)
* **[Sessions API](https://platform.claude.com/docs/en/managed-agents/sessions)**: Run stateful agent sessions in managed cloud sandboxes (`POST /v1/sessions`, `GET /v1/sessions/{id}/events/stream`)
* **[Environments API](https://platform.claude.com/docs/en/managed-agents/environments)**: Configure sandbox templates for agent sessions (`POST /v1/environments`, `GET /v1/environments`)

For the complete API reference with all endpoints, parameters, and response schemas, explore the API reference pages listed in the navigation. To access beta features, see [Beta headers](https://platform.claude.com/docs/en/api/beta-headers).

## Authentication

For details on both authentication methods and when to use each, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication). All requests to the Claude API must include these headers:

| Header              | Value                                                                                                                                                                                                                       | Required                              |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `x-api-key`         | Your API key from Console                                                                                                                                                                                                   | One of `x-api-key` or `Authorization` |
| `Authorization`     | `Bearer <token>`, where `<token>` is a short-lived access token obtained from `POST /v1/oauth/token` through [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) | One of `x-api-key` or `Authorization` |
| `anthropic-version` | API version (for example, `2023-06-01`)                                                                                                                                                                                     | Yes                                   |
| `content-type`      | `application/json`                                                                                                                                                                                                          | Yes                                   |

If you are using the [Client SDKs](https://platform.claude.com/docs/en/api/overview#client-sdks), the SDK will send these headers automatically. For API versioning details, see [API versions](https://platform.claude.com/docs/en/api/versioning).

When accessing Claude through a [cloud platform](https://platform.claude.com/docs/en/api/overview#claude-api-vs-cloud-platforms), authentication is integrated with the cloud provider's IAM system. See the platform-specific documentation for supported credential types, required headers, and authentication options.

### Getting API keys

The API is made available through the web [Console](https://platform.claude.com/). You can use [Playground](https://platform.claude.com/playground) to try out the API in the browser and then generate API keys in [Account Settings](https://platform.claude.com/settings/keys). You choose each key's [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration) when you create it. Use [workspaces](https://platform.claude.com/settings/workspaces) to segment your API keys and [control spend](https://platform.claude.com/docs/en/api/rate-limits) by use case.

## Client SDKs

Anthropic provides official SDKs that simplify API integration by handling authentication, request formatting, error handling, and more.

**Benefits:**

* Automatic header management (`x-api-key`, `anthropic-version`, `content-type`)
* Type-safe request and response handling
* Built-in retry logic and error handling
* Streaming support
* Request timeouts and connection management

For a list of client SDKs, see [Client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).

## Claude API vs cloud platforms

Claude is available through the direct Claude API and through cloud platforms. Choose based on your infrastructure, feature availability, compliance requirements, and pricing preferences.

### Claude API

* **Direct access** to the latest models and features
* **Anthropic billing and support**
* **Best for:** New integrations, full feature access, direct relationship with Anthropic

### Cloud platform APIs

Access Claude through AWS, Google Cloud, or Microsoft Azure:

* **Integrated** with cloud provider billing and IAM
* **Feature availability varies by platform:** Anthropic-operated platforms include [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry); partner-operated platforms include Amazon Bedrock and Google Cloud. See each platform's page for feature availability and timing.
* **Best for:** Existing cloud commitments, specific compliance requirements, consolidated cloud billing

| Platform               | Provider                             | Documentation                                                                                                    |
| ---------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Agent Platform         | Google Cloud                         | [Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)              |
| Amazon Bedrock         | AWS                                  | [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)       |
| Claude Platform on AWS | AWS (Anthropic-operated)             | [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)           |
| Microsoft Foundry      | Microsoft Azure (Anthropic-operated) | [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) |

<Note>
  Claude Managed Agents is available through the direct Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws). For feature availability across platforms, see the [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview).
</Note>

## Request and response format

### Request size limits

| Endpoint                                                                                      | Maximum request size |
| --------------------------------------------------------------------------------------------- | -------------------- |
| Messages, Token Counting                                                                      | 32 MB                |
| [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) | 256 MB               |
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)                      | 500 MB               |
| Sessions, Agents, Environments                                                                | 32 MB                |

If you exceed these limits, you'll receive a 413 `request_too_large` error.

<Note>
  Partner-operated platforms have their own request size limits: Bedrock limits requests to 20 MB, and Google Cloud limits requests to 30 MB. Claude Platform on AWS uses the same limits as the direct Claude API. Consult your platform's documentation for current values.
</Note>

### Response headers

The Claude API includes the following headers in its responses:

| Header                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request-id`                | A globally unique identifier for the request, such as `req_018EeWyXxfu5pfWkrYcMdjWG`. Include it when you contact support about a specific request. See [Request ID](https://platform.claude.com/docs/en/api/errors#request-id).                                                                                                                                                                                                                                                                                                                                                        |
| `anthropic-organization-id` | The ID of the organization that the API key or access token used in the request belongs to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `anthropic-workspace-id`    | The `wrkspc_`-prefixed ID of the [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) that the API key or access token resolved to, such as `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`, including when that is your organization's Default Workspace. Absent when the credential doesn't resolve to a workspace (for example, on Admin API requests) or the request fails before authentication completes. See [Identify the workspace behind an API response](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response). |

For the rate limit headers, see [Response headers](https://platform.claude.com/docs/en/api/rate-limits#response-headers) in Rate limits. For examples that read a response header by name with each SDK, see [Identify the workspace behind an API response](https://platform.claude.com/docs/en/manage-claude/workspaces#identify-the-workspace-behind-an-api-response).

<Note>
  Claude Platform on AWS adds an AWS request ID (`x-amzn-requestid`) alongside the standard `request-id` header. See [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids) for the dual-ID handling pattern.
</Note>

## Pagination

List endpoints return results in pages. Most newer list endpoints use the `page` and `next_page` cursor scheme described in this section. Some use a different scheme; see the note at the end of this section. Use the `limit` query parameter to control the page size and the `page` query parameter to fetch an adjacent page. Each response includes a `data` array alongside cursor fields for navigating between pages.

| Name        | Location        | Description                                                                                                                                                                             |
| ----------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`     | Query parameter | Maximum number of items to return per page.                                                                                                                                             |
| `page`      | Query parameter | Opaque cursor from a previous response. Pass a `next_page` or `prev_page` value here to fetch the adjacent page.                                                                        |
| `order`     | Query parameter | Sort direction for the results (`asc` or `desc`), on list endpoints that support sorting. A `page` cursor is only valid with the `order` it was created with.                           |
| `next_page` | Response field  | Cursor for the next page, or `null` if there are no more results.                                                                                                                       |
| `prev_page` | Response field  | Cursor for the previous page on endpoints that support backward pagination (currently `GET /v1/sessions`), or `null` if you are on the first page. Other list endpoints omit the field. |

To go back a page, pass `prev_page` as the `page` parameter. `prev_page` is `null` when you're on the first page. Not all list endpoints support `prev_page`. Only `GET /v1/sessions` returns `prev_page`; on list endpoints that do not support backward pagination, the field is absent from the response rather than `null`. For a request walkthrough, see [Listing sessions](https://platform.claude.com/docs/en/managed-agents/session-operations#listing-sessions).

Every SDK provides an auto-paginating iterator that follows `next_page` for you. In Python and TypeScript, you get it by iterating the list result directly. The other SDKs provide the iterator through a separate method. SDK auto-pagination is forward-only; to go back a page, read `prev_page` from the response and pass it back as the `page` parameter yourself. See [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) for language-specific details.

<Note>
  Some list endpoints use a different cursor scheme. The [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing), the [Models API](https://platform.claude.com/docs/en/api/models/list), and several [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) endpoints take `after_id` and `before_id` query parameters instead of `page`. Their responses return `has_more`, `first_id`, and `last_id` instead of `next_page`. The [Files API](https://platform.claude.com/docs/en/build-with-claude/files) also uses that scheme when a request includes the `files-api-2025-04-14` beta header; without the header, `GET /v1/files` takes `page` and returns `next_page`. Some endpoints that use the `page` scheme, such as `GET /v1/skills`, also return a `has_more` Boolean alongside `next_page`. See the reference page for each endpoint for its exact pagination fields.
</Note>

## Rate limits and availability

### Rate limits

The API enforces rate limits and spend limits to prevent misuse and manage capacity. Limits are organized into usage tiers; your organization is placed on a tier automatically and can move to a higher tier over time. Each tier has:

* **Spend limits**: Maximum monthly cost for API usage
* **Rate limits**: Maximum number of requests per minute (RPM) and tokens per minute (TPM)

You can view your rate limits on the [Rate limits](https://platform.claude.com/settings/limits) page and your spend limits on the [Billing](https://platform.claude.com/settings/billing) page in the Console. For higher rate limits or a higher monthly spend cap, use **Request rate limit increase** on the Rate limits page.

For detailed information about limits, tiers, and the token bucket algorithm used for rate limiting, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits).

### Availability

The Claude API is available in [many countries and regions](https://platform.claude.com/docs/en/api/supported-regions) worldwide. Check the supported regions page to confirm availability in your location.

## Next steps

<CardGroup cols={2}>
  <Card title="Messages API reference" icon="book" href="https://platform.claude.com/docs/en/api/messages/create">
    Complete API specification for direct model interactions
  </Card>

  <Card title="Claude Managed Agents reference" icon="brain" href="https://platform.claude.com/docs/en/managed-agents/sessions">
    Agents, Sessions, and Environments endpoints
  </Card>

  <Card title="Client SDKs" icon="code" href="https://platform.claude.com/docs/en/cli-sdks-libraries/overview">
    Python, TypeScript, C#, Go, Java, PHP, and Ruby
  </Card>

  <Card title="Rate limits" icon="gauge" href="https://platform.claude.com/docs/en/api/rate-limits">
    Usage tiers, requesting higher limits, and the token bucket algorithm
  </Card>
</CardGroup>
