> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote compute clusters

> Connect a machine you can reach over SSH (a lab workstation or an HPC login node) so Claude can run jobs on it.

Connect a machine you can reach over SSH (a lab workstation or an HPC login node) so Claude can run jobs on it. Use it to connect to a remote workstation with a GPU, or your existing HPC cluster. Claude Science uses your existing `~/.ssh/config`, authenticates with your key or `ssh-agent`, and installs nothing on the host itself.

## Adding a host

Go to **Settings > Compute** > **SSH hosts** > **Add SSH host**.\
Choose or type an alias from your `~/.ssh/config`. The address, user, port, and any `ProxyJump` come from that file.\
Optionally add notes about the host (partition, account code, module loads, whether software can be installed). Claude reads these before the first job.\
Optionally override **User**, **Port**, or **Identity file** under **Advanced**.\
Click **Add**.

Adding a host runs a read-only probe that records CPUs, memory, GPUs, CUDA driver, presence of conda/modules/Apptainer, scratch directories, and whether `sbatch` exists. On SLURM clusters it reads partitions. Results are saved as editable notes on the host's detail page; re-run with **Probe**.

## Running jobs

Workstations run jobs as detached processes. SLURM clusters receive jobs via `sbatch`. Jobs survive connection loss.

On the host's detail page, set **Scratch directory** (must be on a shared filesystem for SLURM) and **Concurrent job limit** (default 100).

When Claude proposes a remote job, a **Run this job on `<host>`?** card shows the command and script. Approve with **Once**, **This conversation**, **This project**, or **Global** scope. On approval, the job script and inputs are copied to a job directory under the scratch directory.

<Warning>
  Remote jobs run outside the sandbox, as your user on the host, with access to everything your account can read and write there.
</Warning>

Default job timeout is 30 minutes; tell Claude before submitting longer work. When a job finishes, outputs are pulled back into the session. Files over the size threshold (about 100 MB by default) stay on the host, and Claude records their paths.

## Host details

Claude reads host-specific instructions from the Details document on the host's detail page. It holds notes that describe the host's setup and how to run jobs on it: how environments are activated, where data and packages live, and the cluster's scheduling conventions. Claude updates these as it works with the host, and you can edit them at any time.
