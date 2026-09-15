# Set up Salesforce in Claude for your organization

Salesforce in Claude is a plugin built by Salesforce that brings your organization's Salesforce data and workflows into Claude. This article walks admins through enabling the plugin and connecting Salesforce for your organization.

For end-user instructions about how to use Salesforce in Claude, see **[Use Salesforce in Claude](https://support.claude.com/en/articles/16952186)**.

Salesforce in Claude is available in beta on all paid plans for organizations Salesforce approves through its beta sign-up. It currently works in chat and Claude Cowork (web and desktop).

## What's included

Salesforce in Claude bundles:

- 37 sales skills built by Salesforce, covering workflows like renewal prep, QBR decks, pipeline coverage, and meeting follow-up.

- The Salesforce and Slack connectors, so the plugin works without connecting each service separately.

- A setup skill that runs the first time a user opens the plugin. It learns the user's role and book of business and personalizes the skills to them.

## Before you begin

Your organization needs access to the latest Sales Cloud enterprise edition to be eligible for beta.

## Step 1: Request access to the Salesforce in Claude plugin (Salesforce admins)

To install the Salesforce in Claude plugin, admins on your Salesforce account can request access through AgentExchange:

1. Go to **[AgentExchange](https://agentexchange.salesforce.com/sales-cloud-in-claude-beta-access)**.

2. Fill out the form to request access to the Salesforce in Claude plugin. Admins will receive an acceptance email with a link to a Salesforce help article for setup instructions.

3. Complete the setup instructions in your acceptance email.

## Step 2: Enable Salesforce in Claude for your organization (Claude admins)

After you complete step 1, choose your installation preference and connect the MCP connector. You need Primary Owner or Owner access for the Claude organization to complete these steps.

To choose your installation preference:

1. Go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

2. Find **Salesforce Marketplace**.

3. Choose an installation preference for the groups you want to use it: installed by default, available for install, or required. Learn more about **[controlling plugin distribution](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization#h_cef6a5f497)**.

To activate and configure the Salesforce MCP Connector:

1. Your Salesforce admin follows Salesforce's setup guide to turn on the Salesforce MCP server.

2. The admin sends you the External Client App's consumer key and consumer secret.

3. In Claude, go to **Organization settings > Connectors** and select "Salesforce (Beta)." Enter the consumer key in the **OAuth client ID** field and the consumer secret in the **OAuth client secret** field, then save.

After that, each member signs in to Salesforce with their own account the first time they use the plugin.

## Step 3: Activate the Salesforce in Claude plugin (members of your organization)

After you complete steps 1 and 2, members of your organization can turn on and use the plugin.

If you’re a member of an organization and want to learn more about using the Salesforce in Claude plugin, see **[Use Salesforce in Claude](https://support.claude.com/en/articles/16952186)**.

## What Claude can see and do in Salesforce

Claude signs in as each user's own Salesforce account and sees only what that user's existing Salesforce permissions already allow. By default, Claude asks you to approve each proposed change before it's written.