# How to create custom skills

Skills are available for users on free, Pro, Max, Team, and Enterprise plans. This feature requires **[code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)**. Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Custom skills let you enhance Claude with specialized knowledge and workflows specific to your organization or personal work style. This article explains how to create, structure, and test your own skills.

Skills can be as simple as a few lines of instructions or as complex as multi-file packages with executable code. The best skills:

- Solve a specific, repeatable task

- Have clear instructions that Claude can follow

- Include examples when helpful

- Define when they should be used

- Are focused on one workflow rather than trying to do everything

---

## Create a skill.md file

Every skill consists of a directory containing at minimum a skill.md file, which is the core of the skill. This file must start with a YAML frontmatter to hold name and description fields, which are required metadata. It can also contain additional metadata, instructions for Claude or reference files, executable scripts, or tools.

### Required metadata fields

**name:** A human-friendly name for your skill (64 characters maximum)

- **Example:** Brand Guidelines

**description:** A clear description of what the skill does and when to use it.

- This is critical—Claude uses this to determine when to invoke your skill (200 characters maximum).

- **Example:** Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.

### Optional metadata fields

**dependencies:** Software packages required by your skill.

- **Example:** python>=3.8, pandas>=1.5.0

The metadata in the skill.md file serves as the first level of a progressive disclosure system, providing just enough information for Claude to know when the skill should be used without having to load all of the content.

### Markdown body

The markdown body is the second level of detail after the metadata, so Claude will access this if needed after reading the metadata. Depending on your task, Claude can access the skill.md file and use the skill.

### Example skill.md

**Brand guidelines skill**

```
## Metadata
name: Brand Guidelines
description: Apply Acme Corp brand guidelines to all presentations and documents

## Overview
This skill provides Acme Corp's official brand guidelines for creating consistent, professional materials. When creating presentations, documents, or marketing materials, apply these standards to ensure all outputs match Acme's visual identity. Claude should reference these guidelines whenever creating external-facing materials or documents that represent Acme Corp.

## Brand Colors

Our official brand colors are:
- Primary: #FF6B35 (Coral)
- Secondary: #004E89 (Navy Blue)
- Accent: #F7B801 (Gold)
- Neutral: #2E2E2E (Charcoal)

## Typography

Headers: Montserrat Bold
Body text: Open Sans Regular
Size guidelines:
- H1: 32pt
- H2: 24pt
- Body: 11pt

## Logo Usage

Always use the full-color logo on light backgrounds. Use the white logo on dark backgrounds. Maintain minimum spacing of 0.5 inches around the logo.

## When to Apply

Apply these guidelines whenever creating:
- PowerPoint presentations
- Word documents for external sharing
- Marketing materials
- Reports for clients

## Resources

See the resources folder for logo files and font downloads.
```

## Add resources

If you have too much information to add to a single skill.md file (e.g., sections that only apply to specific scenarios), you can add more content by adding files within your skill directory. For example, add a REFERENCE.md file containing supplemental and reference information to your skill directory. Referencing it in skill.md will help Claude decide if it needs to access that resource when executing the skill.

## Add scripts

For more advanced skills, attach executable code files to skill.md, allowing Claude to run code. For example, our document skills use the following programming languages and packages:

- Python (pandas, numpy, matplotlib)

- JavaScript/Node.js

- Packages to help with file editing

- Visualization tools

**Note:** Claude and Claude Code can install packages from standard repositories (Python PyPI, JavaScript npm) when loading skills. It’s not possible to install additional packages at runtime with API Skills—all dependencies must be pre-installed in the container.

---

## Package your skill

Once your skill folder is complete:

1. Ensure the folder name matches your skill's name.

2. Create a ZIP file of the folder.

3. The ZIP should contain the skill folder as its root (not a subfolder).

**Correct structure:**

my-skill.zip

└── my-skill/

├── skill.md

└── resources/

**Incorrect structure:**

my-skill.zip

└── (files directly in ZIP root)

---

## Test your skill

### Before uploading

1. Review your skill.md for clarity.

2. Check that the description accurately reflects when Claude should use the skill.

3. Verify all referenced files exist in the correct locations.

4. Test with example prompts to ensure Claude invokes it appropriately.

### After uploading to Claude

1. Enable the skill in **[Customize > Skills](https://claude.ai/customize/skills)**.

2. Try several different prompts that should trigger it.

3. Review Claude's thinking to confirm it's loading the skill.

4. Iterate on the description if Claude isn't using it when expected.

When you're iterating on a skill with Claude in chat, you can edit the skill files directly where they open beside the conversation. Highlight the text you want changed, click "Edit with Claude," and type your request. For skills with multiple files, leave edit requests across the files and send them together, and Claude applies them in one pass. Learn more about **[editing artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them#h_9cbf05e668)**.

**Note for Team and Enterprise plans:** To make a skill available to all users in your organization, see **[Provision and manage skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)**.

---

## Best practices

**Keep it focused:** Create separate skills for different workflows. Multiple focused skills compose better than one large skill.

**Write clear descriptions:** Claude uses descriptions to decide when to invoke your skill. Be specific about when it applies.

**Start simple:** Begin with basic instructions in Markdown before adding complex scripts. You can always expand on the skill later.

**Use examples:** Include example inputs and outputs in your skill.md file to help Claude understand what success looks like.

**Test incrementally:** Test after each significant change rather than building a complex skill all at once.

**Skills can build on each other:** While skills can't explicitly reference other skills, Claude can use multiple skills together automatically. This composability is one of the most powerful parts of the skills feature.

**Review the open Agent Skills specification:** Follow the guidelines at **[agentskills.io](http://agentskills.io)**, so skills you create can work across platforms that adopt the standard.

For a more in-depth guide to skill creation, refer to **[Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)** in our Claude Docs.

---

## Security considerations

- Exercise caution when adding scripts to your skill.md file.

- Don't hardcode sensitive information (API keys, passwords).

- Review any skills you download before enabling them.

- Use appropriate MCP connections for external service access.

---

## Example skills to reference

Visit our repository on GitHub for example skills you can use as templates: **<https://github.com/anthropics/skills/tree/main/skills>**.