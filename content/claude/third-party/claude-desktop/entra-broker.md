> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sign in through the OS identity broker

> Use the operating system's native Microsoft Entra sign-in broker so Claude Desktop on 3P satisfies device-based Conditional Access policies

Several Claude Desktop on 3P features can authenticate to Microsoft Entra ID, including the Microsoft Foundry inference provider, gateway and Workforce Identity sign-in when Entra ID is the identity provider, managed MCP servers, and the Microsoft 365 connector. Each of these can run its Entra sign-in through the operating system's native identity broker instead of a browser or device code. This page covers what the broker is, when to choose it, and the prerequisites that apply wherever the app uses it. The feature-specific pages linked under [Where the broker is used](#where-the-broker-is-used) describe how to turn it on for each feature.

## What the broker is

The OS identity broker is the operating system's built-in Microsoft sign-in component. On Windows it is Web Account Manager (WAM), which ships with Windows 10 and later. On macOS it is provided by the Intune Company Portal app together with the Microsoft Enterprise SSO plug-in. When Claude Desktop signs in through the broker, the operating system shows its own account picker, the user selects or signs in to a work account, and the broker issues the token. Nothing opens in a web browser, and the app never handles the user's password.

## Why use the broker

The broker is the most reliable sign-in flow for Microsoft Entra Conditional Access policies that require a compliant or managed device, or that require token protection, because it always carries the device identity claim those policies evaluate. Device-code sign-in never carries that claim. Browser sign-in carries it only when the browser itself is integrated with device identity (for example, Microsoft Edge signed in with the work account on an Entra-joined Windows device, or a macOS browser with Microsoft's Enterprise SSO integration deployed). The broker satisfies these policies on any supported device without relying on browser configuration.

The broker also removes the need for a `localhost` or `127.0.0.1` loopback redirect on the device, which some network policies block, and it is not affected by Conditional Access policies that block the device-code authentication flow.

## Where the broker is used

| Feature                                                      | How to enable it                                         | Page                                                                                                  |
| ------------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Microsoft Foundry inference provider                         | Set `inferenceFoundryAuthFlow` to `broker`               | [Microsoft Foundry](/docs/third-party/claude-desktop/foundry#in-app-entra-id-sign-in)                      |
| LLM gateway single sign-on                                   | Set `inferenceGatewayOidcAuthFlow` to `broker`           | [LLM gateway](/docs/third-party/claude-desktop/gateway#single-sign-on-configuration-keys)                  |
| Workforce Identity sign-in for Google Cloud's Agent Platform | Set `inferenceVertexWorkforceAuthFlow` to `broker`       | [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex#in-app-workforce-identity-sign-in) |
| Managed MCP server                                           | Set `authFlow` to `broker` in the entry's `oauth` object | [Managed MCP servers](/docs/third-party/claude-desktop/extensions#managed-mcp-servers-admin)               |

For the gateway and Workforce Identity flows, the broker is available only when your identity provider is Microsoft Entra ID: the `issuer` in `inferenceGatewayOidc` or `inferenceVertexWorkforceOidc` must have the form `https://login.microsoftonline.com/TENANT_ID/v2.0`. For a managed MCP server, the `oauth` object must also set `tenantId`, `clientId`, and `scope`.

The [Microsoft 365 connector](/docs/third-party/claude-desktop/connectors-m365#how-users-sign-in) also uses the OS broker for its own Entra sign-in. Its broker setup is documented on that page, and its app registration needs the same settings described under [Register the Entra ID application](#register-the-entra-id-application).

## Platform support

Brokered sign-in is available on Windows and macOS. Linux has no OS identity broker.

What happens on Linux, or on a Windows or macOS device where the broker is unavailable, depends on the feature. For the inference sign-in flows (Foundry, gateway, and Workforce Identity), the app shows an error that names the browser flow as the alternative rather than falling back to a browser or device-code flow, because a silent fallback would bypass the device policy the broker was chosen to satisfy. Managed MCP servers and the [Microsoft 365 connector](/docs/third-party/claude-desktop/connectors-m365#how-users-sign-in) fall back to the system browser instead.

## Register the Entra ID application

Brokered sign-in places two requirements on the Entra ID app registration that the feature signs in against. These are in addition to whatever API permissions the feature itself needs.

Under **Authentication**, set **Allow public client flows** to **Yes**. The control is on the **Settings** tab under **Web and SPA settings** (on older versions of the portal, under **Advanced settings**). Brokered token requests carry no client secret, so Entra ID relies on this setting to classify the app as a public client. With it set to No, brokered sign-in fails with error code `AADSTS7000218`.

Under **Authentication**, add the broker redirect URI for each platform you deploy to under the **Mobile and desktop applications** platform:

| Platform | Redirect URI                                                     |
| -------- | ---------------------------------------------------------------- |
| Windows  | `ms-appx-web://Microsoft.AAD.BrokerPlugin/APPLICATION_CLIENT_ID` |
| macOS    | `msauth.com.anthropic.claudefordesktop://auth`                   |

Replace `APPLICATION_CLIENT_ID` in the Windows value with the registration's own Application (client) ID. The macOS value is a fixed string.

## Prepare devices

On Windows, WAM is built into the operating system. The device must be Entra joined, Entra hybrid joined, or Entra registered so the broker has a work account to present. For Conditional Access policies that require a compliant device, the device must also be marked compliant in Intune (or hybrid joined) as your policy requires.

On macOS, the broker is provided by Intune Company Portal. Each device needs:

* Intune Company Portal installed.
* An Extensible SSO configuration profile of type Redirect, pointed at the Microsoft Enterprise SSO plug-in, deployed through your MDM. The broker is unavailable without it.
* Enrollment in an MDM and registration in Entra ID. For Conditional Access policies that require a compliant device, the device must also be marked compliant in Intune as your policy requires. For MDMs other than Intune, use the partner device-compliance integration that reports compliance to Intune and Entra.

## Token storage

The operating system's broker holds the credential and renews it silently from the device's primary refresh token. The app stores only a reference to the signed-in account, not a refresh token. When the broker can no longer renew silently (for example, the device falls out of compliance or the user's sessions are revoked in Entra), the app prompts the user to sign in again.

## Troubleshoot

If sign-in fails with error code `AADSTS7000218`, **Allow public client flows** is set to No on the app registration. Set it to **Yes** under **Authentication**.

If sign-in fails with error code `AADSTS50011` or `AADSTS900971`, the platform's broker redirect URI is missing from the app registration or does not exactly match the value under [Register the Entra ID application](#register-the-entra-id-application). Add or correct it under **Authentication → Mobile and desktop applications**.

If sign-in fails with a message that the OS identity broker is unavailable, the device does not meet the requirements under [Prepare devices](#prepare-devices). On macOS, confirm Company Portal is installed and the Enterprise SSO configuration profile is deployed. On Windows, confirm the device is Entra joined or registered.

The broker writes its own diagnostic log outside the app. On Windows, WAM events appear in Event Viewer under **Applications and Services Logs → Microsoft → Windows → AAD → Operational**. On macOS, Company Portal writes to the unified log; view it with `log show --predicate 'subsystem == "com.microsoft.CompanyPortalMac"' --last 1h` in Terminal. The app's own log records when a brokered sign-in was attempted and the error it returned; see [Data storage and residency](/docs/third-party/claude-desktop/data-storage) for the log location.
