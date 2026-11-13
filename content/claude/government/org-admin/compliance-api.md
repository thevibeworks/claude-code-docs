> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compliance API

> Stream your organization's audit events into a SIEM or log management system.

> **Who this is for:** Organization owners, tenant administrators, and the security or compliance teams who connect Claude for Government to their agency's log management or SIEM platform.

The Compliance API is a read-only HTTP endpoint that lets your security tools pull a continuous feed of audit events covering administrative activity across your organization, such as sign-ins, role changes, key creations, and seat assignments. A scheduled job can poll the endpoint and forward each event to a SIEM such as Splunk or Microsoft Sentinel.

The API is available to every Claude for Government organization by default, and it is read-only, so a compromised key cannot change anything in your organization.

## Managing API keys

Create the key in the portal that covers the events you want:

* **One organization**: go to **Settings > Admin API keys** in the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it) and [create a key](https://claude.com/docs/government/org-admin/admin-api-keys.md#create-a-key) with **Compliance activity feed** selected. It returns events for that organization only, regardless of who holds the key.
* **Every organization in your tenant**: go to **Settings > Compliance API keys** in the [tenant admin portal](https://claude.com/docs/government/tenant-admin/overview.md), enter a name, click **Create key**, and copy the key before you click **Done**. Only tenant administrators can open that portal. The key returns the events of every organization in the tenant, together with tenant-level activity such as changes to single sign-on, to the list of tenant administrators, and to tenant-wide settings.

Both kinds of key are shown only once, never expire, and are [rotated and revoked](https://claude.com/docs/government/org-admin/admin-api-keys.md#rotate-or-revoke-a-key) the same way, each on the page where it was created.

## Calling the API

Send a GET request to your Claude for Government host followed by the fixed path `/gateway-api/v1/compliance/activities`, with your key in the `x-api-key` header. The Claude for Government host is the domain name in the address of your organization admin portal. If you are unsure of it, ask your Anthropic representative.

```http theme={null}
GET https://<claude-for-government-host>/gateway-api/v1/compliance/activities?since=<start-time>&limit=500
x-api-key: <your-compliance-api-key>
```

### Query parameters

| Parameter | Description |
| - | - |
| `since` or `created_at.gte` | The earliest event time to return, as an RFC 3339 timestamp or epoch seconds. If you build the URL yourself, write a `+` in an offset as `%2B`. A lower bound is required on every request that does not carry a cursor. |
| `until` or `created_at.lte` | The latest event time to return, in the same format. Optional. |
| `after_id` | An opaque cursor that continues from where a previous page left off. Pass the `last_id` value from the previous response. |
| `before_id` | An opaque cursor that pages in the other direction. Pass the `first_id` value from the previous response. Cannot be combined with `after_id`. |
| `actor_ids[]` | Return only events performed by the listed actors. Repeat the parameter to pass more than one. |
| `activity_types[]` | Return only events of the listed types. Repeat the parameter to pass more than one. |
| `limit` | Maximum events per page, from 1 to 5000. Defaults to 100. |

The exclusive bounds `created_at.gt` and `created_at.lt` are also accepted if your collector needs them.

The API serves the most recent 30 days of activity. A lower bound earlier than that is treated as 30 days ago.

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
* `anthropic_actor` for an action performed by Anthropic personnel or systems on your behalf, such as initial provisioning. No individual identity is included.

Each event also carries fields specific to its type, such as the role a user was changed to or the name of a key that was created.

### Identifying users

When one of your own users performs an action, `actor.user_id` and `actor.email_address` name them, including on sign-in events. Actions taken by Anthropic personnel or automated systems appear as `anthropic_actor` with no individual identity, by design.

On every `user.*` activity, two top-level fields identify the user the event is about, so your SIEM can map events back to people in your directory without a separate lookup.

| Field | Description |
| - | - |
| `user_id` | The Claude for Government user ID, in the same `usr_` format as `actor.user_id`. |
| `user_email` | The user's email address at the time of the event. |

The user an event is about is not always the actor. When an administrator changes someone's role, the `actor` block names the administrator and these fields name the user whose role changed.

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
    "email_address": "tenant-admin@agency.example.com"
  },
  "user_id": "usr_00000000-0000-0000-0000-000000000002",
  "user_email": "person@agency.example.com",
  "old": "owner",
  "new": "primary_owner",
  "by_tenant_admin": true
}
```

On `user.role_changed` or `user.seat_tier_changed`, `by_tenant_admin: true` means that a tenant administrator who isn't a [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles) of the organization made a change that an Owner can't make, such as granting the Primary Owner role. Otherwise, the field is absent.

### Activity types

Event types use a dotted `resource.action` naming convention. The categories emitted today include:

* **Users** such as `user.created`, `user.signed_in`, `user.role_changed`, `user.seat_tier_changed`, `user.deactivated`, and `user.reactivated`.
* **Organizations** such as `org.created`, `org.renamed`, and `org.deactivated`.
* **Credentials** such as `api_key.created` and `api_key.revoked`.
* **Seats and tiers** such as `seat_allocation.set`, `seat_allocation.tier_assigned`, `seat_tier.created`, and `seat_tier.updated`.
* **Configuration** such as `org_config.capabilities_set`.
* **Tenant** such as `tenant.sso_configured`, `tenant.admin_added`, and `tenant.config_set`. Only keys created in the tenant admin portal return these types.

New types may be added over time, so a collector should forward unfamiliar types rather than reject them.

## Connecting to your SIEM

Most deployments run a small scheduled worker that polls the API on a fixed interval, forwards each event to the SIEM's HTTP ingest endpoint, and records a time watermark so the next run picks up where the last one left off. A worker that falls more than 30 days behind cannot recover the gap.

A typical run requests `since=<watermark>`, forwards every event returned, and if `has_more` is true, follows `after_id=<last_id>` for each further page until `has_more` is false. After all pages are drained, advance your watermark to one hour before the newest `created_at` you saw, because an event can reach the feed after a newer one. Event `id` values are stable and unique, so your collector should deduplicate on `id`, and can then safely retry a page or use an overlapping `since` without creating duplicate records in the SIEM.

## When the API is disabled

Your tenant administrator can turn off the **Compliance API** setting on the [tenant Config page](https://claude.com/docs/government/tenant-admin/configuration.md). When that setting is off, nobody can create a key for this API in the organization or tenant admin portal, and every call to `/gateway-api/v1/compliance/activities` returns a 400 error, including calls made with keys that were valid before the setting changed.

Listing and revoking existing keys in either portal remains available even when the setting is off, so an exposed key can still be revoked.

## Things to know

* The Claude for Government Compliance API is served from the Claude for Government service hostname, not from `api.anthropic.com`. Use the same host you use to reach the admin portal.
* There is no separate Splunk add-on. The polling pattern described under [Connecting to your SIEM](#connecting-to-your-siem) is the reference implementation for a Splunk HTTP Event Collector job.
* The OpenTelemetry export from the Claude applications is a separate log stream, configured with **Telemetry endpoint** on the [Config](https://claude.com/docs/government/config/settings.md#telemetry-endpoint) page. It carries per-session tool and telemetry events to a collector you specify, while this API carries administrative audit events.
* The Compliance API returns governance and audit events only. It does not return conversation content, files, or anything your users type into Claude.
* Keys created in the tenant admin portal have their own limit of 50 active keys, separate from each organization's [limit](https://claude.com/docs/government/org-admin/admin-api-keys.md#create-a-key).
* Events are returned newest first within each page.
* `first_id` and `last_id` are opaque cursors. Pass them back exactly as received rather than constructing them yourself.
* If your network enforces a [tenant restriction](https://claude.com/docs/government/tenant-admin/tenant-restrictions.md), the same restriction applies to Compliance API requests.
