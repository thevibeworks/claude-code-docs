> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compute providers

> Claude Science can run jobs on an external cloud provider you control, and connect to model servers that serve scientific models over HTTP.

Claude Science can run jobs on Modal using a Modal account you own and control. You connect your account, jobs run on it, and Modal bills you directly. Anthropic doesn't provide or bill compute and never sees a payment method.

## Connecting Modal

In Settings > Compute > **Cloud providers**, click Connect on the Modal card. If you've signed in with the Modal CLI (`modal token new`), the app reads `~/.modal.toml` automatically; click Check again after the file exists. Alternatively, paste a **Token ID** and **Token secret** in Settings > Credentials, under Modal. Tokens are stored encrypted on your computer and never shown to Claude.

## Running cloud jobs

When work needs a GPU or more memory than your machine has, Claude proposes a job and a **Start a Modal job?** card appears. The card shows the Modal profile, exact machine spec (for example, H100, 8 CPUs, 32 GiB), a note that billing is per-second, and the maximum billable time. It links to Modal's pricing page. Approve per job, or for the conversation or project.

A separate card asks before Claude opens a Modal setup shell (capped at 30 minutes, no GPU).

Input files are limited to 1 GiB per submit. For larger inputs, Claude can stage data to a Modal Volume and mount it into the job. Outputs written to `./out/` (up to 5 GiB) are returned with logs.

<Note>
  Closing the app doesn't cancel a running Modal job; it continues billing until it finishes or times out.
</Note>

Cost controls: there's no spend ceiling. Each job is approved individually with its machine and time limit visible. **Concurrent jobs** (default 10, set on the Modal page under Settings > Compute) caps simultaneous containers that Claude Science on this machine can run. **Default container timeout** is 12 hours (maximum 23), enforced by Modal. Track spend on Modal's dashboard.

On the Modal page under Settings > Compute you can set the Modal environment and the default application name used for containers.

## Container images

Claude derives a container image from the environment a job needs and builds it once on Modal's build servers, then reuses that image for later jobs until the environment changes. Claude tracks built images in the Details document on the Modal page under Settings > Compute.

## Model endpoints

Claude Science can connect to a model server (hosted, or a container you run) that serves a scientific model over HTTP, and call it directly from analyses.

### NVIDIA BioNeMo NIM

In Settings > Compute, under Model endpoints, click Connect on NVIDIA BioNeMo NIM. Import the skills from the BioNeMo Agent Toolkit, add your NVIDIA NGC API credential, and connect to NVIDIA-hosted API endpoint, or choose to run the model as a local container (On a machine with an NVIDIA GPU). Once connected, ask Claude to start a local Docker NIM container or set up a remote connection for a specific NIM skill from the BioNeMo Agent Toolkit.
