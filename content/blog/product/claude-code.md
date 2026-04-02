Title: Claude Code | Anthropic's agentic coding system

URL Source: https://www.anthropic.com/product/claude-code

Markdown Content:
Claude Code is an agentic coding system that reads your codebase, makes changes across files, runs tests, and delivers committed code. For builders without an engineering background, it's an entry point to software development that didn't exist until recently.

## If you can describe it, you can build it

The tools engineers use to build software are now capable of building software themselves. That changes what it means to be an engineer. At Anthropic, the majority of code is now written by [Claude Code](https://claude.com/product/claude-code). Engineers focus on architecture, product thinking, and continuous orchestration: managing multiple agents in parallel, giving direction, and making the decisions that shape what gets built. [Claude Code](https://claude.com/product/claude-code) extends that capability to anyone who can describe what they want to build.

## Common use cases for Claude Code

01

### Navigating unfamiliar code

Deep knowledge of systems and architecture that was previously held by a few engineers becomes accessible to the whole team with Claude Code. It searches codebases, traces dependencies, and helps new members get up to speed on projects in minutes.

02

### Developing across the whole codebase

Claude Code searches directories to build context and understand how modules connect. It creates and edits files across a codebase, taking on ambitious work like building new features or executing multi-file refactors at a scale, saving days of work.

03

### Executing across your toolchain

Developers don't need to memorize commands for git, Kubernetes, or other CLI tools. They describe what they want and Claude Code uses tools like the GitHub CLI natively, running the right commands with the right syntax.

04

### Running tests and managing CI failures

When tests fail, Claude Code reads the errors, fixes the code, and runs the suite again until everything passes. It monitors CI pipelines on GitHub and GitLab and commits fixes automatically.

## Democratizing who builds software

[Claude Code](https://www.anthropic.com/product/claude-code) makes development accessible to anyone with an idea. The ability to describe a goal in plain language and get working software back has opened development to people outside engineering. Founders, product managers, designers, and operations teams are building prototypes, internal tools, and personal projects without auditing code line by line.

## How Claude Code impacts teams

From regulated industries to large-scale codebases, engineering organizations are already changing the way their engineering teams work.

### Broad engineering adoption

**Stripe** deployed Claude Code across 1,370 engineers of all levels through a zero-configuration enterprise binary. One team completed a 10,000-line Scala-to-Java migration in four days, work estimated at ten engineer-weeks.

### Faster incident response

**Ramp** integrated Claude Code into their development workflow and cut incident investigation time by 80%. Non-engineering teams across sales, risk, and finance now query their data warehouse using natural language instead of writing SQL.

### Shorter project timelines

**Wiz** migrated a 50,000-line Python library to Go in roughly 20 hours of active development, a project the team estimated at two to three months of manual work.

### Faster time to market

**Rakuten** reduced the average delivery time for new features from 24 working days to 5. Engineers now run multiple Claude Code sessions in parallel, delegating tasks across the codebase simultaneously.

## Agent safety

Developers control how much autonomy Claude Code has, from approving every action to letting built-in classifiers distinguish safe actions from risky ones automatically. The default is cautious: Claude Code asks before making changes to your files or running commands.

Anthropic’s approach to agent safety, including how we design for trust, access boundaries, and human control, is documented in our research.

[Read our research on agent safety](https://www.anthropic.com/research)

### How is Claude Code different from code completion tools?

Code completion tools suggest the next line or function as a developer types. Claude Code operates at the project level. It reads the full codebase, plans an approach across multiple files, executes changes, runs tests, and iterates on failures. The developer defines the goal and reviews the result rather than guiding each step.

### Who should use Claude Code?

Developers who want to hand off full tasks rather than autocomplete lines of code. But we've also seen product managers, founders, and operations teams start building working tools by describing outcomes in plain language.

### What does "agentic" mean in this context?

An agentic system acts toward a goal with a degree of autonomy, rather than responding to one prompt at a time. Claude Code reads a codebase, plans a sequence of actions, executes them using real development tools, evaluates the result, and adjusts its approach. The developer sets the objective and retains control over what gets committed, but the execution loop runs independently.

### How does Anthropic approach safety for an autonomous coding agent?

Claude Code requires explicit permission before modifying files or running commands. It works within the developer's existing environment and uses their tools rather than operating in an opaque backend. Decisions about what code ships remain with the human. Anthropic's broader research on agent safety, including trust calibration, access boundaries, and oversight mechanisms, informs how Claude Code is designed.
