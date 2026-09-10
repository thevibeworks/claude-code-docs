> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot federated cloud access

> Errors from Claude Tag's federated cloud access and what fixes each: console dialog messages, requests Claude reports as blocked or failed, and rejections your gateway, AWS, Google Cloud, or authorization server records.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Federated connections are managed at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation. Changing them needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

This page covers what goes wrong after you connect a gateway, AWS role, Google Cloud identity, or authorization server through **Federated cloud access**. It's organized by where the problem shows up: a message in a console dialog, an error Claude reports in the thread, or a rejection in your own logs. The token terms used below are explained on the [identity token reference](/docs/claude-tag/admins/federated-access/token-reference).

First confirm two things that have nothing to do with federation:

* The connection is in an [Access bundle attached to the channel's scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle). For a gateway, the scope's custom instructions also [name the gateway's address](/docs/claude-tag/admins/federated-access/connect-a-gateway#let-agents-reach-the-gateway), so Claude knows the gateway exists.
* You tested in a new thread. A thread already running isn't told about a connection added after it started; ask Claude for the service by name, or send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) at the channel's top level.

If Claude reports that a host isn't allowed before any request is sent, see [Claude says a host isn't allowed](/docs/claude-tag/admins/troubleshooting#claude-says-a-host-isn%E2%80%99t-allowed-or-it-can%E2%80%99t-reach-the-internet).

## Messages in the console

Most dialog messages say what to do. The table adds what the message doesn't. The one message that needs more, "The check didn't pass", has its own entry below the table, followed by what removing and reconnecting a gateway does.

| Message                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | What it means                                                                                                                                                                                                                                                                                                                                                                                                                               | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "The check can't run right now. Try again later, or skip the check and record why."                                                                                                                                                                                                                                                                                                                                                                                                  | Anthropic couldn't produce the test tokens for the connection check. The problem is on Anthropic's side, not your gateway's.                                                                                                                                                                                                                                                                                                                | Wait a few minutes and click **Run check and connect** again. If the message persists, select the **Skip the check** option, enter a **Reason for skipping**, and click **Connect without the check**; remove and reconnect the gateway later to record a passed check.                                                                                                                                                                   |
| "Too many checks in a short time." followed by how long to wait                                                                                                                                                                                                                                                                                                                                                                                                                      | Your organization ran the connection check too many times in quick succession. The limit counts every admin in the organization. Entering an address that is already registered runs the check again and counts too, unless the **Skip the check** option is selected.                                                                                                                                                                      | Wait the time the message names. To add an existing gateway to a bundle, click **Add to bundle** in its row of the **Gateways** table instead of entering its address again.                                                                                                                                                                                                                                                              |
| "Too many attempts in a short time." in the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                                                                                                                               | A general request limit, not the connection check; registering a token endpoint never runs the check.                                                                                                                                                                                                                                                                                                                                       | Wait the time the message names and try again.                                                                                                                                                                                                                                                                                                                                                                                            |
| "Connecting a gateway needs full Claude Tag management permission. Ask an organization owner." or "This needs full Claude Tag management permission. Ask an organization owner."                                                                                                                                                                                                                                                                                                     | Your account can't change federated connections. Channel managers, and admins whose Claude Tag permission covers specific channels only, can't connect a gateway, cloud role, or authorization server.                                                                                                                                                                                                                                      | Ask an organization Owner, or an admin with full Claude Tag management permission, to make the connection from their own account.                                                                                                                                                                                                                                                                                                         |
| A dialog message containing "isn't enabled for your organization yet", or **Federated cloud access** is missing from the left navigation                                                                                                                                                                                                                                                                                                                                             | Federated cloud access isn't available to organizations whose compliance configuration excludes it. The navigation item is also hidden from channel managers and from admins whose Claude Tag permission covers specific channels only, because connecting a system needs full Claude Tag management permission.                                                                                                                            | Ask an organization Owner, or an admin with full Claude Tag management permission, to open the page. If it's missing for them too, your organization's compliance configuration excludes the feature.                                                                                                                                                                                                                                     |
| "This organization has reached its limit of 5 gateways. Remove one to connect another." or, in the **Connect an authorization server** dialog, "…limit of 5 registered gateways, which includes token endpoints."                                                                                                                                                                                                                                                                    | An organization can register 5 addresses. A token endpoint is registered the same way as a gateway, so it counts toward the same 5 and appears in the **Gateways** table marked "Used by a connected authorization server. Manage it from the Authorization servers section." An address is either a gateway or a token endpoint in your organization, not both.                                                                            | In the **Gateways** table, click **Remove** in the row of a gateway you no longer use. To free a token endpoint's row, click **Remove** in the server's row of the **Authorization servers** table first, then remove the endpoint from the **Gateways** table. See [Removing and reconnecting a gateway](#removing-and-reconnecting-a-gateway).                                                                                          |
| "This gateway is already registered. Close this dialog and pick it from the list to add it to a bundle."                                                                                                                                                                                                                                                                                                                                                                             | The address is already registered in your organization, and the dialog couldn't load its row to continue. This message is rare: entering a registered address normally runs the connection check again without changing the stored result, then moves on to the bundle step.                                                                                                                                                                | Click **Cancel**, then click **Add to bundle** in the gateway's row of the **Gateways** table.                                                                                                                                                                                                                                                                                                                                            |
| "`<address>` is already in the bundle `<bundle>`. Assign that bundle to a channel to use the gateway there.", "This role is already connected in the bundle `<bundle>`.", or "This token endpoint is already connected in the bundle `<bundle>`."                                                                                                                                                                                                                                    | A gateway, AWS role, or token endpoint can be connected in only one Access bundle, and this one already is.                                                                                                                                                                                                                                                                                                                                 | To use the connection in more channels, [attach that bundle to each scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) instead. To move it, in **Access bundles**, open the bundle's **Credentials** tab, open the **⋮** menu on the connection's row, and choose **Delete**. Then add it to the new bundle: **Add to bundle** in the gateway's row of the **Gateways** table, or the connect dialog again for the other types. |
| "`<name>` already covers `<host>` in this bundle, so Claude would never use this connection for the hosts they share. Change the hosts or choose another bundle." in the **Connect a Google Cloud identity** dialog                                                                                                                                                                                                                                                                  | Another Google Cloud connection in the bundle you chose already has that host under **Allowed hosts**, whatever its provider or service account. Claude uses the first connection in a bundle whose hosts match a request, so the new connection would never be used for the shared host. A wildcard such as `*.googleapis.com` covers every subdomain but not `googleapis.com` itself. The dialog won't connect until the overlap is gone. | Remove the shared host from the new connection's **Allowed Google hosts**, or choose another bundle. To give the host to the new connection instead, first narrow the existing one: in **Access bundles**, open the bundle's **Credentials** tab, open the **⋮** menu on the connection's row, choose **Edit**, and change **Allowed hosts**.                                                                                             |
| "Couldn't connect the gateway. Try again.", "Couldn't add the gateway to the bundle.", "Couldn't connect the role. Try again.", "Couldn't connect the identity. Try again.", "Couldn't register the authorization server. Try again.", or "Couldn't connect the authorization server. Try again."                                                                                                                                                                                    | The request failed for a reason the dialog doesn't name, most often a temporary one.                                                                                                                                                                                                                                                                                                                                                        | Try once more. If the message persists, contact your Anthropic account team with the details under [Contact Anthropic](#contact-anthropic).                                                                                                                                                                                                                                                                                               |
| "The issuer URL must be an https URL on the same host as the token endpoint. Leave it empty to use the token endpoint as the audience." in the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                            | The **Issuer URL** value must be an HTTPS URL on the same host as the token endpoint, or empty. The token is only ever presented to that server, so its audience must name that server.                                                                                                                                                                                                                                                     | Enter the issuer identifier your authorization server uses, on the token endpoint's host, or clear the field to use the token endpoint as the audience.                                                                                                                                                                                                                                                                                   |
| "This token endpoint is already connected. Manage it from the Authorization servers section." in the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                                                                      | An authorization server with this token endpoint is already connected in one of your organization's Access bundles, and a server can be connected only once. The dialog checks this before it registers anything.                                                                                                                                                                                                                           | To use the server in more channels, [attach its bundle to each scope](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle). To connect it again, remove it first: in the **Authorization servers** table, click **Remove** in the server's row.                                                                                                                                                                                          |
| "That address is already connected as a gateway. Enter your authorization server's own addresses, or remove the gateway first." in the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                                    | The token endpoint, or the **Issuer URL** value, is the address of a gateway connected in one of your organization's Access bundles. One address can't be both, because a token sent to the gateway could be replayed to the server as a grant.                                                                                                                                                                                             | Enter the token endpoint and issuer identifier your authorization server publishes. To use that address for the server instead, remove the gateway first: in **Access bundles**, open the bundle that holds the gateway, open its **Credentials** tab, open the **⋮** menu on the gateway's row, and choose **Delete**. Then, in the **Gateways** table under **Federated cloud access**, click **Remove** in the gateway's row.          |
| "That address is registered by a connected authorization server. Enter your gateway's address, or remove the server first." in the **Connect a gateway** dialog                                                                                                                                                                                                                                                                                                                      | The address you entered is a connected authorization server's token endpoint or audience, for example a server whose **Issuer URL** is the bare host `https://auth.example.com`. One address can't be both, because a token sent to the gateway could be replayed to that server as a grant.                                                                                                                                                | Enter the host your gateway answers on. To use that address for a gateway instead, remove the server first: in the **Authorization servers** table, click **Remove** in the server's row.                                                                                                                                                                                                                                                 |
| "That address is already a connected authorization server's audience. Enter this server's own issuer URL." in the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                                                         | The **Issuer URL** value (or the token endpoint, when **Issuer URL** is empty) is already another connected authorization server's audience or token endpoint. Two servers can't share an audience, because a token minted for one would be valid at the other.                                                                                                                                                                             | In the **Issuer URL** field, enter the issuer identifier this server publishes. If the other server holds this identifier by mistake, remove that server first: in the **Authorization servers** table, click **Remove** in its row, then connect it again with its own issuer URL.                                                                                                                                                       |
| "The address is too long. Issuer URLs have at most 256 characters." under the **Issuer URL** field of the **Connect an authorization server** dialog                                                                                                                                                                                                                                                                                                                                 | The **Issuer URL** field accepts at most 256 characters, the same limit as the **Token endpoint** field.                                                                                                                                                                                                                                                                                                                                    | Check that the field holds only the issuer identifier, for example `https://auth.example.com`, and not a longer value pasted by mistake.                                                                                                                                                                                                                                                                                                  |
| "Couldn't check the addresses against your gateways and servers. Close this dialog and try again." in the **Connect an authorization server** dialog, or "Couldn't check the address against your authorization servers. Close this dialog and try again." in the **Connect a gateway** dialog                                                                                                                                                                                       | Before it registers an address, each dialog loads your organization's existing connections to check that the address doesn't clash with a connected gateway or authorization server. That list didn't load, and the dialog doesn't register an address it couldn't check.                                                                                                                                                                   | Close the dialog and open it again. If the message persists, reload the page, then contact your Anthropic account team with the details under [Contact Anthropic](#contact-anthropic).                                                                                                                                                                                                                                                    |
| An address-field message such as "Enter only the host, like [https://gateway.example.com](https://gateway.example.com), with no path, port or trailing slash.", "Enter a host name, not an IP address.", "That is an Anthropic address. Enter your own gateway's host name.", "That host name only works inside a private network. Enter a host name that is reachable from the internet.", or "That host is reserved for cloud token exchange. Enter your own gateway's host name." | A gateway address is an HTTPS host only, with a domain name of at least two labels. A token endpoint may have a path, but no port, query, fragment, or sign-in details. Neither can be an IP address, a private-network name, an Anthropic-owned host, or a host cloud providers use for token exchange.                                                                                                                                    | Enter the public address the service answers on, for example `https://gateway.example.com` or `https://auth.example.com/oauth2/token`. The console can't register a private address even with the check skipped.                                                                                                                                                                                                                          |

### The check didn't pass

**What you see**

The **Connect a gateway** dialog shows "The check didn't pass. Claude couldn't reach the gateway, or the gateway didn't reject a token whose subject isn't your organization while accepting one that is. Fix the gateway and run the check again, or skip the check and record why."

**What it means**

The connection check sent two requests to your gateway and didn't get the two answers it needs. The gateway must reject a token whose subject isn't your organization, and it must accept a token for your **Control subject**. The console shows this one message for every failed check, so it doesn't say which request failed. If this was a new address, nothing was registered.

**How to resolve**

The check sends an empty `POST` to the address itself, with nothing added after the host, twice. Work through the causes in order.

| Check                                                           | What to do                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude can reach the address from the internet over HTTPS       | Confirm the host resolves publicly, the TLS certificate is valid, and the gateway isn't behind a VPN.                                                                                                                                                  |
| An empty `POST` to the address itself is answered directly      | The check doesn't follow redirects, and any status other than the two expected ones fails it, including a 503 from a gateway that couldn't fetch the signing keys.                                                                                     |
| The token whose subject isn't your organization gets 401 or 403 | If the gateway answered 2xx, the subject check is missing or wrong.                                                                                                                                                                                    |
| The token for the **Control subject** gets 2xx                  | A gateway that rejects every token is usually missing the control subject, or has a wrong issuer, audience, or key setting. With the sample gateway, add the **Control subject** as a `principals` entry with `allowed_services: []` in `config.yaml`. |

A 503 from the gateway usually means it can't reach `https://identity.anthropic.com` to fetch the keys. For a gateway that rejects every token, [Your gateway rejects every token](#your-gateway-rejects-every-token) lists each setting to compare. If you deployed [Anthropic's sample gateway](https://github.com/anthropics/claude-tag-wif-gateway-sample), its `config.yaml` must carry your real organization ID in the control-subject entry.

If the gateway can't be fixed right away, select the **Skip the check** option, enter a **Reason for skipping**, and click **Connect without the check**. To run the check later, remove the gateway and connect it again; see [Removing and reconnecting a gateway](#removing-and-reconnecting-a-gateway).

### Removing and reconnecting a gateway

In the **Gateways** table, click **Remove** in the gateway's row. Claude stops using the gateway at once. A connection that used the gateway stays in its Access bundle but stops working, and Claude reports [request blocked: this credential's audience isn't registered as a gateway for this organization](#request-blocked-this-credential%E2%80%99s-audience-isn%E2%80%99t-registered-as-a-gateway-for-this-organization) until the gateway is registered again.

To reconnect, click **Connect a gateway** in the **Gateways** section and enter the same address. Registering the address restores the existing connection, which is still in the bundle, so don't add it to the bundle again; the dialog refuses if you try.

## Errors Claude reports in the thread

When a request from a channel can't be sent with a federated credential, it fails with an HTTP status and a one-line reason, which Claude usually quotes. Reasons with HTTP 403 and 502 end with the connection's name in parentheses, for example `("gateway.example.com")`. The two 503 reasons don't name the connection.

Messages that begin "request blocked" come with HTTP 403. The request was refused on purpose, and retrying won't help. A 503 is temporary. A 502 usually means AWS, Google Cloud, or your authorization server refused the token exchange. A response from your gateway or from the cloud API itself reaches Claude as is, so those show as whatever status the other side returned.

### request blocked: this credential only works in channel sessions, not personal ones

**What you see**

Claude's request got HTTP 403 with this reason.

**What it means**

Federated connections work only in Slack channels, where Claude acts under your organization's [agent identity](/docs/claude-tag/concepts/agent-identity). The request came from a direct message, or from another session running under a person's own account, which has no agent identity for the token to name.

**How to resolve**

Use the connection from a channel whose scope has the bundle attached. No setting enables it in direct messages.

### request blocked: this credential's audience isn't registered as a gateway for this organization

**What you see**

Claude's request got HTTP 403 with this reason.

**What it means**

The gateway was removed from the **Gateways** table, but its connection is still in an Access bundle. Claude can't get a token for an address that isn't registered.

**How to resolve**

To keep the gateway, register the same address again; see [Removing and reconnecting a gateway](#removing-and-reconnecting-a-gateway). To drop it, in **Access bundles**, open the bundle's **Credentials** tab, open the **⋮** menu on the connection's row, and choose **Delete**.

### request blocked: Google (gcp) credentials aren't enabled for this organization

**What you see**

Claude's request got HTTP 403 with this reason.

**What it means**

A Google Cloud identity is connected in a bundle, but Google Cloud federation is off for your organization.

**How to resolve**

Contact your Anthropic account team with the details under [Contact Anthropic](#contact-anthropic).

### request blocked: this credential has restrict\_credential\_minting set, so Google's credential-minting endpoints are refused

**What you see**

Claude's request got HTTP 403 with this reason.

**What it means**

The Google Cloud identity was connected with **Block requests that mint new credentials** selected, and Claude tried to call a Google endpoint that creates keys, tokens, or other credentials. The block worked as intended.

**How to resolve**

Usually nothing: the block worked. If Claude needs that call, review the identity's IAM permissions first, because the block is a safeguard on top of IAM and not a replacement for it. The setting is chosen when the identity is connected, so in the **Cloud roles** table, click **Remove** in the identity's row, and connect the identity again with the **Block requests that mint new credentials** checkbox cleared.

### request blocked: this Google credential only works for requests to Google API hosts

**What you see**

Claude's request got HTTP 403 with this reason.

**What it means**

Claude tried to send a Google Cloud credential to a host Google doesn't serve. The credential is attached only to `googleapis.com`, its subdomains, and subdomains of `clients6.google.com`.

**How to resolve**

If the target is a Google API, check the host Claude used. If it isn't, the request needs a different connection.

### request blocked: this credential's allowed hosts include its own token endpoint

**What you see**

Claude's request got HTTP 403 with the reason "request blocked: this credential's allowed hosts include its own token endpoint; an admin must remove the token endpoint's host from the allowed hosts".

**What it means**

The authorization server connection's allowed hosts cover the token endpoint's own host, for example through a wildcard such as `*.example.com` that covers `auth.example.com`. The connect dialog refuses this when the connection is created, and so does every later edit of its allowed hosts, so the message isn't expected; the same rule is checked again on every request. The access token your server returns must never be sent back to the server that issued it, so every request with this connection is refused until an admin fixes it.

**How to resolve**

In **Access bundles**, open the bundle's **Credentials** tab, open the **⋮** menu on the connection's row, choose **Edit**, and in the **Edit connection** dialog set **Allowed hosts** to only the APIs Claude calls with the returned token, for example `api.example.com`, with no wildcard that covers the token endpoint's host. If the API and the token endpoint share a host, use a different host for one of them.

### credential injection temporarily unavailable; retry the request

**What you see**

Claude's request got HTTP 503 with this reason, or with "injection capacity exceeded; retry the request".

**What it means**

Something was briefly unavailable. Anthropic's identity service, your cloud provider's token exchange, or your authorization server answered with a server error (5xx) or 429, or timed out, or a failure moments earlier is still being backed off.

**How to resolve**

Ask Claude to retry. If one connection keeps failing this way, check that your authorization server or cloud provider is reachable and healthy, then contact your Anthropic account team with the details under [Contact Anthropic](#contact-anthropic).

### injection failed

**What you see**

Claude's request got HTTP 502 with the reason `injection failed ("<connection name>")`.

**What it means**

Most often, the system Claude's identity token was presented to refused the exchange. AWS refused `AssumeRoleWithWebIdentity`, Google Cloud's token exchange refused the token, or your authorization server answered the grant with an error. Claude's reply doesn't say why; your own logs do.

**How to resolve**

Look up the refusal where it happened and fix the configuration it names.

| Connection            | Where to look                                                                                                                                                    | Entry                                                                                       |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| AWS role              | CloudTrail, the `AssumeRoleWithWebIdentity` event for the role                                                                                                   | [AWS refuses AssumeRoleWithWebIdentity](#aws-refuses-assumerolewithwebidentity)             |
| Google Cloud identity | Cloud Audit Logs, the Security Token Service API entry for the token exchange and, if you named a service account, the IAM Service Account Credentials API entry | [Google Cloud refuses the token exchange](#google-cloud-refuses-the-token-exchange)         |
| Authorization server  | Your server's log for the `POST` to the token endpoint                                                                                                           | [Your authorization server rejects the grant](#your-authorization-server-rejects-the-grant) |

Allow for log delivery delay before concluding there was no attempt. If your logs show none at the time of the request, the token wasn't issued, and you should [contact Anthropic](#contact-anthropic) with the details listed there. A gateway connection doesn't produce this error. Your gateway's own response reaches Claude, so Claude reports the status your gateway returned, usually 401 or 403; see [Your gateway rejects every token](#your-gateway-rejects-every-token).

### The cloud API answers 403 after a successful exchange

**What you see**

Claude reports a 403 from an AWS or Google Cloud API, with the provider's own error body rather than a reason beginning "request blocked".

**What it means**

The token exchange worked and Claude called the API with the exchanged credential, but the role or identity lacks permission for that action. For Google Cloud, the exchange always requests the `cloud-platform` scope, so IAM alone decides what the credential can do.

**How to resolve**

Grant the IAM permission to the AWS role, the Google Cloud service account, or the federated identity when no service account is named. For AWS, a 403 also makes Claude assume the role again on the next request, so a fix takes effect on the next try.

## Rejections in your own logs

### Your gateway rejects every token

**What you see**

Every request from Claude gets 401 or 403 from your gateway, including the connection check's token for the **Control subject**.

**What it means**

One of the standard checks is configured with the wrong value. Your gateway's log of the failing check is the fastest route; if it logs nothing, work down the list. The values to compare against are shown in the **Connect a gateway** dialog before you enter an address, as described on [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway#copy-the-values-and-deploy-the-gateway).

**How to resolve**

| Check        | What to confirm                                                                                                                                                                                                                                                                                                                                                                              |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audience     | The `aud` claim is a JSON array with one element, your gateway address exactly as the console stored it: `https://` plus the lowercase host, no path or trailing slash. Use your library's audience option rather than comparing the raw claim to a string.                                                                                                                                  |
| Issuer       | Exactly `https://identity.anthropic.com/agents`, including the path. A verifier configured with any other issuer value, such as the bare host, a different path, or a trailing slash, rejects every token, including the connection check's token.                                                                                                                                           |
| Signing keys | Fetched from the JSON Web Key Set (JWKS) named in `https://identity.anthropic.com/agents/.well-known/openid-configuration`. Accept ES256 only. Select the key by `kid`, and refetch the JWKS on an unknown `kid` before rejecting.                                                                                                                                                           |
| Time         | The token expires 10 minutes after issue (`exp`) and is valid from 15 seconds before issue (`nbf`). Check `exp`, allowing up to 60 seconds of clock skew, and make sure your gateway's clock is right.                                                                                                                                                                                       |
| Subject      | The subject check accepts your listed agents' full subjects and the **Control subject**, or at minimum every subject starting with your **Subject prefix**, `wimse://identity.anthropic.com/org/<your organization ID>/agent/`, including the `/agent/`. A list that omits the **Control subject** fails the connection check, and a list that omits an agent rejects that agent's requests. |

### Your gateway sees the same token ID on many requests

**What you see**

Requests within a few minutes of each other carry a token with the same `jti`. A gateway that treats a repeated `jti` as a replay rejects almost everything.

**What it means**

This is normal. Claude reuses one token for a session's requests to the same gateway for about five minutes, or until your gateway answers 401, and then requests a new one. A plain 403 from your gateway doesn't refresh the token. Exchanges are different: AWS, Google Cloud, and an authorization server each see a token once per exchange.

**How to resolve**

Don't do per-request replay detection at a gateway. Rely on the signature, audience, expiry, and subject checks.

### Your gateway, trust policy, or IAM binding pins a full agent subject

**What you see**

One of two things. The connection check passed, but Claude's requests from a channel get 403 from your gateway. Or a gateway mapping, AWS trust policy condition, or Google Cloud IAM binding that matched a full subject ending in `/agent/cagt_...` stopped matching after the Slack channel was deleted and recreated.

**What it means**

Your rule accepts only specific agents. The connection check's **Control subject** is a reserved agent, so a rule listing it passes the check while rejecting real agents. And each channel's agent has its own ID: deleting and recreating a channel creates a new agent, so a pinned subject no longer appears in any token. By default the sample gateway accepts only the subjects listed in its configuration, and it logs the verified subject of each agent it rejects.

**How to resolve**

If you pin exact subjects, keep the list current. Log the verified subject of each rejected request, add each new agent's full subject to your rule (and, for a gateway, the **Control subject** with no access), and update the rule whenever a channel is deleted and recreated. The console doesn't display agent IDs, so your own logs are where you learn them. If keeping the list current isn't practical, accept every subject that starts with your **Subject prefix**, `wimse://identity.anthropic.com/org/<your organization ID>/agent/`, instead, which is the minimum form of the subject check. In the sample gateway, that is an `organization_principals` entry in `config.yaml`.

### AWS refuses AssumeRoleWithWebIdentity

**What you see**

Claude reports `injection failed` with HTTP 502, and CloudTrail shows an `AssumeRoleWithWebIdentity` event for the role with an error code.

**What it means**

STS refused to issue credentials for Claude's token. The trust relationship between your role and Anthropic's issuer isn't right.

**How to resolve**

| CloudTrail error       | What to confirm                                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InvalidIdentityToken` | The IAM OIDC identity provider's URL is exactly `https://identity.anthropic.com/agents`, with the `/agents` path (AWS displays it without `https://`), and its audience list includes `sts.amazonaws.com`.                                                                                                                                                                                                 |
| `AccessDenied`         | The trust policy's condition keys start with `identity.anthropic.com/agents:`; the `aud` condition is `StringEquals` on `sts.amazonaws.com`; the `sub` condition matches the token's subject, either `StringEquals` on this agent's full subject or `StringLike` on `wimse://identity.anthropic.com/org/<your organization ID>/agent/*`. `AccessDenied` also appears when the role was deleted or renamed. |
| Any other code         | AWS's STS documentation describes it. If the two rows above check out, the token itself is fine.                                                                                                                                                                                                                                                                                                           |

AWS credentials are reused for up to an hour for the same agent, so several threads' requests can appear under one CloudTrail session, and a trust policy change takes effect only when those credentials expire or AWS answers a request with 403.

### Google Cloud refuses the token exchange

**What you see**

Claude reports `injection failed ("<connection name>")` with HTTP 502. Google's token exchange rejected the token, or the service account impersonation that follows it was refused. Claude shows this one message for every refusal from Google, so the message doesn't say which check failed.

**What it means**

The workload identity pool's provider or attribute condition doesn't accept the token, or the federated identity can't act as the service account you named.

**How to resolve**

Google records the reason in your Cloud Audit Logs. The Security Token Service API entry covers the token exchange, and, if you named a service account, the IAM Service Account Credentials API entry covers the impersonation. Both are Data Access audit logs, which Google keeps off by default, as described under [Verify the connection](/docs/claude-tag/admins/federated-access/gcp#verify-the-connection). If the logs were on and show no entry at the time of the request, the token wasn't issued; see [injection failed](#injection-failed). Otherwise, work through the checks in order.

| Check                                   | What to confirm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attribute condition                     | The provider's attribute condition accepts this token. A condition that lists full subjects must include this agent's subject. A condition on your **Subject prefix**, `assertion.sub.startsWith("wimse://identity.anthropic.com/org/<your organization ID>/agent/")`, accepts every agent in your organization, as does `attribute.org == "<your organization ID>"` if you mapped `attribute.org` from `assertion.tenant`. Comparing the subject to the prefix with `==`, as in `assertion.sub == "wimse://identity.anthropic.com/org/<your organization ID>/agent/"`, never matches, because every subject continues past the prefix with an agent's ID. Use `startsWith` on the prefix, or `==` on a full subject. |
| Issuer, attribute mapping, and audience | The provider's issuer is `https://identity.anthropic.com/agents`, its attribute mapping sets `google.subject` to `assertion.sub` (and `attribute.org` to `assertion.tenant` if your condition or grants use it), and the **Workload identity provider** you entered in the console is the provider's full resource name, which is the token's audience.                                                                                                                                                                                                                                                                                                                                                               |
| Service account grant                   | If you named a service account, the federated identity holds a role on it that allows `iam.serviceAccounts.getAccessToken`, such as `roles/iam.workloadIdentityUser`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Your authorization server rejects the grant

**What you see**

Claude reports `injection failed` with HTTP 502, and your authorization server's log shows a `POST` to the token endpoint answered with a 4xx, typically `{"error":"invalid_grant"}`.

**What it means**

Your server didn't accept Claude's identity token as a JWT bearer assertion.

**How to resolve**

| Check           | What to confirm                                                                                                                                                                                                                                                                                                                         |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Grant shape     | The token endpoint accepts `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` with the token in `assertion`, plus `resource` and `scope` if you set them, as a form-encoded `POST` with `Accept: application/json`. No `client_id` or client secret is sent, so the endpoint must accept the grant without client authentication. |
| Audience        | The token's `aud` is your authorization server's issuer identifier exactly as you entered it when connecting the server, or the token endpoint URL exactly as registered if you left the issuer identifier empty, as a one-element array. The **Audience** row of the **Connect an authorization server** dialog shows the value.       |
| Issuer and keys | As for a gateway: issuer `https://identity.anthropic.com/agents`, keys from its discovery document, ES256 only.                                                                                                                                                                                                                         |
| Subject         | Your server must accept only your own agents' full subjects, or at minimum require the **Subject prefix** shown in the **Connect an authorization server** dialog (or pin `iss` and `tenant`, which is the same check). The console's connection check doesn't run for token endpoints, so nothing tests this check for you.            |
| Response        | A JSON body with `access_token`, `expires_in`, and, if `token_type` is present, the value `Bearer`. An `expires_in` under 5 minutes or over 1 day, or a missing one, makes Claude exchange a fresh token on every request, which shows in your log as one grant per request.                                                            |

Claude doesn't read `error_description`, so put the detail in your server's log rather than in the response.

## Contact Anthropic

If no entry resolves the problem, contact your Anthropic account team and include:

* Your organization name and the channel where it happened
* The time of the failing request, with the time zone
* The error text Claude reported, including the HTTP status and the connection's name where the error shows one
* For a gateway, the line from your gateway's log; for AWS, the CloudTrail event; for Google Cloud, the audit log entry; for an authorization server, the request and response your server logged

Never send a token itself. Anthropic's logs record why a token was refused or not issued, and the time and connection name are enough to find the entry.

## Related resources

* [Federated cloud access overview](/docs/claude-tag/admins/federated-access/overview): how the token works and which connection type to use
* [Connect a gateway](/docs/claude-tag/admins/federated-access/connect-a-gateway): the setup steps and the connection check in full
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim, the lifetime, and key rotation
* [Limits](/docs/claude-tag/admins/federated-access/limits): counts, lengths, and lifetimes
* [Troubleshoot Claude Tag setup](/docs/claude-tag/admins/troubleshooting): errors outside federated cloud access
