---
title: Get Compliance Settings
url: https://platform.claude.com/docs/en/api/beta/organization/compliance_settings/retrieve
---

# Get Compliance Settings

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

## Returns

- `BetaComplianceSettings object`

  - `type: "compliance_settings"`

    default: compliance_settings

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `BetaComplianceSettingsStateEnabled object`

      - `type: "enabled"`

        default: enabled

    - `BetaComplianceSettingsStateDisabled object`

      - `type: "disabled"`

        default: disabled

## Example

```bash
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```
