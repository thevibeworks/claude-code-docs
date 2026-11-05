# Enterprise configuration for Claude Desktop

Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

On the Enterprise plan, owners can set several of these controls in Organization settings (beta), with no MDM tool. See **[Manage Claude Desktop from Organization settings](#h_21135034c8)**.

**Note:** Enterprise policy controls at the user-machine level will override the in-app **[allowlist](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)**. If you want to use the allowlist, ensure `isDesktopExtensionEnabled` and `isDesktopExtensionDirectoryEnabled` are not set to "false" so the allowlist can populate the available registry.

---

## macOS enterprise configuration

Deploy configuration settings through your MDM solution using configuration profiles. Claude Desktop reads preferences from the domain `com.anthropic.claudefordesktop`. Use your MDM tool (Jamf Pro, Kandji, Microsoft Intune) to deploy configuration profiles to target machines or user groups. Configuration profiles allow you to manage Claude Desktop settings centrally without user intervention.

**Configuration profile tools:**

- Built-in MDM profile editors (Jamf Pro, Kandji, Intune)

- **[ProfileCreator](https://github.com/profileCreator/ProfileCreator/)** - Profile management

- **[iMazing Profile Editor](https://imazing.com/profile-editor)** - Configuration profiles

---

## Windows enterprise configuration

Deploy configuration settings through your enterprise management solution using **[Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)** or Intune policies. Settings can be configured at machine-wide (HKLM) or per-user (HKCU) level. Machine-level settings take priority over user-level settings when both are configured.

```
# Set machine-wide settings (recommended)
New-Item -Path "HKLM:\SOFTWARE\Policies\Claude" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "disableAutoUpdates" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "autoUpdaterEnforcementHours" -Value 72 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionDirectoryEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isLocalDevMcpEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isClaudeCodeForDesktopEnabled" -Value 1 -Type DWord
```

---

## Enterprise policy options

| **Key**                              | **Type**        | **Default**  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------ | --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `allowedWorkspaceFolders`            | string[] (JSON) | Unrestricted | Filepath or filepaths the user can mount to Cowork<br>Enterprise plan: also available in Organization settings.                                                                                                                                                                                                                                                                                                                        |
| `autoUpdaterEnforcementHours`        | Integer (1-72)  | 72           | Hours before forcefully restarting Claude to apply a prepared update<br>Enterprise plan: also available in Organization settings.                                                                                                                                                                                                                                                                                                      |
| `disableAutoUpdates`                 | Boolean         | false        | Disable automatic updates. Set this when your MDM manages Claude Desktop versions; leave unset to let the app self-update after a one-time provisioned install. See **[Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)**.<br>Enterprise plan: also available in Organization settings.                                                                           |
| `effortLevel`                        | string          | null         | Sets the default effort level (`low`, `medium`, `high`, `xhigh`, or `max`) for Claude Code sessions in Claude Desktop. The managed value applies fresh at the start of every session, even if someone changed the effort level from the picker in an earlier session. Requires Claude Desktop version 1.25927.0 or later. Doesn't apply to Cowork sessions in Claude Desktop.                                                          |
| `forceLoginOrgUUID`                  | string / array  | null         | Require login to belong to a specific organization. Accepts a single UUID string, which also pre-selects that organization during login, or an array of UUIDs where any listed organization is accepted without pre-selection. Login fails if the authenticated account does not belong to a listed organization. To list more than one organization, see **[Set forceLoginOrgUUID for multiple organizations](#h_403de560dd)** below. |
| `isClaudeCodeForDesktopEnabled`      | Boolean         | true         | Enable Claude Code access in desktop                                                                                                                                                                                                                                                                                                                                                                                                   |
| `isDesktopExtensionEnabled`          | Boolean         | true         | Enable/disable extensions<br>Enterprise plan: also available in Organization settings.                                                                                                                                                                                                                                                                                                                                                 |
| `isDesktopExtensionDirectoryEnabled` | Boolean         | true         | Enable extension directory access<br>Enterprise plan: also available in Organization settings.                                                                                                                                                                                                                                                                                                                                         |
| `isLocalDevMcpEnabled`               | Boolean         | true         | Enable local MCP servers<br>Enterprise plan: also available in Organization settings.                                                                                                                                                                                                                                                                                                                                                  |
| `secureVmFeaturesEnabled`            | Boolean         | true         | Enable **[Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)** access in desktop                                                                                                                                                                                                                                                                                                                     |
| `coworkEDRIntegration`               | string          | Not set      | Full path of your EDR vendor's signed sensor package on the user's computer (beta). If it isn't set, no package is installed. On Windows, set this under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude`.                                                                                                                                                                                                                                |
| `coworkEDRIntegrationVendor`         | string          | Not set      | Your EDR vendor's ID, in lowercase. On Windows, set this under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude`. Learn more about **[running your EDR sensor in Claude Cowork](https://support.claude.com/en/articles/17828685-run-your-endpoint-detection-and-response-edr-sensor-in-claude-cowork)**.                                                                                                                                   |

---

## Manage Claude Desktop from Organization settings (beta)

On the Enterprise plan, owners can set these Claude Desktop controls in Organization settings (beta), with no MDM tool needed, unless you need what an MDM key adds.

- **Turn on “Limit Claude Desktop to allowed organizations (shadow IT)” under “Security” in [Organization settings > Organization and access](https://claude.ai/admin-settings/organization):** After a member signs in to your organization in Claude Desktop on a computer, the app on that computer blocks personal accounts and other organizations you haven't allowed, starting the next time it opens. To block them before anyone signs in, set `forceLoginOrgUUID` through MDM.

  - **Limitations:** This block isn’t permanent. It ends if a member doesn’t use your organization on that computer for 30 days, and anyone using the computer can remove it. If you allow more than one organization, set the same list of allowed organizations in each organization.

- **Turn off “Auto-updates” in [Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities):** Claude Desktop stops checking for and downloading updates. Users can still update from the app menu, and a downloaded update still installs.

- **Allow workspace folders in [Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities):** Choose “Allow only the folders on the list,” or turn it off to allow none. Mark a folder “Read only” and Claude’s file tools can’t change files there.

  - **Limitations:** “Read only” covers Claude’s file tools only. In the Code tab, commands, MCP servers, and hooks can still change those folders and reach others, and it’s ignored on folders holding Claude Desktop’s own data, such as a home folder. It doesn’t apply over SSH to Windows. Each computer uses its own OS list, and SSH sessions use the list of the computer they start from. WSL and localhost SSH are blocked when folders are limited. Missing folders aren’t created.

- **Turn off “Allow local MCP servers” ([Organization settings > Plugins > Connectors](https://claude.ai/admin-settings/connectors)):** Local MCP servers that users add don’t start. Desktop extensions can still run local servers, so also choose “Block all desktop extensions” to stop those.

- **Choose “Block all desktop extensions” ([Organization settings > Plugins > Connectors](https://claude.ai/admin-settings/connectors)):** Installed extensions stop working and none can be installed.

If a policy on the computer sets the matching key, the policy wins on that computer, even if it’s less strict. For Auto-updates, `autoUpdaterEnforcementHours` counts too. These settings follow the account, so they don’t apply to a personal account. These settings need Claude Desktop 4.29.0 or later.

---

## Set `forceLoginOrgUUID` for multiple organizations

To accept more than one organization, set `forceLoginOrgUUID` to a JSON array of organization UUIDs, saved as a single string value.

**Windows**

Use a string value (REG_SZ) whose data is the JSON text. Don’t use a multi-string value (REG_MULTI_SZ).

```
New-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Claude' -Name forceLoginOrgUUID
-PropertyType String -Value '["<uuid-1>","<uuid-2>"]' -Force
```

**macOS**

In your configuration profile for the `com.anthropic.claudefordesktop` domain, set the key as a string that contains the JSON text:

```
<key>forceLoginOrgUUID</key>
<string>["<uuid-1>","<uuid-2>"]</string>
```

Claude Desktop reads this setting when it launches. After you change it, quit and reopen Claude Desktop. To check the value the app read, go to **Help > Troubleshooting > Generate Diagnostic Report**.