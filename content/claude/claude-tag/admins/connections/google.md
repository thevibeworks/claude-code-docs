> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Google Drive, Calendar, and Gmail

> Connect Google Drive, Calendar, and Gmail to Claude Tag so it can read docs, sheets, events, and email. Covers OAuth setup, the service-account option, and what each grants.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting Google Drive, Calendar, and Gmail lets Claude read documents, spreadsheets, calendar events, and email in any channel where the connector is on. Claude connects with its own credential, not a person's.

This connector calls Google's HTTP APIs, and it's separate from members' personal claude.ai connectors. A member's own Google connector applies in one-to-one DMs. Claude can also [use it in a channel](/docs/claude-tag/concepts/personal-connectors) for that member's own tasks, after the member allows it.

## Choose OAuth or a service account

The **Add a connector** dialog offers two routes to Google:

| Route | When to use |
| :- | :- |
| **Google sign-in** (the **Google Drive**, **Google Calendar**, or **Gmail** entry) | Fastest path. An admin signs in with a Google account that has access to the content Claude needs. |
| **GCP service-account key** (the **Custom connector** entry) | When you want a dedicated non-human identity in Google with auditable access, or need domain-wide delegation across your Workspace. |

Both routes create a credential and an allowed-websites rule for the Google hosts the connector uses.

## Add the connector with Google sign-in

<Warning>Use a dedicated Google account for this connector (for example, `claude@yourcompany.example.com`), not your own. The connector is shared: anyone in a channel where it's on can ask Claude to read whatever this account can see in Drive, Calendar, and Gmail. A dedicated account starts with no access until you share the specific folders and calendars Claude needs, and keeps its activity under a separate identity in Google's audit log.</Warning>

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Google Drive**, **Google Calendar**, or **Gmail**. The connect form lists the Google hosts the connector can reach; there are no scopes to choose. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you sign in. Click **Sign in with Google Drive** (or **Sign in with Google Calendar**, or **Sign in with Gmail**), approve the Google consent screen, and the credential is saved.

The connector's reach is whatever the signed-in Google account can see. Share the relevant folders and calendars with that account in Google before testing.

## Add the connector with a service account

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **Custom connector**. Fill in these fields in the connect form.

| Field | Value |
| :- | :- |
| Name | A name for the connector, such as `Google Workspace` |
| Credential type | **GCP access token (with Service Account Key)** |
| GCP service account key (JSON) | The JSON key file from Google Cloud Console |
| Scopes (optional) | The Google API scopes to request (for example `https://www.googleapis.com/auth/drive.readonly`). If you leave the field empty, the connector requests `https://www.googleapis.com/auth/cloud-platform`. |
| Subject (optional) | A user email to impersonate via domain-wide delegation. Set this for Workspace data (Drive, Calendar, Gmail, Docs). |
| Allowed websites | `*.googleapis.com` |

The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. Click **Connect** to save the connector.

For Google Workspace data (Drive, Calendar, Gmail, Docs), the service account needs domain-wide delegation configured in your Google Admin console. In the service account's domain-wide delegation entry, list every scope you entered in **Scopes**, or `https://www.googleapis.com/auth/cloud-platform` if you left **Scopes** empty. Google's guide is at [developers.google.com/identity/protocols/oauth2/service-account](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority).

Google refuses the token request when the domain-wide delegation entry is missing one of the requested scopes. Claude then reports HTTP 502 with a reason that starts with `injection failed ("<connection name>")`.

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

Google Drive, Calendar, or Gmail appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

To confirm the connector works, ask Claude in the same thread to read something from the service, such as today's calendar events or a named document.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/find-answers): grounding answers in your team's documents
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
