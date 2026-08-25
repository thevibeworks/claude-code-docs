> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Microsoft 365

> Give Claude access to your organization's Outlook, OneDrive, SharePoint, and Teams data through a connector you register in your own Microsoft Entra tenant.

<Info>
  The remote connector is hosted by Anthropic. Data in transit passes through Anthropic's infrastructure, which is based in the United States. Anthropic does not collect or store any data that transits through the server. To keep all Microsoft 365 traffic between the user's device and Microsoft instead, use the [local connector](#local-connector).
</Info>

When Claude Desktop is deployed on third-party inference, Claude can read your organization's Microsoft 365 data (Outlook mail and calendar, OneDrive, SharePoint, and Teams) through a connector registered in your own Microsoft Entra tenant. Two connectors are available: a [remote connector](#remote-connector) hosted by Anthropic, and a [local connector](#local-connector) built into the desktop app.

## Choose a connector

Both connectors provide the same read and search tools; they differ in data path and authentication. Write actions (sending mail, managing drafts and calendar events, and working with files) are available on the local connector when you grant [write scopes](#grant-write-scopes). For write actions on the remote connector, contact your Anthropic representative. Use this table to pick one, then follow that connector's section below.

|                                 | Remote connector                                                         | Local connector                                                       |
| ------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Microsoft 365 data path         | Transits Anthropic's infrastructure (no storage)                         | Stays between the user's device and Microsoft                         |
| App registrations you own       | One desktop client app, plus tenant consent to Anthropic's connector app | One dedicated public client app                                       |
| Token exchange                  | On-behalf-of exchange in Anthropic's infrastructure                      | Tokens acquired and stored on the device                              |
| Allowlisting with Anthropic     | Required (two to three business days)                                    | Not needed                                                            |
| Device egress                   | `login.microsoftonline.com` and the connector host                       | `login.microsoftonline.com` and `graph.microsoft.com`                 |
| Device-based Conditional Access | Not supported (the server-side exchange has no device identity)          | Supported on managed Windows and Mac devices through brokered sign-in |
| Write actions                   | Contact your Anthropic representative                                    | Available with [write scopes](#grant-write-scopes)                    |
| US Government clouds            | Separate connector deployment; contact your Anthropic representative     | Built in; set `azureCloud`                                            |

## Remote connector

When Claude Desktop is deployed on third-party inference, Claude can read your organization's Microsoft 365 data (Outlook mail and calendar, OneDrive, SharePoint, and Teams) through Anthropic's Microsoft 365 connector service. The desktop app authenticates with an app registration you create in your own Microsoft Entra tenant, and the connector service performs the Microsoft Graph calls on the signed-in user's behalf.

Anthropic's connector service receives the desktop's delegated access token on each request and exchanges it on-behalf-of the user for a short-lived Graph token. Neither token is persisted server-side beyond the request, and Anthropic never holds your tenant's client secrets or the user's refresh token (the refresh token stays encrypted on the user's device).

Setup takes about fifteen minutes and requires a Global Administrator or Cloud Application Administrator in your Entra tenant.

### How the connection works

Three applications participate in the sign-in chain. Understanding which one each ID refers to makes the setup steps below easier to follow.

| Application             | Owner                           | Purpose                                                                      |
| ----------------------- | ------------------------------- | ---------------------------------------------------------------------------- |
| Desktop client app      | You (registered in your tenant) | What Claude Desktop signs in as. Public client, PKCE, no secret.             |
| Anthropic connector app | Anthropic (multi-tenant)        | Receives the desktop's token and calls Microsoft Graph on the user's behalf. |
| Microsoft Graph         | Microsoft                       | The Microsoft 365 data APIs.                                                 |

Claude Desktop signs in through your desktop client app, receives a token scoped to the Anthropic connector app, and sends that token to Anthropic's connector service. The connector service exchanges it for a Graph token using the on-behalf-of flow and makes Graph calls as the signed-in user.

### Set up the remote connector

The four steps below cover tenant consent, app registration, allowlisting, and desktop configuration.

<Steps>
  <Step title="Consent the Anthropic connector app into your tenant">
    A tenant administrator must consent to Anthropic's multi-tenant connector app once for the organization. This creates a service principal in your tenant; no secret is exchanged.

    Open the following URL after replacing `YOUR_TENANT_ID` with the Directory (tenant) ID shown in **Entra admin center → Overview**.

    ```text theme={null}
    https://login.microsoftonline.com/YOUR_TENANT_ID/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17
    ```

    The consent screen lists the delegated Microsoft Graph permissions the connector requests. All are read-only:

    | Scope                                     | Purpose                                                     |
    | ----------------------------------------- | ----------------------------------------------------------- |
    | `User.Read`                               | Read the signed-in user's profile                           |
    | `Mail.Read`, `Mail.Read.Shared`           | Read mail in the user's and shared mailboxes                |
    | `Calendars.Read`, `Calendars.Read.Shared` | Read events in the user's and shared calendars              |
    | `Files.Read.All`                          | Read files the user can access in OneDrive and SharePoint   |
    | `Sites.Read.All`                          | Read SharePoint site content the user can access            |
    | `Chat.Read`, `ChatMessage.Read`           | Read Teams chat messages the user can access                |
    | `offline_access`                          | Allow the desktop to refresh its token without re-prompting |

    Review the permissions and select **Accept**.

    <Note>
      FedRAMP and GovCloud deployments use a different connector app ID and a
      different connector service hostname. Contact your Anthropic representative
      for the app ID to use in this URL and in the scope string in step 4, and for
      the connector URL to use in step 4.
    </Note>
  </Step>

  <Step title="Register a desktop client app in your tenant">
    Create the public client that Claude Desktop will sign in as.

    1. In **Entra admin center → App registrations → New registration**, set **Name** to `Claude Desktop` (or your preferred name), set **Supported account types** to *Accounts in this organizational directory only*, and add a **Redirect URI** of platform *Mobile and desktop applications* with the value `http://127.0.0.1/callback`.
    2. Select **Register**, then note the **Application (client) ID** and **Directory (tenant) ID** shown on the overview page.
    3. Under **API permissions → Add a permission → APIs my organization uses**, search for `Anthropic` (or paste the connector app ID from step 1), select **Delegated permissions → access\_as\_user**, then **Add permissions**.
    4. Select **Grant admin consent for \{your organization}**.

    No client secret is needed; this is a public client that uses PKCE.
  </Step>

  <Step title="Send Anthropic your IDs">
    Anthropic maintains an allowlist of tenant and client IDs that may call the connector service. Email your Anthropic representative, or open a support ticket, with your Directory (tenant) ID and the Application (client) ID from step 2. Allowlisting is typically completed within two to three business days, as it requires a connector service deployment.

    Until the allowlist is updated, sign-in will succeed but the connector returns *Client application is not authorized for this resource*.
  </Step>

  <Step title="Configure Claude Desktop">
    In the Claude Desktop [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration), open **Connectors**, select **Add server → Microsoft 365**, and enter the values below.

    | Field     | Value                                                                      |
    | --------- | -------------------------------------------------------------------------- |
    | Client ID | The Application (client) ID from step 2                                    |
    | Tenant ID | Your Directory (tenant) ID                                                 |
    | Scope     | `api://07c030f6-5743-41b7-ba00-0a6e85f37c17/access_as_user offline_access` |

    Select **Save**, then deploy the configuration through your device-management tool as usual.

    If you manage configuration through JSON or a plist directly instead of the in-app configuration window, add the following entry to [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers).

    ```json theme={null}
    {
      "name": "m365",
      "url": "https://microsoft365.mcp.claude.com/mcp",
      "transport": "http",
      "oauth": {
        "clientId": "APPLICATION_CLIENT_ID_FROM_STEP_2",
        "tenantId": "DIRECTORY_TENANT_ID",
        "scope": "api://07c030f6-5743-41b7-ba00-0a6e85f37c17/access_as_user offline_access"
      }
    }
    ```
  </Step>
</Steps>

### Sign in as a user

After the configuration is deployed, each user opens **Customize → Connectors** in Claude Desktop and selects **Connect** next to Microsoft 365. Their browser opens to your tenant's sign-in page; once they consent, the connector is ready to use in conversations.

### Allow the required network hosts

In addition to the [base egress hosts](/docs/third-party/claude-desktop/telemetry#required-egress-paths), Claude Desktop needs outbound HTTPS access to the hosts below. The connector service itself calls `graph.microsoft.com` from Anthropic's infrastructure, so user devices do not need egress to Graph.

| Host                          | Purpose                                                       |
| ----------------------------- | ------------------------------------------------------------- |
| `login.microsoftonline.com`   | Microsoft Entra sign-in                                       |
| `microsoft365.mcp.claude.com` | The connector service (substitute your deployment's hostname) |

### Troubleshoot sign-in errors

The errors below are the ones most commonly seen during setup. Each maps to a specific step that was missed or misconfigured.

| Error                                                    | Cause                                                                                                                               | Fix                               |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| `AADSTS50011` redirect mismatch                          | Redirect URI is not exactly `http://127.0.0.1/callback`, or was registered under *Web* instead of *Mobile and desktop applications* | Re-check step 2.1                 |
| `AADSTS50194` multi-tenant required                      | Tenant ID is missing from the configuration                                                                                         | Add Tenant ID in step 4           |
| `AADSTS65001` admin consent required                     | Step 1 was not completed, or step 2.4 was skipped                                                                                   | Complete admin consent            |
| `Client application is not authorized for this resource` | Anthropic allowlist not yet updated                                                                                                 | Wait for confirmation from step 3 |
| `AADSTS9000411` duplicate prompt parameter               | Older Claude Desktop build                                                                                                          | Upgrade to the current release    |

## Local connector

Claude Desktop includes a built-in copy of the Microsoft 365 server. As an alternative to the remote connector, you can configure the app to run that server as a local process on each user's machine: the user signs in to Microsoft Entra on the device, and the server calls Microsoft Graph directly from the device. No Microsoft 365 data or tokens pass through Anthropic's infrastructure.

Choose the local connector when your data-residency requirements do not allow Microsoft 365 content to transit infrastructure outside your control, when your tenant enforces device-based Conditional Access policies (such as *Require compliant device*) that the remote connector's server-side token exchange cannot satisfy, or when you want to avoid the allowlisting step. The [comparison table](#choose-a-connector) above summarizes the differences.

### Set up the local connector

<Steps>
  <Step title="Register a public client app for local mode">
    <Warning>
      Do not reuse the desktop client app you registered for the remote connector. That app is consented only for the connector's own scope, so its tokens can reach nothing but the connector service. The local-mode app needs Microsoft Graph permissions directly, and adding those to the remote connector app's client ID would let any token minted for it read Microsoft 365 data directly, tenant-wide. Register a separate app dedicated to local mode.
    </Warning>

    1. In **Entra admin center → App registrations → New registration**, set **Name** to `Claude Desktop M365 Local` (or your preferred name) and set **Supported account types** to *Accounts in this organizational directory only*.
    2. Under **Authentication**, open the **Redirect URI configuration** tab and select **Add redirect URI** (on older versions of the portal, select **+ Add a platform** instead). Choose the **Mobile and desktop applications** card (the Windows, UWP, and Console card, not the iOS / macOS card, which takes a bundle ID rather than a redirect URI). Leave the suggested redirect URIs unchecked, enter `http://localhost` in the **Custom redirect URIs** box, and select **Configure**. This is the standard loopback redirect for desktop apps: during browser sign-in, Microsoft Entra redirects to a listener on the device itself, so the response never leaves the machine. For brokered sign-in on managed devices, also add the per-platform broker redirect URI shown under [How users sign in](#how-users-sign-in). Add it to the same platform by selecting **Edit** on the **Mobile and desktop applications** section that appears on the Authentication page, rather than adding another platform, and select **Save** at the top when you finish (on older versions of the portal, add the broker URI via the **Add URI** row inside the platform section instead). After you save, Microsoft Entra may display the `msauth` URI under a separate **iOS / macOS** section. That placement is expected because both sections map to `publicClient.redirectUris` in the app's manifest.
    3. Under **Authentication**, set **Allow public client flows** to **Yes**, and select **Save**. The control is on the **Settings** tab under **Web and SPA settings** (on older versions of the portal, under **Advanced settings**). Brokered sign-in on managed devices issues token requests without a redirect URI, so Microsoft Entra relies on this setting to classify the app as a public client. With it set to No, brokered silent token acquisition fails with `AADSTS7000218`. To prevent device-code phishing, apply a tenant Conditional Access policy that blocks the device-code authentication flow. Conditional Access policies target the resource a token is requested for rather than the requesting client, so scope the policy to All resources, not to this registration.
    4. Under **API permissions → Add a permission → Microsoft Graph → Delegated permissions**, add the scopes the connector will request (the default set is listed under [Configure scopes](#configure-scopes)), then select **Grant admin consent for \{your organization}**.
    5. Note the **Application (client) ID** and **Directory (tenant) ID** from the overview page.
  </Step>

  <Step title="Configure Claude Desktop">
    In the Claude Desktop [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration), open **Connectors**, select **Add server**, and choose **Microsoft 365** under the **Built-in** group. Enter the values below, then select **Test connection** to verify that the server starts and lists its tools, and select **Save**.

    | Field       | Value                                                                                                       |
    | ----------- | ----------------------------------------------------------------------------------------------------------- |
    | Tenant ID   | Your Directory (tenant) ID                                                                                  |
    | Client ID   | The Application (client) ID from step 1                                                                     |
    | Azure cloud | `global` (default), `us-gov-high`, or `us-gov-dod`                                                          |
    | Access      | Leave empty for standard read access, or list scopes explicitly (see [Configure scopes](#configure-scopes)) |

    If you manage configuration through JSON or a plist directly, add an entry to [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) with the `server` field set to `microsoft365`:

    ```json theme={null}
    {
      "name": "Microsoft 365",
      "server": "microsoft365",
      "tenantId": "DIRECTORY_TENANT_ID",
      "clientId": "APPLICATION_CLIENT_ID_FROM_STEP_1"
    }
    ```

    | Field        | Required | Description                                                                                                                                                                   |
    | ------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `name`       | Yes      | Unique display name, shown to users in connector settings.                                                                                                                    |
    | `server`     | Yes      | Must be `microsoft365`. Built-in entries use this field instead of `url`, `transport`, or `command`; an entry that mixes `server` with those fields is rejected.              |
    | `clientId`   | Yes      | The Application (client) ID of the local-mode app from step 1.                                                                                                                |
    | `tenantId`   | Yes      | Your Directory (tenant) ID.                                                                                                                                                   |
    | `azureCloud` | No       | `global` (default), `us-gov-high`, or `us-gov-dod`. Selects the Microsoft Entra and Microsoft Graph hosts for US Government clouds.                                           |
    | `scope`      | No       | Space-separated delegated Graph scopes to request instead of the default read set. A string array named `scopes` is also accepted. See [Configure scopes](#configure-scopes). |
    | `toolPolicy` | No       | Per-tool approval locks, the same as for any managed server. See [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers).                                 |

    The server ships inside the app, so nothing else needs to be installed on the device, and it activates only from managed configuration; users cannot add it themselves. Deploy the configuration through your device-management tool as usual.
  </Step>

  <Step title="Allow the required network hosts for local mode">
    The local connector calls Microsoft directly from the device, so in addition to the [base egress hosts](/docs/third-party/claude-desktop/telemetry#required-egress-paths), devices need outbound HTTPS access to:

    | Host                        | Purpose                   |
    | --------------------------- | ------------------------- |
    | `login.microsoftonline.com` | Microsoft Entra sign-in   |
    | `graph.microsoft.com`       | Microsoft Graph data APIs |

    US Government cloud deployments use `login.microsoftonline.us` and `graph.microsoft.us` (or `dod-graph.microsoft.us` for `us-gov-dod`) instead, matching the `azureCloud` setting. GCC High (`us-gov-high`) support has been confirmed in customer deployments. No egress to any Anthropic host is needed for Microsoft 365 data with the local connector.
  </Step>
</Steps>

### Configure scopes

With no `scope` field, the connector requests the standard read set at sign-in:

| Scope                                     | Purpose                                                                |
| ----------------------------------------- | ---------------------------------------------------------------------- |
| `User.Read`                               | Read the signed-in user's profile                                      |
| `Mail.Read`, `Mail.Read.Shared`           | Read mail in the user's and shared mailboxes                           |
| `Calendars.Read`, `Calendars.Read.Shared` | Read events in the user's and shared calendars, and find meeting times |
| `Files.Read.All`                          | Read files the user can access in OneDrive and SharePoint              |
| `Sites.Read.All`                          | Read SharePoint site content the user can access                       |
| `Chat.Read`                               | Read Teams chat messages the user can access                           |
| `OnlineMeetings.Read`                     | Read the user's online meetings                                        |
| `offline_access`                          | Refresh tokens without re-prompting                                    |

To request a different set, list scopes in the entry's `scope` field. The connector then requests exactly that list (plus `User.Read` and `offline_access`, which are always included). Use the list to narrow the read surface, to add the optional read scopes below, or to add [write scopes](#grant-write-scopes). Whatever you list must also be consented on the app registration from step 1; keep the two lists in sync.

Three optional read scopes are not in the standard set:

* `ChannelMessage.Read.All` adds Teams channel messages to chat search results. Requires tenant-admin consent.
* `OnlineMeetingTranscript.Read.All` enables reading meeting transcripts. Requires tenant-admin consent.
* `MailboxSettings.Read` enables reading mail filters and automatic-reply settings.

Until the first two are granted, chat search omits channel results and transcript requests return a permission error.

The `scope` field accepts only scopes the connector can use. An entry containing an unrecognized scope name is rejected as a whole at configuration load, with an error in the app's main log listing the valid names, and the connector does not appear.

<Note>
  Narrowing or removing `scope` shrinks what the connector requests at the next sign-in, but it does not narrow tokens already obtainable for the registration: Microsoft Entra issues tokens carrying every scope previously consented for the app, regardless of what is requested. To revoke access, remove the consent in Entra under **Enterprise applications → your app → Permissions**.
</Note>

The connector provides these read and search tools:

| Tool                                            | What it does                                                                       |
| ----------------------------------------------- | ---------------------------------------------------------------------------------- |
| `outlook_email_search`                          | Search Outlook mail                                                                |
| `outlook_calendar_search`                       | Search calendar events                                                             |
| `find_meeting_availability`                     | Find free meeting times                                                            |
| `chat_message_search`                           | Search Teams chat (1:1 and group; channel messages need `ChannelMessage.Read.All`) |
| `sharepoint_search`, `sharepoint_folder_search` | Search SharePoint and OneDrive                                                     |
| `read_resource`                                 | Fetch a specific item, such as a message, event, or file                           |

Granting write scopes enables write tools; see [Grant write scopes](#grant-write-scopes).

### Grant write scopes

With only read scopes granted, the connector is read-only. To let Claude take actions in Microsoft 365 (sending mail, managing drafts, labels, filters, and calendar events, and working with files in OneDrive and SharePoint), grant write scopes: add them to the entry's `scope` field and consent them on the app registration from step 1, the same as any other scope. Each write tool appears only when its scope is in the entry's list, so granting a subset of the write scopes exposes a matching subset of the tools, and removing the write scopes from the list returns the connector to read-only. Write tools require Claude Desktop version 1.19367.0 or later.

| Scope                       | What it enables                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `Mail.Send`                 | Send mail, send drafts, and forward mail                                                                      |
| `Mail.ReadWrite`            | Create, update, and delete drafts; trash, untrash, and delete messages; apply and remove labels on messages   |
| `Calendars.ReadWrite`       | Create, update, delete, and respond to calendar events                                                        |
| `Files.ReadWrite.All`       | Create, update, rename, move, copy, and delete files and folders the user can edit in OneDrive and SharePoint |
| `MailboxSettings.ReadWrite` | Manage labels, mail filters, and automatic replies                                                            |

Sending drafts and forwarding mail also require a mail read scope (one of `Mail.Read`, `Mail.ReadWrite`, or `Mail.Read.Shared`) for the pre-send checks; the standard read set already includes one.

Every write tool requires user approval on each call by default. Administrators can change a tool's approval state with [`toolPolicy`](/docs/third-party/claude-desktop/configuration#managedmcpservers), except for the send tools (`outlook_send_mail`, `outlook_send_draft`, `outlook_forward_mail`, `outlook_create_event`, `outlook_update_event`): an `allow` setting for them resolves to `ask`, so they always require approval on each call.

### How users sign in

After the configuration is deployed, the connector appears in **Customize → Connectors** in Claude Desktop. Sign-in starts when the user selects **Connect**.

On both Windows and macOS, sign-in goes through the device's native authentication broker when the device is set up for it: a system account-picker dialog appears instead of the browser, and the issued tokens carry the device identity claim that device-based Conditional Access policies (such as *Require compliant device*) evaluate. When the broker is unavailable, sign-in opens the system browser instead. The requirements for each platform are listed below.

Browser sign-in works on tenants without device-based Conditional Access policies. It satisfies device policies only when the browser itself carries the device identity: on Windows, a browser signed in with the work account on an Entra-joined device (such as Microsoft Edge) provides this; on macOS, deploy Microsoft's Enterprise SSO browser integration, or use brokered sign-in instead.

<AccordionGroup>
  <Accordion title="Requirements for brokered sign-in on Windows">
    Brokered sign-in on Windows requires Claude Desktop version 1.13576.0 or later.

    * Windows 10 or later (desktop editions). The broker (Web Account Manager, or WAM) is built into Windows; no separate install is needed.
    * The device is joined or registered to Entra ID (Entra joined, Entra hybrid joined, or Entra registered). For device-based Conditional Access, the device must also be marked compliant in Intune or hybrid-joined, as your policy requires.
    * The broker redirect URI is registered on the local-mode app under **Mobile and desktop applications**, with `APPLICATION_CLIENT_ID` replaced by the Application (client) ID from step 1:

    ```text theme={null}
    ms-appx-web://Microsoft.AAD.BrokerPlugin/APPLICATION_CLIENT_ID
    ```

    If the broker rejects the app's sign-in request, or a brokered attempt fails with an error the broker cannot recover from, the connector falls back to the system browser automatically and stays on the browser flow until Claude Desktop restarts. A user canceling the broker dialog does not trigger the fallback. On tenants that require a compliant device, tool calls then fail with `AADSTS53003`, unless the browser itself carries the device identity (see above); fix the broker requirement that caused the fallback (most often a missing broker redirect URI) and restart the app. A fallback is recorded in the connector's log file as a `local_auth_broker_fallback` event.
  </Accordion>

  <Accordion title="Requirements for brokered sign-in on macOS">
    Brokered sign-in on macOS requires Claude Desktop version 1.19367.0 or later.

    * The Mac is enrolled in an MDM (Intune, Jamf, or similar), registered in Entra ID, and marked compliant. For non-Intune MDMs, use the partner device-compliance integration that reports compliance to Intune and Entra.
    * **Intune Company Portal** is installed; it provides the broker.
    * An **Extensible SSO** configuration profile of type **Redirect**, pointed at the Microsoft Enterprise SSO plug-in, is deployed through MDM. The broker is unavailable without it.
    * The broker redirect URI is registered on the local-mode app under **Mobile and desktop applications** (it appears under the **iOS / macOS** section after saving):

    ```text theme={null}
    msauth.com.anthropic.claudefordesktop://auth
    ```

    If the app registration also lists `msauth.com.anthropic.claudefordesktop.helper://auth`, remove that entry. Claude Desktop does not use it.

    If the broker rejects the app's sign-in request, or a brokered attempt fails with an error the broker cannot recover from, the connector falls back to the system browser automatically and stays on the browser flow until Claude Desktop restarts. A user canceling the broker dialog does not trigger the fallback. On tenants that require a compliant device, tool calls then fail with `AADSTS53003`, unless the browser itself is signed in through the device's SSO integration; fix the broker requirement that caused the fallback (most often a missing broker redirect URI or SSO profile) and restart the app. A fallback is recorded in the connector's log file as a `local_auth_broker_fallback` event.
  </Accordion>
</AccordionGroup>

### Token storage and sign-out

The connector's Entra tokens are stored on the device, encrypted by Claude Desktop using the operating system's secure storage. Each configured entry has its own token store, and tokens persist across app restarts so users are not asked to sign in again each session.

Selecting **Disconnect** next to the connector signs the user out and deletes its stored tokens. Where the user signed in through the broker, the device's work or school account itself is managed by the operating system and remains after Disconnect, as with any other brokered app; remove the account in Windows Settings (**Accounts → Access work or school**) or macOS Company Portal, or revoke the user's sessions in Entra, to end access entirely (revocation takes effect once the current access token expires).

### Troubleshoot the local connector

| Symptom                                                                       | Cause                                                                                                                                                                                                                                                                                                                          | Fix                                                                                                                                             |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test connection** reports that the built-in server is not included          | The installed Claude Desktop version predates the built-in connector                                                                                                                                                                                                                                                           | Upgrade Claude Desktop                                                                                                                          |
| **Microsoft 365** is missing from the **Add server** options                  | The installed Claude Desktop version predates the built-in connector                                                                                                                                                                                                                                                           | Upgrade Claude Desktop, or author the JSON entry directly                                                                                       |
| Connector missing from settings                                               | The entry was rejected during configuration parsing: an unrecognized scope name in `scope`, a missing `tenantId` or `clientId`, or a `url`, `transport`, or `command` field mixed into the entry                                                                                                                               | Check the app's main log for a line naming the dropped entry                                                                                    |
| Sign-in opens the browser on a managed device where the broker was expected   | macOS: Claude Desktop is older than 1.19367.0, Company Portal is not installed, the SSO configuration profile is not deployed, or the broker redirect URI is not registered. Windows: Claude Desktop is older than 1.13576.0, the device is not Entra-joined or Entra-registered, or the broker redirect URI is not registered | Re-check the brokered sign-in requirements above                                                                                                |
| `AADSTS50011` redirect mismatch                                               | The redirect URI named in the error message (`http://localhost` for browser sign-in, or the platform's broker redirect URI for brokered sign-in) is missing from the local-mode app registration, was entered with a different value, or was added under *Web* instead of *Mobile and desktop applications*                    | Add or correct that URI under *Mobile and desktop applications* (step 1.2, or the brokered sign-in requirements above)                          |
| `AADSTS900971` no reply address provided                                      | The macOS broker redirect URI is not registered on the local-mode app                                                                                                                                                                                                                                                          | Register `msauth.com.anthropic.claudefordesktop://auth` as described in step 1.2 (after you save, it appears under the **iOS / macOS** section) |
| `AADSTS65001` admin consent required                                          | Graph delegated permissions were not admin-consented                                                                                                                                                                                                                                                                           | Re-check step 1.4                                                                                                                               |
| `AADSTS53003` blocked by Conditional Access                                   | A device-compliance policy is evaluating a sign-in that carries no device claim                                                                                                                                                                                                                                                | Meet the brokered sign-in requirements for the platform, then restart Claude Desktop                                                            |
| `AADSTS7000218` request body must contain client\_assertion or client\_secret | **Allow public client flows** is set to No on the local-mode app registration, so brokered token requests are classified as confidential                                                                                                                                                                                       | Set **Allow public client flows** to **Yes** (step 1.3)                                                                                         |
| Tools return a permission error or Graph `403`                                | A scope the tool needs is not consented on the app registration, or is excluded by an explicit `scope` list                                                                                                                                                                                                                    | Add the scope in both places and grant admin consent                                                                                            |
| Write tools are missing or fail                                               | The matching write scope is not listed in the entry's `scope` field, or the installed Claude Desktop version predates write support                                                                                                                                                                                            | Add the scope to the entry and consent it on the app registration (see [Grant write scopes](#grant-write-scopes)), and upgrade Claude Desktop   |

The connector writes its sign-in and Microsoft Graph errors to its own log file in the Claude Desktop logs directory (`~/Library/Logs/Claude-3p/` on macOS, `%LOCALAPPDATA%\Claude-3p\logs\` on Windows), named `mcp-server-office365-builtin.log`. Configuration parsing and connection lifecycle messages appear in `main.log` in the same directory.
