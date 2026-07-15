# Claude Code cheatsheet

This page collects the vocabulary, commands, and keyboard shortcuts that are worth committing to muscle memory. Keep it open in a browser tab (or printed beside your keyboard) during your first few weeks with Claude Code. Most of the friction new users hit comes from not knowing a command already exists for what they are trying to do, so a quick scan here before reaching for a workaround usually pays off.

---

## Glossary

| **Term**                         | **Definition**                                                                                                                                                                                                                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Session**                      | One run of `claude` in a directory, from launch to exit. Each session has its own conversation history, while project memory (`CLAUDE.md`) persists across sessions.                                                                                                              |
| **Context window**               | The total amount of text — your prompts, Claude's replies, and any files it has read — that the model can hold in mind at once. When it fills up, older content is compacted or dropped. It is managed with `/clear` and `/compact`.                                              |
| **Token**                        | The unit models use to measure text (roughly ¾ of a word). Usage limits and API billing are counted in tokens. You will mostly encounter this via `/cost` or the context indicator.                                                                                               |
| **CLAUDE.md**                    | A markdown file (project root, home directory, or subfolder) that Claude reads automatically at the start of every session. It holds your project's conventions, commands, and constraints so you do not have to repeat them.                                                     |
| **Plan mode**                    | A read-only mode in which Claude explores, explains, and proposes but will not edit files or run commands. Use it to review an approach before letting Claude execute. Toggle with **Shift+Tab** or enter directly with `/plan`.                                                  |
| **Accept Edits mode**            | A mode that auto-approves file edits for the rest of the session, while other actions such as shell commands still prompt for approval. It is useful once you trust the direction of the work and no longer want to confirm every diff. Toggle with **Shift+Tab**.                |
| **Permissions**                  | The rules governing which actions Claude can take without asking. By default it asks for everything that touches your machine. You can adjust these per project with `/permissions` or in settings.                                                                               |
| **Tool**                         | A capability Claude can invoke, such as reading a file, editing, running bash, or searching the web. Each tool call appears in the transcript so you can see exactly what happened.                                                                                               |
| **MCP (Model Context Protocol)** | An open standard for plugging external systems — such as GitHub, Jira, databases, or internal APIs — into Claude as tools. If your team has MCP servers configured, Claude can query and act on those systems directly.                                                           |
| **Subagent**                     | A secondary Claude instance that the main session can spawn to handle a focused subtask, such as running tests, searching a large codebase, or reviewing code, in its own context window before reporting back. Subagents are configured via `/agents`.                           |
| **Hook**                         | A shell command that runs automatically at a defined point in Claude's lifecycle, such as before a tool runs, after an edit, or on session start. Hooks are commonly used for auto-formatting, linting, or blocking unsafe commands.                                              |
| **Skill**                        | A packaged set of instructions and helper files that teaches Claude a specific workflow, such as generating a PDF report, scaffolding a component, or following a deploy runbook. Skills are invoked with / like built-in commands and can also load automatically when relevant. |
| **Command**                      | Any input starting with /. Built-in commands control the session (see the table below); custom ones are skills your team defines in `.claude/skills/<name>/SKILL.md` (the legacy `.claude/commands/` path still works).                                                           |

---

## Commands

Type `/` on an empty prompt to see every command available in your setup, including custom, plugin, and MCP-provided ones. The list below covers the built-in defaults (and the bundled skills that ship with every install) you will reach for most often while learning the tool. A few entries vary by platform and plan.

| **Command**          | **What it does**                                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `/help`              | List all available commands.                                                                                   |
| `/init`              | Explore the codebase and generate a starter `CLAUDE.md`.                                                       |
| `/clear`             | Wipe conversation history and start fresh (project memory stays). Aliases: `/reset`, `/new`.                   |
| `/compact`           | Summarize the conversation so far to free up context. Accepts optional focus instructions.                     |
| `/btw`               | Ask a quick side question without adding it to the main conversation or consuming context.                     |
| `/rewind`            | Roll the conversation and/or your code back to an earlier checkpoint.                                          |
| `/model`             | View or switch the active model.                                                                               |
| `/cost`              | Show token usage and spend for this session.                                                                   |
| `/usage`             | Show your plan's usage limits and current rate-limit status.                                                   |
| `/context`           | Visualize what is currently loaded into the context window and where it is being spent.                        |
| `/memory`            | View or edit the `CLAUDE.md` files in scope.                                                                   |
| `/add-dir`           | Grant Claude file access to an additional directory for this session.                                          |
| `/permissions`       | View or change which tools require approval.                                                                   |
| `/config`            | Open configuration settings (theme, defaults, editor mode). Alias: `/settings`.                                |
| `/plan`              | Drop straight into Plan Mode, optionally with a task description.                                              |
| `/diff`              | Open an interactive viewer of uncommitted changes and per-turn diffs.                                          |
| `/copy`              | Copy the last response (or a selected code block) to your clipboard.                                           |
| `/export`            | Save the current conversation to a file or the clipboard.                                                      |
| `/mcp`               | Manage MCP server connections and authentication.                                                              |
| `/agents`            | List, create, or edit subagents.                                                                               |
| `/hooks`             | View hook configuration for tool events.                                                                       |
| `/skills`            | List the skills available in this session.                                                                     |
| `/simplify`          | Bundled skill: review your recently changed files for reuse, quality, and efficiency issues, then apply fixes. |
| `/status`            | Show account, model, working directory, and version.                                                           |
| `/doctor`            | Diagnose install and environment issues.                                                                       |
| `/feedback`          | Report an issue to Anthropic with session context attached. Alias: `/bug`.                                     |
| `/resume`            | Reopen a previous session and continue where you left off. Alias: `/continue`.                                 |
| `/login` / `/logout` | Authenticate, switch accounts, or sign out.                                                                    |
| `/exit`              | Quit the CLI. Alias: `/quit`.                                                                                  |

---

## Keyboard shortcuts

| **Key**         | **Action**                                                                                                                                                              |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + Tab** | Cycle permission mode: `default → acceptEdits → plan`. Also includes auto after running `claude --enable-auto-mode`, and `bypassPermissions` when that mode is enabled. |
| **Esc**         | Interrupt Claude mid-response so you can type again.                                                                                                                    |
| **Esc, Esc**    | Open the rewind/checkpoint menu to roll back to an earlier point in the session.                                                                                        |
| **Ctrl + C**    | Cancel the current input, or exit on an empty prompt.                                                                                                                   |
| **Ctrl + R**    | Reverse search through your prompt history.                                                                                                                             |
| **Ctrl + O**    | Expand to the verbose, full transcript view.                                                                                                                            |
| **↑ / ↓**       | Scroll through your prompt history.                                                                                                                                     |
| **`@` + path**  | Reference a file or directory in your prompt.                                                                                                                           |
| **`/`**         | Open the command menu.                                                                                                                                                  |
| **`?`**         | Show shortcuts for your current terminal or IDE.                                                                                                                        |

Shortcuts vary slightly by terminal and IDE. Press **`?`** inside a session for the exact list in your environment.