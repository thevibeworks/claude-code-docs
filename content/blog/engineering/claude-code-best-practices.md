Title: Claude Code overview - Claude Code Docs

URL Source: https://www.anthropic.com/engineering/claude-code-best-practices

Markdown Content:
Claude Code overview - Claude Code Docs
===============

[Skip to main content](https://www.anthropic.com/engineering/claude-code-best-practices#content-area)

[Claude Code Docs home page![Image 1: light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![Image 2: dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](https://www.anthropic.com/docs)

![Image 3: US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K Ask AI

*   [Claude Developer Platform](https://platform.claude.com/)
*   [Claude Code on the Web](https://claude.ai/code)
*   [Claude Code on the Web](https://claude.ai/code)

Search...

Navigation

Getting started

Claude Code overview

[Getting started](https://www.anthropic.com/docs/en/overview)[Build with Claude Code](https://www.anthropic.com/docs/en/sub-agents)[Deployment](https://www.anthropic.com/docs/en/third-party-integrations)[Administration](https://www.anthropic.com/docs/en/setup)[Configuration](https://www.anthropic.com/docs/en/settings)[Reference](https://www.anthropic.com/docs/en/cli-reference)[Resources](https://www.anthropic.com/docs/en/legal-and-compliance)

##### Getting started

*   [Overview](https://www.anthropic.com/docs/en/overview)
*   [Quickstart](https://www.anthropic.com/docs/en/quickstart)
*   [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

##### Core concepts

*   [How Claude Code works](https://www.anthropic.com/docs/en/how-claude-code-works)
*   [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview)
*   [Common workflows](https://www.anthropic.com/docs/en/common-workflows)
*   [Best practices](https://www.anthropic.com/docs/en/best-practices)

##### Outside of the terminal

*   [Claude Code on the web](https://www.anthropic.com/docs/en/claude-code-on-the-web)
*   [Claude Code on desktop](https://www.anthropic.com/docs/en/desktop)
*   [Chrome extension (beta)](https://www.anthropic.com/docs/en/chrome)
*   [Visual Studio Code](https://www.anthropic.com/docs/en/vs-code)
*   [JetBrains IDEs](https://www.anthropic.com/docs/en/jetbrains)
*   [GitHub Actions](https://www.anthropic.com/docs/en/github-actions)
*   [GitLab CI/CD](https://www.anthropic.com/docs/en/gitlab-ci-cd)
*   [Claude Code in Slack](https://www.anthropic.com/docs/en/slack)

On this page
*   [Get started in 30 seconds](https://www.anthropic.com/engineering/claude-code-best-practices#get-started-in-30-seconds)
*   [What Claude Code does for you](https://www.anthropic.com/engineering/claude-code-best-practices#what-claude-code-does-for-you)
*   [Why developers love Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices#why-developers-love-claude-code)
*   [Use Claude Code everywhere](https://www.anthropic.com/engineering/claude-code-best-practices#use-claude-code-everywhere)
*   [Next steps](https://www.anthropic.com/engineering/claude-code-best-practices#next-steps)
*   [Additional resources](https://www.anthropic.com/engineering/claude-code-best-practices#additional-resources)

Getting started

Claude Code overview
====================

Copy page

Learn about Claude Code, Anthropic’s agentic coding tool that works in your terminal, IDE, desktop app, and browser to help you turn ideas into code faster than ever before.

Copy page

[​](https://www.anthropic.com/engineering/claude-code-best-practices#get-started-in-30-seconds)

Get started in 30 seconds
--------------------------------------------------------------------------------------------------------------------------

Prerequisites:
*   Meet the [system requirements](https://www.anthropic.com/docs/en/setup#system-requirements)
*   A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**To install Claude Code, use one of the following methods:

*   Native Install (Recommended) 
*   Homebrew 
*   WinGet 

**macOS, Linux, WSL:**

Copy

Ask AI

```
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Copy

Ask AI

```
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Copy

Ask AI

```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Native installations automatically update in the background to keep you on the latest version.

Copy

Ask AI

```
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

Copy

Ask AI

```
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

**Start using Claude Code:**

Copy

Ask AI

```
cd your-project
claude
```

You’ll be prompted to log in on first use. That’s it! [Continue with Quickstart (5 minutes) →](https://www.anthropic.com/docs/en/quickstart)

See [advanced setup](https://www.anthropic.com/docs/en/setup) for installation options, manual updates, or uninstallation instructions. Visit [troubleshooting](https://www.anthropic.com/docs/en/troubleshooting) if you hit issues.

Claude Code also runs in [VS Code](https://www.anthropic.com/docs/en/vs-code), [JetBrains IDEs](https://www.anthropic.com/docs/en/jetbrains), as a [desktop app](https://www.anthropic.com/docs/en/desktop), [on the web](https://www.anthropic.com/docs/en/claude-code-on-the-web), and in [Slack](https://www.anthropic.com/docs/en/slack). See [all platforms](https://www.anthropic.com/engineering/claude-code-best-practices#use-claude-code-everywhere) below.
[​](https://www.anthropic.com/engineering/claude-code-best-practices#what-claude-code-does-for-you)

What Claude Code does for you
----------------------------------------------------------------------------------------------------------------------------------

*   **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
*   **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
*   **Navigate any codebase**: Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](https://www.anthropic.com/docs/en/mcp) can pull from external data sources like Google Drive, Figma, and Slack.
*   **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

[​](https://www.anthropic.com/engineering/claude-code-best-practices#why-developers-love-claude-code)

Why developers love Claude Code
--------------------------------------------------------------------------------------------------------------------------------------

*   **Meets you where you work**: Use Claude Code in your terminal, your IDE, or a standalone desktop app. It integrates with the tools you already use.
*   **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](https://www.anthropic.com/docs/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use _your_ custom developer tooling.
*   **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"`_works_. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
*   **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](https://www.anthropic.com/docs/en/security), [privacy](https://www.anthropic.com/docs/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

[​](https://www.anthropic.com/engineering/claude-code-best-practices#use-claude-code-everywhere)

Use Claude Code everywhere
----------------------------------------------------------------------------------------------------------------------------

Claude Code works across your development environment: in your terminal, in your IDE, in the cloud, and in Slack.
*   **[Terminal (CLI)](https://www.anthropic.com/docs/en/quickstart)**: the core Claude Code experience. Run `claude` in any terminal to start coding.
*   **[Claude Code on the web](https://www.anthropic.com/docs/en/claude-code-on-the-web)**: use Claude Code from your browser at [claude.ai/code](https://claude.ai/code) or the Claude iOS app, with no local setup required. Run tasks in parallel, work on repos you don’t have locally, and review changes in a built-in diff view.
*   **[Desktop app](https://www.anthropic.com/docs/en/desktop)**: a standalone application with diff review, parallel sessions via git worktrees, and the ability to launch cloud sessions.
*   **[VS Code](https://www.anthropic.com/docs/en/vs-code)**: a native extension with inline diffs, @-mentions, and plan review.
*   **[JetBrains IDEs](https://www.anthropic.com/docs/en/jetbrains)**: a plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with IDE diff viewing and context sharing.
*   **[GitHub Actions](https://www.anthropic.com/docs/en/github-actions)**: automate code review, issue triage, and other workflows in CI/CD with `@claude` mentions.
*   **[GitLab CI/CD](https://www.anthropic.com/docs/en/gitlab-ci-cd)**: event-driven automation for GitLab merge requests and issues.
*   **[Slack](https://www.anthropic.com/docs/en/slack)**: mention Claude in Slack to route coding tasks to Claude Code on the web and get PRs back.
*   **[Chrome](https://www.anthropic.com/docs/en/chrome)**: connect Claude Code to your browser for live debugging, design verification, and web app testing.

[​](https://www.anthropic.com/engineering/claude-code-best-practices#next-steps)

Next steps
--------------------------------------------------------------------------------------------

[Quickstart ---------- See Claude Code in action with practical examples](https://www.anthropic.com/docs/en/quickstart)[Common workflows ---------------- Step-by-step guides for common workflows](https://www.anthropic.com/docs/en/common-workflows)[Troubleshooting --------------- Solutions for common issues with Claude Code](https://www.anthropic.com/docs/en/troubleshooting)[Desktop app ----------- Run Claude Code as a standalone application](https://www.anthropic.com/docs/en/desktop)

[​](https://www.anthropic.com/engineering/claude-code-best-practices#additional-resources)

Additional resources
----------------------------------------------------------------------------------------------------------------

[About Claude Code ----------------- Learn more about Claude Code on claude.com](https://claude.com/product/claude-code)[Build with the Agent SDK ------------------------ Create custom AI agents with the Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)[Host on AWS or GCP ------------------ Configure Claude Code with Amazon Bedrock or Google Vertex AI](https://www.anthropic.com/docs/en/third-party-integrations)[Settings -------- Customize Claude Code for your workflow](https://www.anthropic.com/docs/en/settings)[Commands -------- Learn about CLI commands and controls](https://www.anthropic.com/docs/en/cli-reference)[Reference implementation ------------------------ Clone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)[Security -------- Discover Claude Code’s safeguards and best practices for safe usage](https://www.anthropic.com/docs/en/security)[Privacy and data usage ---------------------- Understand how Claude Code handles your data](https://www.anthropic.com/docs/en/data-usage)

Was this page helpful?

Yes No

[Quickstart](https://www.anthropic.com/docs/en/quickstart)

⌘I

[Claude Code Docs home page![Image 4: light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![Image 5: dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](https://www.anthropic.com/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
