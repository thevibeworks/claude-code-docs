---
title: Organization webhooks
url: https://platform.claude.com/docs/en/manage-claude/organization-webhooks
description: Register webhook endpoints for events about your organization's user profiles, customer-managed encryption keys, and customer-owned storage, and respond to each event.
featureMetadata:
  status: beta
  betaHeader: webhooks-2026-10-07
  supportedPlatforms:
    Claude API: beta
---

An organization webhook endpoint is a URL where Anthropic sends events about your organization, such as an encryption key that stops working. Use this page to choose the events you need, register an endpoint, respond to each event, and catch up when an event doesn’t arrive. You manage endpoints with the Admin API under `/v1/organizations/webhooks`, or [in the Claude Console](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#manage-endpoints) for some event types.

<Note>
  Delivery of the two [user profile events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#user-profile-events) isn’t live: Anthropic doesn’t send them. You can register endpoints for them and build your handler from the event format on this page.
</Note>

## Before you start

You need the following:

* An organization on the Claude API that has organization webhooks turned on. Without them, [requests return a `404`](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#errors). The first case that fits your organization applies:

  * It has [HIPAA readiness](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness) enabled: it can’t use organization webhooks.
  * It can use [customer-managed encryption keys](https://platform.claude.com/docs/en/manage-claude/cmek): it has organization webhooks.
  * Any other organization, including one that has only [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage): contact your Anthropic account team to request access.

* One of these credentials:

  * An [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys).
  * An [OAuth bearer token](https://platform.claude.com/docs/en/manage-claude/admin-api#oauth-bearer-token) with the `org:admin` scope.
  * A [personal or service account key](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) that isn’t scoped to a workspace.

With an Admin API key, you can make every request in [Manage endpoints](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#manage-endpoints). With an `org:admin` token, you can make the same requests. If the token is bound to a workspace other than your organization’s [Default Workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work), you can’t make any of them. With a personal or service account key, the requests you can make depend on the account’s [organization role](https://platform.claude.com/docs/en/manage-claude/admin-api#organization-roles-and-permissions):

* To list or get webhook endpoints: `developer` or `admin`
* To create, update, or delete webhook endpoints, or to replace a signing secret: `admin`

## Event types

An endpoint receives the event types that you list in its [`enabled_events`](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#endpoint-fields) when you [create or update it](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#manage-endpoints). This page covers these groups of event types:

* [User profile events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#user-profile-events): Anthropic restricts or bans one of your [user profiles](https://platform.claude.com/docs/en/manage-claude/user-profiles), or the restriction or ban ends.
* [Encryption key events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#encryption-key-events): your key management service (KMS) keeps refusing one of your customer-managed encryption keys, or the key works again.
* [Customer-owned storage events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#customer-owned-storage-events): one of your buckets fails Anthropic’s daily check, or passes it again.

For other event types, see `enabled_events` in the [API reference for creating an endpoint](https://platform.claude.com/docs/en/api/beta/organization/webhooks/create).

## User profile events

The following event types are about [enforcement actions](https://platform.claude.com/docs/en/manage-claude/user-profiles#check-whether-anthropic-has-restricted-or-banned-a-profile) on user profiles. Anthropic doesn’t send them.

| Event | Trigger |
| ----- | ----- |
| `user_profile.enforcement_action_opened` | Anthropic opens an enforcement action on a user profile. |
| `user_profile.enforcement_action_resolved` | An enforcement action ends. Anthropic resolves it, or its `expires_at` time passes. |

Deleting a profile ends its open actions without a `user_profile.enforcement_action_resolved` event.

### Before your first event

In any request whose `anthropic-beta` header has `user-profiles-2026-09-04` or an earlier user profiles beta, responses leave out the `enforcement_status` and `enforcement_actions` fields. In such a request, the `enforcement_status[]` list filter returns a `400`. To get the fields, remove that beta from your requests.

If an enforcement action opened before Anthropic turned on event delivery for your organization, or before you registered your endpoint, you don’t get a `user_profile.enforcement_action_opened` event for it. The action still appears on the profile. To find these actions, [list your profiles](https://platform.claude.com/docs/en/api/user_profiles/list) with `enforcement_status[]=restricted` and `enforcement_status[]=banned`. A response might return fewer profiles than `limit`, or none, before the list ends, so keep requesting pages until `next_page` is `null`.

### What an event contains

User profile events carry IDs, not the action or the profile. `data.id` is the profile’s ID, and `data.enforcement_action_id` is the action’s ID, which starts with `enac_`:

```json
{
  "type": "event",
  "id": "whe_4f2a9c1e7b3d5a8f0e6c2b9d1a7f3e5c",
  "created_at": "2026-10-15T17:02:41Z",
  "data": {
    "type": "user_profile.enforcement_action_opened",
    "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    "enforcement_action_id": "enac_011CZkZEq4TnWb7xLfRgPm2v",
    "organization_id": "org_011CZkZBj9RsYd3wNcHvKq6t"
  }
}
```

To see what changed, [retrieve the profile](https://platform.claude.com/docs/en/api/user_profiles/retrieve) with `GET /v1/user_profiles/{id}` (python, ruby: `client.user_profiles.retrieve()`; typescript: `client.userProfiles.retrieve()`; go: `client.UserProfiles.Get()`; java: `client.userProfiles().retrieve()`; csharp: `client.UserProfiles.Retrieve()`; php: `$client->userProfiles->retrieve()`; cli: `ant user-profiles retrieve`), using `data.id`. Its `enforcement_actions` list shows its open actions. Each action has a `type` (`restriction` or `ban`), an `id`, a `reason`, an `opened_at` time, and an `expires_at` time or `null`. `enforcement_status` summarizes them: `banned` while a ban is open, `restricted` while any other action is open, and `unrestricted` when none is. Treat any other value as `restricted`.

Anthropic sends an event only after the profile shows the change, so the profile you retrieve shows that change or a later one. Events might arrive late or out of order, so use the profile’s current state, not the order events arrive in. After `user_profile.enforcement_action_resolved`, the resolved action is no longer in the list. A `404` means the profile was deleted.

## Encryption key events

These events are about your organization’s [customer-managed encryption keys](https://platform.claude.com/docs/en/manage-claude/cmek) (CMEK). The Admin API calls such a key an external key, so the event types start with `external_key`:

| Event | Trigger |
| ----- | ----- |
| `external_key.failed` | Your KMS keeps refusing Anthropic’s use of a key, for example because someone disabled the key or removed Anthropic’s access to it. |
| `external_key.recovered` | After Anthropic sends `external_key.failed`, the key works again when Anthropic uses it. |

Only a real refusal starts these events. There’s no test event.

When a key fails or recovers, Anthropic usually also emails the members of your organization who can manage encryption keys. The failure email names workspaces that your KMS recently refused, but it might not list all of them.

The event names the key in `data.id`, which starts with `ekey_`:

```json
{
  "type": "event",
  "id": "whe_8c1d5e2a9f4b7036d1e8a5c2f9b40d73",
  "created_at": "2026-11-20T09:14:07.482913Z",
  "data": {
    "type": "external_key.failed",
    "id": "ekey_011CZkZFr7KpXc4nMgSvQh3w",
    "organization_id": "org_011CZkZBj9RsYd3wNcHvKq6t"
  }
}
```

* **Time:** `created_at` is when Anthropic first tried to send the event, not when the key failed or recovered. It can include fractional seconds.
* **Workspaces:** The event doesn’t name a workspace, because several can use one key.

### Respond to an encryption key event

After you return `2xx` for either event, [validate the key](https://platform.claude.com/docs/en/api/organization/external_keys/validate) with `POST /v1/organizations/external_keys/{external_key_id}/validate`. Use `data.id` as the ID, and an Admin API key or an `org:admin` token. What you do next depends on the `status` in the response:

* **`failure`, and the `error` message says to try again:** Do what it says, and validate again.
* **`failure`, with any other message:** Find the fix in [Troubleshoot CMEK](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting).
* **`success`:** Check each workspace that uses the key, because validation tests one at most. Your KMS might refuse others, as with an [AWS key policy that lists workspaces](https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces).

To check the workspaces:

1. [List your workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) with `include_default=true`.
2. Find those with the key’s ID in `external_key_id`.
3. Send a Messages API request in each one, with an API key that can act in that workspace.

| Result of the request | What it means for the workspace |
| ----- | ----- |
| [`cmek_key_disabled`](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#cmek-key-disabled) or [`cmek_key_network_blocked`](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#cmek-key-network-blocked) error | Your KMS refuses Anthropic. |
| [`cmek_key_unreachable`](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#cmek-key-unreachable) error | Anthropic can’t reach your KMS. |
| Success | The key works, or it stopped working less than an hour ago. |

[Requests can succeed for up to 1 hour](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#what-each-action-does) after a key stops working, so if a request succeeds, send it again an hour after `external_key.failed`. An error can last a few minutes after a fix.

After a fix, repeat these checks. Don’t wait for `external_key.recovered`, which might not arrive.

### When encryption key events arrive

If each workspace that uses the key gets about one Messages API request a minute, the events usually arrive at these times. With less traffic, they take longer:

* **`external_key.failed`:** Within 30 minutes of someone disabling the key or removing Anthropic’s access to it. Requests might still succeed when it arrives.
* **`external_key.recovered`:** About 30 minutes after the key works again.

### When an encryption key event might not arrive

Don’t make these events your only signal. Also, alert on the three `cmek_key` errors from the Messages API, and [catch up on missed events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#catch-up-on-missed-events) at a regular interval.

In these cases, you might miss one or both events:

| Case | What you might miss |
| ----- | ----- |
| No request uses the key | `external_key.failed`, because Anthropic sees a refusal only when a request uses the key |
| No request uses the key within about a day of the last refusal | `external_key.recovered`, because Anthropic stops waiting for a success |
| Your KMS has an outage or times out | Both events, because an outage isn’t a refusal |
| Keys at several organizations start to fail at about the same time | Both events and the emails, because the cause might be Anthropic or a cloud provider |
| [Your Default Workspace’s key](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#if-your-default-workspace-uses-an-encryption-key) fails, and it encrypts a value of your endpoint | Every event until the key works again, including its own `external_key.failed` |

Because you can miss either event, you might receive `external_key.failed` twice in a row, or `external_key.recovered` with no `external_key.failed` before it.

## Customer-owned storage events

These events are about the buckets that you use as [customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage). The Admin API calls such a bucket External Storage, so the event types start with `external_storage`:

| Event | Trigger |
| ----- | ----- |
| `external_storage.failed` | A bucket fails [Anthropic’s daily check](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#bucket-health). |
| `external_storage.recovered` | After Anthropic sends `external_storage.failed`, the bucket passes a check again. |

The check covers each bucket that a workspace uses for [Sealed Safety Data](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored). It also covers each bucket in the [`draining` status](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage?method=api#api-check), which workspaces have stopped using. Don’t rely on these events for a bucket that receives only Transcripts and Safety Cases.

Only the daily check starts these events. There’s no test event.

When a bucket fails or recovers, Anthropic usually also emails the members of your organization whose role lets them manage encryption keys, such as `admin`. You don’t need a key to get these emails.

To receive the events, your organization needs organization webhooks, as [Before you start](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#before-you-begin) describes.

The event names the bucket in `data.id`, which starts with `estrg_`:

```json
{
  "type": "event",
  "id": "whe_2b7e9d4c1a6f8035e2d9b6c3a0f51e84",
  "created_at": "2026-12-02T06:41:19.305127Z",
  "data": {
    "type": "external_storage.failed",
    "id": "estrg_01SDCCSbTxrXDpWc1phhtcfK",
    "organization_id": "org_011CZkZBj9RsYd3wNcHvKq6t"
  }
}
```

* **Time:** `created_at` is when Anthropic first tried to send the event, not when the check ran. It can include fractional seconds.
* **Cause and workspaces:** The event doesn’t say why the bucket failed or which workspaces use it.

### Respond to a storage event

After you return `2xx` for either event, [get the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage?method=api#api-check) with `GET /v1/organizations/external_storage/{external_storage_id}`. Use `data.id` as the ID, and an Admin API key or an `org:admin` token. The requests in this section need the `anthropic-beta: efs-2026-10-01` header.

The response isn’t a live test. `status.healthy` says whether the bucket passed the latest check that reached a result, and `status.last_checked_at` says when that check ran.

If `status.healthy` is `false`:

1. Tell your Anthropic account team at once, one time for each failure. Sealed Safety Data that doesn’t reach your bucket might be lost.
2. Follow [If your bucket stops working](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working).
3. Get the bucket again about a day after `status.last_checked_at`. If `status.healthy` is still `false`, repeat from step 2.

`status.healthy` usually stays `false` until the next check passes. Don’t wait for `external_storage.recovered`, which might not arrive. If writes still work, look for a changed setting, such as [an added lifecycle rule](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#what-removes-data), which also fails the check.

If `status.healthy` is `true` after a failure, tell your Anthropic account team that the bucket works again. They can then confirm whether Anthropic needs to recover data from the time it failed.

To see which workspaces a failure affects:

1. [List your workspaces](https://platform.claude.com/docs/en/api/organization/workspaces/list) with `include_default=true`.
2. Look for the bucket’s ID in the `external_storage_id` fields under [`inference_data_privacy`](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage?method=api#api-attach).

### When storage events arrive

The check runs once a day, so an event can arrive a day or more after the change in your bucket:

* **`external_storage.failed`:** Usually about 15 minutes after the check that fails. While the bucket keeps failing, later checks don’t send it again.
* **`external_storage.recovered`:** Usually within minutes of the next daily check that passes.

### When a storage event might not arrive

Don’t make these events your only signal. Also, [watch for objects arriving in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#if-your-bucket-stops-working) while you send requests, and [catch up on missed events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#catch-up-on-missed-events) at a regular interval.

In these cases, you might miss one or both events:

| Case | What you might miss | `status.healthy` |
| ----- | ----- | ----- |
| Writes fail and work again between two checks | Both events | Unchanged |
| Only the IAM roles for Transcripts and Safety Cases fail | Both events | Might not change |
| The check reaches no result | Both events, until a check reaches a result | Unchanged |
| The bucket failed before you added these events to an endpoint | `external_storage.failed` | `false` |
| Buckets at several organizations, yours included, start failing on the same day | Both events and the emails | Usually `false` |
| [Your Default Workspace’s key](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#if-your-default-workspace-uses-an-encryption-key) fails, and it encrypts a value of your endpoint | Every event until the key works again | Up to date |

Two of these cases need a check of your own:

* **The IAM roles for Transcripts and Safety Cases:** The daily check can pass while they fail, so watch for those objects in your bucket.
* **A check that reaches no result:** `status.last_checked_at` stops moving. A removed or changed IAM role can cause this, so check the roles that give Anthropic access.

Because you can miss either event, you might receive `external_storage.failed` twice in a row, or `external_storage.recovered` with no `external_storage.failed` before it.

## Endpoint fields

An organization webhook endpoint has these fields:

| Field | Type | Description |
| ----- | ----- | ----- |
| `id` | string | The endpoint’s ID, which starts with `wep_`. Set by Anthropic. |
| `url` | string | Where Anthropic sends events. Must be HTTPS on port 443, with a public domain name, not an IP address. Two enabled organization webhook endpoints in your organization can’t share a URL. |
| `enabled_events` | array of strings | The [event types](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#event-types) this endpoint receives. A create request must list at least one. |
| `name` | string | An optional label for your own use. |
| `description` | string | An optional description for your own use. |
| `state` | string | `enabled` or `disabled`. |
| `disabled_reason` | string | Why Anthropic disabled the endpoint. Empty otherwise. |
| `created_at` | string | When the endpoint was created. Set by Anthropic. |
| `updated_at` | string | When the endpoint last changed. Set by Anthropic. |
| `signing_secret` | string | A `whsec_`-prefixed secret, created with the endpoint. Only the responses that create the endpoint or replace the secret include it, so store it securely. |

```json
{
  "id": "wep_011CZkZDf8HnUq2mTxRbVn4s",
  "url": "https://example.com/anthropic-webhooks",
  "name": "Enforcement actions",
  "description": "",
  "enabled_events": [
    "user_profile.enforcement_action_opened",
    "user_profile.enforcement_action_resolved"
  ],
  "state": "enabled",
  "disabled_reason": "",
  "created_at": "2026-10-20T19:00:00Z",
  "updated_at": "2026-10-20T19:00:00Z"
}
```

An organization can have up to 32 organization webhook endpoints. Disabled webhook endpoints still count toward this total.

## Deliveries

Deliveries follow the [Standard Webhooks](https://www.standardwebhooks.com/) specification. Each one carries the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers. Before you trust an event, verify its signature with the endpoint’s signing secret, using any Standard Webhooks library.

Return any `2xx` status within 5 seconds, and do slow work afterward. Any other response, or no response, counts as a failed attempt.

* **Duplicates:** An endpoint might receive the same event more than once, with the same event `id` (the same value as the `webhook-id` header). Deduplicate on it.

* **Retries:** If a delivery fails, Anthropic retries it a few times over the next few minutes. If every attempt fails, Anthropic drops the event, so even a short outage of your endpoint can lose events.

* **Automatic disabling:** Anthropic disables an endpoint when:

  * It returns a redirect (`3xx`).
  * Its URL resolves to a non-public IP address.
  * Its deliveries keep failing.

  Anthropic skips events for a disabled endpoint and doesn’t send them later.

### Catch up on missed events

Anthropic doesn’t tell you when it drops an event, disables an endpoint, or skips an event for a disabled endpoint. Catch up at a regular interval, such as once a day, and at these times:

* When you first add event types to an endpoint
* After an outage of your endpoint
* After you turn an endpoint back on

Each time, check that your endpoint’s `state` is `enabled`. Then, check the resources behind each group of events that you use:

* **User profiles:** List your profiles by enforcement status, as in [Before your first event](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#before-your-first-event). A profile that’s missing from those lists has no open action.

* **Encryption keys:** [List your keys](https://platform.claude.com/docs/en/api/organization/external_keys/list), and [validate each one](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#respond-to-an-encryption-key-event). If you received no event for the key, a `success` needs no more checks unless Messages API requests fail.

* **Customer-owned storage:** [List your buckets](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage?method=api#api-check), and look at each bucket that the daily check covers:

  * If `status.healthy` is `false`, follow [Respond to a storage event](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#respond-to-a-storage-event).
  * If `status.last_checked_at` is more than 2 days old, tell your Anthropic account team.

## Manage endpoints

With the Admin API, you can make these requests:

| Task | Request |
| ----- | ----- |
| List your organization’s endpoints | [`GET /v1/organizations/webhooks`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/list) |
| Create an endpoint | [`POST /v1/organizations/webhooks`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/create) |
| Get one endpoint | [`GET /v1/organizations/webhooks/{webhook_endpoint_id}`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/retrieve) |
| Update an endpoint’s `url`, `name`, `description`, `enabled_events`, or `state` | [`POST /v1/organizations/webhooks/{webhook_endpoint_id}`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/update) |
| Delete an endpoint | [`DELETE /v1/organizations/webhooks/{webhook_endpoint_id}`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/delete) |
| Replace the signing secret | [`POST /v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret`](https://platform.claude.com/docs/en/api/beta/organization/webhooks/regenerate_signing_secret) |

In an update, `enabled_events` replaces the endpoint’s whole list of event types. An empty list doesn’t clear the list: the endpoint keeps the event types it had. To stop deliveries, send `"state": "disabled"` or delete the endpoint.

To turn an endpoint back on, including after Anthropic disabled it, send `"state": "enabled"` in an update request.

When you replace the signing secret, the old secret stops working at once. Deliveries from then on, including retries of earlier events, are signed with the new secret, so update your receiver right away.

Send the `anthropic-beta: webhooks-2026-10-07` header with every request. The SDK and the CLI send it for you. This example lists your organization’s endpoints, using an Admin API key from `ANTHROPIC_API_KEY`.

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/webhooks" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: webhooks-2026-10-07"
  ```

  ```bash CLI
  ant beta:organization:webhooks list
  ```

  ```python Python
  client = anthropic.Anthropic()

  endpoints = client.beta.organization.webhooks.list()

  for endpoint in endpoints:
      print(f"{endpoint.id}: {endpoint.url} ({endpoint.state})")
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const endpoints = await client.beta.organization.webhooks.list();

  for await (const endpoint of endpoints) {
    console.log(`${endpoint.id}: ${endpoint.url} (${endpoint.state})`);
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var page = await client.Beta.Organization.Webhooks.List();

  await foreach (var endpoint in page.Paginate())
  {
      Console.WriteLine($"{endpoint.ID}: {endpoint.Url} ({endpoint.State.Raw()})");
  }
  ```

  ```go Go
  client := anthropic.NewClient()

  endpoints := client.Beta.Organization.Webhooks.ListAutoPaging(context.Background(), anthropic.BetaOrganizationWebhookListParams{})

  for endpoints.Next() {
  	endpoint := endpoints.Current()
  	fmt.Printf("%s: %s (%s)\n", endpoint.ID, endpoint.URL, endpoint.State)
  }
  if err := endpoints.Err(); err != nil {
  	log.Fatal(err)
  }
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  var endpoints = client.beta().organization().webhooks().list();

  for (var endpoint : endpoints.autoPager()) {
      IO.println(endpoint.id() + ": " + endpoint.url() + " (" + endpoint.state().asString() + ")");
  }
  ```

  ```php PHP
  $client = new Client();

  $endpoints = $client->beta->organization->webhooks->list();

  foreach ($endpoints->pagingEachItem() as $endpoint) {
      echo "{$endpoint->id}: {$endpoint->url} ({$endpoint->state})\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  endpoints = client.beta.organization.webhooks.list

  endpoints.auto_paging_each do |endpoint|
    puts "#{endpoint.id}: #{endpoint.url} (#{endpoint.state})"
  end
  ```
</CodeGroup>

With no endpoints, the API returns an empty list:

```json
{
  "data": [],
  "has_more": false
}
```

A list returns up to 20 endpoints by default. Set `limit` to get up to 100. If `has_more` is `true`, pass the response’s `last_id` as `after_id` to get the next page.

This example creates an endpoint for the two user profile events, which Anthropic doesn’t send. To receive other events, such as `external_key.failed` and `external_key.recovered`, list their types in `enabled_events` instead:

<CodeGroup>
  ```bash cURL
  curl "https://api.anthropic.com/v1/organizations/webhooks" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2026-10-21" \
    -H "anthropic-beta: webhooks-2026-10-07" \
    -H "content-type: application/json" \
    -d '{
      "url": "https://example.com/anthropic-webhooks",
      "name": "Enforcement actions",
      "enabled_events": [
        "user_profile.enforcement_action_opened",
        "user_profile.enforcement_action_resolved"
      ]
    }'
  ```

  ```bash CLI
  ant beta:organization:webhooks create \
    --url https://example.com/anthropic-webhooks \
    --name "Enforcement actions" \
    --enabled-event user_profile.enforcement_action_opened \
    --enabled-event user_profile.enforcement_action_resolved
  ```

  ```python Python
  client = anthropic.Anthropic()

  endpoint = client.beta.organization.webhooks.create(
      url="https://example.com/anthropic-webhooks",
      name="Enforcement actions",
      enabled_events=[
          "user_profile.enforcement_action_opened",
          "user_profile.enforcement_action_resolved",
      ],
  )

  print(endpoint.id)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const endpoint = await client.beta.organization.webhooks.create({
    url: "https://example.com/anthropic-webhooks",
    name: "Enforcement actions",
    enabled_events: [
      "user_profile.enforcement_action_opened",
      "user_profile.enforcement_action_resolved"
    ]
  });

  console.log(endpoint.id);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Organization.Webhooks;

  AnthropicClient client = new();

  var endpoint = await client.Beta.Organization.Webhooks.Create(new WebhookCreateParams
  {
      UrlValue = "https://example.com/anthropic-webhooks",
      Name = "Enforcement actions",
      EnabledEvents =
      [
          EnabledEvent.UserProfileEnforcementActionOpened,
          EnabledEvent.UserProfileEnforcementActionResolved,
      ],
  });

  Console.WriteLine(endpoint.ID);
  ```

  ```go Go
  client := anthropic.NewClient()

  endpoint, err := client.Beta.Organization.Webhooks.New(context.Background(), anthropic.BetaOrganizationWebhookNewParams{
  	URL:  "https://example.com/anthropic-webhooks",
  	Name: anthropic.String("Enforcement actions"),
  	EnabledEvents: []string{
  		"user_profile.enforcement_action_opened",
  		"user_profile.enforcement_action_resolved",
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(endpoint.ID)
  ```

  ```java Java
  import com.anthropic.models.beta.organization.webhooks.WebhookCreateParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      var params = WebhookCreateParams.builder()
          .url("https://example.com/anthropic-webhooks")
          .name("Enforcement actions")
          .addEnabledEvent(WebhookCreateParams.EnabledEvent.USER_PROFILE_ENFORCEMENT_ACTION_OPENED)
          .addEnabledEvent(WebhookCreateParams.EnabledEvent.USER_PROFILE_ENFORCEMENT_ACTION_RESOLVED)
          .build();

      var endpoint = client.beta().organization().webhooks().create(params);

      IO.println(endpoint.id());
  }
  ```

  ```php PHP
  $client = new Client();

  $endpoint = $client->beta->organization->webhooks->create(
      url: 'https://example.com/anthropic-webhooks',
      name: 'Enforcement actions',
      enabledEvents: [
          'user_profile.enforcement_action_opened',
          'user_profile.enforcement_action_resolved',
      ],
  );

  echo $endpoint->id, "\n";
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  endpoint = client.beta.organization.webhooks.create(
    url: "https://example.com/anthropic-webhooks",
    name: "Enforcement actions",
    enabled_events: [
      "user_profile.enforcement_action_opened",
      "user_profile.enforcement_action_resolved"
    ]
  )

  puts endpoint.id
  ```
</CodeGroup>

The response is the new endpoint, as shown in [Endpoint fields](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#endpoint-fields), plus its `signing_secret`.

If you have the `admin` organization role, you can instead manage endpoints for encryption key events and customer-owned storage events in the Claude Console. Use the **Organization** tab of the [Webhooks](https://platform.claude.com/settings/webhooks) page, which shows the signing secret once, when you create an endpoint or replace its secret.

## If your Default Workspace uses an encryption key

Anthropic stores your organization’s endpoints in your [Default Workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work). If that workspace uses a [customer-managed encryption key](https://platform.claude.com/docs/en/manage-claude/cmek), Anthropic encrypts these values with the key:

| Value | Requests that encrypt it |
| ----- | ----- |
| `name` and `description` | Create the endpoint, or send any update to it |
| Signing secret | Create the endpoint, or replace the secret |

Anthropic doesn’t encrypt other fields, such as `url`, with your key.

On an endpoint created before [your key takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect), each value stays under Anthropic’s key until one of those requests encrypts it. No field shows which key protects a value. To move an endpoint’s values under your key, update the endpoint and replace its secret.

Once your key encrypts any value of an endpoint, the endpoint depends on the key. While Anthropic can’t use the key, deliveries and requests that need it fail. Requests usually return a `500` error:

| What fails | For which endpoints |
| ----- | ----- |
| Deliveries of every event type | Those that depend on the key |
| Get and delete requests | Those that depend on the key |
| List requests | All, if any endpoint depends on the key |
| Create, update, and replace-secret requests | Usually all |

Anthropic drops the events that it can’t deliver, and doesn’t send them later. The endpoints stay enabled, and deliveries resume once Anthropic can use the key. Then, [catch up on missed events](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#catch-up-on-missed-events).

If you delete the key in your KMS, all of these failures are permanent, and you can’t create another endpoint. For what else stops Anthropic from using a key, see [What happens when you rotate, disable, or delete your encryption key](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle).

## Errors

A request returns a `400` if:

* Its `url` doesn’t meet the rules in [Endpoint fields](https://platform.claude.com/docs/en/manage-claude/organization-webhooks#endpoint-fields), or a create request lists no event types. The error message says what’s wrong.
* Your organization has no Default Workspace.
* It would give your organization more than 32 organization webhook endpoints.
* Its `enabled_events` includes an event type that organization webhook endpoints don’t accept. The error message lists the accepted types.

A request returns a `403` if your account’s role doesn’t include the permission the request needs. The error names that permission.

A request returns a `404` if:

* It doesn’t send the `anthropic-beta: webhooks-2026-10-07` header.
* Anthropic hasn’t turned on organization webhooks for your organization.
* Your organization has HIPAA readiness enabled.
* It uses a kind of credential these requests don’t accept.
* Its `webhook_endpoint_id` doesn’t match an endpoint in your organization.

A request returns a `409` if:

* It would make two enabled organization webhook endpoints share a URL.
* Another request changed your organization’s endpoints at the same time. Retry the request.
