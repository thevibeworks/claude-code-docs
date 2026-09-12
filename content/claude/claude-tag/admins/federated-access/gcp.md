> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect a Google Cloud identity

> Let Claude call Google Cloud through workload identity federation with a short-lived identity token instead of a service account key. Covers the pool, provider, and IAM grants to create, with or without a service account, and how to connect the identity in the console.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Google Cloud identities are connected at [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag): open **Federated cloud access** in the left navigation and use the **Cloud roles** section. Connecting an identity needs an organization Owner, or an admin with full Claude Tag management permission.</Note>

With a Google Cloud identity connection, Claude exchanges a short-lived identity token at a workload identity pool you create and calls Google Cloud APIs with the result. No service account key is stored in Claude. The token names your organization and the [agent](/docs/claude-tag/concepts/agent-identity) making the request (Claude's identity in one Slack channel), and your pool's attribute condition decides which tokens to accept. If someone else manages your Google Cloud project, give them the values from Claude's admin settings and the settings below; the console steps need a Claude Tag admin.

Before you start, decide whether Claude acts as the federated identity itself, with roles granted to it directly, or as a service account you create. Both forms are covered below.

## Before you begin

* You're an organization Owner, or an admin with full Claude Tag management permission.
* You can create a workload identity pool and provider in a Google Cloud project (any project; it doesn't have to own the resources) and grant IAM roles on the resources Claude will use. Use a workload identity pool; workforce identity pools aren't supported.
* If an organization policy restricts which issuers your workload identity pools may trust, allow `https://identity.anthropic.com/agents` first.
* You know which Google API hosts Claude will call, for example `storage.googleapis.com`.

## Copy the values from the console

In **Cloud roles**, click **Connect a Google Cloud identity** and copy the **Issuer** and **Subject prefix** rows from the **Set the workload identity provider to accept these values** card (the **JWKS URL** row isn't needed, because Google reads the keys from the issuer). Then click **Cancel**; you connect the identity after setting up Google Cloud.

| Value          | What it is                                                                                                                                                                                                                                         |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issuer         | `https://identity.anthropic.com/agents`. The issuer URL of the provider you create in the pool.                                                                                                                                                    |
| Subject prefix | `wimse://identity.anthropic.com/org/<your organization ID>/agent/`. Every token's subject starts with this prefix and ends with one agent's ID. The organization ID between `/org/` and `/agent/` is also the value of the token's `tenant` claim. |

## Create the pool and provider in Google Cloud

Create a workload identity pool and an OpenID Connect (OIDC) provider in it with these settings. Replace `<your organization ID>` with the ID from your **Subject prefix**.

| Setting             | Value                                                                                                                                                                                                                                                                                |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Issuer URL          | `https://identity.anthropic.com/agents`                                                                                                                                                                                                                                              |
| Allowed audiences   | Leave at Google's default, the provider's own resource name, which Google accepts with or without a leading `https:`. Claude sends the name exactly as you enter it in Claude's admin settings, so if you pin allowed audiences instead, pin that same spelling.                     |
| Attribute mapping   | `google.subject` = `assertion.sub`. You can also map `attribute.org` = `assertion.tenant`, which lets you grant roles to all of your organization's agents as one principal set in [Grant access](#grant-access).                                                                    |
| Attribute condition | `assertion.sub == "<full subject>"` for one agent. To allow several agents, join one comparison per agent with CEL's or operator. To admit every agent in your organization instead, `assertion.sub.startsWith("wimse://identity.anthropic.com/org/<your organization ID>/agent/")`. |

Google doesn't require an attribute condition, and nothing checks it for you. Without one, agents of every other Claude Tag organization can authenticate to your pool, because every organization's tokens come from the same issuer; see [Authorize on the subject](/docs/claude-tag/admins/federated-access/token-reference#authorize-on-the-subject). The condition on `assertion.sub` is the subject check every connection type needs. The exact form accepts only the agents you list, and the prefix form accepts every agent in your organization, because every subject carries your organization ID between `/org/` and `/agent/`.

Listing exact subjects is the strongest form. The prefix form is the minimum, and it admits every agent in your organization to the pool. With the prefix form, you can still grant IAM roles only to individual agents' `principal://` members, as shown under [Grant access](#grant-access). Claude's admin settings don't show agent IDs, so you learn a subject from Cloud Audit Logs after a first exchange, and you update the condition or the grants when a Slack channel is deleted and recreated, because the new channel's agent has a new ID.

Mapping `attribute.org` from `assertion.tenant` is optional. The `tenant` claim carries the same organization ID as the subject, so the condition `attribute.org == "<your organization ID>"` is the prefix check in claim form. The mapping is standard Google attribute mapping.

## Grant access

Choose one of the two forms. The console step "Name the service account, or leave the field empty" depends on your choice.

### Without a service account

Grant IAM roles on each resource directly to the federated identity. To grant a role to one channel's agent, use the agent's full subject, unescaped, for example `principal://iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/claude/subject/wimse://identity.anthropic.com/org/<your organization ID>/agent/<agent ID>`.

To grant a role to all of your organization's agents at once, map `attribute.org` from `assertion.tenant` as described under [Create the pool and provider in Google Cloud](#create-the-pool-and-provider-in-google-cloud), and use the principal set

```text wrap theme={null}
principalSet://iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/claude/attribute.org/<your organization ID>
```

with your project number, pool ID, and organization ID.

Grant only what Claude needs, and grant nothing to the pool-wide principal set (`principalSet://…/workloadIdentityPools/claude/*`). In this form, don't grant the federated identity any permission that mints credentials, such as `iam.serviceAccounts.getAccessToken`, `iam.serviceAccounts.signJwt`, or service account key creation, because Claude could then obtain a Google credential that works outside Claude. (The form with a service account grants one such permission on purpose, on one service account.)

### With a service account

Create a dedicated service account in any project and grant it the roles Claude needs. The console accepts only addresses of the form `<name>@<project>.iam.gserviceaccount.com`, so the default Compute Engine and App Engine service accounts can't be used. Enable the IAM Service Account Credentials API in the service account's project. Then grant the **Workload Identity User** role (`roles/iam.workloadIdentityUser`) to the same `principalSet://` or `principal://` member as in [Without a service account](#without-a-service-account), on the service account's own IAM policy rather than on the project. Don't grant the service account any permission to mint further credentials or create keys.

## Connect the identity in the console

<Steps>
  <Step title="Open the Connect a Google Cloud identity dialog">
    In **Cloud roles**, click **Connect a Google Cloud identity**.
  </Step>

  <Step title="Enter the provider resource name">
    In the **Workload identity provider** field, enter `//iam.googleapis.com/` followed by the provider's full name as Google reports it, for example `//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/claude/providers/agents`. Use the project number, not the project ID (find it on the project's dashboard in the Google Cloud console). The value is stored as you type it and is the token's audience.
  </Step>

  <Step title="Name the service account, or leave the field empty">
    In the **Service account to act as (optional)** field, enter the service account's email, for example `claude@my-project.iam.gserviceaccount.com`, if you chose the form with a service account. Leave the field empty to have Claude act as the federated identity itself. The connection is named after the service account, or after the provider's ID (the last part of its resource name) when there is none.
  </Step>

  <Step title="Decide whether to block credential minting">
    The **Block requests that mint new credentials** checkbox is selected by default. With it selected:

    * Claude can't use this identity to call Google endpoints that create keys, tokens, or other credentials, even if IAM would allow the call.
    * Requests to a list of services that deal in credentials are refused entirely. See [what the credential-minting block refuses](/docs/claude-tag/admins/federated-access/limits#what-the-credential-minting-block-refuses) on the limits page.
    * gRPC calls are refused, so tell Claude in the custom instructions to use the REST transport of client libraries such as Spanner, Bigtable, Firestore, and Pub/Sub.

    If Claude needs one of the refused services, clear the checkbox and rely on your IAM grants alone. The token exchange itself, including acting as the service account, happens inside Agent Proxy and isn't affected by this checkbox or by the allowed hosts.
  </Step>

  <Step title="Narrow the allowed Google hosts">
    Replace the prefilled `*.googleapis.com` entry in the **Allowed Google hosts** field with the hosts Claude needs, for example `storage.googleapis.com`. A wildcard as the leftmost label, such as `*.storage.googleapis.com`, matches any subdomain but not the name itself. Every host must be `googleapis.com`, a subdomain of it, or a subdomain of `clients6.google.com`. You can change the list later from the connection's [**Edit connection** dialog](/docs/claude-tag/admins/add-connections#set-allowed-websites) on the bundle's **Credentials** tab.
  </Step>

  <Step title="Confirm the attribute condition">
    Select the checkbox labeled **The provider's attribute condition requires the subject prefix shown above**. The **Connect identity** button stays disabled until you do. Select the checkbox only if the provider's attribute condition pins `assertion.sub` to one or more full subjects under your **Subject prefix**, or at minimum pins `assertion.sub` to your **Subject prefix** (or, if you mapped it, `attribute.org` to your organization ID), as described under [Create the pool and provider in Google Cloud](#create-the-pool-and-provider-in-google-cloud).
  </Step>

  <Step title="Choose an Access bundle and connect">
    Choose a bundle from the **Access bundle** list, or click **New bundle**, enter a **Bundle name**, and click **Create bundle**. Then click **Connect identity**. This creates a [connection](/docs/claude-tag/admins/add-connections) in that bundle, labeled **Google Cloud identity** on its **Credentials** tab, with the hosts you entered under **Allowed hosts**. The same provider can be connected more than once, for example once with a service account and once without, as long as no two Google Cloud connections in one bundle share a host under **Allowed hosts**. To use a connection in several scopes (workspaces or channels), attach its bundle to each.
  </Step>
</Steps>

The **Cloud roles** table has **Role**, **Access bundle**, **Allowed hosts**, **Added**, and **Actions** columns. Each connection's name appears under **Role** with the provider and a **Google Cloud** chip beneath it, which also names the service account when the connection acts as one, and **Remove** is under **Actions**.

## Let agents use the identity

Claude uses the identity in channels whose scope has the bundle attached. [Attach the bundle to a workspace or channel](/docs/claude-tag/admins/attach-to-scope#attach-the-bundle) if it isn't attached already.

Claude also needs to know what the identity is for. Add a line like this to the scope's [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions):

```text wrap theme={null}
Use the Cloud Storage JSON API at storage.googleapis.com to read the bucket example-reports. Google Cloud access is already set up.
```

[Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) exchanges the token and attaches the resulting Google credential to each request at the network boundary, so the sandbox never holds it.

New threads pick up the connection on their own. In a thread already running, ask Claude to use Google Cloud. If Claude still can't, send [`@Claude !restart`](/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session) at the channel's top level (not inside a thread) to start a fresh session with your organization's current configuration.

## Verify the connection

In a channel whose workspace or channel has the bundle attached, start a new thread and ask Claude to run a connectivity check. The check reads a bucket's metadata, so the identity needs the `storage.buckets.get` permission on the bucket, and `storage.googleapis.com` must be under the connection's **Allowed hosts**. Send Claude this prompt, replacing `example-reports` with a bucket the identity can read:

```text wrap theme={null}
@Claude Connectivity check for this channel's Google Cloud connection. Please run exactly:

curl -sS -o /tmp/resp.txt -w '%{http_code}' https://storage.googleapis.com/storage/v1/b/example-reports

and tell me the HTTP status code it prints, then paste the contents of /tmp/resp.txt.
```

A status of 200 with a JSON body whose `kind` is `storage#bucket` means the token exchange and the API call both worked. For log evidence, enable Data Access audit logs beforehand for the Security Token Service API, for Cloud Storage, and, with a service account, for the IAM Service Account Credentials API, because Google keeps them off by default. The Security Token Service entry records each token exchange, with Google's reason when it refuses one, which Claude's own error doesn't show. The Cloud Storage entry shows the caller as the service account, or as the federated identity with the agent's full subject.

If Claude reports that the request was refused, the two most common causes are these:

* A token refused by your provider usually means the attribute condition didn't accept it. Check the organization ID in the condition, then the issuer URL and the allowed audience.
* A permission error on the API call means the role grant is missing or too narrow.

See [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting) for the errors Claude shows and the other causes.

To disconnect an identity, click **Remove** in the identity's row of the **Cloud roles** table, then **Remove role** in the confirmation. Claude stops using the identity within about a minute, in existing threads as well as new ones, and the connection is removed from its bundle. A Google credential from an earlier exchange stays valid with Google until it expires, held only by Agent Proxy, never by Claude's sandbox. To end the trust on the Google side as well, delete the provider or remove the IAM bindings.

## Common errors

Two messages come up while connecting:

* **A message that a connection "already covers" a host "in this bundle"**: another Google Cloud connection in the bundle you chose already has that host under **Allowed hosts**, so Claude would never use the new connection for it. Remove the shared host or choose another bundle.
* **A rejected Workload identity provider or Service account to act as value**: the value doesn't match the form the field describes, usually because the resource name carries the project ID instead of the project number, or the service account is a default one.

For other dialog messages, see [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting).

## Related resources

* [Give Claude access](/docs/claude-tag/admins/add-connections): the Access bundle and connection model
* [Attach a bundle to a scope](/docs/claude-tag/admins/attach-to-scope): where an identity connection applies
* [Identity token reference](/docs/claude-tag/admins/federated-access/token-reference): every claim in the token, lifetimes, and key rotation
* [Limits](/docs/claude-tag/admins/federated-access/limits): what the credential-minting block refuses, and the other limits for Google Cloud identities
* [Troubleshoot federated cloud access](/docs/claude-tag/admins/federated-access/troubleshooting): console and runtime errors for every connection type
* [BigQuery](/docs/claude-tag/admins/connections/bigquery): the stored-key alternative for one Google service
