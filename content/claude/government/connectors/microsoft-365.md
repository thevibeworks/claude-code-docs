> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up the Microsoft 365 connector

> Register an application in your Microsoft Entra tenant so that Claude Desktop can read your agency's Outlook, OneDrive, SharePoint, and Teams content on each member's behalf.

> **Who this is for:** Organization owners and tenant administrators who want Claude to reach their agency's Microsoft 365 content, and who can register an application in Microsoft Entra ID (or can work with someone who can).

The Microsoft 365 connector lets Claude read and search your agency's Outlook mail and calendar, OneDrive and SharePoint files, and Teams chat from Claude Desktop. The connector runs locally on each member's machine: when a member signs in with their own Microsoft account, Claude Desktop calls Microsoft Graph directly from their device, so those calls and the member's sign-in tokens stay between their device and Microsoft and never pass through any Anthropic service. What Claude reads into a conversation is then handled like anything else the member sends to Claude.

Because each member signs in individually, Claude can only reach content that the signed-in member can already open in Microsoft 365. Your existing Microsoft 365 permissions, sharing rules, and Conditional Access policies apply unchanged.

Setup has two parts. First, someone with administrator access in Microsoft Entra ID registers an application in your Microsoft tenant. Then you enter that application's details on the **Microsoft 365** card on the [Config](/docs/government/org-admin/configuration) page.

## Before you start

You need someone with the **Cloud Application Administrator**, **Application Administrator**, or **Global Administrator** role in your Microsoft Entra tenant. That person registers the application and approves the Microsoft Graph permissions for your whole tenant. If that isn't you, send them the [Register an application in Microsoft Entra](#register-an-application-in-microsoft-entra) section below; you can fill in the Config page form once they send you the two IDs.

Open the [Config](/docs/government/org-admin/configuration) page in another tab and find the **Microsoft 365** card. You'll paste two values from Entra into it at the end.

## Register an application in Microsoft Entra

<Steps>
  <Step title="Create the app registration">
    1. In the [Microsoft Entra admin center](https://entra.microsoft.com), open **App registrations** from the left navigation and select **+ New registration**.
    2. Enter a display name, for example "Claude for Government Microsoft 365".
    3. Under **Supported account types**, choose **Single tenant only - \{your organization}**. Older versions of the portal label this option **Accounts in this organizational directory only (Single tenant)**.
    4. Leave **Redirect URI** blank for now, and select **Register**.
  </Step>

  <Step title="Add the redirect URIs">
    On the new application's left navigation, go to **Manage** > **Authentication** and open the **Redirect URI configuration** tab (on older versions of the portal, select **+ Add a platform** instead).

    1. Select **Add redirect URI**. In the sidebar, choose the **Mobile and desktop applications** card (the Windows, UWP, and Console card, not the iOS/macOS card).
    2. Leave the suggested redirect URIs unchecked. In the **Custom redirect URIs** box, enter `http://localhost` and select **Configure**.
    3. Close the sidebar. A **Mobile and desktop applications** section now appears on the Authentication page. Select **Edit** on that section, and in the empty box that appears under `http://localhost`, enter each of the two broker redirect URIs below (a new empty box appears after you enter each one). Replace `APPLICATION_CLIENT_ID` with the **Application (client) ID** shown on the application's Overview page, and select **Save** at the top when done.

    ```text theme={null}
    ms-appx-web://Microsoft.AAD.BrokerPlugin/APPLICATION_CLIENT_ID
    msauth.com.anthropic.claudefordesktop://auth
    ```

    The `http://localhost` URI is the standard loopback redirect for browser sign-in. When a member signs in through their browser, Microsoft Entra sends the response to a temporary listener on the member's own machine, so it never leaves the device. The other two URIs let Claude Desktop sign in through the operating system's account broker on Windows and macOS devices that meet the [brokered sign-in requirements](#brokered-sign-in-requirements). Brokered sign-in carries the device-identity claim that Conditional Access policies such as **Require compliant device** evaluate, so register all three now even if you are not sure you need them.

    <Note>
      All three URIs must be under **Mobile and desktop applications**, not **Web**. Registering them as **Web** causes Entra error `AADSTS50011` at sign-in. After you save, Entra may display the `msauth.com.anthropic.claudefordesktop://auth` URI under a separate **iOS/macOS** section. That's expected, since both sections are public-client platforms. To double-check, open **Manage** > **Manifest** and confirm the three URIs appear under `publicClient.redirectUris` rather than `web.redirectUris`. If the list also contains `msauth.com.anthropic.claudefordesktop.helper://auth`, remove that entry. Claude Desktop does not use it.
    </Note>
  </Step>

  <Step title="Allow public client flows">
    Still under **Authentication**, find **Allow public client flows** (on the **Settings** tab under **Web and SPA settings**, or under **Advanced settings** on older versions of the portal), set it to **Yes**, and select **Save**.

    This tells Microsoft Entra that the application runs on end-user devices and does not hold a secret. Claude Desktop signs in as a public client with no client secret, and with this setting off, brokered sign-in on managed devices fails with Entra error `AADSTS7000218`.

    <Warning>
      Setting **Allow public client flows** to **Yes** also permits the device-code sign-in flow, which attackers can abuse for phishing. To close that path, apply a tenant Conditional Access policy that blocks the device-code authentication flow. Scope the policy to **All resources**, not to this app registration, because Conditional Access evaluates the resource a token is requested for rather than the requesting client.
    </Warning>
  </Step>

  <Step title="Add and approve Microsoft Graph permissions">
    On the application's left navigation, go to **Manage** > **API permissions**.

    1. Select **+ Add a permission** > **Microsoft Graph** > **Delegated permissions**.
    2. Add `User.Read` (under **User**) and `offline_access` (under **OpenId permissions**). `User.Read` is usually already listed on a new application, so leave it in place. The connector always requests these two at sign-in, so they must be approved regardless of what you select under **Access** later.
    3. Add every permission you plan to select under **Access** on the Config page. At minimum, add the eight Default permissions (`Mail.Read`, `Mail.Read.Shared`, `Calendars.Read`, `Calendars.Read.Shared`, `Files.Read.All`, `Sites.Read.All`, `Chat.Read`, `OnlineMeetings.Read`), since those are pre-selected on the Config page. See [Choose which Microsoft 365 permissions to allow](#choose-which-microsoft-365-permissions-to-allow) for what each one does and for the optional write permissions.
    4. Select **Add permissions**.
    5. Select **Grant admin consent for \{your tenant name}** and confirm.

    The **Grant admin consent** step approves these permissions once for every member of your Microsoft tenant, so individual members are not asked to approve them again when they sign in. Until you complete this step, members see Entra error `AADSTS65001` at sign-in (or, on tenants that allow members to approve permissions themselves, a per-member consent prompt).

    <Note>
      A delegated permission lets the application act on a member's behalf, limited to whatever that member can already do. It does not let Claude see content the member cannot see. For example, granting `Files.Read.All` lets Claude read files the signed-in member can open, not every file in your tenant.
    </Note>
  </Step>

  <Step title="Copy the two IDs">
    On the application's **Overview** page, copy the **Application (client) ID** and the **Directory (tenant) ID**. You'll paste both into the Config page when you [configure the connector](#configure-the-connector-on-the-config-page).
  </Step>
</Steps>

### If your Microsoft tenant is in a US Government cloud

Microsoft 365 GCC (the standard Government Community Cloud) uses the commercial Microsoft Entra service, so follow the steps above unchanged and leave **Azure cloud** set to **Commercial** when you [configure the connector on the Config page](#configure-the-connector-on-the-config-page).

GCC High and DoD tenants use the Azure Government cloud instead. Register the application at `https://entra.microsoft.us` (or `https://portal.azure.us`) rather than `entra.microsoft.com`, and select the matching **Azure cloud** value when you [configure the connector on the Config page](#configure-the-connector-on-the-config-page). Claude Desktop then signs in at `login.microsoftonline.us` and calls `graph.microsoft.us` (or `dod-graph.microsoft.us` for DoD) instead of the commercial hosts.

### Allow outbound network access

The connector calls Microsoft directly from each member's device, so devices need outbound HTTPS access to the Microsoft Entra and Microsoft Graph hosts for your cloud.

| Azure cloud            | Sign-in host                | Microsoft Graph host     |
| ---------------------- | --------------------------- | ------------------------ |
| Commercial             | `login.microsoftonline.com` | `graph.microsoft.com`    |
| US Government GCC-High | `login.microsoftonline.us`  | `graph.microsoft.us`     |
| US Government DoD      | `login.microsoftonline.us`  | `dod-graph.microsoft.us` |

No outbound access to any Anthropic host is needed for the connector's Microsoft 365 calls.

## Configure the connector on the Config page

On the [Config](/docs/government/org-admin/configuration) page, expand the **Microsoft 365** card and fill in the form.

| Field           | What to enter                                                                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tenant ID**   | The **Directory (tenant) ID** from the application's Overview page.                                                                                                                                                                                                                   |
| **Client ID**   | The **Application (client) ID** from the application's Overview page.                                                                                                                                                                                                                 |
| **Azure cloud** | **Commercial** for most tenants, including Microsoft 365 GCC. Choose **US Government GCC-High** or **US Government DoD** only if your Microsoft tenant is in one of those clouds.                                                                                                     |
| **Access**      | The Microsoft Graph permissions the connector requests when a member signs in. The standard read-only permissions are already selected; add or remove permissions as needed. See [Choose which Microsoft 365 permissions to allow](#choose-which-microsoft-365-permissions-to-allow). |

Save the card. The connector reaches each member's Claude Desktop the next time it starts or the member signs in to Claude for Government. Members who already have Claude Desktop open are prompted to relaunch the next time the app checks for changes, which it does about every 30 minutes, and the connector appears after the relaunch.

## Choose which Microsoft 365 permissions to allow

The **Access** picker controls which Microsoft Graph delegated permissions Claude Desktop requests when a member signs in. The permissions marked **Default** below are already selected when you first open the card and give read-only access to the member's mail, calendar, files, sites, Teams chat, and online meetings. Add write or administrator-approval permissions if you need them, or clear read permissions you do not want. At least one permission must be selected.

Whatever you select here must also be added and approved on the Entra app registration (step 4 above). Keep the two lists in sync. Claude Desktop also always requests `User.Read` and `offline_access`. These two do not appear in the picker, but they must still be approved on the Entra app registration.

### Read access

| Permission                        | What it lets Claude do                                                      |
| --------------------------------- | --------------------------------------------------------------------------- |
| `Mail.Read` (Default)             | Read the member's mail                                                      |
| `Mail.Read.Shared` (Default)      | Read mail in mailboxes shared with the member                               |
| `Calendars.Read` (Default)        | Read the member's calendar events                                           |
| `Calendars.Read.Shared` (Default) | Read events on calendars shared with the member and find free meeting times |
| `Files.Read.All` (Default)        | Read files the member can open in OneDrive and SharePoint                   |
| `Sites.Read.All` (Default)        | Read SharePoint site content the member can open                            |
| `Chat.Read` (Default)             | Read the member's Teams chats                                               |
| `OnlineMeetings.Read` (Default)   | Read the member's online meetings                                           |
| `MailboxSettings.Read`            | Read the member's mail rules and automatic-reply settings                   |

### Read access requiring administrator approval

These two permissions always require the **Grant admin consent** step in Entra, regardless of your tenant's user-consent policy. Until that step is done, sign-in fails for every member when either permission is requested.

| Permission                         | What it lets Claude do                                |
| ---------------------------------- | ----------------------------------------------------- |
| `ChannelMessage.Read.All`          | Include Teams channel messages in chat search results |
| `OnlineMeetingTranscript.Read.All` | Read meeting transcripts                              |

### Write access

Write permissions let Claude take actions in Microsoft 365 on the member's behalf, such as sending mail, creating calendar events, and editing files. Members approve each write action in Claude Desktop before it runs. The connector is read-only unless you select at least one of these.

| Permission                  | What it lets Claude do                                                                                                                                                                                            |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Mail.Send`                 | Send mail, send drafts, and forward mail on the member's behalf. Forwarding and sending drafts also use a mail read permission (any of `Mail.Read`, `Mail.Read.Shared`, or `Mail.ReadWrite`) for pre-send checks. |
| `Mail.ReadWrite`            | Create, edit, and delete drafts; trash, restore, and delete messages; apply and remove labels on messages                                                                                                         |
| `Calendars.ReadWrite`       | Create, update, delete, and respond to calendar events                                                                                                                                                            |
| `Files.ReadWrite.All`       | Create, edit, rename, move, copy, and delete files and folders the member can edit in OneDrive and SharePoint                                                                                                     |
| `Sites.ReadWrite.All`       | Additional SharePoint write access beyond files. No Claude action requires this permission; `Files.ReadWrite.All` covers file actions in both OneDrive and SharePoint.                                            |
| `ChatMessage.Send`          | Send messages in the member's existing Teams chats                                                                                                                                                                |
| `ChannelMessage.Send`       | Post messages to Teams channels                                                                                                                                                                                   |
| `Chat.Create`               | Start new Teams chats                                                                                                                                                                                             |
| `MailboxSettings.ReadWrite` | Manage the member's labels, mail rules, and automatic replies                                                                                                                                                     |

<Note>
  Removing a permission from the **Access** picker changes what Claude Desktop requests the next time a member signs in, but it does not revoke permissions that Microsoft Entra has already approved for the application. To revoke a permission entirely, remove it in the Entra admin center under **Enterprise applications** > your application > **Permissions**.
</Note>

## What members see

After you save the card, **Microsoft 365** appears under **Settings** > **Connectors** in each member's Claude Desktop. The member selects **Connect** and signs in with their Microsoft work account. On devices that meet the brokered sign-in requirements below, this opens the operating system's account picker; otherwise, it opens the default browser. Once connected, Claude can search and read the member's Microsoft 365 content in conversations.

Sign-in tokens are stored encrypted on the member's device and persist across restarts, so members are not asked to sign in again each session. Selecting **Disconnect** deletes the connector's stored tokens from the device. On the brokered sign-in path, the device's work or school account is managed by the operating system and remains after Disconnect, so selecting **Connect** again can re-acquire tokens without a fresh prompt. To end a member's access entirely, revoke the member's sessions in the Entra admin center (revocation takes effect once the member's current access token expires), or remove the account from the device in Windows Settings (**Accounts** > **Access work or school**) or macOS Company Portal.

### Brokered sign-in requirements

If your Conditional Access policies require a compliant or managed device, sign-in must carry a device-identity claim. Brokered sign-in provides that claim directly; browser sign-in provides it only when the browser itself is integrated with device identity (for example, Microsoft Edge signed in with the work account on an Entra-joined Windows device, or a macOS browser with the Enterprise SSO integration deployed). Without the claim, members see Entra error `AADSTS53000` or `AADSTS53003` when Claude calls Microsoft 365.

Brokered sign-in requires the broker redirect URIs from step 2, **Allow public client flows** set to **Yes** (step 3), and the following on each device:

| Platform | Broker availability requirements                                                                                                                                                                                                                                                                                                                                     |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows  | Windows 10 or Windows Server 2019 or later. The device is joined or registered to Entra ID (Entra joined, Entra hybrid joined, or Entra registered).                                                                                                                                                                                                                 |
| macOS    | macOS 10.15 or later. The Mac is enrolled in device management and registered in Entra ID. **Intune Company Portal** is installed, and an **Extensible SSO** configuration profile of type **Redirect** pointed at the Microsoft Enterprise SSO plug-in is deployed through device management. The broker is unavailable without Company Portal and the SSO profile. |

When the broker is unavailable, Claude Desktop falls back to browser sign-in automatically and stays on browser sign-in until Claude Desktop restarts.

When the broker is available, it carries the device claim, and Conditional Access then evaluates that claim against your policy, so the device must also satisfy whichever grant control your policy applies: marked compliant in Intune (or by a partner compliance integration that reports to Intune) for a **Require compliant device** policy, or hybrid joined for a **Require Entra hybrid joined device** policy. A device with a working broker that does not satisfy the policy still fails with `AADSTS53000` or `AADSTS53003`.

## Common problems

| What the member sees                                                                           | What it means                                                                                                                                                                                                                                                    | How to fix it                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entra error `AADSTS50011` at sign-in                                                           | One of the redirect URIs from step 2 is missing from the app registration, was entered with a different value, or was added under the **Web** platform instead of **Mobile and desktop applications**. The error message names the URI that Claude Desktop sent. | Compare it with step 2 and add or correct that URI under **Mobile and desktop applications**.                                                                                                                                                                                                                                                        |
| Entra error `AADSTS900971` at sign-in on macOS                                                 | No redirect URI is registered for macOS brokered sign-in.                                                                                                                                                                                                        | Add `msauth.com.anthropic.claudefordesktop://auth` under **Mobile and desktop applications** (step 2).                                                                                                                                                                                                                                               |
| Entra error `AADSTS65001` at sign-in                                                           | The Microsoft Graph permissions have not been approved for the tenant, or a permission the connector requests is not listed under the app registration's **API permissions** (so **Grant admin consent** never covered it).                                      | Confirm that every permission selected under **Access** on the Config page, plus `User.Read` and `offline_access`, is listed under the app registration's **API permissions**. Add any that are missing, then select **Grant admin consent** (step 4).                                                                                               |
| A Microsoft consent prompt appears at sign-in even though you selected **Grant admin consent** | Same cause as `AADSTS65001` above, on a tenant that allows members to approve permissions themselves.                                                                                                                                                            | See the `AADSTS65001` row above.                                                                                                                                                                                                                                                                                                                     |
| Entra error `AADSTS7000218` at sign-in                                                         | **Allow public client flows** is set to **No** on the app registration.                                                                                                                                                                                          | Set it to **Yes** (step 3).                                                                                                                                                                                                                                                                                                                          |
| Entra error `AADSTS53000` or `AADSTS53003` when Claude calls Microsoft 365                     | A Conditional Access policy requires a compliant or managed device, and either sign-in fell back to the browser because brokered sign-in is not available, or the device does not satisfy the policy's grant control.                                            | Meet the [brokered sign-in requirements](#brokered-sign-in-requirements) for the member's platform, confirm the device satisfies whichever grant control your policy applies (marked compliant, or hybrid joined), and restart Claude Desktop. On macOS, the most common broker cause is a missing Company Portal install or Extensible SSO profile. |
| Entra error `AADSTS700016` at sign-in                                                          | The **Client ID** or **Tenant ID** on the Config page does not match an application in the selected **Azure cloud**.                                                                                                                                             | Re-check the Client ID and Tenant ID against the application's Overview page, and confirm that **Azure cloud** matches the cloud where you registered the application.                                                                                                                                                                               |
| Sign-in or Claude's Microsoft 365 calls fail with a network error and no `AADSTS` code         | The member's device cannot reach the Microsoft Entra or Microsoft Graph host for your Azure cloud.                                                                                                                                                               | Allow outbound HTTPS to the hosts listed under [Allow outbound network access](#allow-outbound-network-access).                                                                                                                                                                                                                                      |
| A tool returns a permission error                                                              | The Microsoft Graph permission that tool needs is not approved on the app registration, or is not selected under **Access**.                                                                                                                                     | Add the permission in both places and select **Grant admin consent** again.                                                                                                                                                                                                                                                                          |

## Things to know

* Read and write permissions are separate per Microsoft 365 service. You can approve read broadly while limiting write to specific services or none at all by selecting only the permissions you want under [Choose which Microsoft 365 permissions to allow](#choose-which-microsoft-365-permissions-to-allow).
* The **Access** selection applies to everyone who receives this connector card. There is no separate per-group write toggle inside the card. To give different groups different permissions, set the card at the group scope on the Config page; see [Group-specific settings](/docs/government/config/overview#group-specific-settings).
