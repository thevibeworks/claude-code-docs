> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud storage

> Connect Amazon S3, Google Cloud Storage, or Azure Blob Storage so Claude can read data and write results in place, with your permission.

Connect Amazon S3, Google Cloud Storage, or Azure Blob Storage so Claude can read data and write results in place, with your permission.

In **Settings > Credentials**, choose **AWS**, **Google Cloud**, or **Microsoft Azure**, then Connect. Provide the credential (access key, service-account JSON, HMAC key, service principal, or connection string) and list the bucket names (AWS, GCP) or **Blob containers** (Azure) this credential covers. S3-compatible stores use the AWS form with the **S3-compatible endpoint** field; you'll need to allowlist that endpoint host separately.

Listing a bucket adds its address to the sandbox network allowlist so code can reach it without a network permission card. Access within the bucket is still limited to the credential's permissions. Credentials are stored encrypted on your computer. When you approve one, code that Claude writes receives its value, so that the code can reach the provider.

Claude reads and writes objects with ordinary code using the provider's Python library (`boto3`, Azure SDK). **Settings > Storage** lists connected credentials and lets you browse and import objects (up to 100 GB) or export artifacts.

> [!NOTE]
>
> From code, reach Google Cloud Storage with an **HMAC key** via `boto3`, or use the import/export flow. `gsutil`, `gcloud storage`, and the google-cloud-storage Python library use path-style addresses that aren't reachable from the sandbox.

> [!WARNING]
>
> Code that Claude writes can use a credential you add here only after you approve a **Credentials** card that names it. By default, approval lasts for the conversation, but Claude Science can still ask about code that uses the credential. See [What auto mode checks](https://claude.com/docs/claude-science/auto-mode.md#what-auto-mode-checks). If a bucket should never be reachable from an analysis session, don't add its credential.
