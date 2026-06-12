Title: Your first day in Claude Code

URL Source: https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code

Markdown Content:
**Goal:** In about 15 minutes, you will install Claude Code, sign in, and complete your first AI-assisted change. This guide covers only what is needed on day one; links to deeper material appear at the end.

## Step 1: Install Claude Code (2 minutes)

Pick the command that matches your machine and paste it into a terminal.

Verify the installation:

## Step 2: Sign in (2 minutes)

How you authenticate depends on how your organization has provisioned access. Pick one of the following:

If you are unsure which method applies, check with your administrator or try `/login` first, which is the default for most organizations.

## Step 3: Open a project (1 minute)

Claude Code reads your files on demand, so there is nothing to upload or attach. Simply start it from inside the repository you want to work on.

## Step 4: Understand the one safety rule (1 minute)

Claude will **always ask before changing a file or running a command.** When it proposes a change, you will see a diff and three choices:

You can press **Shift+Tab** at any time to cycle between modes (Plan → Accept Edits → default). If a change produces an unexpected result, your git history remains untouched until you commit, so `git checkout` will undo it.

## Step 5: Five things to try first

Copy and paste these into the prompt one at a time. Each example demonstrates a different core capability.

### 1. Get oriented

_Why this is useful:_ It shows how Claude explores files on its own, without being pointed at specific paths.

### 2. Find something

_Why this is useful:_ It is often faster than `grep` when you do not know the exact symbol or filename.

### 3. Make a safe edit

_Why this is useful:_ It lets you practice reviewing and approving a diff on a low-risk change.

### 4. Fix something real

_Why this is useful:_ This is the primary workflow—you describe the symptom, and Claude investigates and proposes a fix.

### 5. Let it handle git

_Why this is useful:_ Claude can run `git` on your behalf (with approval) and will match your repository's existing commit conventions.

## Step 6: Before you finish for the day

Run this once per project:

This generates a `CLAUDE.md` file at your project root that captures your codebase's conventions. Claude reads it automatically at the start of every session, so future responses will already be tailored to your project. It is the single highest-value setup step you can take.

## Next steps

* * *

Related Articles

[Give Claude context: CLAUDE.md and better prompts](https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts)[Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)[Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)[Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)[Claude Code communications kit](https://support.claude.com/en/articles/14555877-claude-code-communications-kit)
