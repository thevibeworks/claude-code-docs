# Prompt Optimizer

Meta prompt for analyzing and improving user-written prompts according to Anthropic's official best practices.

## Sources

All techniques derived from official Anthropic documentation:

| Source | URL |
|--------|-----|
| Prompt Engineering Overview | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview.md |
| Prompt Improver | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-improver.md |
| Prompt Generator | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-generator.md |
| Be Clear and Direct | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct.md |
| XML Tags | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags.md |
| Chain of Thought | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought.md |
| System Prompts | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts.md |
| Multishot Prompting | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting.md |
| Prefill Response | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prefill-claudes-response.md |
| Claude 4 Best Practices | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices.md |
| Building Effective Agents | https://www.anthropic.com/engineering/building-effective-agents |
| Context Engineering | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Prompt Library | https://platform.claude.com/docs/en/resources/prompt-library/library.md |
| Interactive Tutorial | https://github.com/anthropics/prompt-eng-interactive-tutorial |

---

## Meta Prompt (Full Version)

```xml
You are an expert prompt engineer. Analyze the user's prompt and improve it according to Anthropic's official best practices.

<best_practices>
1. BE EXPLICIT
   - Tell Claude exactly what you want
   - "Create X" → "Create X with Y, Z features. Go beyond basics."
   - Request "above and beyond" behavior explicitly for Claude 4.x

2. PROVIDE CONTEXT
   - Explain WHY, not just WHAT
   - Bad: "Never use ellipses"
   - Good: "Output feeds TTS engine; ellipses cause pronunciation errors"
   - Context helps Claude generalize correctly

3. USE XML TAGS
   - Structure: <instructions>, <context>, <examples>, <output>
   - Nest hierarchically: <outer><inner></inner></outer>
   - Reference tags: "Using the data in <input> tags..."
   - Consistent naming throughout prompt

4. CHAIN OF THOUGHT
   For complex tasks, instruct stepwise reasoning:
   - Basic: "Think step-by-step"
   - Guided: "First analyze X, then evaluate Y, finally decide Z"
   - Structured: "Reason in <thinking> tags. Answer in <answer> tags."
   - Always output thinking (no output = no thinking)

5. ROLE PROMPTING (System Prompt)
   - Define persona in system parameter
   - Specificity matters: "data scientist" < "senior data scientist at Fortune 500 specializing in customer analytics"
   - Persona changes depth, tone, focus

6. EXAMPLES (Few-Shot)
   - 3-5 diverse, canonical examples
   - Wrap in <example> tags (nested in <examples>)
   - Cover edge cases and variations
   - Quality > quantity; examples are "pictures worth 1000 words"

7. PREFILLING
   Start Claude's response to enforce format:
   - JSON output: prefill with `{`
   - Skip preamble: prefill with direct output start
   - Maintain character: prefill with `[CHARACTER_NAME]`
   - Note: not available with extended thinking

8. OUTPUT CONTROL
   - Tell what TO DO, not what NOT to do
   - Match prompt style to desired output style
   - For minimal markdown: write instructions in plain prose
   - Use XML format indicators: "Write in <prose> tags"
</best_practices>

<claude_4_specific>
Claude 4.x models (Sonnet 4.5, Opus 4.5, Haiku 4.5) have specific behaviors:

- MORE EXPLICIT = BETTER: These models follow instructions precisely. Be specific.
- PROVIDE MOTIVATION: Explain why rules exist; helps Claude generalize.
- ACTION vs SUGGESTION: "Change X" triggers action; "Can you suggest changes?" only suggests.
- PARALLEL TOOLS: State explicitly if independent operations can run simultaneously.
- STATE TRACKING: Use JSON for structured data, freeform text for progress notes.
- WORD SENSITIVITY: Avoid "think" when extended thinking is off; use "consider", "evaluate".
- CONCISE BY DEFAULT: Add "provide detailed updates" if verbose output needed.
</claude_4_specific>

<improvement_pattern>
An improved prompt should include:

1. ROLE (system prompt)
   Clear persona with relevant expertise

2. TASK DEFINITION
   What to do, success criteria, scope

3. STRUCTURED SECTIONS (XML tags)
   - <context> background info
   - <instructions> step-by-step
   - <constraints> limitations/rules
   - <output_format> expected structure

4. REASONING INSTRUCTIONS
   Chain of thought for complex tasks

5. EXAMPLES (if applicable)
   Demonstrate ideal input → output

6. OUTPUT SPECIFICATION
   Format, length, style requirements
</improvement_pattern>

<task>
Analyze the user's prompt. Then produce an improved version.

Steps:
1. Identify weaknesses (vague instructions, missing context, no structure, etc.)
2. Determine which best practices apply
3. Restructure with XML tags where beneficial
4. Add reasoning steps if complexity warrants
5. Specify output format explicitly

Output format:
<analysis>
[Brief assessment: 2-4 bullet points on key issues]
</analysis>

<improved_prompt>
[The optimized prompt, ready to use]
</improved_prompt>

<changes>
[What was changed and why, 2-3 sentences]
</changes>
</task>

<user_prompt>
{{PROMPT_TO_IMPROVE}}
</user_prompt>
```

---

## Meta Prompt (Minimal Version)

For quick optimization without verbose analysis:

```xml
You optimize prompts. Apply these rules:

1. EXPLICIT > vague. Say exactly what you want.
2. CONTEXT: explain WHY, not just WHAT.
3. STRUCTURE: use XML tags <instructions>, <context>, <output>
4. COMPLEX TASKS: add <thinking> for step-by-step reasoning
5. EXAMPLES: 3-5 diverse cases in <example> tags
6. OUTPUT: specify format explicitly; prefill if needed

Input prompt:
<prompt>
{{PROMPT_TO_IMPROVE}}
</prompt>

Output only:
1. Issues (max 3 bullet points, 10 words each)
2. Improved prompt (no commentary)
```

---

## Usage Examples

### Example 1: Vague Task

**Before:**
```
Summarize this article.
```

**After:**
```xml
Your task is to summarize the article below for a busy executive.

<article>
{{ARTICLE}}
</article>

<instructions>
1. Extract the 3 most important points
2. Note any action items or decisions required
3. Flag risks or concerns if present
</instructions>

<output_format>
- Format: bullet points
- Length: max 100 words
- Tone: direct, no fluff
</output_format>
```

### Example 2: Complex Analysis

**Before:**
```
Review this code for issues.
```

**After:**
```xml
You are a senior software engineer conducting a code review.

<code>
{{CODE}}
</code>

<instructions>
1. Identify bugs, security issues, performance problems
2. For each issue: location, severity (high/medium/low), fix suggestion
3. Note positive patterns worth keeping
</instructions>

Think through the code systematically in <analysis> tags before providing your review in <review> tags.

<output_format>
## Issues Found
[table: location | severity | issue | fix]

## Positive Patterns
[brief list]

## Summary
[1-2 sentences: overall assessment]
</output_format>
```

---

## Quick Reference Card

```
+------------------+----------------------------------------+
| TECHNIQUE        | WHEN TO USE                            |
+------------------+----------------------------------------+
| XML tags         | Always (structure helps)               |
| Role prompting   | Domain expertise needed                |
| Chain of thought | Complex reasoning, multi-step          |
| Examples         | Format matters, edge cases exist       |
| Prefilling       | Enforce output format, skip preamble   |
| Context/WHY      | Rules that need generalization         |
+------------------+----------------------------------------+

CLAUDE 4.x QUICK TIPS:
- Be explicit about desired behavior
- Explain motivation behind rules
- "Do X" not "Can you do X?"
- Match prompt style to output style
```

---

## Related Files

- `prompts/prompt-library.md` - Curated prompts from Anthropic
- `prompts/agent-patterns.md` - Patterns for agentic workflows
- `content/en/build-with-claude/prompt-engineering/` - Full docs
