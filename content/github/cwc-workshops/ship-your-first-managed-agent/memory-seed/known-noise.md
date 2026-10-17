# Known noise

Things that look alarming in the log and are not the cause of anything:

- auth: `upstream identity-provider timeout` for a minute or two, a few times a week. idp.internal blips, the circuit breaker opens and closes, logins recover on their own. Does not page. Ignore unless it lasts more than five minutes.
- `GC pause` warnings under 400ms on any service. Normal.
- `healthcheck OK` debug lines. Volume only.
