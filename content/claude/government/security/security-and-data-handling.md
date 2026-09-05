> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Security and data handling

> Answers for agency security review: sandbox isolation, network egress and required domains, approvals, connector credentials, telemetry, and where data is stored.

> **Who this is for:** Security, compliance, and IT reviewers who are assessing Claude for Government for their agency, and administrators who need to explain the product's runtime behavior.

The answers on this page cover the Claude Desktop application in Claude for Government and address the security and data-handling questions that come up most often during agency security review. Claude Desktop offers three ways to work with Claude: **Chat** for simple conversations, **Cowork** for longer tasks with a local workspace folder, and **Code** for software development. Each answer states what is specific to Claude for Government (the FedRAMP High boundary, the defaults Anthropic applies for government tenants, and the relevant admin portal control), then links to the Claude Desktop documentation for the underlying mechanism. For assurance materials such as the security architecture overview, SOC 2 report, and penetration testing summary, request access through the [Anthropic Trust Center](https://trust.anthropic.com).

## Claude Desktop

The sections below cover the Claude Desktop application. For the admin portal and the Compliance API, see the [Organization administration](/docs/government/org-admin/overview) and [Tenant administration](/docs/government/tenant-admin/overview) sections.

### Sandbox and isolation

In Cowork, and for the file-analysis steps in Chat, the Claude Desktop application runs shell commands and model-written code inside a dedicated local virtual machine. In Claude for Government, this sandbox is always the execution path for the code and shell commands that Claude runs in Chat and Cowork. Code sessions run on the workstation itself rather than in the virtual machine, as described under [Code in Claude Desktop](#code-in-claude-desktop). For the detailed threat model and isolation design, request the security architecture overview through the [Anthropic Trust Center](https://trust.anthropic.com).

<AccordionGroup>
  <Accordion title="What does the sandbox isolate, and what runs outside it?">
    The sandbox virtual machine runs the shell commands and model-written code of Cowork sessions and of the file-analysis steps in Chat. The agent loop, built-in file tools, web fetch, and the connector client run in the Claude Desktop application on the user's device and are governed by separate controls: per-action approval prompts, administrator-set per-tool policies, and the network egress allowlist applied when each tool runs. Code sessions also run outside the virtual machine, as described under [Code in Claude Desktop](#code-in-claude-desktop). For a deeper description of the layered controls inside and outside the virtual machine, see the security architecture overview available through the [Anthropic Trust Center](https://trust.anthropic.com).
  </Accordion>

  <Accordion title="What can the sandbox reach on the host?">
    The sandbox sees the workspace folders the user has attached to the session, its own scratch area, and read-only reference material bundled by the application (such as skill and plugin directories). It does not see the rest of the user's filesystem. File-read and file-write tools default to those same attached folders, and prompt the user before reading or writing outside them; see [Approvals and Auto mode](#approvals-and-auto-mode). Administrators can restrict which local folders users may attach with **Allowed workspace folders** on the [Config](/docs/government/config/settings#allowed-workspace-folders) page; the desktop client then refuses folders outside that list in both the workspace picker and Claude's file tools. See [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access) for how folder scoping is enforced.
  </Accordion>

  <Accordion title="How are attached folders made available to the sandbox?">
    When a user attaches a local folder to a Cowork session, the entire folder is made available to that session's sandbox as a filesystem mount, so changes Claude makes are written directly to the folder on disk. A mapped network drive on Windows is an exception: Claude's host-side file tools can read, write, and search it, but shell commands in the sandbox cannot reach network shares, so a task that runs a script or build against those files must copy them to a local folder first (see [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access#network-drives-on-windows)). Files the user attaches individually to a conversation are copied or hard-linked into a per-conversation uploads directory and mounted read-only; where the filesystem hard-links, edits to the original file while the conversation is open can be visible to it. The allowed-folders setting is a policy control enforced by the desktop application. See [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access).
  </Accordion>

  <Accordion title="Which file types need the sandbox in Chat?">
    Some attachment types, such as Excel and PowerPoint, need a conversion step that runs inside the sandbox. Enabling **Advanced file analysis in Chat** under **Product availability** on the [Config](/docs/government/config/settings#product-availability) page lets Claude run code against attachments in an offline sandbox, including that conversion. You do not need to make Cowork available to get this capability. See [Chat in Claude Desktop](/docs/third-party/claude-desktop/chat) for how Chat handles file attachments.
  </Accordion>
</AccordionGroup>

### Code in Claude Desktop

Code sessions use Claude Code built into the desktop application and run on the user's workstation itself, not in the virtual machine. The shell commands Claude runs during a Code session execute on the workstation's own operating system under the user's own account.

On macOS, those shell commands run inside an operating-system-level sandbox that the application builds from your organization's **Allowed network hosts** and **Allowed workspace folders** settings on the [Config](/docs/government/config/settings#allowed-network-hosts) page. The sandbox is in place whenever either setting restricts access, which the default configuration does. Inside the sandbox, a command can create or change files only in the session's folder, the other folders **Allowed workspace folders** permits, and temporary locations, but the sandbox does not limit which files the command reads: it can read any file on the device that the user's account can open, and by default it runs without asking the user first. A user can exempt specific commands from this sandbox in a Claude Code settings file, and an exempted command runs outside the sandbox under the permission mode the user selects for the session.

The macOS sandbox also blocks connections to local Unix sockets. A command that talks to a local agent through a socket, such as git signing a commit with a key held in an SSH agent or a hardware-backed key manager, cannot reach that agent from inside the sandbox. A user who needs such a command to work can list the agent's socket path under `sandbox.network.allowUnixSockets` in their Claude Code settings file, which keeps the command inside the sandbox. Every sandboxed command in that user's Code sessions can then ask the agent to sign or authenticate, so this is appropriate only for an agent that asks the user to approve each use, for example with Touch ID, and not for an agent that signs without prompting. See [Sandbox settings](https://code.claude.com/docs/en/settings-reference#sandbox-settings) in the Claude Code documentation.

Exempting git commands such as `git commit` with `sandbox.excludedCommands` is not a safe way around the socket restriction. A sandboxed command can still change files that git runs during a commit, such as hook scripts kept in the working tree, and an exempted `git commit` would then run that code outside the sandbox. Git also cannot reach remotes over SSH from inside the sandbox, so a user who needs to push can use an HTTPS remote whose host is on the **Allowed network hosts** list, or push from a terminal outside the Code session.

On Windows, there is no operating-system-level sandbox for Code sessions. Shell commands run directly on the device under the permission mode the user selects for the session and under your agency's own endpoint and network controls. The **Allowed network hosts** and **Allowed workspace folders** settings do not confine what those commands can reach, read, or change.

On both operating systems, the application starts a Code session only in a folder that **Allowed workspace folders** permits when that setting is configured, and Claude's file reading and editing tools then work only inside the permitted folders. Administrators can also require a prompt on every shell command, in every permission mode, with the **Require approval for each command** sub-setting on the **Shell commands** card of the [Config](/docs/government/config/settings#tool-and-connector-cards) page.

Code sessions in Claude for Government run on the local workstation only, and the environment options for Windows Subsystem for Linux (WSL) and SSH remote hosts are not available. Commands that belong to Claude Code's terminal interface, such as `/sandbox`, are not part of Code sessions in the desktop application. See [how your configuration reaches Code sessions](/docs/third-party/claude-desktop/code). If your agency also deploys Claude Code's own managed settings to the same devices, those settings take precedence over the macOS sandbox policy described above unless they opt in to merging, as that page explains.

### Network egress, required domains, and proxies

The desktop application and the sandbox honor the operating system's proxy settings, and a single allowlist controls outbound network access from Claude's tools. You manage the allowlist with the **Allowed network hosts** setting on the [Config](/docs/government/config/settings#allowed-network-hosts) page.

<AccordionGroup>
  <Accordion title="What does the egress allowlist control?">
    The allowlist governs outbound network access from the shell commands and package installs of Cowork sessions, which run in the sandbox virtual machine, from the sandboxed shell commands of Code sessions on macOS (see [Code in Claude Desktop](#code-in-claude-desktop)), and from the host-side web fetch tool. It does not govern web search (which routes through the Claude for Government service) or connector traffic (covered under [Connectors](#connectors) below). When the list is empty or unset, the only hosts reachable from those tools are the Claude for Government service address and, if you have set a **Telemetry endpoint** on the [Config](/docs/government/config/settings#telemetry-endpoint) page, that collector's host, which the application adds to the allowlist automatically. Package installs and page fetches to any other host fail. The list accepts exact hostnames, wildcard patterns such as `*.example.com`, or `*` to allow all outbound traffic. See [Web search and web fetch](/docs/third-party/claude-desktop/web-tools) for the full allowlist semantics.
  </Accordion>

  <Accordion title="Which domains does Claude Desktop need to reach?">
    For configuration and model inference, the application reaches the Claude for Government service hostname provided to your agency during onboarding. Sign-in happens in the user's default browser, which must reach that same hostname, the Claude for Government sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider; see the network prerequisites in [Connect Claude Desktop to Claude for Government](/docs/government/deploy-desktop/configure#before-you-begin). Anthropic-bound telemetry endpoints are not contacted in Claude for Government. Allow `downloads.claude.ai` for the sandbox virtual machine image and the Claude Code command-line tool, which are fetched at session start (not required if your agency uses the offline installer variant that bundles both), and `www.claudeusercontent.com` for the artifact preview frame. For automatic application updates, the required hosts depend on how your agency distributes the client; see the network-requirements table in [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) and confirm the update hosts for your deployment before finalizing your allowlist.
  </Accordion>

  <Accordion title="Can administrators control when Claude Desktop updates?">
    Yes. An agency that distributes Claude Desktop updates itself, for example to keep devices on an assessed version until the next one is approved, turns on **Block automatic updates** on the [Config](/docs/government/config/settings#block-automatic-updates) page and also blocks automatic updates in each device's managed configuration, as described under [Automatic updates](/docs/government/deploy-desktop/configure#automatic-updates). With both in place, the application neither downloads nor installs updates on its own. An agency that leaves automatic updates on can use **Restart deadline for updates** on the [Config](/docs/government/config/settings#restart-deadline-for-updates) page to set how long members may postpone the restart that installs a downloaded update.
  </Accordion>

  <Accordion title="Does Claude for Government depend on claude.ai or anthropic.com?">
    The core product does not. Configuration and model inference go through the dedicated Claude for Government service hostname, and sign-in goes through that hostname, the separate Claude for Government sign-in service, and your agency's identity provider, none of which are under either domain. Blocking `*.claude.ai` and `*.anthropic.com` leaves sign-in and inference working. Blocking `*.claude.ai` also blocks `downloads.claude.ai`, which prevents Cowork and Code sessions from starting and Advanced file analysis in Chat from running, unless the offline installer variant was used.
  </Accordion>

  <Accordion title="Does blocking claude.ai affect Claude for Government?">
    Blocking `claude.ai` does not affect sign-in or inference; neither uses any host under that domain. A personal Claude account cannot sign in to Claude for Government, and a Claude for Government account cannot sign in to `claude.ai`, so there is no shared sign-in surface to restrict. If you allow automatic application updates, keep the update hosts listed in the network-requirements table reachable.
  </Accordion>

  <Accordion title="Is web fetch always checked against the allowlist?">
    Yes. Every web page fetch is checked against your egress allowlist before the request is made, and redirects are re-checked against the allowlist on each hop. See [Web search and web fetch](/docs/third-party/claude-desktop/web-tools). Do not rely on this allowlist alone to restrict access to your private network; see **Allowed network hosts** on the [Config](/docs/government/config/settings#allowed-network-hosts) page.
  </Accordion>

  <Accordion title="Can all traffic route through a single proxy?">
    Yes. Both the desktop application and the sandbox honor the operating system's proxy settings, including PAC URLs, and route all outbound traffic through your proxy. TLS inspection at your proxy should work; validate this in your environment before rollout. See [Network proxy](/docs/third-party/claude-desktop/network-proxy) for details. Web search requests pass through your proxy to the Claude for Government service, and the service's onward call to the search provider originates from inside the FedRAMP High boundary.
  </Accordion>
</AccordionGroup>

### Approvals and Auto mode

By default, Claude for Government prompts the user for file writes outside the attached workspace, connector actions, and each web search. In Cowork, shell commands run without a prompt because they run inside the sandbox virtual machine. Web page fetches run without a prompt in both Chat and Cowork and are checked against the egress allowlist described above. Administrators can require a prompt on every shell command or fetch with the **Require approval** sub-settings on the [Config](/docs/government/config/settings#tool-and-connector-cards) page. In Chat, every shell command prompts regardless. The reduced-approval option in Claude for Government is Auto mode, which is off by default and can be enabled through device managed configuration (it is not a setting on the Config page). Cowork does not offer a Bypass Permissions mode.

<AccordionGroup>
  <Accordion title="Can write and send actions be gated behind approval?">
    Yes. Administrators can set each built-in and connector tool to **ask** (approval required on every call), **allow** (pre-approved), or **blocked** (removed entirely), and users cannot override those settings. For the Microsoft 365 connector, certain irreversible write tools (sending or forwarding mail, and creating or updating calendar events) are fixed to **ask** and cannot be changed to **allow**. See the [Configuration reference](/docs/third-party/claude-desktop/configuration) for the per-tool policy options.
  </Accordion>

  <Accordion title="Can Auto mode be disabled when a sensitive connector is attached?">
    Auto mode can be disabled by policy, but not conditionally based on which connector is attached. The Auto mode policy, delivered through device managed configuration, controls whether users see Auto mode in the Cowork and Code permission selectors, and it defaults to off in Claude for Government. You can combine that policy with per-tool policies (setting a sensitive connector's tools to **ask** or **blocked**) to achieve a similar effect.
  </Accordion>

  <Accordion title="Can individual shell commands be allowlisted enterprise-wide?">
    No. Policy controls whole tools (shell, file read, web fetch, and so on) but not individual commands within a tool. In Chat, each shell command prompts the user with no standing approval. For analyses that take many steps, Cowork runs shell commands in the sandbox without prompting; you make Cowork available to members under **Product availability** on the [Config](/docs/government/config/settings#product-availability) page.
  </Accordion>

  <Accordion title="Can users suppress approval prompts with an Always allow choice?">
    For most tools, users who see an approval prompt can choose **Always allow**, which suppresses that prompt for them going forward. Administrators can remove that option by setting the tool's policy to **ask**, which forces a fresh prompt on every call. The create-artifact prompt and code execution in Chat are exceptions: neither offers a standing approval. See the [Configuration reference](/docs/third-party/claude-desktop/configuration) for the full tool-policy options.
  </Accordion>

  <Accordion title="Why does Chat prompt on every analysis step?">
    Chat is designed for user-guided interaction, so each analysis step (including opening an attachment in the sandbox) runs as a shell command with a one-time Allow or Deny prompt and no standing approval. For analyses that take many steps, Cowork runs the same work in the same sandbox without a prompt on each shell command. See [Chat in Claude Desktop](/docs/third-party/claude-desktop/chat).
  </Accordion>
</AccordionGroup>

### Connectors

In Claude for Government, connectors fall into three main categories: built-in tools (Web search, Web fetch, and Shell commands), the built-in Microsoft 365 connector, and connectors an administrator adds on the Connectors card of the [Config](/docs/government/config/settings#tool-and-connector-cards) page.

<AccordionGroup>
  <Accordion title="Where do connectors run, and where are tokens stored?">
    Connectors are called from the desktop application, outside the sandbox. The built-in Microsoft 365 connector and administrator-added connectors call their endpoints directly from the user's device, through the system proxy where one is configured. OAuth tokens for both are stored encrypted on each user's device using operating system encryption (macOS Keychain on Mac, DPAPI on Windows). For administrator-added connectors, the bearer header entered on the Config page is delivered to each user's desktop. A plugin package can include skills, slash commands, sub-agents, and hooks, which run on the member's machine. The Config page asks the administrator to confirm trust before adding a plugin that declares components that can run code on the member's machine, for example hooks or an MCP server. A plugin's declared local MCP server is disabled in Claude for Government and does not run, and a connector declared inside a plugin package does not become available as an organization connector unless the plugin was delivered through device management. End users cannot add their own connectors. End users can upload their own plugin files in Claude Desktop; a user-uploaded plugin's skills, commands, sub-agents, and hooks run on that user's machine, and any connector it declares does not become available as an organization connector. Administrators distribute plugins to members on the Config page with a per-plugin choice of automatic installation or member opt-in. See [Connectors](/docs/government/connectors/overview) and the Plugins card under [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards).
  </Accordion>

  <Accordion title="Do connectors follow the sandbox egress allowlist?">
    No. The built-in Microsoft 365 connector calls Microsoft Graph directly from the user's device; see the [Microsoft 365 connector](/docs/government/connectors/microsoft-365) page. Administrator-added connectors connect directly from the user's device to the address configured for that connector. Both pass through the system proxy where one is configured. Web search is a built-in tool rather than a connector and routes through the Claude for Government service; see [Web search and web fetch](#web-search-and-web-fetch) below.
  </Accordion>

  <Accordion title="Can artifacts be blocked from calling connectors?">
    Artifacts honor the same per-tool approval policy as Claude's direct connector calls: tools set to **blocked** are refused and tools set to **ask** require user confirmation. There is no single switch to disable artifact-to-connector calls while keeping connectors available to Claude directly.
  </Accordion>
</AccordionGroup>

### Telemetry and logging

In Claude for Government, Anthropic-bound error and usage telemetry is always disabled. The OpenTelemetry export to your own collector is a separate setting and sends data only to the endpoint you configure.

<AccordionGroup>
  <Accordion title="Is there an inline DLP or inspection point?">
    No. Claude for Government does not include an inline content-inspection or DLP gate. The available inspection points are your own network proxy, which sees all endpoint traffic, and the desktop's OpenTelemetry export, which sends tool-call metadata (tool name, connector, outcome, duration, and approval status) to your collector for after-the-fact review. You set the OpenTelemetry endpoint with **Telemetry endpoint** on the [Config](/docs/government/config/settings#telemetry-endpoint) page. The **Telemetry content capture** setting on the [Config](/docs/government/config/settings#telemetry-content-capture) page adds prompt, response, and tool content to the export for the categories you select, and nothing is selected by default. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry).
  </Accordion>

  <Accordion title="What is logged for connector actions and outbound requests?">
    Chat, Cowork, and Code sessions write a local audit log to the user's disk recording tool invocations, permission decisions, and file operations; that log never leaves the device. The desktop can also export OpenTelemetry events to a collector you specify: tool name, connector, outcome, duration, and approval status are sent. Prompt text, Claude's responses, and tool inputs and results are included only for the categories you select in the **Telemetry content capture** setting on the [Config](/docs/government/config/settings#telemetry-content-capture) page. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for what the export can include. Server-side, the [Compliance API](/docs/government/org-admin/compliance-api) records identity and configuration events but never tool calls or conversation content.
  </Accordion>
</AccordionGroup>

### Data storage and retention

In Claude for Government, conversation content stays on the user's device. If you select content categories in the **Telemetry content capture** setting on the [Config](/docs/government/config/settings#telemetry-content-capture) page, Claude Desktop also sends the selected prompt, response, and tool content to your own OpenTelemetry collector, and never to Anthropic. Model requests are proxied through the Claude for Government service to the model endpoint inside the FedRAMP High boundary, and the service records only per-request metadata, not content.

<AccordionGroup>
  <Accordion title="Can Anthropic view conversations?">
    No. Chat transcripts are stored on the user's workstation, and the Claude for Government service does not log request or response bodies. Inference requests pass through the service to the model endpoint but are not retained. If you select content categories in the **Telemetry content capture** setting on the [Config](/docs/government/config/settings#telemetry-content-capture) page, Claude Desktop also sends the selected content to your own OpenTelemetry collector, and never to Anthropic. See [User identity and local data](/docs/third-party/claude-desktop/data-storage) for where conversation content is stored.
  </Accordion>

  <Accordion title="Where on the device is conversation content stored?">
    Conversation content lives under the owner-only application data directory (`%LOCALAPPDATA%\Claude-3p` on Windows, `~/Library/Application Support/Claude-3p` on macOS). User-visible outputs such as artifacts are written separately to the user files directory (default `~/Claude`). See [User identity and local data](/docs/third-party/claude-desktop/data-storage) for the full list of what each location holds.
  </Accordion>

  <Accordion title="Is local history kept separate for each organization?">
    No. Claude Desktop keeps conversation history in the application data directory of the operating system account in use on the device, and it does not divide that history by the Claude for Government organization or tenant the user signs in to. A user who is moved to another organization, or who signs in to a second tenant from the same operating system account, sees the same conversations and projects as before. Each operating system account's application data directory is written with owner-only permissions, so other accounts on the device cannot read it, and [Removing data](/docs/third-party/claude-desktop/data-storage#removing-data) describes how to clear it. In the folder layout that [User identity and local data](/docs/third-party/claude-desktop/data-storage) describes, Claude for Government uses a single fixed organization ID. The Claude Desktop [configuration reference](/docs/third-party/claude-desktop/configuration#deploymentorganizationuuid) lists a `deploymentOrganizationUuid` key that separates local data by organization in other deployments. That key does not apply to Claude for Government, so leave it out of your [configuration profile](/docs/government/deploy-desktop/configure#deploy-to-your-fleet).
  </Accordion>

  <Accordion title="Where are files added to a project stored, and are they indexed?">
    A project in Claude for Government is stored in the application data directory on the user's own device, together with any instructions, links, and folder references the user adds to it. Files added to a project stay on the user's local disk; there is no service-side project store, and files are not vectorized or indexed. Claude reads them directly from disk on demand with its file tools. Content Claude reads from those files is handled like the rest of the conversation: inference requests pass through the Claude for Government service to the model endpoint but are not retained. See [Desktop and filesystem access](/docs/third-party/claude-desktop/local-access).
  </Accordion>

  <Accordion title="Can the local data location be changed for backup or sync?">
    No. The location is fixed to the per-user application data directory, and the application avoids the roaming profile because the sandbox image cache can be large. Chat history exists only on the device that created it, so back up the application data directory through your endpoint management tools if you need to preserve it. Artifacts and project folders are separate locations on the same device; see the question above. See [User identity and local data](/docs/third-party/claude-desktop/data-storage) for the folder layout.
  </Accordion>
</AccordionGroup>

### Web search and web fetch

<AccordionGroup>
  <Accordion title="How does web search reach the internet?">
    Web search is operated by Anthropic inside the Claude for Government FedRAMP High boundary, and the search provider's API is the one case where traffic egresses that boundary. Before search is enabled, an administrator must acknowledge a disclosure covering this data flow when enabling the **Web search** card on the [Config](/docs/government/config/settings#tool-and-connector-cards) page. By default, users approve each query before it is sent, and Claude transforms it into a generic, de-identified search request and shows the user the exact text. Anthropic has a zero-data-retention agreement with the search provider. The [Web search and web fetch](/docs/third-party/claude-desktop/web-tools) page covers how web search is configured in other Claude Desktop deployments; the Claude for Government search path described here is specific to this deployment.
  </Accordion>

  <Accordion title="How do administrators enable web search?">
    Web search is built in and does not require obtaining a separate connector. An organization owner opens the [Config](/docs/government/config/settings#tool-and-connector-cards) page, finds the **Web search** card, turns it on, and acknowledges the data-flow notice. The **Require approval for each search** setting is on by default.
  </Accordion>

  <Accordion title="Why does Chat's web fetch fail with an empty allowlist?">
    Chat includes a web fetch tool, and every fetch is checked against the same egress allowlist that governs Cowork. With the allowlist empty or unset, a fetch to anything other than the Claude for Government service address (or, when configured, the **Telemetry endpoint** collector host) returns an error. Add hosts to **Allowed network hosts** on the [Config](/docs/government/config/settings#allowed-network-hosts) page to let Chat fetch from them, or turn off the **Web fetch** card on the same page if you prefer Claude not to see the tool. See [Web search and web fetch](/docs/third-party/claude-desktop/web-tools).
  </Accordion>
</AccordionGroup>

### Chat and Cowork differences

<AccordionGroup>
  <Accordion title="Are projects available in both Chat and Cowork?">
    Yes. Chat and Cowork share one list of projects, and users can start a Chat conversation or a Cowork session inside a project. A project in Claude for Government is stored only on the user's device. There is no service-side project store, and projects are not shared between users. A Chat conversation inside a project does not gain access to the project's folders, while Cowork sessions in a project use the same execution model as the rest of Cowork. Chat conversations in a project can read the project's [memory](/docs/third-party/claude-desktop/data-storage#memory) but cannot add to or change it. See [Data storage and retention](#data-storage-and-retention) for where project contents are stored.
  </Accordion>

  <Accordion title="Are artifacts available in Chat?">
    Yes. Artifacts are available in both Chat and Cowork. Claude creates an artifact by calling a tool when the output suits an interactive view, and the artifact opens in a side panel next to the conversation. Artifacts do not depend on the sandbox, so they remain available in Chat even when **Advanced file analysis** is disabled.
  </Accordion>
</AccordionGroup>

## More information

Assurance materials including the security architecture overview, SOC 2 Type 2 report, and penetration testing summary are available on request through the [Anthropic Trust Center](https://trust.anthropic.com).
