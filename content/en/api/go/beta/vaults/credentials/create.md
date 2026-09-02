# Create Credential

`client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (*BetaManagedAgentsCredential, error)`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

## Parameters

- `vaultID string`

- `params BetaVaultCredentialNewParams`

  - `Auth param.Field[BetaVaultCredentialNewParamsAuthUnion]`

    Body param: Authentication details for creating a credential.

    - `type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}`

      Parameters for creating an MCP OAuth credential.

      - `AccessToken string`

        OAuth access token.

        minLength: 1, maxLength: 8192

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `Type BetaManagedAgentsMCPOAuthCreateParamsType`

      - `ExpiresAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `Refresh BetaManagedAgentsMCPOAuthRefreshParamsResp Optional`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `ClientID string`

          OAuth client ID.

          minLength: 1, maxLength: 1024

        - `RefreshToken string`

          OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

          - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

          - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

        - `Resource string Optional`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `Scope string Optional`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}`

      Parameters for creating a static bearer token credential.

      - `Token string`

        Static bearer token value.

        minLength: 1, maxLength: 8192

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `Type BetaManagedAgentsStaticBearerCreateParamsType`

    - `type BetaManagedAgentsEnvironmentVariableCreateParamsResp struct{…}`

      Parameters for creating an environment variable credential.

      - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

        - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

      - `SecretName string`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `SecretValue string`

        Secret value. Write-only; never returned in responses.

        minLength: 1, maxLength: 4096

      - `Type BetaManagedAgentsEnvironmentVariableCreateParamsType`

      - `InjectionLocation BetaManagedAgentsInjectionLocationParamsResp Optional`

        Where in the outbound request the secret value may be substituted.

        - `Body bool Optional`

          Substitute when the placeholder appears in the request body.

        - `Header bool Optional`

          Substitute when the placeholder appears in a request header value.

  - `DisplayName param.Field[string] Optional`

    Body param: Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

## Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

      - `ExpiresAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse Optional`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

        - `Resource string Optional`

          OAuth resource indicator.

        - `Scope string Optional`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string Optional`

    Human-readable name for the credential.

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.New(
		context.TODO(),
		"vlt_011CZkZDLs7fYzm1hXNPeRjv",
		anthropic.BetaVaultCredentialNewParams{
			Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
				OfStaticBearer: &anthropic.BetaManagedAgentsStaticBearerCreateParams{
					Token:        "bearer_exampletoken",
					MCPServerURL: "https://example-server.modelcontextprotocol.io/sse",
					Type:         anthropic.BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer,
				},
			},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
```

### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```
