> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage your listing after publishing

> Update your MCP server, plugin, and directory listing after publication

## Update your MCP server

An MCP server is a live API. To add, change, or remove tools, deploy the change to your server—no resubmission to Anthropic is required, and there is no scheduled re-review. Claude picks up the new tool surface on the next connection.

## Update your plugin

Plugin updates are pushed via your GitHub repo. CI mirrors changes to the public marketplace and runs automated screening on each update.

## Update your listing

Edit your description, categories, icon, and other listing metadata from the submissions dashboard at [Organization settings > Directory](https://claude.ai/admin-settings/directory/submissions) in Claude.ai. See [Managing your listing](/docs/connectors/building/managing-your-listing) for what you can edit directly and which changes require review.

## Slugs are permanent

Your directory slug is fixed after publication. It determines your connector's permanent listing URL:

```text theme={null}
https://claude.ai/directory/connectors/SLUG
```

Share this URL from your own documentation or a "Connect to Claude" button to send users directly to your listing. Display names can change via the dashboard; the URL slug cannot.

## Delist your connector

To voluntarily remove your connector from the directory, email `mcp-review@anthropic.com`.
