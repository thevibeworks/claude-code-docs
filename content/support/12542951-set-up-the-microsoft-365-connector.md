# Set up the Microsoft 365 connector

This article walks admins through enabling the Microsoft 365 connector for their organization in Claude—including granting Microsoft Entra consent, restricting access, and managing permissions. Once setup is complete, people in your tenant can connect Microsoft 365 to their own Claude accounts to search across SharePoint, OneDrive, Outlook, and Teams from Claude. You can also enable write tools, which let Claude send email, manage calendar events, and create and update files on a member's behalf.

The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

For end-user instructions on connecting and using Microsoft 365 once setup is complete, see **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774-)**.

**Important:** The Microsoft 365 connector requires a Microsoft Entra tenant tied to a Microsoft Business plan. Personal Microsoft accounts (such as @outlook.com or @hotmail.com addresses) can't be used to connect.

---

## Setup overview

Two things need to happen before anyone in your organization can connect Microsoft 365, plus an optional third step if you want to enable write tools:

1. **On Team and Enterprise plans:** A Claude organization owner enables the Microsoft 365 connector for the organization.

2. **In every tenant:** A Microsoft Entra Global Administrator grants a one-time consent that authorizes the integration for your tenant.

3. **To enable write tools:** A Microsoft Entra administrator consents to the updated permission set, and you enable write tools for your organization. See **[Enable write tools](#h_a51d877afd)** below.

After completing these steps, members can connect Microsoft 365 to their own Claude accounts following the steps in **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774-)**.

## Enable the connector for your organization

This step applies to Team and Enterprise plans only. On Free, Pro, and Max plans, skip to the next section.

1. Sign in to Claude.

2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

3. Click “+ Add” at the top of the page, then “All available.”

4. Find **Microsoft 365** and click “Add to your team.”

## Grant Microsoft Entra admin consent

A Microsoft Entra Global Administrator in your tenant needs to authorize the integration before anyone can connect. There are two ways to do this.

### Option 1: Consent through Claude

If your Microsoft Entra Global Administrator has a Claude account, they can grant consent during the standard connection flow:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.

2. Find **Microsoft 365** and click “Connect.”

3. Authenticate with Microsoft 365 credentials.

4. Review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

After this, other people in the same Entra tenant can connect by following the standard end-user steps. They won't see the consent prompt—they'll just authenticate and start using the integration.

### Option 2: Manual setup in Microsoft Entra ID

Use this path if your Microsoft Entra Global Administrator doesn't have a Claude account, or if you need to troubleshoot the app install and permissions setup. You can add the connector apps and grant admin consent directly in Microsoft Entra ID.

This process adds two service principals to your tenant. Each principal establishes a service-level identity for one of the two M365 MCP for Claude app registrations, allowing them to access and interact with your organization's data and resources via the Microsoft Graph API.

**1. Add the service principals**

Using Microsoft Graph Explorer, add both required service principals:

M365 MCP Client for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals
{"appId":"08ad6f98-a4f8-4635-bb8d-f1a3044760f0"}
```

M365 MCP Server for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals
{"appId":"07c030f6-5743-41b7-ba00-0a6e85f37c17"}
```

**2. Grant admin consent**

Construct and visit the following URLs in your browser, replacing {your-tenant-id} with your organization's tenant ID.

M365 MCP Client for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0
```

M365 MCP Server for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17
```

When you visit each URL, you'll be prompted to consent to the delegated permissions required by the integration on behalf of your organization.

**3. Finish setup**

- **Team and Enterprise plans:** A Claude organization Owner needs to enable the connector in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. Then members can connect individually.

- **Free, Pro, and Max plans:** Members can connect by navigating to **[Customize > Connectors](http://claude.ai/customize/connectors)**, finding **Microsoft 365**, and clicking “Connect.”

### Restrict who can use the connector

To limit which people in your tenant can authenticate to Microsoft 365 through Claude:

1. Go to the Microsoft Entra admin center at entra.microsoft.com.

2. Navigate to the **M365 MCP Server for Claude** enterprise application.

3. Go to **Properties** and set **Assignment required?** to “Yes.”

4. Under **Users and groups**, add the specific users or groups who should have access.

5. Repeat the same steps for the **M365 MCP Client for Claude** enterprise application.

Both components need to be restricted to the same set of authorized people.

### Restrict which permissions the connector can use

To limit which types of resources the integration can access, selectively revoke permissions from the default set of authorized scopes. This requires Microsoft Entra admin access.

1. As a Microsoft Entra admin, go to entra.admin.com.

2. Select “Enterprise Applications.”

3. Next to the search box, remove the application type filter.

4. Search for and click “M365 MCP Server for Claude.”

5. Go to **Permissions**.

6. Under the **Admin consent** tab and in the Microsoft Graph list of permissions, select the permission you would like to revoke and click the “**…**” button.

7. Select “Revoke permission” and confirm with “Yes, revoke.”

Once revoked, attempts to access a resource with that permission will return a "Failed to call tool" error.

Members can also individually turn off specific tools in their own Microsoft 365 settings to prevent Claude from trying to access a tool for which the permission has been revoked.

To restore a revoked permission, follow the steps to grant admin consent described in **Option 2: Manual setup in Microsoft Entra ID**. This will revert the permissions to the default state.

---

## Enable write tools

Write tools let Claude send email, manage drafts and calendar events, update mailbox settings, and create and update files in OneDrive and SharePoint. Read and search tools work the same whether or not write tools are enabled.

**1. Re-consent to the updated permissions**

The connector's permission set now includes additional Microsoft Graph scopes to support write tools. If your tenant consented before write tools launched, a Microsoft Entra Global Administrator needs to review and approve the updated permission set before write tools activate. Review and approve the updated permissions for the connector in your tenant's **Enterprise Applications** consent flow. This is a one-time action per tenant.

**2. Enable write tools for your organization**

If your organization was using the connector before write tools launched, they will be blocked by default. Enable them for everyone by going to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**, finding “Microsoft 365,” and setting the appropriate permissions. Enterprise plans can enable them for a subset of users through **[custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_979e558d00)**.

**3. Verify**

Once enabled, ask Claude to perform a low-risk write action, such as "Draft an email to myself, but don't send it," to confirm write tools are active.

**Note:** Emails Claude sends include an attribution header identifying them as agent-initiated. File and calendar writes aren't currently tagged. Attachments aren’t supported in write tools, so sending, forwarding, and drafting all reject messages with attachments. Write tools are also subject to per-user limits on writes, sends, and recipients.

---

## Permissions reference

The Microsoft 365 connector uses **delegated permissions**, meaning Claude acts on behalf of each individual user and can only access data that user already has permission to view in Microsoft 365. Permissions are read-only—Claude can't modify, delete, or create content in your tenant.

During authentication, the integration requests the following permissions:

**Basic access**

- `User.Read`: Sign in and read user profile

- `openid`: Sign in with organizational account

- `offline_access`: Maintain access to data

- `email`: View email address

- `profile`: View basic profile information

**Email (Outlook)**

- `Mail.Read`: Read email messages

- `Mail.ReadBasic`: Read email metadata (sender, subject, date)

- `Mail.Read.Shared`: Read emails in mailboxes the user has access to

- `MailboxFolder.Read`: Read mailbox folder structure

- `MailboxItem.Read`: Read items in mailbox

- `MailboxSettings.Read`: Read mailbox settings, like the user's timezone

**Note:** Shared mailbox access is included through the `Mail.Read.Shared` permission. Members can search shared mailboxes they have delegate access to in Microsoft 365, including full access and folder-level delegation. No setup is needed beyond standard admin consent and the delegate permissions already configured in Microsoft 365.

**Calendar**

- `Calendars.Read`: Read calendar events

- `Calendars.Read.Shared`: Read calendars shared with the user

**Teams chat**

- `Chat.Read`: Read Teams chat messages

- `Chat.ReadBasic`: Read Teams chat metadata

- `ChatMember.Read`: Read information about chat participants

- `ChatMessage.Read`: Read Teams chat messages

**Teams channels**

- `Channel.ReadBasic.All`: Read channel names and descriptions

- `ChannelMessage.Read.All`: Read channel messages

**Meetings**

- `OnlineMeetings.Read`: Read online meetings

- `OnlineMeetingTranscript.Read.All`: Read meeting transcripts

- `OnlineMeetingAiInsight.Read`: Read AI-generated meeting insights

- `OnlineMeetingArtifact.Read.All`: Read meeting recordings and artifacts

- `OnlineMeetingRecording.Read.All`: Read meeting recordings

**Files (OneDrive and SharePoint)**

- `Files.Read`: Read user files

- `Files.Read.All`: Read all files the user can access

- `Sites.Read.All`: Read items in SharePoint sites

**Write permissions**

The following permissions support write tools and are included in the updated consent set:

- `Mail.Send`: Send and forward email

- `Mail.ReadWrite`: Create, update, and delete drafts; move and label messages

- `Calendars.ReadWrite`: Create, update, delete, and respond to calendar events

- `Files.ReadWrite.All`: Create and update files in OneDrive and SharePoint

- `MailboxSettings.ReadWrite`: Manage categories, inbox rules, and automatic replies

**User directory**

- `User.ReadBasic.All`: Read basic profile information for all users in the organization (used for finding meeting availability)

The Microsoft 365 connector searches SharePoint across the entire tenant using the permissions of the user. Site-specific search restriction isn't supported.

## Privacy and security

- **Permission inheritance:** Claude mirrors each user's existing Microsoft 365 permissions. Members can't access anything through Claude that they couldn't already see directly in Microsoft 365.

- **On-demand access:** Claude only accesses data when a user explicitly asks a question that requires it.

- **Revocable access:** Members can disconnect their own integration through **[Customize > Connectors](http://claude.ai/customize/connectors)**. Team and Enterprise plan Owners can also remove the connector for the entire organization in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

For more detail, see the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-)**.

---

## Troubleshooting

### A member can't authenticate

1. Confirm their account is tied to a Microsoft Entra tenant, not a personal Microsoft account.

2. Confirm their Microsoft 365 license is active.

3. Confirm admin consent has been granted using Option 1 or Option 2 above.

4. Check whether organizational policies (such as conditional access) are blocking third-party app authentication.

### Members are seeing "Failed to call tool" errors

A permission may have been selectively revoked in Microsoft Entra. Members can turn off the corresponding tool in their Microsoft 365 settings to suppress the error, or you can restore the permission by repeating the admin consent steps in **[Option 2: Manual setup in Microsoft Entra ID](#h_c5f095c9cf)**.

### Write tools aren't appearing for members

1. Confirm a Microsoft Entra administrator has consented to the updated permission set that includes write scopes.

2. Confirm write tools are enabled in the Microsoft 365 connector configuration, or that the member is covered by a role-based access policy that grants them.

3. Have the member disconnect and reconnect Microsoft 365 in **[Customize > Connectors](http://claude.ai/customize/connectors)**.

---

## Frequently asked questions

### What happens if a member tries to connect before consent is granted?

They'll see an error message indicating that an administrator must grant app permissions before they can use the integration. The connection will fail until a Microsoft Entra Global Administrator approves the necessary permissions.

### Can the Microsoft 365 connector be used with enterprise search?

Yes. When enterprise search is enabled, it can query Microsoft 365 alongside other connected services for unified search across Slack, Google Workspace, Microsoft 365, and more.

### Can the integration modify Microsoft 365 data?

Only after an Entra admin grants write scopes. With write tools on, Claude can send email, manage drafts and calendar events, update mailbox settings, and create and update files in OneDrive and SharePoint, always within each member's existing Microsoft 365 permissions. Without them, the integration is read-only. Claude can't post Teams messages or change Teams settings or permissions in either case, since there are no tools allowing this.