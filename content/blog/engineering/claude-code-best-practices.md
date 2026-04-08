Title: Best Practices for Claude Code - Claude Code Docs

URL Source: https://www.anthropic.com/engineering/claude-code-best-practices

Markdown Content:
# Best Practices for Claude Code - Claude Code Docs

[Skip to main content](https://www.anthropic.com/engineering/claude-code-best-practices#content-area)

[Claude Code Docs home page![Image 1: light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![Image 2: dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://www.anthropic.com/docs/en/overview)

![Image 3: US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K Ask AI

*   [Claude Developer Platform](https://platform.claude.com/)
*   [Claude Code on the Web](https://claude.ai/code)
*   [Claude Code on the Web](https://claude.ai/code)

Search...

Navigation

Use Claude Code

Best Practices for Claude Code

[Getting started](https://www.anthropic.com/docs/en/overview)[Build with Claude Code](https://www.anthropic.com/docs/en/sub-agents)[Deployment](https://www.anthropic.com/docs/en/third-party-integrations)[Administration](https://www.anthropic.com/docs/en/setup)[Configuration](https://www.anthropic.com/docs/en/settings)[Reference](https://www.anthropic.com/docs/en/cli-reference)[What's New](https://www.anthropic.com/docs/en/whats-new)[Resources](https://www.anthropic.com/docs/en/legal-and-compliance)

##### Getting started

*   [Overview](https://www.anthropic.com/docs/en/overview)
*   [Quickstart](https://www.anthropic.com/docs/en/quickstart)
*   [Changelog](https://www.anthropic.com/docs/en/changelog)

##### Core concepts

*   [How Claude Code works](https://www.anthropic.com/docs/en/how-claude-code-works)
*   [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview)
*   [Explore the .claude directory](https://www.anthropic.com/docs/en/claude-directory)
*   [Explore the context window](https://www.anthropic.com/docs/en/context-window)

##### Use Claude Code

*   [Store instructions and memories](https://www.anthropic.com/docs/en/memory)
*   [Permission modes](https://www.anthropic.com/docs/en/permission-modes)
*   [Common workflows](https://www.anthropic.com/docs/en/common-workflows)
*   [Best practices](https://www.anthropic.com/docs/en/best-practices)

##### Platforms and integrations

*   [Overview](https://www.anthropic.com/docs/en/platforms)
*   [Remote Control](https://www.anthropic.com/docs/en/remote-control)
*   Claude Code on the web 
*   Claude Code on desktop 
*   [Chrome extension (beta)](https://www.anthropic.com/docs/en/chrome)
*   [Computer use (preview)](https://www.anthropic.com/docs/en/computer-use)
*   [Visual Studio Code](https://www.anthropic.com/docs/en/vs-code)
*   [JetBrains IDEs](https://www.anthropic.com/docs/en/jetbrains)
*   Code review & CI/CD 
*   [Claude Code in Slack](https://www.anthropic.com/docs/en/slack)

On this page

*   [Give Claude a way to verify its work](https://www.anthropic.com/engineering/claude-code-best-practices#give-claude-a-way-to-verify-its-work)
*   [Explore first, then plan, then code](https://www.anthropic.com/engineering/claude-code-best-practices#explore-first-then-plan-then-code)
*   [Provide specific context in your prompts](https://www.anthropic.com/engineering/claude-code-best-practices#provide-specific-context-in-your-prompts)
*   [Provide rich content](https://www.anthropic.com/engineering/claude-code-best-practices#provide-rich-content)
*   [Configure your environment](https://www.anthropic.com/engineering/claude-code-best-practices#configure-your-environment)
*   [Write an effective CLAUDE.md](https://www.anthropic.com/engineering/claude-code-best-practices#write-an-effective-claude-md)
*   [Configure permissions](https://www.anthropic.com/engineering/claude-code-best-practices#configure-permissions)
*   [Use CLI tools](https://www.anthropic.com/engineering/claude-code-best-practices#use-cli-tools)
*   [Connect MCP servers](https://www.anthropic.com/engineering/claude-code-best-practices#connect-mcp-servers)
*   [Set up hooks](https://www.anthropic.com/engineering/claude-code-best-practices#set-up-hooks)
*   [Create skills](https://www.anthropic.com/engineering/claude-code-best-practices#create-skills)
*   [Create custom subagents](https://www.anthropic.com/engineering/claude-code-best-practices#create-custom-subagents)
*   [Install plugins](https://www.anthropic.com/engineering/claude-code-best-practices#install-plugins)
*   [Communicate effectively](https://www.anthropic.com/engineering/claude-code-best-practices#communicate-effectively)
*   [Ask codebase questions](https://www.anthropic.com/engineering/claude-code-best-practices#ask-codebase-questions)
*   [Let Claude interview you](https://www.anthropic.com/engineering/claude-code-best-practices#let-claude-interview-you)
*   [Manage your session](https://www.anthropic.com/engineering/claude-code-best-practices#manage-your-session)
*   [Course-correct early and often](https://www.anthropic.com/engineering/claude-code-best-practices#course-correct-early-and-often)
*   [Manage context aggressively](https://www.anthropic.com/engineering/claude-code-best-practices#manage-context-aggressively)
*   [Use subagents for investigation](https://www.anthropic.com/engineering/claude-code-best-practices#use-subagents-for-investigation)
*   [Rewind with checkpoints](https://www.anthropic.com/engineering/claude-code-best-practices#rewind-with-checkpoints)
*   [Resume conversations](https://www.anthropic.com/engineering/claude-code-best-practices#resume-conversations)
*   [Automate and scale](https://www.anthropic.com/engineering/claude-code-best-practices#automate-and-scale)
*   [Run non-interactive mode](https://www.anthropic.com/engineering/claude-code-best-practices#run-non-interactive-mode)
*   [Run multiple Claude sessions](https://www.anthropic.com/engineering/claude-code-best-practices#run-multiple-claude-sessions)
*   [Fan out across files](https://www.anthropic.com/engineering/claude-code-best-practices#fan-out-across-files)
*   [Run autonomously with auto mode](https://www.anthropic.com/engineering/claude-code-best-practices#run-autonomously-with-auto-mode)
*   [Avoid common failure patterns](https://www.anthropic.com/engineering/claude-code-best-practices#avoid-common-failure-patterns)
*   [Develop your intuition](https://www.anthropic.com/engineering/claude-code-best-practices#develop-your-intuition)
*   [Related resources](https://www.anthropic.com/engineering/claude-code-best-practices#related-resources)

Use Claude Code

# Best Practices for Claude Code

Copy page

Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions.

Copy page

Claude Code is an agentic coding environment. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.But this autonomy still comes with a learning curve. Claude works within certain constraints you need to understand.This guide covers patterns that have proven effective across Anthropic’s internal teams and for engineers using Claude Code across various codebases, languages, and environments. For how the agentic loop works under the hood, see [How Claude Code works](https://www.anthropic.com/docs/en/how-claude-code-works).

* * *

Most best practices are based on one constraint: Claude’s context window fills up fast, and performance degrades as it fills.Claude’s context window holds your entire conversation, including every message, every file Claude reads, and every command output. However, this can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens.This matters since LLM performance degrades as context fills. When the context window is getting full, Claude may start “forgetting” earlier instructions or making more mistakes. The context window is the most important resource to manage. To see how a session fills up in practice, [watch an interactive walkthrough](https://www.anthropic.com/docs/en/context-window) of what loads at startup and what each file read costs. Track context usage continuously with a [custom status line](https://www.anthropic.com/docs/en/statusline), and see [Reduce token usage](https://www.anthropic.com/docs/en/costs#reduce-token-usage) for strategies on reducing token usage.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#give-claude-a-way-to-verify-its-work)

Give Claude a way to verify its work

Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do.

Claude performs dramatically better when it can verify its own work, like run tests, compare screenshots, and validate outputs.Without clear success criteria, it might produce something that looks right but actually doesn’t work. You become the only feedback loop, and every mistake requires your attention.

| Strategy | Before | After |
| --- | --- | --- |
| **Provide verification criteria** | _”implement a function that validates email addresses"_ | _"write a validateEmail function. example test cases: [[email protected]](https://www.anthropic.com/cdn-cgi/l/email-protection#3f4a4c5a4d7f5a475e524f535a115c5052) is true, invalid is false, [[email protected]](https://www.anthropic.com/cdn-cgi/l/email-protection#2b5e584e596b05484446) is false. run the tests after implementing”_ |
| **Verify UI changes visually** | _”make the dashboard look better"_ | _"[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them”_ |
| **Address root causes, not symptoms** | _”the build is failing"_ | _"the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don’t suppress the error”_ |

UI changes can be verified using the [Claude in Chrome extension](https://www.anthropic.com/docs/en/chrome). It opens new tabs in your browser, tests the UI, and iterates until the code works.Your verification can also be a test suite, a linter, or a Bash command that checks output. Invest in making your verification rock-solid.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#explore-first-then-plan-then-code)

Explore first, then plan, then code

Separate research and planning from implementation to avoid solving the wrong problem.

Letting Claude jump straight to coding can produce code that solves the wrong problem. Use [Plan Mode](https://www.anthropic.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis) to separate exploration from execution.The recommended workflow has four phases:

1

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Explore

Enter Plan Mode. Claude reads files and answers questions without making changes.

claude (Plan Mode)

```
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.
```

2

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Plan

Ask Claude to create a detailed implementation plan.

claude (Plan Mode)

```
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.
```

Press `Ctrl+G` to open the plan in your text editor for direct editing before Claude proceeds.

3

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Implement

Switch back to Normal Mode and let Claude code, verifying against its plan.

claude (Normal Mode)

```
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.
```

4

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Commit

Ask Claude to commit with a descriptive message and create a PR.

claude (Normal Mode)

```
commit with a descriptive message and open a PR
```

Plan Mode is useful, but also adds overhead.For tasks where the scope is clear and the fix is small (like fixing a typo, adding a log line, or renaming a variable) ask Claude to do it directly.Planning is most useful when you’re uncertain about the approach, when the change modifies multiple files, or when you’re unfamiliar with the code being modified. If you could describe the diff in one sentence, skip the plan.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#provide-specific-context-in-your-prompts)

Provide specific context in your prompts

The more precise your instructions, the fewer corrections you’ll need.

Claude can infer intent, but it can’t read your mind. Reference specific files, mention constraints, and point to example patterns.

| Strategy | Before | After |
| --- | --- | --- |
| **Scope the task.** Specify which file, what scenario, and testing preferences. | _”add tests for foo.py"_ | _"write a test for foo.py covering the edge case where the user is logged out. avoid mocks.”_ |
| **Point to sources.** Direct Claude to the source that can answer a question. | _”why does ExecutionFactory have such a weird api?"_ | _"look through ExecutionFactory’s git history and summarize how its api came to be”_ |
| **Reference existing patterns.** Point Claude to patterns in your codebase. | _”add a calendar widget"_ | _"look at how existing widgets are implemented on the home page to understand the patterns. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards to pick a year. build from scratch without libraries other than the ones already used in the codebase.”_ |
| **Describe the symptom.** Provide the symptom, the likely location, and what “fixed” looks like. | _”fix the login bug"_ | _"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it”_ |

Vague prompts can be useful when you’re exploring and can afford to course-correct. A prompt like `"what would you improve in this file?"` can surface things you wouldn’t have thought to ask about.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#provide-rich-content)

Provide rich content

Use `@` to reference files, paste screenshots/images, or pipe data directly.

You can provide rich data to Claude in several ways:
*   **Reference files with `@`** instead of describing where code lives. Claude reads the file before responding.
*   **Paste images directly**. Copy/paste or drag and drop images into the prompt.
*   **Give URLs** for documentation and API references. Use `/permissions` to allowlist frequently-used domains.
*   **Pipe in data** by running `cat error.log | claude` to send file contents directly.
*   **Let Claude fetch what it needs**. Tell Claude to pull context itself using Bash commands, MCP tools, or by reading files.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#configure-your-environment)

Configure your environment

A few setup steps make Claude Code significantly more effective across all your sessions. For a full overview of extension features and when to use each one, see [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview).
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#write-an-effective-claude-md)

Write an effective CLAUDE.md

Run `/init` to generate a starter CLAUDE.md file based on your current project structure, then refine over time.

CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can’t infer from code alone.The `/init` command analyzes your codebase to detect build systems, test frameworks, and code patterns, giving you a solid foundation to refine.There’s no required format for CLAUDE.md files, but keep it short and human-readable. For example:

CLAUDE.md

```
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use [skills](https://www.anthropic.com/docs/en/skills) instead. Claude loads them on demand without bloating every conversation.Keep it concise. For each line, ask: _“Would removing this cause Claude to make mistakes?”_ If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!

| ✅ Include | ❌ Exclude |
| --- | --- |
| Bash commands Claude can’t guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like “write clean code” |

If Claude keeps doing something you don’t want despite having a rule against it, the file is probably too long and the rule is getting lost. If Claude asks you questions that are answered in CLAUDE.md, the phrasing might be ambiguous. Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude’s behavior actually shifts.You can tune instructions by adding emphasis (e.g., “IMPORTANT” or “YOU MUST”) to improve adherence. Check CLAUDE.md into git so your team can contribute. The file compounds in value over time.CLAUDE.md files can import additional files using `@path/to/import` syntax:

CLAUDE.md

```
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

You can place CLAUDE.md files in several locations:
*   **Home folder (`~/.claude/CLAUDE.md`)**: applies to all Claude sessions
*   **Project root (`./CLAUDE.md`)**: check into git to share with your team
*   **Project root (`./CLAUDE.local.md`)**: personal project-specific notes; add this file to your `.gitignore` so it isn’t shared with your team
*   **Parent directories**: useful for monorepos where both `root/CLAUDE.md` and `root/foo/CLAUDE.md` are pulled in automatically
*   **Child directories**: Claude pulls in child CLAUDE.md files on demand when working with files in those directories

### [​](https://www.anthropic.com/engineering/claude-code-best-practices#configure-permissions)

Configure permissions

Use [auto mode](https://www.anthropic.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) to let a classifier handle approvals, `/permissions` to allowlist specific commands, or `/sandbox` for OS-level isolation. Each reduces interruptions while keeping you in control.

By default, Claude Code requests permission for actions that might modify your system: file writes, Bash commands, MCP tools, etc. This is safe but tedious. After the tenth approval you’re not really reviewing anymore, you’re just clicking through. There are three ways to reduce these interruptions:
*   **Auto mode**: a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions. Best when you trust the general direction of a task but don’t want to click through every step
*   **Permission allowlists**: permit specific tools you know are safe, like `npm run lint` or `git commit`
*   **Sandboxing**: enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries

Read more about [permission modes](https://www.anthropic.com/docs/en/permission-modes), [permission rules](https://www.anthropic.com/docs/en/permissions), and [sandboxing](https://www.anthropic.com/docs/en/sandboxing).
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#use-cli-tools)

Use CLI tools

Tell Claude Code to use CLI tools like `gh`, `aws`, `gcloud`, and `sentry-cli` when interacting with external services.

CLI tools are the most context-efficient way to interact with external services. If you use GitHub, install the `gh` CLI. Claude knows how to use it for creating issues, opening pull requests, and reading comments. Without `gh`, Claude can still use the GitHub API, but unauthenticated requests often hit rate limits.Claude is also effective at learning CLI tools it doesn’t already know. Try prompts like `Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#connect-mcp-servers)

Connect MCP servers

Run `claude mcp add` to connect external tools like Notion, Figma, or your database.

With [MCP servers](https://www.anthropic.com/docs/en/mcp), you can ask Claude to implement features from issue trackers, query databases, analyze monitoring data, integrate designs from Figma, and automate workflows.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#set-up-hooks)

Set up hooks

Use hooks for actions that must happen every time with zero exceptions.

[Hooks](https://www.anthropic.com/docs/en/hooks-guide) run scripts automatically at specific points in Claude’s workflow. Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.Claude can write hooks for you. Try prompts like _“Write a hook that runs eslint after every file edit”_ or _“Write a hook that blocks writes to the migrations folder.”_ Edit `.claude/settings.json` directly to configure hooks by hand, and run `/hooks` to browse what’s configured.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#create-skills)

Create skills

Create `SKILL.md` files in `.claude/skills/` to give Claude domain knowledge and reusable workflows.

[Skills](https://www.anthropic.com/docs/en/skills) extend Claude’s knowledge with information specific to your project, team, or domain. Claude applies them automatically when relevant, or you can invoke them directly with `/skill-name`.Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`:

.claude/skills/api-conventions/SKILL.md

```
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

Skills can also define repeatable workflows you invoke directly:

.claude/skills/fix-issue/SKILL.md

```
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

Run `/fix-issue 1234` to invoke it. Use `disable-model-invocation: true` for workflows with side effects that you want to trigger manually.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#create-custom-subagents)

Create custom subagents

Define specialized assistants in `.claude/agents/` that Claude can delegate to for isolated tasks.

[Subagents](https://www.anthropic.com/docs/en/sub-agents) run in their own context with their own set of allowed tools. They’re useful for tasks that read many files or need specialized focus without cluttering your main conversation.

.claude/agents/security-reviewer.md

```
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

Tell Claude to use subagents explicitly: _“Use a subagent to review this code for security issues.”_
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#install-plugins)

Install plugins

Run `/plugin` to browse the marketplace. Plugins add skills, tools, and integrations without configuration.

[Plugins](https://www.anthropic.com/docs/en/plugins) bundle skills, hooks, subagents, and MCP servers into a single installable unit from the community and Anthropic. If you work with a typed language, install a [code intelligence plugin](https://www.anthropic.com/docs/en/discover-plugins#code-intelligence) to give Claude precise symbol navigation and automatic error detection after edits.For guidance on choosing between skills, subagents, hooks, and MCP, see [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview#match-features-to-your-goal).

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#communicate-effectively)

Communicate effectively

The way you communicate with Claude Code significantly impacts the quality of results.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#ask-codebase-questions)

Ask codebase questions

Ask Claude questions you’d ask a senior engineer.

When onboarding to a new codebase, use Claude Code for learning and exploration. You can ask Claude the same sorts of questions you would ask another engineer:
*   How does logging work?
*   How do I make a new API endpoint?
*   What does `async move { ... }` do on line 134 of `foo.rs`?
*   What edge cases does `CustomerOnboardingFlowImpl` handle?
*   Why does this code call `foo()` instead of `bar()` on line 333?

Using Claude Code this way is an effective onboarding workflow, improving ramp-up time and reducing load on other engineers. No special prompting required: ask questions directly.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#let-claude-interview-you)

Let Claude interview you

For larger features, have Claude interview you first. Start with a minimal prompt and ask Claude to interview you using the `AskUserQuestion` tool.

Claude asks about things you might not have considered yet, including technical implementation, UI/UX, edge cases, and tradeoffs.

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

Once the spec is complete, start a fresh session to execute it. The new session has clean context focused entirely on implementation, and you have a written spec to reference.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#manage-your-session)

Manage your session

Conversations are persistent and reversible. Use this to your advantage!
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#course-correct-early-and-often)

Course-correct early and often

Correct Claude as soon as you notice it going off track.

The best results come from tight feedback loops. Though Claude occasionally solves problems perfectly on the first attempt, correcting it quickly generally produces better solutions faster.
*   **`Esc`**: stop Claude mid-action with the `Esc` key. Context is preserved, so you can redirect.
*   **`Esc + Esc` or `/rewind`**: press `Esc` twice or run `/rewind` to open the rewind menu and restore previous conversation and code state, or summarize from a selected message.
*   **`"Undo that"`**: have Claude revert its changes.
*   **`/clear`**: reset context between unrelated tasks. Long sessions with irrelevant context can reduce performance.

If you’ve corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned. A clean session with a better prompt almost always outperforms a long session with accumulated corrections.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#manage-context-aggressively)

Manage context aggressively

Run `/clear` between unrelated tasks to reset context.

Claude Code automatically compacts conversation history when you approach context limits, which preserves important code and decisions while freeing space.During long sessions, Claude’s context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude.
*   Use `/clear` frequently between tasks to reset the context window entirely
*   When auto compaction triggers, Claude summarizes what matters most, including code patterns, file states, and key decisions
*   For more control, run `/compact <instructions>`, like `/compact Focus on the API changes`
*   To compact only part of the conversation, use `Esc + Esc` or `/rewind`, select a message checkpoint, and choose **Summarize from here**. This condenses messages from that point forward while keeping earlier context intact.
*   Customize compaction behavior in CLAUDE.md with instructions like `"When compacting, always preserve the full list of modified files and any test commands"` to ensure critical context survives summarization
*   For quick questions that don’t need to stay in context, use [`/btw`](https://www.anthropic.com/docs/en/interactive-mode#side-questions-with-btw). The answer appears in a dismissible overlay and never enters conversation history, so you can check a detail without growing context.

### [​](https://www.anthropic.com/engineering/claude-code-best-practices#use-subagents-for-investigation)

Use subagents for investigation

Delegate research with `"use subagents to investigate X"`. They explore in a separate context, keeping your main conversation clean for implementation.

Since context is your fundamental constraint, subagents are one of the most powerful tools available. When Claude researches a codebase it reads lots of files, all of which consume your context. Subagents run in separate context windows and report back summaries:

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

The subagent explores the codebase, reads relevant files, and reports back with findings, all without cluttering your main conversation.You can also use subagents for verification after Claude implements something:

```
use a subagent to review this code for edge cases
```

### [​](https://www.anthropic.com/engineering/claude-code-best-practices#rewind-with-checkpoints)

Rewind with checkpoints

Every action Claude makes creates a checkpoint. You can restore conversation, code, or both to any previous checkpoint.

Claude automatically checkpoints before changes. Double-tap `Escape` or run `/rewind` to open the rewind menu. You can restore conversation only, restore code only, restore both, or summarize from a selected message. See [Checkpointing](https://www.anthropic.com/docs/en/checkpointing) for details.Instead of carefully planning every move, you can tell Claude to try something risky. If it doesn’t work, rewind and try a different approach. Checkpoints persist across sessions, so you can close your terminal and still rewind later.

Checkpoints only track changes made _by Claude_, not external processes. This isn’t a replacement for git.

### [​](https://www.anthropic.com/engineering/claude-code-best-practices#resume-conversations)

Resume conversations

Run `claude --continue` to pick up where you left off, or `--resume` to choose from recent sessions.

Claude Code saves conversations locally. When a task spans multiple sessions, you don’t have to re-explain the context:

```
claude --continue    # Resume the most recent conversation
claude --resume      # Select from recent conversations
```

Use `/rename` to give sessions descriptive names like `"oauth-migration"` or `"debugging-memory-leak"` so you can find them later. Treat sessions like branches: different workstreams can have separate, persistent contexts.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#automate-and-scale)

Automate and scale

Once you’re effective with one Claude, multiply your output with parallel sessions, non-interactive mode, and fan-out patterns.Everything so far assumes one human, one Claude, and one conversation. But Claude Code scales horizontally. The techniques in this section show how you can get more done.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#run-non-interactive-mode)

Run non-interactive mode

Use `claude -p "prompt"` in CI, pre-commit hooks, or scripts. Add `--output-format stream-json` for streaming JSON output.

With `claude -p "your prompt"`, you can run Claude non-interactively, without a session. Non-interactive mode is how you integrate Claude into CI pipelines, pre-commit hooks, or any automated workflow. The output formats let you parse results programmatically: plain text, JSON, or streaming JSON.

```
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json
```

### [​](https://www.anthropic.com/engineering/claude-code-best-practices#run-multiple-claude-sessions)

Run multiple Claude sessions

Run multiple Claude sessions in parallel to speed up development, run isolated experiments, or start complex workflows.

There are three main ways to run parallel sessions:
*   [Claude Code desktop app](https://www.anthropic.com/docs/en/desktop#work-in-parallel-with-sessions): Manage multiple local sessions visually. Each session gets its own isolated worktree.
*   [Claude Code on the web](https://www.anthropic.com/docs/en/claude-code-on-the-web): Run on Anthropic’s secure cloud infrastructure in isolated VMs.
*   [Agent teams](https://www.anthropic.com/docs/en/agent-teams): Automated coordination of multiple sessions with shared tasks, messaging, and a team lead.

Beyond parallelizing work, multiple sessions enable quality-focused workflows. A fresh context improves code review since Claude won’t be biased toward code it just wrote.For example, use a Writer/Reviewer pattern:

| Session A (Writer) | Session B (Reviewer) |
| --- | --- |
| `Implement a rate limiter for our API endpoints` |  |
|  | `Review the rate limiter implementation in @src/middleware/rateLimiter.ts. Look for edge cases, race conditions, and consistency with our existing middleware patterns.` |
| `Here's the review feedback: [Session B output]. Address these issues.` |  |

You can do something similar with tests: have one Claude write tests, then another write code to pass them.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#fan-out-across-files)

Fan out across files

Loop through tasks calling `claude -p` for each. Use `--allowedTools` to scope permissions for batch operations.

For large migrations or analyses, you can distribute work across many parallel Claude invocations:

1

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Generate a task list

Have Claude list all files that need migrating (e.g., `list all 2,000 Python files that need migrating`)

2

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Write a script to loop through the list

```
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

3

[](https://www.anthropic.com/engineering/claude-code-best-practices#)

Test on a few files, then run at scale

Refine your prompt based on what goes wrong with the first 2-3 files, then run on the full set. The `--allowedTools` flag restricts what Claude can do, which matters when you’re running unattended.

You can also integrate Claude into existing data/processing pipelines:

```
claude -p "<your prompt>" --output-format json | your_command
```

Use `--verbose` for debugging during development, and turn it off in production.
### [​](https://www.anthropic.com/engineering/claude-code-best-practices#run-autonomously-with-auto-mode)

Run autonomously with auto mode

For uninterrupted execution with background safety checks, use [auto mode](https://www.anthropic.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). A classifier model reviews commands before they run, blocking scope escalation, unknown infrastructure, and hostile-content-driven actions while letting routine work proceed without prompts.

```
claude --permission-mode auto -p "fix all lint errors"
```

For non-interactive runs with the `-p` flag, auto mode aborts if the classifier repeatedly blocks actions, since there is no user to fall back to. See [when auto mode falls back](https://www.anthropic.com/docs/en/permission-modes#when-auto-mode-falls-back) for thresholds.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#avoid-common-failure-patterns)

Avoid common failure patterns

These are common mistakes. Recognizing them early saves time:
*   **The kitchen sink session.** You start with one task, then ask Claude something unrelated, then go back to the first task. Context is full of irrelevant information.
> **Fix**: `/clear` between unrelated tasks.

*   **Correcting over and over.** Claude does something wrong, you correct it, it’s still wrong, you correct again. Context is polluted with failed approaches.
> **Fix**: After two failed corrections, `/clear` and write a better initial prompt incorporating what you learned.

*   **The over-specified CLAUDE.md.** If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise.
> **Fix**: Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.

*   **The trust-then-verify gap.** Claude produces a plausible-looking implementation that doesn’t handle edge cases.
> **Fix**: Always provide verification (tests, scripts, screenshots). If you can’t verify it, don’t ship it.

*   **The infinite exploration.** You ask Claude to “investigate” something without scoping it. Claude reads hundreds of files, filling the context.
> **Fix**: Scope investigations narrowly or use subagents so the exploration doesn’t consume your main context.

* * *

## [​](https://www.anthropic.com/engineering/claude-code-best-practices#develop-your-intuition)

Develop your intuition

The patterns in this guide aren’t set in stone. They’re starting points that work well in general, but might not be optimal for every situation.Sometimes you _should_ let context accumulate because you’re deep in one complex problem and the history is valuable. Sometimes you should skip planning and let Claude figure it out because the task is exploratory. Sometimes a vague prompt is exactly right because you want to see how Claude interprets the problem before constraining it.Pay attention to what works. When Claude produces great output, notice what you did: the prompt structure, the context you provided, the mode you were in. When Claude struggles, ask why. Was the context too noisy? The prompt too vague? The task too big for one pass?Over time, you’ll develop intuition that no guide can capture. You’ll know when to be specific and when to be open-ended, when to plan and when to explore, when to clear context and when to let it accumulate.
## [​](https://www.anthropic.com/engineering/claude-code-best-practices#related-resources)

Related resources

*   [How Claude Code works](https://www.anthropic.com/docs/en/how-claude-code-works): the agentic loop, tools, and context management
*   [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview): skills, hooks, MCP, subagents, and plugins
*   [Common workflows](https://www.anthropic.com/docs/en/common-workflows): step-by-step recipes for debugging, testing, PRs, and more
*   [CLAUDE.md](https://www.anthropic.com/docs/en/memory): store project conventions and persistent context

Was this page helpful?

Yes No

[Common workflows](https://www.anthropic.com/docs/en/common-workflows)[Overview](https://www.anthropic.com/docs/en/platforms)

⌘I

[Claude Code Docs home page![Image 4: light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![Image 5: dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://www.anthropic.com/docs/en/overview)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy choices](https://www.anthropic.com/engineering/claude-code-best-practices#)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
