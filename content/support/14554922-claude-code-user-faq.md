# Claude Code user FAQ

Short answers to the questions that come up most at office hours, with a link to go deeper. Organized by where you are in your first few weeks.

## How to use this guide

Five sections follow the arc of a developer’s first weeks: getting started, day-to-day use, leveling up, common gotchas, privacy, and trust. Skim the section that matches where you are, or search for a specific question.

## 1. Getting started

| **Question**                                                    | **Answer**                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.1 How do I install it?**                                    | **macOS/Linux:** `curl -fsSL <https://claude.ai/install.sh> | bash`
​**Windows PowerShell:** `irm <https://claude.ai/install.ps1> | iex`
​**Homebrew:** `brew install --cask claude-code`
​**WinGet:** `winget install Anthropic.ClaudeCode`
Then run `claude` from any repo.<br>
Reference: **[Quickstart](https://code.claude.com/docs/en/quickstart)**                                                     |
| **1.2 Installed, but “claude: command not found”**              | The native installer puts the binary at `~/.local/bin/claude` (Windows: `%USERPROFILE%\.local\bin`). Add that directory to your PATH, e.g. `export PATH="$PATH:$HOME/.local/bin"` in `~/.zshrc` or `~/.bashrc`, then restart your terminal.<br>
Reference: **[Troubleshooting: PATH](https://code.claude.com/docs/en/troubleshooting)**                                                                               |
| **1.3 Login opens a browser on the wrong machine / I’m on SSH** | Press `c` at the login prompt to copy the auth URL. Open it in a local browser, then paste the code back into the terminal.<br>
Reference: **[Troubleshooting: auth](https://code.claude.com/docs/en/troubleshooting)**                                                                                                                                                                                               |
| **1.4 Auth errors right after login, but I have access**        | **400 “organization disabled”:** a stray `ANTHROPIC_API_KEY` env var is overriding your login. Unset it, remove from your shell profile, restart. Run `/status` to confirm which auth is active.
​**403 Forbidden:** your admin hasn’t enabled Claude Code for your workspace yet, or a corporate proxy is interfering.<br>
Reference: **[Troubleshooting: auth](https://code.claude.com/docs/en/troubleshooting)** |
| **1.5 Is Claude Code included in my plan?**                     | Yes. It’s included with Team and Enterprise seats and with Console (API) access. Log in with your work account; SSO is handled automatically. A 403 after login usually means your admin still needs to enable it for the workspace.<br>
Reference: **[Authentication](https://code.claude.com/docs/en/authentication)**                                                                                              |
| **1.6 Claude Code vs. desktop app vs. claude.ai?**              | **Claude Code:** terminal agent that reads your repo, edits files, runs commands.
​**Desktop / claude.ai:** chat interfaces for conversations and one-off questions.
Same model family underneath, different shape of tool.<br>
Reference: **[Overview](https://code.claude.com/docs/en/overview)**                                                                                                               |
| **1.7 Does it work in my IDE?**                                 | Yes. Extensions are available for VS Code and JetBrains IDEs (IntelliJ, PyCharm, etc.). Same features, embedded in the editor instead of a separate terminal.<br>
Reference: **[VS Code](https://code.claude.com/docs/en/vs-code)** · **[JetBrains](https://code.claude.com/docs/en/jetbrains)**                                                                                                                      |
| **1.8 How is this different from Copilot/Cursor autocomplete?** | Autocomplete suggests the next few lines. Claude Code is an agent: give it a task (“fix the failing tests”) and it reads files, runs commands, and makes multi-file edits until done. Less “finish my sentence,” more “here’s a problem, go work it.”<br>
Reference: **[Overview](https://code.claude.com/docs/en/overview)**                                                                                         |
| **1.9 What should I try first?**                                | Point it at a tedious-but-not-hard bug you’ve been putting off. Example: *“the test in [file] is flaky, figure out why.”* Let it read the code instead of you explaining the code.<br>
Reference: **[Common use cases](https://code.claude.com/docs/en/common-workflows)**                                                                                                                                            |
| **1.10 How do I update it?**                                    | Native installs auto-update in the background. To force one now, run `claude update`.
Homebrew/WinGet don’t auto-update: run `brew upgrade claude-code` or `winget upgrade Anthropic.ClaudeCode` periodically.<br>
Reference: **[Setup: updates](https://code.claude.com/docs/en/setup)**                                                                                                                           |

---

## 2. Day-to-day use

| **Question**                                             | **Answer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2.1 It keeps asking permission for the same commands** | Approvals last for the current session by default. To make them persist:
• Pick “always allow” at the prompt
• Add the pattern to `permissions.allow` in `.claude/settings.json`
• Or run `/permissions` to manage interactively<br>
Reference: **[Permissions](https://code.claude.com/docs/en/permissions)**                                                                                                                                                                                                                                                               |
| **2.2 Permission modes and how to switch**               | Press **Shift+Tab** to cycle modes:<br>     **default** · asks before risky edits or commands<br>**acceptEdits** · file edits go through; still asks before running commands<br>**plan** · read-only; proposes a plan and waits for approval<br>**auto** · auto-approves with a background safety check. Requires your org to enable it *and* you to opt in with claude --enable-auto-mode; available only when authenticated against the Anthropic API (not Bedrock, Vertex, or Foundry).<br>
Reference: **[Permission modes](https://code.claude.com/docs/en/permission-modes)** |
| **2.3 What is /init and when do I run it?**              | Run it once, early, in any repo you’ll work in more than once. It scans the project and writes `CLAUDE.md` with build commands, architecture, and conventions. Every future session loads it automatically, so Claude starts with context.<br>
Reference: **[Memory and CLAUDE.md](https://code.claude.com/docs/en/memory)**                                                                                                                                                                                                                                                       |
| **2.4 What goes in CLAUDE.md?**                          | Things tooling can’t enforce that a new teammate would get wrong on day one: “deploy from `release`, not `main`”, “all IDs are strings”, “never call the DB directly from a route handler.” Keep it under two screens; longer gets skimmed.<br>
Reference: **[Memory and CLAUDE.md](https://code.claude.com/docs/en/memory)**                                                                                                                                                                                                                                                      |
| **2.5 Claude isn’t following my CLAUDE.md**              | • Too long or too vague: trim to the rules that actually matter
• Buried in prose: put hard rules near the top, use imperative language (“Never X. Always Y.”)<br>
Reference: **[Best practices](https://code.claude.com/docs/en/best-practices)**                                                                                                                                                                                                                                                                                                                               |
| **2.6 Point it at a specific file without pasting it**   | Type `@` then the path (tab-completes). The mentioned file is read before Claude responds.<br>
Reference: **[Common workflows](https://code.claude.com/docs/en/common-workflows)**                                                                                                                                                                                                                                                                                                                                                                                                 |
| **2.7 Paste a screenshot into the prompt**               | Drag the image into the terminal, or press **Ctrl+V**. On Mac that’s Ctrl, not Cmd (Cmd+V pastes text). Works for error dialogs, UI mockups, whiteboard photos.<br>
Reference: **[Working with images](https://code.claude.com/docs/en/common-workflows#work-with-images)**                                                                                                                                                                                                                                                                                                        |
| **2.8 Copy Claude’s response out of the terminal**       | `/copy` puts the last response on your clipboard. `/export` writes the whole conversation to a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **2.9 Get a previous session back**                      | `claude --continue` resumes the most recent one. `claude --resume` opens a list to pick from. Sessions are stored locally per project directory.<br>
Reference: **[Common workflows: resume](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)**                                                                                                                                                                                                                                                                                                     |
| **2.10 Switch models**                                   | `/model` opens the picker. Set a default in `.claude/settings.json` if you want the same model every session.<br>
Reference: **[Model configuration](https://code.claude.com/docs/en/model-config)**                                                                                                                                                                                                                                                                                                                                                                               |
| **2.11 Extended thinking**                               | On by default. The reasoning itself is hidden in the normal view; press **Ctrl+O** to switch to the verbose transcript if you want to read it. Use `/effort` to dial depth up or down. Worth the extra latency for tricky debugging or architecture calls.<br>
Reference: **[Extended thinking](https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode)**                                                                                                                                                                                            |
| **2.12 Stop it mid-task**                                | Press **Ctrl+C** to cancel the current generation, then tell it what to do instead. No need to start the conversation over.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

---

## 3. Leveling up

| **Question**                                 | **Answer**                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **3.1 What is MCP?**                         | MCP connects Claude Code to your external tools: GitHub, Linear, Slack, your database, your observability stack. One `.mcp.json` config and Claude can read your issues, query your data, and work the same tools you do. Common first connector: your issue tracker.<br>
Reference: **[MCP](https://code.claude.com/docs/en/mcp)**                                                        |
| **3.2 Wire up your first MCP server**        | • Add a `.mcp.json` at the project root, or use `claude mcp add`
• Each entry names a server package plus any env vars (usually an auth token)
• Restart Claude Code and run `/mcp` to confirm it’s connected<br>
Reference: **[MCP setup](https://code.claude.com/docs/en/mcp)**                                                                                                      |
| **3.3 What are hooks for?**                  | Shell scripts that fire on events (before a tool runs, after a file edit, when Claude is waiting on you). Common first hook: a **Notification** hook that pings your desktop when Claude needs input. Same mechanism can run your linter after every edit, post to Slack, or block edits to protected paths.<br>
Reference: **[Hooks guide](https://code.claude.com/docs/en/hooks-guide)** |
| **3.4 Make a reusable prompt / skill**       | Create `.claude/skills/ship/SKILL.md` and the folder name becomes the command: `/ship`. Plain English, no special syntax. Easiest path: ask Claude to write it for you. (The legacy `.claude/commands/ship.md` path still works.)<br>
Reference: **[Skills](https://code.claude.com/docs/en/skills)**                                                                                      |
| **3.5 Skills vs. legacy commands**           | Same mechanism; commands have been merged into skills. `.claude/commands/foo.md` and `.claude/skills/foo/SKILL.md` both create `/foo`. The skill form is preferred and gives you a folder for supporting files (reference docs, templates, helper scripts).<br>
Reference: **[Skills](https://code.claude.com/docs/en/skills)**                                                            |
| **3.6 What are subagents good for?**         | Parallel work: search different parts of the codebase, review a diff along separate dimensions, or generate competing implementations at the same time. The main session aggregates the results.<br>
Reference: **[Subagents](https://code.claude.com/docs/en/sub-agents)**                                                                                                                |
| **3.7 Run non-interactively (CI / scripts)** | `claude -p "your prompt"` runs once and prints the result. Good for CI hooks, pre-commit checks, or piping into other tools. Auth via your logged-in session or `ANTHROPIC_API_KEY`.<br>
Reference: **[Unix-style usage](https://code.claude.com/docs/en/common-workflows)**                                                                                                               |
| **3.8 Undo what it did**                     | `/rewind` rolls back to an earlier checkpoint. Checkpoints are taken automatically at every prompt you send. For anything already committed, use a normal `git revert`.<br>
Reference: **[Checkpointing](https://code.claude.com/docs/en/checkpointing)**                                                                                                                                  |
| **3.9 Share your setup with the team**       | Check `.claude/` into the repo (CLAUDE.md, commands, MCP config). Anyone who clones the repo gets the same setup automatically. Skills can also be packaged as a **plugin** that teams install via `/plugin`.<br>
Reference: **[Plugins](https://code.claude.com/docs/en/plugins)**                                                                                                        |

---

## 4. Common gotchas

| **Question**                                             | **Answer**                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **4.1 Can’t find files / search returns nothing**        | Claude Code ships with a bundled copy of ripgrep, so you do not need to install it. The bundled binary can fail on Alpine/musl systems; in that case install a system copy (`apk add ripgrep`) and set `USE_BUILTIN_RIPGREP=0` so Claude uses it instead.<br>
Reference: **[Troubleshooting: search](https://code.claude.com/docs/en/troubleshooting#search-and-discovery-issues)** |
| **4.2 Copy/paste and scroll broken over SSH or in tmux** | The terminal UI captures mouse events. Hold Shift while selecting to bypass it, or configure tmux to pass mouse events through. `/copy` and `/export` sidestep the issue entirely.                                                                                                                                                                                                    |
| **4.3 Slow on WSL**                                      | Reading Windows files through `/mnt/c/` is a known penalty. Move the repo into the WSL filesystem (`~/` instead of `/mnt/c/...`). The speed difference is dramatic.<br>
Reference: **[Troubleshooting: WSL](https://code.claude.com/docs/en/troubleshooting)**                                                                                                                      |
| **4.4 Image paste isn’t working on Mac**                 | Use **Ctrl+V**, not Cmd+V. Cmd+V pastes text; Ctrl+V is the image-from-clipboard path.                                                                                                                                                                                                                                                                                                |
| **4.5 Wildcard permission rule doesn’t match**           | Build rules incrementally: approve commands interactively first, check what got written to settings, then generalize.<br>
Reference: **[Permissions patterns](https://code.claude.com/docs/en/permissions)**                                                                                                                                                                        |
| **4.6 Non-interactive -p mode behaves differently**      | MCP servers that need OAuth can’t prompt in non-interactive mode<br>Interactive approvals don’t carry over<br>For non-interactive/CI runs, prefer API-key auth and MCP servers configured with env-var tokens.                                                                                                                                                                        |
| **4.7 Ran out of context mid-task**                      | `/compact` summarizes earlier conversation to free up space. `/clear` starts fresh while keeping `CLAUDE.md` and settings loaded. For long tasks, break into steps with a `/clear` between phases.<br>
Reference: **[Managing context](https://code.claude.com/docs/en/common-workflows)**                                                                                          |

---

## 5. Privacy and trust

| **Question**                                                          | **Answer**                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5.1 Does Anthropic train on my code?**                              | No. Under your organization’s Team/Enterprise terms, your code and conversations are not used to train models.<br>
Reference: **[Data usage](https://code.claude.com/docs/en/data-usage)**                                                                                                                                            |
| **5.2 Where does my code actually go?**                               | Claude Code runs on your machine. Source files are read locally, and only the portions needed for the current task are sent to the API to generate a response. Nothing is indexed, uploaded as a whole repo, or used for training.<br>
Reference: **[Data usage](https://code.claude.com/docs/en/data-usage)**                        |
| **5.3 Can anyone else see my conversations?**                         | No. Sessions are stored locally on your machine, per project directory, and are not shared with teammates or visible in any dashboard. Use `/export` if you *want* to share a conversation.<br>
Reference: **[Data usage](https://code.claude.com/docs/en/data-usage)**                                                               |
| **5.4 How do I keep secrets and .env files out of the conversation?** | Claude only reads files it needs for the task; it doesn’t scan your whole repo. To hard-block specific files, add a Read deny rule in `.claude/settings.json` (e.g. `"Read(.env*)"`). Denied files can’t be read even if you accidentally ask for them.<br>
Reference: **[Permissions](https://code.claude.com/docs/en/permissions)** |
| **5.5 What can “acceptEdits” mode do without asking me?**             | File edits go through without a prompt. It still asks before running shell commands, making network calls, or touching anything outside your working directory. For tighter control, stay in default mode.<br>
Reference: **[Permissions](https://code.claude.com/docs/en/permissions)**                                              |

---

## Appendix: Still stuck?

| **Resource**                                  | **What it’s for**                                         |
| --------------------------------------------- | --------------------------------------------------------- |
| `/help`                                       | Built-in command listing what’s available in your session |
| `/feedback`                                   | File an issue from the terminal (alias for `/bug`)        |
| **[Full docs](https://code.claude.com/docs)** | Everything here, in detail                                |
| Your team’s `#claude-code` channel            | Small wins and weird errors both belong there             |

---

## Appendix: Resource directory

| **Page**             | **Link**                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| Quickstart           | **[code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)**           |
| Troubleshooting      | **[code.claude.com/docs/en/troubleshooting](https://code.claude.com/docs/en/troubleshooting)** |
| Permissions          | **[code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)**         |
| Memory and CLAUDE.md | **[code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)**                   |
| MCP                  | **[code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)**                         |
| Data usage           | **[code.claude.com/docs/en/data-usage](https://code.claude.com/docs/en/data-usage)**           |

Claude Code ships frequently. Verify version-specific details against **[code.claude.com/docs](https://code.claude.com/docs)** before distributing internally.