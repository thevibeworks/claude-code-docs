> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools and environments

> Claude writes and runs Python, R, and shell commands.

Claude writes and runs Python, R, and shell commands (PowerShell on Windows). Python and R run in a persistent kernel that keeps variables in memory across steps in a session. The kernel ends after about 30 minutes idle, when a package install restarts its environment, or when the session ends.

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

To have conda and pip download packages from an internal mirror instead, see [Point package installs at an internal mirror](https://claude.com/docs/claude-science/corporate-networks.md#point-package-installs-at-an-internal-mirror).

A package installed into an environment is permanent and available in every session and project using that environment. A package installed inline in a code cell (`pip install` or `install.packages()`) lasts only until the kernel restarts. To keep a package, ask Claude to install it into the environment. For a Python package Claude can't install there with pip, see [Python package sources for starter and task environments](#python-package-sources-for-starter-and-task-environments).

For tools without a package, Claude downloads source, builds it in the sandbox with compilers from conda-forge, and saves the build as an artifact for reuse.

The sandbox has no root access or system package manager. `apt` and `sudo` aren't available; Claude uses conda-forge or builds from source instead.

### Python package sources for starter and task environments

When Claude uses pip to install a Python package into a [starter](#starter-environments) or [task environment](#task-environments), it installs only prebuilt packages (wheels) from PyPI or, if one is set up, your [internal mirror](https://claude.com/docs/claude-science/corporate-networks.md#point-package-installs-at-an-internal-mirror). It doesn't install a package from a git repository, a web address, a local folder, or a local file. If the package, or a package it depends on, has no wheel for your computer and Python version, the install fails. That includes a package published only as source code.

When the newest version of a package has no wheel for your computer and Python version but an older version does, pip installs the older version. To find out which version you have, ask Claude. If you need the newest version, use one of the ways below.

To use a package Claude can't install this way, ask Claude to install it into the environment with conda if conda-forge has it. Otherwise, ask Claude to install it with pip in a code cell, where it lasts only until the kernel restarts.

### Environments in granted folders

On Linux, a uv, conda, mamba, or pixi environment in a folder you've granted **Read & write** can still be read-only to Claude. This happens when the environment's package files are hard links shared with the tool's package cache, the folder where the tool keeps the packages it has downloaded. A change to those files could also change the cache and other environments that share them.

Claude can still run code from the environment but can't add, update, or remove packages in it. The failure shows as `Read-only file system` from pip, uv, and pixi, and as `EnvironmentNotWritableError` from conda. In a uv project, `uv run` and `uv sync` fail the same way whenever they have to update the environment, for example after `pyproject.toml` changes.

To add packages, choose one of these:

* **In a uv project, ask Claude to use a separate environment.** Have Claude set `UV_PROJECT_ENVIRONMENT` to the full path of a folder in the session's [workspace folder](https://claude.com/docs/claude-science/core-concepts.md#projects-and-sessions) and run uv as usual. The variable has to stay set for later uv commands, including `uv run` and `uv sync`. The separate environment belongs to that session, so another session starts without it. For a change every session keeps, change the environment yourself in a terminal outside Claude Science.
* **With any of these tools, change the environment yourself.** In a terminal outside Claude Science, use the tool's own commands to add, update, or remove packages.

## GPUs

If your Linux machine has NVIDIA GPUs, the sandbox makes them available to code Claude runs, including on multi-GPU machines. To use them, turn on the **Host GPU** switch in **Settings > Compute**. Sessions you start after that can use the GPU. A session started while the switch was off keeps running without it, and so does a session continued from it with **Continue as a new session**.

> [!NOTE]
>
> Turning on the **Host GPU** switch reduces the default sandboxing configuration applied by Claude Science.

If Claude Science finds no GPU, Claude notes this when a task needs one and can run the work on the remote compute you've connected. See [Remote compute clusters](https://claude.com/docs/claude-science/remote-compute-clusters.md) and [Compute providers](https://claude.com/docs/claude-science/compute-providers.md). If your machine has an NVIDIA GPU but the **Host GPU** switch isn't in **Settings > Compute**, or Claude says there's no GPU in a session started with the switch on, see [How Claude Science detects a GPU](#how-claude-science-detects-a-gpu).

### How Claude Science detects a GPU

On Linux, Claude Science detects an NVIDIA GPU by running `nvidia-smi`. When it finds no GPU this way, Claude treats the machine as having no GPU, and the **Host GPU** switch doesn't appear in **Settings > Compute** unless it's already on.

Claude Science runs the first `nvidia-smi` it finds in these folders, in this order:

1. `/usr/local/nvidia/bin`
2. `/usr/bin`
3. `/bin`
4. `/usr/lib/wsl/lib`
5. `/opt/bin`

To see which folder yours is in, run `command -v nvidia-smi` in a terminal outside Claude Science. Claude Science doesn't look for `nvidia-smi` in any other folder, such as `/usr/local/bin`. If the `nvidia-smi` in a listed folder is a link, the file it finally leads to, after any other links, must also be named `nvidia-smi` and be under `/usr`, `/lib`, `/lib64`, `/bin`, `/sbin`, or `/opt`. To see the file a link finally leads to, run `readlink -f` with its path, for example `readlink -f /usr/bin/nvidia-smi`.

`nvidia-smi` also has to work without the `LD_LIBRARY_PATH` environment variable, because Claude Science doesn't pass that variable on to it, even when your terminal has it set. To check, run it in a terminal outside Claude Science by its full path with the variable removed, for example `env -u LD_LIBRARY_PATH /usr/bin/nvidia-smi`. If that fails where plain `nvidia-smi` works, the variable is the reason. Make `nvidia-smi` work without the variable, or ask your system administrator to.

If `nvidia-smi` is in another folder, link it into `/usr/bin`, which takes administrator (`sudo`) access. If you don't have that access, ask your system administrator to make the link. For example, when `nvidia-smi` is in `/usr/local/bin`, run this in a terminal outside Claude Science:

```bash theme={null}
sudo ln -s /usr/local/bin/nvidia-smi /usr/bin/nvidia-smi
```

After either fix is in place, run `claude-science stop` in a terminal outside Claude Science and start Claude Science again. If Claude Science then finds the GPU, the **Host GPU** switch is in **Settings > Compute** and its label shows the GPU's name. Turn it on if it's off, then start a new session, not one made with **Continue as a new session**.
