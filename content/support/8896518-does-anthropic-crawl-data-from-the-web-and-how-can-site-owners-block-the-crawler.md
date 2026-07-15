# Does Anthropic crawl data from the web, and how can site owners block the crawler?

As per industry standard, Anthropic uses a variety of robots to gather data from the public web for model development, to search the web, and to retrieve web content at users’ direction. Anthropic uses different robots to enable website owner transparency and choice. Below is information on the three robots that Anthropic uses and how to set your site preferences to enable those you want to access your content and limit those you don’t.

| **Bot**          | **Use**                                                                                                                                                                           | **What happens when you disable it**                                                                                                                                                                                                                                                                |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ClaudeBot        | ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training.                         | When a site restricts ClaudeBot access, it signals that the site's future materials should be excluded from our AI model training datasets.                                                                                                                                                         |
| Claude-User      | Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent.                                                 | Claude-User allows site owners to control which sites can be accessed through these user-initiated requests. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search. |
| Claude-SearchBot | Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. | Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.                                                                                                        |

As part of our mission to build safe and reliable frontier systems and advance the field of responsible AI development, we’re sharing the principles by which we collect data as well as instructions on how to opt out of our crawling going forward:

- Our collection of data should be *transparent*. Anthropic uses the Bots described above to access web content.

- Our crawling should *not* *be* *intrusive or disruptive*. We aim for minimal disruption by being thoughtful about how quickly we crawl the same domains and respecting Crawl-delay where appropriate.

- Anthropic’s Bots *respect “do not crawl”* signals by honoring industry standard directives in robots.txt.

- Anthropic’s Bots *respect anti-circumvention technologies* (e.g., we will not attempt to bypass CAPTCHAs for the sites we crawl.)

To limit crawling activity, we support the non-standard Crawl-delay extension to robots.txt. An example of this might be:

User-agent: ClaudeBot

Crawl-delay: 1

To block a Bot from your entire website, add this to the robots.txt file in your top-level directory. Please do this for every subdomain that you wish to opt out from. An example of this is:

User-agent: ClaudeBot

Disallow: /

Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file in the manner above. Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file. If a crawler has a source IP address on **[this list](https://claude.com/crawling/bots.json)**, it indicates that the crawler is coming from Anthropic.

You can learn more about our data handling practices and commitments at our **[Help Center](https://support.claude.com/en/collections/4078534-privacy-and-legal)**. If you have further questions, or believe that our Bots may be malfunctioning, please reach out to <claudebot@anthropic.com>. Please reach out from an email that includes the domain you are contacting us about, as it is otherwise difficult to verify reports.

You can be notified of substantial changes to this article by clicking here and completing the form:

[Subscribe to updates](https://docs.google.com/forms/d/e/1FAIpQLScQk_jt1NrI0AZU3RfBCDkCe4RBS2lAzMVILBICWdi4xwBaRw/viewform)