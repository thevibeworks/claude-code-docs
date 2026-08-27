> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration changelog

> Managed configuration keys by the Claude Desktop release they first shipped in

Configuration keys by Claude Desktop release. Each section lists keys added in that release, with the MDM key name (for plist/registry deployment) and the equivalent JSON shape (for local-file or bootstrap remote configuration).

<Update label="v1.37937.3" description="2026-08-26">
  No configuration changes in this release.
</Update>

<Update label="v1.37937.2" description="2026-08-26">
  No configuration changes in this release.
</Update>

<Update label="v1.37937.1" description="2026-08-25">
  No configuration changes in this release.
</Update>

<Update label="v1.37937.0" description="2026-08-25">
  <div className="cfg-keys">
    | MDM key                                                                                                        | Type       | Description                          |
    | -------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------ |
    | [`inferenceModelPricingEnabled`](/docs/third-party/claude-desktop/configuration#inferencemodelpricingenabled)       | `boolean`  | Show estimated cost                  |
    | [`inferenceModelPricingMultiplier`](/docs/third-party/claude-desktop/configuration#inferencemodelpricingmultiplier) | `number`   | Price multiplier                     |
    | [`inferenceModelPricing`](/docs/third-party/claude-desktop/configuration#inferencemodelpricing)                     | `object[]` | Model pricing                        |
    | [`userPluginMarketplacesEnabled`](/docs/third-party/claude-desktop/configuration#userpluginmarketplacesenabled)     | `boolean`  | Allow user-added plugin marketplaces |
    | [`userPluginUploadsEnabled`](/docs/third-party/claude-desktop/configuration#userpluginuploadsenabled)               | `boolean`  | Allow user-added plugins             |
    | [`mcpToolTimeoutSec`](/docs/third-party/claude-desktop/configuration#mcptooltimeoutsec)                             | `integer`  | MCP tool call timeout                |
    | [`skipWebFetchPreflight`](/docs/third-party/claude-desktop/configuration#skipwebfetchpreflight)                     | `boolean`  | Skip WebFetch domain check           |
    | [`organizationInstructions`](/docs/third-party/claude-desktop/configuration#organizationinstructions)               | `string`   | Organization instructions            |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "models": {
      "pricing": {
        "enabled": "<boolean>",
        "multiplier": "<number>",
        "models": [
          {
            "name": "<string>",
            "inputPerMtok": "<number>",
            "outputPerMtok": "<number>",
            "cacheReadPerMtok": "<number>",
            "cacheWritePerMtok": "<number>"
          }
        ]
      }
    },
    "plugins": {
      "userPluginMarketplacesEnabled": "<boolean>",
      "userPluginUploadsEnabled": "<boolean>"
    },
    "mcp": {
      "toolTimeoutSec": "<integer>"
    },
    "workspace": {
      "skipWebFetchPreflight": "<boolean>",
      "organizationInstructions": "<string>"
    }
  }
  ```

  **Changed:**

  * `builtinToolPolicy` accepts argument-scoped Claude Code permission rules such as `Bash(curl *)` or `Edit(**/*.env)` as keys, in addition to bare tool names; `WebSearch` and `WebFetch` take the bare name only, and a key that is not a usable rule is dropped with a configuration error. Deploy argument-scoped entries once your whole fleet is on this release: an older build drops an argument-scoped `ask` entry as an unknown tool, so that tool runs without a prompt.
</Update>

<Update label="v1.34493.1" description="2026-08-21">
  No configuration changes in this release.
</Update>

<Update label="v1.34493.0" description="2026-08-20">
  No configuration changes in this release.
</Update>

<Update label="v1.32885.1" description="2026-08-18">
  <div className="cfg-keys">
    | MDM key                                                                                      | Type     | Description                     |
    | -------------------------------------------------------------------------------------------- | -------- | ------------------------------- |
    | [`bootstrapHeaders`](/docs/third-party/claude-desktop/configuration#bootstrapheaders)             | `object` | Bootstrap request headers       |
    | [`bootstrapHeadersHelper`](/docs/third-party/claude-desktop/configuration#bootstrapheadershelper) | `string` | Bootstrap headers helper script |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "bootstrap": {
      "headers": "<object>",
      "headersHelper": "<string>"
    }
  }
  ```

  **Changed:**

  * `managedMcpServers[].oauth` accepts a new `mode` value, `hosted`: the app signs in to that MCP server with an Anthropic-hosted client identity (Anthropic vouches for the client on each token request) instead of a client you register yourself, pinned to the exact issuer URL(s) you list in `authorizationServer`; it requires the Claude.ai sign-in and is available once the hosted signer is enabled for your organization.
</Update>

<Update label="v1.32352.1" description="2026-08-18">
  No configuration changes in this release.
</Update>

<Update label="v1.32352.0" description="2026-08-17">
  <div className="cfg-keys">
    | MDM key                                                                                                             | Type      | Description                                                                                                                                                                                                                        |
    | ------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | [`claudeAiImport.exportEnabled`](/docs/third-party/claude-desktop/configuration#claudeaiimport)                          | `boolean` | New subfield: lets users export this computer's chats, Cowork tasks, and Code sessions from Settings > Import & export as a zip that another install can import; no effect unless `enabled` is `true` (default `false`).           |
    | [`allowedPluginMarketplaces[].manifestSha256`](/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces) | `string`  | New subfield (beta): SHA-256 of the exact hosted `marketplace.json` a `url` marketplace may serve; required when `installationPreference` is `auto_install` or `required`, and a served manifest with any other digest is refused. |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "claudeAiImport": {
      "exportEnabled": "<boolean>"
    },
    "plugins": {
      "marketplaces": [
        {
          "source": "url",
          "url": "<string>",
          "manifestSha256": "<string>",
          "credentialKind": "<anonymous|userGit|credentialHelper|inferenceCredential>"
        }
      ]
    }
  }
  ```

  **Changed:**

  * **Breaking:** Managed-config URL settings now reject values that embed credentials (`https://user:password@host…`). Configurations that relied on this fail to load until the credentials are removed; use `bootstrapHeaders` / `bootstrapHeadersHelper` (available from 1.32885.1) to send authentication instead.
  * `allowedPluginMarketplaces[].source` (beta) accepts a new `url` value: a hosted `marketplace.json` whose plugins are zip archives, fetched over HTTPS with no git on the device; set `url` to the manifest address (`repo`, `ref`, and `path` do not apply).
  * `allowedPluginMarketplaces[].credentialKind` (beta) accepts a new `inferenceCredential` value, for `url` marketplaces on the inference gateway's own origin: fetches carry the same bearer credential the app already sends the gateway for inference.
</Update>

<Update label="v1.30096.5" description="2026-08-14">
  No configuration changes in this release.
</Update>

<Update label="v1.30096.1" description="2026-08-13">
  <div className="cfg-keys">
    | MDM key                                                                                           | Type     | Description                                                                                                                                                                            |
    | ------------------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | [`otlpAuthMode`](/docs/third-party/claude-desktop/configuration#otlpauthmode)                          | `enum`   | Collector authentication                                                                                                                                                               |
    | [`otlpHeadersHelper`](/docs/third-party/claude-desktop/configuration#otlpheadershelper)                | `string` | OpenTelemetry headers helper script                                                                                                                                                    |
    | [`inferenceGatewayOidc.resource`](/docs/third-party/claude-desktop/configuration#inferencegatewayoidc) | `string` | New subfield: RFC 8707 resource indicator sent on gateway sign-in and token refresh so the IdP audience-restricts the access token to the gateway; leave unset for Microsoft Entra ID. |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "otlp": {
      "authMode": "<none|inference-credential>",
      "headersHelper": "<string>"
    },
    "inference": {
      "credential": {
        "oidc": {
          "resource": "<string>"
        }
      }
    }
  }
  ```

  **Changed:**

  * `inferenceBedrockBaseUrl` and `inferenceVertexBaseUrl`: only affects users who entered the bootstrap server URL themselves (in Settings or a local config file). Those users are now asked once to allow a Bedrock or Vertex endpoint that server delivers (and again if it changes) before it takes effect, the same `trustBootstrapDelivery` consent prompt `inferenceGatewayBaseUrl` already shows; the provider's default endpoint is used until they allow it. Managed deployments (bootstrap URL set by device management, or `trustBootstrapDelivery: true`) see no change.
</Update>

<Update label="v1.28929.0" description="2026-08-11">
  <div className="cfg-keys">
    | MDM key                                                                                     | Type      | Description                                                                                                          |
    | ------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------- |
    | [`modelPrefer1mContext`](/docs/third-party/claude-desktop/configuration#modelprefer1mcontext)    | `boolean` | Default to 1M context                                                                                                |
    | [`claudeAiImport.enabled`](/docs/third-party/claude-desktop/configuration#claudeaiimport)        | `boolean` | New subfield: turns history import on; the banner and import actions stay off until set to `true` (default `false`). |
    | [`claudeAiImport.bannerBehavior`](/docs/third-party/claude-desktop/configuration#claudeaiimport) | `enum`    | New subfield: when the import banner appears: `off` (default), `detect`, or `show`.                                  |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "models": {
      "prefer1mContext": "<boolean>"
    },
    "claudeAiImport": {
      "enabled": "<boolean>",
      "bannerBehavior": "<off|detect|show>"
    }
  }
  ```

  **Changed:**

  * `inferenceGatewayBaseUrl` delivered by a bootstrap server now goes through the `trustBootstrapDelivery` consent prompt: unless the bootstrap URL came from device management or `trustBootstrapDelivery` is `true`, each user is asked once to allow the address, and again if it changes, before it takes effect.
</Update>

<Update label="v1.26832.0" description="2026-08-06">
  <div className="cfg-keys">
    | MDM key                                                                                               | Type      | Description                                                                             |
    | ----------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------- |
    | [`updateViaUpdatesHost`](/docs/third-party/claude-desktop/configuration#updateviaupdateshost)              | `boolean` | Check for updates on releases.claude.com                                                |
    | [`allowedWorkspaceFolders[].mode`](/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) | `enum`    | New subfield: `ro` makes the folder read-only in Cowork; Code enforces file tools only. |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "autoUpdate": {
      "viaUpdatesHost": "<boolean>"
    }
  }
  ```

  `trustBootstrapLocalExec` was renamed to `trustBootstrapDelivery`; the previous name is still accepted.
</Update>

<Update label="v1.25927.0" description="2026-08-04">
  <div className="cfg-keys">
    | MDM key                                                                                                          | Type      | Description                              |
    | ---------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------- |
    | [`inferenceGatewayOidcAuthFlow`](/docs/third-party/claude-desktop/configuration#inferencegatewayoidcauthflow)         | `enum`    | Gateway sign-in flow                     |
    | [`inferenceVertexWorkforceAuthFlow`](/docs/third-party/claude-desktop/configuration#inferencevertexworkforceauthflow) | `enum`    | Workforce Identity sign-in flow          |
    | [`trustBootstrapLocalExec`](/docs/third-party/claude-desktop/configuration#trustbootstrapdelivery)                    | `boolean` | Trust bootstrap-delivered local commands |
    | [`skillCreationEnabled`](/docs/third-party/claude-desktop/configuration#skillcreationenabled)                         | `boolean` | Allow user-created skills                |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "authFlow": "<browser|broker>"
      }
    },
    "bootstrap": {
      "trustBootstrapLocalExec": "<boolean>"
    },
    "workspace": {
      "skillCreationEnabled": "<boolean>"
    }
  }
  ```

  **Changed:**

  * `claudeAiImport`, `deploymentDisplayName`, and `deploymentDisplaySubtitle` now accept values from MDM and a local configuration file as well as a bootstrap server, and `disableDeepLinkRegistration`, `microsoftAuthBroker`, `userContentRendererUrl`, `inferenceFoundryTenantId`, `inferenceFoundryClientId`, `inferenceCredentialHelper` (with its TTL, timeout, and silent-refresh keys), `inferenceBedrockProfile`, `inferenceBedrockAwsDir`, `inferenceBedrockAwsCliPath`, and `inferenceVertexCredentialsFile` can now be delivered by a bootstrap server. The keys that name a local executable go through the `trustBootstrapLocalExec` consent prompt.
  * `managedMcpServers` gains a built-in `github` server: set `server` to `github` and supply your own GitHub OAuth app client ID with the device flow enabled. The new `host`, `toolsets`, and `readOnly` subfields point the connector at a GitHub Enterprise Server instance, choose which toolsets load, and offer read tools only.
  * `managedMcpServers[].oauth.authFlow` is a new subfield that lets a managed connector sign in through the operating system's Microsoft Entra account broker on Windows and macOS, so Conditional Access policies that require a managed device no longer block it. Devices without a broker keep using browser sign-in.
  * `enduserAttribution` is renamed to the corrected spelling `endUserAttribution`. The previous spelling is still accepted and now records a configuration warning.
  * `organizationPluginsUrl` is deprecated and removed from the configuration reference. The key is still honored, but organization plugins are better configured with `allowedPluginMarketplaces`.
</Update>

<Update label="v1.24012.11" description="2026-08-03">
  No configuration changes in this release.
</Update>

<Update label="v1.24012.9" description="2026-07-24">
  <div className="cfg-keys">
    | MDM key                                                                                                        | Type      | Description                     |
    | -------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------- |
    | [`mcpPersistentAlwaysAllowEnabled`](/docs/third-party/claude-desktop/configuration#mcppersistentalwaysallowenabled) | `boolean` | Allow persistent tool approvals |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "mcp": {
      "persistentAlwaysAllowEnabled": "<boolean>"
    }
  }
  ```
</Update>

<Update label="v1.24012.0" description="2026-07-21">
  <div className="cfg-keys">
    | MDM key                                                                                      | Type      | Description                    |
    | -------------------------------------------------------------------------------------------- | --------- | ------------------------------ |
    | [`enduserAttribution`](/docs/third-party/claude-desktop/configuration#enduserattribution)         | `boolean` | End-user attribution           |
    | [`userContentRendererUrl`](/docs/third-party/claude-desktop/configuration#usercontentrendererurl) | `string`  | Artifact preview iframe origin |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "deploymentDisplayName": "<string>",
    "deploymentDisplaySubtitle": "<string>",
    "enduserAttribution": "<boolean>",
    "userContentRendererUrl": "<string>"
  }
  ```
</Update>

<Update label="v1.22209.3" description="2026-07-19">
  No configuration changes in this release.
</Update>

<Update label="v1.22209.0" description="2026-07-16">
  <div className="cfg-keys">
    | MDM key                                                                            | Type      | Description          |
    | ---------------------------------------------------------------------------------- | --------- | -------------------- |
    | [`otlpTracesEnabled`](/docs/third-party/claude-desktop/configuration#otlptracesenabled) | `boolean` | Export traces (beta) |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "otlp": {
      "tracesEnabled": "<boolean>"
    }
  }
  ```
</Update>

<Update label="v1.21459.3" description="2026-07-16">
  No configuration changes in this release.
</Update>

<Update label="v1.21459.0" description="2026-07-14">
  <div className="cfg-keys">
    | MDM key                                                                                                            | Type      | Description                                                                                                  |
    | ------------------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------ |
    | [`disableFeatureDiscovery`](/docs/third-party/claude-desktop/configuration#disablefeaturediscovery)                     | `boolean` | Hide feature announcements                                                                                   |
    | [`inferenceModels[].prefer1m`](/docs/third-party/claude-desktop/configuration#inferencemodels)                          | `boolean` | New subfield: make the 1M-context variant the default picker selection when this model is the default entry. |
    | [`managedMcpServers[].envHelper`](/docs/third-party/claude-desktop/configuration#managedmcpservers)                     | `string`  | New subfield: helper executable that prints environment variables as JSON for a managed stdio server.        |
    | [`managedMcpServers[].envHelperTtlSec`](/docs/third-party/claude-desktop/configuration#managedmcpservers)               | `integer` | New subfield: maximum age in seconds of a cached `envHelper` result (default 300).                           |
    | [`managedMcpServers[].headersHelperRefreshBufferSec`](/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: how many seconds before credential expiry the `headersHelper` re-runs (default 60).            |
    | [`toolSearchEnabled`](/docs/third-party/claude-desktop/configuration#toolsearchenabled)                                 | `boolean` | Enable tool search                                                                                           |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "featureDiscovery": {
      "disabled": "<boolean>"
    },
    "workspace": {
      "toolSearchEnabled": "<boolean>"
    }
  }
  ```

  **Changed:**

  * `chatTabEnabled` and `chatAdvancedFileAnalysisEnabled` are no longer Beta: the Chat tab and advanced file analysis are generally available. Availability and defaults are unchanged, and both remain opt-in.
  * `orgPluginSettings[].tools.permission` accepts a new `ask-session` value. In this release the value is accepted but behaves as `ask` (a prompt on every use); the once-per-session approval flow is not yet enabled.
</Update>

<Update label="v1.20186.9" description="2026-07-14">
  No configuration changes in this release.
</Update>

<Update label="v1.20186.0" description="2026-07-09">
  No configuration changes in this release.
</Update>

<Update label="v1.19367.0" description="2026-07-07">
  <div className="cfg-keys">
    | MDM key                                                                                                | Type      | Description                                                                       |
    | ------------------------------------------------------------------------------------------------------ | --------- | --------------------------------------------------------------------------------- |
    | [`inferenceFoundryAuthFlow`](/docs/third-party/claude-desktop/configuration#inferencefoundryauthflow)       | `enum`    | Entra ID sign-in flow                                                             |
    | [`microsoftAuthBroker`](/docs/third-party/claude-desktop/configuration#microsoftauthbroker)                 | `enum`    | Microsoft 365 native sign-in broker                                               |
    | [`managedMcpServers[].startupTimeoutSec`](/docs/third-party/claude-desktop/configuration#managedmcpservers) | `integer` | New subfield: maximum wait in seconds for the server to start and list its tools. |
  </div>

  **JSON (e.g. for non-MDM users or Bootstrap):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "authFlow": "<device-code|browser>"
      }
    },
    "authentication": {
      "microsoftAuthBroker": "<auto|disabled>"
    }
  }
  ```

  **Changed:**

  * `isDesktopExtensionEnabled` — default changed from `true` to `false`: Desktop Extensions (`.dxt`, `.mcpb`) no longer load unless explicitly enabled.
  * `allowedPluginMarketplaces` (beta) — can now be delivered per-user through the bootstrap server; previously MDM-only.
</Update>

<Update label="v1.18286.2" description="2026-07-07">
  No configuration changes in this release.
</Update>

<Update label="v1.18286.0" description="2026-07-02">
  **Removed:**

  * `disableDefaultPlugins` — third-party deployments always skip the default plugin marketplaces and standard deployments always include them, so the key no longer has an effect.
</Update>

<Update label="v1.17377.2" description="2026-07-01">
  No configuration changes in this release.
</Update>

<Update label="v1.17377.1" description="2026-06-30">
  <div className="cfg-keys">
    | MDM key                                                                                                                    | Type       | Description                                                                                                                              |
    | -------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
    | [`allowedPluginMarketplaces`](/docs/third-party/claude-desktop/configuration#allowedpluginmarketplaces)                         | `object[]` | Admin-configured plugin marketplace git URLs appear under the Directory's Organization tab. (MDM-only; not settable via bootstrap JSON.) |
    | [`inferenceVertexWorkforceOidc.omitOfflineAccess`](/docs/third-party/claude-desktop/configuration#inferencevertexworkforceoidc) | `boolean`  | New subfield: omit `offline_access` from the OIDC scope request.                                                                         |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "oidc": {
          "omitOfflineAccess": "<boolean>"
        }
      }
    }
  }
  ```
</Update>

<Update label="v1.15962.2" description="2026-06-30">
  No configuration changes in this release.
</Update>

<Update label="v1.15962.1" description="2026-06-26">
  No configuration changes in this release.
</Update>

<Update label="v1.15962.0" description="2026-06-25">
  <div className="cfg-keys">
    | MDM key                                                                                     | Type      | Description                                                              |
    | ------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------ |
    | [`otlpContentCapture`](/docs/third-party/claude-desktop/configuration#otlpcontentcapture)        | `enum[]`  | Content capture categories                                               |
    | [`disableBundledSkills`](/docs/third-party/claude-desktop/configuration#disablebundledskills)    | `boolean` | Disable bundled skills and workflows                                     |
    | [`managedMcpServers[].server`](/docs/third-party/claude-desktop/configuration#managedmcpservers) | `enum`    | Gained `"websearch"` — managed web search (Brave, Tavily, Exa or custom) |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "otlp": {
      "contentCapture": [
        "<userPrompts|assistantResponses|toolDetails|toolContent|rawApiBodies>"
      ]
    },
    "workspace": {
      "disableBundledSkills": "<boolean>"
    },
    "mcp": {
      "managedServers": [
        {
          "name": "Web search",
          "server": "websearch",
          "provider": "<brave|tavily|exa|custom>",
          "headers": { "<header-name>": "<string>" },
          "customUrl": "<string, provider=custom only>"
        }
      ]
    }
  }
  ```
</Update>

<Update label="v1.15200.0" description="2026-06-23">
  No configuration changes in this release.
</Update>

<Update label="v1.14271.0" description="2026-06-18">
  <div className="cfg-keys">
    | MDM key                           | Type      | Description              |
    | --------------------------------- | --------- | ------------------------ |
    | `chatAdvancedFileAnalysisEnabled` | `boolean` | Advanced file analysis   |
    | `inferenceSessionLifetimeSec`     | `integer` | Sign-in session lifetime |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "chatSurface": {
      "advancedFileAnalysis": "<boolean>"
    },
    "inference": {
      "sessionLifetimeSec": "<integer>"
    }
  }
  ```

  **Deprecated:**

  * `betaFeaturesEnabled` — Allow beta features (added and deprecated in this release)
</Update>

<Update label="v1.13576.0" description="2026-06-16">
  <div className="cfg-keys">
    | MDM key                      | Type      | Description    |
    | ---------------------------- | --------- | -------------- |
    | `chatTabEnabled`             | `boolean` | Allow Chat tab |
    | `inferenceBedrockAwsCliPath` | `string`  | AWS CLI path   |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "chatSurface": {
      "enabled": "<boolean>"
    },
    "inference": {
      "awsEnv": {
        "awsCliPath": "<string>"
      }
    }
  }
  ```
</Update>

<Update label="v1.12603.0" description="2026-06-11">
  <div className="cfg-keys">
    | MDM key                         | Type     | Description             |
    | ------------------------------- | -------- | ----------------------- |
    | `inferenceVertexOAuthLoginHint` | `string` | Vertex OAuth login hint |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "loginHint": "<string>"
      }
    }
  }
  ```
</Update>

<Update label="v1.10628.0" description="2026-06-03">
  <div className="cfg-keys">
    | MDM key                                         | Type      | Description                        |
    | ----------------------------------------------- | --------- | ---------------------------------- |
    | `inferenceVertexWorkforceAudience`              | `string`  | Workforce Identity audience        |
    | `inferenceVertexWorkforceUserProject`           | `string`  | Workforce Identity billing project |
    | `inferenceVertexWorkforceOidc`                  | `object`  | Workforce Identity IdP (OIDC)      |
    | `organizationPluginsUrl`                        | `string`  | Organization plugins endpoint      |
    | `autoModeEnabled`                               | `boolean` | Allow Auto mode                    |
    | `inferenceCredentialHelperSilentRefreshEnabled` | `boolean` | Re-run helper for silent refresh   |
    | `bootstrapEnabled`                              | `boolean` | Use bootstrap config               |
    | `bootstrapUrl`                                  | `string`  | Bootstrap config URL               |
    | `bootstrapOidc`                                 | `object`  | Bootstrap OIDC parameters          |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "audience": "<string>",
        "userProject": "<string>",
        "oidc": {
          "issuer": "<string>",
          "authorizationUrl": "<string>",
          "tokenUrl": "<string>",
          "clientId": "<string>",
          "scopes": "<string>",
          "redirectPort": "<integer>"
        },
        "silentRefreshEnabled": "<boolean>"
      }
    }
  }
  ```
</Update>

<Update label="v1.9659.0" description="2026-06-02">
  <div className="cfg-keys">
    | MDM key            | Type      | Description      |
    | ------------------ | --------- | ---------------- |
    | `coworkTabEnabled` | `boolean` | Allow Cowork tab |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "coworkSurface": {
      "enabled": "<boolean>"
    }
  }
  ```
</Update>

<Update label="v1.9255.0" description="2026-05-27">
  <div className="cfg-keys">
    | MDM key                    | Type     | Description                    |
    | -------------------------- | -------- | ------------------------------ |
    | `otlpDesktopLogLevel`      | `enum`   | Desktop telemetry export level |
    | `inferenceFoundryTenantId` | `string` | Entra ID tenant ID             |
    | `inferenceFoundryClientId` | `string` | Entra ID client ID             |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "otlp": {
      "desktopLogLevel": "<off|error|warn|info|debug>"
    },
    "inference": {
      "credential": {
        "tenantId": "<string>",
        "clientId": "<string>"
      }
    }
  }
  ```
</Update>

<Update label="v1.8555.0" description="2026-05-25">
  <div className="cfg-keys">
    | MDM key                   | Type   | Description     |
    | ------------------------- | ------ | --------------- |
    | `inferenceCredentialKind` | `enum` | Credential kind |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "kind": "<static|helper-script|interactive|vendor-profile>"
      }
    }
  }
  ```
</Update>

<Update label="v1.8089.0" description="2026-05-19">
  <div className="cfg-keys">
    | MDM key                               | Type      | Description                                                       |
    | ------------------------------------- | --------- | ----------------------------------------------------------------- |
    | `inferenceAnthropicApiKey`            | `string`  | Claude API key                                                    |
    | `inferenceCustomHeaders`              | `object`  | Custom inference headers (renamed from `inferenceGatewayHeaders`) |
    | `modelDiscoveryEnabled`               | `boolean` | Model discovery                                                   |
    | `orgPluginSettings`                   | `object`  | Organization plugin settings                                      |
    | `builtinToolPolicy`                   | `object`  | Built-in tool policy                                              |
    | `inferenceCredentialHelperTimeoutSec` | `integer` | Credential helper timeout                                         |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "apiKey": "<string>",
        "timeoutSec": "<integer>"
      },
      "customHeaders": "<object>"
    }
  }
  ```
</Update>

<Update label="v1.7196.0" description="2026-05-16">
  <div className="cfg-keys">
    | MDM key  | Type     | Description         |
    | -------- | -------- | ------------------- |
    | `banner` | `object` | Organization banner |
  </div>
</Update>

<Update label="v1.6889.0" description="2026-05-08">
  <div className="cfg-keys">
    | MDM key                       | Type      | Description                          |
    | ----------------------------- | --------- | ------------------------------------ |
    | `disableDeepLinkRegistration` | `boolean` | Disable claude:// deep-link handling |
    | `inferenceGatewayOidc`        | `object`  | Gateway SSO IdP (OIDC)               |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "oidc": {
          "issuer": "<string>",
          "authorizationUrl": "<string>",
          "tokenUrl": "<string>",
          "clientId": "<string>",
          "scopes": "<string>",
          "redirectPort": "<integer>",
          "bearerTokenType": "<id_token|access_token>",
          "appendOfflineAccess": "<boolean>"
        }
      }
    }
  }
  ```
</Update>

<Update label="v1.6259.0" description="2026-05-06">
  <div className="cfg-keys">
    | MDM key                        | Type     | Description        |
    | ------------------------------ | -------- | ------------------ |
    | `inferenceBedrockSsoStartUrl`  | `string` | AWS SSO start URL  |
    | `inferenceBedrockSsoRegion`    | `string` | AWS SSO region     |
    | `inferenceBedrockSsoAccountId` | `string` | AWS SSO account ID |
    | `inferenceBedrockSsoRoleName`  | `string` | AWS SSO role name  |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "ssoStartUrl": "<string>",
        "ssoRegion": "<string>",
        "ssoAccountId": "<string>",
        "ssoRoleName": "<string>"
      }
    }
  }
  ```
</Update>

<Update label="v1.5354.0" description="2026-04-29">
  <div className="cfg-keys">
    | MDM key                  | Type     | Description                       |
    | ------------------------ | -------- | --------------------------------- |
    | `otlpResourceAttributes` | `object` | OpenTelemetry resource attributes |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "otlp": {
      "resourceAttributes": "<object>"
    }
  }
  ```
</Update>

<Update label="v1.5186.0" description="2026-04-28">
  <div className="cfg-keys">
    | MDM key                       | Type   | Description          |
    | ----------------------------- | ------ | -------------------- |
    | `inferenceBedrockServiceTier` | `enum` | Bedrock service tier |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "serviceTier": "<flex|priority>"
    }
  }
  ```
</Update>

<Update label="v1.3834.0" description="2026-04-21">
  <div className="cfg-keys">
    | MDM key                        | Type      | Description               |
    | ------------------------------ | --------- | ------------------------- |
    | `disableDeploymentModeChooser` | `boolean` | Disable Claude.ai sign-in |
  </div>
</Update>

<Update label="v1.3036.0" description="2026-04-16">
  <div className="cfg-keys">
    | MDM key                      | Type   | Description         |
    | ---------------------------- | ------ | ------------------- |
    | `inferenceGatewayAuthScheme` | `enum` | Gateway auth scheme |
  </div>

  **JSON (Non-MDM User, Bootstrap Remote):**

  ```json theme={null}
  {
    "inference": {
      "credential": {
        "authScheme": "<auto|x-api-key|bearer|sso>"
      }
    }
  }
  ```
</Update>

<Update label="Baseline">
  <div className="cfg-keys">
    | MDM key                               | Type                                  | Description                                                       |
    | ------------------------------------- | ------------------------------------- | ----------------------------------------------------------------- |
    | `isDesktopExtensionEnabled`           | `boolean`                             | Allow desktop extensions (renamed from `isDxtEnabled`)            |
    | `isDesktopExtensionSignatureRequired` | `boolean`                             | Require signed extensions (renamed from `isDxtSignatureRequired`) |
    | `isLocalDevMcpEnabled`                | `boolean`                             | Allow user-added MCP servers                                      |
    | `isClaudeCodeForDesktopEnabled`       | `boolean`                             | Allow Claude Code tab                                             |
    | `coworkEgressAllowedHosts`            | `array<string>`                       | Allowed egress hosts                                              |
    | `otlpEndpoint`                        | `string`                              | OpenTelemetry collector endpoint                                  |
    | `otlpProtocol`                        | `enum`                                | OpenTelemetry exporter protocol                                   |
    | `otlpHeaders`                         | `object`                              | OpenTelemetry exporter headers                                    |
    | `autoUpdaterEnforcementHours`         | `integer`                             | Auto-update enforcement window                                    |
    | `disableAutoUpdates`                  | `boolean`                             | Block auto-updates                                                |
    | `inferenceProvider`                   | `enum`                                | Inference provider                                                |
    | `inferenceGatewayBaseUrl`             | `string`                              | Gateway base URL                                                  |
    | `inferenceGatewayApiKey`              | `string`                              | Gateway API key                                                   |
    | `inferenceVertexProjectId`            | `string`                              | GCP project ID                                                    |
    | `inferenceVertexRegion`               | `string`                              | GCP region                                                        |
    | `inferenceVertexCredentialsFile`      | `string`                              | GCP credentials file path                                         |
    | `inferenceVertexOAuthClientId`        | `string`                              | Vertex OAuth client ID                                            |
    | `inferenceVertexOAuthClientSecret`    | `string`                              | Vertex OAuth client secret                                        |
    | `inferenceVertexOAuthScopes`          | `string`                              | Vertex OAuth scopes                                               |
    | `inferenceVertexBaseUrl`              | `string`                              | Vertex AI base URL                                                |
    | `inferenceBedrockRegion`              | `string`                              | AWS region                                                        |
    | `inferenceBedrockBearerToken`         | `string`                              | AWS bearer token                                                  |
    | `inferenceBedrockBaseUrl`             | `string`                              | Bedrock base URL                                                  |
    | `inferenceBedrockProfile`             | `string`                              | AWS profile name                                                  |
    | `inferenceBedrockAwsDir`              | `string`                              | AWS config directory                                              |
    | `inferenceFoundryResource`            | `string`                              | Azure AI Foundry resource name                                    |
    | `inferenceFoundryApiKey`              | `string`                              | Azure AI Foundry API key                                          |
    | `inferenceModels`                     | `array<string\|object>`               | Model list                                                        |
    | `deploymentOrganizationUuid`          | `string`                              | Organization UUID                                                 |
    | `disableEssentialTelemetry`           | `boolean`                             | Block essential telemetry                                         |
    | `disableNonessentialTelemetry`        | `boolean`                             | Block nonessential telemetry                                      |
    | `disableNonessentialServices`         | `boolean`                             | Block nonessential services                                       |
    | `managedMcpServers`                   | `array<object\|object\|object\|null>` | Managed MCP servers                                               |
    | `disabledBuiltinTools`                | `array<string>`                       | Disabled built-in tools                                           |
    | `allowedWorkspaceFolders`             | `array<string\|object>`               | Allowed workspace folders                                         |
    | `inferenceCredentialHelper`           | `string`                              | Helper script                                                     |
    | `inferenceCredentialHelperTtlSec`     | `integer`                             | Helper script TTL                                                 |
    | `inferenceMaxTokensPerWindow`         | `integer`                             | Max tokens per window                                             |
    | `inferenceTokenWindowHours`           | `integer`                             | Token cap window                                                  |
  </div>

  **Deprecated:**

  * `requireCoworkFullVmSandbox` — Require full VM sandbox
</Update>
