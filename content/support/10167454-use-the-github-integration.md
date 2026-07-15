# Use the GitHub integration

For more information on enabling GitHub within your account, see **[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**.

Connect your GitHub repositories directly to Claude to provide comprehensive context for your software development tasks. You can easily add repositories by selecting them from a list, helping Claude better understand and assist with your codebase.

## How to add GitHub repositories

**Note:**  If you're currently unauthenticated with GitHub, you'll be redirected to GitHub to authenticate before you can use this integration.

### Chats

1. Click the "+" button on the lower left corner of the chat interface.

2. Select "Add from GitHub" from the drop-down.

3. Use the file browser to select specific files and folders.

4. When you send your message, Claude will access and process the content to inform its response.

### Projects

1. Click the "+" button in the upper right corner of your project knowledge section.

2. Select "GitHub" from the drop-down.

3. Search through your accessible repositories, or paste a repository URL.

4. Use the file browser to select specific files and folders.

5. Your selected content will be added to the project knowledge for Claude to access and process.

6. You can use the "Sync" icon to ensure you're working with the most up-to-date version of your codebase.

7. You can use the "Configure files" icon to modify which files and folders Claude analyzes.

## Connect to private repositories

- **If Claude cannot access a repository after you enter a valid URL, it most likely means you're attempting to connect Claude to a private repository**: Follow the link to our GitHub App, where you can grant access to repos if you're a GitHub administrator, or send a request to your GitHub organization's administrators.

- **Grant access yourself if you can**: You can choose between letting Claude access all repos or specific ones.

- **Request access if you don't have the necessary permissions**: The administrators of your GitHub organization will receive an email notification about your request. Once they approve the request, you'll be able to sync and access the repository in Claude.

---

## Best practices

1. **Start small**: Begin by selecting a small subset of your codebase to analyze. This will help you get familiar with how Claude interprets and discusses your code.

2. **Iterate and refine**: If Claude's initial response doesn't fully address your question, don't hesitate to ask follow-up questions or request clarification.

3. **Combine with human expertise**: Use Claude's insights as a starting point for further investigation and discussion with your team. Please review Claude's work.

4. **Thoughtful file selection**: When using "Configure files," be strategic about your selections. Include key files and directories that are central to your current task or project, but avoid selecting unnecessary files to keep within token limits and maintain focus.

5. **Regular updates**: Remember to refresh your project's GitHub sync periodically to ensure Claude is working with the most up-to-date version of your codebase and especially before starting a new analysis or when you know there have been significant changes to your repo.

---

## Troubleshooting

### Repositories from an organization don't appear after connecting

If your GitHub connection shows as connected but private repositories from a specific organization don't appear, that organization may require single sign-on (SSO). When SSO is required, each user must separately authorize the Claude app for that organization. Until you do, GitHub filters that organization's private repositories from your view, even though your connection is otherwise working.

When Claude detects this state, the repository picker shows a banner prompting you to authorize SSO. To authorize the Claude app for your organization:

1. Go to **[github.com/settings/applications](https://github.com/settings/applications)** and open the **Claude** entry.

2. Under **Organization access**, click "Grant" next to the relevant GitHub organization.

3. If the button reads "Request" instead of "Grant," you don't have permission to authorize the app yourself. A GitHub organization admin must approve your request from the organization's OAuth application policy settings.

**Important:** Disconnecting and reconnecting GitHub in your Claude settings won't fix this. A fresh connection doesn't automatically authorize organizations that require SSO, so you'll need to complete the authorization steps above.

If your organization uses GitHub Enterprise Cloud with Enterprise Managed Users (EMU), the Claude app must also be approved at the enterprise level. Learn more in **[Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code#h_49cea7a027)**.

---

## Frequently asked questions

### What information is retrieved from GitHub?

Only files (names and contents) in a repo on a specific branch are synced. We do not retrieve commit history, PRs, or other metadata.

### What happens if my repository is updated after adding it to a project?

You can click "Sync now" to fetch the latest changes from your repository. This will update all previously selected files and folders.

### Can I add multiple repositories to a single project or chat?

Yes, you can add multiple repositories to provide Claude with comprehensive context for your development tasks. The repositories must fit within Claude's context window.

### What happens if I lose access to a repository?

If you lose access to a repository, you won't be able to view its contents in projects where it was previously added. The repository preview will be removed, though the conversation history will be maintained.

Browse all available connectors in the **[Connectors Directory](https://claude.ai/directory)**.