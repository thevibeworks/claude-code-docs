> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors and skills

> Connectors give Claude access to external data sources during an analysis.

Connectors give Claude access to external data sources during an analysis. Skills are written instructions Claude loads when relevant, covering how to run a method, which tools to use, and what to verify. Both are managed in Settings and apply across all projects.

## Featured connectors

Claude Science includes Featured connectors to public life-sciences databases. All are on by default and can be turned off individually in **Settings > Connectors**. Featured connectors are read-only and don't require an account or key. Some underlying databases have non-commercial or attribution terms; review each source's license for your use case.

| Connector                 | Sources                                              |
| ------------------------- | ---------------------------------------------------- |
| Genomes                   | Ensembl (incl. VEP), UCSC                            |
| Genes & Ontologies        | MyGene, UniProt, GO, Reactome, OLS                   |
| Variants                  | gnomAD, ClinVar, dbSNP                               |
| Human Genetics            | GWAS Catalog, eQTL Catalogue, FinnGen, BioBank Japan |
| Clinical Genomics         | ClinGen, CIViC, Open Targets                         |
| Expression                | GTEx                                                 |
| Regulation                | ENCODE, JASPAR, UniBind                              |
| Protein Annotation        | InterPro, Pfam, Human Protein Atlas, STRING          |
| Structures & Interactions | PDB, AlphaFold, EMDB, Complex Portal, IntAct         |
| RNA                       | Rfam                                                 |
| Omics Archives            | GEO, ArrayExpress, PRIDE, MGnify, MetaboLights       |
| Cancer Models             | cBioPortal                                           |
| Chemistry                 | PubChem, ChEBI, Rhea, BindingDB                      |
| Drug Regulatory           | FDA drug data, openFDA                               |
| Literature Graph          | OpenAlex, arXiv                                      |
| Research Resources        | Grants.gov, Antibody Registry                        |

Additional Featured connectors: **BioMart**, **CellGuide** (CELLxGENE cell types), **ZINC** (purchasable chemical space), and **Ketcher Chemistry** (2D molecule sketcher).

Four Directory connectors are available from the [connector directory](https://claude.com/connectors) and are accessible in Claude Science and other Claude products: **PubMed**, **Clinical Trials**, **ChEMBL**, and **bioRxiv**. On Team and Enterprise plans, directory connectors appear only after an admin adds them.

By choosing to enable connectors, you authorize Claude to use the optional enabled resources on your behalf and confirm you have the necessary rights and licenses. These resources and content they reach may be subject to third-party terms (viewable in Settings), and you are solely responsible for compliance.

## Using connectors

Name a source in your request, or describe what you need and Claude chooses from available connector tools. Connector queries appear in the conversation as expandable code steps. Featured connectors you've previously enabled run without a permission card. Connectors you add yourself prompt for approval per tool, with Once, This conversation, This project, or Global scope.

The databases behind Featured connectors are on the network allowlist in groups under Settings > Network. Turning off a group disables the connectors that depend on it.

## Skills

**Settings > Skills** lists the skills Claude can load. Featured science skills include literature review, indication dossier, and model-specific skills for AlphaFold2, Boltz-2, Chai-1, ESMFold2, OpenFold3, ProteinMPNN (with LigandMPNN and SolubleMPNN), DiffDock, ESM-2, Evo 2, Borzoi, scGPT, and scvi-tools.

Claude loads a skill automatically when the work calls for it. Type **/** in the composer to open the skill picker and insert one explicitly.

**Add skill** lets you create your own via **Chat with Claude**, **Write from scratch**, **Upload a skill**, or **Import from GitHub**. **Import from GitHub** works with private repositories too, once you add a GitHub token under **Settings > Credentials**. You can also ask Claude to distill a workflow from an existing session into a skill.
