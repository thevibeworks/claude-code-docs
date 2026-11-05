# Does Anthropic crawl data from the web, and how can site owners block the crawler?

This page covers Anthropic's robots (crawlers and fetchers). For browsers hosted by Anthropic that Claude uses to complete tasks for users, including in Claude Duet (`Claude-Agent`), see **[How do Anthropic-hosted browsers identify themselves when they browse the web on a user's behalf?](https://support.claude.com/en/articles/18234133)**

## Block or limit Anthropic’s bots

As per industry standard, Anthropic uses a variety of robots to gather data from the public web for model development, to search the web, and to retrieve web content at users’ direction. Anthropic uses different robots to enable website owner transparency and choice. Below is information on the three robots that Anthropic uses and how to set your site preferences to enable those you want to access your content and limit those you don’t.

| **Bot**            | **Use**                                                                                                                                                                             | **What happens when you disable it**                                                                                                                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ClaudeBot`        | `ClaudeBot` helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training.                         | When a site restricts `ClaudeBot` access, it signals that the site's future materials should be excluded from our AI model training datasets.                                                                                                                                                           |
| `Claude-User`      | `Claude-User` supports Claude AI users. When individuals ask questions to Claude, it may access websites using a `Claude-User` agent.                                               | `Claude-User` allows site owners to control which sites can be accessed through these user-initiated requests. Disabling `Claude-User` on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search. |
| `Claude-SearchBot` | `Claude-SearchBot` navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. | Disabling `Claude-SearchBot` on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.                                                                                                          |

As part of our mission to build safe and reliable frontier systems and advance the field of responsible AI development, we’re sharing the principles by which we collect data as well as instructions on how to opt out of our crawling going forward:

- Our collection of data should be *transparent*. Anthropic uses the Bots described above to access web content.

- Our crawling should *not* *be* *intrusive or disruptive*. We aim for minimal disruption by being thoughtful about how quickly we crawl the same domains and respecting Crawl-delay where appropriate.

- Anthropic’s Bots *respect “do not crawl”* signals by honoring industry standard directives in robots.txt.

- Anthropic’s Bots *respect anti-circumvention technologies* (e.g., we will not attempt to bypass CAPTCHAs for the sites we crawl.)

To limit crawling activity, we support the non-standard Crawl-delay extension to robots.txt. An example of this might be:

```
User-agent: ClaudeBot
Crawl-delay: 1
```

To block a Bot from your entire website, add this to the robots.txt file in your top-level directory. Please do this for every subdomain that you wish to opt out from. An example of this is:

```
User-agent: ClaudeBot
Disallow: /
```

Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file in the manner above. Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file. If a crawler has a source IP address on **[this list](https://claude.com/crawling/bots.json)**, it indicates that the crawler is coming from Anthropic.

## How Anthropic honors website preferences for AI training

As of October 30, 2026, Anthropic has begun recognizing a machine-readable signal that lets website owners express a preference about whether their content may be used to train AI models.

This announcement is a continued commitment to respecting robot.txt where ClaudeBot is explicitly named. We’re now confirming that we will honor a new preference signal that lets website owners say “no AI training”.

We’re rolling this out across all of our services over time and globally, and will provide updates on our progress.

The signal follows **[a draft based on work done by the IETF](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal)**, the group that sets many of the internet’s technical standards, in its aipref working group. Because standards in this space are still evolving, the way we read and apply these settings may change too.

### How ClaudeBot rules take priority

ClaudeBot is our training crawler, and we treat rules that name it directly as more specific than the general signal. In practice, for a given path:

- **If your robots.txt file names ClaudeBot**, we follow that rule, even if your general setting says something different.

- **If your robots.txt file doesn’t mention ClaudeBot**, we follow the general setting described above.

You can learn more about our data handling practices in our **[Privacy and legal](https://support.claude.com/en/collections/4078534-privacy-and-legal)** collection. If you have questions, or believe our crawlers aren’t working as described, reach out to **<claudebot@anthropic.com>** from an email that includes the domain you’re asking about.

You can be notified of substantial changes to this article by clicking here and completing the form:

[Subscribe to updates](https://docs.google.com/forms/d/e/1FAIpQLScQk_jt1NrI0AZU3RfBCDkCe4RBS2lAzMVILBICWdi4xwBaRw/viewform)