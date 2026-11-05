# How do Anthropic-hosted browsers identify themselves when they browse the web on a user's behalf?

Some Claude products, including **[Claude Duet](https://claude.com/product/claude-duet)**, can use a browser hosted by Anthropic to complete tasks at a user's direction. This is known as agentic browser use. This article explains how website owners can identify traffic from this type of agentic browser use and choose whether to allow it.

Agentic browser use is different from Anthropic's robots (crawlers and fetchers, including `ClaudeBot`, `Claude-User`, and `Claude-SearchBot`). To learn about those, see **[Does Anthropic crawl data from the web, and how can site owners block the crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)**

## How to identify agentic browser traffic

**User-Agent:** Requests come from a real browser running on Anthropic's infrastructure. They carry the `User-Agent` header of the browser itself, with the addition of the token `Claude-Agent` to indicate that the browser is being driven by a hosted Claude agent.

For example:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko;
compatible; Claude-Agent/1.0) Chrome/154.0.0.0 Safari/537.36
```

Other parts of this string can change, so match on the `Claude-Agent` token rather than the full string.

**IP addresses:** This traffic comes from the IP addresses published at **<https://claude.com/.well-known/sail>**, listed under `Claude-Agent`. These addresses may change over time, so we recommend updating your rules from this file automatically rather than hardcoding them.

Anyone can send the same `User-Agent` header, so be sure to check that the traffic originated from one of the listed IPs before concluding that it is genuine. For technical details on the publication format and considerations around using it, see **[draft-kelley-webbotauth-sail-00](https://www.ietf.org/archive/id/draft-kelley-webbotauth-sail-00.html)**. This is not yet a standard, so it may evolve over time.

Allowing or disallowing this traffic will control whether your users can ask their Claude services that leverage this type of agentic browser use to complete tasks on your website. Your preferences for Anthropic's robots (crawlers and fetchers) are independent and **[you can manage them separately](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)**.