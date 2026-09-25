> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector verification

> How Anthropic reviews connectors in the directory, what the Verified, Community, and Custom labels mean, and how to stay safe with third-party connectors.

The [Connectors Directory](/docs/connectors/directory) lists connectors from Anthropic and from third-party developers, and each one shows how much Anthropic has reviewed it. Use this page to understand what those labels mean before you connect one.

<Note>
  If you build connectors and want yours listed, see [List your own connector](#list-your-own-connector).
</Note>

## Connector labels

A connector's label reflects the level of review it received. The label affects how the connector is displayed and discovered in the directory, not how the connector itself functions: once connected, a Community connector has the same capabilities and access as any connector you grant.

### Verified

Anthropic has tested a Verified connector's tools for quality and compatibility, and it met the [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) requirements at the time of review. Verified connectors show a checkmark next to their name.

Verification means Anthropic has reviewed the connector more closely than a Community connector. It isn't a security audit or a guarantee of how the connector will perform. The developer operates the connector and controls its tools, which can change after review.

### Community

A third-party developer built a Community connector. Anthropic screens Community connectors before listing them but hasn't reviewed them in depth. Anthropic doesn't control the tools a Community developer makes available and can't guarantee they will work as intended or won't change, so only connect to developers you trust.

Community connectors show a **Community** label in the directory and in [**Customize > Connectors**](https://claude.ai/customize/connectors). Before you connect one, Claude shows a reminder that it hasn't been reviewed in depth.

### Custom

You added a Custom connector yourself, and Anthropic hasn't reviewed it. [Custom connectors](/docs/connectors/custom/add-unlisted#add-a-connector-by-url) explains how to add one.

## Directory listing versus custom connectors

The directory is a catalog of connectors, and listing is optional. Connectors in the directory and custom connectors you add yourself use the same technology, so if you have a connector's URL, you can add it as a custom connector whether or not it's in the directory.

Listing a connector in the directory makes it discoverable by other people and gives it a review label: a checkmark if Anthropic has verified it, or **Community** if Anthropic has screened it but not reviewed it in depth. Listing doesn't change the tools the connector exposes. [Directory vs custom](/docs/connectors/building/directory-vs-custom) has a detailed comparison.

## Stay safe with third-party connectors

Whatever the label, this advice applies to any connector built by someone other than Anthropic:

* Only connect to servers from developers and organizations you trust
* A connector's developer controls which tools it exposes and can change them at any time
* Anthropic doesn't run a third-party connector's servers and doesn't control how it handles your data
* Carefully review requested permission scopes during authentication
* Stay aware of prompt injection risks, even though Claude has built-in protections
* Monitor for unexpected changes in tool behavior

For more, see [security and privacy](/docs/connectors/custom/add-unlisted#security-and-privacy) for custom connectors.

## List your own connector

If you build connectors and want yours in the directory, start with the [connector pre-submission checklist](/docs/connectors/building/review-criteria) and then [submit your connector](/docs/connectors/building/submission).

When you submit a server, Anthropic scans it automatically for policy compliance and, by default, lists it in the directory as a Community connector. Anthropic may then escalate listings flagged as highly useful to Claude users to Verified review, which is higher touch and slower, and in which reviewers run a functional test of each tool. That escalation is assessed automatically. There's no separate application for the **Verified** label, and you don't need to take any action.

## Related resources

* [Connectors Directory](/docs/connectors/directory): browse and connect Verified and Community connectors
* [Custom connectors](/docs/connectors/custom/add-unlisted#add-a-connector-by-url): add a connector by URL, and the security and privacy guidance that applies
* [Publish to the directory](/docs/directory/publish): the developer's overview of submitting a connector or plugin
