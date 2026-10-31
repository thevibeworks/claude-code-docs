> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install financial services plugins for Cowork

> Add the open-source financial services plugin set to Cowork for workflows such as financial modeling, equity research, investment banking, and private equity.

A set of open-source plugins extends Cowork with specialized
capabilities for financial services workflows, including financial
modeling, equity research, investment banking, and private equity.
The plugins also work in Claude Code.

The plugins live in a
[public GitHub repository](https://github.com/anthropics/financial-services)
that you can add as a marketplace in Cowork.

## What's included

The repository contains a core plugin and several add-on plugins that
build on it.

| Plugin | What it does |
| - | - |
| Financial analysis (core) | Build comparable company analyses, DCF models, LBO models, and 3-statement financials. Includes all shared MCP connectors for financial data providers. Install this first. |
| Investment banking | Draft CIMs, teasers, and process letters. Build buyer lists, run merger models, and create strip profiles. |
| Equity research | Write earnings updates and initiating coverage reports. Track catalysts and screen for new ideas. |
| Private equity | Source and screen deals, run due diligence checklists, draft IC memos, and monitor portfolio company KPIs. |

The repository also includes partner-built plugins from LSEG and S\&P
Global, which bring their financial data and analytics directly into
Cowork.

## Add the marketplace

**1. Open Cowork**

Open the Claude Desktop app and select the Cowork tab in the mode
selector.

**2. Open plugin browser**

Select "Customize" on the left sidebar, then "Browse plugins".

**3. Add the marketplace**

Select "Personal", click the "+" button, then select "Add
marketplace from GitHub". Enter the repository URL:
`https://github.com/anthropics/financial-services`

Once added, you'll see the available financial services plugins in your
marketplace.

## Install plugins

**1. Browse the marketplace**

From your plugin marketplace, browse the available financial
services plugins.

**2. Install the core first**

Install the financial analysis plugin first. It provides shared
tools and data connectors that the other plugins use.

**3. Install workflow add-ons**

Install any additional plugins that match your workflow needs.

Once installed, plugins activate automatically. Skills are applied when
relevant, or you can invoke them manually during your Cowork session by
typing `/` or clicking the "+" button.

## Available Skills

After installation, you can invoke Skills like the following.

> [!WARNING]
>
> AI-generated financial analysis should always be reviewed by a
> qualified professional before being used in decision-making.

| Skill | What it does |
| - | - |
| `/comps [company]` | Run a comparable company analysis. |
| `/dcf [company]` | Build a DCF valuation model. |
| `/earnings [company] [quarter]` | Generate a post-earnings update report. |
| `/one-pager [company]` | Create a one-page company profile. |
| `/ic-memo [project name]` | Draft an investment committee memo. |
| `/source [criteria]` | Source deals based on criteria. |

## MCP connectors

The financial analysis core plugin includes connectors for third-party
financial data providers including Daloopa, Morningstar, S\&P Global,
FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and
Egnyte.

> [!NOTE]
>
> Access to these connectors may require a separate subscription or API
> key from the respective provider. Contact your data provider for
> details.

## Customize plugins for your firm

These plugins are starting points. Plugins are file-based Markdown and
JSON, so no code or infrastructure is required to customize them. Edit
the plugin files directly to match your firm's workflows.

* Add your firm's terminology, processes, and formatting standards to
  skill files.
* Swap or add MCP connectors to point at your specific data providers.
* Adjust workflow instructions to reflect how your team does analysis.
* Use `/ppt-template` to teach Claude your firm's branded PowerPoint
  layouts.

## Learn more

See the [Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance)
blog post for background on how the plugins were designed.
