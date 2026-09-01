> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network requirements

> The domains Claude Science connects to, grouped for a proxy or firewall allowlist: the app's connections to Anthropic, the analysis sandbox's package and research domains, the domains a package mirror adds and removes, and the built-in list of domains it always blocks.

Claude Science connects to a small, fixed set of domains for sign-in, the Claude API, and the app's own literature search, and to a larger set of package and research domains when Claude runs analysis code, which members adjust on their own computers or your organization manages for every member. This page lists them for the team that manages your proxy or firewall allowlist.

Connections are outbound-only and almost entirely HTTPS on TCP 443 (an internal package mirror may use 8443). The app's own domains are fixed, apart from open-access full-text downloads (covered below); the analysis-sandbox domains are a built-in allowlist that members adjust during onboarding or under **Settings** > **Network**, or that the organization manages for every member (see [Analysis sandbox domains](#analysis-sandbox-domains)).

The domains fall into three groups: the app's own connections every member needs, the analysis sandbox's package and research domains, and the domains the member's browser loads. For the proxy and TLS-inspection settings, see [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks).

## App connections

Every Claude Science install makes these connections, which travel through the member's outbound proxy and TLS inspection, so they need the proxy and corporate-certificate settings from the corporate networks page. All are outbound HTTPS on TCP 443.

| Domain                                  | Required when                                       | Purpose                                                                                                                                                                                            |
| --------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `claude.ai`                             | Always                                              | Browser-based sign-in, usage analytics, feature configuration, and the catalog of available connectors                                                                                             |
| `platform.claude.com`                   | Always                                              | Completing sign-in (the OAuth token exchange)                                                                                                                                                      |
| `api.anthropic.com`                     | Always                                              | The Claude API for every request Claude makes, plus account and usage information                                                                                                                  |
| `o1158394.ingest.us.sentry.io`          | When telemetry is on (the default)                  | Crash and error reporting (the error type and where it happened in Claude Science's own code, never error messages, conversation content, or research data); blocking it degrades diagnostics only |
| `*.mcp.claude.com`                      | When members use the Anthropic-hosted connectors    | PubMed, ClinicalTrials.gov, ChEMBL, and bioRxiv connectors                                                                                                                                         |
| `storage.googleapis.com`                | When automatic updates are on                       | Update manifests and installers                                                                                                                                                                    |
| `api.github.com`, `codeload.github.com` | When members import skills from a GitHub repository | Fetching the skill repository's contents                                                                                                                                                           |

Custom connectors and remote compute that members add reach whatever hosts they are configured with, so allow those case by case. Installs with telemetry turned off (see [Telemetry](/docs/claude-science/manage-on-devices#telemetry)) send no error reports, and blocking `o1158394.ingest.us.sentry.io` affects only error reporting, not the rest of the app.

### Full-text and literature retrieval

When Claude searches the scientific literature or retrieves full text, the app itself contacts these hosts over its own connections, which pass through your outbound proxy and TLS inspection like the app connections above, so the proxy must allow them even though several are also on the sandbox allowlist. Full-text downloads come from wherever the open-access copy of an article is hosted, so on a network that allows only listed hosts, expect retrieval of some full-text copies to fail; the domains below keep literature search and PubMed retrieval working.

| Domain                                            | Required when                                              | Purpose                                        |
| ------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------- |
| `api.unpaywall.org`                               | When Claude retrieves full text                            | Locating open-access copies of articles        |
| `doi.org`                                         | When Claude resolves a DOI                                 | DOI resolution                                 |
| `eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov` | When Claude searches PubMed                                | PubMed/PMC article records and full-text files |
| `api.semanticscholar.org`, `api.crossref.org`     | When Claude searches the literature                        | Scholarly search and citation metadata         |
| `api.openalex.org`                                | When a member adds an OpenAlex API key                     | Validating the stored key                      |
| `api.elsevier.com`, `api.springernature.com`      | Only when the member has stored those publishers' API keys | Publisher full-text APIs                       |

## Analysis sandbox domains

When Claude runs code, its network access passes through a local filtering proxy that allows only the domains on the sandbox's built-in allowlist, grouped by purpose below. By default, each member manages the list on their own computer. Members can turn off any group except package management, during onboarding or under **Settings** > **Network**, and add allowed domains of their own in Settings. An administrator can also use the per-device configuration file, whose `[sandbox.network]` keys add allowed or denied domains, or disable sandbox networking entirely.

An organization can instead manage the list for every member from **Organization settings** > **Claude Science**, with one switch per domain and custom domains of its own. Members then see their **Network** settings read-only, and the domains a member or a configuration file added are set aside while the organization manages the list. See [Network allowlist](/docs/claude-science/admin-controls#network-allowlist) for what the organization's list covers and how changes reach members.

### Package management domains

These domains supply Python, R, and system packages when Claude builds an analysis environment. Members can't turn them off. An organization that manages the allowlist can turn the CRAN and Bioconductor, npm, and GitHub domains off, and the PyPI and conda domains off once an organization package mirror replaces them.

| Domain                                                                                    | Purpose                                         |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `pypi.org`, `*.pypi.org`, `files.pythonhosted.org`                                        | Python packages from PyPI                       |
| `conda.anaconda.org`, `repo.anaconda.com`, `anaconda.org`, `*.anaconda.org`, `*.conda.io` | conda packages                                  |
| `cran.r-project.org`, `cloud.r-project.org`, `bioconductor.org`, `www.bioconductor.org`   | R packages from CRAN and Bioconductor           |
| `registry.npmjs.org`                                                                      | npm packages for connectors that need them      |
| `github.com`, `*.github.com`, `*.githubusercontent.com`                                   | Tools and packages published as GitHub releases |

Claude Science itself does not require GitHub; the package manager ships inside the app. The GitHub domains are used only when a package Claude installs is published as a GitHub release or a member imports a skill from a GitHub repository, and blocking them fails only those operations.

When you configure a conda channel mirror, Claude Science removes only the conda hosts (`conda.anaconda.org`, `repo.anaconda.com`, `anaconda.org`, `*.anaconda.org`) from the allowlist, and a Python index mirror removes only `pypi.org`, `*.pypi.org`, and `files.pythonhosted.org`. The `*.conda.io`, CRAN and Bioconductor, npm, and GitHub rows stay. A removed host is reachable again if a member re-adds it under **Settings** > **Network** or an administrator lists it in `[sandbox.network] allowed_domains`, which takes precedence over the removal. Environment builds contact the mirror host directly from the workstation, not through the outbound proxy, so it must be reachable directly (over your VPN or internal network if the mirror is internal, HTTPS on TCP 443 or 8443). A proxy allowlist entry alone does not make the mirror reachable for builds, and build-time mirror traffic will not appear in your proxy logs. See [Point package installs at an internal mirror](/docs/claude-science/corporate-networks#point-package-installs-at-an-internal-mirror).

An organization package mirror set under **Organization settings** > **Claude Science** removes the same hosts for every member and is admitted the same way. When the organization manages the allowlist, the removed hosts stay unreachable even if they are switched on in the organization's list, and a member's own mirror host is reachable only if the organization's list includes it.

### Research database domains

These groups are on by default. Members can turn them off during onboarding or anytime under **Settings** > **Network**. When the organization manages the allowlist, the organization's per-domain switches apply instead.

| Group                    | Domains                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NCBI and NIH             | `*.ncbi.nlm.nih.gov`, `*.nih.gov`, `cactus.nci.nih.gov`                                                                                                                                                                                                                                                                                                                                                                                              |
| Genomics and biology     | `rest.ensembl.org`, `grch37.rest.ensembl.org`, `*.ensembl.org`, `reactome.org`, `*.reactome.org`, `rest.kegg.jp`, `*.kegg.jp`, `cellguide.cellxgene.cziscience.com`, `gnomad.broadinstitute.org`, `gtexportal.org`, `jaspar.elixir.no`, `www.encodeproject.org`, `mygene.info`, `rfam.org`, `www.cbioportal.org`, `sparql.rhea-db.org`, `bindingdb.org`, `www.bindingdb.org`, `r12.finngen.fi`, `pheweb.jp`, `api.genome.ucsc.edu`, `unibind.uio.no` |
| Proteomics               | `rest.uniprot.org`, `*.uniprot.org`, `string-db.org`, `*.string-db.org`, `*.ebi.ac.uk`, `search.foldseek.com`, `rcsb.org`, `*.rcsb.org`, `*.proteinatlas.org`                                                                                                                                                                                                                                                                                        |
| Literature and citations | `api.semanticscholar.org`, `api.biorxiv.org`, `www.biorxiv.org`, `api.crossref.org`, `doi.org`, `api.openalex.org`, `arxiv.org`, `*.arxiv.org`                                                                                                                                                                                                                                                                                                       |
| Clinical and pharma      | `api.fda.gov`, `clinicaltrials.gov`, `*.clinicaltrials.gov`, `api.clinpgx.org`, `api.platform.opentargets.org`, `cancer.sanger.ac.uk`, `actionability.clinicalgenome.org`, `search.clinicalgenome.org`, `erepo.genome.network`, `civicdb.org`, `api.grants.gov`, `www.antibodyregistry.org`, `cartblanche22.docking.org`, `files.docking.org`                                                                                                        |

### Optional compute integrations

These domains matter only when a member turns on the matching integration.

| Domain                            | Required when                                           | Purpose                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `health.api.nvidia.com`           | When members enable NVIDIA-hosted BioNeMo inference     | NVIDIA's hosted inference endpoint; a member can enter a different endpoint host when connecting BioNeMo under **Settings** > **Compute** |
| `nvcr.io`                         | When members run NVIDIA NIM containers locally          | Pulling NVIDIA container images                                                                                                           |
| `api.modal.com`, `*.w.modal.host` | When members connect a Modal account for remote compute | Modal's API and its dynamic worker hosts, reached from the member's machine                                                               |

### Domains the sandbox always blocks

The sandbox blocks a built-in list of common destinations for moving data out of an organization (anonymous file-upload and paste services, chat and webhook endpoints that accept posted data without an account, reverse-tunnel services, and path-style cloud object storage addresses), and neither members nor configuration can remove entries from it. The blocklist is enforced only inside the analysis sandbox, so it does not affect the app's own connections, such as the update check to `storage.googleapis.com` listed under App connections above.

For the path-style object-storage entries (`s3.amazonaws.com`, `s3.<region>.amazonaws.com`, `storage.googleapis.com`, `commondatastorage.googleapis.com`, and `r2.cloudflarestorage.com`), a bucket named in the URL path is blocked, while a bucket named in the hostname (for example `<bucket>.s3.us-west-2.amazonaws.com` or `<bucket>.storage.googleapis.com`) can be added to the allowlist under **Settings** > **Network**. If your package mirror or a cloud workflow stores data in object storage, address the bucket by hostname.

## Domains the member's browser loads

Sign-in pages and interactive previews load in the member's web browser, so they are governed by your web-filtering policy rather than the outbound proxy or the sandbox allowlist. If your policy blocks these domains, sign-in pages fail to load or interactive previews render blank or broken.

| Domain                                                            | Purpose                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `claude.ai`                                                       | The sign-in authorization page                                                                                                                                                                                                                                 |
| `console.anthropic.com`                                           | The sign-in fallback page, which shows a one-time code the member pastes into the app when the browser cannot return to the app's local callback address                                                                                                       |
| `cdn.jsdelivr.net`, `esm.sh`, `unpkg.com`, `cdnjs.cloudflare.com` | JavaScript display libraries for interactive previews                                                                                                                                                                                                          |
| `3dmol.org`, `3dmol.csb.pitt.edu`                                 | Molecular structure viewer                                                                                                                                                                                                                                     |
| `*.claudemcpcontent.com`                                          | Isolated frames that display Claude's HTML previews and interactive connector output. A standard desktop install serves these frames from the app's own local address, so this entry matters mainly where members open Claude Science from a non-local address |

## Related resources

* [Use Claude Science on a corporate network](/docs/claude-science/corporate-networks): proxy, TLS-inspection, and package-mirror settings
* [Configuration file reference](/docs/claude-science/configuration-file-reference): the network keys in the configuration file
* [Manage Claude Science on devices](/docs/claude-science/manage-on-devices): deploying the configuration file with device management
