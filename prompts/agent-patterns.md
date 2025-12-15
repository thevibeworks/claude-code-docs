# Agent Patterns

Patterns for building effective AI agents, derived from Anthropic's engineering blog and documentation.

## Sources

| Source | URL |
|--------|-----|
| Building Effective Agents | https://www.anthropic.com/engineering/building-effective-agents |
| Context Engineering | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Writing Tools for Agents | https://www.anthropic.com/engineering/writing-tools-for-agents |
| Agent Skills | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md |
| Tool Use | https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md |

---

## Core Principles

```
1. SIMPLICITY FIRST
   Start with simple prompts. Add complexity only when simpler solutions fail.

2. TRANSPARENCY
   Make agent planning visible. Users should see what the agent is doing.

3. TOOL DESIGN = UX
   Invest as much effort in agent-computer interfaces as human-computer interfaces.
```

---

## Architectural Patterns

### When to Use What

| Pattern | Use When |
|---------|----------|
| **Workflows** | Well-defined tasks needing predictability |
| **Agents** | Open-ended problems, unpredictable steps |

### Workflow Patterns

**1. Prompt Chaining**
Decompose into sequential steps with validation gates.

```
[Task] → [Step 1] → [Validate] → [Step 2] → [Validate] → [Output]
```

**2. Routing**
Classify input → route to specialized handler.

```
[Input] → [Classifier] → [Handler A]
                       → [Handler B]
                       → [Handler C]
```

**3. Parallelization**
Run independent subtasks simultaneously.

```
[Task] → [Subtask A] ─┐
       → [Subtask B] ─┼→ [Aggregate]
       → [Subtask C] ─┘
```

**4. Orchestrator-Workers**
Central LLM dynamically breaks down tasks.

```
[Task] → [Orchestrator] → [Worker 1] ─┐
                        → [Worker 2] ─┼→ [Synthesize]
                        → [Worker N] ─┘
```

**5. Evaluator-Optimizer**
Iterative refinement with evaluation feedback.

```
[Draft] → [Evaluate] → [Refine] → [Evaluate] → ... → [Final]
```

---

## Tool Engineering

### Design Principles

```
1. FORMAT OPTIMIZATION
   Choose formats requiring minimal overhead.
   Avoid unnecessary escaping or line counting.

2. CLEAR DOCUMENTATION
   Include: example usage, edge cases, input requirements, tool boundaries.

3. POKA-YOKE (Error-Proofing)
   Design arguments that prevent misuse.
   Example: require absolute filepaths, not relative.

4. EXTENSIVE TESTING
   Validate tool usage patterns in dev before production.

5. MODEL-CENTRIC DESIGN
   Consider what the model finds intuitive.
   Tools should match how the model "thinks."
```

### Tool Definition Template

```xml
<tool name="example_tool">
  <description>
    One-line purpose. When to use vs when NOT to use.
  </description>

  <parameters>
    <param name="required_arg" type="string" required="true">
      What this is. Format expected. Example value.
    </param>
    <param name="optional_arg" type="integer" required="false" default="10">
      When to change from default.
    </param>
  </parameters>

  <returns>
    What the tool returns. Format. Error cases.
  </returns>

  <examples>
    <example>
      Input: {"required_arg": "foo"}
      Output: {"result": "bar"}
    </example>
  </examples>
</tool>
```

---

## Context Engineering

### System Prompt Design

```
1. RIGHT ALTITUDE
   Balance specificity and flexibility.
   Avoid: hardcoded brittle logic OR vague assumptions.

2. ORGANIZATION
   Structure with XML tags or Markdown headers:
   - Background/role
   - Instructions
   - Tool guidance
   - Output description

3. MINIMALISM
   Start minimal with best model.
   Add instructions based on observed failure modes.
```

### Context Retrieval Strategy

```
1. JUST-IN-TIME
   Maintain lightweight identifiers (paths, URLs, queries).
   Load data dynamically at runtime.

2. PROGRESSIVE DISCLOSURE
   Enable incremental discovery via exploration.
   Use metadata cues: naming, timestamps, folder structure.

3. HYBRID MODEL
   Pre-load critical data.
   Autonomous exploration for the rest.
```

---

## Long-Horizon Task Management

### Compaction
Summarize conversation history approaching context limits.
Preserve critical details, discard redundant outputs.

### Structured Note-Taking
External memory files (NOTES.md, TODO.md) persist across context windows.

```markdown
# NOTES.md
## Session 3 Progress
- Fixed authentication token validation
- Next: investigate user_management test failures
- Do NOT remove tests (could miss bugs)
```

### Sub-Agent Architecture
Specialized agents for focused tasks.
Return condensed summaries (1-2k tokens) to coordinator.

```
[Coordinator] → [Research Agent] → summary
             → [Code Agent]     → summary
             → [Review Agent]   → summary
             → [Final Output]
```

---

## State Tracking (Claude 4.x)

Claude 4.x excels at long-horizon state tracking.

### Best Practices

```
1. STRUCTURED DATA: JSON for test results, task status
   {
     "tests": [{"id": 1, "name": "auth", "status": "passing"}],
     "total": 200, "passing": 150
   }

2. UNSTRUCTURED: freeform text for progress notes
   "Session 3: Fixed auth, next is user_management"

3. GIT FOR STATE: commits as checkpoints, log as history

4. INCREMENTAL FOCUS: few things at a time, steady progress
```

### Multi-Context Window Workflow

```
First window:
  - Set up framework (tests, init scripts)
  - Write tests in structured format (tests.json)
  - Create setup scripts (init.sh)

Subsequent windows:
  - Review progress.txt, tests.json, git logs
  - Run integration test before new features
  - Continue from todo-list
```

---

## Quick Reference

```
+----------------------+------------------------------------------+
| PATTERN              | USE CASE                                 |
+----------------------+------------------------------------------+
| Prompt Chaining      | Sequential steps with validation         |
| Routing              | Input classification to handlers         |
| Parallelization      | Independent subtasks                     |
| Orchestrator-Workers | Dynamic task breakdown                   |
| Evaluator-Optimizer  | Iterative refinement                     |
| Sub-Agents           | Specialized focused tasks                |
+----------------------+------------------------------------------+

GUIDING PRINCIPLE:
"Find the smallest set of high-signal tokens that maximize
 the likelihood of your desired outcome."
```
