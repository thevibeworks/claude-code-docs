> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate Claude Desktop from a cloud provider to Claude Enterprise

> Migrate Claude Desktop from a cloud provider such as Amazon Bedrock to Claude Enterprise and keep each user's local chats, sessions, projects, tasks, and skills

Move Claude Desktop from your cloud provider, where the app is named Claude (third-party), to Claude Enterprise. After one configuration change, each user's work migrates when they sign in to Claude Enterprise on the same computer. You choose one option: move everyone to Claude Enterprise, or let each user switch between your cloud provider and Claude Enterprise at sign-in.

![Flow diagram: IT updates Claude Desktop, turns on two skills settings, and changes the configuration. Cloud provider controls don't apply in Claude Enterprise. Each user signs in to Claude Enterprise. Claude Desktop migrates earlier work (chats, sessions, projects, scheduled tasks), then adds skills, plugins, extensions, and local MCP servers. The user approves tools in scheduled tasks, adds their instructions and Cowork memory, and checks their skills.](https://mintcdn.com/claude-ai/1Uf_o4hnNbOJpCy9/images/third-party/diagrams/move-to-claude-enterprise-flow.svg?fit=max\&auto=format\&n=1Uf_o4hnNbOJpCy9\&q=85\&s=7cd669f4802ca30d628f7a3768c1b1f0)

## What is migrated

The migration never changes or deletes the Claude (third-party) data.

**Migrated automatically:**

* Chats, which appear in Cowork
* Cowork sessions and projects, with their folders, except a few system or network folders
* Code sessions in folders Claude Code trusts
* Scheduled tasks, on or off as before, except Code tasks in untrusted folders
* Local MCP servers and most desktop extensions, as before
* App preferences

**Migrated after one step:**

* Skills, and plugins users uploaded, after the [skills settings](#before-you-begin)
* Plugin marketplaces users added over HTTPS from github.com, gitlab.com, bitbucket.org, or a GitHub Enterprise host your organization connected to Claude, after the [skills settings](#before-you-begin). Claude must be able to access the repository. Users then install the plugins they want in **Customize > Plugins**.
* Personal instructions the account doesn't have yet, after **Add instructions** in **Settings > Import**
* Cowork [memory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#memory), after the [memory settings](#before-you-begin) and **Add to memory** in **Settings > Import**. Claude saves what's useful to the user's memory, in its own words. Requires Claude Desktop 4.4212.0 or later.
* Code sessions in untrusted folders, after the user trusts the folder and adds them in **Settings > Import**

**Not migrated:**

* Remote connectors, other plugin marketplaces, and plugins users didn't upload. Set them up again.
* Skills with plugin components or an unreadable header, or over about 10 MB or 200 files
* Scheduled Code tasks in folders Claude Code doesn't trust
* A few system or network folders. The user can attach most of them again.

Migrated sessions stay on the computer and don't sync to claude.ai. Continuing one sends its content to Anthropic. Uploaded skills, added instructions, added Cowork memory, plugin marketplaces, and MCP tool on/off settings go to the user's account. Claude also sends standard usage data.

## Before you begin

1. **Update first.** Update every computer to Claude Desktop 3.1623.0 or later before the configuration change. Each user's work migrates on the version installed when they first open Claude Enterprise after the change. A computer that migrated on an earlier release adds plugin marketplaces after it updates, if `importThirdPartyHistoryIntoOrgUUID` is still deployed, but doesn't add folders to the sessions and projects it already migrated.
2. **Turn on the skills settings.** In [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy), turn on **User-created skills** and **Skill and plugin security scanning**. For custom roles, also give them the skills permissions in [**Organization settings > Roles**](https://claude.ai/admin-settings/roles). Skills need both settings. Plugins and plugin marketplaces need only **User-created skills**.
3. **Turn on memory.** For Cowork to use each user's memory, turn on **Memory** and [**Chat and Cowork unified**](https://support.claude.com/en/articles/17444462-set-up-and-manage-the-new-unified-claude-experience-for-your-enterprise-organization) in [**Organization settings > Capabilities**](https://claude.ai/admin-settings/capabilities). Users turn on memory for themselves in the [steps for each user](#steps-for-each-user).
4. **Replace the controls** listed in [What changes for your security controls](#what-changes-for-your-security-controls).

Special cases:

* If Cowork runs only in its VM sandbox in your organization (for example, because [`requireCoworkFullVmSandbox`](https://claude.com/docs/third-party/claude-desktop/configuration#requirecoworkfullvmsandbox) is enforced), nothing is migrated. Ask your Anthropic account team.
* If your organization needs HIPAA, make it HIPAA-ready before users first sign in. A HIPAA-ready organization migrates no skills, local MCP servers, extensions, plugins, plugin marketplaces, instructions, or Cowork memory.
* With the MSIX install on Windows 10 Enterprise LTSC 2021, or Windows 10 older than 21H1, update Claude in place. Uninstalling or resetting it deletes the Claude (third-party) data.

## What changes for your security controls

While a user works in Claude Enterprise, most of your cloud provider settings in the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) don't apply to them, including permission, plugin, and browser limits. Claude shows no warning, even if the keys stay deployed. Set up replacements first:

* Cowork's telemetry and network egress: your organization settings.
* Code sessions' telemetry, SSH host limits (any host is allowed until you set a list), and session retention (`cleanupPeriodDays`): Claude Code's managed settings.
* Remote [managed MCP servers](https://claude.com/docs/third-party/claude-desktop/configuration.md#managedmcpservers): add them as connectors. The Microsoft 365 connector keeps working.

Telemetry opt-outs, the egress list for Code sessions, Cowork's session retention, and locally run managed MCP servers have no replacement. The command sandbox in Code sessions stays on only where [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) is set. Migrated plugins aren't scanned. Migrated skills and plugins arrive on or off as before, with their hooks and tool permissions.

## Migrate your fleet

Make one change to the policy or profile that carries your Claude settings: an `HKEY_LOCAL_MACHINE` policy on Windows (not `HKEY_CURRENT_USER`), or a [configuration profile](https://claude.com/docs/third-party/claude-desktop/mdm.md) on macOS.

**1. Remove or keep the cloud provider keys**

Choose one option for the keys that connect Claude to your cloud provider, such as keys that start with `inference` or `bootstrap`:

* **To move everyone to Claude Enterprise**, remove those keys. Also remove [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) and [`deploymentOrganizationUuid`](https://claude.com/docs/third-party/claude-desktop/configuration#deploymentorganizationuuid). If your settings come from a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md), copy the keys you want to keep into the policy or profile itself.
* **To let each user switch between your cloud provider and Claude Enterprise**, keep those keys and `deploymentOrganizationUuid`. They must be in the same `HKEY_LOCAL_MACHINE` policy or configuration profile as `importThirdPartyHistoryIntoOrgUUID`, because on Windows Claude [reads one policy location](https://claude.com/docs/third-party/claude-desktop/mdm.md#4-deploy-the-configuration). Make sure [`disableDeploymentModeChooser`](https://claude.com/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) isn't set in the policy or profile, or by your bootstrap server. Claude's welcome screen then offers **Or sign in with Claude.ai**. Your cloud provider settings still apply while a user works with your cloud provider.

Leave other keys in place. In Claude Enterprise, the desktop extensions feature is on unless [`isDesktopExtensionEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#isdesktopextensionenabled) is set to `false`.

**2. Set your organization ID**

For either option, copy the **Organization ID** from [**Organization settings > Organization and access**](https://claude.ai/admin-settings/organization). Set `importThirdPartyHistoryIntoOrgUUID` to this ID, without braces or quotation marks. To keep Claude on these computers from using another organization or a personal account, where nothing migrates, you can also set `forceLoginOrgUUID` to the same ID. The app then blocks Claude accounts that aren't in that organization.

On Windows, in an elevated PowerShell window:

```powershell theme={null}
reg add "HKLM\SOFTWARE\Policies\Claude" /v importThirdPartyHistoryIntoOrgUUID /t REG_SZ /d "YOUR-ORGANIZATION-UUID" /f
# Optional: keeps these computers on this organization
reg add "HKLM\SOFTWARE\Policies\Claude" /v forceLoginOrgUUID /t REG_SZ /d "YOUR-ORGANIZATION-UUID" /f
```

On macOS, in a custom settings payload for the preference domain `com.anthropic.claudefordesktop`:

```xml theme={null}
<key>importThirdPartyHistoryIntoOrgUUID</key>
<string>YOUR-ORGANIZATION-UUID</string>
<!-- Optional: keeps these computers on this organization -->
<key>forceLoginOrgUUID</key>
<string>YOUR-ORGANIZATION-UUID</string>
```

**3. Roll out in stages**

Deploy to a few computers on each operating system, then to the rest. Send users the [steps for each user](#steps-for-each-user).

Afterward, keep `importThirdPartyHistoryIntoOrgUUID` deployed and keep the Claude (third-party) data. **Settings > Import** needs both. Work done in Claude Enterprise stays there and doesn't appear in Claude (third-party).

To roll everyone back, restore your earlier configuration. If users could switch, also set `disableDeploymentModeChooser` to `true` in the policy or profile. Claude then opens with your cloud provider for everyone.

### Nothing migrated

Claude shows no error on screen when nothing migrates. The app's `main.log` usually gives the reason. Check for each of these causes:

* `importThirdPartyHistoryIntoOrgUUID` didn't arrive as a device policy.
* Claude opened with your cloud provider instead of asking the user to sign in to Claude Enterprise. If you removed the cloud provider keys, one remains. If you kept them, the user didn't click **Or sign in with Claude.ai** yet.
* The user signed in to another organization.
* If you kept the cloud provider keys and the welcome screen doesn't show **Or sign in with Claude.ai**, `disableDeploymentModeChooser` is still set. Remove it from the policy or profile, or from what your bootstrap server returns.

## Steps for each user

1. Quit Claude fully, including from the menu bar or system tray. Then open it again.
2. If Claude opens as before instead of asking you to sign in to Claude Enterprise, choose **Sign out** from the account menu. Then, on the welcome screen, click **Or sign in with Claude.ai**. Claude restarts.
3. Sign in to your company's Claude Enterprise organization on this computer, in the same Windows or macOS user account as before. If macOS asks for access to Documents, allow it, so that scheduled tasks can migrate.

Your chats (now in Cowork), sessions, projects, and scheduled tasks appear. Your Claude (third-party) work doesn't change. Then:

* If a scheduled task asks to use a tool, choose **Allow for all scheduled runs**.
* Turn on [memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context#h_c9b905eb3f) in your settings. **Notes from Cowork** shows only while it's on.
* In **Settings > Import**, click **Add instructions** for each set of instructions listed, **Add to memory** until **Notes from Cowork** disappears, and **Import…** if a skill is missing from **Customize > Skills**. Claude may leave out notes on how it should respond, so add those to your [instructions](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features).
* Set up remote connectors and any missing plugin marketplaces again, install the plugins you want in **Customize > Plugins**, and add any keys or sign-ins your plugins and extensions need.

If your IT team kept your cloud provider available, you can switch between it and Claude Enterprise:

* **To go back to your cloud provider**, choose **Log out** from the account menu, then quit Claude and open it again. Claude opens with your cloud provider whenever you start it while logged out of Claude Enterprise. Sign in to your cloud provider again if Claude asks. Your Claude Enterprise work is kept for when you return.
* **To return to Claude Enterprise**, choose **Sign out** from the account menu. Then click **Or sign in with Claude.ai** on the welcome screen. Claude restarts. Sign in, and your work is where you left it. Projects and scheduled tasks that you created with your cloud provider also appear. In **Settings > Import**, click **Import…** to add chats and sessions that you started with your cloud provider, and click **Add to memory** until **Notes from Cowork** disappears.

> [!WARNING]
>
> Don't click **Remove** on the home page banner or in **Settings > Import**. It deletes your migrated chats, sessions, and projects, including any work you added after the migration.
