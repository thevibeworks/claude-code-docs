---
title: Review Safety Cases
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases
description: How your team receives, investigates, and responds to the Safety Cases that Anthropic sends, and where to get help.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

Automated safety monitoring checks your prompts and responses for signs of serious misuse, such as attempts to develop offensive cyber or biological capabilities. Enterprise Frontier Safeguards requires [Anthropic Human Review](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency#turn-off-anthropic-human-review) to be off. With it off, a potential violation of Anthropic’s Usage Policy that automated safety monitoring finds can become a Safety Case that your own team reviews. Anthropic expects Safety Cases to be rare for most organizations.

## How Safety Case review works

1. **[Anthropic sends you a Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#where-cases-arrive).**
2. **[You review it](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#read-a-case)** to see which messages it covers and what kind of risk it reports.
3. **[You investigate](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#investigate)**, with your own logs and the Transcripts.
4. **[You respond](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#respond-to-a-case)** to confirm that you investigated.
5. **[Anthropic closes the Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#after-you-respond).**

## Get Safety Cases

Safety Cases can reach you in two ways: as files in your own storage and through the API.

On Claude Platform, keep the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) on. A request that you send while it’s off has no Transcript in your [Case bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) or through the Safety Cases API. Without a Case bucket, you also get no Safety Cases while it’s off.

### In your own storage

Anthropic writes readable Safety Cases and Transcripts to a [bucket in your own cloud account](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-owned-storage#what-is-stored). To select one:

1. Read [Transcripts and Safety Cases in your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#case-and-transcript-bucket) before you select a bucket. Not every Amazon S3 bucket can receive Safety Cases.
2. For each workspace, select the bucket under **Safety Case and Transcript storage** in the Claude Console.

When Anthropic sends you a Safety Case, it adds [Safety Case files](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files) to your storage.

Two limits apply:

* You get Safety Case files only for a workspace that has a [safety data bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) (see [Set up customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage)). That bucket holds Sealed Safety Data, which your team can’t read. You select it under **Sealed Safety Data storage**, which is a separate setting from **Safety Case and Transcript storage**.
* On Claude Platform, you also get Safety Case files only for messages that you send after the workspace starts using its safety data bucket.

### Through the API

The [Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api) serves the same Safety Cases over HTTP. It lets you read and respond to Safety Cases. It’s available only on Claude Platform. It is in beta.

Whether you also need a Case bucket depends on your platform:

* **Claude Platform:** You can also select a Case bucket for each workspace under **Safety Case and Transcript storage**. Without one, you get no Safety Cases for messages with a user profile.
* **Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS:** Safety Cases can reach your team only through a Case bucket. Monitor that bucket, because the 7 days to respond start when Anthropic sends a Safety Case.

### How you know when a Safety Case is created

Anthropic doesn’t notify you automatically when it creates a Safety Case. Monitor your storage or [poll the API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll) for Safety Cases, so that you can respond quickly. See [Alerts for new files](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#alerts) for ways to send an alert to your SIEM or ticketing system based on storage updates.

## Review a Safety Case

### What a Safety Case includes

Each Safety Case includes:

* Its ID
* The policy category, such as `cyber` or `bio`
* The ID of each message, and where to find its Transcript
* The workspace that sent the messages, and sometimes the user profiles that sent them

In your bucket, a Safety Case is a JSON file. [Safety Case file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#safety-case-file) describes its fields.

Through the API, [list your Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll), then [read each message](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#read-a-message). The API also returns the user or API key that Anthropic recorded for a message.

### Investigate a Safety Case

Most Safety Cases come down to one of four outcomes:

| What you find | What to do |
| ----- | ----- |
| **Authorized work.** For example, your red team ran a penetration test under the Cyber Verification Program. | Confirm it with the team that owns the work. Respond with `no_violation`. |
| **An employee or user acting on their own, against policy.** They broke your policies or Anthropic’s Usage Policy without your organization’s approval. | Remove their access and follow your own process. Respond with `violation`. |
| **An external user or a stolen credential.** | Block the user or rotate the key. Respond with `violation`. |
| **A false positive.** Automated safety monitoring misread the intent or the content. | Nothing to fix. Respond with `no_violation`. |

Who you involve, including HR, legal, or a manager, is up to your own process.

<Note>
  Be careful when you put these Transcripts into Claude or another AI model. They can lead to another Safety Case.
</Note>

## Respond to a Safety Case

Respond within 7 calendar days of the Safety Case’s `created_at`, the time when Anthropic sent it. By responding, you confirm that you have investigated and identified the cause and, if there was a violation, taken steps to ensure it does not happen again.

Your Safety Case Response says whether you found a violation. You don’t need to share names, evidence, or Transcripts with Anthropic. Any information you choose to share with Anthropic as part of your response becomes part of the Safety Case. A response closes the Safety Case, so you can’t change it or add to it later.

You can respond in either of two ways. Use one of them for each Safety Case, because Anthropic counts the first response.

### Option 1: Write a response file

Write a [response file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file) to the bucket that holds your Safety Cases. Its path depends on your storage provider:

* **Amazon S3:** `review-responses/<case_id>.json`
* **Google Cloud Storage bucket connected in the Claude Console:** `<organization ID>/review-responses/<case_id>.json`

Check the file against [Rules for a valid file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file-rules), because only a valid file counts.

### Option 2: Respond through the API

Send one request to [respond to the Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#respond).

### After you respond

When Anthropic reads a valid response, it closes the Safety Case. A close reason of `responded` confirms that Anthropic has received your response. Through the API, the Safety Case closes at once. If a Safety Case is still open a day after you wrote a file, see [Why a Safety Case stays open](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#still-open).

If Anthropic needs more information from you about your response, it sends a Safety Notice (see [Poll for Safety Notices](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll-for-notices)), or your Anthropic account team contacts you.

## If Anthropic takes action

Enterprise Frontier Safeguards doesn’t change Anthropic’s [Usage Policy](https://www.anthropic.com/legal/aup) or the standard for enforcing it. Anthropic reserves enforcement for clear, intentional harm.

### If you don’t respond

Responding promptly can help keep your account in good standing. If 7 calendar days pass with no valid response, Anthropic closes the Safety Case. If a Safety Case stays unanswered, Anthropic may suspend access.

### If Anthropic suspends access

In the rare case that automated safety monitoring finds clear, intentional harm, Anthropic can suspend access to limit further harm while you investigate. A suspension can be as narrow as one user or user profile. The Safety Case can name the user profile if you send one. To ask for access back, contact your Anthropic account team. If the Safety Case is open, also respond to it. While your whole organization is suspended, the Safety Cases API refuses your key.

## Best practices

* **Log message IDs.** To trace a message to its sender, Anthropic recommends logging the `id` (`msg_...`) of each Messages API response with your own user ID. It often makes sense to start on this early, because your logs only cover requests from then on. You can also set `metadata.user_id` to an opaque ID, which comes back in the Transcript.
* **Save the Transcripts you need.** Transcripts expire (see [What’s in the bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#whats-in-the-bucket)).

## Reach out for help

Your Anthropic account team is your contact for Safety Cases. Quote the Safety Case’s ID so that Anthropic can find the right Safety Case. You do not need to quote or provide a Transcript.

With no Anthropic Human Review, the people at Anthropic who handle a Safety Case see limited details, such as its ID, its category, and any proposed action. They can’t read your Transcripts.

* **You need more time:** Tell your Anthropic account team before the 7 days end. The Safety Case still closes on time.
* **You think a Safety Case is wrong:** Respond with `no_violation`.

## Questions and troubleshooting

<AccordionGroup>
  <Accordion title="Does your team need 24/7 coverage?">
    Anthropic doesn’t ask for 24/7 coverage for Safety Cases. Anthropic expects them to be rare, and you have days, not hours, to respond. Send alerts to a queue that someone checks every working day.
  </Accordion>

  <Accordion title="Can you test the process before a real Safety Case arrives?">
    Ask your Anthropic account team whether a test Safety Case is available for your organization.
  </Accordion>

  <Accordion title="Does Anthropic send webhooks for Safety Cases?">
    No. [Monitor your bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#set-up-alerts) or [poll the Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll) instead.
  </Accordion>

  <Accordion title="Who reviews when Anthropic Human Review is on?">
    A small, specialized team at Anthropic can review what automated safety monitoring finds. You can keep Anthropic Human Review on only for a workspace on Anthropic-managed storage. Enterprise Frontier Safeguards requires it to be off.
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Check your setup" icon="check" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-console#check-your-setup">
    On Claude Platform, check that your setup works before you start production use.
  </Card>

  <Card title="Set up customer-owned storage" icon="database" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage">
    Keep your Sealed Safety Data in storage in your own cloud account.
  </Card>

  <Card title="Human Review and Access Transparency" icon="shield" href="https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/human-review-and-access-transparency">
    See who at Anthropic reviews your data, and what record you get.
  </Card>
</CardGroup>
