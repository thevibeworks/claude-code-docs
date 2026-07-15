# Use Claude Code CLI with a screen reader

The screen reader mode brings Claude Code back to the basic terminal experience: plain, sequential text with added labels and cues and no visual embellishments. It was built with and for screen reader users, and it's useful to anyone who wants plain output for braille displays, slow connections, or transcripts.

## Turn on the screen reader mode

The screen reader mode requires Claude Code version 2.1.181 or later and it can be enabled in multiple ways:

- For one session: run `claude --ax-screen-reader`

- For every session in a terminal: set the environment variable `CLAUDE_AX_SCREEN_READER=1`

- Permanently: add `"axScreenReader": true` to your Claude Code settings file (`~/.claude/settings.json`)

The first line of the session announces that the screen reader mode is on. In Claude Code v2.1.206 and later it announces: `[Screen Reader Mode: on via flag]` (or `via env` / `via settings`).

## What to expect

- **Your prompts and Claude’s responses are labeled.** Your messages start with `you:` and Claude's replies start with `claude:`. Tool activity starts with `tool:` and permission prompts with `Permission Required:`. The labels are also searchable, so you can use your terminal's search to jump between parts of the conversation.

- **Menus become numbered lists.** Instead of moving a highlight with the arrow keys, you hear each option as a numbered line, then type the number of the option you want and press Enter. For yes-or-no prompts, type `y` or `n` and press Enter.

- **Visual decorations are removed.** Spinners, progress animations, and in-place redraws become plain text that reads in order, and decorative characters such as box-drawing lines are removed.

- **A terminal bell tells you when Claude needs you.** You'll hear your terminal's alert sound when Claude finishes a reply, when a permission prompt appears, and when a long-running tool finishes. If you don't hear it, check the bell setting in your terminal application—some terminals keep the alert sound off by default. Claude Code's own notification channel can be set with `/config` under notifications.

To explore comprehensive documentation regarding line markers, list navigation, and existing constraints, visit the **[Accessibility section of the Claude Code guide](https://code.claude.com/docs/en/accessibility)**.

## Report an issue

​​If something doesn't work with your screen reader or terminal, open an issue at **[the Claude Code GitHub repository](https://github.com/anthropics/claude-code/issues)** and mention your screen reader in the title. Please include your operating system, terminal application, and screen reader name and version.

**Note:** One setting that's easy to mix up: `CLAUDE_CODE_ACCESSIBILITY=1` is a different, unrelated setting—it keeps the terminal cursor visible for screen magnifiers and does not turn on screen reader mode. For a screen reader, use the methods above.