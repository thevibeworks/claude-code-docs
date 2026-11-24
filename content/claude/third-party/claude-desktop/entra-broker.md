> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sign in through the OS identity broker

> Use the operating system's native Microsoft Entra sign-in broker so Claude Desktop on 3P satisfies device-based Conditional Access policies

Several Claude Desktop on 3P features can authenticate to Microsoft Entra ID, including the Microsoft Foundry inference provider, gateway and Workforce Identity sign-in when Entra ID is the identity provider, managed MCP servers, and the Microsoft 365 connector. Each of these can run its Entra sign-in through the operating system's native identity broker instead of a browser or device code. To turn on the broker for a feature, see [Where the broker is used](#where-the-broker-is-used).

## What the broker is

The OS identity broker is the operating system's built-in Microsoft sign-in component. On Windows it is Web Account Manager (WAM), which ships with Windows 10 and later. On macOS it is provided by the Intune Company Portal app together with the Microsoft Enterprise SSO plug-in. When Claude Desktop signs in through the broker, the operating system shows its own account picker, the user selects or signs in to a work account, and the broker issues the token. Nothing opens in a web browser, and the app never handles the user's password.

## Why use the broker

The broker is the most reliable sign-in flow for Microsoft Entra Conditional Access policies that require a compliant or managed device, or that require token protection, because it always carries the device identity claim those policies evaluate. Device-code sign-in never carries that claim. Browser sign-in carries it only when the browser itself is integrated with device identity (for example, Microsoft Edge signed in with the work account on an Entra-joined Windows device, or a macOS browser with Microsoft's Enterprise SSO integration deployed). The broker satisfies these policies on any supported device without relying on browser configuration.

The broker also removes the need for a `localhost` or `127.0.0.1` loopback redirect on the device, which some network policies block, and it is not affected by Conditional Access policies that block the device-code authentication flow.

## Where the broker is used

| Feature | How to enable it | Page |
| - | - | - |
| Microsoft Foundry inference provider | Set `inferenceFoundryAuthFlow` to `broker` | [Microsoft Foundry](https://claude.com/docs/third-party/claude-desktop/foundry.md#in-app-entra-id-sign-in) |
| LLM gateway single sign-on | Set `inferenceGatewayOidcAuthFlow` to `broker` | [LLM gateway](https://claude.com/docs/third-party/claude-desktop/gateway.md#single-sign-on-configuration-keys) |
| Workforce Identity sign-in for Google Cloud's Agent Platform | Set `inferenceVertexWorkforceAuthFlow` to `broker` | [Google Cloud's Agent Platform](https://claude.com/docs/third-party/claude-desktop/vertex.md#in-app-workforce-identity-sign-in) |
| Amazon Bedrock identity provider sign-in (through a proxy) | Set `inferenceIdpAuthFlow` to `broker` | [Amazon Bedrock](https://claude.com/docs/third-party/claude-desktop/bedrock.md#sign-in-with-your-identity-provider) |
| Managed MCP server | Set `authFlow` to `broker` in the entry's `oauth` object | [Managed MCP servers](https://claude.com/docs/third-party/claude-desktop/extensions.md#managed-mcp-servers-admin) |

For the gateway, Amazon Bedrock, and Workforce Identity flows, the broker is available only when your identity provider is Microsoft Entra ID: the `issuer` in `inferenceGatewayOidc`, `inferenceIdpOidc`, or `inferenceVertexWorkforceOidc` must have the form `https://login.microsoftonline.com/TENANT_ID/v2.0`. For a managed MCP server, the `oauth` object must also set `tenantId`, `clientId`, and `scope`. For a GCC High or DoD tenant, see [GCC High and DoD tenants](#gcc-high-and-dod-tenants).

The [Microsoft 365 connector](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md#how-users-sign-in) also uses the OS broker for its own Entra sign-in. Its broker setup is documented on that page, and its app registration needs the same settings described under [Register the Entra ID application](#register-the-entra-id-application).

## Platform support

Brokered sign-in is available on Windows and macOS. Linux has no OS identity broker.

What happens on Linux, or on a Windows or macOS device where the broker is unavailable, depends on the feature. For the inference sign-in flows (Foundry, gateway, Amazon Bedrock, and Workforce Identity), the app shows an error that names the browser flow as the alternative rather than falling back to a browser or device-code flow, because a silent fallback would bypass the device policy the broker was chosen to satisfy. Managed MCP servers and the [Microsoft 365 connector](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md#how-users-sign-in) fall back to the system browser instead. To make the Microsoft 365 connector's sign-in fail rather than fall back, set [`microsoftAuthBroker`](https://claude.com/docs/third-party/claude-desktop/configuration#microsoftauthbroker) to `required` (Claude Desktop 1.49585.0 or later).

## GCC High and DoD tenants

Brokered sign-in for Microsoft Foundry, gateway, Amazon Bedrock, Workforce Identity, and managed MCP servers works with commercial and Microsoft 365 GCC tenants only. For these features, Claude Desktop asks the broker to sign in at `login.microsoftonline.com`. GCC High and DoD tenants sign in at `login.microsoftonline.us`. This limit doesn't apply to the local [Microsoft 365 connector](https://claude.com/docs/third-party/claude-desktop/connectors-m365.md#set-up-the-local-connector), which signs in at the host that its `azureCloud` setting selects.

For a GCC High or DoD tenant, set up the following features to sign in through the system browser:

* **Managed MCP server**: in the entry's [`oauth` object](https://claude.com/docs/third-party/claude-desktop/mcp-sign-in#oauth-fields), set `authorizationServer` to `["https://login.microsoftonline.us/TENANT_ID/v2.0"]` alongside `clientId` and `scope`. Leave `tenantId` and `authFlow` unset. Register the [loopback redirect URI](https://claude.com/docs/third-party/claude-desktop/extensions.md#oauth-sign-in). If sign-in fails with Microsoft Entra error `AADSTS9010010`, see [Omit the resource parameter](https://claude.com/docs/third-party/claude-desktop/mcp-sign-in.md#omit-the-resource-parameter).
* **Gateway, Amazon Bedrock, and Workforce Identity**: set the `issuer` in `inferenceGatewayOidc`, `inferenceIdpOidc`, or `inferenceVertexWorkforceOidc` to `https://login.microsoftonline.us/TENANT_ID/v2.0`. Set `inferenceGatewayOidcAuthFlow`, `inferenceIdpAuthFlow`, or `inferenceVertexWorkforceAuthFlow` to `browser`, or leave the key unset. Register the redirect URI `http://127.0.0.1/callback`.

If your Conditional Access policy requires a compliant or managed device, browser sign-in satisfies it only when the browser is [integrated with device identity](#why-use-the-broker).

For Microsoft Foundry, the device-code and browser flows also sign in at `login.microsoftonline.com`, so a different sign-in flow doesn't change the host.

## Register the Entra ID application

Brokered sign-in places two requirements on the Entra ID app registration that the feature signs in against. These are in addition to whatever API permissions the feature itself needs.

Under **Authentication**, set **Allow public client flows** to **Yes**. The control is on the **Settings** tab under **Web and SPA settings** (on older versions of the portal, under **Advanced settings**). Brokered token requests carry no client secret, so Entra ID relies on this setting to classify the app as a public client. With it set to No, brokered sign-in fails with error code `AADSTS7000218`.

Under **Authentication**, add the broker redirect URI for each platform you deploy to under the **Mobile and desktop applications** platform:

| Platform | Redirect URI |
| - | - |
| Windows | `ms-appx-web://Microsoft.AAD.BrokerPlugin/APPLICATION_CLIENT_ID` |
| macOS | `msauth.com.anthropic.claudefordesktop://auth` |

Replace `APPLICATION_CLIENT_ID` in the Windows value with the registration's own Application (client) ID. The macOS value is a fixed string.

## Prepare devices

On Windows, WAM is built into the operating system. The device must be Entra joined, Entra hybrid joined, or Entra registered so the broker has a work account to present. For Conditional Access policies that require a compliant device, the device must also be marked compliant in Intune (or hybrid joined) as your policy requires.

On macOS, the broker is provided by Intune Company Portal. Each device needs:

* Intune Company Portal installed.
* An Extensible SSO configuration profile of type Redirect, pointed at the Microsoft Enterprise SSO plug-in, deployed through your MDM. The broker is unavailable without it.
* Enrollment in an MDM and registration in Entra ID. For Conditional Access policies that require a compliant device, the device must also be marked compliant in Intune as your policy requires. For MDMs other than Intune, use the partner device-compliance integration that reports compliance to Intune and Entra.

## Token storage

The operating system's broker holds the credential and renews it silently from the device's primary refresh token. The app stores only a reference to the signed-in account, not a refresh token. When the broker can no longer renew silently (for example, the device falls out of compliance or the user's sessions are revoked in Entra), the app prompts the user to sign in again.

Claude Code in the terminal doesn't use the broker. If you let it sign in to your gateway with the browser, it can store a refresh token on the computer. See [Allow browser sign-in where your gateway uses the Entra broker](#allow-browser-sign-in-where-your-gateway-uses-the-entra-broker).

## Allow browser sign-in where your gateway uses the Entra broker

Claude Code in the terminal can't use the OS identity broker. If you [manage Claude Code in the terminal from the Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md) and your gateway's sign-in flow is `broker`, Claude Code can't use your gateway. In that case, after a developer signs in to your organization, Claude Code doesn't start unless the developer's computer sets a provider itself. You can turn on a switch so that Claude Code signs in with the browser instead, while Claude Desktop still uses the broker. The switch changes the following:

* **Provider settings**: the next time a signed-in developer starts Claude Code, your gateway replaces their own provider settings and `apiKeyHelper`
* **Gateway sign-in**: the developer approves the gateway's address and then signs in to the gateway, with `/login` in Claude Code. Until then, Claude Code refuses each prompt.
* **Stored sign-in**: the browser sign-in stays on the developer's computer, with a refresh token if Entra returns one. On Linux and Windows, the sign-in is in the unencrypted file `.credentials.json`. Some Windows computers use Windows Credential Manager instead.

**1. Add the redirect URI**

In your Entra app registration, add `http://127.0.0.1/gateway-sign-in/callback` under **Mobile and desktop applications**. If your **Redirect host** is `localhost`, add the `localhost` form. If the portal refuses the address, add it in the app manifest as a redirect URI for a public client (mobile and desktop).

**2. Check consent and Conditional Access**

If your tenant requires it, grant consent for `offline_access`. If your Conditional Access policies check the device, set up developers' browsers to identify the device, as described in [Why use the broker](#why-use-the-broker). A browser can't meet a policy that requires token protection.

**3. Turn on both switches**

Go to **Organization settings > Products > Claude Code**, and turn on the **Allow sign-in from Claude Code in terminals and IDEs** switch. Then turn on the **Allow Claude Code to sign in with the browser instead of the Entra broker** switch, which appears when the first switch is on, and click **Save changes**. To test with one group first, if your organization has a parent organization, turn on both switches in the **Claude Code** section of that group's policy instead.

To store no refresh token, fill in **Scopes** without `offline_access`. If **Bearer token** is **Access token**, also turn off **Append offline\_access**. Developers then sign in again each time the token expires. **Scopes** also applies to Claude Desktop.

If you turn the browser sign-in switch off, the change applies the next time each developer starts Claude Code. Turning the switch off revokes nothing. The token stays on the computer until the developer runs `claude auth logout` in their terminal. To stop the stored refresh tokens from working, revoke the developers' sessions in Entra. Revoking the sessions also ends the developers' other Microsoft sign-ins, and Claude Desktop asks the developers to sign in again.

## Troubleshoot

If sign-in fails with error code `AADSTS7000218`, **Allow public client flows** is set to No on the app registration. Set it to **Yes** under **Authentication**.

If sign-in fails with error code `AADSTS50011` or `AADSTS900971`, the platform's broker redirect URI is missing from the app registration or does not exactly match the value under [Register the Entra ID application](#register-the-entra-id-application). Add or correct it under **Authentication → Mobile and desktop applications**.

If sign-in fails with a message that the OS identity broker is unavailable, the device does not meet the requirements under [Prepare devices](#prepare-devices). On macOS, confirm Company Portal is installed and the Enterprise SSO configuration profile is deployed. On Windows, confirm the device is Entra joined or registered.

The broker writes its own diagnostic log outside the app. On Windows, WAM events appear in Event Viewer under **Applications and Services Logs → Microsoft → Windows → AAD → Operational**. On macOS, Company Portal writes to the unified log; view it with `log show --predicate 'subsystem == "com.microsoft.CompanyPortalMac"' --last 1h` in Terminal. The app's own log records when a brokered sign-in was attempted and the error it returned; see [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) for the log location.
