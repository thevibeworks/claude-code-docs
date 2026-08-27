# Federation

## Federation › Issuers

### Create Federation Issuer

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

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Body parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### List Federation Issuers

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `data: array of BetaFederationIssuer`

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

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

### Get Federation Issuer

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

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

### Update Federation Issuer

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer to update.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Body parameters

- `check_jti: optional boolean or null`

  Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

- `issuer_url: optional string or null`

  Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

  minLength: 1

- `jwks: optional BetaJWKSDiscovery or BetaJWKSExplicitURL or BetaJWKSInline or null`

  Replaces the entire JWKS configuration.

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

- `jwks_polling_disabled: optional boolean or null`

  Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

- `max_jwt_lifetime_seconds: optional number or null`

  Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  maximum: 176400, exclusiveMinimum: 0

- `name: optional string or null`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

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

### Archive Federation Issuer

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Path parameters

- `federation_issuer_id: string`

  ID of the federation issuer to archive.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

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

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

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

## Federation › Rules

### Create Federation Rule

**POST** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist
in the same organization; invalid references are rejected with a 400
error. The workspace reference is validated. Membership is not checked
at rule creation: token exchange resolves a single enabled workspace per
call and is rejected unless the target service account is a member of
that workspace (it is implicitly a member of the default workspace).
Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite,
Terraform Cloud, Google) must constrain tenant identity via an
identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). OAuth callers may only
manage rules whose `oauth_scope` is `workspace:developer` or
`workspace:inference`; other scopes require a Console session.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Body parameters

- `issuer_id: string`

  Tagged ID of the federation issuer.

- `match: BetaFederationRuleMatch`

  Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string or null`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: optional map[string] or null`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string or null`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: optional string or null`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: string`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `oauth_scope: string`

  Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: BetaServiceAccountTarget`

  Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

  - `service_account_name: optional string or null`

    Service account's display name at read time. Ignored on writes.

- `applies_to_all_workspaces: optional boolean`

  When true, enable this rule for every workspace in the org (including workspaces created later).

- `attributes: optional map[string] or null`

  CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string or null`

  Optional free-text description.

  maxLength: 2000

- `token_lifetime_seconds: optional number`

  Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: optional string or null`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_id": "issuer_id",
          "match": {},
          "name": "x",
          "oauth_scope": "x",
          "target": {
            "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
            "type": "service_account"
          }
        }'
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### List Federation Rules

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Query parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

  default: false

- `issuer_id: optional string`

  Filter to rules referencing this federation issuer.

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `data: array of BetaFederationRule`

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

- `next_page: string or null`

  Opaque cursor for the next page, or null if no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Rule

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Update Federation Rule

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule to update.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Body parameters

- `applies_to_all_workspaces: optional boolean or null`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: optional map[string] or null`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: optional string or null`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `match: optional BetaFederationRuleMatch or null`

  Does the incoming JWT qualify?

  All populated fields must pass; omitted fields are skipped. At least one
  of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
  or `condition` is required; `audience` alone is not sufficient.

  - `audience: optional string or null`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: optional map[string] or null`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: optional string or null`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: optional string or null`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: optional string or null`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `oauth_scope: optional string or null`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: optional BetaServiceAccountTarget or null`

  Bind to a fixed service account by ID.

  - `service_account_id: string`

    Tagged ID of the service account to mint tokens for.

  - `type: "service_account"`

  - `service_account_name: optional string or null`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: optional number or null`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: optional string or null`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Archive Federation Rule

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule to archive.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `BetaFederationRule object`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `id: string`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: boolean`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: string or null`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: map[string] or null`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: string`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: string or null`

    Optional free-text description.

  - `issuer_id: string`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: string or null`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: optional string or null`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: optional map[string] or null`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: optional string or null`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: optional string or null`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: string`

    Admin-chosen slug identifier.

  - `oauth_scope: string`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `service_account_id: string`

      Tagged ID of the service account to mint tokens for.

    - `type: "service_account"`

    - `service_account_name: optional string or null`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: number`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `type: "federation_rule"`

    default: federation_rule

  - `updated_at: string`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: string or null`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: string or null`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: array of string`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Federation › Rules › Workspaces

### Add Federation Rule Workspace

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Body parameters

- `workspace_id: string`

  Tagged ID of the workspace to enable this rule for.

#### Returns

- `BetaFederationRuleWorkspace object`

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_id": "workspace_id"
        }'
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

### List Federation Rule Workspaces

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

#### Query parameters

- `limit: optional number`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `data: array of BetaFederationRuleWorkspace`

  - `created_at: string`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: string`

    Tagged ID of the federation rule.

  - `type: "federation_rule_workspace"`

    default: federation_rule_workspace

  - `workspace_id: string`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: string or null`

    Workspace display name. Populated when listing; null in the enable response.

- `next_page: string or null`

  Opaque cursor for the next page; null when there are no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Federation Rule Workspace

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Path parameters

- `federation_rule_id: string`

  ID of the federation rule.

- `workspace_id: string`

  ID of the workspace to disable for.

#### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

#### Returns

- `federation_rule_id: string`

  Tagged ID of the federation rule.

- `type: "federation_rule_workspace_deleted"`

  default: federation_rule_workspace_deleted

- `workspace_id: string`

  Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```bash
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```
