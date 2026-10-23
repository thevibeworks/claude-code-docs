> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create custom skills

> Create a custom skill for Claude: write the SKILL.md file, add resources and scripts, package the skill, and test it.

A custom skill is a folder with a `SKILL.md` file of instructions, and optionally scripts and reference files, that Claude loads when a task matches the skill's description. This guide is for anyone writing a skill of their own. It explains how to create, structure, and test one.

If you already know what the skill should do, start with the [directory structure](#directory-structure). If you're not sure a skill is the right tool, read [Decide what skill to create](#decide-what-skill-to-create) first.

> [!NOTE]
>
> Skills follow the [Agent Skills specification](https://agentskills.io/specification). See the specification for more in-depth information.

## Decide what skill to create

A skill pays off when Claude does a task for you repeatedly and you want it done the same way every time. Good candidates are tasks where you find yourself correcting Claude with the same instructions, such as a report format your team uses, a review checklist, a multi-step procedure, or work that needs a reference file or a script to come out right. A skill can also teach Claude how your team uses a tool you've connected, such as which project new issues go in and which labels and template to use in your issue tracker. Write the skill once, and Claude applies it whenever a request matches the skill's description, for you and for anyone you share it with.

A skill isn't the right tool for everything:

* **A one-off task**: describe what you want in the conversation instead
* **Live data from another service**: that's what an [MCP connector](https://claude.com/docs/connectors/getting-started.md) provides. A skill can tell Claude how to use a connector, but it can't reach the service itself
* **Instructions for every conversation**: put those in your [personal preferences or project instructions](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) rather than a skill, which loads only when a task matches

To start, write down the task in one sentence and what a good result looks like. That sentence becomes the skill's `description`, and the rest becomes the instructions. If you'd rather have Claude draft the skill with you, ask it to use the [skill-creator skill](#measure-whether-the-skill-improves-the-output), then edit what it produces.

## Directory structure

A skill is a folder named after the skill. The only required file is `SKILL.md`; the other folders are optional and hold material that `SKILL.md` points Claude to. Select a file in the explorer to see what goes in it and what Claude does with it.

What goes in the skill folder

This example skill, `brand-guidelines`, has one of each kind of file a skill can carry. Select a file to read what it's for and see a minimal example.

Skill folder

brand-guidelines/

Selected file

The one required file. Its frontmatter names and describes the skill, and Claude reads the `description` to decide when the skill applies. The body holds the instructions Claude follows once it does.In this example, the skill applies Acme's brand guidelines and tells Claude where the supporting files are:

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---
Use these guidelines whenever you produce a document or deck for Acme.

1. Use the colors and fonts in the sections below.
2. For wording, follow `references/voice-and-tone.md`.
3. For slides, start from `assets/slide-template.md`.
4. Before you finish, run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_contrast.py` on any color pairs you chose.
```

Longer background that Claude reads only when a step calls for it, so it doesn't crowd `SKILL.md`. Mention the file by path at the step where Claude needs it.In this example, the file holds the writing rules the instructions point to in step 2:

```markdown references/voice-and-tone.md theme={null}
# Voice and tone
- Write in the second person and the present tense.
- Prefer short sentences. Avoid exclamation marks.
- Product names are always capitalized: Acme Cloud, Acme Sync.
```

Templates, images, and data files that Claude copies or fills in rather than reads for guidance.In this example, the asset is the slide outline that step 3 tells Claude to start from:

```markdown assets/slide-template.md theme={null}
# [Deck title]
## Agenda
## [Section 1]
## [Section 2]
## Next steps
```

Code that Claude runs while following the skill, for work that is more reliable as a program than as instructions. Reference it from `SKILL.md` with `${CLAUDE_SKILL_DIR}` so the path resolves wherever the skill is installed.In this example, the script checks that a text and background color pair has enough contrast:

```python scripts/check_contrast.py theme={null}
import sys

def luminance(hex_color):
    r, g, b = (int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

fg, bg = sys.argv[1], sys.argv[2]
l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
ratio = (l1 + 0.05) / (l2 + 0.05)
print(f"{ratio:.2f}", "OK" if ratio >= 4.5 else "LOW")
```

As a plain tree, the same skill looks like this. The directory name must match the `name` field in your `SKILL.md`, and everything except `SKILL.md` is optional:

```text theme={null}
brand-guidelines/
├── SKILL.md              # required: frontmatter and instructions
├── references/           # optional: documentation Claude reads when a step calls for it
│   └── voice-and-tone.md
├── assets/               # optional: templates and files Claude copies or fills in
│   └── slide-template.md
└── scripts/              # optional: code Claude runs while following the skill
    └── check_contrast.py
```

## Create a `SKILL.md` file

The `SKILL.md` file must start with YAML frontmatter containing required metadata, followed by markdown instructions.

### Required fields

A `SKILL.md` file starts with YAML frontmatter that names and describes the skill:

```markdown SKILL.md theme={null}
---
name: brand-guidelines
description: Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.
---
```

Both frontmatter fields are required:

| Field | Type | Description |
| :- | :- | :- |
| `name` | string | Lowercase letters, numbers, and hyphens only, up to 64 characters. Must match the skill's directory name |
| `description` | string | What the skill does and when to use it. Claude reads this to decide when to load the skill. Up to 1,024 characters, the limit in the [Agent Skills specification](https://agentskills.io/specification) |

### Write the instructions

After the frontmatter, the rest of the file is the instructions Claude follows when the skill loads, written as ordinary text. You can add headings, lists, and bold with Markdown formatting, the lightweight markup many note-taking apps use, but plain paragraphs work too. Useful things to include:

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

## Add resources

Claude reads all of `SKILL.md` every time the skill loads, so anything long that Claude needs only some of the time is better kept in a separate file that `SKILL.md` points to. Claude then opens that file only when a step calls for it, which keeps the skill quick to load and leaves more of the conversation for your actual task. Separate files also let a skill carry things that aren't instructions at all, such as a template to fill in or a table to look values up in. Put them in folders next to `SKILL.md`:

* **`references/`**: Additional documentation Claude can read when needed
* **`assets/`**: Templates, images, lookup tables, schemas
* **`scripts/`**: Executable code, which [Add scripts](#add-scripts) covers

Mention each file in `SKILL.md` at the step where Claude should use it, for example "Fill in `assets/report-template.md`", so Claude knows when to open it. Keep each file focused on one thing.

## Add scripts

A skill can include scripts that Claude runs while following it, in any language available where the skill runs: in Claude Code that's whatever is installed on your machine, and in chat on claude.ai it's what the code-execution environment provides. Put scripts in a `scripts/` folder inside the skill's own folder, next to `SKILL.md`. In a plugin, that looks like this:

```text theme={null}
my-plugin/
└── skills/
    └── render-chart/
        ├── SKILL.md
        └── scripts/
            └── render.py
```

In `SKILL.md`, write the script's path with `${CLAUDE_SKILL_DIR}`, for example `python3 ${CLAUDE_SKILL_DIR}/scripts/render.py`. Claude Code and Cowork replace `${CLAUDE_SKILL_DIR}` with the skill's folder when the skill loads. It's a placeholder in the skill text, not an environment variable. In chat on claude.ai, the skill's whole folder, scripts included, is copied into the code execution sandbox, so also keep the path readable relative to `SKILL.md`, such as `scripts/render.py`.

In Claude Code, running a script is a Bash tool call, so it needs your permission. When you test with [`claude -p`](https://code.claude.com/docs/en/headless), which can't stop to ask, allow the script on the command line, for example `--allowedTools "Bash(python3 /path/to/my-plugin/skills/render-chart/scripts/render.py *)"`, using the script's absolute path. Claude runs the script by its absolute path, and `Bash()` rules match the whole command line, so a rule that names the exact path approves only that script; a wildcard before the path would approve more than you intend.

Don't put API keys, passwords, or other credentials in a script or anywhere else in the skill: everyone you share the skill with receives its files. When a script needs to reach an outside service, have Claude use a [connector](https://claude.com/docs/connectors/getting-started.md) for that service instead, so each person signs in with their own account.

## Package your skill

You upload a skill to Claude as a ZIP file. The ZIP must contain the skill directory itself as its top level, because Claude looks for `<skill-name>/SKILL.md` inside the archive; a `SKILL.md` sitting at the root of the ZIP isn't recognized as a skill. The packaged file looks like this:

```
my-skill.zip
└── my-skill/
    ├── SKILL.md
    └── scripts/
```

**1. Check the directory name**

Make sure the directory name matches the `name` field in `SKILL.md`.

**2. Zip the directory from its parent folder**

Where the `zip` command is available, such as on macOS and Linux, run it from the folder that contains the skill directory, so the directory becomes the top level of the archive:

```bash theme={null}
zip -r my-skill.zip my-skill/
```

If you use another tool to create the ZIP, compress the skill folder itself rather than the files inside it.

**3. Confirm the structure**

List the archive and check that every entry starts with `my-skill/`:

```bash theme={null}
unzip -l my-skill.zip
```

If `SKILL.md` appears without the `my-skill/` prefix, you zipped the contents instead of the folder; zip again from the parent folder.

To check the skill's contents rather than the archive shape, [validate it before uploading](#before-uploading) with `skills-ref validate` or `claude plugin validate`, or ask Claude to review the folder against the [Agent Skills specification](https://agentskills.io/specification).

## Test your skill

Test the skill's files before you upload it, try it in Claude Code if you have it, confirm that Claude loads it after you upload, and then measure whether it improves Claude's output.

### Before uploading

Before you upload the ZIP, check the skill's files:

**1. Review SKILL.md**

Review `SKILL.md` for clarity.

**2. Check the description**

Verify the description accurately reflects when Claude should use the skill.

**3. Check referenced files**

Check that all referenced files exist.

**4. Validate the skill**

Check the frontmatter against the Agent Skills specification with the [`skills-ref` reference tool](https://github.com/agentskills/agentskills/tree/main/skills-ref). It isn't preinstalled: clone that repository and install it into a Python virtual environment as its README describes, which puts `skills-ref` on your `PATH` while the environment is active. Then, from the folder that contains the skill directory, run:

```bash theme={null}
skills-ref validate ./my-skill
```

A skill that passes prints `Valid skill: ./my-skill`. Otherwise the command lists each problem, such as a `name` that doesn't match the directory or a frontmatter field the specification doesn't define.

If the skill is inside a plugin folder, running `claude plugin validate ./my-plugin` in your terminal also parses each skill's frontmatter: it reports a `SKILL.md` whose frontmatter doesn't parse, and prints `✔ Validation passed` when the plugin passes.

### In Claude Code

If you use [Claude Code](https://code.claude.com/docs/en/overview), you can try the skill from your terminal without uploading it. Copy the skill folder into `~/.claude/skills/`, so the file sits at `~/.claude/skills/my-skill/SKILL.md`, then start `claude` in any project. Describe a task the skill's `description` covers and check that Claude uses it, or type `/my-skill` to run it directly. If Claude doesn't pick the skill up on its own, revise the description. [Extend Claude with skills](https://code.claude.com/docs/en/skills) covers the other places Claude Code loads skills from, including a project's `.claude/skills/` folder and plugins.

### After uploading

After you upload, confirm that Claude loads the skill when it should:

**1. Turn the skill on**

Go to [**Customize > Skills**](https://claude.ai/customize/skills) in claude.ai or the desktop app and turn the skill on.

**2. Try prompts that should trigger it**

Send prompts that should trigger the skill, and review Claude's thinking to confirm it's loading the skill.

**3. Iterate on the description**

Iterate on the description if Claude isn't using it when expected.

### Measure whether the skill improves the output

Trying a few prompts tells you the skill loads, not whether Claude's answers are better with it. To check that, use [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator), a skill from Anthropic that runs your skill on test prompts you agree on, shows you the results, and helps you revise it. On claude.ai, turn it on under [**Customize > Skills**](https://claude.ai/customize/skills), where it's listed as from Anthropic, then ask Claude to evaluate your skill.

`skill-creator` does more in Cowork and Claude Code than in chat:

* **Chat**: `skill-creator` works through the test prompts one at a time and shows you the results in the conversation
* **Cowork and Claude Code**: it also runs the same prompts without the skill as a baseline, runs everything in parallel, and adds pass rates, timing, and token counts so you can compare the two. In Claude Code you install it as a plugin, as [Run evals with skill-creator](https://code.claude.com/docs/en/skills#run-evals-with-skill-creator) describes

If the skill is part of a plugin, you can also test the whole plugin from the Claude Code command line with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals), which grades eval cases you write and compares against a run without the plugin.

## Best practices

Follow these practices when you write a skill:

* **Keep it focused**: create separate skills for different workflows. Several focused skills combine better than one large skill, and Claude can use more than one in a conversation
* **Write a specific description**: say when the skill applies and include the words a request for that task would use. The description is the only part Claude reads before deciding to load the skill
* **Start with instructions**: begin with Markdown instructions and add scripts only when a step needs code
* **Show the output you expect**: include example inputs and outputs so Claude can match them
* **Test after each change**: run the skill on a real request after each significant edit, as [Test your skill](#test-your-skill) describes

For more, the Agent Skills site covers [best practices for skill creation](https://agentskills.io/skill-creation/best-practices) and [writing descriptions that trigger reliably](https://agentskills.io/skill-creation/optimizing-descriptions) in depth.

## Example skills

Anthropic's [skills repository](https://github.com/anthropics/skills/tree/main/skills) has working skills you can read and copy. These four cover the common shapes, from instructions only to instructions with reference files and scripts:

* **[brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)**: a single `SKILL.md` with no scripts or reference files. A good model for a skill that is only instructions, such as a style or formatting rule
* **[internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)**: instructions plus an `examples/` folder of sample documents that `SKILL.md` tells Claude to consult, the pattern from [Add resources](#add-resources)
* **[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)**: instructions, two reference files for less common tasks, and a `scripts/` folder Claude runs to fill forms and extract tables, the pattern from [Add scripts](#add-scripts)
* **[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)**: the skill that helps you write and test other skills, described in [Measure whether the skill improves the output](#measure-whether-the-skill-improves-the-output)

Copy a skill's structure rather than its contents: keep the folder layout and frontmatter, and replace the instructions with your own.

## Share or package your skill

After your skill works, you can give it to other people on its own or as part of a plugin. People you share it with should be able to read what it does, so keep the instructions and scripts plain enough to review.

* **Share or publish one skill**: on Team and Enterprise plans, open the skill from **Customize > Skills** and use the same **Share** and **Publish to org** controls that a plugin has. They work the way [sharing a plugin with specific people](https://claude.com/docs/plugins/share.md#share-a-plugin-with-specific-people) and [publishing a plugin to your organization](https://claude.com/docs/plugins/share.md#publish-a-plugin-to-your-organization) describe
* **Package skills and connectors together**: when you want several skills, or a skill plus the connector it uses, installed together, [build a plugin](https://claude.com/docs/plugins/build.md) that contains them

## Next steps

* [Skills in Claude Code](https://code.claude.com/docs/en/skills): create and test skills from the Claude Code CLI, including the `/skills` manager
* [Plugin structure and testing](https://claude.com/docs/plugins/build.md): package your skill as a plugin so other people can install it
* [Submit your plugin](https://claude.com/docs/plugins/submit.md): submit the plugin to the directory, where Anthropic reviews it before it's listed
