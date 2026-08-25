> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating custom skills

> Learn how to create, structure, and test your own custom skills

Custom skills extend Claude with specialized knowledge and workflows. This guide explains how to create, structure, and test your own skills.

Skills can range from simple instruction sets to multi-file packages with executable code. Effective skills:

* Solve a specific, repeatable task
* Have clear instructions Claude can follow
* Include examples when helpful
* Define when they should be used
* Focus on one workflow rather than trying to do everything

<Note>
  Skills follow the [Agent Skills specification](https://agentskills.io/specification) — see the specification for more in-depth information.
</Note>

## Directory structure

A skill is a directory containing at minimum a `SKILL.md` file:

```
brand-guidelines/
├── SKILL.md
├── scripts/        # Optional: executable code
├── references/     # Optional: additional documentation
└── assets/         # Optional: templates, images, data files
```

The directory name must match the `name` field in your `SKILL.md`.

## Creating a `SKILL.md` file

The `SKILL.md` file must start with YAML frontmatter containing required metadata, followed by markdown instructions.

### Required fields

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---
```

**name**: Lowercase letters, numbers, and hyphens only. Maximum 64 characters. Must match the directory name.

**description**: Explains what the skill does and when to use it. Claude uses this to determine when to invoke your skill.

<Warning>
  Claude.ai limits descriptions to **200 characters**. The [Agent Skills specification](https://agentskills.io/specification) allows up to 1024 characters, but skills uploaded to Claude.ai must use the shorter limit.
</Warning>

### Markdown body

After the frontmatter, write markdown instructions for Claude. Include:

* Step-by-step procedures
* Examples of inputs and outputs
* Templates or formatting requirements
* Edge cases to handle

Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

### Complete example

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---

# Brand Guidelines

Apply these standards when creating presentations, documents, or marketing materials for Acme Corp.

## Brand colors

- Primary: #FF6B35 (Coral)
- Secondary: #004E89 (Navy Blue)
- Accent: #F7B801 (Gold)
- Neutral: #2E2E2E (Charcoal)

## Typography

- Headers: Montserrat Bold
- Body text: Open Sans Regular
- Size guidelines: H1 32pt, H2 24pt, Body 11pt

## Logo usage

Use the full-color logo on light backgrounds, white logo on dark backgrounds. Maintain minimum spacing of 0.5 inches around the logo.

## When to apply

Apply these guidelines when creating:
- PowerPoint presentations
- Word documents for external sharing
- Marketing materials
- Reports for clients

See the [assets/](assets/) folder for logo files and font downloads.
```

## Adding resources

For content too detailed for `SKILL.md`, add files to your skill directory:

* **`references/`**: Additional documentation Claude can read when needed
* **`assets/`**: Templates, images, lookup tables, schemas
* **`scripts/`**: Executable code (see below)

Reference these files in `SKILL.md` so Claude knows when to load them. Keep files focused—smaller files mean less context usage.

## Adding scripts

Skills can include executable code in Python, JavaScript/Node.js, or Bash. Place scripts in the `scripts/` directory.

Claude can install packages from standard repositories (PyPI, npm) when loading skills. Declare dependencies in your frontmatter:

```markdown SKILL.md theme={null}
---
name: data-analysis
description: Analyze CSV files and generate visualizations.
dependencies: python>=3.8, pandas>=1.5.0, matplotlib
---
```

## Packaging your skill

To upload a skill to Claude:

1. Ensure the directory name matches your skill's `name` field
2. Create a ZIP file containing the skill directory

**Correct structure:**

```
my-skill.zip
└── my-skill/
    ├── SKILL.md
    └── scripts/
```

**Incorrect structure:**

```
my-skill.zip
├── SKILL.md  # files directly in ZIP root
└── scripts/
```

## Testing your skill

### Before uploading

1. Review `SKILL.md` for clarity
2. Verify the description accurately reflects when Claude should use the skill
3. Check that all referenced files exist
4. Validate using `skills-ref validate ./my-skill` ([validation tool](https://github.com/agentskills/agentskills/tree/main/skills-ref))

### After uploading

1. Enable the skill in **Customize > Skills**
2. Try prompts that should trigger it
3. Review Claude's thinking to confirm it's loading the skill
4. Iterate on the description if Claude isn't using it when expected

## Best practices

**Keep it focused**: Create separate skills for different workflows. Multiple focused skills compose better than one large skill.

**Write clear descriptions**: Be specific about when the skill applies. Include keywords that help Claude identify relevant tasks.

**Start simple**: Begin with markdown instructions before adding scripts.

**Use examples**: Include example inputs and outputs to help Claude understand what success looks like.

**Test incrementally**: Test after each significant change.

**Leverage composability**: Claude can use multiple skills together automatically.

## Security considerations

* Don't hardcode sensitive information (API keys, passwords)
* Review any downloaded skills before enabling them
* Use MCP connections for external service access

## Example skills

See [github.com/anthropics/skills](https://github.com/anthropics/skills/tree/main/skills) for example skills you can use as templates.

## Related topics

<Columns cols={2}>
  <Card title="Skills in Claude Code" icon="terminal" href="https://code.claude.com/docs/en/skills">
    Create and test skills from the Claude Code CLI, including the `/skills` manager.
  </Card>

  <Card title="Distribute as a plugin" icon="puzzle-piece" href="/docs/plugins/submit">
    Package your skill for the plugin directory.
  </Card>
</Columns>
