> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect BigQuery

> Connect BigQuery to Claude Tag so it can run read-only queries on your datasets. BigQuery has no preset, so it is added as a custom credential with a GCP service-account key.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<Note>Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.</Note>

Connecting BigQuery lets Claude run queries against your datasets from any channel under the bundle's scope. Add it as a custom credential with **Custom tool**; BigQuery has no preset button in the picker.

This is an HTTP API connection, not a personal claude.ai connector. Pair it with a plugin that covers BigQuery so Claude knows how to form and run queries; without one, Claude can reach the API but has to work out the request shape on its own. See [Attach plugins](/docs/claude-tag/admins/add-connections#attach-plugins).

## Create the credential in Google Cloud

Create a dedicated service account for the agent in the Google Cloud project that holds your BigQuery data, then create a JSON key for it. Google's guides cover [creating a service account](https://cloud.google.com/iam/docs/service-accounts-create) and [creating a service account key](https://cloud.google.com/iam/docs/keys-create-delete).

## Grant access to specific datasets

You scope what Claude can read on the Google Cloud side, through the service account's role grants. The connection itself has no dataset setting. Grant the service account two roles:

* **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) on each dataset Claude should query. Grant it on the specific datasets, not on the project, so Claude can read only those datasets.
* **BigQuery Job User** (`roles/bigquery.jobUser`) on the project, so the service account can run query jobs.

Together the two grants let Claude run read-only queries against those datasets. To widen or narrow access later, edit the dataset grants in Google Cloud; the connection needs no change.

## Add the connection to a bundle

In the bundle, click **Connect** next to **Custom tool** and choose **GCP access token (with Service Account Key)**.

| Field                          | Value                                                                                                                                                                                                                                                                              |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credential type                | **GCP access token (with Service Account Key)**                                                                                                                                                                                                                                    |
| GCP service account key (JSON) | The JSON key file from Google Cloud Console                                                                                                                                                                                                                                        |
| Scopes (optional)              | `https://www.googleapis.com/auth/bigquery`. The field is labeled optional, but leave it empty and the token defaults to a broader scope. BigQuery's query endpoints don't accept a read-only scope; the dataset roles in the section above are what keep the connection read-only. |
| Allowed websites               | `bigquery.googleapis.com`                                                                                                                                                                                                                                                          |

Agent Proxy exchanges the service-account key for an access token and injects it at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel under the bundle's scope, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

BigQuery appears in the list once the connection is live. New threads pick up the connection on their own; in an existing thread, ask Claude to use the service by name.

Then confirm a query runs against a dataset you granted:

```text wrap theme={null}
@Claude how many rows are in <dataset>.<table>?
```

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/answer-data-questions): warehouse questions answered with charts in the thread
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
