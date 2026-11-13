---
title: Get an organization's security posture
url: https://platform.claude.com/docs/en/api/compliance/organizations/security_posture/retrieve
---

# Get an organization's security posture

**GET** `/v1/compliance/organizations/{organization_id}/security_posture`

Get an organization's security controls and their current results.

Returns the organization's security controls, evaluated at the time of the
request, each with its attestation when this endpoint returns one. The controls come
in one `controls` list, which is not paginated. A control can have no entry, for
example when it is about a feature that the organization cannot have, so a missing
control is not a pass.

The `anthropic-version` header is required: a request without it, or with a value
that is not an available version, returns 400.
The endpoint takes no query parameters, so there is no filter, and a request with
any query parameter also returns 400. A request also returns 400 when the Compliance
API is not enabled for the API key's parent organization.
The request returns 404 when `organization_id` names no organization, names one
that the API key cannot read, or names one whose security controls are not
available. A request over a rate limit returns 429.

One error has an `error_code` in `error.details`. A 503 with
`posture_evaluation_failed` means that the evaluation could not be completed.
Wait for the time in the `Retry-After` header before trying again. A 504 means
that the evaluation did not finish in time, and the request can be tried again.

## Path parameters

- `organization_id: string`

  The organization's UUID

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. A request that omits this header, or sends a value that is not an available version, returns a 400 error.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Returns

- `type: "security_posture"`

  Always `security_posture`.

- `comments_status: "available" or "not_enabled" or "not_permitted" or 2 more`

  Whether attestation comments were read. More values can be added; read an unknown one as `unavailable`.

  - `"available"`

    Comments were read, so a null `comment` means that there is none, or that the attestation was saved moments ago.

  - `"not_enabled"`

    This endpoint does not return comments for the organization, so every `comment` is null.

  - `"not_permitted"`

    The API key holds neither `read:compliance_user_data` nor `read:org_audit`, so every `comment` and every `attested_by` is null.

  - `"requires_organization_key"`

    The API key was not created in the organization, for example because it was created for the parent organization, so no comment is read and every `comment` is null. `attested_by` is returned as it is to a key created in the organization. This value does not say whether this endpoint returns comments for the organization. Retrying does not help: only a key created in the organization can read its comments.

  - `"unavailable"`

    Comments could not be read for this response. A later request may succeed, but some causes persist, for example when the organization's customer-managed encryption key cannot be used.

- `controls: array of object`

  The organization's controls, never empty. A control can have no entry, for example when it is about a feature that the organization cannot have, so a missing control is not a pass.

  - `id: string`

    The control's identifier, which is the same for every organization and never changes.

  - `attestation: object or null`

    The attestation of this control. It is still returned after it stops being in effect; see its `state`. Null when nobody has attested, when attestations of this kind are not enabled for the organization, and while the status is `descriptive`, `not_applicable` or `not_evaluated`. It is also null when the attestation stored for the control is of a kind that this endpoint does not return, so null does not prove that nobody has attested.

    - `attested_at: string`

      When the attestation was made.

      format: date-time

    - `attested_by: object or null`

      Who made the attestation. Null when the response's `comments_status` is `not_permitted`, when showing who attested is not enabled for the organization, when the person's account has been deleted, or while Anthropic holds back who attested for every organization.

      - `type: "user_actor"`

        Always `user_actor`.

      - `user_id: string`

        User identifier (tagged ID, prefixed `user_`).

    - `comment: string or null`

      The comment saved with the attestation, of at most 2,000 characters. It is the text of the last save, which can keep words that an earlier administrator wrote. Null if there is none, or if the response's `comments_status` is not `available`.

    - `state: "check_passing" or "in_force" or "review_due" or "setting_changed" or null`

      Whether the attestation is still in effect. Null only on a manual control, and only when end dates do not apply to the organization; the attestation is then in effect. More values can be added; read an unknown one as not in effect.

      - `"check_passing"`

        Not in effect: the automatic check passes.

      - `"in_force"`

        The attestation is in effect.

      - `"review_due"`

        Not in effect: the attestation's end date, also called its review date, has come, so it is due for review.

      - `"setting_changed"`

        Not in effect: the automatic check fails, either on a different value from the one whose risk was accepted, or after the accepted risk was recorded as ended.

  - `current_value: string or null`

    The value read for the control, as display text whose wording can change. It is in English, apart from values taken from the organization's settings, such as its allowed email domains. A list names only the entries that this endpoint recognizes, followed by the number of other entries, if any. Null on a manual control, while the status is `not_evaluated`, and while the status is `not_applicable` because the control applies only when another setting has a certain value.

  - `desired_state: string or null`

    The recommended value, as display text whose wording can change. It is in English, apart from values such as the organization's ID. Null when there is none for this organization.

  - `display_name: string`

    The control's display name, in English.

  - `rating: "descriptive" or "failed" or "not_attested" or "passed"`

    The control's overall result, which follows from `status`. More values can be added; read an unknown one as not passed.

    - `"descriptive"`

      Descriptive: not rated, which includes controls that do not apply or could not be read.

    - `"failed"`

      Failed. Because of an attestation that this endpoint does not return, a control can have this rating while the Security posture page shows it as Passed.

    - `"not_attested"`

      Not attested: a manual control with no attestation in effect.

    - `"passed"`

      Passed. This includes a control with an accepted risk in effect, whether automatic or manual.

  - `section: "capabilities" or "chats_desktop_mdm" or "claude_code_admin_console" or 7 more`

    The section that this control belongs to. More values can be added; treat an unknown one as a section of its own.

    - `"capabilities"`

      Capabilities

    - `"chats_desktop_mdm"`

      Chats: desktop device management

    - `"claude_code_admin_console"`

      Claude Code: admin console

    - `"claude_code_managed_settings"`

      Claude Code: managed settings

    - `"connectors_integrations"`

      Connectors and integrations

    - `"cowork_admin_console"`

      Cowork: admin console

    - `"cowork_desktop_mdm"`

      Cowork: desktop device management

    - `"data_privacy"`

      Data and privacy

    - `"healthy_adoption"`

      Healthy adoption

    - `"identity_access"`

      Identity and access

  - `setting_name: string or null`

    The `name` of the entry in the organization's effective settings that this control reads. Null when it reads no such entry.

  - `status: "attestation_not_enabled" or "attested_accepted_risk" or "attested_completed" or 10 more`

    Why the control has its rating. A manual control is one that only a person can check. An automatic control reads a value from the organization, usually one of its settings, and some are checked against a recommended value. The recommended values are those of the standard profile, which every organization is rated under. More values can be added; count a control with an unknown one by its `rating`.

    - `"attestation_not_enabled"`

      A manual control that nobody in the organization can attest to.

    - `"attested_accepted_risk"`

      A manual control attested as Accepted risk, with the attestation in effect.

    - `"attested_completed"`

      A manual control attested as Completed, with the attestation in effect.

    - `"descriptive"`

      The control is reported for information only.

    - `"exceeds_baseline"`

      The current value is stricter than the recommended value.

    - `"failed"`

      The current value does not meet the recommended value. An attestation that this endpoint does not return can also give a control this status.

    - `"failed_check_accepted_risk"`

      The automatic check fails, and an accepted risk is in effect.

    - `"matches_profile"`

      The current value equals the recommended value.

    - `"not_applicable"`

      The control does not apply to the organization.

    - `"not_attested"`

      A manual control that can be attested to, with no attestation in effect.

    - `"not_evaluated"`

      The setting behind the control, or another setting that decides whether the control applies, could not be read.

    - `"passed"`

      The current value meets the recommended value.

    - `"review"`

      The current value is looser than the recommended value.

- `evaluated_at: string`

  The time at which every control was evaluated.

  format: date-time

- `organization_id: string`

  The organization's UUID.

## Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/security_posture \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "comments_status": "not_enabled",
  "controls": [
    {
      "id": "sso_enabled",
      "attestation": {
        "attested_at": "2025-03-12T18:22:41.123456Z",
        "attested_by": {
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "comment": null,
        "state": "in_force"
      },
      "current_value": "On",
      "desired_state": "On",
      "display_name": "Single sign-on (SSO)",
      "rating": "passed",
      "section": "identity_access",
      "setting_name": "sso_enabled",
      "status": "passed"
    }
  ],
  "evaluated_at": "2025-03-12T18:22:41.123456Z",
  "organization_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "type": "security_posture"
}
```
