> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app configuration

> Build, test, and export a Claude Desktop on 3P configuration from inside the app, with validation and per-provider guidance

The in-app configuration window is the recommended way to configure Claude Desktop for third-party inference. It validates values as you enter them, shows exactly which fields your inference provider requires, tests the connection against your endpoint, and computes the network egress allowlist for your settings.

## Open the configuration window

From the macOS menu bar (or on Windows, the application menu ☰ in the top-left of the sign-in screen), go to **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure Third-Party Inference…**.

If you turn on Developer mode while the app is running a third-party configuration, it stays on across restarts. If you turned it on before that, the **Developer** menu is gone once the app relaunches into a third-party configuration, for example after **Apply Changes**. Go to **Help → Troubleshooting → Enable Developer Mode** again, and it stays on from then on. If the configuration sets [`developerModeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#developermodeenabled) to `false`, neither that item nor the **Developer** menu appears.

To turn Developer mode off again, go to **Developer → Open Developer Config File**, change `"allowDevTools": true` to `false` in the file that opens (or delete the file), save it, then quit and reopen Claude Desktop. The **Developer** menu is gone on the next launch.

![Claude Desktop in-app configuration window with the sidebar of setting groups on the left and the Connection form on the right.](https://mintcdn.com/claude-ai/kVj7_7KF4fI3bEAn/images/third-party/in-app-configuration-window.png?fit=max\&auto=format\&n=kVj7_7KF4fI3bEAn\&q=85\&s=c3f15a85dea85082bc6dbc9459e6a974)

The in-app configuration window, showing the Connection section for a gateway provider.

The sidebar groups settings the same way the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) does. Fill in **Connection** first, then work down through the sections your deployment needs.

## Apply locally or export for a fleet

Use **Apply Changes** to write the configuration to this device only and relaunch into it. This is the [single-machine setup](https://claude.com/docs/third-party/claude-desktop/installation.md#single-machine-setup) path for evaluation and pilots.

Use the **Export** menu to generate deployment artifacts for a fleet:

| Export option | Use with |
| - | - |
| `.mobileconfig` profile | Jamf or any macOS MDM |
| `.reg` policy file | Intune, Group Policy, or any Windows MDM |
| ADMX template (`.zip`) | Intune or Group Policy; a schema-only template, you enter values in the management console |
| Profile Manifest (`.plist`) | A profile editor such as iMazing Profile Editor or ProfileCreator; a schema-only template, you enter values there to build the profile that your MDM installs |
| JSON config | The response body for a [bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md), a file to import into the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#start-from-an-existing-configuration-file), or a file that a user loads with **Import configuration…** on a device without MDM |
| Firewall allowlist (`.txt`) | Your firewall or network team |

See [Deploy with MDM](https://claude.com/docs/third-party/claude-desktop/mdm.md) or [Deploy with a bootstrap server](https://claude.com/docs/third-party/claude-desktop/bootstrap.md) to distribute what you exported.

When a managed profile on the device sets any key other than the [app-behavior keys and the keys treated like them](https://claude.com/docs/third-party/claude-desktop/mdm.md#update-keys-and-managed-precedence), the window opens in read-only mode and shows the deployed values. Its **Export** menu offers **JSON config (redacted)**, a file to [import into the Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md#start-from-an-existing-configuration-file). This option requires Claude Desktop 4.23118.0 or later. Author new configurations from a device without such a profile.

### Set up a device without MDM

Export **JSON config** and send the file to the user. In the [configuration window](#open-the-configuration-window) on their device, the user opens the configuration picker at the top right, chooses **Import configuration…**, selects the file, clicks **Apply Changes**, and then clicks **Relaunch now**. The exported file holds your API key in plain text, so handle it as you handle the key.

> [!WARNING]
>
> Don't set up another device or user account by copying files from the `configLibrary/` directory, for example in a setup script, a disk image, or a profile template. Where the app can use the device's secure storage, the API key in those files is encrypted for the OS user account that saved it. On another device or account, the app then shows the banner **Claude can’t read your saved key** and starts no sessions until the user enters the key and restarts the app. Before Claude Desktop 4.4212.0, the files held the key unencrypted. See [Unreadable saved API keys](https://claude.com/docs/third-party/claude-desktop/data-storage.md#unreadable-saved-api-keys).
