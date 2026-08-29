# Unwrap

`client.Beta.Webhooks.Unwrap(ctx) error`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Example

```go
package main

import (
	"context"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	err := client.Beta.Webhooks.Unwrap(context.TODO())
	if err != nil {
		panic(err.Error())
	}
}
```
