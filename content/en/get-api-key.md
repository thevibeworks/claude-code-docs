---
title: Get your Claude API key
url: https://platform.claude.com/docs/en/get-api-key
description: Find, create, and manage your API keys for the Claude API in the Claude Console.
---

API keys for the Claude API (also called Anthropic API keys) live in the Claude Console. To view your existing keys or create a new one, go to [Settings → API keys](https://platform.claude.com/settings/keys).

## Choose a key type

When you create a key, you choose its type, which determines what the key can do, where it works, and when it stops working. A **personal key** acts as you, and stops working if you leave an organization. A **service account key** represents a [service account](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#service-accounts) which can be used by workloads such as CI pipelines, production services, or agents. Use a personal key for your own development, and a service account key for anything shared.

You can also create a **workspace key**, a legacy key without an owner: it belongs to the workspace you create it in and keeps working after its creator leaves. It is preferable to use a personal or service account key, as these stop working automatically when their associated account is removed from the organization.

## Create an API key

<Steps>
  <Step title="Sign in to the Claude Console">
    Go to [platform.claude.com](https://platform.claude.com/) and sign in, or create an account if you don't have one yet.
  </Step>

  <Step title="Open the API keys page">
    Go to [Settings → API keys](https://platform.claude.com/settings/keys).
  </Step>

  <Step title="Create a key">
    Click **Create key**, name the key, choose an [expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration), and set **Linked account** to yourself or a service account. You can also choose a [workspace](https://platform.claude.com/settings/workspaces) to scope the key to.
  </Step>

  <Step title="Copy and store the key">
    The Console shows the full key, which starts with `sk-ant-`, only once, at creation. Copy it and store it somewhere safe, such as a secrets manager. If you lose a key, you can't view it again in the Console. Create a new key instead.
  </Step>
</Steps>

If the **Create key** button on the API keys page is disabled, your role may not allow you to create keys there. Ask an organization admin to change your role, or to create a service account key for your workload.

## Use your API key

Set the key as an environment variable:

```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

The [client SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) read `ANTHROPIC_API_KEY` automatically. Direct HTTP requests send the key in the `x-api-key` header. If your API key works on multiple workspaces, you must also send the `anthropic-workspace-id` header on each Claude API request, as shown in [Select a workspace](https://platform.claude.com/docs/en/manage-claude/authentication#select-a-workspace). For the Admin API, see [API keys and the Admin API](https://platform.claude.com/docs/en/get-api-key#api-keys-and-the-admin-api).

To make your first request, follow the [Quickstart](https://platform.claude.com/docs/en/get-started), and see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication) for the full picture, including short-lived credentials with Workload Identity Federation.

## API keys and the Admin API

The [Admin API](https://platform.claude.com/docs/en/api/admin) includes endpoints for managing your organization's API keys programmatically, such as [Retrieve API Key](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve) and [List API Keys](https://platform.claude.com/docs/en/api/admin/api_keys/list). These endpoints are for organization admins automating key management. They accept an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys), an OAuth token with the `org:admin` scope, or a personal or service account key that isn't scoped to a specific workspace; workspace keys don't work there. They never return a key's secret value, only a partially redacted hint.

<Note>
  The Admin API can't recover a lost key or give you a key to call the Claude API with. To get a usable API key, create one in [Settings → API keys](https://platform.claude.com/settings/keys) in the Claude Console.
</Note>
