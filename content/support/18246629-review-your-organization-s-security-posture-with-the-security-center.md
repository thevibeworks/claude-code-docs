# Review your organization's security posture with the security center

The security center (beta) is a page in Organization settings for Claude Enterprise. It shows how your organization's Claude settings compare with Anthropic's recommended configuration across chats, Claude Cowork, and Claude Code, so your security and IT teams can review them in one place. It also shows which settings are new or recently changed.

For each control, the security center shows the current value, the recommended value where there is one, whether the control passed, and where to change the setting. It's built for the people who own your organization's Claude configuration: Claude Owners, and the IT and security teams who review how Claude is set up.

Security center is in beta for Claude Enterprise organizations.

## Open the security center

1. In Claude, open your account menu and choose “Organization settings.”

2. Select “**[Security posture](https://claude.ai/admin-settings/security-center)**.”

## What the page shows

- **Control groups:** controls are grouped into Org, chats, Cowork, and Claude Code, each with its own count of controls that passed. Each group covers both Organization settings and settings you manage through device management or Claude Code managed settings.

- **For each security control:** its current value, its recommended value where there is one, and its status: **Passed** (matches the recommendation), **Failed** (doesn't match, with why it matters and where to change it), **Not attested** (needs a person to confirm it), or **Shown for information** (reported, not judged).

- **Trends over time:** how your results have moved.

- **New and recently changed:** markers on controls that were recently added or whose value recently changed.

## Additional capabilities

- **Adoption and activity:** figures on how your members use Claude, shown beside the controls.

- **Roles and connectors:** what each of your custom roles allows across connectors and Claude features. Custom roles apply only to members whose role type is Custom.

- **Attestation:** for controls the security center can't check, such as settings in your device management tool or network proxy, record the current state of each control, accept risks, and flag issues in one place. Security center shows who attested and when.

- **Download a report:** in a web browser, select "Download report" and save it as a PDF to share with auditors. It marks which controls were checked automatically and which an Owner confirmed, and it isn't a security certification.

- **Compliance API and programmatic data:** when Compliance API is enabled, you can read the data programmatically to bring it into your security tools. When a control's status changes, an event is sent to your organization's activity feed.

## Frequently asked questions

### Does the security center change any of my settings?

No. It's view-only. You change each setting on its own page in Organization settings.

### Why does a control say "Check manually?"

The setting is managed outside Claude's admin settings, for example in your device management tool or Claude Code managed settings, so the security center can't read it. You can attest to it instead.

### Who can see the security center?

Owners and the Primary Owner. Admins and users can't open it.

**Important:** Security center is guidance, not a guarantee. Its checks compare your settings with Anthropic's recommended configuration, and neither the page nor its PDF report is a security certification. Results Claude checks automatically are labeled separately from controls an Owner confirms by hand.