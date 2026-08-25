> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Science

> Anthropic's AI workbench for rigorous science.

Claude Science is a desktop application that pairs Claude with an analysis environment on your computer. Available in beta on macOS and Linux.

You describe a research task or analysis in plain language; Claude writes and runs Python, R, or shell code in a sandbox, reads the folders you grant it, pulls data from scientific databases through connectors, and saves results as versioned artifacts with a full provenance record. A background reviewer can check Claude's claims against the work that was actually run.

Your files stay on your computer, and code runs in a sandbox. You approve each new folder, network host, and remote job before Claude can use it.

<Note>
  Claude can make mistakes. The reviewer reduces, but doesn't eliminate, errors. It checks claims against the execution record and doesn't re-run analyses. Verify results before relying on them in research, publication, or downstream decisions. Claude Science is a research tool and isn't intended for clinical or diagnostic use.
</Note>

## Requirements

* A Claude account on a Pro, Max, Team, or Enterprise plan. On Team and Enterprise plans, an Owner must [enable Claude Science for the organization](/docs/claude-science/enable-claude-science) first.
* macOS 13 or later (Apple silicon or Intel), or Linux x64 on a glibc-based distribution.
* About 5 GB of free disk space for the runtime and starter environments.
* On Linux: socat, bubblewrap 0.8.0 or later, and unprivileged user namespaces permitted by the kernel.
