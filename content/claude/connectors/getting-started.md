> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with connectors

> Learn to connect Claude to your tools and data

This tutorial walks you through setting up and using Claude's connector integrations to enhance your workflow.

## What you'll learn

* Setting up your first connector
* Using connectors in conversations
* Best practices for each integration
* Troubleshooting common issues

## Prerequisites

* A Claude account (Pro, Max, Team, or Enterprise for most connectors)
* Accounts on the services you want to connect

## Setting up your first connector

### Step 1: Access connector settings

1. Go to [claude.ai](https://claude.ai)
2. Select **Customize** in the sidebar
3. Select **Connectors**

### Step 2: Choose a connector

Available connectors include:

* Google Drive, Gmail, Calendar
* GitHub
* Slack
* Microsoft 365

### Step 3: Authenticate

1. Click "Connect" next to your chosen service
2. Log in to your account on that service
3. Grant Claude the requested permissions
4. Return to Claude

## Using connectors in conversations

### In chat

1. Start a new conversation
2. Click the "+" button
3. Select "Add from \[Service]"
4. Choose the content you want to include
5. Ask your question

### In projects

1. Open your project
2. Click "Add Content"
3. Select the connector
4. Add documents to your project knowledge

## Connector-specific tips

### Google Drive

* Best for: Document analysis, research
* Add multiple Google Docs for comprehensive context
* Documents sync automatically with updates

### Gmail & Calendar

* Best for: Finding information, scheduling context
* Ask questions like "What did Sarah say about the budget?"
* Claude can search your emails but can't send them

### GitHub

* Best for: Code understanding, documentation
* Add entire repositories or specific files
* Use with Projects for persistent codebase context

### Slack

* Best for: Finding discussions, team context
* Search channels and direct messages
* Requires installing the earlier Claude in Slack app first

### Microsoft 365

* Best for: Enterprise document search
* Access SharePoint, OneDrive, Outlook, Teams
* Requires a work or school Microsoft account

## Best practices

1. **Connect what you need**: Only connect services with relevant data
2. **Review permissions**: Understand what Claude can access
3. **Keep context focused**: Don't overload with too much data

## Troubleshooting

<AccordionGroup>
  <Accordion title="Connector won't authenticate">
    * Clear browser cookies and try again
    * Check that you have the right account permissions
    * Try a different browser
  </Accordion>

  <Accordion title="Data not showing up">
    * Verify you have access to the data in the source service
    * Wait a moment for sync to complete
    * Try disconnecting and reconnecting
  </Accordion>

  <Accordion title="Connection expired">
    * Go to Customize > Connectors
    * Click "Reconnect" or "Refresh"
    * Re-authenticate with the service
  </Accordion>
</AccordionGroup>

## Related topics

<Columns cols={2}>
  <Card title="Connectors Overview" icon="plug" href="/docs/connectors/overview">
    See all available connectors.
  </Card>

  <Card title="Custom Connectors" icon="code" href="/docs/connectors/custom/remote-mcp">
    Build your own integrations with MCP.
  </Card>
</Columns>
