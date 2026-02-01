Title: Claude Code overview - Claude Code Docs

URL Source: https://www.anthropic.com/engineering/claude-code-best-practices

Markdown Content:
Get started in 30 seconds
-------------------------

Prerequisites:

*   A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**To install Claude Code, use one of the following methods:

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

**Start using Claude Code:**

```
cd your-project
claude
```

You’ll be prompted to log in on first use. That’s it! [Continue with Quickstart (5 minutes) →](https://code.claude.com/docs/en/quickstart)

What Claude Code does for you
-----------------------------

*   **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
*   **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
*   **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](https://code.claude.com/docs/en/mcp) can pull from external data sources like Google Drive, Figma, and Slack.
*   **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

Why developers love Claude Code
-------------------------------

*   **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
*   **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](https://code.claude.com/docs/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use _your_ custom developer tooling.
*   **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"`_works_. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
*   **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](https://code.claude.com/docs/en/security), [privacy](https://code.claude.com/docs/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

Use Claude Code everywhere
--------------------------

Claude Code works across your development environment: in your terminal, in your IDE, in the cloud, and in Slack.

*   **[Terminal (CLI)](https://code.claude.com/docs/en/quickstart)**: the core Claude Code experience. Run `claude` in any terminal to start coding.
*   **[Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)**: use Claude Code from your browser at [claude.ai/code](https://claude.ai/code) or the Claude iOS app, with no local setup required. Run tasks in parallel, work on repos you don’t have locally, and review changes in a built-in diff view.
*   **[Desktop app](https://code.claude.com/docs/en/desktop)**: a standalone application with diff review, parallel sessions via git worktrees, and the ability to launch cloud sessions.
*   **[VS Code](https://code.claude.com/docs/en/vs-code)**: a native extension with inline diffs, @-mentions, and plan review.
*   **[JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)**: a plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with IDE diff viewing and context sharing.
*   **[GitHub Actions](https://code.claude.com/docs/en/github-actions)**: automate code review, issue triage, and other workflows in CI/CD with `@claude` mentions.
*   **[GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)**: event-driven automation for GitLab merge requests and issues.
*   **[Slack](https://code.claude.com/docs/en/slack)**: mention Claude in Slack to route coding tasks to Claude Code on the web and get PRs back.
*   **[Chrome](https://code.claude.com/docs/en/chrome)**: connect Claude Code to your browser for live debugging, design verification, and web app testing.

Next steps
----------

Additional resources
--------------------
