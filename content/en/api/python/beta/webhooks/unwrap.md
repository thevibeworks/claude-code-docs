---
title: Unwrap
url: https://platform.claude.com/docs/en/api/python/beta/webhooks/unwrap
---

# Unwrap

`beta.webhooks.unwrap()`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
client.beta.webhooks.unwrap()
```
