# Claude Code model configuration

This guide shows you three ways to change which Claude model you're using with Claude Code: the quick `/model` command for instant changes, the `--model` flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

## Easiest method: Use /model command

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

1. Start Claude Code: `claude`

2. Type `/model` and choose your desired model from the interactive menu.

3. Your model change takes effect immediately.

**Note:** You can check your current model anytime by running `/status` in Claude Code.

## Supported models

- Opus 5, `claude-opus-5`

- Sonnet 5, `claude-sonnet-5`

- Fable 5, `claude-fable-5`

- Opus 4.8, `claude-opus-4-8`

- Opus 4.7, `claude-opus-4-7`

- Sonnet 4.6, `claude-sonnet-4-6`

- Opus 4.6, `claude-opus-4-6`

- Opus 4.5, `claude-opus-4-5-20251101`

- Haiku 4.5, `claude-haiku-4-5-20251001`

- Sonnet 4.5, `claude-sonnet-4-5-20250929`

## Change model for current session only

Use the `--model` flag when starting Claude Code.

1. Start a fresh Terminal session.

2. Enter the following commands (depending on the model you’d like to use for that session):

  - **For Opus 5**: `claude --model claude-opus-5`

  - **For Sonnet 5**: `claude --model claude-sonnet-5`

  - **For Fable 5**: `claude --model claude-fable-5`

  - **For Opus 4.8**: `claude --model claude-opus-4-8`

  - **For Opus 4.7**: `claude --model claude-opus-4-7`

  - **For Sonnet 4.6**:  `claude --model claude-sonnet-4-6`

  - **For Opus 4.6**:  `claude --model claude-opus-4-6`

  - **For Opus 4.5**:  `claude --model claude-opus-4-5-20251101`

  - **For Haiku 4.5:** `claude --model claude-haiku-4-5-20251001`

  - **For Sonnet 4.5**: `claude --model claude-sonnet-4-5-20250929`

## Change default model for all future sessions

**Step 1)** Check your shell type by running: `echo $SHELL`

- `/bin/zsh` → You're using zsh (macOS default)

- `/bin/bash` → You're using bash (Linux default)

**Step 2)** Add model setting to your shell config:

### For ZSH users (macOS)

- Opus 5: `echo 'export ANTHROPIC_MODEL="claude-opus-5"' >> ~/.zshrc`

- Sonnet 5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-5"' >> ~/.zshrc`

- Fable 5: `echo 'export ANTHROPIC_MODEL="claude-fable-5"' >> ~/.zshrc`

- Opus 4.8: `echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.zshrc`

- Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.zshrc`

- Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.zshrc`

- Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.zshrc`

- Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc`

- Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.zshrc`

- Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.zshrc`

### For BASH users (Linux)

- Opus 5: `echo 'export ANTHROPIC_MODEL="claude-opus-5"' >> ~/.bashrc`

- Sonnet 5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-5"' >> ~/.bashrc`

- Fable 5: `echo 'export ANTHROPIC_MODEL="claude-fable-5"' >> ~/.bashrc`

- Opus 4.8: `echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.bashrc`

- Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.bashrc`

- Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.bashrc`

- Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.bashrc`

- Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.bashrc`

- Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.bashrc`

- Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.bashrc`

**Step 3)** Apply the changes:

- For ZSH: `source ~/.zshrc`

- For BASH: `source ~/.bashrc`

**Step 4)** Close Terminal completely, then reopen it.

**Step 5)** Start Claude Code in a fresh Terminal session: `claude`.

Now your chosen model will be the default for all future Claude Code sessions.