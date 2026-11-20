# Set up computer use for Team and Enterprise plans

Computer use lets Claude see a user's screen and work in the desktop apps they allow. Claude clicks and types like you would on Claude Desktop. This article explains how admins can turn computer use on for your organization, limit it to certain users, restrict it to specific apps, and manage it with device management (MDM).

Computer use is in beta on Team and Enterprise plans, and it's off by default. This is rolling out to organizations gradually.

## Availability

Computer use works only in the new Claude experience, which is available where the **Chat and Cowork unified** capability is turned on. There, users can use it from:

- **Claude Desktop**, on macOS 14 or later and Windows.

- **Claude on the web and Claude Mobile**, if your organization's **Computer access** setting is on, with a computer that has Claude Desktop open.

It doesn't work in tasks started with the separate "Cowork" option, or in Claude Code. Owners can learn more in the article that applies to your plan:

- **[Set up and manage the new unified Claude experience for your Team organization](https://support.claude.com/en/articles/18342806-set-up-and-manage-the-new-unified-claude-experience-for-your-team-organization)**

- **[Set up and manage the new unified Claude experience for your Enterprise organization](https://support.claude.com/en/articles/17444462-set-up-and-manage-the-new-unified-claude-experience-for-your-enterprise-organization)**

Organizations that can't turn on computer use include those with:

- The HIPAA-ready configuration

- Zero Data Retention (ZDR) for Claude Code

- Customer-managed encryption keys (CMEK)

- FERPA or K-12 settings

**Note:** **Computer use** and **Computer access** are different settings. Computer use lets Claude see the screen and work in apps. Computer access lets users reach their computer from scheduled tasks, Claude on the web, or Claude Mobile.

## Before you turn on computer use

Review **[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)** and keep the following in mind:

- Computer use has no sandbox between Claude and a user's applications. Content on the screen, such as web pages or emails, could cause Claude to take unintended actions.

- Computer use isn't limited to the folders a user has connected. Through the apps a user approves, Claude can open, change, or delete files outside those folders.

- If you **[limit which folders users can connect](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)**, that limit doesn't apply to computer use. Marking a folder "Read only" doesn't apply to computer use either.

- If you're on an Enterprise plan and want to keep computer use from some users, read **Limit computer use to certain users** below before you turn it on.

## Screenshots and your data

Claude takes screenshots to see and navigate the screen, and they're saved with the chat. They can include personal or confidential information. The automated check that reviews Claude's actions can also see the latest screenshot, and Anthropic can keep a copy of it in its record of the check. Your data is handled according to our **[Commercial Terms](https://www.anthropic.com/legal/commercial-terms)** and **[Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum)**.

## Enable or disable computer use

To turn computer use on or off for your organization:

1. Sign in to Claude as an Owner or Primary Owner.

2. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

3. Make sure **Chat and Cowork unified** is on. Computer use doesn't work without it.

4. Under **Claude Desktop**, find **Computer use** and turn it on or off.

5. On Enterprise plans, if a list of roles opens, clear every role that shouldn't have computer use, then click "Turn on."

Only an Owner or Primary Owner can change this setting. If the setting isn't there or can't be turned on, it hasn't reached your organization yet, or your organization can't have it. See **Availability** above.

When you turn computer use off, the change can take about an hour, sometimes longer, to reach each user's Claude Desktop. Until then, Claude can still see their screen and use the apps they allow.

To keep computer use off on chosen computers, see **Manage computer use with device management (MDM)** below.

## Limit computer use to certain users (Enterprise plans)

Computer use is a capability in custom roles, like other features. Team plans have no custom roles, so the setting covers every user. Learn more in **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

### Users with a built-in role

Users whose role is User, Admin, Owner, or Primary Owner get computer use as soon as you turn it on. To keep it from a user, set their role to "Custom," and wait 15 minutes before you turn it on.

### Users with a custom role

To use computer use, a user on a custom role needs a role that includes the **Chat and Cowork unified** capability.

When you turn computer use on, your custom roles are listed, usually already selected. Clear every role that shouldn't have it.

You can't clear a role set to "All capabilities" in the list. To keep computer use from that role:

1. Before you turn computer use on, set the role's **Capability access** to "Only selected."

2. Turn off **Computer use** on the role.

3. Wait 15 minutes.

4. Turn computer use on for your organization, and clear that role in the list.

### Change role access later

Once computer use is on, change which custom roles have it with "Edit role access," beside the setting, or on each role's **Capabilities** tab. Taking it away can take about an hour, sometimes longer, to reach each user's Claude Desktop.

## Restrict computer use to specific apps

The **App access** setting has two lists of apps. Only an Owner or Primary Owner can change it.

- **Block these apps:** The apps on your block list, such as a password manager, are denied.

- **Allow only these apps:** Every app is denied except the ones on your allow list. Users still approve each app.

Claude can't use a denied app through computer use, except as described in **Enter an app's ID** and **What the block and allow lists don’t cover**. Choosing a list in the dropdown puts it in use, and the other list stays saved. An empty allow list goes into use when you add its first app. The apps you list are sent to your users' computers. Claude Desktop doesn't show users the list, but someone could find it, so don't include anything confidential.

While an allow list is in use, users who aren't on the latest Claude Desktop lose computer use until they update.

### Add or remove apps

To add apps:

1. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.

2. Under **Claude Desktop**, find **App access**, below **Computer use**.

3. Choose "Block these apps" or "Allow only these apps."

4. Click "Add app."

5. Under **Apps**, search the list of common apps and select each app you want to add. If an app isn't in the list, type its ID in the box **App IDs, one per line**, below the search.

6. Click "Done."

If you open **Organization settings** in Claude Desktop, the search also lists most of the apps on your computer. Those apps are denied, or allowed, only on computers with the same operating system.

To remove an app, click the trash icon at the end of its row. If you remove the last app from an allow list in use, Claude can't use any app.

### Check an app

To check an app:

1. Wait a minute after your change.

2. Quit and reopen Claude Desktop on a computer that has the app.

3. In a new chat, ask Claude for the app by its exact name. See **What changes for your users** below.

A new version of an app can change its ID.

### Enter an app's ID

- **Mac:** Enter the bundle ID, such as `com.microsoft.Excel`.

- **Windows:** Enter the program's file name, such as `excel.exe`, or a Microsoft Store app's Application User Model ID (AUMID).

Nothing checks that a typed ID names a real app.

On Windows, some apps start from one program and show their window from another. For example, LibreOffice's window belongs to soffice.bin. Put the window's file name on your block list. Otherwise, Claude can still use the app once a user approves it, even if it passes the check above.

### What changes for your users

If a user asks for a denied app, Claude says that their organization blocked it, or that it isn't on their organization's list. Earlier approvals of the app stop counting. Claude can't click or type in the app, or see it in screenshots, except as described in **Enter an app's ID** and **What the block and allow lists don’t cover**.

Adding or removing an app, or switching lists, can take about an hour, sometimes longer, to reach each user's Claude Desktop. Until then, Claude can still use an app that you've just denied.

### What the block and allow lists don’t cover

- **Claude's other tools:** This includes Claude in Chrome, the built-in browser, Claude Code, and desktop extensions. Denying Google Chrome stops only computer use in Chrome.

- **Other accounts:** If a user switches Claude Desktop to a personal account or to another organization, your block and allow lists don't apply there.

- **Websites and browser extensions:** The block and allow lists don't cover these, such as a password manager's extension, in a browser that a user approves.

- **Remote desktops and virtual machines:** The block and allow lists don't cover apps inside a remote desktop or virtual machine window that a user approves.

- **Indirect effects on a denied app:** Claude can affect a denied app through what it does in apps a user approves.

- **Text copied from a denied app:** Claude can read it, such as by pasting it into an app that a user approves.

- **Recordings made with Record a skill:** A recording includes every app on the screen, including denied ones.

- **Windows notifications:** A denied app's Windows notifications stay visible in screenshots, and so do the Start menu, search, and File Explorer.

## What your users need

Users need the latest Claude Desktop, open on the computer Claude will use. Each user turns on **Enable computer use** there, on each computer and for each account, if it isn't already on.

### Claude on the web and Claude Mobile

Using computer use from Claude on the web or Claude Mobile also needs your organization's **Computer access** setting to be on. The chat must also be connected to the computer Claude will use. Users pick the computer when asked, or in Claude on the web, under "+" > "Devices."

### macOS permissions

On macOS, computer use needs the Accessibility and Screen Recording permissions. In **System Settings > Privacy & Security**, they appear as:

- **Accessibility** (**Device Control and Data Access** on macOS 27)

- **Screen & System Audio Recording**

Users who aren't administrators on their Mac may need an administrator's name and password to turn them on. To prepare both with your MDM tool, see **Prepare macOS permissions** below.

## Manage computer use with device management (MDM)

If you manage your users' computers with an MDM tool such as Jamf or Intune, you can keep computer use off on chosen computers. You can also make it easier to set up on a Mac. On Windows, computer use needs no operating system permission, so there's nothing to prepare.

### Keep computer use off on a computer

To keep computer use off on a computer, whichever account is signed in, set Claude Desktop's policy key computerUseEnabled to false. To learn how to deploy policy keys, see **[Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667)**.

**Before you deploy the key**

The key needs Claude Desktop 5.1231.0 or later. Update Claude Desktop on all computers first. An older version doesn't know the key, so it doesn't turn computer use off.

**Warning:** On Windows, an older version rejects the whole policy if `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude` holds no setting that it knows (for example, if `computerUseEnabled` is the only value there). It then ignores settings saved in the app on that computer, such as a third-party inference setup, until you update the app or remove the key.

**Important:** Deploy the key at the computer level, not to a user. A user-level setting covers only that one user of the computer.

**macOS**

Set the key as a Boolean in a configuration profile for the preference domain `com.anthropic.claudefordesktop`. For example:

`<key>computerUseEnabled</key><false/>`

If a computer-level profile for that domain is installed, Claude Desktop ignores user-level profiles for the domain, or will after an update. If your other Claude settings are in a user-level profile, put them in the computer-level profile too.

**Windows**

Set the key as a `DWORD` value of `0` under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude`. For example, in PowerShell run as administrator, run these commands:

```
New-Item -Path "HKLM:\SOFTWARE\Policies\Claude" -ErrorAction SilentlyContinue
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "computerUseEnabled" -Value 0 -Type DWord
```

No user-level Claude setting is read while `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Claude` holds any value. If your other Claude settings are under `HKEY_CURRENT_USER`, move them to `HKEY_LOCAL_MACHINE` as well.

**Check that the key works**

Claude Desktop reads the key only when it starts, so the key takes effect once Claude Desktop has been quit and reopened. Closing its window isn't enough.

To check a computer, open **Settings** in Claude Desktop on the computer. The **Enable computer use** toggle is grayed out, and when you hover over it, it says: "Your organization has turned off computer use on this computer. Ask your IT administrator for access."

If Claude Desktop finds a Claude policy on the computer but can't read it, it turns computer use off too. Users then see: "Couldn’t check whether computer use is allowed on this computer. Quit and reopen Claude to try again. If it’s still off, ask your IT administrator."

**What the key doesn't cover**

The key doesn't cover Record a skill, Claude in Chrome, the built-in browser, Claude Code in a terminal, local MCP servers, or desktop extensions. The key changes how Claude Desktop behaves. It isn't a lock against someone who can change the app or the computer's settings.

Like any Claude Desktop policy key, `computerUseEnabled` makes Claude Desktop treat the computer as managed, whether it's true or false. On a managed computer, users can't choose a release channel, and Claude Desktop stops reading users' own values for other app behavior settings. On a managed Windows computer, Code tab sessions in WSL are refused unless `disableWslSessions` is set to false under `HKEY_LOCAL_MACHINE`.

### Prepare macOS permissions

On macOS, the two permissions that computer use needs, Accessibility and Screen Recording, are granted to Claude Desktop itself, not to a Claude account. Claude Desktop's quick entry feature uses them too. See **What your users need** above.

You can prepare both with a Privacy Preferences Policy Control (PPPC) payload. It needs user-approved MDM enrollment, and it can't be installed by hand. Add one entry for Claude Desktop. The helper tools inside the app use its permissions.

- **Identifier:** `com.anthropic.claudefordesktop`

- **Identifier type:** `bundleID`

- **Code requirement:** `identifier "com.anthropic.claudefordesktop" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = Q6L2SF6YDW`

To check the code requirement, run `codesign -d -r - /Applications/Claude.app` on a Mac that has Claude Desktop. The text after `designated =>` should match the code requirement above.

| **Permission**                  | **PPPC service** | **What to set**                                                                                                | **What it does**                                                                                                                                               |
| ------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accessibility                   | Accessibility    | `Authorization` set to `Allow`                                                                                 | On macOS 14 to 26, the user isn't asked and can't change it.                                                                                                   |
| Screen & System Audio Recording | ScreenCapture    | `Authorization` set to `AllowStandardUserToSetSystemService`, if your users aren't administrators on their Mac | A profile can't turn this permission on. This setting lets users who aren't administrators turn it on themselves, in **System Settings > Privacy & Security**. |

Keep the following in mind:

- If your users aren't administrators on their Mac, allow Accessibility in the profile. `AllowStandardUserToSetSystemService` doesn't work for Accessibility, so without the profile those users may need an administrator's name and password to turn it on.

- If two profiles give Claude Desktop different settings for the same permission, macOS uses the more restrictive one, so a Deny takes precedence.

- If a permission is already granted when a user sets up computer use, Claude Desktop should show it as granted, and the user can skip that step.

- If a user turns on Screen Recording while Claude Desktop is open, they may need to quit and reopen Claude Desktop.

- If a profile that you already deploy denies Accessibility or Screen Recording to Claude Desktop, computer use fails on those Macs. Claude Desktop can't say why. It only shows the permission as not granted.

A Deny also takes the permission away from Claude Desktop's quick entry feature, so it isn't a good way to keep computer use off. Set `computerUseEnabled` to false instead.

Preparing these permissions doesn't turn computer use on.

### What MDM can't do

- **Turn computer use on:** Your organization's **Computer use** setting, the user's role on Enterprise plans, and each user's own switch decide that. Setting `computerUseEnabled` to true does the same for computer use as leaving it unset.

- **Turn on a user's own switch:** Each user turns on **Enable computer use** in Claude Desktop, on each computer and for each account, if it isn't already on.

- **Approve apps for Claude:** Each user approves apps themselves.

- **Turn on Screen & System Audio Recording:** macOS leaves that to the person at the Mac.

## What your users see

Users who can use computer use see this under the **Computer use** heading in **Settings** in Claude Desktop: "For your organization, computer use works in the new Claude experience. It isn’t available in Cowork tasks or Claude Code."

For users who can't turn it on, the toggle is grayed out and says why when they hover over it. For each message and what to do, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)**.