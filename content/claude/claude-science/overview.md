> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Science

> Anthropic's AI workbench for rigorous science.

Claude Science is a desktop application that pairs Claude with an analysis environment on your computer. Available in beta on macOS, Windows, and Linux. You install it separately from the Claude desktop app; see [Get started](/docs/claude-science/get-started#install) for the installers.

You describe a research task or analysis in plain language; Claude writes and runs Python, R, or shell code in a sandbox, reads the folders you grant it, pulls data from scientific databases through connectors, and saves results as versioned artifacts with a full provenance record. A background reviewer can check Claude's claims against the work that was actually run.

Your files stay on your computer, and code runs in a sandbox. You approve each new folder, network host, and remote job before Claude can use it.

<Note>
  Claude can make mistakes. The reviewer reduces, but doesn't eliminate, errors. It checks claims against the execution record and doesn't re-run analyses. Verify results before relying on them in research, publication, or downstream decisions. Claude Science is a research tool and isn't intended for clinical or diagnostic use.
</Note>

## Use Claude Science outside the life sciences

Claude Science isn't limited to the life sciences. Besides biology, chemistry, and clinical and medical research, it supports computer science and machine learning, engineering, materials science, mathematics, physics, the social sciences, and other fields. Claude Science is for anyone who works through the loop of scientific discovery: generating hypotheses, reviewing literature, designing experiments, running long and complex data analyses, and turning the results into reproducible figures and findings. Claude writes and runs code and [installs the packages](/docs/claude-science/tools-and-environments#installing-packages) an analysis needs.

In any field, Claude Science also gives you these tools:

* **Remote compute.** For long-running or heavy analyses, Claude can run jobs on [a workstation or Slurm cluster you reach over SSH](/docs/claude-science/remote-compute-clusters), or on cloud GPUs through [your own Modal account](/docs/claude-science/compute-providers). On Team and Enterprise plans, your organization's admin decides whether you can use SSH hosts and Modal.
* **Credentials.** Store credentials for [licensed literature](/docs/claude-science/literature-access), [cloud storage](/docs/claude-science/cloud-storage), and other APIs in **Settings > Credentials**, where they're encrypted on your computer.
* **Review.** [The reviewer](/docs/claude-science/the-reviewer) can check Claude's claims against the work that actually ran, and you can add review criteria for your own field in **Settings > Specialists > Reviewer**.

Researchers in the life sciences also get specialized [Featured connectors](/docs/claude-science/connectors-and-skills#featured-connectors) to databases in their fields, and skills for specific models, such as AlphaFold2 for protein structure. Other Featured connectors and skills work in any field: for example, the Literature Graph and Research Resources connectors search scholarly literature and funding opportunities, and the literature review skill helps Claude find, verify, and synthesize papers. To give Claude a data source or method from your own field, see [When the connector you need isn't listed](/docs/claude-science/connectors-and-skills#when-the-connector-you-need-isn%E2%80%99t-listed) and [Skills](/docs/claude-science/connectors-and-skills#skills).

## Requirements

* A Claude account on a Pro, Max, Team, or Enterprise plan. On Team and Enterprise plans, an Owner must [enable Claude Science for the organization](/docs/claude-science/enable-claude-science) first.
* A country or region where Anthropic offers claude.ai. See [Supported countries and regions](https://www.anthropic.com/supported-countries).
* macOS 13 or later (Apple silicon or Intel), Windows 11 (x64), or Linux x64 on a glibc-based distribution.
* About 5 GB of free disk space for the runtime and starter environments.
* On Linux: socat, bubblewrap 0.8.0 or later, and unprivileged user namespaces permitted by the kernel.

## Plans and usage

Claude Science is included in Pro, Max, Team, and Enterprise plans, with nothing separate to buy. Team and Enterprise Owners control whether Claude Science is available to their members through [an admin setting](/docs/claude-science/enable-claude-science). Claude Science isn't available on the Free plan. Scientists at academic and nonprofit research institutions can also get it through the discounted [Claude Team plan for scientists](https://claude.com/programs/team-plan-for-scientists).

Your Claude Science usage counts toward the same usage limits as the rest of your Claude plan, including Claude Code and Cowork. In Claude Science, **Settings > Usage** shows how much you've used and when each limit resets.

You pay more than your plan's price only in these cases:

* **Usage credits and extra usage.** On Pro and Max plans, you can turn on usage credits under **Settings > Usage** in Claude Science to keep working past your limits, and set a monthly spend limit there. Team plans call the same option extra usage, and your admin turns it on. In Claude Science it appears as **Usage credits**, but only Pro and Max plans can change it there. On Team and Enterprise plans, your admin sets spend limits. Some models need usage credits on some plans, and [Claude pricing](https://claude.com/pricing) lists which models each plan includes.
* **Usage-based Enterprise plans.** Instead of fixed usage limits, your organization pays for usage on top of the seat price, within the spend limits your admin sets.
* **Services you connect with your own account.** Services such as [Modal](/docs/claude-science/compute-providers) bill you directly. Anthropic doesn't bill for them.

### When you reach a usage limit

On plans with usage limits, there's a limit that resets every 5 hours and a weekly limit. As you approach one, Claude Science asks whether the session should continue. For the 5-hour limit, you can choose **Keep going** or hold the session until the limit resets. For the weekly limit, the warning offers only **Keep going**.

* **Without usage credits or extra usage, when the reset is less than 8 hours away.** The session pauses, and the composer shows when it will resume. As long as Claude Science stays open, the session picks up where it left off when the limit resets.
* **Without usage credits or extra usage, when the reset is more than 8 hours away.** The session pauses for up to 8 hours, then stops and shows when the limit resets. This can happen at a weekly limit. To continue after the reset, select **Resume** or send a message.
* **At the limit, with usage credits or extra usage turned on.** By default, Claude Science asks whether to keep going on your usage credits or extra usage. Until you answer, the session waits. If you choose not to continue, the session waits for the reset, or stops if the reset is more than 8 hours away.

In each of these cases, your conversation and artifacts are kept.
