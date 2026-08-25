> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector verification

> How Anthropic reviews connectors, and what Verified, Community, and Custom mean

The [Connectors Directory](/docs/connectors/directory) includes connectors built by Anthropic and by third-party developers. Each connector shows how much Anthropic has reviewed it, so you can decide what to connect to.

## Verified

Anthropic has tested this connector's tools for quality and compatibility and it has met our [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) requirements at the time of review. Verified connectors show a checkmark next to their name. Verification means Anthropic has reviewed the connector more closely than a Community connector, but it is not a security audit or a guarantee of how the connector will perform. The developer operates the connector and controls its tools, which can change after review.

## Community

A third-party developer built this connector. Anthropic screens community connectors before listing, but has not reviewed this connector in depth. We do not control the tools the Community developer makes available and cannot guarantee they will work as intended or will not change, so only connect developers you trust.

Community connectors show a "Community" label in the directory and in [Customize > Connectors](https://claude.ai/customize/connectors). Before you connect one, Claude shows a reminder that it has not been reviewed in depth.

The label reflects the level of review each connector received. It affects how the connector is displayed and discovered in the directory, not how the connector itself functions: once connected, a community connector has the same capabilities and access as any connector you grant.

## Custom

You added this connector yourself. Anthropic has not reviewed it.

See [custom connectors](/docs/connectors/custom/remote-mcp) to learn how to add one.

## The directory is optional

The directory is a catalog, not a separate kind of connector. Connectors in the directory and custom connectors you add yourself use the same technology.

If you have a connector's URL, it can be added as a custom connector. A connector does not need to be in the directory for you to use it.

Listing a connector in the directory makes it discoverable by other people and gives it a review label (a checkmark if Anthropic has verified it, or "Community" if Anthropic has screened but not reviewed it in depth). It does not change the tools the connector exposes. See [directory vs custom](/docs/connectors/building/directory-vs-custom) for a detailed comparison.

## Advice for all third-party connectors

Whatever the label, this advice applies to any connector built by someone other than Anthropic:

* Only connect to servers from developers and organizations you trust.
* A connector's developer controls which tools it exposes and can change them at any time.
* Anthropic does not run a third-party connector's servers and does not control how it handles your data.
* Carefully review requested permission scopes during authentication.
* Be aware of prompt injection risks; Claude has built-in protections.
* Monitor for unexpected changes in tool behavior.

For more, see [security and privacy](/docs/connectors/custom/remote-mcp#security-and-privacy).

## List your own connector

If you build connectors and want yours in the directory, start with the [review criteria](/docs/connectors/building/review-criteria) and the [submission guidelines](/docs/connectors/building/submission).
