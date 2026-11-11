---
title: Map Security posture events to OCSF
url: https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/ocsf-mapping
description: Map each Security posture activity in the Compliance API to its Open Cybersecurity Schema Framework (OCSF) class and attributes before you store it.
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

The [Open Cybersecurity Schema Framework](https://schema.ocsf.io/) (OCSF) is an open schema for security events. Apply this mapping to [Security posture](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview) activities in your own pipeline, after you read them and before you store them. To ingest them into your security information and event management (SIEM) system, start at [Send Security posture events to your SIEM](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events).

## OCSF version

This mapping uses OCSF 1.6.0. If you validate against another version, check the attributes on this page against that version. For example, in OCSF 1.7.0, `metadata.uid` is the identifier of the OCSF event itself, and `metadata.original_event_uid` holds the identifier from the source. OCSF 1.9.0 deprecates `actor.app_name` in favor of `actor.application`.

## Attributes for every Security posture activity

Map these fields on every event.

| Activity field      | OCSF attribute                 | Note                                                                                                                                                                                                                                     |
| ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | `metadata.uid`                 | Copy unchanged.                                                                                                                                                                                                                          |
| `type`              | `metadata.event_code`          | Copy unchanged.                                                                                                                                                                                                                          |
| `created_at`        | `time`                         | Convert the RFC 3339 string to milliseconds since the Unix epoch and truncate to a whole number.                                                                                                                                         |
| `created_at`        | `metadata.original_time`       | Copy the string unchanged.                                                                                                                                                                                                               |
| None                | `metadata.logged_time`         | The time at which you stored the activity (`stored_at` on [Detect changes](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes#before-you-write-a-rule)), in milliseconds since the Unix epoch. |
| `organization_uuid` | `metadata.tenant_uid`          | Copy unchanged.                                                                                                                                                                                                                          |
| `organization_id`   | `unmapped.organization_id`     | Copy unchanged.                                                                                                                                                                                                                          |
| None                | `metadata.version`             | Constant: `1.6.0`.                                                                                                                                                                                                                       |
| None                | `metadata.product.vendor_name` | Constant: `Anthropic`.                                                                                                                                                                                                                   |
| None                | `metadata.product.name`        | Constant: `Compliance API`.                                                                                                                                                                                                              |
| None                | `type_uid`                     | `class_uid * 100 + activity_id`.                                                                                                                                                                                                         |
| None                | `severity_id`                  | Set to `1` (Informational) on every event and set an alert’s priority in the [detection rule](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes) that raises it.                              |

Put every field that has no OCSF attribute in the `unmapped` object under its Activity Feed name, including fields that your handler does not recognize. Where a field is absent or `null`, leave out the OCSF attribute.

Map the `actor` object:

| Activity field        | OCSF attribute            | Note                                                                           |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------ |
| None                  | `metadata.profiles`       | Add `host`, the OCSF profile (an optional attribute set) that carries `actor`. |
| `actor.type`          | `unmapped.actor.type`     | Copy unchanged.                                                                |
| `actor.user_id`       | `actor.user.uid`          | `user_actor` only.                                                             |
| `actor.email_address` | `actor.user.email_addr`   | `user_actor` only.                                                             |
| `actor.ip_address`    | `src_endpoint.ip`         | `user_actor` only.                                                             |
| `actor.user_agent`    | `http_request.user_agent` | `user_actor` only.                                                             |
| `actor.service`       | `actor.app_name`          | `system_actor` only.                                                           |

## Attestation activities: Entity Management

Map an [`org_security_control_attestation_updated`](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#attestation-activity) activity to the OCSF Entity Management class (3004). Entity Management events report an operation on a managed entity, here the organization’s attestation for a security control.

| Activity field    | OCSF attribute             | Note                                                                 |
| ----------------- | -------------------------- | -------------------------------------------------------------------- |
| None              | `class_uid`                | Constant: `3004` (Entity Management).                                |
| None              | `category_uid`             | Constant: `3` (Identity & Access Management).                        |
| `action`          | `activity_id`              | From the table of `action` values that follows.                      |
| `action`          | `unmapped.action`          | Copy unchanged, because two `action` values share one `activity_id`. |
| None              | `entity.type_id`           | Constant: `99` (Other).                                              |
| None              | `entity.type`              | Constant: `Security control attestation`.                            |
| `control`         | `entity.uid`               | Copy unchanged.                                                      |
| `status`          | `entity.data.status`       | Copy unchanged: the attestation’s value.                             |
| `review_date`     | `entity.data.review_date`  | Copy unchanged: the attestation’s end date.                          |
| `previous_status` | `unmapped.previous_status` | Copy unchanged: the attestation’s value before the change.           |

Do not map `status` to `status_id` or to any pass or fail value: an attestation is a person’s statement about a control, not the result of a check.

| `action`        | `activity_id`     | `type_uid` |
| --------------- | ----------------- | ---------- |
| `attested`      | `1` (Create)      | `300401`   |
| `changed`       | `3` (Update)      | `300403`   |
| `renewed`       | `3` (Update)      | `300403`   |
| `cleared`       | `4` (Delete)      | `300404`   |
| `lapsed`        | `11` (Deactivate) | `300411`   |
| Any other value | `99` (Other)      | `300499`   |

For `99` (Other), set `activity_name` to the `action` value.

An `attested` activity maps to an event like this one, with sample values:

```json
{
  "class_uid": 3004,
  "category_uid": 3,
  "activity_id": 1,
  "type_uid": 300401,
  "severity_id": 1,
  "time": 1794495872517,
  "metadata": {
    "version": "1.6.0",
    "profiles": ["host"],
    "uid": "activity_01Kp5RvNd8Wc3TgMy6BxQf4Z",
    "event_code": "org_security_control_attestation_updated",
    "original_time": "2026-11-12T15:04:32.517208Z",
    "logged_time": 1794495910000,
    "tenant_uid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
    "product": { "vendor_name": "Anthropic", "name": "Compliance API" }
  },
  "actor": {
    "user": {
      "uid": "user_01TuVwXyZaBcDeFgH2JkLmN4",
      "email_addr": "admin@example.com"
    }
  },
  "src_endpoint": { "ip": "192.0.2.34" },
  "http_request": { "user_agent": "ExampleBrowser/1.0" },
  "entity": {
    "type_id": 99,
    "type": "Security control attestation",
    "uid": "mdm_chat_required_organization",
    "data": { "status": "completed" }
  },
  "unmapped": {
    "action": "attested",
    "actor": { "type": "user_actor" },
    "organization_id": "org_01JuY4bkwkH1x4PodBJaWmh2"
  }
}
```
