> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Claude for Microsoft 365 in Claude for Government

> Download the Claude for Microsoft 365 manifest from your Claude for Government host and deploy the add-in to users from the Microsoft 365 admin center.

> **Who this is for:** Microsoft 365 administrators who make the Claude for Microsoft 365 add-in available to agency users in Excel, Word, and PowerPoint.

In Claude for Government, Claude for Microsoft 365 is in early access. To request access for your agency, contact your Anthropic representative.

Claude for Microsoft 365 is an Office add-in that opens Claude in a pane beside the workbook, document, or presentation a user is editing. In Claude for Government, Office loads the add-in from your Claude for Government host, and the add-in sends its sign-in and chat traffic to that host. The host is written into the add-in's manifest, a small XML file that tells Office where to load the add-in from. You make the add-in available from the Microsoft 365 admin center by uploading the manifest and assigning it to users.

Microsoft 365 Government tenants can't use the public add-in store, so you deploy the manifest yourself (see Microsoft's [guidance for Office Add-ins on government clouds](https://learn.microsoft.com/en-us/office/dev/add-ins/publish/government-cloud-guidance)).

This page covers the add-in that runs inside Office. The [Microsoft 365 connector](/docs/government/connectors/microsoft-365), which lets Claude Desktop read your agency's Outlook, OneDrive, SharePoint, and Teams content, is a separate feature with its own setup.

## Before you begin

Confirm each of the following before you deploy the manifest.

* **Claude for Microsoft 365 is turned on for the organization.** Check the **Claude for Microsoft 365** switch under [Product availability](/docs/government/config/settings#product-availability). It is off by default. While it is off, users who sign in from the add-in are told that Claude for Microsoft 365 is not turned on for their organization.
* **User accounts exist.** The add-in signs users in to the same accounts as this portal. Each user needs a [routing rule](/docs/government/tenant-admin/identity-and-access) that covers them and a [seat tier](/docs/government/org-admin/seat-tiers) with at least one model enabled.
* **Office is a supported version.** The add-in needs the Office builds listed under supported versions for [Excel](/docs/office-agents/excel#supported-versions), [Word](/docs/office-agents/word#supported-versions), and [PowerPoint](/docs/office-agents/powerpoint#supported-versions).
* **Devices can reach your Claude for Government host.** Office on every device must reach your Claude for Government host over HTTPS (port 443). That host serves the add-in and carries its sign-in requests and chat traffic.
* **Devices can reach Microsoft's Office add-in library.** At startup the pane loads Microsoft's `office.js` library from one of these Microsoft hosts, chosen by the `?officecdn=` parameter you add when you [download the manifest](#download-the-manifest):
  * no `?officecdn=` parameter: `appsforoffice.microsoft.com`
  * `?officecdn=gcc`: `appsforoffice.gcc.cdn.office.net`
  * `?officecdn=gcch`: `appsforoffice.gcch.cdn.office.net`
  * `?officecdn=dod`: `appsforoffice.dod.cdn.office.net`
* **Your telemetry collector accepts the add-in's requests.** When a [**Telemetry endpoint**](/docs/government/config/settings#telemetry-endpoint) is set, the pane on each device sends traces and logs directly to that collector. The collector must be reachable from users' networks and must accept cross-origin requests from your Claude for Government host, which is the add-in's origin.
* **Your connectors accept the add-in's requests.** The pane on each device connects directly to every connector that applies to Claude for Microsoft 365 (see the [**Connectors** card](/docs/government/config/settings#tool-and-connector-cards)). Each connector must be reachable from users' networks and must accept cross-origin requests from your Claude for Government host, which is the add-in's origin.
* **Browsers can reach sign-in.** Sign-in happens in the user's default web browser, not in the pane. Browsers on each device must reach your Claude for Government host, the Claude for Government sign-in service (a separate host that your Anthropic representative provides), and your agency's identity provider. These are the same hosts [Claude Desktop sign-in](/docs/government/deploy-desktop/configure#before-you-begin) needs.
* **You can deploy add-ins in the Microsoft 365 admin center.** Users need the Microsoft 365 Apps versions and Exchange Online mailboxes listed in Microsoft's [requirements for Centralized Deployment](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-of-add-ins).

## Download the manifest

Your Claude for Government host serves the manifest at the fixed path `/office/manifest-fedstart.xml`. If you are unsure of your host, ask your Anthropic representative.

```text theme={null}
https://<claude-for-government-host>/office/manifest-fedstart.xml
```

If your tenant is in GCC High or DoD, add `?officecdn=gcch` or `?officecdn=dod` to the end of the address, and in GCC you can add `?officecdn=gcc`. The pane then loads Microsoft's `office.js` library from the Office CDN inside your cloud, as Microsoft's [guidance for Office Add-ins on government clouds](https://learn.microsoft.com/en-us/office/dev/add-ins/publish/government-cloud-guidance) recommends.

```text theme={null}
https://<claude-for-government-host>/office/manifest-fedstart.xml?officecdn=gcch
```

Choose the cloud before your first deployment. To change it later, remove the add-in in the admin center, download the file again with the new parameter, and deploy the new file.

Open the address in a browser and save the file. Open the saved file and check that the `SourceLocation` line names your Claude for Government host. If it doesn't, contact your Anthropic representative.

If your host answers to more than one name, pick one name and always download from it. The add-in's identity follows the host name in the address, so files downloaded under two names install as two separate add-ins.

The manifest installs Claude in Excel, Word, and PowerPoint and asks Office for permission to read and change the open document, which is how Claude edits the file a user is working in. The admin center and Office list the add-in as **Claude for Government**, and the ribbon button is labeled **Claude**.

## Deploy from the Microsoft 365 admin center

Microsoft doesn't offer its **Integrated apps** page in its [government clouds](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/test-and-deploy-microsoft-365-apps), so GCC, GCC High, and DoD tenants deploy from **Settings** > **Add-ins** (Microsoft's [Centralized Deployment](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-of-add-ins)). If your admin center shows **Integrated apps** instead, follow [Deploy from Integrated apps](#deploy-from-integrated-apps). In either case, upload the file you saved rather than entering its web address, so that Microsoft's service doesn't have to reach your Claude for Government host.

### Deploy from the Add-ins page

<Steps>
  <Step title="Open the Microsoft 365 admin center">
    Sign in to the Microsoft 365 admin center for your cloud with an account that can deploy add-ins.
  </Step>

  <Step title="Open the Add-ins page">
    In the left pane, select **Show all**, then select **Settings** > **Add-ins**.
  </Step>

  <Step title="Start a custom deployment">
    Select **Deploy Add-in**, then select **Next**.
  </Step>

  <Step title="Choose a custom upload">
    Under **Deploy a custom add-in**, select **Upload custom apps**.
  </Step>

  <Step title="Upload the manifest">
    Choose the option to upload a manifest file from your device, browse to the `manifest-fedstart.xml` file you saved, and select **Upload**.
  </Step>

  <Step title="Choose users">
    On the **Configure add-in** page, choose who gets the add-in: **Everyone**, **Specific users/groups**, or **Just me**. Deploying to yourself or a small group first lets you confirm the add-in works on a representative device before a wider rollout.
  </Step>

  <Step title="Deploy">
    Select **Deploy**.
  </Step>
</Steps>

### Deploy from Integrated apps

<Steps>
  <Step title="Open the Microsoft 365 admin center">
    Sign in to the Microsoft 365 admin center with an account that can deploy add-ins.
  </Step>

  <Step title="Open Integrated apps">
    Select **Settings** > **Integrated apps**.
  </Step>

  <Step title="Start a custom upload">
    Select **Upload custom apps** and choose **Office Add-in** as the app type.
  </Step>

  <Step title="Upload the manifest">
    Choose the option to upload the manifest file from your device and upload `manifest-fedstart.xml`.
  </Step>

  <Step title="Choose users">
    Assign the add-in to everyone, specific users or groups, or just yourself. A small group first lets you confirm it works before a wider rollout.
  </Step>

  <Step title="Review the summary">
    Select **Next** through the remaining pages and review the summary.
  </Step>

  <Step title="Finish the deployment">
    Select **Finish deployment**.
  </Step>
</Steps>

A deployment can take up to 24 hours to reach every assigned user, and users may need to restart the Office application before the add-in appears.

To change who has the add-in or to remove it later, see Microsoft's [Manage add-ins in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center).

## What users see

Once the deployment reaches a user, a **Claude** button appears on the **Home** tab of the ribbon in Excel, Word, and PowerPoint. The add-in is also listed under **Admin Managed** in Office's add-ins window. Selecting the button opens the Claude pane, which shows a **Log in** button.

When the user selects **Log in**, the pane shows a short code and opens the Claude for Government sign-in page in the user's default browser. If the browser doesn't open, the user selects **Continue in browser** under the code. The code is valid for 10 minutes, after which the pane offers **Start over**. In the browser, the user:

1. Enters their agency email address.
2. Signs in through your agency's identity provider.
3. Acknowledges the U.S. Government system-use notification.
4. Checks that the code shown matches the one in the pane, then selects **Approve**.

When the user returns to the pane it shows **You're signed in**, and selecting **Continue** opens Claude. On a user's first sign-in the pane shows a short welcome and a notice to acknowledge before the chat box appears. For what users can do once signed in, see the Claude for Microsoft 365 guides for [Excel](/docs/office-agents/excel), [Word](/docs/office-agents/word), and [PowerPoint](/docs/office-agents/powerpoint).

## Confirm the deployment

<Steps>
  <Step title="Open the pane">
    As a user you assigned the add-in to, open Excel, Word, or PowerPoint, select the **Claude** button on the **Home** tab of the ribbon, then select **Log in** in the pane.
  </Step>

  <Step title="Sign in">
    Complete sign-in in the browser as described under [What users see](#what-users-see), select **Continue** if the pane shows it, and step through the welcome screens.
  </Step>

  <Step title="Ask Claude about the file">
    Ask Claude a question about the open file and confirm it answers.
  </Step>
</Steps>
