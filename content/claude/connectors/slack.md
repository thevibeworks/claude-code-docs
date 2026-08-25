> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack integration

> Use Claude directly in Slack and connect your workspace

Integrate Claude and Slack in two ways: add Claude directly to your Slack workspace, or enable the Slack connector for your Claude apps.

<Note>
  This page covers the earlier per-user Claude in Slack app. The current product is [Claude Tag](/docs/claude-tag/overview), which gives your team one Claude identity set up by an admin. If your organization used the earlier app, see [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier).
</Note>

## Claude in Slack (earlier app)

Claude is available to paid Slack plan users. Slack admins must approve the app before individual users can access it.

### Ways to interact with Claude

1. **Direct messaging**: Start private conversations with @Claude
2. **AI assistant panel**: Click Claude's icon in Slack's AI assistant header
3. **Thread participation**: Mention @Claude in any thread for assistance

All surfaces support the same Claude capabilities you've enabled, including web search and tool integrations.

<Note>
  Team and Enterprise plan users with Claude Code access can route coding tasks directly to Claude Code by mentioning @Claude.
</Note>

## Installation

### For Slack admins

1. Navigate to the Claude app in Slack's App Marketplace
2. Click "Add to Slack"
3. Review and approve for your organization
4. Deploy org-wide or to specific workspaces

**For multi-workspace deployment:**

* Access your Slack management workspace
* Navigate to **Integrations → Installed apps → Add to more workspaces**
* Toggle through relevant workspaces

### For individual users

1. Find Claude in your apps list or the Slack App Marketplace
2. Click "Connect Account"
3. Select your organization
4. Click "Authorize" to grant access
5. Return to Slack and click "+ New Chat" or @mention Claude

**Tip**: Add Claude to your Slack header by clicking the three dots and selecting "Add this app to header."

## Slack connector

Available for Team and Enterprise plans, the Slack connector allows Claude to search your workspace's channels, direct messages, and files for relevant context.

<Warning>
  You must install Claude in Slack before enabling and using the Slack connector.
</Warning>

### Enabling the connector

**For Owners**: Navigate to **Organization settings > Connectors** and enable the Slack connector.

**For Individual Users**: Go to **Customize > Connectors**, find Slack, and click "Connect."

## Managing connections

### Viewing connection status

1. Click Claude in your Slack sidebar
2. Go to the "Home" tab
3. View your connection details

### Disconnecting

**Claude app**: Go to Claude's Home tab and click the red "Disconnect" button.

**Slack connector**: Go to [claude.ai/customize/connectors](https://claude.ai/customize/connectors), find Slack, and select "Disconnect."

<Note>
  Disconnecting removes your account connection and deletes past conversations within 30 days.
</Note>

## Privacy & data

* Slack conversations remain separate from your Claude web history
* Conversations initiated in Slack don't appear in your Claude chat history
* Each platform maintains separate conversation histories
* Conversations auto-delete within 30 days if you disconnect
* Slack retention policies apply to your workspace messages

## Troubleshooting

<Accordion title="Can't install Claude in Slack">
  If your company Slack requires admin approval and you lack admin access, you'll see a "Request to install" prompt. Contact your Slack Admin to approve the app.
</Accordion>
