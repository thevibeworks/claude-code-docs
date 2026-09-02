# Create Federation Issuer

**POST** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Register an OIDC issuer that Anthropic will trust for workload identity
federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and
takes one of three shapes selected by `type`: `discovery` (resolve keys
through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS
URL), or `inline` (provide a static key set). When `jwks.type` is
`discovery` and no `discovery_base` is set, the issuer URL must be
publicly reachable over HTTPS so Anthropic can fetch the discovery
document; for `explicit_url` and `inline` modes the issuer URL is only
matched as the JWT's `iss` claim and is not fetched.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

## Body parameters

- `issuer_url: string`

  The `iss` claim value to match against.

  minLength: 1

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

  How signing keys are obtained. Defaults to OIDC discovery.

  - `BetaJWKSDiscovery object`

    JWKS via the issuer's OIDC discovery document.

    - `type: "discovery"`

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

    - `discovery_base: optional string or null`

      Set when the discovery URL differs from `issuer_url`.

  - `BetaJWKSExplicitURL object`

    JWKS fetched from a fixed endpoint.

    - `type: "explicit_url"`

    - `url: string`

      JWKS endpoint.

      minLength: 1

    - `ca_cert_pem: optional string or null`

      Optional custom CA (PEM) for TLS verification of the JWKS fetch.

      maxLength: 8192

  - `BetaJWKSInline object`

    JWKS supplied directly; no network fetch.

    - `keys: array of map[unknown]`

      Inline JWK objects.

      minItems: 1

    - `type: "inline"`

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

## Returns

- `BetaFederationIssuer object`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `id: string`

    Tagged ID of the federation issuer.

  - `archived_at: string or null`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `check_jti: boolean`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `created_at: string`

    When this issuer was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `issuer_url: string`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `jwks: BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline`

    How signing keys are obtained for signature verification.

    - `BetaJWKSDiscovery object`

      JWKS via the issuer's OIDC discovery document.

      - `type: "discovery"`

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `discovery_base: optional string or null`

        Set when the discovery URL differs from `issuer_url`.

    - `BetaJWKSExplicitURL object`

      JWKS fetched from a fixed endpoint.

      - `type: "explicit_url"`

      - `url: string`

        JWKS endpoint.

        minLength: 1

      - `ca_cert_pem: optional string or null`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `BetaJWKSInline object`

      JWKS supplied directly; no network fetch.

      - `keys: array of map[unknown]`

        Inline JWK objects.

        minItems: 1

      - `type: "inline"`

  - `jwks_polling_disabled_at: string or null`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `max_jwt_lifetime_seconds: number`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `name: string`

    Admin-chosen slug identifier.

  - `poll_status: BetaFederationIssuerPollStatus or null`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `consecutive_failures: number`

      Consecutive fetch failures since the last success.

    - `last_fetched_at: string or null`

      When the last successful fetch completed.

      format: date-time

    - `next_poll_at: string or null`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `type: "federation_issuer"`

    default: federation_issuer

  - `updated_at: string`

    When this issuer was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_url": "x",
          "name": "x"
        }'
```

### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```
