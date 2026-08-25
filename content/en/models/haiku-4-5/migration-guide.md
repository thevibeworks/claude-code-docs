---
title: Migrating to Claude Haiku 4.5
url: https://platform.claude.com/docs/en/models/haiku-4-5/migration-guide
description: "Migrate to Claude Haiku 4.5 from earlier Haiku models: model IDs, breaking changes, and a migration checklist."
---

<Note>
  This guide covers migrating [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) code. If you use [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), no changes beyond updating the model name are required.
</Note>

<Tip>
  **Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

  ```text wrap
  /claude-api migrate this project to claude-opus-5
  ```

  The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.
</Tip>

Claude Haiku 4.5 is the fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality for interactive applications and high-volume processing.

For a complete overview of capabilities, see the [models overview](https://platform.claude.com/docs/en/models/overview).

<Note>
  For Claude Haiku 4.5 pricing, see [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing).
</Note>

<Tip>
  For significant performance improvements on coding and reasoning tasks, consider enabling extended thinking with `thinking: {type: "enabled", budget_tokens: N}`.
</Tip>

<Note>
  Extended thinking impacts [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#caching-with-thinking-blocks) efficiency.

  Extended thinking is deprecated in Claude 4.6 models and removed in Claude Opus 4.7. If using newer models, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) instead.
</Note>

## Migrating to Claude Haiku 4.5 from Claude Haiku 3.5 and earlier Haiku models

**Update your model name:**

```python
# From Haiku 3.5
model = "claude-3-5-haiku-20241022"  # Before
model = "claude-haiku-4-5-20251001"  # After
```

**Review new rate limits:** Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits](https://platform.claude.com/docs/en/api/rate-limits) documentation for details.

**Explore new capabilities:** See the [models overview](https://platform.claude.com/docs/en/models/overview) for details on context awareness, increased output capacity (64k tokens), higher intelligence, and improved speed.

### Breaking changes

These breaking changes apply when migrating from Claude 3.x Haiku models.

1. **Update sampling parameters**

   <Warning>
     This is a breaking change when migrating from Claude 3.x models.
   </Warning>

   Use only `temperature` OR `top_p`, not both. Setting both returns a 400 error on Claude Haiku 4.5.

2. **Update tool versions**

   <Warning>
     This is a breaking change when migrating from Claude 3.x models.
   </Warning>

   Update to the latest tool versions (`text_editor_20250728`, `code_execution_20250825`). Remove any code using the `undo_edit` command.

3. **Handle the `refusal` stop reason**

   Update your application to [handle `refusal` stop reasons](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals).

4. **Update your prompts for behavioral changes**

   Claude 4 models have a more concise, direct communication style. Review [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) for optimization guidance.

### Haiku 4.5 migration checklist

* Update model ID to `claude-haiku-4-5-20251001`
* **BREAKING:** Update tool versions to latest (`text_editor_20250728`, `code_execution_20250825`); legacy versions are not supported
* **BREAKING:** Remove any code using the `undo_edit` command (if applicable)
* **BREAKING:** Update sampling parameters to use only `temperature` OR `top_p`, not both (setting both returns a 400 error)
* Handle new `refusal` stop reason in your application
* Review and adjust for new rate limits (separate from Haiku 3.5)
* Review and update prompts following [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
* Consider enabling extended thinking for complex reasoning tasks
* Test in development environment before production deployment
