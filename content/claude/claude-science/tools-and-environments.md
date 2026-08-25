> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools and environments

> Claude writes and runs Python, R, and shell commands.

Claude writes and runs Python, R, and shell commands. Python and R run in a persistent kernel that keeps variables in memory across steps in a session. The kernel ends after about 30 minutes idle, when a package install restarts its environment, or when the session ends.

## Starter environments

First launch creates two read-only conda environments in \~/.claude-science:

* Python: numpy, pandas, scipy, matplotlib, seaborn, pillow
* R: tidyverse, ggplot2, jsonlite

## Task environments

When work needs packages the starters don't have, Claude reuses an existing named environment or proposes creating a new one (for example, single-cell or structural-biology). A permission card shows the environment name and initial packages. Environments are shared across all projects on the machine. To list or delete environments, ask Claude; there's no settings page for them.

## Installing packages

Claude installs from these sources by default:

* Conda: micromamba from the conda-forge, bioconda, defaults, and pytorch channels
* Python: pip from PyPI
* R: CRAN and Bioconductor

A package installed into an environment is permanent and available in every session and project using that environment. A package installed inline in a code cell (`pip install` or `install.packages()`) lasts only until the kernel restarts. To keep a package, ask Claude to install it into the environment.

For tools without a package, Claude downloads source, builds it in the sandbox with compilers from conda-forge, and saves the build as an artifact for reuse.

The sandbox has no root access or system package manager. `apt` and `sudo` aren't available; Claude uses conda-forge or builds from source instead. Package sources can't be redirected to a different server.

## GPUs

If your Linux machine has GPUs, the sandbox makes them available to code Claude runs, including on multi-GPU machines. You first need to turn GPU access on in the Settings > Compute pane.

<Note>
  Allowing GPU access reduces the default sandboxing configuration applied by Claude Science.
</Note>

If your machine has no GPU, Claude notes this when a task needs one and can run the work on the remote compute you've connected. See Remote compute clusters and External compute providers.
