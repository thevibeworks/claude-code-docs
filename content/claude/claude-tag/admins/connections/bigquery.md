> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect BigQuery

> Connect BigQuery to Claude Tag so it can run read-only queries on your datasets, using a GCP service-account key.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Connecting BigQuery lets Claude run queries against your datasets in any channel where the connector is on. Claude connects with its own credential, not a person's.

This connector calls BigQuery's HTTP API, and it's separate from members' personal claude.ai connectors. Pair it with a plugin that covers BigQuery so Claude knows how to form and run queries; without one, Claude can reach the API but has to work out the request shape on its own. Add the plugin on the [**Skills and plugins**](https://claude.ai/admin-settings/claude-tag?access=plugins) tab.

## Create the credential in Google Cloud

Create a dedicated service account for the agent in the Google Cloud project that holds your BigQuery data, then create a JSON key for it. Google's guides cover [creating a service account](https://cloud.google.com/iam/docs/service-accounts-create) and [creating a service account key](https://cloud.google.com/iam/docs/keys-create-delete).

## Grant access to specific datasets

You scope what Claude can read on the Google Cloud side, through the service account's role grants. The connector itself has no dataset setting. Grant the service account two roles:

* **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) on each dataset Claude should query. Grant it on the specific datasets, not on the project, so Claude can read only those datasets.
* **BigQuery Job User** (`roles/bigquery.jobUser`) on the project, so the service account can run query jobs.

Together the two grants let Claude run read-only queries against those datasets. To widen or narrow access later, edit the dataset grants in Google Cloud; the connector needs no change.

## Add the connector

Go to [**Organization settings > Claude Tag > Connectors**](https://claude.ai/admin-settings/claude-tag?access=connectors), click **Add**, and select **BigQuery**. The first credential you add for a service from the **Connectors** tab is on in every workspace and channel as soon as you save it. To give it narrower reach, see [where a new connector applies](/docs/claude-tag/admins/add-connections#add-a-connection) before you save the connector. In the connect form, paste the whole JSON key file from Google Cloud Console into **Claude's service account key (JSON)**, then click **Connect** to save the connector.

The access tokens Claude gets from this key carry only Google's `cloud-platform.read-only` scope, so Google refuses BigQuery API calls that create or delete tables or run load jobs. Queries still run with whatever the service account's roles allow, so the [dataset roles](#grant-access-to-specific-datasets) decide what a query can reach.

Agent Proxy exchanges the service-account key for an access token and injects it at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

## Verify the connection

In a channel where the connector is on, in a new thread:

```text wrap theme={null}
@Claude what can you access from this channel?
```

BigQuery appears in the list once the connector is live. New threads pick up the connector on their own; in an existing thread, ask Claude to use the service by name.

Then confirm a query runs against a dataset you granted:

```text wrap theme={null}
@Claude how many rows are in <dataset>.<table>?
```

## Allow the connection through a VPC Service Controls perimeter

If the Google Cloud project that holds your BigQuery data is inside a [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview) perimeter, Claude's queries fail with `Request is prohibited by organization's policy` and a `vpcServiceControlsUniqueIdentifier` in the error details. To let them through, add an ingress rule that admits the [service account you created for Claude](#create-the-credential-in-google-cloud).

If you allowlist [Anthropic's published egress IP range](/docs/claude-tag/admins/network-requirements) in an access level, Claude's queries still fail, because they reach your perimeter from inside Google Cloud rather than from that range. The source your perimeter sees is a Google Cloud project that Anthropic owns and can change without notice, so don't admit that project by its number.

Add an [ingress rule](https://cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to the perimeter with these settings:

* For the identity, admit the service account you created for Claude.
* For the source, allow any source (an access level of `*`).
* For the target, allow the BigQuery API (`bigquery.googleapis.com`) on the project inside the perimeter.

To confirm the rule works, ask Claude to run the query that failed. The query returns results.

### What the VPC Service Controls ingress rule allows

The ingress rule lets requests authenticated as the service account you created for Claude cross the perimeter, and only to reach BigQuery in the project the rule names. It doesn't give the service account access to any data. The [dataset roles you granted](#grant-access-to-specific-datasets) still decide which datasets Claude can read, so keep those grants narrow.

Once the connection works, delete the key file that Google Cloud downloaded to your machine when you created the key. With this rule in place, the perimeter doesn't stop a leaked key for this service account, because a request authenticated with any of the account's valid keys passes the rule from any source. [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy) holds the key you uploaded and Claude never sees it. To limit that risk further, don't create more keys for the service account.

## Related resources

* [What this connection adds](/docs/claude-tag/users/use-cases/answer-data-questions): warehouse questions answered with charts in the thread
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference
