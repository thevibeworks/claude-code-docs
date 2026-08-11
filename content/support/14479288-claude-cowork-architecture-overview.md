# Claude Cowork architecture overview

This article explains where Claude Cowork runs, how each execution mode is isolated, and the admin controls available for restricting its scope.

This article is for Enterprise admins. The architecture described here is the same across all plans. The device-level admin controls at the end apply to Team and Enterprise plans.

Claude Cowork is in beta on web and mobile for Max, Team, and Enterprise plans, and will be rolling out to Pro plans over the next several weeks.

## Where Claude Cowork runs

Cowork sessions run in the cloud by default: the agent loop and code execution run on Anthropic's servers, and sessions and files are saved to the member's Claude account. Cloud execution is in beta and rolling out gradually across plans.

Local execution remains available for existing desktop deployments: the agent loop and code execution run on the member's device, as described below.

### Cloud session architecture

In a session in the cloud, the agent loop and code execution run in an isolated, temporary sandbox on Anthropic-managed infrastructure. Each session gets its own sandbox, created when the session starts and destroyed when it ends, and sandboxes don't share state with each other or across organizations. This infrastructure is kept separate from Anthropic's corporate, research, and model-training environments.

Key properties of a session in the cloud:

- **No access to your network by default.** The sandbox can't reach private, internal, link-local, or cloud-metadata addresses, and it can't reach Anthropic-internal systems, so it can't be used to pivot into your network.

- **Network access follows your existing policy.** A cloud session uses the same network-access setting that governs local Cowork and chat. No network access is the default for Enterprise organizations.

- **Egress is enforced outside the sandbox.** All traffic leaving the sandbox passes through a mandatory proxy the sandbox can't reconfigure or bypass, and only allow-listed destinations are reachable.

- **Short-lived credentials only.** The sandbox holds only session-scoped tokens that expire within hours. Connector authorization tokens never enter the sandbox; connector calls are made on the server side.

- **Tenant isolation at the data layer.** Every stored record is scoped to your organization and account.

When a session in the cloud needs something on the user’s device, like a local file or the browser, the request goes through the Claude Desktop app on that device over an Anthropic-brokered connection. Local file access is limited to folders the member has connected on the desktop, and each local tool call is checked against the member's permissions before it runs. If the desktop app is offline, a session in the cloud can't reach the device.

Because a session in the cloud runs on Anthropic's servers, the agent's work, including any local files it opens through the desktop app, is processed on Anthropic's servers rather than staying on the device. Conversation data is handled under the same commercial commitments as other Team and Enterprise data and isn't used to train Claude.

### Local session architecture

Local sessions apply to existing desktop deployments and use two execution environments on the member's device:

- **The agent loop runs natively on the device.** This includes Claude's conversation handling, file reads and writes in connected folders, web fetches, and local plugin MCP servers. Access is gated by an application-layer permission system that enforces the member's connected-folder rules and your organization's network egress settings.

- **Code execution runs in an isolated virtual machine (VM).** Shell commands and any code Claude writes execute inside a dedicated Linux VM, isolated from the host operating system by the platform's hypervisor (Apple Virtualization.framework on macOS, Hyper-V on Windows). The VM enforces its own network egress filtering, syscall restrictions, and per-session user isolation.

For a detailed technical overview, see the **[Claude Cowork desktop security architecture overview](https://trust.anthropic.com/resources?s=2a7bbzo1lyymvdt551q7kl&name=claude-cowork-desktop-security-architecture-overview)** on our Trust Center.

---

## Admin controls for managed devices

Two MDM keys let you restrict Cowork's scope on managed devices. Both are device-level settings applied through your MDM solution, not from organization settings.

- **Disable local MCP servers:** Set `isLocalDevMcpEnabled` to false to disable plugin-bundled and locally configured MCP servers.

- **Disable desktop extensions:** Set `isDesktopExtensionEnabled` to false to block MCPB and DXT extension servers from running.

Both controls are described in **[Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)**.

These MDM keys govern the Claude Desktop app, so they apply to local sessions and to anything a session in the cloud reaches through the desktop app. Local MCP servers don't run in sessions in the cloud.

The organization-wide Cowork toggle in **Organization settings > Cowork** (**Enable for your organization**) controls whether Cowork is available at all. The device-level controls above only apply when Cowork is enabled.

---

## Organization controls for sessions in the cloud

Beyond the organization-wide Cowork toggle, sessions in the cloud have their own controls in organization settings:

- Turn sessions in the cloud on or off for the organization, while leaving local desktop Cowork available.

- Set the network-access policy that determines which destinations a session in the cloud can reach.

- Require fresh approval for every permission-gated tool call by turning off persistent "always allow," and control whether members can run sessions without per-call approval prompts.

- Require trusted-device enrollment and a recent sign-in for sessions in the cloud. When enabled, this applies to every session in the cloud in the organization.

The device-level MDM keys above govern the Claude Desktop app, so they also apply to what a session in the cloud can reach through the app. With local MCP servers disabled on a managed device, only the folder-limited desktop file tools remain available to sessions in the cloud.

---

## Frequently asked questions

### What happens if a member's device can't start the VM?

This applies to local sessions. Cowork continues running file and web tools while the VM is unavailable. Shell commands and code execution report "workspace unavailable" until the VM recovers.

### Does a session in the cloud have access to users' devices or our network?

Not by default. Sessions in the cloud run in isolated environments on Anthropic's servers, outside your network, and can't reach private or internal addresses. A session in the cloud reaches a member's local files or browser only through the Claude Desktop app on that device, only for folders the member has connected, and only while the app is online.

### Is Cowork activity captured in the Compliance API or OpenTelemetry?

Yes. Cowork via Claude, Claude Desktop, and Claude Mobile is captured in Compliance API. Learn more about **[retrieving remote sessions in the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)**.
​
If you're a Team or Enterprise plan admin, you can **[use OpenTelemetry (OTel) to monitor Claude Cowork activity](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)** across your organization.

### Can endpoint detection (EDR) tools inspect activity inside the VM?

No. The VM is isolated from host-based security tools by design, and sessions in the cloud run entirely outside your endpoints, so EDR tools can't observe them either. If your compliance posture depends on endpoint visibility, account for this before rolling out Cowork.