---
title: Enterprise Frontier Safeguards on Amazon Bedrock
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/setup-amazon-bedrock
description: Find AWS's setup guide for Enterprise Frontier Safeguards on Amazon Bedrock.
---

To use [Enterprise Frontier Safeguards](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview) (EFS) on Amazon Bedrock, you get access and set it up through AWS, not in the Claude Console. EFS on Bedrock is in beta.

<Warning>
  EFS is only live once you connect your own Amazon S3 bucket, even if Bedrock already shows EFS as `enabled`. Until then, Bedrock stores copies of your prompts and responses in storage that AWS manages, and that setup isn’t EFS.
</Warning>

To set up EFS, follow [AWS’s setup guide](https://docs.aws.amazon.com/bedrock/latest/userguide/anthropic-efs-enterprise-data-controls.html). Use it for storage, keys, and Safety Cases too, because the other pages in this guide describe the Claude Console.

During the beta, some controls and data retention on Bedrock can differ from what this guide describes. Ask AWS for details.
