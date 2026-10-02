> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub integration

> Add a GitHub repository to a conversation, or files and folders from a repository to a project, so Claude can read your code

The GitHub integration lets you add a GitHub repository to a conversation, or files and folders from a repository to a project, so Claude can read your code and answer development questions with that context. It's available on every plan, including Free, and works with public repositories and with private repositories you grant access to.

By the end of this page you have added repository content to a chat or a project and asked Claude about it. Claude reads file names and contents only: it doesn't see commit history, pull requests, or issues.

<Note>
  If you want Claude to edit code, run commands, and open pull requests in your repository, see [Claude Code](https://code.claude.com/docs).
</Note>

## Add repository content

You can add repository content to a single conversation, or to a [project](https://support.claude.com/en/articles/9517075-what-are-projects), a workspace in Claude where a set of chats share the same background documents. Choose the tab below for where you want the content available.

<Tabs>
  <Tab title="In a chat">
    In a chat, the **Add from GitHub** option appears only after your GitHub account is connected to Claude. To connect your GitHub account, follow these steps:

    1. Go to [**Customize > Connectors**](https://claude.ai/customize/connectors).
    2. Select **GitHub Integration**.
    3. Select **Connect**.

    After your GitHub account is connected, add a repository to a chat:

    <Steps>
      <Step title="Open the add menu">
        In the conversation, select **+** at the lower left of the message box.
      </Step>

      <Step title="Choose GitHub">
        Select **Add from GitHub**.
      </Step>

      <Step title="Pick a repository">
        Search the repositories you have access to, or paste a repository URL.
      </Step>

      <Step title="Add the repository">
        Select **Add repository**. Claude adds the repository's URL to your message.
      </Step>

      <Step title="Send your message">
        Send your question.
      </Step>
    </Steps>
  </Tab>

  <Tab title="In a project">
    You can add repository content only to a private project, one you haven't shared with other people. In a shared project, the **GitHub** option is dimmed and shows **Only accessible from private projects**.

    If your GitHub account isn't connected to Claude yet, selecting **GitHub** sends you to GitHub to sign in before you continue.

    <Steps>
      <Step title="Open project knowledge">
        Open the project and, in its project knowledge section, select **+**.
      </Step>

      <Step title="Choose GitHub">
        Select **GitHub**.
      </Step>

      <Step title="Pick a repository">
        Search the repositories you have access to, or paste a repository URL.
      </Step>

      <Step title="Select files and folders">
        Use the file browser to select the files and folders you want Claude to read.
      </Step>

      <Step title="Add the files">
        Select **Add files**.
      </Step>
    </Steps>

    The selected content is added to the project's knowledge.
  </Tab>
</Tabs>

## Grant Claude access to a private repository

When you pick a private repository that Claude doesn't have access to yet, or paste its URL, the **Add content from GitHub** dialog shows **Claude cannot access that resource. If you know that it exists, you may first need to grant or request access here.** The **here** link in that message opens the Claude GitHub App installation page on GitHub, where you have two options:

* **Grant access yourself**: allow Claude access to all of your repositories or only to specific ones
* **Request access**: for a repository owned by a GitHub organization you don't administer, ask for access. The organization's administrators receive an email notification from GitHub.

After access is granted, pick the repository again.

## Try the connector

After you add repository content, ask Claude something that depends on the code you added. For example, ask Claude:

* Explain how request authentication works in this repository
* Where is the retry logic, and what happens when it gives up?

Claude doesn't see commit history, pull requests, issues, or repository metadata. [Review what Claude retrieves from GitHub](#review-what-claude-retrieves-from-github) has the full list.

## Keep repository content current

After you add a repository to a project, use these controls in your project knowledge to keep its content current:

* **Sync**: select **Sync now** on the repository in your project knowledge to fetch the latest changes, especially before a new analysis or after major changes to the repository
* **Multiple repositories**: you can add several repositories for broader context, as long as the selected content fits within Claude's context window
* **Lost access**: if you lose access to a repository, you can no longer view its contents in projects where it was added. The repository preview is removed, but your conversation history remains

### Change which files Claude reads in a project

You can change which files and folders Claude reads from a repository you already added to a project.

1. Open the project.
2. In your project knowledge, select the repository.
3. Select the files and folders you want Claude to read.
4. Select **Update**.

## Review what Claude retrieves from GitHub

The table lists what the integration reads from a repository and what it leaves out.

| Retrieved | Not retrieved |
| - | - |
| File names | Commit history |
| File contents | Pull requests |
| Branch content | Issues |
| | Repository metadata |

## Best practices

These habits help when you add repository content to a project:

* **Start small**: begin with a small subset of the codebase to see how Claude interprets your code
* **Select files thoughtfully**: include the files central to your task while staying within token limits
* **Iterate and refine**: ask follow-up questions when an initial response needs clarification
* **Combine with human expertise**: treat Claude's analysis as a starting point for team discussion
* **Sync regularly**: refresh the GitHub sync periodically, especially before a new analysis or after major repository changes

## Troubleshooting

The GitHub integration is built into Claude and managed from [**Customize > Connectors**](https://claude.ai/customize/connectors), where it's listed as **GitHub Integration** under **Your connectors** whether or not you've connected it.

### Add from GitHub doesn't appear in a chat

The **+** menu in a chat shows **Add from GitHub** only after your GitHub account is connected to Claude. Go to [**Customize > Connectors**](https://claude.ai/customize/connectors), select **GitHub Integration** under **Your connectors**, and select the **Connect** button. Then open the **+** menu in the chat again.

On Team and Enterprise plans, **GitHub Integration** appears in **Customize > Connectors** only while GitHub is turned on for your organization. If it isn't listed there, ask someone who manages your organization's settings to turn it on in [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors).

### Claude cannot access that resource

Claude couldn't reach the repository you picked or pasted. If the repository exists, it's most likely private and Claude doesn't have access to it yet. Follow [Grant Claude access to a private repository](#grant-claude-access-to-a-private-repository), then pick the repository again.

## Next steps

* [Add a connector from the directory](/docs/connectors/getting-started#add-a-connector-from-the-directory): find a connector for another service in the directory and connect it
* [Connectors directory](/docs/connectors/directory): browse verified and community integrations
