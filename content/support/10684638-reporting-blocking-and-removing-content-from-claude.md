# Reporting, Blocking, and Removing Content from Claude

Anthropic supports a variety of ways to allow people to control their content and personal information. As a site owner, you can control what shows up in Claude outputs that use web search. As a user or member of the public, you can report problematic content that another user shares publicly or that you receive in a Claude output. For each type of concern, follow the reporting instructions below.

Please note, we reserve the right to suspend users who frequently provide manifestly illegal content and suspend the processing of notices for users who frequently submit notices which are manifestly unfounded. We will provide a warning before suspension.

## How to report safety issues

We welcome reports concerning safety issues so that we can enhance the safety and harmlessness of our models. We would also like to hear from you if you identify our safety mechanisms causing any user experience issues. Please report such issues to <usersafety@anthropic.com> with enough detail for us to replicate the issue.

### Help us improve AI safety by reporting universal jailbreaks

This [form](https://docs.google.com/forms/d/1bjD-H30kVJAbIHnFXKzFcSjkUNjE-mwRHSF7R2uSjYM/edit) allows you to submit universal jailbreaks for ASL-3 uses of concern (meaning elicit information related to biological threats) that you've identified. Universal jailbreaks are techniques that allow users to consistently bypass safety measures across multiple harmful queries. Thank you very much for helping us to keep Anthropic safe.

## How to block or remove content

### Blocking or removing websites from Claude web search

| Remove content from your site                                 | Applicable: all content types<br>Removing content from your site is the best way to ensure that it won't appear in Claude outputs when Claude searches the web.                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Password-protect your files                                   | Applicable: all content types<br>If you have confidential or private content on your site, you need to password protect it to ensure only authorized users can access it. This will also prevent that content from appearing in Claude outputs that rely on web search, or if it already appears, it will eventually remove that content from our search results.                                                         |
| `noindex` tag                                                 | Applicable: all content types<br>The `noindex` robots meta tag is a rule that tells our partners not to index your content so that they don’t send it to us in response to your web search query. Your content can still be linked to and visited through other web pages, or directly visited by users with a link, but the content will not appear in Claude outputs that use web search.                               |
| Disallow crawling with robots.txt                             | Applicable: images and video<br>Our search partners only index images and videos that their bots are allowed to crawl. To prevent them from accessing your media files, use robots.txt rules to block the files.                                                                                                                                                                                                          |
| Disallow Anthropic’s Bots                                     | Applicable: all content types<br>Follow the instructions [here](https://privacy.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler).                                                                                                                                                                                                                      |
| Block access to a URL already appearing in Claude outputs<br> | Applicable: all content types<br>Submit a request to <webresultsoptout@anthropic.com>, including information necessary to prove you own the URL, which can be: an [ICANN registration](https://www.icann.org/resources/pages/register-domain-name-2017-06-20-en), [WHOIS lookup result](https://whois.domaintools.com/), domain registration payment receipt, SSL certificate, or use of a domain-specific email address. |

### Blocking or removing content from shared Claude content

| Report content in-product<br>                        | Applicable: all content within a shared Claude conversation<br>Use the “report” button on the shared content.                                             |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Report content through our standalone reporting form | Applicable: all content within a shared Claude conversation<br>Please report it through [this form](https://claude.com/form/anthropic-content-reporting). |

### Blocking or removing content from Claude outputs or shared Claude content

| Report content<br> | Applicable: all content types<br>If you believe content violates Anthropic’s usage policies or local laws and should be removed or restricted, you can report it through [this form](https://claude.com/form/anthropic-content-reporting).<br>For copyright and trademark disputes, please follow the instructions [here](https://support.anthropic.com/en/articles/10023646-i-think-a-user-is-infringing-my-copyright-or-other-intellectual-property-how-do-i-report-it). |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |