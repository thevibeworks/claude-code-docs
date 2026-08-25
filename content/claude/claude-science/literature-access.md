> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Literature access

> Claude retrieves open-access full text without credentials; add publisher keys or a library proxy to reach paywalled text you're entitled to.

Claude retrieves open-access full text without credentials. To reach paywalled text you're entitled to, add publisher keys or your library's proxy in the Claude Science app: select the gear icon and choose **Settings**, then select **Credentials**, then choose **Literature access (journals, etc.)** in the **Services** list. No key bypasses a paywall.

<Note>
  These panels live in the Claude Science app's own **Settings**, separate from your claude.ai account and organization settings. If you've added custom credentials, the **Services** list appears below your **Custom** credentials.
</Note>

Given a DOI or title, Claude tries in order: an open-access copy (Unpaywall, Semantic Scholar, PubMed Central), CrossRef full-text links, publisher routes you hold keys for, your library proxy, then the publisher page. Retrieved files (PDF, XML, or text) are saved into the session.

## Available credentials

Each credential in the **Literature access (journals, etc.)** form is optional and independent.

| Credential                                     | Effect                                                        |
| ---------------------------------------------- | ------------------------------------------------------------- |
| **Elsevier API key** + institutional token     | Enables the Elsevier route (subscription still required)      |
| **Springer Nature API key**                    | Enables the Springer Nature route                             |
| **Semantic Scholar API key**                   | Speeds the Semantic Scholar step                              |
| **NCBI API key**                               | Raises the PubMed rate limit from 3 to 10 requests per second |
| **CORE API key**                               | Gives skills access to the CORE open-access aggregator        |
| Institutional **EZproxy URL** + session cookie | Retries publisher links through your library                  |

OpenAlex has its own entry in the same **Services** list: add a free **OpenAlex API key** there (create one on the [OpenAlex API settings page](https://openalex.org/settings/api)). OpenAlex requires a key on every request, so OpenAlex-backed literature search needs one configured.

NCBI, EBI, and OurResearch (Unpaywall) ask callers to provide a contact email. The first time this applies, a **Share a contact email with research data services?** card appears. Sharing an email enables the Unpaywall step. You can also set this in the app's **Settings**, on the **General** tab, under **Contact email**.

Claude paces requests to each provider at one per second, backs off when asked, and identifies itself in every request. Paywalled HTML isn't scraped.
