Title: Claude Code overview - Claude Code Docs

URL Source: https://www.anthropic.com/engineering/claude-code-best-practices

Markdown Content:
Claude Code is an agentic coding tool that reads your codebase, edits files, and runs commands. It works in your terminal, IDE, browser, and as a desktop app.

Get started
-----------

Choose your environment to get started. Most surfaces require a [Claude subscription](https://claude.com/pricing) or [Anthropic Console](https://console.anthropic.com/) account. The Terminal CLI and VS Code also support [third-party providers](https://code.claude.com/docs/en/third-party-integrations).

*   Terminal

*   VS Code

*   Desktop app

*   Web

*   JetBrains

The full-featured CLI for working with Claude Code directly in your terminal. Edit files, run commands, and manage your entire project from the command line.To install Claude Code, use one of the following methods:

*   Native Install (Recommended)

*   Homebrew

*   WinGet

**macOS, Linux, WSL:**

```
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

```
brew install --cask claude-code
```

```
winget install Anthropic.ClaudeCode
```

Then start Claude Code in any project:

```
cd your-project
claude
```

You’ll be prompted to log in on first use. That’s it! [Continue with the Quickstart →](https://code.claude.com/docs/en/quickstart)

The VS Code extension provides inline diffs, @-mentions, plan review, and conversation history directly in your editor.

*   [Install for VS Code](vscode:extension/anthropic.claude-code)
*   [Install for Cursor](cursor:extension/anthropic.claude-code)

Or search for “Claude Code” in the Extensions view (`Cmd+Shift+X` on Mac, `Ctrl+Shift+X` on Windows/Linux). After installing, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`), type “Claude Code”, and select **Open in New Tab**.[Get started with VS Code →](https://code.claude.com/docs/en/vs-code#get-started)

A standalone app for running Claude Code outside your IDE or terminal. Review diffs visually, run multiple sessions side by side, and kick off cloud sessions.Download and install:

*   [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs) (Intel and Apple Silicon)
*   [Windows](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs) (x64)

After installing, launch Claude, sign in, and click the **Code** tab to start coding.[Learn more about the desktop app →](https://code.claude.com/docs/en/desktop#installation-and-setup)

Run Claude Code in your browser with no local setup. Kick off long-running tasks and check back when they’re done, work on repos you don’t have locally, or run multiple tasks in parallel. Available on desktop browsers and the Claude iOS app.Start coding at [claude.ai/code](https://claude.ai/code).[Get started on the web →](https://code.claude.com/docs/en/claude-code-on-the-web#getting-started)

A plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with interactive diff viewing and selection context sharing.Install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains Marketplace and restart your IDE.[Get started with JetBrains →](https://code.claude.com/docs/en/jetbrains)

What you can do
---------------

Here are some of the ways you can use Claude Code:

Use Claude Code everywhere
--------------------------

Each surface connects to the same underlying Claude Code engine, so your CLAUDE.md files, settings, and MCP servers work across all of them.Beyond the [Terminal](https://code.claude.com/docs/en/quickstart), [VS Code](https://code.claude.com/docs/en/vs-code), [JetBrains](https://code.claude.com/docs/en/jetbrains), [Desktop](https://code.claude.com/docs/en/desktop), and [Web](https://code.claude.com/docs/en/claude-code-on-the-web) environments above, Claude Code integrates with CI/CD, chat, and browser workflows:

| I want to… | Best option |
| --- | --- |
| Start a task locally, continue on mobile | [Web](https://code.claude.com/docs/en/claude-code-on-the-web) or [Claude iOS app](https://apps.apple.com/app/claude-by-anthropic/id6473753684) |
| Automate PR reviews and issue triage | [GitHub Actions](https://code.claude.com/docs/en/github-actions) or [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) |
| Route bug reports from Slack to pull requests | [Slack](https://code.claude.com/docs/en/slack) |
| Debug live web applications | [Chrome](https://code.claude.com/docs/en/chrome) |
| Build custom agents for your own workflows | [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) |

Next steps
----------

Once you’ve installed Claude Code, these guides help you go deeper.

*   [Quickstart](https://code.claude.com/docs/en/quickstart): walk through your first real task, from exploring a codebase to committing a fix
*   Level up with [best practices](https://code.claude.com/docs/en/best-practices) and [common workflows](https://code.claude.com/docs/en/common-workflows)
*   [Settings](https://code.claude.com/docs/en/settings): customize Claude Code for your workflow
*   [Troubleshooting](https://code.claude.com/docs/en/troubleshooting): solutions for common issues
*   [code.claude.com](https://code.claude.com/): demos, pricing, and product details
