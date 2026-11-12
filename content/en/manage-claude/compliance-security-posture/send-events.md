---
title: Send Security posture events to your SIEM
url: https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events
description: Request the Security posture activities from the Compliance API Activity Feed, read one of them field by field, and keep your SIEM current with a scheduled read that catches late activities.
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

This page takes you from a Compliance Access Key to Security posture activities arriving as events in your security information and event management (SIEM) system on a schedule. The overview says [which organizations have these activities](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#availability). You need a Compliance Access Key that covers the organization, with the `read:compliance_activities` or `read:org_audit` scope.

## Request the activities

To read only these activities, filter the feed with `activity_types[]`. In this request, `created_at.gte` sets the earliest `created_at` to read, and `order=asc` returns the oldest activities first:

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/activities" \
  -H "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  -H "anthropic-version: 2026-10-21" \
  --data-urlencode "activity_types[]=org_security_control_attestation_updated" \
  --data-urlencode "created_at.gte=2026-10-20T00:00:00Z" \
  --data-urlencode "order=asc" \
  --data-urlencode "limit=5000"
```

The [API reference](https://platform.claude.com/docs/en/api/compliance/activities/list) describes each parameter.

## Read one activity

Each element of the response’s `data` array is an activity like this one.

```json
{
  "id": "activity_01Hq7ZtYc4Vb2NmKx8RsPd3W",
  "type": "org_security_control_attestation_updated",
  "created_at": "2026-10-20T15:04:00.220114Z",
  "organization_id": "org_01JuY4bkwkH1x4PodBJaWmh2",
  "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
  "actor": {
    "type": "user_actor",
    "email_address": "priya@example.com",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "ip_address": "192.0.2.34",
    "user_agent": "Mozilla/5.0..."
  },
  "control": "directory_sync_enabled",
  "action": "attested",
  "status": "accepted_risk"
}
```

* `control` names the [security control](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#controls), one recommended setting or practice.
* `action` says what happened to the [control’s attestation](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#attestations), a person’s recorded statement about the control. Here `attested` means one was recorded for a control that had none.
* `status` is the attestation’s value. Here it is Accepted risk (`accepted_risk`): the control is not in place, and the organization accepts the risk.
* `actor` here identifies the [person who attested](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#who-can-see-who-attested), by user ID and email address.
* `created_at` here is when they attested.

The [Security posture events reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference) lists more fields and values.

## If the response is empty

An empty `data` array is valid. The feed holds only changes made since it [began recording these activities for the organization](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#what-the-feed-does-not-record). It is empty until an attestation is made or changed.

Check that the organization [has these activities](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#availability). Then have someone attest to a control. After a while, repeat the request.

## Run it on a schedule

Any of these activities can become queryable later than the Activity Feed’s usual 1-minute [indexing lag](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns#window-polling), with a `created_at` that is already in the past. So an integration that only moves forward, from a cursor or an advancing `created_at.gte`, never sees such an activity. Re-read a fixed look-back window of 4 hours on every run and drop the activities you already stored:

```text
query = activity_types[]=org_security_control_attestation_updated
      & created_at.gte={now - 4 hours}
      & order=asc
      & limit=5000
cursor = null
loop:
  if cursor is null:
    page = GET /v1/compliance/activities?{query}
  else:
    page = GET /v1/compliance/activities?{query}&after_id={cursor}
  for activity in page.data:
    if activity.id is not in stored_ids:
      store(activity)
      add activity.id to stored_ids
  if not page.has_more: break
  cursor = page.last_id
```

* **Run often:** Run the loop as often as your alerts need, for example every 5 minutes.
* **Keep the same query for the whole run:** Compute `created_at.gte`, in UTC and URL-encoded, at the start of each run. Send the same filters and `order` on every page. With `order=asc`, passing `last_id` as `after_id` returns the next page of newer activities. [Paginate results](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed#paginate-results) explains `after_id` and `last_id`.
* **Deduplicate on `id`:** This step is required, because consecutive runs overlap.
* **Handle failed runs:** If a request fails after the retries in [Handle Compliance API errors](https://platform.claude.com/docs/en/manage-claude/compliance-errors), end the run. The next run reads its whole window again. If runs fail or stop for longer than 4 hours, the next [daily re-read](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events#re-read-15-days-once-a-day) reads the activities they missed.

## Re-read 15 days once a day

Once a day, run the same loop with a look-back window of 15 days in place of 4 hours. This daily re-read also reads an activity that becomes queryable up to 14 days after its `created_at`.

* Record the start time of each daily re-read that completes.
* Delete a stored `id` only if you stored it more than 16 days before the latest recorded start.
* If no start is recorded, set `created_at.gte` as far back as you need; the feed keeps activities for 6 years.
* If more than a day has passed since the latest recorded start, run the next daily re-read with `created_at.gte` set to 15 days before that start.

## If you already ingest the full feed

An integration that reads the whole Activity Feed, with no `activity_types[]` filter that leaves these activities out, already receives them. Check two things:

* **Unrecognized values:** Your handler passes through any `type` or [field value](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference) that it does not recognize. See [Understand the Activity object](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed#understand-the-activity-object).
* **Late activities:** An integration that only asks for newer activities misses one that becomes queryable late. Add the [4-hour re-read](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events#run-it-on-a-schedule) and the [daily 15-day re-read](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events#re-read-15-days-once-a-day) to the integration.

## Check that it works

After someone attests to a control, run the loop until it stores the new activity. Then run it again: it does not store that activity a second time.

## Next steps

To alert on the time you stored an activity, not on its `created_at`, see [Detect changes in Security posture](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes#before-you-write-a-rule). For the Open Cybersecurity Schema Framework (OCSF), see [Map Security posture events to OCSF](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/ocsf-mapping). For current results, see [Security posture results reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference).
