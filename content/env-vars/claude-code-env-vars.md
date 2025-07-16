# Claude Code Environment Variables

Found **225 unique environment variables** supported by Claude Code from v1.0.48 package analysis (verified complete).

## Extraction Methodology & Best Practices

### How to Extract Environment Variables

1. **Primary extraction from main CLI bundle:**
   ```bash
   rg -o 'process\.env\.[a-zA-Z_][a-zA-Z0-9_]*' package/cli.js | sed 's/process\.env\.//' | sort | uniq > vars_cli.txt
   ```

2. **Check additional files in package:**
   ```bash
   rg -o 'process\.env\.[a-zA-Z_][a-zA-Z0-9_]*' package/sdk.mjs | sed 's/process\.env\.//' | sort | uniq > vars_sdk.txt
   rg -o 'process\.env\.[a-zA-Z_][a-zA-Z0-9_]*' package/scripts/preinstall.js | sed 's/process\.env\.//' | sort | uniq > vars_scripts.txt
   ```

3. **Combine and deduplicate:**
   ```bash
   cat vars_*.txt | sort | uniq > all_vars.txt
   ```

4. **Compare with existing documentation:**
   ```bash
   grep -o '^- `[A-Z_][A-Z0-9_]*`' claude-code-env-vars.md | sed 's/^- `//; s/`.*$//' | sort | uniq > documented_vars.txt
   comm -13 documented_vars.txt all_vars.txt  # Find new vars
   comm -23 documented_vars.txt all_vars.txt  # Find over-documented vars
   ```

### Update Process for New Releases

1. Download latest package: `npm pack @anthropic-ai/claude-code@latest`
2. Extract: `tar -xzf anthropic-ai-claude-code-*.tgz`
3. Run extraction methodology above
4. Update this file with new variables and increment count
5. Categorize new variables appropriately
6. Document version number and date in commit message

### Extraction Notes

- **Pattern**: `process\.env\.[a-zA-Z_][a-zA-Z0-9_]*` captures both uppercase and lowercase env var naming
- **Sources**: cli.js (main), sdk.mjs (4 vars), scripts/preinstall.js (0 vars in v1.0.40)
- **False positives**: Manually verify vars that look suspicious or too generic
- **Categories**: Group by function (auth, cloud providers, debugging, etc.) for maintainability

## Core Authentication & Configuration
- `ANTHROPIC_API_KEY` - Main API key for Anthropic services
- `ANTHROPIC_AUTH_TOKEN` - Alternative authentication token
- `ANTHROPIC_BASE_URL` - Custom base URL for Anthropic API
- `CLAUDE_CONFIG_DIR` - Configuration directory path
- `CLAUDE_CODE_USE_BEDROCK` - Enable AWS Bedrock integration
- `CLAUDE_CODE_USE_VERTEX` - Enable Google Vertex AI integration
- `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` - API key helper TTL in milliseconds
- `CLAUDE_CODE_AUTO_CONNECT_IDE` - Auto-connect to IDE integration

## Model & API Settings
- `ANTHROPIC_MODEL` - Specify which model to use
- `ANTHROPIC_SMALL_FAST_MODEL` - Small/fast model for quick operations
- `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` - AWS region for small model
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS` - Maximum output tokens limit
- `CLAUDE_CODE_MAX_RETRIES` - Maximum retry attempts for API calls
- `CLAUDE_CODE_OAUTH_TOKEN` - OAuth token for authentication
- `API_TIMEOUT_MS` - API request timeout in milliseconds
- `MAX_THINKING_TOKENS` - Maximum tokens for thinking/reasoning
- `MAX_MCP_OUTPUT_TOKENS` - Maximum MCP output tokens

## Feature Flags & Controls
- `CLAUDE_CODE_ENABLE_TELEMETRY` - Enable telemetry collection
- `DISABLE_TELEMETRY` - Disable telemetry collection
- `DISABLE_PROMPT_CACHING` - Disable prompt caching
- `CLAUDE_CODE_DISABLE_FINE_GRAINED_TOOL_STREAMING` - Disable fine-grained tool streaming
- `DISABLE_INTERLEAVED_THINKING` - Disable interleaved thinking mode
- `DISABLE_COST_WARNINGS` - Disable cost warning notifications
- `DISABLE_ERROR_REPORTING` - Disable error reporting
- `CLAUDE_CODE_ENABLE_UNIFIED_READ_TOOL` - Enable unified read tool
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` - Disable non-essential network traffic

## Cloud Provider Authentication Bypass
- `CLAUDE_CODE_SKIP_BEDROCK_AUTH` - Skip AWS Bedrock authentication
- `CLAUDE_CODE_SKIP_VERTEX_AUTH` - Skip Google Vertex authentication

## AWS Configuration
- `AWS_REGION` - AWS region
- `AWS_DEFAULT_REGION` - Default AWS region
- `AWS_ACCESS_KEY_ID` - AWS access key
- `AWS_SECRET_ACCESS_KEY` - AWS secret key
- `AWS_SESSION_TOKEN` - AWS session token
- `AWS_PROFILE` - AWS profile name
- `AWS_EXECUTION_ENV` - AWS execution environment
- `BEDROCK_BASE_URL` - Custom Bedrock base URL

## Google Cloud Configuration
- `GOOGLE_CLOUD_PROJECT` - GCP project ID
- `GOOGLE_APPLICATION_CREDENTIALS` - GCP service account credentials
- `GOOGLE_CLOUD_QUOTA_PROJECT` - GCP quota project
- `google_cloud_project` - GCP project ID (lowercase)
- `google_application_credentials` - GCP service account credentials (lowercase)
- `gcloud_project` - Google Cloud project (alternate form)
- `ANTHROPIC_VERTEX_PROJECT_ID` - Vertex AI project ID
- `VERTEX_BASE_URL` - Custom Vertex base URL
- `VERTEX_REGION_CLAUDE_3_5_HAIKU` - Vertex region for Claude 3.5 Haiku
- `VERTEX_REGION_CLAUDE_3_5_SONNET` - Vertex region for Claude 3.5 Sonnet  
- `VERTEX_REGION_CLAUDE_3_7_SONNET` - Vertex region for Claude 3.7 Sonnet
- `VERTEX_REGION_CLAUDE_4_0_OPUS` - Vertex region for Claude 4.0 Opus
- `VERTEX_REGION_CLAUDE_4_0_SONNET` - Vertex region for Claude 4.0 Sonnet
- `GCLOUD_PROJECT` - Google Cloud project
- `GCP_PROJECT` - GCP project identifier
- `CLOUD_ML_REGION` - Cloud ML region

## Tool & System Configuration
- `BASH_DEFAULT_TIMEOUT_MS` - Default bash command timeout
- `BASH_MAX_TIMEOUT_MS` - Maximum bash command timeout
- `BASH_MAX_OUTPUT_LENGTH` - Maximum bash output length
- `MCP_TIMEOUT` - MCP operation timeout
- `MCP_TOOL_TIMEOUT` - MCP tool-specific timeout
- `USE_BUILTIN_RIPGREP` - Use built-in ripgrep instead of system
- `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` - Maintain project working directory
- `CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS` - OpenTelemetry shutdown timeout

## Development & Debug
- `DEBUG` - Enable debug mode
- `DEBUG_AUTH` - Enable authentication debugging
- `NODE_DEBUG` - Node.js debug flags
- `NODE_EXTRA_CA_CERTS` - Additional CA certificates for Node.js
- `NODE_V8_COVERAGE` - V8 coverage output directory
- `DEV` - Development mode flag
- `IS_DEMO` - Demo mode flag
- `IS_SANDBOX` - Sandbox environment flag
- `DISABLE_ERROR_REPORTING` - Disable error reporting
- `CLAUDE_CODE_ENTRYPOINT` - Application entrypoint
- `CLAUDE_CODE_ACTION` - Current action being performed
- `DISABLE_AUTOUPDATER` - Disable automatic updates
- `DISABLE_BUG_COMMAND` - Disable bug reporting command
- `IGNORE_TEST_WIN32` - Ignore Windows 32-bit tests

## IDE Integration
- `CLAUDE_CODE_IDE_HOST_OVERRIDE` - Override IDE host
- `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` - Skip automatic IDE installation
- `CLAUDE_CODE_IDE_SKIP_VALID_CHECK` - Skip IDE validation checks
- `CLAUDE_CODE_SSE_PORT` - Server-sent events port
- `CURSOR_TRACE_ID` - Cursor editor trace ID

## Telemetry & Monitoring (OpenTelemetry)
- `OTEL_EXPORTER_OTLP_ENDPOINT` - OTLP exporter endpoint
- `OTEL_EXPORTER_OTLP_HEADERS` - OTLP exporter headers
- `OTEL_EXPORTER_OTLP_INSECURE` - Use insecure OTLP connection
- `OTEL_EXPORTER_OTLP_PROTOCOL` - OTLP protocol type
- `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` - OTLP logs protocol
- `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` - OTLP metrics protocol
- `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` - Metrics temporality
- `OTEL_EXPORTER_PROMETHEUS_HOST` - Prometheus exporter host
- `OTEL_EXPORTER_PROMETHEUS_PORT` - Prometheus exporter port
- `OTEL_LOGS_EXPORTER` - Logs exporter type
- `OTEL_LOGS_EXPORT_INTERVAL` - Logs export interval
- `OTEL_LOG_USER_PROMPTS` - Log user prompts flag
- `OTEL_METRIC_EXPORT_INTERVAL` - Metrics export interval
- `OTEL_METRICS_EXPORTER` - Metrics exporter type

## Error Reporting (Sentry)
- `SENTRY_DSN` - Sentry Data Source Name
- `SENTRY_ENVIRONMENT` - Sentry environment
- `SENTRY_NAME` - Sentry server name
- `SENTRY_RELEASE` - Sentry release version
- `SENTRY_TRACE` - Sentry trace header
- `SENTRY_BAGGAGE` - Sentry baggage header
- `SENTRY_TRACES_SAMPLE_RATE` - Sentry trace sampling rate
- `SENTRY_USE_ENVIRONMENT` - Use environment for Sentry

## Network & Proxy
- `HTTP_PROXY` - HTTP proxy URL
- `HTTPS_PROXY` - HTTPS proxy URL
- `NO_PROXY` - No proxy domains
- `http_proxy` - HTTP proxy URL (lowercase)
- `https_proxy` - HTTPS proxy URL (lowercase)
- `no_proxy` - No proxy domains (lowercase)
- `grpc_proxy` - gRPC proxy URL
- `no_grpc_proxy` - No gRPC proxy domains
- `ANTHROPIC_CUSTOM_HEADERS` - Custom headers for Anthropic API
- `ANTHROPIC_BETAS` - Beta features to enable
- `CLAUDE_CODE_CLIENT_CERT` - Client certificate for TLS authentication
- `CLAUDE_CODE_CLIENT_KEY` - Client private key for TLS authentication
- `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE` - Passphrase for client private key

## Cloud Platform Detection
### Vercel
- `VERCEL` - Vercel platform flag
- `VERCEL_REGION` - Vercel deployment region
- `VERCEL_BITBUCKET_COMMIT_SHA` - Bitbucket commit SHA
- `VERCEL_GIT_COMMIT_SHA` - Git commit SHA
- `VERCEL_GITHUB_COMMIT_SHA` - GitHub commit SHA
- `VERCEL_GITLAB_COMMIT_SHA` - GitLab commit SHA

### Netlify
- `NETLIFY` - Netlify platform flag

### IBM Cloud
- `IBM_CLOUD_REGION` - IBM Cloud region

### Tencent Cloud
- `TENCENTCLOUD_REGION` - Tencent Cloud region
- `TENCENTCLOUD_APPID` - Tencent Cloud app ID
- `TENCENTCLOUD_ZONE` - Tencent Cloud zone

### Alibaba Cloud
- `ALIYUN_REGION_ID` - Alibaba Cloud region

### Azure
- `WEBSITE_SITE_NAME` - Azure website name
- `REGION_NAME` - Azure region name

### GCP Additional
- `GAE_MODULE_NAME` - Google App Engine module
- `GAE_SERVICE` - Google App Engine service
- `GCE_METADATA_HOST` - GCE metadata host
- `GCE_METADATA_IP` - GCE metadata IP
- `FUNCTION_NAME` - Cloud Function name
- `FUNCTION_TARGET` - Cloud Function target
- `K_CONFIGURATION` - Knative configuration
- `K_SERVICE` - Knative service
- `CLOUD_RUN_JOB` - Cloud Run job

### CI/CD Platforms
- `GITHUB_ACTIONS` - GitHub Actions flag
- `GITHUB_ACTOR` - GitHub actor
- `GITHUB_ACTOR_ID` - GitHub actor ID
- `GITHUB_EVENT_NAME` - GitHub event name
- `GITHUB_REPOSITORY_OWNER` - Repository owner
- `GITHUB_REPOSITORY_OWNER_ID` - Repository owner ID
- `GITHUB_SHA` - GitHub commit SHA
- `RUNNER_ENVIRONMENT` - Runner environment
- `RUNNER_OS` - Runner operating system
- `CF_PAGES_COMMIT_SHA` - Cloudflare Pages commit SHA
- `COMMIT_REF` - Commit reference
- `ZEIT_BITBUCKET_COMMIT_SHA` - Zeit Bitbucket commit SHA
- `ZEIT_GITHUB_COMMIT_SHA` - Zeit GitHub commit SHA
- `ZEIT_GITLAB_COMMIT_SHA` - Zeit GitLab commit SHA

## System & Environment
- `HOME` - User home directory
- `USERPROFILE` - Windows user profile
- `LOCALAPPDATA` - Windows local app data
- `APPDATA` - Windows app data
- `TEMP` - Temporary directory
- `SYSTEMROOT` - Windows system root
- `PATH` - System PATH
- `PATHEXT` - Windows path extensions
- `PWD` - Present working directory
- `SHELL` - User shell
- `EDITOR` - Default editor
- `VISUAL` - Visual editor
- `BROWSER` - Default browser

## Terminal & Display Detection
- `TERM` - Terminal type
- `TERM_PROGRAM` - Terminal program name
- `ALACRITTY_LOG` - Alacritty terminal logging
- `GNOME_TERMINAL_SERVICE` - GNOME terminal service
- `KONSOLE_VERSION` - Konsole terminal version
- `KITTY_WINDOW_ID` - Kitty terminal window ID
- `TERMINAL_EMULATOR` - Terminal emulator name
- `TERMINATOR_UUID` - Terminator terminal UUID
- `TILIX_ID` - Tilix terminal ID
- `VTE_VERSION` - VTE terminal version
- `XTERM_VERSION` - Xterm version
- `WT_SESSION` - Windows Terminal session
- `STY` - Screen session

## Remote Access
- `SSH_CLIENT` - SSH client info
- `SSH_CONNECTION` - SSH connection info
- `SSH_TTY` - SSH TTY

## XDG Base Directory
- `XDG_CACHE_HOME` - XDG cache directory
- `XDG_CONFIG_HOME` - XDG config directory
- `XDG_DATA_HOME` - XDG data directory
- `XDG_STATE_HOME` - XDG state directory

## Package Managers & Tools
- `BUN_INSTALL` - Bun installation path
- `COREPACK_ENABLE_AUTO_PIN` - Corepack auto-pin
- `NODE_OPTIONS` - Node.js options
- `PKG_CONFIG_PATH` - pkg-config path
- `npm_package_config_libvips` - npm package config for libvips

## Development Tools
- `VSCODE_GIT_ASKPASS_MAIN` - VS Code Git askpass
- `GRACEFUL_FS_PLATFORM` - Graceful-fs platform override
- `TEST_GRACEFUL_FS_GLOBAL_PATCH` - Test graceful-fs patching
- `__MINIMATCH_TESTING_PLATFORM__` - Minimatch testing platform

## Graphics & Libraries
- `SHARP_FORCE_GLOBAL_LIBVIPS` - Force global libvips for Sharp
- `SHARP_IGNORE_GLOBAL_LIBVIPS` - Ignore global libvips for Sharp

## Network Libraries
- `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` - gRPC SSL roots file
- `GRPC_EXPERIMENTAL_ENABLE_OUTLIER_DETECTION` - gRPC outlier detection
- `GRPC_NODE_TRACE` - gRPC Node.js tracing
- `GRPC_NODE_USE_ALTERNATIVE_RESOLVER` - gRPC alternative resolver
- `GRPC_NODE_VERBOSITY` - gRPC Node.js verbosity
- `GRPC_SSL_CIPHER_SUITES` - gRPC SSL cipher suites
- `GRPC_TRACE` - gRPC tracing
- `GRPC_VERBOSITY` - gRPC verbosity
- `UNDICI_NO_FG` - Undici no file descriptor guard
- `WS_NO_BUFFER_UTIL` - WebSocket no buffer util
- `WS_NO_UTF_8_VALIDATE` - WebSocket no UTF-8 validation

## Miscellaneous System
- `OSTYPE` - Operating system type
- `SESSIONNAME` - Windows session name
- `WSL_DISTRO_NAME` - WSL distribution name
- `MSYSTEM` - MSYS2 system
- `IGNORE_TEST_WIN32` - Ignore Windows 32-bit tests
- `JEST_WORKER_ID` - Jest worker ID
- `C` - C locale override
- `__CFB` - CloudFlare bypass
- `__CFBundleIdentifier` - macOS bundle identifier
- `ZDOTDIR` - Zsh dot directory
- `CLAUBBIT` - Custom Claude bit flag
- `comspec` - Windows command interpreter
- `ConEmuTask` - ConEmu task environment
- `CLAUDE_CODE_DONT_INHERIT_ENV` - Don't inherit environment
- `CLAUDE_CODE_EXTRA_BODY` - Extra request body data
- `CLAUDE_SDK_MCP_SERVERS` - SDK MCP servers configuration
- `USE_LOCAL_OAUTH` - Use local OAuth
- `METADATA_SERVER_DETECTION` - Metadata server detection
- `DETECT_GCP_RETRIES` - Detect GCP retries
- `FLY_REGION` - Fly.io region
- `DYNO` - Heroku dyno identifier
- `FORCE_CODE_TERMINAL` - Force code terminal
- `ENABLE_BACKGROUND_TASKS` - Enable background tasks

## Permission Skip Variables (Limited)
- `CLAUDE_CODE_SKIP_BEDROCK_AUTH` - Skip AWS Bedrock authentication (sets `skipAuth: true`)
- `CLAUDE_CODE_SKIP_VERTEX_AUTH` - Skip Google Vertex authentication (provides dummy auth client)

**Note:** These are the only permission-related skip variables found. No general file system or directory permission bypass flags exist.