---
title: Verify Access Transparency events with the transparency log
url: https://platform.claude.com/docs/en/manage-claude/access-transparency-log
description: Use signed checkpoints and Merkle proofs from the Compliance API to verify that no Access Transparency event was removed or altered after it was committed to the log.
featureMetadata:
  status: beta
---

Learn how to cryptographically verify that no [Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency) event was removed or altered after it was committed to your organization's transparency log.

<Note>
  The transparency log is in beta, and its endpoints and response shapes may change during the beta. It is part of Access Transparency, which is available to eligible customers on request and is not self-serve (see [Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency)). Anthropic maintains one for your organization once Access Transparency is enabled. You read it through the Compliance API with the same key and scope you use for the [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed).

  Your log is created when the first Access Transparency event is recorded for your organization after enablement. Until then, every transparency log endpoint returns `404`.

  The transparency log is provided for your information. It is not designed or certified to satisfy any security, privacy, or regulatory requirement. You are responsible for determining whether it fits your own obligations.
</Note>

## How the transparency log works

A transparency log is a technique for making a record tamper-evident. Entries are only ever appended. Each time the log grows, its operator signs a short statement, called a checkpoint, that commits to every entry so far through a Merkle tree hash. Anyone who keeps a checkpoint can later demand proof that the current log still contains everything that checkpoint covered, unchanged and in the same order. Removing or rewriting an entry therefore cannot go unnoticed by a verifier who kept a checkpoint that covered that entry. Certificate Transparency and the Go module checksum database are built on the same technique. [C2SP tlog-tiles](https://c2sp.org/tlog-tiles) is an open specification for serving such a log as signed checkpoints plus static, cacheable tiles of hashes and entries, so that clients can fetch the hashes and compute every proof themselves.

When Access Transparency is enabled, Anthropic maintains a transparency log for your organization. It is an append-only, cryptographically signed record of Access Transparency events (`anthropic_access` and `cmek_preserve`). Each such event recorded for your organization after the log was created is appended to it. The log follows the C2SP tlog-tiles format, so tooling built for that standard understands its checkpoints, tiles, and proofs.

* **One log per organization.** Each organization's log has a fixed origin string: `axt.anthropic.com/<your organization UUID>`. The origin never changes for the life of the organization.
* **Every new event becomes a leaf.** When an Access Transparency event becomes eligible to appear on your Activity Feed, it is first appended to your log as a leaf, and only then served on the feed. A leaf is a deterministic serialization of the event's documented fields. The event on your feed carries `transparency_log_leaf_index`, its zero-based position in your log.
* **Checkpoints commit to the whole history.** The log is a Merkle tree. Whenever it grows, Anthropic publishes a signed checkpoint: a short text document stating the log's origin, its current size, and the root hash that commits to every leaf. Each checkpoint carries exactly one signature from the log's signing key.
* **Two proofs follow.** An inclusion proof shows that a specific event is present at its position under a checkpoint. A consistency proof shows that a later checkpoint is an append-only extension of an earlier one you saved, so nothing between them was removed or changed.
* **Verification keys are served in-band.** The [verifier keys endpoint](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys) returns the public keys that sign checkpoints. In a planned key rotation, the new key is added to that list before it starts signing, and earlier keys stay listed. Checkpoints you already hold therefore keep verifying.

### What the transparency log proves

* The leaf fields of an event you hold (listed in [How an event becomes a leaf](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#how-an-event-becomes-a-leaf)) are, byte for byte, what Anthropic committed to the log.
* The log for your organization only ever grows. Verification against a checkpoint you hold fails if an event committed to the log is later deleted or rewritten there. It also fails if you are served a different history from the one you were served before.
* New entries can only be appended. An event cannot be inserted into history you have already verified.

### What it does not prove or change

* It does not prove that every access was recorded, or that a recorded event accurately describes the access. It proves only that what Anthropic committed to the log has not changed since.
* It does not change [what Access Transparency covers](https://platform.claude.com/docs/en/manage-claude/access-transparency#what-access-transparency-covers) or when events arrive.
* Served fields outside the leaf, such as `workspace_uuid` and any field added later, are not covered by the proof.
* An inclusion proof speaks for an event you were served. It does not by itself prove that the feed listed every leaf the log holds. The log's [entry bundles](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-an-entry-bundle) contain every leaf, so you can read the complete set of committed events directly when you need it.
* The presence of `transparency_log_leaf_index` on an event is a pointer, not a proof. Always verify inclusion before treating an event as committed in the log.
* The protection against a rewritten history comes from the checkpoints you keep. A checkpoint's signature by a key listed in [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints) proves that it came from Anthropic's log. A consistency proof from the checkpoint you saved last time proves that the history you already observed only grew.

## Before you begin

You need:

* A Compliance Access Key with the `read:compliance_activities` scope, the same key and scope you use for the [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed). A parent-organization key can read each enrolled child organization's log by naming the child organization on every request.
* Your organization's UUID. Find it in the Claude Console under **Settings > Organization**. It is the same value the Activity Feed serves as `organization_uuid`, but take it from the Console. This value is what makes a checkpoint yours, so it must not come from the API you are verifying. You derive your log's origin from it as `axt.anthropic.com/<organization UUID>`. Derive this string yourself. Do not read it from an API response.
* Somewhere durable to keep the last checkpoint you verified. That saved checkpoint is what turns "the log is consistent today" into "the log has been consistent since you started watching."

## Timing

* **Events:** Access Transparency events appear on your Activity Feed within two business days of the access. An event enters the log only once it is eligible to be served, so the log never reveals an event early. Because the log is written before the feed serves the event, an entry can briefly appear in the log before its event appears on your feed. That gap is not a discrepancy.
* **Checkpoints:** A new checkpoint is published whenever your log grows.
* **Inclusion proofs:** A proof for a newly served event is available once a checkpoint covering the event's position is published, normally very shortly after the event appears. If you request one sooner, you receive a `404` and retry after a short delay.
* **Verification cadence:** Run your verification at least daily. Hourly is reasonable.
* **Disenrollment:** If your organization stops using Access Transparency, nothing is deleted. Your log stays readable through the same endpoints. If Access Transparency is enabled again later, the same log continues.

## Retention and deletion

* **Transparency log:** Anthropic does not delete entries from your log, and the log has no expiry. It is kept if your organization stops using Access Transparency and after your organization is deleted, because removing entries is the change the log exists to detect. [Entry bundles](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-an-entry-bundle) hold the [leaf fields](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#how-an-event-becomes-a-leaf) of each event, so those fields are kept for as long as the log is.
* **Activity Feed:** Access Transparency events on the Activity Feed follow the feed's retention. Activities are retained for 6 years. See [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed).
* **No deletion by you:** The transparency log endpoints are read-only. There is no way to delete or amend an entry.

## Transparency log endpoints

Six read-only endpoints are served under `https://api.anthropic.com/v1/compliance/transparency_log/`:

| Endpoint                                                                                                                      | Returns                                                          |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`GET /checkpoint`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-latest-checkpoint)     | The latest signed checkpoint                                     |
| [`GET /keys`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys)               | The verifier key set                                             |
| [`GET /inclusion`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#fetch-an-inclusion-proof)        | An inclusion proof for one event                                 |
| [`GET /consistency`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#fetch-a-consistency-proof)     | A consistency proof from a checkpoint you hold to the latest one |
| [`GET /tile/{level}/{index}`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-a-hash-tile)     | A Merkle hash tile                                               |
| [`GET /tile/entries/{index}`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-an-entry-bundle) | An entry bundle of leaf bytes                                    |

Checkpoints, tiles, and entry bundles follow the C2SP tlog-tiles wire format exactly. The two proof endpoints are conveniences: every proof is also computable from tiles, so you never have to trust a proof endpoint's output. You verify the hashes it returns against a signed checkpoint.

### Authentication and scoping

Send your Compliance Access Key in the `x-api-key` header and the `anthropic-version` header, as for every Compliance API request (see [Versioning](https://platform.claude.com/docs/en/manage-claude/compliance-api#versioning)). The Compliance API must be enabled for your organization.

There is no separate transparency log permission. Any key that can read your organization's Activity Feed, for your organization or its parent, can read your whole log, including the event fields in its entry bundles.

Every request reads exactly one organization's log:

* An organization-level key reads its own organization's log. The `organization_id` query parameter is optional. If present, it must name the key's own organization.
* A parent-organization-level key must pass `organization_id`, naming one child organization.
* `organization_id` accepts the `org_...` tagged ID or the organization UUID.

A `404` means there is no log this key can read. An organization outside the key's scope, a nonexistent organization, and an organization whose log has not been created yet are deliberately indistinguishable. The log of an organization that has since stopped using Access Transparency is not this case: it continues to be served.

### Errors

Errors use the standard Compliance API JSON error envelope on every endpoint, including the text and binary ones. See [Errors](https://platform.claude.com/docs/en/manage-claude/compliance-errors) for the envelope and the shared error types.

| Status | Meaning on this surface                                                                                                                                                              |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `400`  | `organization_id` is malformed or is omitted with a parent-organization key, the Compliance API is not enabled, a query parameter is unknown, or a per-endpoint validation failed    |
| `401`  | The API key is missing or not valid                                                                                                                                                  |
| `403`  | The key lacks the required scope                                                                                                                                                     |
| `404`  | No log readable by this key, or the per-endpoint "not covered" and "beyond the tree" cases                                                                                           |
| `429`  | Rate limited. These endpoints share the Compliance API's per-parent-organization [rate limit](https://platform.claude.com/docs/en/manage-claude/compliance-api). Honor `retry-after` |
| `503`  | The log is temporarily unavailable. Retry with backoff                                                                                                                               |

### Caching

Responses are cacheable only by the requesting client. `Cache-Control` always includes `private`, and responses carry `Vary: x-api-key`. Do not put a shared cache in front of these endpoints. Full tiles and full entry bundles never change and are served with `Cache-Control: private, max-age=604800, immutable`. Everything else, including checkpoints, proofs, keys, partial tiles, and errors, is served with `Cache-Control: private, no-store`.

### Read the latest checkpoint

`GET /v1/compliance/transparency_log/checkpoint`

```bash
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/transparency_log/checkpoint" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

The response is `text/plain`: a C2SP [signed note](https://c2sp.org/signed-note). The body lines are the origin, the tree size in decimal, and the base64 root hash. A blank line follows, then the signature line, which starts with an em dash (U+2014), names the origin, and ends with a base64 value. Values here are illustrative:

```text wrap
axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b
1207
C6C4HzGRqDNlbu54LWCvpDX0NcB5DRTmLcjM4u5vWUI=

— axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b q83vATBFAiEAvL8m…(base64)…
```

* The first four bytes of the decoded signature value are the signing key's `key_hash`, which tells you which entry in the [verifier key set](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys) to verify with. The remaining bytes are an ASN.1 DER ECDSA P-256 signature over the SHA-256 of the note body: every byte before the blank line, including the body's trailing newline.
* A checkpoint can carry additional lines after the root hash. Ignore lines you do not understand. They are covered by the signature.
* Ignore a signature line whose name is not your origin or whose key hash you do not hold.
* Never cache a checkpoint. A stale one hides the log's current size, so newly served events look uncovered.

### Read the verifier keys

`GET /v1/compliance/transparency_log/keys`

```bash
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/transparency_log/keys" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

```json
{
  "type": "transparency_log_keys",
  "origin": "axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b",
  "log_keys": [
    {
      "verifier_key": "axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b+<key_hash>+<base64 key>",
      "key_hash": "<8 lowercase hex digits>",
      "fingerprint": "<64 lowercase hex digits>",
      "algorithm": "ecdsa_p256_sha256",
      "public_key": "<base64 DER SubjectPublicKeyInfo>"
    }
  ]
}
```

| Field                     | Type   | Description                                                                                                                                                                                                                                                                                              |
| ------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                    | string | Always `transparency_log_keys`                                                                                                                                                                                                                                                                           |
| `origin`                  | string | The origin line every checkpoint of this log carries. Informational: compare checkpoints against the origin you derive yourself, not against this field                                                                                                                                                  |
| `log_keys`                | array  | The key that signs new checkpoints first, then every other key the log serves, newest first. Never empty                                                                                                                                                                                                 |
| `log_keys[].verifier_key` | string | The key as a C2SP note-verifier string, `<origin>+<key_hash>+<base64 key>`, accepted by tlog-tiles tooling that supports ECDSA note keys (for example, the Go `github.com/transparency-dev/formats` module). The base64 part decodes to the algorithm byte `0x02` followed by the DER-encoded public key |
| `log_keys[].key_hash`     | string | Eight lowercase hex digits. The 4-byte selector that matches this key to a checkpoint's signature line. It is the first four bytes of `fingerprint` and is not an identity                                                                                                                               |
| `log_keys[].fingerprint`  | string | 64 lowercase hex digits: the SHA-256 of the DER `SubjectPublicKeyInfo`                                                                                                                                                                                                                                   |
| `log_keys[].algorithm`    | string | The key type, currently `ecdsa_p256_sha256`. Values may be added. Skip a key whose algorithm you do not support                                                                                                                                                                                          |
| `log_keys[].public_key`   | string | The public key as base64 DER `SubjectPublicKeyInfo`                                                                                                                                                                                                                                                      |

The `key_hash` covers only the key bytes: it is the first four bytes of SHA-256 over the DER `SubjectPublicKeyInfo`, which is the rule the ECDSA note-verifier encoding uses. It is not the name-dependent key ID that the base signed-note format defines for Ed25519 keys, so it does not change with the origin. A valid signature by a key listed in [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints) proves the checkpoint came from Anthropic's transparency log service. The origin line inside the signed checkpoint is what binds it to your organization. That is why you compare that line against the origin you derive yourself.

Keys can rotate:

* A rotation is a cutover. From some checkpoint on, new checkpoints are signed by the new key.
* In a planned rotation, the new key appears in `log_keys` before it signs anything, and earlier keys stay listed. A checkpoint you saved before the rotation therefore keeps verifying.
* A verifier can fetch the key set on every run or hold it locally. A verifier that holds it locally re-reads this endpoint when it meets a signature whose `key_hash` it does not hold.

#### Published key fingerprints

Anthropic publishes the fingerprint of every key that signs checkpoints here, outside the API. This lets you check a key you hold locally against a source the serving path cannot alter. The key you hold may come from an earlier `GET /keys` response or from tooling that pins the key.

| Key hash   | SHA-256 fingerprint                                                | Algorithm           | Signing since | Status              |
| ---------- | ------------------------------------------------------------------ | ------------------- | ------------- | ------------------- |
| `1dff5fe4` | `1dff5fe420d49743fe444a04fc17f818eea856699dec2ebbc24df15602c74a58` | `ecdsa_p256_sha256` | 2026-08-17    | Current signing key |

A planned rotation is announced on this page at least 30 days before the new key signs its first checkpoint. During that notice period the new key is listed in `log_keys` and in this table with its switch date. Retired keys stay listed with their service dates. A key that does not appear in this table is not legitimate, whatever `GET /keys` returns. Treat a checkpoint that verifies under no listed key as a verification failure, and report it to your Anthropic account representative or [Anthropic support](https://support.claude.com).

[`axt-verify`](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#verify-with-axt-verify) carries the current key in each release and never reads a key from the API. Each release carries exactly one key. On the switch date, Anthropic starts signing with the new key and publishes the `axt-verify` release that carries it. On the same date Anthropic re-issues every organization's latest checkpoint under the new key, even for a log that has not grown. Upgrade on the switch date. Running the old release after the switch fails with exit status `1`, and so does running the new release before it. Either failure clears once you run the matching release. A verifier you maintain yourself needs the new fingerprint, with its switch date, added before that date.

### Fetch an inclusion proof

`GET /v1/compliance/transparency_log/inclusion?leaf_index={index}`

| Parameter         | Type              | Description                                                                                                                            |
| ----------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `leaf_index`      | integer, required | The event's position in the log: the `transparency_log_leaf_index` the Activity Feed served on the event. Must be zero or greater      |
| `organization_id` | string, optional  | See [Authentication and scoping](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#authentication-and-scoping) |

```bash
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/transparency_log/inclusion" \
  --data-urlencode "leaf_index=41" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

```json
{
  "type": "transparency_log_inclusion_proof",
  "leaf_index": 41,
  "hashes": [
    "mUdyOWMp0zXIq0CDMvSYDUSBl9yAvnTZzdm51RwWpUM=",
    "yR6tDHkAhKvdQSLqQATVjXOo4GM3FDyiKF2XCKTtMUI=",
    "..."
  ],
  "checkpoint": "axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b\n42\nCsRlS31ITFHrX9GR5XjyPw8n0MkfrB8Yh2UDHl3Lr3E=\n\n— axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b q83vATBEAiB0…(base64)…\n"
}
```

| Field        | Type             | Description                                                                                |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------ |
| `type`       | string           | Always `transparency_log_inclusion_proof`                                                  |
| `leaf_index` | integer          | The event's position in the log, echoed from the request                                   |
| `hashes`     | array of strings | The base64 sibling hashes of the audit path, ordered from the leaf up to the root          |
| `checkpoint` | string           | The latest signed checkpoint, the one the proof verifies against. It carries the tree size |

There is no lookup by activity ID. You always hold the index, because it arrives on the event, and you check the proof against the event bytes you fetched from the feed.

A `404` means the latest published checkpoint does not cover the supplied position:

* For an index you read off a served event, this is transient. A covering checkpoint is published shortly, so retry after a short delay.
* The same `404` answers any other uncovered position, such as an index the feed never served. For such a position there is no promise that a covering checkpoint is ever published. The response does not say which case you are in.

A `leaf_index` that is missing or is not a non-negative integer returns `400`.

### Fetch a consistency proof

`GET /v1/compliance/transparency_log/consistency?from={size}`

| Parameter         | Type              | Description                                                                                                                            |
| ----------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `from`            | integer, required | The tree size of the earlier checkpoint you hold. Must be at least 1 and at most the latest checkpoint's tree size                     |
| `organization_id` | string, optional  | See [Authentication and scoping](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#authentication-and-scoping) |

```bash
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/transparency_log/consistency" \
  --data-urlencode "from=1180" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

```json
{
  "type": "transparency_log_consistency_proof",
  "hashes": [
    "dGw0aPzu2N0pdc4C5ZAvNIbkXF7J6F9ZQLkPpV6v8Vg=",
    "9PSWm1T9RUmhjF6z6YQzB9CW6E2m2n3mK0aVgqf5Qm0=",
    "..."
  ],
  "checkpoint": "axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b\n1207\nC6C4HzGRqDNlbu54LWCvpDX0NcB5DRTmLcjM4u5vWUI=\n\n— axt.anthropic.com/25f6429a-3293-49bf-afed-cb312911554b q83vATBFAiEAvL8m…(base64)…\n"
}
```

| Field        | Type             | Description                                                                          |
| ------------ | ---------------- | ------------------------------------------------------------------------------------ |
| `type`       | string           | Always `transparency_log_consistency_proof`                                          |
| `hashes`     | array of strings | The base64 proof hashes, in RFC 9162 order                                           |
| `checkpoint` | string           | The latest signed checkpoint, the one the proof extends to. It carries the tree size |

* The proof always extends to the latest published checkpoint. This API never serves historical checkpoints: you keep the ones you are served.
* A `from` equal to the latest checkpoint's tree size returns the empty proof.
* A held checkpoint of tree size 0 needs no consistency proof, because every log extends the empty log. Adopt the latest checkpoint directly in that case.
* A `from` less than 1, or greater than the latest checkpoint's tree size, returns `400`.
* If the log can no longer prove that it extends a checkpoint it once signed for you, treat that as a verification failure, not a usage error.

### Read a hash tile

`GET /v1/compliance/transparency_log/tile/{level}/{index}`

Returns `application/octet-stream`: concatenated 32-byte SHA-256 hashes, per tlog-tiles. Tile addressing follows tlog-tiles exactly, including the `{level}` and `{index}` path grammar, the `x001/234` index form for large trees, and the partial-tile suffix `.p/{width}`. Hash tiles are the unit from which tlog-tiles clients compute proofs themselves.

* Full tiles are immutable and are served with `Cache-Control: private, max-age=604800, immutable`.
* Partial tiles are superseded as the tree grows and are served with `Cache-Control: private, no-store`. Once a tile fills, a request for its earlier partial form can return `404` even though the full tile exists. Falling back from the partial tile to the full tile is the client's job, as tlog-tiles specifies, and standard clients already do it.
* A malformed `level`, `index`, or partial-tile width returns `400`. A tile position beyond the current tree size returns `404`.

### Read an entry bundle

`GET /v1/compliance/transparency_log/tile/entries/{index}`

Returns `application/octet-stream`: consecutive leaf entries, each prefixed with its big-endian `uint16` length, per tlog-tiles. Entry bundles contain event plaintext: the [canonical bytes](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#how-an-event-becomes-a-leaf) of each Access Transparency event. That is why the whole surface requires the Activity Feed's scope. Addressing, the partial form, caching, and errors are identical to hash tiles.

## The `transparency_log_leaf_index` field on Activity Feed events

`anthropic_access` and `cmek_preserve` events on `GET /v1/compliance/activities` carry `transparency_log_leaf_index`, an integer, whenever the event has a leaf. Other activity types never carry it.

* **The key is absent, not `null`, when the event has no leaf.** A robust verifier treats an absent key and a `null` value the same way.
* **An event is served without `transparency_log_leaf_index` in only two cases.** The first is while your organization is not enrolled in Access Transparency, that is, before enrollment or between an un-enrollment and a re-enrollment. The second is when the event was recorded before your organization's log was created. For an organization enrolled before the transparency log was introduced, that includes its earlier history. Once your log exists and while you are enrolled, every event is appended to the log before the feed serves it. If a fault prevents the feed from learning the index, the feed delays the event rather than serving it without one. The event is not lost: it is already in the log and appears on the feed, index included, once the fault is remediated. An index-less event is not expected when it is dated after your log was created and falls inside a period when you were enrolled.
* **A present index is a pointer, not a proof.** Verify inclusion before treating the event as committed in the log. The anomaly worth escalating is a present index whose inclusion proof still cannot be fetched long after a covering checkpoint should have been published.
* The index is assigned when the event is appended to the log and is not one of the fields that make up the leaf.

## How an event becomes a leaf

A leaf entry is the schema-version byte `0x01` followed by canonical JSON of 11 fields. The JSON follows [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) (JSON Canonicalization Scheme), and the fields are taken from the event exactly as the Activity Feed serves it:

* `id`, `type`, `created_at`, `accessed_at`, `organization_id`, `organization_uuid`, `workspace_id`, `accessor_department`, and `reason_code`
* `actor`, with its nested `type` and `email_address`
* `resource_details`, with its nested `type`, `id`, and `parent`

The rules:

* Served fields outside that set, such as `workspace_uuid` and `transparency_log_leaf_index` itself, are ignored.

* A documented field that the served event omits enters the leaf as `null`. An empty string is distinct from `null`.

* `actor` and `resource_details` are objects with exactly their documented keys when the served event carries them. Under version `0x01`, `actor.email_address` and `resource_details.parent` are always `null`. When the served event omits one of these objects or serves it as `null`, the whole value is `null` in the leaf, not an object of `null` fields. Many access events carry no `resource_details`.

* String values, including both timestamps and `reason_code`, are taken byte for byte as served. If you re-derive a timestamp from another representation, reproduce the served rendering exactly:

  * RFC 3339 UTC with a `Z` suffix.
  * `created_at` has no fractional digits when its microseconds are zero, and exactly six otherwise.
  * `accessed_at` has zero, three, six, or nine fractional digits, the shortest that preserves its nanoseconds exactly.

* Canonical JSON means object keys sorted, no insignificant whitespace, and minimal string escaping. No numbers appear anywhere in the leaf.

* The leaf hash is RFC 6962's `SHA-256(0x00 || entry)`. Interior nodes hash as `SHA-256(0x01 || left || right)`.

* A verifier rejects an unknown version byte, and a `0x01` leaf whose `type` is not one of the two Access Transparency types. New event types or rule changes ship under a new version byte. Existing leaves never re-hash.

For example, this access event as the Activity Feed serves it:

```json
{
  "id": "activity_01GPXmAhizavrUuoXNn3tzeA",
  "type": "anthropic_access",
  "created_at": "2025-07-08T18:40:00Z",
  "accessed_at": "2025-07-08T18:39:58Z",
  "organization_id": "org_015gtSHLz269eTwgrH8NX5yk",
  "organization_uuid": "25f6429a-3293-49bf-afed-cb312911554b",
  "workspace_id": "wrkspc_01PaGUP2rbg1XDh7Z9W1CEpd",
  "workspace_uuid": "b6ce2143-1083-d4a7-247c-17530f55a076",
  "accessor_department": "Trust & Safety",
  "reason_code": "safety_review",
  "actor": { "type": "anthropic_actor", "email_address": null },
  "resource_details": { "type": "message", "id": "msg_01HXAMPLE12345678" },
  "transparency_log_leaf_index": 17
}
```

becomes this canonical JSON. It has exactly the 11 documented keys, sorted, on one line. `workspace_uuid` and `transparency_log_leaf_index` drop out, and `resource_details.parent`, absent from the served event, enters as `null`:

```text wrap
{"accessed_at":"2025-07-08T18:39:58Z","accessor_department":"Trust & Safety","actor":{"email_address":null,"type":"anthropic_actor"},"created_at":"2025-07-08T18:40:00Z","id":"activity_01GPXmAhizavrUuoXNn3tzeA","organization_id":"org_015gtSHLz269eTwgrH8NX5yk","organization_uuid":"25f6429a-3293-49bf-afed-cb312911554b","reason_code":"safety_review","resource_details":{"id":"msg_01HXAMPLE12345678","parent":null,"type":"message"},"type":"anthropic_access","workspace_id":"wrkspc_01PaGUP2rbg1XDh7Z9W1CEpd"}
```

The leaf entry is the byte `0x01` followed by those UTF-8 bytes. Its leaf hash, `SHA-256(0x00 || entry)`, is `6ro7vTcFq+sYDZiiGvZaFetUIoMSLig3DGDrCKK1HFU=` in base64. Use this example as a test vector for your own canonicalization code.

## Verify your log

Verification runs on your own infrastructure. Everything the API returns is untrusted until it verifies against two things you hold yourself. The first is the origin you derive from your organization UUID. The second is the checkpoint you saved on your last run. A complete verification run does the following, in order:

1. Fetch the [verifier key set](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys). Compute each key's fingerprint yourself as the SHA-256 of its base64-decoded `public_key`. Keep only the keys whose fingerprint appears in [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints), together with each key's status there. Verify a newly fetched checkpoint only under a key that table lists as current on that date. Accept a retired key only for a checkpoint you saved before its retirement date.
2. Establish the latest checkpoint. On the first run, fetch it from the [checkpoint endpoint](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-latest-checkpoint). On every later run, request a [consistency proof](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#fetch-a-consistency-proof) from the tree size you saved. The response carries the latest checkpoint together with the proof.
3. Check the checkpoint's origin line first. Compare its first line, byte for byte, with the origin you derived. Reject any checkpoint whose origin differs, before doing anything else.
4. Verify the checkpoint's signature. Find the signature line named for your origin whose first four decoded bytes equal the `key_hash` of a currently valid key you kept. Verify the remaining bytes as an ECDSA P-256 signature over the SHA-256 of the note body, using that key's `public_key`. If no signature line matches such a key, or the signature does not verify, reject the checkpoint.
5. Prove append-only. If the new tree size is smaller than the one you saved, fail. If it is equal, the root hashes must match. If it is larger, verify the RFC 9162 consistency proof from your saved size and root hash to the new size and root hash.
6. Prove each event is included. Read every Access Transparency event the Activity Feed serves. For each new one, rebuild its [leaf](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#how-an-event-becomes-a-leaf), hash it, and fetch its [inclusion proof](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#fetch-an-inclusion-proof). Walk the audit path from your leaf hash at the event's index up to the checkpoint's root hash. A mismatch means the event you were served is not the event the log committed. The proof response can carry a different checkpoint from the one you hold. Link it into your history with a consistency proof before you verify anything against it.
7. Re-check what you saw before. Whenever you read an event again, it must be served with the same index and the same leaf bytes as when you verified it. No event may lose the index it had, and while you are enrolled no event may newly appear without one. The events served without an index on your first run are your pre-log history. A run that re-reads only recent events re-checks only those. To re-check older ones, verify the copies you kept (step 8) again.
8. Save the checkpoint you verified and a record of each event you verified. They are your evidence and your starting point for the next run.

### Verify with axt-verify

[`axt-verify`](https://github.com/anthropics/axt-verify) is Anthropic's open-source verifier for this log. It is a single Go binary that you run on your own infrastructure. Each release has exactly one log signing key from [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints) built in, so it never asks the API which key to trust. When Anthropic rotates the key, you upgrade to the release that carries the new one on the switch date. `axt-verify` derives your origin from the organization UUID you pass with `--org`, which is the one you took from the Console in [Before you begin](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#before-you-begin). It rejects any checkpoint whose origin line differs.

Install it with Go 1.26 or newer. It reads your Compliance Access Key from the `ANTHROPIC_COMPLIANCE_ACCESS_KEY` environment variable, never from a flag or a file. The `run` command is the one to schedule:

```bash
go install github.com/anthropics/axt-verify/cmd/axt-verify@latest

export ANTHROPIC_COMPLIANCE_ACCESS_KEY="<your Compliance Access Key>"
axt-verify --org 25f6429a-3293-49bf-afed-cb312911554b \
  --state /var/lib/axt-verify/25f6429a-3293-49bf-afed-cb312911554b.state \
  run
```

Each `run` fetches the latest checkpoint and verifies its signature and origin line. It then proves the log is an append-only extension of the checkpoint the previous run saved. Next it pages through the Access Transparency events on your Activity Feed. It starts seven days (by `created_at`) before the newest event the previous run read, so that events listed late or out of order are still picked up. It rebuilds each event's leaf, verifies an inclusion proof for it, and compares any event it verified before against what it recorded then. Finally, it saves the new checkpoint and its progress to the `--state` file, which the next run starts from. Run it at least daily. Hourly is reasonable. With a parent-organization key, run one copy per child organization, each with its own `--org` and `--state` file. Each child organization's UUID also comes from the Claude Console, not from the Compliance API responses you are verifying. Find it on the child organization's **Settings > Organization** page or in your parent organization's list of organizations in the Console. `axt-verify checkpoint` does only the checkpoint and append-only steps. `axt-verify events FILE` verifies events you already hold, such as an auditor's sample or your own export. It proves that each event in the file is still committed in the log under the current checkpoint. It does not read the feed or touch the state file.

One limit follows from that window: `run` re-reads only the last seven days of events, so it re-checks recently served events (step 7), not your whole history. Keep the events you export (see [Keep your own checkpoint archive](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#keep-your-own-checkpoint-archive)). `axt-verify events FILE` proves at any later date that those copies are still committed in the log, but it does not re-read the feed. To detect an older event removed from or rewritten on the feed, re-export that range from the Activity Feed and compare it with the copies you kept. You can also verify the re-export itself with `axt-verify events FILE`. The seven-day overlap is longer than the feed's two-business-day delivery time, so a late-arriving event still falls inside a later run's window. `--overlap` changes the duration if you need to.

If you need your own implementation instead, follow the preceding checklist with a tlog-tiles library that supports ECDSA note keys.

### Interpret the result

`axt-verify` prints your origin, the tree size and root hash of the checkpoint it verified, the tree size the append-only check started from, and a count of events by outcome. Pass `--json` to get the same report as one JSON object per line. Each event has one of four outcomes:

* **Verified:** the leaf rebuilt from the served event is committed at the event's index in the signed log.
* **Pending:** the event's index is beyond the latest published checkpoint. This is normal for a short time after an event appears. In `run`, `axt-verify` remembers the event, verifies it on a later run once a checkpoint covers it, and fails it if that takes longer than 24 hours. `events FILE` has no later run to settle it, so it waits up to a minute for a covering checkpoint to be published. If none arrives, it reports the event as not yet covered and ends with exit status `3`. Run it again later. If `events FILE` reports the same event as not yet covered on two runs at least a day apart, treat it as a verification failure and escalate as for exit status `1`.
* **Not logged:** the event was served without an index. An event is served without `transparency_log_leaf_index` only while your organization is not enrolled in Access Transparency, or when it was recorded before your organization's log was created (see [The `transparency_log_leaf_index` field on Activity Feed events](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#the-transparency-log-leaf-index-field-on-activity-feed-events)). `axt-verify` reports such events as not logged and does not fail the run on them. An index-less event is not expected when it is dated after your log was created and falls inside a period when you were enrolled. Review the not-logged list in the run's summary or `--json` output rather than relying on the exit status alone.
* **Failed:** see exit status `1`.

The exit status tells your scheduler what happened:

* **`0`:** Nothing failed. Not-logged events are reported, not failed, and so are pending events in `run`.

* **`1`:** A verification failure. This is a security finding, not a transient error. Keep the state file and the output, and report it to your Anthropic account representative or [Anthropic support](https://support.claude.com). The causes are:

  * A checkpoint with the wrong origin, or a signature that does not verify under the key built into your `axt-verify` release. Compare the `key_hash` on the failing checkpoint's signature line with [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints). A key listed there with a switch date you have not upgraded for means you need the matching release. A key not listed there is a security finding, whatever release you run. On this failure `axt-verify` prints the key hash of every signature on the served checkpoint and the key hash of the key it trusts, as eight hex digits each. That output is enough to make the comparison.
  * A checkpoint that is not a well-formed signed note, for example one whose root hash is not 32 bytes.
  * A log that shrank, or that cannot prove it extends the checkpoint you saved. The output then carries both checkpoints and the proof, so the evidence stands on its own.
  * Two signed checkpoints for the same tree size with different root hashes. The output carries both checkpoints.
  * A checkpoint file passed with `--from` whose signature does not verify under the key built into your `axt-verify` release, or a `--from` or `--from-trusted` file whose origin is not yours. For an archive signed before a key rotation, see [Keep your own checkpoint archive](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#keep-your-own-checkpoint-archive).
  * An inclusion proof that does not reproduce the signed root hash for the event you were served.
  * An event inside the run's window served differently from how an earlier run recorded it: different leaf bytes, a different index, or no index where it had one.
  * An event still pending 24 hours after the run first saw it.
  * A refused inclusion proof (`400`, `401`, or `403`) for an event the feed served you.
  * An inclusion proof returned for a different `leaf_index` from the one requested.
  * In `events FILE`, an event at an index the latest checkpoint already covered when the check began, for which no inclusion proof is served before the wait runs out.
  * An event whose `organization_uuid` is not the organization UUID you passed with `--org`. When a parent organization runs `events FILE` on an export that covers several child organizations, every other organization's event fails this way, so split the export by organization first and verify each part with its own `--org`.
  * The same activity `id` at two different indices, or twice at one index with different content, within one run or one `events FILE` input.
  * An event whose leaf cannot be rebuilt: for example, a documented field that is not a string, a field name that appears twice, or a `type` that is missing or is an unrecognized variant of an Access Transparency type. `events FILE` skips rows of other activity types and does not fail them.

* **`2`:** A usage or configuration error. The causes are:

  * A missing or malformed flag.
  * No `ANTHROPIC_COMPLIANCE_ACCESS_KEY`.
  * A key the API rejects (`401` or `403`) before any checkpoint has verified.
  * A state file that cannot be read or belongs to another origin.

* **`3`:** The run could not complete. In `run`, what had already been verified is saved to the state file. Run again. The causes are:

  * An event in `events FILE` whose index no published checkpoint covered within the wait. For such an event the **Pending** outcome says when to stop re-running and escalate.
  * Network errors, rate limiting, or server errors that outlasted the retries.
  * An unexpected response.
  * A state or `--save` file that could not be written.

  An exit status `3` with `404` responses is expected until Anthropic has recorded a first Access Transparency event for your organization, because every transparency log endpoint returns `404` until that event creates the log. Escalate if the transparency log endpoints still return `404` more than a few days after your Activity Feed first shows an Access Transparency event, whether or not that event carries a `transparency_log_leaf_index`. That combination is not expected. Once a run has succeeded, escalate an exit status `3` that persists.

### Keep your own checkpoint archive

The strongest evidence you can hold is your own record of what the log said on a given day. `axt-verify --save FILE` writes the checkpoint a run verified, verbatim, and `--from FILE` on a later run makes the log prove it still extends that checkpoint. Archive a saved checkpoint in storage you control, for example daily. Months later, a [consistency proof](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#fetch-a-consistency-proof) from that archived checkpoint's tree size must still lead to whatever checkpoint the log serves, or verification fails. Earlier keys stay listed in the [verifier key set](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys) after a planned rotation, so an archived checkpoint keeps verifying. With `axt-verify`, if the key that signed an archived checkpoint has since rotated out, pass that archive with `--from-trusted` instead of `--from`. Keep the events too. The Access Transparency events you export from the feed are valid input to `axt-verify events FILE`, which proves at any later date that those copies are still committed in the log under its current checkpoint. Because `events FILE` does not re-read the feed, your kept export is also the reference you compare a later re-export of the same range against.

## Frequently asked questions

<AccordionGroup>
  <Accordion title="Do I have to verify the transparency log?">
    No. Anthropic maintains the log for your organization whether anyone verifies it. Verification is how you check the log for yourself. An auditor can verify a sample of events you hand them with the same steps, given an API key with the Activity Feed scope.
  </Accordion>

  <Accordion title="Why did an inclusion proof return 404 for an event I was just served?">
    The event was served moments before a checkpoint covering its position was published. A covering checkpoint follows shortly, so retry after a short delay. An event whose proof is still unavailable a day later is the anomaly to escalate.
  </Accordion>

  <Accordion title="What happens when Anthropic rotates the signing key?">
    Planned rotations are announced in [Published key fingerprints](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#published-key-fingerprints) at least 30 days ahead, with a switch date. On the switch date Anthropic starts signing with the new key and publishes the `axt-verify` release that carries it. On the same date Anthropic re-issues every organization's latest checkpoint under the new key, even for a log that has not grown. Each `axt-verify` release carries one key, so upgrade on the switch date. Running the old release after the switch fails with exit status `1`, and so does running the new release before it. Either failure clears once you run the matching release. Checkpoints you saved under the old key stay valid starting points, because the append-only proof from a saved checkpoint to a new one does not depend on which key signed the old one. The new key appears at the front of the [verifier key set](https://platform.claude.com/docs/en/manage-claude/access-transparency-log#read-the-verifier-keys) and earlier keys stay listed. Checkpoints you already verified or archived therefore keep verifying against that set. A verifier of your own that pins the published fingerprints needs the new fingerprint, with its switch date, added before that date. A verifier that holds the key set locally re-fetches it when it meets a signature whose key hash it does not hold. A checkpoint commits to the whole history. Once one checkpoint signed by the new key verifies, and a consistency proof from your saved checkpoint leads to it, every earlier entry is re-established as well.
  </Accordion>

  <Accordion title="Can I compute proofs myself instead of calling the proof endpoints?">
    Yes. Hash tiles are the primary interface, and a tlog-tiles client that supports ECDSA note keys can compute inclusion and consistency proofs from them. The proof endpoints are a convenience. A generic client needs a thin wrapper to send the `x-api-key` header and, for a parent-organization key, the `organization_id` parameter.
  </Accordion>

  <Accordion title="What if my organization stops using Access Transparency?">
    Nothing is deleted. Your log stays readable and verifiable through the same endpoints, so keep verifying it as before. If your organization enables Access Transparency again later, the same log continues, and consistency proofs span the gap.
  </Accordion>

  <Accordion title="Can I verify all of my child organizations with one key?">
    Yes. A parent-organization key reads any enrolled child organization's log by passing `organization_id`. Each child organization has its own log, origin, and saved checkpoint. Run one verification per child organization, each with its own state.
  </Accordion>
</AccordionGroup>

## Related resources

* [Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency)
* [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)
* [Compliance API overview](https://platform.claude.com/docs/en/manage-claude/compliance-api)
* [Errors](https://platform.claude.com/docs/en/manage-claude/compliance-errors)
* [axt-verify](https://github.com/anthropics/axt-verify), Anthropic's open-source verifier for the transparency log
* [C2SP tlog-tiles](https://c2sp.org/tlog-tiles) and [C2SP signed note](https://c2sp.org/signed-note), the wire formats for tiles, entry bundles, and checkpoints
* [RFC 9162](https://www.rfc-editor.org/rfc/rfc9162), the Merkle tree, inclusion proof, and consistency proof algorithms
* [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785), the JSON Canonicalization Scheme used for leaves
