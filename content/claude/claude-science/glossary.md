> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> One-sentence definitions for the terms you meet in Claude Science, from artifact to workspace.

One-sentence definitions for the terms you meet in Claude Science, from artifact to workspace.

**[Artifact](/docs/claude-science/artifacts)**: any file Claude makes and saves for you, listed in its session's Files view.

**Cell**: one block of code Claude runs in a kernel; the cell, its output, and the environment it ran in are recorded in the session's Notebook.

**Cloud provider**: your own account at a cloud service where Claude can start jobs; you pay that provider directly.

**[Comment](/docs/claude-science/comments)**: a note you pin to part of an artifact by selecting it; Claude reads pending comments as instructions on its next turn.

**Connector**: an outside data source or tool wired into Claude over MCP; Claude Science includes a featured set, you can access partner connectors from the Connectors Directory, and you can add your own under Settings > Connectors.

**Data directory**: the `~/.claude-science` folder on your computer holding the database, artifacts, session workspaces, and logs.

**[Environment](/docs/claude-science/tools-and-environments)**: a named set of installed packages (conda) that a kernel runs in, reused across sessions.

**Execution log**: the slice of a session's Notebook cells that produced a given artifact version, shown as a tab in its Provenance pane.

**Kernel**: the live Python or R process that runs a session's cells and keeps variables in memory between them.

**Memory**: notes Claude keeps about you and your projects across sessions, which you can review and edit.

**Model endpoint**: a scientific domain-specific model server you register under Settings > Compute, that runs locally or connects to a vendor's hosted solution, that Claude sends single prediction requests to.

**Network allowlist**: the list of every outside host that sandboxed code may reach, kept under Settings or, on Team and Enterprise plans, managed by your organization.

**Permission card**: the card that replaces the message box when Claude needs your permission for running code, running a job, accessing a network host, a folder, a connector tool, or re-configuring Claude Science; you allow or deny it.

**Provenance (the artifact record)**: the panel behind every artifact version showing the code, cells, conversation, environment, and findings that produced it.

**[Reviewer](/docs/claude-science/the-reviewer)**: the independent agent that re-examines Claude's claims and artifacts at checkpoints, recording each issue it raises as a finding on the artifact's Review tab; on some plans it runs in the background automatically.

**Sandbox**: the isolated environment all of Claude's code runs in; reaching outside it needs your approval.

**Scope**: how long an approval lasts (Once, This conversation, This project, or Global), with every standing grant listed and revocable under Settings > Permissions.

**Session**: one conversation thread inside a project, with its own kernel and workspace.

**Skill**: an installable package of instructions and helper code that teaches Claude a method or tool.

**Specialist**: a named set of skills, connectors, and instructions that a session answers as.

**SSH host**: a remote machine (server, cluster node, or a job submission host) added by its SSH name, that Claude can run jobs on, or dispatch jobs from.

**Version**: one immutable save of an artifact; saving again adds a new version on top instead of overwriting.

**Workspace**: the per-session folder on disk where Claude's code reads and writes files before they are saved as artifacts.
