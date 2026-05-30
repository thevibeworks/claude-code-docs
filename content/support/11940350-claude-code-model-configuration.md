Title: Claude Code model configuration

URL Source: https://support.claude.com/en/articles/11940350-claude-code-model-configuration

Markdown Content:
# Claude Code model configuration | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Claude Code](https://support.claude.com/en/collections/14445694-claude-code) 
3.   Claude Code model configuration

# Claude Code model configuration

Updated yesterday

Table of contents

[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_368fe15da6)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_17f87abc92)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_7c26153cc9)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_1ca76159fb)

This guide shows you three ways to change which Claude model you're using with Claude Code: the quick `/model` command for instant changes, the `--model` flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

## Easiest method: Use /model command

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

1.   Start Claude Code: `claude` 
2.   Type `/model` and choose your desired model from the interactive menu. 
3.   Your model change takes effect immediately. 

**Note:** You can check your current model anytime by running `/status` in Claude Code.

## Supported models

*   Opus 4.8, `claude-opus-4-8` 
*   Opus 4.7, `claude-opus-4-7` 
*   Sonnet 4.6, `claude-sonnet-4-6` 
*   Opus 4.6, `claude-opus-4-6` 
*   Opus 4.5, `claude-opus-4-5-20251101` 
*   Haiku 4.5, `claude-haiku-4-5-20251001` 
*   Sonnet 4.5, `claude-sonnet-4-5-20250929` 

## Change model for current session only

Use the `--model` flag when starting Claude Code.

1.   Start a fresh Terminal session. 
2.   Enter the following commands (depending on the model you’d like to use for that session): 

    *   **For Opus 4.8**: `claude --model claude-opus-4-8` 
    *   **For Opus 4.7**: `claude --model claude-opus-4-7` 
    *   **For Sonnet 4.6**:`claude --model claude-sonnet-4-6` 
    *   **For Opus 4.6**:`claude --model claude-opus-4-6` 
    *   **For Opus 4.5**:`claude --model claude-opus-4-5-20251101` 
    *   **For Haiku 4.5:**`claude --model claude-haiku-4-5-20251001` 
    *   **For Sonnet 4.5**: `claude --model claude-sonnet-4-5-20250929` 

## Change default model for all future sessions

**Step 1)** Check your shell type by running: `echo $SHELL`

*   `/bin/zsh` → You're using zsh (macOS default) 
*   `/bin/bash` → You're using bash (Linux default) 

**Step 2)** Add model setting to your shell config:

### For ZSH users (macOS)

*   Opus 4.8: `echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.zshrc` 
*   Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.zshrc` 
*   Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.zshrc` 
*   Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.zshrc` 
*   Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc` 
*   Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.zshrc` 
*   Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.zshrc` 

### For BASH users (Linux)

*   Opus 4.8: `echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.bashrc` 
*   Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.bashrc` 
*   Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.bashrc` 
*   Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.bashrc` 
*   Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.bashrc` 
*   Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.bashrc` 
*   Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.bashrc` 

**Step 3)** Apply the changes:

*   For ZSH: `source ~/.zshrc` 
*   For BASH: `source ~/.bashrc` 

**Step 4)** Close Terminal completely, then reopen it.

**Step 5)** Start Claude Code in a fresh Terminal session: `claude`.

Now your chosen model will be the default for all future Claude Code sessions.

* * *

Related Articles

[How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)[How large is the Claude API’s context window?](https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window)[Use Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-use-claude-in-microsoft-foundry)[Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)[Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)

Did this answer your question?

😞😐😃

Table of contents

[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_368fe15da6)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_17f87abc92)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_7c26153cc9)[](https://support.claude.com/en/articles/11940350-claude-code-model-configuration#h_1ca76159fb)

[![Image 2: Claude Help Center](https://downloads.intercomcdn.com/i/o/487548/17213f6a445c8e6e874b1f4b/fad85208982e639d11b9108df895a293.png)](https://support.claude.com/en/)

*   [Product](https://www.anthropic.com/product)
*   [Research](https://www.anthropic.com/research)
*   [Company](https://www.anthropic.com/company)
*   [News](https://www.anthropic.com/news)
*   [Careers](https://www.anthropic.com/careers)

*   [Terms of Service - Consumer](https://www.anthropic.com/terms)
*   [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
*   [Privacy Policy](https://www.anthropic.com/privacy)
*   [Usage Policy](https://www.anthropic.com/aup)
*   [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
*   [Compliance](https://trust.anthropic.com/)
