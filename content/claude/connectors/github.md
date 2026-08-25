> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub integration

> Connect your code repositories to Claude

Connect GitHub repositories directly to Claude to provide comprehensive context for software development tasks. Claude can understand your codebase and assist with development questions.

<Note>
  Available on all plans including Free.
</Note>

## Adding GitHub repositories

### In chats

1. Click the "+" button in the lower left corner of the chat interface
2. Select "Add from GitHub" from the dropdown menu
3. Use the file browser to select specific files and folders
4. When sending your message, Claude accesses and processes the selected content

### In projects

1. Click the "+" button in your project knowledge section
2. Select "GitHub" from the dropdown
3. Search accessible repositories or paste a repository URL
4. Use the file browser to select specific files and folders
5. Your selected content is added to project knowledge

**Keeping content current:**

* Use the "Sync" icon to ensure you're working with the latest codebase
* Use the "Configure files" icon to modify which files Claude analyzes

<Note>
  If you're not authenticated with GitHub, you'll be redirected to authenticate before using the integration.
</Note>

## Connecting to private repositories

If you see a warning after entering a valid URL, you're likely attempting to connect to a private repository.

Follow the link to the GitHub App where you can:

* **Grant access yourself**: Choose between allowing Claude access to all repos or specific ones
* **Request access**: GitHub organization administrators receive an email notification. Once approved, you can sync and access the repository

## Best practices

1. **Start small**: Begin with a small codebase subset to understand how Claude interprets your code
2. **Iterate and refine**: Ask follow-up questions if initial responses need clarification
3. **Combine with human expertise**: Use Claude's insights as a starting point for team discussion
4. **Thoughtful file selection**: Include key files central to your task while staying within token limits
5. **Regular updates**: Refresh GitHub sync periodically, especially before new analysis or major repo changes

## What information is retrieved

| Retrieved      | Not Retrieved       |
| -------------- | ------------------- |
| File names     | Commit history      |
| File contents  | Pull requests       |
| Branch content | Issues              |
|                | Repository metadata |

## Frequently asked questions

<AccordionGroup>
  <Accordion title="What if my repository updates after adding it?">
    Click "Sync now" to fetch the latest changes from your repository.
  </Accordion>

  <Accordion title="Can I add multiple repositories?">
    Yes, add multiple repositories to provide comprehensive context, provided they fit within Claude's context window.
  </Accordion>

  <Accordion title="What happens if I lose repository access?">
    You won't be able to view its contents in projects where it was previously added. The repository preview is removed, but conversation history remains.
  </Accordion>
</AccordionGroup>
