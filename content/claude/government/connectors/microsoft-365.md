> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up the Microsoft 365 connector

> Register a Microsoft Entra application for the Microsoft 365 connector in Claude Desktop, choose its read and write permissions, and fix sign-in errors.

> **Who this is for:** Organization owners and tenant administrators who want Claude to reach their agency's Microsoft 365 content, and who can register an application in Microsoft Entra ID (or can work with someone who can).

The Microsoft 365 connector lets Claude Desktop read and search your agency's Outlook mail, calendar, and OneDrive and SharePoint files, and read Teams chats. The connector runs locally on each member's machine: when a member signs in with their own Microsoft account, Claude Desktop calls Microsoft Graph directly from their device, so those calls and the member's sign-in tokens stay between their device and Microsoft and never pass through any Anthropic service. What Claude reads into a conversation is then handled like anything else the member sends to Claude.

Because each member signs in individually, Claude can only reach content that the signed-in member can already open in Microsoft 365. Your existing Microsoft 365 permissions, sharing rules, and Conditional Access policies apply unchanged.

First, someone with administrator access in Microsoft Entra ID registers an application in your Microsoft tenant. Then you enter that application's details on the **Microsoft 365** card on the [Config](https://claude.com/docs/government/org-admin/configuration.md) page. Claude for Microsoft 365, the add-in for Excel, Word, and PowerPoint, is a separate product with [its own setup](https://claude.com/docs/government/deploy-microsoft-365/configure.md).

## Before you start

You need someone with the **Cloud Application Administrator**, **Application Administrator**, or **Global Administrator** role in your Microsoft Entra tenant. That person registers the application and approves the Microsoft Graph permissions for your whole tenant. If that isn't you, send them the [Register an application in Microsoft Entra](#register-an-application-in-microsoft-entra) section below and the permissions you plan to select under [**Access**](#choose-which-microsoft-365-permissions-to-allow); you can fill in the Config page form once they send you the two IDs and tell you which Microsoft cloud the tenant is in.

## Register an application in Microsoft Entra

For the portal screens in more detail, see the first step of [Set up the local connector](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md#set-up-the-local-connector) in the Claude Desktop documentation.

Microsoft 365 GCC (the standard Government Community Cloud) uses the commercial Microsoft Entra service, so follow the steps below unchanged and leave **Azure cloud** set to **Commercial** when you [configure the connector on the Config page](#configure-the-connector-on-the-config-page).

GCC High and DoD tenants use the Azure Government cloud instead. Register the application at `https://entra.microsoft.us` (or `https://portal.azure.us`) rather than `entra.microsoft.com`, and select the matching **Azure cloud** value when you [configure the connector on the Config page](#configure-the-connector-on-the-config-page).

**1. Create the app registration**

1. In the [Microsoft Entra admin center](https://entra.microsoft.com), open **App registrations** from the left navigation and select **+ New registration**.
2. Under **Supported account types**, choose **Single tenant only - \{your organization}**. Older versions of the portal label this option **Accounts in this organizational directory only (Single tenant)**.
3. Leave **Redirect URI** blank for now, and select **Register**.

**2. Add the redirect URIs**

On the **Authentication** page, add these three redirect URIs under **Mobile and desktop applications** (the Windows, UWP, and Console card, not the iOS/macOS card). Replace `APPLICATION_CLIENT_ID` with the **Application (client) ID** shown on the application's Overview page.

```text theme={null}
http://localhost
ms-appx-web://Microsoft.AAD.BrokerPlugin/APPLICATION_CLIENT_ID
msauth.com.anthropic.claudefordesktop://auth
```

The `http://localhost` URI is the standard loopback redirect for browser sign-in. When a member signs in through their browser, Microsoft Entra sends the response to a temporary listener on the member's own machine, so it never leaves the device. The other two URIs let Claude Desktop sign in through the operating system's account broker on Windows and macOS devices that meet the [brokered sign-in requirements](#brokered-sign-in-requirements). Brokered sign-in carries the device-identity claim that Conditional Access policies such as **Require compliant device** evaluate, so register all three now even if you are not sure you need them.

> [!NOTE]
>
> All three URIs must be under **Mobile and desktop applications**, not **Web**. After you save, Entra may display the `msauth.com.anthropic.claudefordesktop://auth` URI under a separate **iOS/macOS** section. That's expected, since both sections are public-client platforms. To double-check, open **Manage > Manifest** and confirm the three URIs appear under `publicClient.redirectUris` rather than `web.redirectUris`. If the list also contains `msauth.com.anthropic.claudefordesktop.helper://auth`, remove that entry. Claude Desktop does not use it.

**3. Allow public client flows**

Still under **Authentication**, set **Allow public client flows** to **Yes**, and select **Save**. Claude Desktop signs in as a public client with no client secret, and with this setting off, brokered sign-in on managed devices fails with Entra error `AADSTS7000218`.

> [!WARNING]
>
> Setting **Allow public client flows** to **Yes** also permits the device-code sign-in flow, which attackers can abuse for phishing. To close that path, apply a tenant Conditional Access policy that blocks the device-code authentication flow. Scope the policy to **All resources**, not to this app registration, because Conditional Access evaluates the resource a token is requested for rather than the requesting client.

**4. Add and approve Microsoft Graph permissions**

Under **API permissions**, add these **Microsoft Graph** **Delegated permissions**, then select **Grant admin consent for \{your tenant name}** and confirm.

* `User.Read` (under **User**) and `offline_access` (under **OpenId permissions**). The connector always requests these two at sign-in, so they must be approved regardless of what you select under **Access** later.
* Every permission you plan to select under **Access** on the Config page. The eight Default permissions (`Mail.Read`, `Mail.Read.Shared`, `Calendars.Read`, `Calendars.Read.Shared`, `Files.Read.All`, `Sites.Read.All`, `Chat.Read`, `OnlineMeetings.Read`) are pre-selected there. See [Choose which Microsoft 365 permissions to allow](#choose-which-microsoft-365-permissions-to-allow) for what each one does.

The **Grant admin consent** step approves these permissions once for every member of your Microsoft tenant, so individual members are not asked to approve them again when they sign in. Until you complete this step, members see Entra error `AADSTS65001` at sign-in (or, on tenants that allow members to approve permissions themselves, a per-member consent prompt).

> [!NOTE]
>
> A delegated permission lets the application act on a member's behalf, limited to whatever that member can already do. It does not let Claude see content the member cannot see. For example, granting `Files.Read.All` lets Claude read files the signed-in member can open, not every file in your tenant.

**5. Copy the two IDs**

On the application's **Overview** page, copy the **Application (client) ID** and the **Directory (tenant) ID**.

### Allow outbound network access

The connector calls Microsoft directly from each member's device, so devices need outbound HTTPS access to the Microsoft Entra and Microsoft Graph hosts for your cloud.

| Azure cloud | Sign-in host | Microsoft Graph host |
| - | - | - |
| Commercial | `login.microsoftonline.com` | `graph.microsoft.com` |
| US Government GCC-High | `login.microsoftonline.us` | `graph.microsoft.us` |
| US Government DoD | `login.microsoftonline.us` | `dod-graph.microsoft.us` |

Downloads of OneDrive and SharePoint files also need access to your Microsoft tenant's SharePoint and OneDrive hosts. For Office documents, see the network hosts step of [Set up the local connector](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md#set-up-the-local-connector) in the Claude Desktop documentation.

No outbound access to any Anthropic host is needed for the connector's Microsoft 365 calls.

## Configure the connector on the Config page

On the [Config](https://claude.com/docs/government/org-admin/configuration.md) page, select the **Integrations** category, expand the **Microsoft 365** card, and fill in the form.

| Field | What to enter |
| - | - |
| **Tenant ID** | The **Directory (tenant) ID** from the application's Overview page. |
| **Client ID** | The **Application (client) ID** from the application's Overview page. |
| **Azure cloud** | **Commercial** for most tenants, including Microsoft 365 GCC. Choose **US Government GCC-High** or **US Government DoD** only if your Microsoft tenant is in one of those clouds. |
| **Access** | See [Choose which Microsoft 365 permissions to allow](#choose-which-microsoft-365-permissions-to-allow). |

Save the card. The connector reaches each member's Claude Desktop the next time it starts or the member signs in to Claude for Government. To turn the connector off, clear both **Tenant ID** and **Client ID** and save the card at each level where it is set. Members who already have Claude Desktop open keep the connector until [the app relaunches](https://claude.com/docs/government/config/overview.md#when-changes-take-effect).

## Choose which Microsoft 365 permissions to allow

The **Access** picker controls which Microsoft Graph delegated permissions Claude Desktop requests when a member signs in. The permissions marked **Default** below are already selected when you first open the card and give read-only access to the member's mail, calendar, files, sites, Teams chat, and online meetings. At least one permission must be selected.

Whatever you select here must also be added and approved on the Entra app registration (step 4 above).

* You can approve read broadly while limiting write to specific services or none at all by selecting only the permissions you want.
* The **Access** selection applies to everyone who receives this connector card. To give different groups different permissions, set the card at the group scope on the Config page; see [Group-specific settings](https://claude.com/docs/government/config/overview.md#group-specific-settings).

### Read access

| Permission | What it lets Claude do |
| - | - |
| `Mail.Read` (Default) | Read the member's mail |
| `Mail.Read.Shared` (Default) | Read mail in mailboxes shared with the member |
| `Calendars.Read` (Default) | Read the member's calendar events |
| `Calendars.Read.Shared` (Default) | Read events on calendars shared with the member and find free meeting times |
| `Files.Read.All` (Default) | Read files the member can open in OneDrive and SharePoint |
| `Sites.Read.All` (Default) | Read SharePoint site content the member can open |
| `Chat.Read` (Default) | Read the member's Teams chats |
| `OnlineMeetings.Read` (Default) | Read the member's online meetings |
| `MailboxSettings.Read` | Read the member's mailbox time zone so that dates in requests follow the member's local time rather than UTC |
| `People.Read` | Search for people by name or email address |
| `Team.ReadBasic.All` | List the member's teams in Microsoft Teams |
| `Channel.ReadBasic.All` | List the channels in the member's teams |

### Read access requiring administrator approval

These two permissions always require the **Grant admin consent** step in Entra, regardless of your tenant's user-consent policy. Until that step is done, sign-in fails for every member when either permission is requested.

| Permission | What it lets Claude do |
| - | - |
| `ChannelMessage.Read.All` | Search messages in the member's Teams chats and channels and, on Claude Desktop 1.49585.0 or later, read channel messages. Without it, `Chat.Read` still lets Claude list and read the member's chats. |
| `OnlineMeetingTranscript.Read.All` | Read meeting transcripts |

### Write access

Write permissions let Claude take actions in Microsoft 365 on the member's behalf, such as sending mail, creating calendar events, and editing files. Members approve each write action in Claude Desktop before it runs. The connector is read-only unless you select at least one of these.

| Permission | What it lets Claude do |
| - | - |
| `Mail.Send` | Send mail, send drafts, and forward mail on the member's behalf. Forwarding and sending drafts also use a mail read permission (any of `Mail.Read`, `Mail.Read.Shared`, or `Mail.ReadWrite`) for pre-send checks. |
| `Mail.ReadWrite` | Create, edit, and delete drafts; trash, restore, and delete messages; apply and remove labels on messages |
| `Calendars.ReadWrite` | Create, update, delete, and respond to calendar events |
| `Files.ReadWrite.All` | Create, edit, rename, move, copy, and delete files and folders the member can edit in OneDrive and SharePoint |
| `Sites.ReadWrite.All` | Additional SharePoint write access beyond files. No Claude action requires this permission; `Files.ReadWrite.All` covers file actions in both OneDrive and SharePoint. |
| `ChatMessage.Send` | Send messages in the member's existing Teams chats |
| `ChannelMessage.Send` | Post messages to Teams channels |
| `Chat.Create` | Start new Teams chats |
| `MailboxSettings.ReadWrite` | Create and delete the member's mail rules, manage labels, and configure automatic replies |

> [!NOTE]
>
> Removing a permission from the **Access** picker changes what Claude Desktop requests the next time a member signs in, but it does not revoke permissions that Microsoft Entra has already approved for the application. To revoke a permission entirely, remove it in the Entra admin center under **Enterprise applications** > your application > **Permissions**.

## What members see

After you save the card, **Microsoft 365** appears under **Customize > Connectors** in each member's Claude Desktop. The member selects **Connect** and signs in with their Microsoft work account. On devices that meet the brokered sign-in requirements below, this opens the operating system's account picker; otherwise, it opens the default browser.

Sign-in tokens are stored encrypted on the member's device and persist across restarts, so members are not asked to sign in again each session. Selecting **Disconnect** deletes the connector's stored tokens from the device. On the brokered sign-in path, the device's work or school account is managed by the operating system and remains after Disconnect, and selecting **Connect** again shows the account picker. To end a member's access entirely, revoke the member's sessions in the Entra admin center or, on the brokered sign-in path, remove the account from the device in Windows Settings (**Accounts > Access work or school**) or macOS Company Portal. On Claude Desktop 1.49585.0 or later, revocation takes effect within minutes where Microsoft's [Continuous Access Evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) applies. Otherwise, it takes effect once the member's current access token expires.

### Brokered sign-in requirements

If your Conditional Access policies require a compliant or managed device, sign-in must carry a device-identity claim. Brokered sign-in provides that claim directly; browser sign-in provides it only when the browser itself is integrated with device identity (for example, Microsoft Edge signed in with the work account on an Entra-joined Windows device, or a macOS browser with the Enterprise SSO integration deployed).

Brokered sign-in requires the broker redirect URIs from step 2, **Allow public client flows** set to **Yes** (step 3), and the following on each device:

| Platform | Broker availability requirements |
| - | - |
| Windows | The device is joined or registered to Entra ID (Entra joined, Entra hybrid joined, or Entra registered). |
| macOS | The Mac is enrolled in device management and registered in Entra ID. **Intune Company Portal** is installed, and an **Extensible SSO** configuration profile of type **Redirect** pointed at the Microsoft Enterprise SSO plug-in is deployed through device management. |

When the broker is unavailable, Claude Desktop falls back to browser sign-in automatically.

## Common problems

| What the member sees | What it means | How to fix it |
| - | - | - |
| **Microsoft 365** is missing from the member's Claude Desktop | The connector is off for the member until a **Microsoft 365** card with a **Tenant ID** and a **Client ID** is in effect for them. | [Fill in the card](#configure-the-connector-on-the-config-page), then restart Claude Desktop. If it is still missing, [look the member up](https://claude.com/docs/government/config/overview.md#comparing-settings-across-levels) to see which level's card they get. |
| Entra error `AADSTS50011` at sign-in | One of the redirect URIs from step 2 is missing from the app registration, was entered with a different value, or was added under the **Web** platform instead of **Mobile and desktop applications**. The error message names the URI that Claude Desktop sent. | Compare it with step 2 and add or correct that URI under **Mobile and desktop applications**. |
| Entra error `AADSTS900971` at sign-in on macOS | No redirect URI is registered for macOS brokered sign-in. | Add `msauth.com.anthropic.claudefordesktop://auth` under **Mobile and desktop applications** (step 2). |
| Entra error `AADSTS65001` at sign-in, or a Microsoft consent prompt even though you selected **Grant admin consent** | The Microsoft Graph permissions have not been approved for the tenant, or a permission the connector requests is not listed under the app registration's **API permissions** (so **Grant admin consent** never covered it). | Confirm that every permission selected under **Access** on the Config page, plus `User.Read` and `offline_access`, is listed under the app registration's **API permissions**. Add any that are missing, then select **Grant admin consent** (step 4). |
| Entra error `AADSTS7000218` at sign-in | **Allow public client flows** is set to **No** on the app registration. | Set it to **Yes** (step 3). |
| Entra error `AADSTS53000` or `AADSTS53003` when Claude calls Microsoft 365 | A Conditional Access policy requires a compliant or managed device, and either sign-in fell back to the browser because brokered sign-in is not available, or the device does not satisfy the policy's grant control. | Meet the [brokered sign-in requirements](#brokered-sign-in-requirements) for the member's platform, confirm the device satisfies whichever grant control your policy applies (marked compliant, or hybrid joined), and restart Claude Desktop. If the error returns, have the member select **Disconnect**, then **Connect**. |
| Entra error `AADSTS700016` at sign-in | The **Client ID** or **Tenant ID** on the Config page does not match an application in the selected **Azure cloud**. | Re-check the Client ID and Tenant ID against the application's Overview page, and confirm that **Azure cloud** matches the cloud where you registered the application. |
| Sign-in or Claude's Microsoft 365 calls fail with a network error and no `AADSTS` code | The member's device cannot reach the Microsoft Entra or Microsoft Graph host for your Azure cloud. | Allow outbound HTTPS to the hosts listed under [Allow outbound network access](#allow-outbound-network-access). |
| A tool returns a permission error | The Microsoft Graph permission that tool needs is not approved on the app registration, or is not selected under **Access**. | Add the permission in both places and select **Grant admin consent** again. |
| Claude finds a OneNote file but cannot open it | Claude cannot open OneNote notebooks or read their pages. | Have the member export the pages from OneNote as a PDF and save the PDF to OneDrive or SharePoint, where Claude can read it. |
