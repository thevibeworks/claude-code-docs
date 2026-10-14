# Deploy Claude Desktop for Windows

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer MSIX packages for Windows deployments via Microsoft Intune, SCCM, Group Policy, or PowerShell.

## Installation requirements

- For individual installations with full feature support including Claude Cowork, administrator privileges are required. Users will see a Windows UAC prompt during installation. Users without admin access can still install Claude, but Cowork on desktop will not be available. Access the user-friendly installer from **[our download page](https://claude.com/download)**.

- For silent deployment without user interaction, use the MSIX package directly with your enterprise management tool.

## Cowork desktop requirements

Claude Desktop for Windows requires the **[Virtual Machine Platform](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)** to use Cowork. You can automate installation of this feature via most endpoint management solutions, but you may also run the following command to install it manually:

```
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart
```

The feature takes effect after the machine restarts. The `-NoRestart` flag suppresses the automatic restart for silent deployment, so schedule one through your management tool.

## Download

- **[Claude MSIX (x64)](https://claude.ai/api/desktop/win32/x64/msix/latest/redirect)**

- **[Claude MSIX (arm64)](https://claude.ai/api/desktop/win32/arm64/msix/latest/redirect)**

## Installation commands

The Claude MSIX is packaged as a per-user application. `Add-AppxPackage` registers it for the current user only, while `Add-AppxProvisionedPackage` stages it machine-wide so it's available to every user on the device, including standard users without admin rights.

### Install for single user

```
Add-AppxPackage -Path "Claude.msix"
```

For more details, see Microsoft's **[Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps)** documentation.

### Install for all users (provisions machine-wide)

```
Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"
```

For more details, see Microsoft's **[Add-AppxProvisionedPackage](https://learn.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2022-ps)** documentation.

## Deploy via MDM

**Important:** Because the MSIX is packaged per-user, uploading it to Intune as a line-of-business (LOB) app installs it in user context rather than machine-wide. The install fails for standard users without admin rights. For machine-wide deployment, run `Add-AppxProvisionedPackage` against the package instead—either pre-stage it on target devices before users sign in, or deliver the command through a Win32 app or PowerShell script wrapper. Intune LOB can't run this command on your behalf.

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

- **[Microsoft Intune](https://docs.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-intune)**

- **[Microsoft Endpoint Configuration Manager (SCCM)](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-mem-adminconsole)**

- **[Group Policy Software Installation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)**

- **[Deployment Image Servicing and Management (DISM.exe)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism?view=windows-10)**

- **[PowerShell Scripts](https://learn.microsoft.com/en-us/windows/msix/desktop/powershell-msix-cmdlets)**

### Manage auto-updates alongside your MDM

By default, Claude Desktop checks for updates approximately every four hours and applies them automatically—independent of the version your MDM has assigned. To keep the in-app updater and your MDM from conflicting, choose one of these approaches before you deploy:

**Option 1: Your MDM manages versions.** Set the `disableAutoUpdates` policy to `1` and push new MSIX builds through your MDM on your own schedule. See **[Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)** for the policy location.

**Option 2: Claude Desktop manages versions.** Leave `disableAutoUpdates` unset. Deploy the MSIX once via a Win32-wrapped `Add-AppxProvisionedPackage` install, then use a custom detection script that checks `Get-AppxPackage -Name Claude` for a version greater than or equal to the one you provisioned. This keeps your MDM reporting **Installed** after the app self-updates.

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see **[Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)**.

---

## Troubleshooting

### MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

### "The parameter is incorrect" after MDM deployment

This usually means the in-app updater and your MDM have both registered the package, leaving duplicate entries under the `Claude` package family. Pick a single update owner using the guidance in **[Manage auto-updates alongside your MDM](#h_1297fb34f3)** above.

### Install fails: "Administrator access is required to install Claude with full features," or error 0x80073D28

Claude Desktop for Windows includes a background service that runs Cowork's virtual machine, and Windows registers that service only when Claude is installed with administrator privileges.

- **Claude Setup (ClaudeSetup.exe):** if the administrator prompt is declined or the elevated install fails, Claude Setup shows "Administrator access is required to install Claude with full features" and exits. Users who can't get administrator approval are offered the choice to install Claude without Cowork instead.

- **MSIX deployed per user (for example, an Intune line-of-business app assigned to users, or Add-AppxPackage run without administrator rights):** Windows refuses the install with error 0x80073D28.

The MSIX package never installs without its Cowork service: either it registers completely, or the install fails.

To fix it, run Claude Setup with administrator approval on that device, or provision Claude machine-wide in system context with `Add-AppxProvisionedPackage`, as described in **[Deploy via MDM](#h_124a24d394)**.

### “Installation failed: AddPackage failed with HRESULT 0x80073CF6”

This error means a previous Claude install or update on the device didn’t finish cleanly and left the package partially registered, so Windows can’t register the new one.

**Warning:** On a device in this state, the installer’s automatic repair removes the previous package’s local app data, including app settings, the saved sign-in, and any files saved only inside Cowork. Chat history and files in the user’s own folders aren’t affected.

To resolve it:

1. Restart the device. A pending removal often completes on restart.

2. Run the current installer elevated.

3. If the install fails again with the same error, **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support)** and include the `ClaudeSetup.log` file from the user’s Temp folder. IT needs to recover the device in system context, and Support will provide the steps.

### Cowork reports missing HCS services or virtualization errors

If Cowork fails to start with an error like "Missing HCS services: HNS, vmcompute, vfpext," the Virtual Machine Platform service stack isn't registered on the machine, even if Claude installed successfully.

**To diagnose and fix:**

Check whether the feature is enabled and its services exist:

```
Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform Get-Service vmcompute, hns
```

If the feature shows as disabled or the services are missing, re-enable it:

```
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All
```

Restart the machine using **Restart**, not shut down and power on. With Windows Fast Startup enabled, a shutdown cycle can leave the virtualization services uninitialized.

If VMware or VirtualBox is also installed on the machine, confirm the Windows hypervisor is set to launch at boot. Run `bcdedit` from an elevated prompt and check that `hypervisorlaunchtype` reads `Auto`. If it doesn't, run `bcdedit /set hypervisorlaunchtype auto` and restart.

**Note:** Virtual machines and VDI environments without nested virtualization aren't supported, so Cowork can't run on these hosts. To see exactly which check is failing, go to **Help > Troubleshooting > Show Logs** in Claude Desktop and review `supported-features-info.json`.