> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack integration

> Use Claude directly in your Slack workspace with the Claude in Slack app, and let Claude search Slack with the Slack connector

You can use Claude with Slack in two ways. The Claude in Slack app puts Claude inside your Slack workspace so you can message it there, and the Slack connector lets Claude in claude.ai search your workspace's channels, direct messages, and files for context. The app is available to paid Slack plans once a Slack admin approves it; the connector is available on Team and Enterprise plans and requires the app to be installed first.

By the end of this page you have installed the app, connected your account, and, if your plan includes it, turned on the connector and asked Claude a question that draws on Slack.

<Note>
  This page covers the earlier per-user Claude in Slack app. The current product is [Claude Tag](/docs/claude-tag/overview), which gives your team one Claude identity set up by an admin. If your organization used the earlier app, see [Migrate from the earlier Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier).
</Note>

## Use the earlier Claude in Slack app

Claude in Slack is available to users on paid Slack plans. A Slack admin must approve the app for your workspace before individual users can connect to it. Once it's installed, you can reach Claude in three places:

* **Direct messages**: start a private conversation with @Claude
* **AI assistant panel**: select Claude's icon in Slack's AI assistant header
* **Threads**: mention @Claude in any thread to bring it into the discussion

Direct messages, the AI assistant panel, and threads all support the same Claude capabilities you've enabled, including web search and tool integrations. On Team and Enterprise plans, users with Claude Code access can also route coding tasks to Claude Code by mentioning @Claude.

### Install the app

A Slack admin adds the app to the workspace first, and then each person connects their own Claude account.

<Tabs>
  <Tab title="Slack admins">
    <Steps>
      <Step title="Find the app">
        Open the Claude app's listing in the Slack App Marketplace.
      </Step>

      <Step title="Add the app to Slack">
        Select **Add to Slack**, then review and approve the app for your organization.
      </Step>

      <Step title="Choose where to deploy">
        Deploy the app org-wide or to specific workspaces.
      </Step>
    </Steps>

    To add the app to more workspaces later, open your Slack management workspace, go to **Integrations > Installed apps > Add to more workspaces**, and turn on each workspace that should have it.
  </Tab>

  <Tab title="Individual users">
    <Steps>
      <Step title="Find Claude">
        Find **Claude** in your Slack apps list or in the Slack App Marketplace.
      </Step>

      <Step title="Connect your account">
        Select **Connect Account**, select your Claude organization, and then select **Authorize** to grant access.
      </Step>

      <Step title="Start a conversation">
        Return to Slack and select **+ New Chat**, or mention @Claude in a channel or thread.
      </Step>
    </Steps>

    If your company's Slack requires admin approval and you aren't an admin, you see a **Request to install** prompt instead. Ask a Slack admin to approve the app, then connect.

    To pin Claude to your Slack header, open the app's three-dot menu in Slack and select **Add this app to header**.
  </Tab>
</Tabs>

## Search Slack with the connector

The Slack connector is available on Team and Enterprise plans. With it turned on, Claude in claude.ai can search your workspace's channels, direct messages, and files to answer your questions. Install the Claude in Slack app before you enable the connector.

### Enable the connector

An Owner enables the connector for the organization once, and then each member connects their own account.

<Steps>
  <Step title="Enable the connector for your organization">
    An Owner goes to [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors) in claude.ai and enables the Slack connector.
  </Step>

  <Step title="Open your connectors">
    Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) in claude.ai. **Customize** is the page that holds your connectors, skills, and plugins.
  </Step>

  <Step title="Connect Slack">
    Find **Slack** and select **Connect**.
  </Step>
</Steps>

When the connection succeeds, the **Connect** button on the Slack connector changes to **Disconnect**.

### Try the connector

In a conversation, select **+** at the lower left of the message box, select **Connectors**, and turn on **Slack**. Then ask a question about something discussed in your workspace. For example, ask Claude:

* What did the team decide about the launch date in #product-planning last week?
* Find the thread about the vendor contract renewal and summarize it

Claude searches your workspace's channels, direct messages, and files and answers from what it finds.

## Manage your connections

You can check the app's connection from inside Slack, and disconnect either the app or the connector separately.

To view your connection status, select **Claude** in your Slack sidebar and open the **Home** tab, which shows your connection details.

To disconnect, use the surface that matches what you want to remove:

* **Claude in Slack app**: on the app's **Home** tab in Slack, select **Disconnect**
* **Slack connector**: go to [**Customize > Connectors**](https://claude.ai/customize/connectors), find **Slack**, and select **Disconnect**

<Note>
  Disconnecting removes your account connection and deletes past conversations within 30 days.
</Note>

## Privacy and data

Conversations with Claude in Slack are kept apart from your claude.ai history:

* Conversations you start in Slack don't appear in your claude.ai chat history. Each platform keeps its own conversation history
* If you disconnect, your Slack conversations with Claude are deleted within 30 days
* Your workspace's Slack retention policies apply to the messages in Slack

## Next steps

* [Claude Tag](/docs/claude-tag/overview): the current product, which gives your team one Claude identity set up by an admin
* [Get started with connectors](/docs/connectors/getting-started): set up another connector and use it in conversations
* [Connectors directory](/docs/connectors/directory): browse verified and community integrations
