> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build your first plugin

> Build a plugin with one skill and an optional MCP connector, test it in Claude Code, validate it, and push it to GitHub, ready to submit your own.

By the end of this quickstart, you have a working example plugin with one skill and, optionally, one remote MCP connector, tested in Claude Code, validated, and pushed to GitHub, which is everything a plugin needs before you submit it to [Anthropic's directory](/docs/directory/publish). A plugin is a folder that packages skills, MCP connectors, commands, and agents, in any combination, so that people add them together.

This quickstart is for developers who have Claude Code installed and want to learn the plugin format by building one. You can follow it with a product that has a remote MCP server, or with only a skill.

<Note>
  * If you want to make a plugin from a conversation without writing files, see [Create a plugin with Claude](/docs/plugins/create-with-claude)
  * If you want to distribute a plugin only inside your own organization, see [Roll out a plugin to your whole organization](/docs/plugins/org-rollout)
  * If you want to look up the folder layout, the manifest fields, or what each surface loads, see [Plugin structure and testing](/docs/plugins/build)
</Note>

## Before you create the plugin

Check that you have each of these before you create the plugin:

* **Claude Code**: [install Claude Code](https://code.claude.com/docs/en/setup). You use it to test and validate the plugin
* **A GitHub repository**: the directory reads plugins from repositories on github.com, and the repository must be public before the listing goes live

## Create the plugin

The steps in this section build a plugin named `expense-reports` for a fictional finance product whose MCP server is at `mcp.example.com`. Replace the names and values with your own.

<Steps>
  <Step title="Write the manifest">
    Create a folder named `expense-reports`, and create `.claude-plugin/plugin.json` inside it. Put only the manifest inside `.claude-plugin/`. Everything else goes at the plugin's top level.

    The directory requires the manifest, and the example has the fields that every surface and the directory read:

    ```json theme={null}
    {
      "name": "expense-reports",
      "displayName": "Expense Reports",
      "version": "1.0.0",
      "description": "File, track, and approve expense reports from a conversation, using your finance system's connector and your company's approval rules.",
      "author": { "name": "Example Corp", "url": "https://example.com" },
      "license": "MIT"
    }
    ```

    People install and refer to the plugin by its `name`. Use lowercase words joined by hyphens, make the name specific to your product, and never change it after release. [Manifest and plugin name](/docs/plugins/pre-submission-checklist#manifest-and-plugin-name) lists the directory's checks on the name.
  </Step>

  <Step title="Add a skill">
    Create `skills/file-expense/SKILL.md`. A skill tells Claude when and how to do a task. The example calls tools from the MCP connector that you add in the next step, so leave the tool calls out of your own skill if your plugin has no connector:

    ```markdown theme={null}
    ---
    name: file-expense
    description: File an expense report. Use when the user mentions a receipt, reimbursement, or expense, or asks to submit spending for approval.
    ---

    To file an expense:

    1. Ask for the receipt if the user hasn't attached one, and read the amount, date, merchant, and currency from it.
    2. Call the expenses connector's `create_report` tool with those fields. Default the category from the merchant type; ask only if it's ambiguous.
    3. If the amount is over the user's approval limit (check with `get_policy`), add their manager as approver before submitting.
    4. Reply with the report number and its approval status. Don't paste the full API response.
    ```

    Claude decides when to load the skill from the `description` line, so write it as the situations a user would be in. [Create custom skills](/docs/skills/how-to) covers the frontmatter fields, resource files, scripts, and testing.
  </Step>

  <Step title="Add an MCP connector">
    Skip this step if your plugin has only a skill. If your product has a remote MCP server, create `.mcp.json` at the plugin root and reference the server by URL:

    ```json theme={null}
    {
      "mcpServers": {
        "expenses": {
          "type": "http",
          "url": "https://mcp.example.com/mcp"
        }
      }
    }
    ```

    There is no server at `mcp.example.com`, so this example connector fails to connect when you test the plugin. Replace the URL with your own server's, or leave `.mcp.json` out.

    Don't put API keys or other secrets in this file, because every person who installs the plugin receives its files. On claude.ai and in Cowork, the entry is listed on the plugin's **Connectors** tab, where the user [adds or connects it](/docs/plugins/overview#bundled-connectors) and signs in through your server's OAuth flow. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.
  </Step>

  <Step title="Write the README">
    Create `README.md` in the plugin folder with at least 40 words. Words inside code blocks don't count. Say what the plugin does, how to use it, and what data it sends. The directory shows your README as the listing's description, and [README and license](/docs/plugins/pre-submission-checklist#readme-and-license) lists what validation checks.

    This README covers those three points for the example plugin:

    ```markdown theme={null}
    # Expense Reports

    File, track, and approve expense reports from a conversation with Claude.

    ## Use it

    Attach a receipt and ask Claude to file it. Claude reads the amount, date,
    and merchant, files the report through the Expense Reports connector, and
    replies with the report number. Ask what's waiting on you to list the
    reports that need your approval.

    ## Data

    The plugin sends receipt details and report fields to your Example Corp
    account through mcp.example.com. It stores nothing itself.
    ```
  </Step>

  <Step title="Check the license">
    The directory requires a `LICENSE` file in the plugin folder or `license` in `plugin.json`, and validation blocks a plugin that has neither. The example manifest sets `license`, which meets the requirement. If you remove that field, add a `LICENSE` file to the plugin folder instead.
  </Step>
</Steps>

## Test the plugin in Claude Code

Load the plugin from your working copy before you push it. From the folder that contains `expense-reports`, start a Claude Code session with the plugin loaded:

```bash theme={null}
claude --plugin-dir ./expense-reports
```

In that session, your skill appears as `/expense-reports:file-expense`. If you added the connector, `/mcp` shows the server's connection state. With the example's `mcp.example.com` URL, the `expenses` server shows as failed because no server exists at that address, and Claude reports that it can't reach the server when the skill calls its tools.

To try the skill, describe one of the situations that its `description` line names, such as a receipt you want reimbursed. Claude decides when to load the skill from that line.

To test the plugin on claude.ai and in Cowork as well, see [Test the plugin on each surface](/docs/plugins/build#test-the-plugin-on-each-surface).

## Validate the plugin

Run `claude plugin validate` on the folder to catch syntax and schema errors on your machine before you push:

```bash theme={null}
claude plugin validate ./expense-reports
```

The command prints `✔ Validation passed` when the manifest and the component files parse, and names the field to fix when they don't.

The plugin is checked at these points before it's listed, and the portal checks more than the command does:

* **The command**: checks the plugin for syntax and schema errors
* **Validate in the developer portal**: the **Validate** button in the [developer portal](https://claude.ai/directory/manage) runs every validation check. The directory's own checks, such as the README, license, and name checks, run there and not in the command
* **The scan after you submit**: checks the plugin's files again and runs a security scan

The [Plugin pre-submission checklist](/docs/plugins/pre-submission-checklist) lists every check and what each result means.

## Push the plugin to GitHub

The directory reads plugins from repositories on github.com, so the plugin folder goes in a GitHub repository.

<Steps>
  <Step title="Create the repository">
    Create an empty repository on github.com for the plugin. The repository must be public before the listing goes live.
  </Step>

  <Step title="Remove system files">
    Remove `.DS_Store`, `Thumbs.db`, `desktop.ini`, and `__MACOSX` entries from the plugin folder, and add them to `.gitignore`. Validation blocks a plugin that contains them.
  </Step>

  <Step title="Commit and push">
    From inside the `expense-reports` folder, commit the files and push them. The example pushes to a repository named `example-corp/expense-reports`, so replace that name with your own:

    ```bash theme={null}
    git init -b main
    git add .
    git commit -m "Add the expense-reports plugin"
    git remote add origin https://github.com/example-corp/expense-reports.git
    git push -u origin main
    ```

    The repository's page on github.com now shows `.claude-plugin/`, `skills/`, and the other plugin files at the repository root.
  </Step>
</Steps>

## Submit your own plugin

The `expense-reports` plugin you built on this page is a small demonstration of the format, so there's no reason to submit it: the directory is for plugins other people will use, and it refuses a name another organization has already listed. Use the same steps to build your own plugin, with its own name, skills, and connector.

When your plugin validates and is pushed to a public GitHub repository, submit it from the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage): select **Submit new**, choose **Plugin bundle**, and follow [Submit a plugin](/docs/plugins/submit#submit-a-plugin) for each field and for what happens after you submit. If your plugin points at a remote MCP server you run, [submit that server as a connector too](/docs/directory/publish#submit-your-plugin-and-your-mcp-server-as-a-connector). [Who can submit to the directory](/docs/directory/publish#confirm-you-can-submit-to-the-directory) has the plan and role requirements.

## Next steps

* [Plugin structure and testing](/docs/plugins/build): look up the folder layout and manifest fields, and test on claude.ai and in Cowork
* [Plugin pre-submission checklist](/docs/plugins/pre-submission-checklist): fix each validation and scan finding before you submit
* [Submit a plugin](/docs/plugins/submit): fill in each portal field, then publish and update the listed plugin
* [Track your submission](/docs/directory/submission-status): check what your submission's status means and who acts next
* [Plugin feature support across platforms](/docs/plugins/platform-support): check which of the plugin's components load in chat, Cowork, and Claude Code
* [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals): write eval cases and compare the plugin's results against a run without the plugin
