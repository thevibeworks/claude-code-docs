> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Claude for Microsoft 365 from the Enterprise Admin Console

> Turn on sign-in for Claude for Excel, PowerPoint, Word, and Outlook from the Enterprise Admin Console, and manage the add-in's settings there.

If you manage Claude Desktop from the
[Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), you
can manage Claude for Microsoft 365 there too.

## How console settings reach the add-in

A member signs in from the add-in with their Claude account. The add-in
then gets its connection and its settings from the console. Prompts still
go to your gateway or cloud provider.

Your settings apply only to members who sign in to this organization.
Members can change the connection. Control access at your gateway or
provider.

For what the add-in sends to Anthropic, see
[What leaves the device](https://claude.com/docs/office-agents/data-storage.md#what-leaves-the-device).
For the features that members get, see the third-party platform column in
[Differences from signing in with a Claude account](https://claude.com/docs/office-agents/third-party-platforms.md#differences-from-signing-in-with-a-claude-account).

## Before you start

Ensure that:

* You're an Owner or Primary Owner of the organization.
* Your users are members of the organization.
* The Connection page under Desktop 3P is saved. Bedrock Mantle and
  custom Bedrock base URLs aren't supported.
* Your provider meets the add-in's
  [requirements](https://claude.com/docs/office-agents/third-party-platforms.md#requirements-by-connection-path).
* If you use a gateway, it accepts members' tokens as
  `Authorization: Bearer` and
  [allows CORS](https://claude.com/docs/office-agents/third-party-platforms.md#cors-requirements)
  from `https://pivot.claude.ai`, including the `authorization` header.
* Your network allows the
  [third-party platform domains](https://claude.com/docs/office-agents/third-party-platforms.md#third-party-platforms-3p),
  plus `claude.ai`, `api.anthropic.com`, `hcaptcha.com`, and
  `*.hcaptcha.com`.

If your add-in gets gateway or Foundry credentials from Microsoft Entra ID
or a bootstrap endpoint, keep that setup and leave sign-in off. A member who
signs in to this organization stops using that setup. They need a token or
key instead, and it doesn't renew.

## Turn on sign-in

Sign-in from the add-in is off by default.

> [!WARNING]
>
> A member who selects "Log in" can also sign in with another paid Claude
> account or organization. This is true whether sign-in is on or off. With a
> personal plan, for example, the add-in sends prompts and document content
> to Anthropic, and your console settings don't apply.
>
> To block personal plans and organizations that you don't allow, set up
> [tenant restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)
> and include this organization's ID in the allowed list. Tenant
> restrictions need a proxy with TLS inspection, and they cover only traffic
> through that proxy. A member can still authorize the sign-in from a device
> or network that doesn't use the proxy, such as a phone or a home network.

**1. Open the Office Agents page**

On claude.ai, switch to the organization and open Organization
settings, Products, Office Agents.

**2. Turn on the switch**

Turn on "Allow sign-in from the Claude add-in". If your provider is
Bedrock, also enter "IAM role for the Microsoft 365 add-in". Select
"Save changes".

**3. Deploy the add-in**

Deploy the add-in from Microsoft AppSource for
[Excel, PowerPoint, and Word](https://claude.com/docs/office-agents/excel.md#deploy-to-your-organization)
or [Outlook](https://claude.com/docs/office-agents/outlook.md#deploy-to-your-organization).
Outlook also needs Microsoft Graph admin consent.

If you can't deploy from AppSource, use the manifest file for
[Excel](https://claude.com/docs/office-agents/excel.md#deploy-to-your-organization),
[PowerPoint](https://claude.com/docs/office-agents/powerpoint.md#deploy-with-a-custom-manifest),
[Word](https://claude.com/docs/office-agents/word.md#deploy-with-a-custom-manifest), or
[Outlook](https://claude.com/docs/office-agents/outlook.md#install-from-a-manifest-file).
Either way, replace any manifest made for a third-party platform,
because it can hide "Log in".

**4. Give members a credential**

Give members the credential for your provider:

* **Gateway**: a gateway token
* **Foundry**: a Foundry API key
* **Vertex AI**: a Google client ID and secret
* **Bedrock**: no credential

The add-in can't use Claude Desktop's sign-in or helper script for your
provider.

## Sign in as a member

Send members these steps. Replace `<organization name>` with the
organization's name as shown on claude.ai.

A member whose add-in is already connected logs out first. Logging out
[deletes their saved Outlook conversations](https://claude.com/docs/office-agents/data-storage.md#outlook-data-deleted-when-a-sign-in-ends).

You can start from this text:

```text wrap theme={null}
Please sign in to <organization name> from the Claude add-in in Excel, PowerPoint, Word, or Outlook.

1. Open the add-in. If it's already connected, select "Logout" from the "More options" menu, then "Sign out" if asked. Logging out deletes your saved Outlook conversations.
2. Select "Log in". In the browser, select "Connect". If asked, pick the organization marked "Enterprise 3P".
3. Check that the page shows "Authorizing for" with <organization name>. Only then select "Authorize".
   - If it shows something else, select "Switch organization", pick <organization name>, and select "Authorize".
   - If you can't switch to it, select "Decline" and log out of claude.ai in that browser. Then repeat step 2 and sign in with your work Claude account.
4. In the add-in, enter the credential from your admin and select "Continue". With Bedrock, the add-in uses your Microsoft work account instead.
```

## Change settings or turn off sign-in

The Office Agents page controls Office apps, features, document access
policies, and skills.

The add-in also uses the console's model list, OpenTelemetry collector, and
supported MCP servers. The
[collector](https://claude.com/docs/office-agents/opentelemetry.md#endpoint-requirements) and the
servers must allow CORS too.

* **When changes take effect**: a change usually reaches an add-in that's
  online within about 10 minutes. If it doesn't, ask the member to restart
  the Office app.
* **After you change the connection**: ask members to select "Logout" and
  sign in again. Logging out deletes their saved Outlook conversations.
  A new gateway address or header applies without logging out if their
  token still works.
* **To turn off sign-in**: turn off the switch and select "Save changes".
  Members then see "Claude
  isn't available for your organization here".
