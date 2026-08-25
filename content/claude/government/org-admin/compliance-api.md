> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compliance API

> Stream your organization's audit events into a SIEM or log management system.

> **Who this is for:** Organization owners and the security or compliance teams who connect Claude for Government to their agency's log management or SIEM platform.

The Compliance API is a read-only HTTP endpoint that lets your security tools pull a continuous feed of audit events covering administrative activity across your organization, such as sign-ins, role changes, key creations, and seat assignments. A scheduled job can poll the endpoint and forward each event to a SIEM such as Splunk or Microsoft Sentinel.

The API is available to every Claude for Government organization by default, and it is read-only, so a compromised key cannot change anything in your organization.

## Managing API keys

Open **Compliance API** in the organization admin portal to create and manage keys. The page lists every key that has been issued for your organization, showing its name, a hint with the last few characters of the key so you can tell them apart, when it was created, and whether it is active or revoked.

To create a key, enter a name and click **Create key**. The full value is shown once, immediately after creation. Copy it somewhere safe before clicking **Done**.

<Warning>
  The full key value is shown **only once**, at creation time. If you lose it, create a new key and revoke the old one.
</Warning>

Keys never expire on their own, so rotate them on whatever schedule your agency's policy requires. You can keep more than one key active at a time, which lets you rotate without interrupting your SIEM feed: create a new key, update your collector to use it, confirm events are still arriving, and then revoke the old key. Revoking a key takes effect immediately, and the next request made with it returns a 401.

Each key is scoped to the organization it was created in. A request can only ever return events for that one organization, regardless of who holds the key.

## Calling the API

Send a GET request to `/v1/compliance/activities` on the Claude for Government host provided to you during onboarding, with your key in the `x-api-key` header.

```http theme={null}
GET /v1/compliance/activities?since=2026-07-01T00:00:00Z&limit=500
Host: <your-deployment-host>
x-api-key: <your-compliance-api-key>
```

### Query parameters

| Parameter                   | Description                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `since` or `created_at.gte` | The earliest event time to return, as an RFC 3339 timestamp or epoch seconds. A lower bound is required on every request that does not carry a cursor. |
| `until` or `created_at.lte` | The latest event time to return, in the same format. Optional.                                                                                         |
| `after_id`                  | An opaque cursor that continues from where a previous page left off. Pass the `last_id` value from the previous response.                              |
| `before_id`                 | An opaque cursor that pages in the other direction. Pass the `first_id` value from the previous response. Cannot be combined with `after_id`.          |
| `actor_ids[]`               | Return only events performed by the listed actors. Repeat the parameter to pass more than one.                                                         |
| `activity_types[]`          | Return only events of the listed types. Repeat the parameter to pass more than one.                                                                    |
| `limit`                     | Maximum events per page, from 1 to 5000. Defaults to 100.                                                                                              |

The exclusive bounds `created_at.gt` and `created_at.lt` are also accepted if your collector needs them.

### Response format

The response is a JSON envelope containing a page of events and the cursors for the next and previous pages.

```json theme={null}
{
  "data": [
    {
      "id": "activity_01js0example000000000000",
      "type": "user.signed_in",
      "created_at": "2026-07-01T14:22:09.412Z",
      "organization_id": "org_00000000-0000-0000-0000-000000000000",
      "organization_uuid": "00000000-0000-0000-0000-000000000000",
      "actor": {
        "type": "user_actor",
        "user_id": "usr_00000000-0000-0000-0000-000000000000",
        "email_address": "person@agency.example.com"
      },
      "user_id": "usr_00000000-0000-0000-0000-000000000000",
      "user_email": "person@agency.example.com"
    }
  ],
  "has_more": true,
  "first_id": "<opaque cursor>",
  "last_id": "<opaque cursor>"
}
```

The `actor` object identifies who performed the action. Its `type` is one of:

* `user_actor` for a person acting through the product or admin portal.
* `admin_api_key_actor` for an action taken through an administrative API key.
* `anthropic_actor` for an action performed by Anthropic personnel or systems on your behalf, such as initial provisioning. No individual identity is included.

Each event also carries fields specific to its type, such as the role a user was changed to or the name of a key that was created.

### Identifying users

When one of your own users performs an action, `actor.user_id` and `actor.email_address` name them, including on sign-in events. Actions taken by Anthropic personnel or automated systems appear as `anthropic_actor` with no individual identity, by design.

On every `user.*` activity, two top-level fields identify the user the event is about, so your SIEM can map events back to people in your directory without a separate lookup.

| Field        | Description                                                                      |
| ------------ | -------------------------------------------------------------------------------- |
| `user_id`    | The Claude for Government user ID, in the same `usr_` format as `actor.user_id`. |
| `user_email` | The user's email address at the time of the event.                               |

The user an event is about is not always the actor. When an owner changes someone's role, the `actor` block names the owner and these fields name the user whose role changed.

```json theme={null}
{
  "id": "activity_01js1example000000000000",
  "type": "user.role_changed",
  "created_at": "2026-07-02T09:18:33.205Z",
  "organization_id": "org_00000000-0000-0000-0000-000000000000",
  "organization_uuid": "00000000-0000-0000-0000-000000000000",
  "actor": {
    "type": "user_actor",
    "user_id": "usr_00000000-0000-0000-0000-000000000001",
    "email_address": "owner@agency.example.com"
  },
  "user_id": "usr_00000000-0000-0000-0000-000000000002",
  "user_email": "person@agency.example.com",
  "old": "user",
  "new": "owner"
}
```

The top-level `user_id` and `user_email` fields appear on activities recorded after they were added to the API. Earlier activities are not updated, so your collector should treat these fields as optional.

### Activity types

Event types use a dotted `resource.action` naming convention. The categories emitted today include:

* **Users** such as `user.created`, `user.signed_in`, `user.role_changed`, `user.deactivated`, and `user.reactivated`.
* **Organizations** such as `org.created`, `org.renamed`, and `org.deactivated`.
* **Credentials** such as `api_key.created` and `api_key.revoked`.
* **Seats and tiers** such as `seat_allocation.set`, `seat_allocation.tier_assigned`, `seat_tier.created`, and `seat_tier.updated`.
* **Configuration** such as `org_config.capabilities_set`.

New types may be added over time, so a collector should forward unfamiliar types rather than reject them.

## Connecting to your SIEM

Most deployments run a small scheduled worker that polls the API on a fixed interval, forwards each event to the SIEM's HTTP ingest endpoint, and records a time watermark so the next run picks up where the last one left off.

A typical run requests `since=<watermark>`, forwards every event returned, and if `has_more` is true, follows `after_id=<last_id>` for each further page until `has_more` is false. After all pages are drained, advance your watermark to the newest `created_at` you saw. Event `id` values are stable and unique, so your collector can deduplicate on `id` and safely retry a page or use an overlapping `since` without creating duplicate records in the SIEM.

## When the API is disabled

Your tenant administrator can turn off the **Compliance API** setting on the [tenant Config page](/docs/government/tenant-admin/configuration). When that setting is off, the Create key button is hidden in the portal, and every call to `/v1/compliance/activities` returns a 400 error, including calls made with keys that were valid before the setting changed.

Listing and revoking existing keys in the portal remains available even when the setting is off, so an exposed key can still be revoked.

## Things to know

* The Claude for Government Compliance API is served from the Claude for Government service hostname, not from `api.anthropic.com`. Use the same host you use to reach the admin portal.
* There is no separate Splunk add-on. The polling pattern described under [Connecting to your SIEM](#connecting-to-your-siem) is the reference implementation for a Splunk HTTP Event Collector job.
* The desktop application's OpenTelemetry export is a separate log stream configured with **Telemetry endpoint (Claude Desktop)** on the [Config](/docs/government/config/settings#telemetry-endpoint-claude-desktop) page. It carries per-session tool and telemetry events to a collector you specify, while this API carries administrative audit events. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for what the OpenTelemetry export includes.
* The Compliance API returns governance and audit events only. It does not return conversation content, files, or anything your users type into Claude.
* Each organization can hold up to 50 active keys at once. Revoked keys do not count toward this limit.
* Events are returned newest first within each page.
* `first_id` and `last_id` are opaque cursors. Pass them back exactly as received rather than constructing them yourself.
* If your network enforces a [tenant restriction](/docs/government/tenant-admin/tenant-restrictions), the same restriction applies to Compliance API requests.
