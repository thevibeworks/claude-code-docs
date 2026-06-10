Title: Claude Cowork desktop architecture overview

URL Source: https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview

Markdown Content:
This article explains how Claude Cowork runs on member devices and the admin controls available for restricting its scope on managed devices.

## Claude Cowork’s two execution environments

Claude Cowork uses two execution environments on each member's device:

## Admin controls for managed devices

Two MDM keys let you restrict Cowork's scope on managed devices. Both are device-level settings applied through your MDM solution, not from organization settings.

The organization-wide Cowork toggle in **Organization settings > Cowork** (**Enable for your organization**) controls whether Cowork is available at all. The device-level controls above only apply when Cowork is enabled.

## Frequently asked questions

### My organization started using Cowork during the research preview. Does this article apply to me?

Not yet. Your organization is still on the older architecture and is being migrated to the one described here. We’ll email your organization admin before the switch.

### What happens if a member's device can't start the VM?

Cowork continues running file and web tools while the VM is unavailable. Shell commands and code execution report "workspace unavailable" until the VM recovers.

### Does Cowork activity show up in audit logs?

### Can endpoint detection (EDR) tools inspect activity inside the VM?

No. The VM is isolated from host-based security tools by design. If your compliance posture depends on endpoint visibility, account for this before rolling out Cowork.

* * *

Related Articles

[Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)
