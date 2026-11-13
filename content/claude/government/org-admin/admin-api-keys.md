> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin API keys

> Admin API keys let organization owners give a script read-only access to their organization's audit events, usage reports, or both.

> **Who this is for:** Owners and Primary Owners who create keys for the security, finance, or reporting tools that read their organization's data.

An admin API key lets a script read your organization's Claude for Government audit events, usage reports, or both, without anyone signing in. Keys are read-only, and each one reads only the organization it was created in.

> [!NOTE]
>
> For a key that reads the audit events of every organization in your tenant, see [Managing API keys](https://claude.com/docs/government/org-admin/compliance-api.md#managing-api-keys) for the Compliance API.

## What a key can read

You choose what a key can read when you create it, and you can't change the choice afterward.

Owners, Primary Owners, and tenant administrators can select each choice when its setting is on.

| **This key can read** | Setting that must be on |
| - | - |
| **Compliance activity feed**, for the [Compliance API](https://claude.com/docs/government/org-admin/compliance-api.md) | [**Compliance API**](https://claude.com/docs/government/config/settings.md#compliance-api) |
| **Usage and cost reports**, for the [Analytics API](https://claude.com/docs/government/org-admin/analytics-api.md) | [**Analytics API**](https://claude.com/docs/government/config/settings.md#analytics-api) |

A key with **Usage and cost reports** can read each member's usage and estimated cost, by the hour, with the member's name and email address. Neither API returns conversation content, files, or anything your users type into Claude.

A key that reads only one of the APIs gets a 403 error from the other.

## Create a key

Each organization can hold up to 50 active keys, whatever they read. Revoked keys don't count toward the limit.

1. In the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it), go to **Settings > Admin API keys**.
2. Under **This key can read**, make sure that **Compliance activity feed**, **Usage and cost reports**, or both are selected.
3. Enter a name and click **Create key**.
4. Copy the key and store it somewhere safe, then click **Done**.

> [!WARNING]
>
> The full key is shown **only once**. If you lose it, create a new key and revoke the old one.

## Rotate or revoke a key

Keys never expire, and they aren't tied to the person who created them. To stop a key when someone who has it changes role or leaves, revoke it.

* **Rotate a key without interrupting the tool that uses it**: [create a new key](#create-a-key) with the same choices under **This key can read**, switch the tool to it, confirm that data still arrives, and then revoke the old key.
* **Revoke a key**: go to **Settings > Admin API keys** in the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it), find the key by the last characters in its **Key** column, click **Revoke** in its row, and click **Revoke** in the dialog. Owners, Primary Owners, and tenant administrators can revoke any of the organization's keys. Revoking takes effect immediately and can't be undone, and the next request made with the key returns a 401 error.
* **Rotate or revoke a key created in the tenant admin portal**: a tenant administrator goes to **Settings > Compliance API keys** in the [tenant admin portal](https://claude.com/docs/government/tenant-admin/overview.md) and follows the same steps there. A new key there needs only a name.

Anthropic can also revoke a key created in either portal, such as one that has leaked.

Turning off the [**Compliance API**](https://claude.com/docs/government/config/settings.md#compliance-api) or [**Analytics API**](https://claude.com/docs/government/config/settings.md#analytics-api) setting doesn't revoke keys. A key that you don't revoke works again once the setting is back on.
