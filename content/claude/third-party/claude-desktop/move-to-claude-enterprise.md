> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate Claude Desktop from a cloud provider to Claude Enterprise

> Migrate Claude Desktop from a cloud provider such as Amazon Bedrock to Claude Enterprise and keep each user's local chats, sessions, projects, tasks, and skills

Move Claude Desktop from your cloud provider, where the app is named Claude (third-party), to Claude Enterprise. After one configuration change, each user's work migrates when they sign in on the same computer.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/YWagxq-iHGacF1MS/images/third-party/diagrams/move-to-claude-enterprise-flow.svg?fit=max&auto=format&n=YWagxq-iHGacF1MS&q=85&s=e6b4faee6754095aede8306ee3ef4207" alt="Flow diagram: IT updates Claude Desktop, turns on two skills settings, and changes the configuration. Cloud provider controls stop applying. Each user signs in to Claude Enterprise. Claude Desktop migrates earlier work (chats, sessions, projects, scheduled tasks), then adds skills, plugins, extensions, and local MCP servers. The user approves tools in scheduled tasks, adds their instructions, and checks their skills." width="1000" height="548" data-path="images/third-party/diagrams/move-to-claude-enterprise-flow.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/YWagxq-iHGacF1MS/images/third-party/diagrams/move-to-claude-enterprise-flow-dark.svg?fit=max&auto=format&n=YWagxq-iHGacF1MS&q=85&s=5d963c2eb678347ecc0be6185ba07b11" alt="Flow diagram: IT updates Claude Desktop, turns on two skills settings, and changes the configuration. Cloud provider controls stop applying. Each user signs in to Claude Enterprise. Claude Desktop migrates earlier work (chats, sessions, projects, scheduled tasks), then adds skills, plugins, extensions, and local MCP servers. The user approves tools in scheduled tasks, adds their instructions, and checks their skills." width="1000" height="548" data-path="images/third-party/diagrams/move-to-claude-enterprise-flow-dark.svg" />

## What is migrated

The migration never changes or deletes the Claude (third-party) data.

**Migrated automatically:**

* Chats, which appear in Cowork
* Cowork sessions and projects, with their folders, except a few broad or network folders
* Code sessions in folders Claude Code trusts
* Scheduled tasks, on or off as before, except Code tasks in untrusted folders
* Local MCP servers and most desktop extensions, as before
* App preferences

**Migrated after one step:**

* Skills, and plugins users uploaded, after the [skills settings](#before-you-begin)
* Personal instructions the account doesn't have yet, after **Add instructions** in **Settings > Import**
* Code sessions in untrusted folders, after the user trusts the folder and adds them in **Settings > Import**

**Not migrated:**

* Remote connectors, and plugins users didn't upload. Set them up again.
* Skills with plugin components or an unreadable header, or over about 10 MB or 200 files
* Scheduled Code tasks in folders Claude Code doesn't trust
* A few broad or network folders, such as the home folder. The user attaches them again.

Migrated sessions stay on the computer and don't sync to claude.ai. Continuing one sends its content to Anthropic, and uploaded skills, added instructions, and MCP tool on/off settings go to the user's account. Claude also sends standard usage data.

## Before you begin

1. **Update first.** Update every computer to the Claude Desktop release of October 15, 2026, or later, before the configuration change, because the migration runs on the version installed when the change arrives.
2. **Turn on the skills settings.** In [**Organization settings > Plugins & skills > Policy**](https://claude.ai/admin-settings/skills?tab=policy), turn on **User-created skills** and **Skill and plugin security scanning**. For custom roles, also give them the skills permissions in [**Organization settings > Roles**](https://claude.ai/admin-settings/roles). Skills need both settings, and plugins need only **User-created skills**.
3. **Replace the controls** listed in [What changes for your security controls](#what-changes-for-your-security-controls).

Special cases:

* If Cowork runs only in its VM sandbox in your organization (for example, because [`requireCoworkFullVmSandbox`](/docs/third-party/claude-desktop/configuration#requirecoworkfullvmsandbox) is enforced), nothing is migrated. Ask your Anthropic account team.
* If your organization needs HIPAA, make it HIPAA-ready before users first sign in. A HIPAA-ready organization migrates no skills, local MCP servers, extensions, plugins, or instructions.
* With the MSIX install on Windows 10 Enterprise LTSC 2021, or Windows 10 older than 21H1, update Claude in place. Uninstalling or resetting it deletes the Claude (third-party) data.

## What changes for your security controls

After the change, most of your cloud provider settings in the [configuration reference](/docs/third-party/claude-desktop/configuration) stop working without warning, even if their keys stay deployed, including permission, plugin, and browser limits. Set up replacements first:

* Cowork's telemetry and network egress: your organization settings.
* Code sessions' telemetry, SSH host limits (any host is allowed until you set a list), and session retention (`cleanupPeriodDays`): Claude Code's managed settings.
* Remote [managed MCP servers](/docs/third-party/claude-desktop/configuration#managedmcpservers): add them as connectors. The Microsoft 365 connector keeps working.

Telemetry opt-outs, the egress list for Code sessions, Cowork's session retention, and locally run managed MCP servers have no replacement. The command sandbox in Code sessions stays on only where [`allowedWorkspaceFolders`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) is set. Migrated plugins aren't scanned. Migrated skills and plugins arrive on or off as before, with their hooks and tool permissions.

## Migrate your fleet

Remove the old keys and set the new one in one change to the policy or profile that carries your Claude settings: an `HKEY_LOCAL_MACHINE` policy on Windows (not `HKEY_CURRENT_USER`), or a [configuration profile](/docs/third-party/claude-desktop/mdm) on macOS.

<Steps>
  <Step title="Remove the cloud provider keys">
    Remove every key that puts the app in third-party mode, such as those that start with `inference` or `bootstrap`. Also remove [`disableDeploymentModeChooser`](/docs/third-party/claude-desktop/configuration#disabledeploymentmodechooser) and [`deploymentOrganizationUuid`](/docs/third-party/claude-desktop/configuration#deploymentorganizationuuid). Leave other keys in place. If your settings come from a [bootstrap server](/docs/third-party/claude-desktop/bootstrap), copy the keys you want to keep into the policy or profile itself.

    The desktop extensions feature is on after the change unless [`isDesktopExtensionEnabled`](/docs/third-party/claude-desktop/configuration#isdesktopextensionenabled) is set to `false`.
  </Step>

  <Step title="Set your organization ID">
    Copy the **Organization ID** from [**Organization settings > Organization and access**](https://claude.ai/admin-settings/organization). Set `importThirdPartyHistoryIntoOrgUUID` to this ID, without braces or quotation marks. To keep Claude on these computers from using another organization or a personal account, where nothing migrates, you can also set `forceLoginOrgUUID` to the same ID. The app then blocks accounts that aren't in that organization.

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
  </Step>

  <Step title="Roll out in stages">
    Deploy to a few computers on each operating system, then to the rest. Send users the [steps for each user](#steps-for-each-user).
  </Step>
</Steps>

Afterward, keep `importThirdPartyHistoryIntoOrgUUID` deployed and keep the Claude (third-party) data. **Settings > Import** needs both. To roll back, restore your earlier configuration. Work done after the migration stays in Claude Enterprise and doesn't appear in Claude (third-party).

If nothing migrates, Claude shows no error on screen. Check that the key arrived as a device policy, that no third-party key remains, and that the user signed in to this organization. The app's `main.log` usually gives the reason.

## Steps for each user

Quit Claude fully, including from the menu bar or system tray, open it again, and sign in to your company's Claude Enterprise organization with the same Windows or macOS account as before. Your chats (now in Cowork), sessions, projects, and scheduled tasks appear, and your Claude (third-party) work isn't changed. On a Mac, allow access to Documents if macOS asks, so that scheduled tasks can migrate. Then:

* If a scheduled task asks to use a tool, choose **Allow for all scheduled runs**.
* In **Settings > Import**, click **Add instructions** for each set of instructions listed, and **Import…** if a skill is missing from **Customize > Skills**.
* Set up remote connectors again, and add any keys or sign-ins your plugins and extensions need.

<Warning>
  Don't click **Remove** on the home page banner or in **Settings > Import**. It deletes your migrated chats, sessions, and projects, including any work you added after the migration.
</Warning>
