# Enterprise configuration for Claude Desktop

Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

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
```powershell
# Set machine-wide settings (recommended)
New-Item -Path "HKLM:\SOFTWARE\Policies\Claude" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "disableAutoUpdates" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "autoUpdaterEnforcementHours" -Value 72 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionDirectoryEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isLocalDevMcpEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isClaudeCodeForDesktopEnabled" -Value 1 -Type DWord
```
```

---

## Enterprise policy options

| **Key**                              | **Type**        | **Default**  | **Description**                                                                                                                                                                                                                                                                                                   |
| ------------------------------------ | --------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `allowedWorkspaceFolders`            | string[] (JSON) | Unrestricted | Filepath or filepaths the user can mount to Cowork                                                                                                                                                                                                                                                                |
| `autoUpdaterEnforcementHours`        | Integer (1-72)  | 72           | Hours before forcefully restarting Claude to apply a prepared update                                                                                                                                                                                                                                              |
| `disableAutoUpdates`                 | Boolean         | false        | Disable automatic updates. Set this when your MDM manages Claude Desktop versions; leave unset to let the app self-update after a one-time provisioned install. See **[Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)**.                   |
| `forceLoginOrgUUID`                  | string / array  | null         | Require login to belong to a specific organization. Accepts a single UUID string, which also pre-selects that organization during login, or an array of UUIDs where any listed organization is accepted without pre-selection. Login fails if the authenticated account does not belong to a listed organization. |
| `isClaudeCodeForDesktopEnabled`      | Boolean         | true         | Enable Claude code access in desktop                                                                                                                                                                                                                                                                              |
| `isDesktopExtensionEnabled`          | Boolean         | true         | Enable/disable extensions                                                                                                                                                                                                                                                                                         |
| `isDesktopExtensionDirectoryEnabled` | Boolean         | true         | Enable extension directory access                                                                                                                                                                                                                                                                                 |
| `isLocalDevMcpEnabled`               | Boolean         | true         | Enable local MCP servers                                                                                                                                                                                                                                                                                          |
| `secureVmFeaturesEnabled`            | Boolean         | true         | Enable **[Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)** access in desktop                                                                                                                                                                                                |