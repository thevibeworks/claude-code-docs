> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Science on a corporate network

> How to run Claude Science behind an outbound proxy, a TLS-inspecting proxy, an internal package mirror, and an egress firewall, with the settings your network team needs for each.

Claude Science runs on each member's computer and connects out for sign-in, the Claude API, and package and research hosts, usually through controls your IT organization manages on a corporate network. This page shows the administrator who runs those controls how to point Claude Science at an internal package mirror, configure an outbound proxy and TLS inspection, and hand the firewall team the [network requirements](/docs/claude-science/network-requirements) it needs.

Claude Science makes three kinds of outbound connections, each passing through a different part of your network policy:

* The app's own connections (sign-in, the Claude API, Anthropic-hosted connectors, update checks) traverse your outbound proxy and TLS inspection.
* The analysis sandbox's connections (package hosts and research databases, when Claude runs code) are filtered by the app's own network allowlist; package downloads can be redirected to your internal mirror.
* Interactive previews load display libraries from public content-delivery networks in the browser, as ordinary browser traffic governed by your endpoint's web policy.

## Setup at a glance

1. Check the [support table](#what-works-on-a-corporate-network) for your operating systems and network shape.
2. Hand the [network requirements](/docs/claude-science/network-requirements) page to the team that manages your proxy or firewall allowlist.
3. [Point package installs at your internal mirror](#point-package-installs-at-an-internal-mirror) if the public package hosts are blocked, and deploy the mirror credential.
4. [Connect through an outbound proxy](#connect-through-an-outbound-proxy) if your network uses one.
5. If your proxy inspects TLS, [deploy your corporate root certificate](#work-behind-tls-inspection) as two bundles: one for the app, and a differently built one for package downloads.
6. [Deploy the settings with device management](/docs/claude-science/manage-on-devices#deploy-configuration-with-device-management) rather than by hand.
7. If sign-in or a first build fails, match the error against [Troubleshooting](#troubleshooting-corporate-network-errors).

## What works on a corporate network

| Network shape                                                                | macOS                                                                                                                                                                       | Windows                                                                                                                                                                  | Linux                                                                                                                                                                       |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit outbound HTTP proxy (HTTP CONNECT)                                  | Supported; detected automatically from the system settings                                                                                                                  | Supported; detected automatically from Windows proxy settings                                                                                                            | Supported                                                                                                                                                                   |
| Proxy that requires Basic authentication                                     | Supported, with credentials in the proxy address                                                                                                                            | Supported, with credentials in the proxy address                                                                                                                         | Supported, with credentials in the proxy address                                                                                                                            |
| Proxy that requires NTLM, Negotiate, or Kerberos authentication              | Not supported                                                                                                                                                               | Not supported                                                                                                                                                            | Not supported                                                                                                                                                               |
| Network that only publishes a PAC or WPAD file                               | Not supported                                                                                                                                                               | Supported in the app window, which follows the proxy the script resolves (see [System proxy settings on macOS and Windows](#system-proxy-settings-on-macos-and-windows)) | Not supported                                                                                                                                                               |
| SOCKS proxy                                                                  | Not supported                                                                                                                                                               | Not supported                                                                                                                                                            | Not supported                                                                                                                                                               |
| TLS inspection on the app's own connections (Zscaler, Netskope, and similar) | Supported with a CA bundle setting                                                                                                                                          | Supported; a corporate root in the computer's certificate store is trusted automatically                                                                                 | Supported with a CA bundle setting                                                                                                                                          |
| TLS inspection on conda package downloads                                    | Supported with a CA bundle setting                                                                                                                                          | Supported automatically through the Windows certificate store                                                                                                            | Supported with a CA bundle setting                                                                                                                                          |
| TLS inspection on pip package downloads                                      | Supported, with the corporate root also installed in the operating system's trust store (see [Corporate root for package downloads](#corporate-root-for-package-downloads)) | Supported automatically through the Windows certificate store                                                                                                            | Supported, with the corporate root also installed in the operating system's trust store (see [Corporate root for package downloads](#corporate-root-for-package-downloads)) |
| Internal package mirror (Artifactory, Nexus)                                 | Supported                                                                                                                                                                   | Supported                                                                                                                                                                | Supported                                                                                                                                                                   |
| Internal package mirror reached only through the corporate proxy             | Not supported                                                                                                                                                               | Not supported                                                                                                                                                            | Not supported                                                                                                                                                               |
| Authenticated package mirror                                                 | Supported, with the credential saved in Settings                                                                                                                            | Supported, with the credential saved in Settings                                                                                                                         | Supported, with the credential saved in Settings                                                                                                                            |
| Local connectors (the bundled research tools) behind TLS inspection          | Not supported                                                                                                                                                               | Not supported                                                                                                                                                            | Not supported                                                                                                                                                               |

## Point package installs at an internal mirror

When your network blocks the public package hosts (`conda.anaconda.org`, `repo.anaconda.com`, `pypi.org`), point Claude Science at your internal artifact repository instead, and every environment build fetches packages through it. You can set the mirror in three places: once for the whole organization under **Organization settings** > **Claude Science** > **Organization package mirror**, for a fleet with the `[conda] channel_mirror` and `pip_index_url` keys in a [deployed `config.toml`](/docs/claude-science/manage-on-devices#deploy-configuration-with-device-management), or for a single machine under **Settings** > **Network** > **Package mirror**, where the same two settings are called the conda channel mirror and the pip index URL. The steps below use the Settings page, the quickest way to test a mirror URL before you deploy it.

The organization setting takes a conda channel URL and a Python package index (PyPI) URL, which apply to every member whether or not the organization manages the network allowlist. They take precedence over a mirror set in a member's configuration file or Settings; the member's values are kept but not used, and their Settings show the package mirror as controlled by their admin. The same URL rules apply as below, and an address that breaks those rules is ignored for that registry rather than stopping the app. Members still sign in to the mirror themselves, once for each mirror host (see [Mirror credentials](#mirror-credentials)), and the mirror removes the public hosts it replaces for every member. See [Organization package mirror](/docs/claude-science/admin-controls#organization-package-mirror).

Set both a conda channel mirror and a pip index: analysis environments are built from conda packages, so a pip index alone leaves the first build stuck trying to reach the public conda host.

<Steps>
  <Step title="Enter the conda channel mirror">
    Open **Settings** > **Network**, select **Configure** on the **Package mirror** row, and paste the base URL of your conda mirror. For JFrog Artifactory that is the conda API root or a virtual conda repository, for example `https://yourorg.jfrog.io/artifactory/api/conda/conda-all`.
  </Step>

  <Step title="Enter the pip index URL">
    Paste your Python package index, including the `/simple` suffix that Artifactory and Nexus PyPI remotes use, for example `https://yourorg.jfrog.io/artifactory/api/pypi/pypi-remote/simple`.
  </Step>

  <Step title="Save, then run the check">
    Select **Save**, then **Check**: a green result confirms the mirror answered, and a `401` or `403` on an authenticated mirror is expected until a credential is saved (see [Mirror credentials](#mirror-credentials)). The mirror takes effect for the next package operation without a restart. On a machine with an outbound proxy, confirm with a test environment build rather than the check alone (see [Mirror traffic and your other network controls](#mirror-traffic-and-your-other-network-controls)).
  </Step>
</Steps>

The mirror must serve the standard conda channel layout, with one base URL, one directory per channel, and one per platform beneath it:

```text theme={null}
<channel mirror>/
  conda-forge/
    noarch/repodata.json
    noarch/<package>.conda
    linux-64/repodata.json
    osx-arm64/...
    win-64/...
  bioconda/
    noarch/...
```

Your mirror must serve at least `conda-forge` (every environment uses it) and `bioconda` for R and bioinformatics work; other channels a member requests (for example `pytorch` or `nvidia`) resolve under the same mirror base, so serve those too if needed. Anaconda's commercial `defaults` channel is rejected while a mirror is configured, so members should use `conda-forge` instead.

<Note>
  Do not point the conda mirror at a remote repository configured for a single channel (for example one whose upstream is `https://conda.anaconda.org/conda-forge`): it returns an empty index that the check reports green while every build then fails with `nothing provides <package>`. Use a remote that proxies the conda host root (`…/artifactory/api/conda/conda-remote`), a virtual conda repository, or the conda API root with channel-named remote repositories beneath it.
</Note>

Mirror URLs must use `https://`, name a host by DNS name rather than IP address, and use port 443 or 8443, so an Artifactory instance on its stock port 8081 needs a 443 or 8443 listener or a reverse proxy in front of it. Credentials embedded in the URL are rejected at save time. The Settings page accepts `https://` mirrors only, while Claude Science also accepts an `http://` mirror from `config.toml` when `[conda] allow_insecure_mirror` is set. Validate mirror URLs before distributing a `config.toml`, since an invalid deployed value prevents the app from starting.

### Mirror credentials

For a mirror that requires authentication, enter one username and access token under **Settings** > **Network** > **Package mirror** > **Mirror credentials**, using an account scoped to reading the mirror, then run the check so it signs in with the credential. The one credential is presented to both the conda-mirror host and the pip-index host, so if those need different accounts, keep one of them anonymous; the credential is sent only to `https://` mirror hosts.

Claude Science stores the credential encrypted in its local database, using a key kept in a file only the member's account can read (on macOS, a copy of that key is in the keychain for recovery), and also writes the credential, automatically, to a plaintext `.netrc` at `~/.claude-science/conda/.netrc` that the conda and pip download tools read during environment builds. Code that runs while an environment builds (a package's `setup.py`, for example) can read that file, Claude's analysis code cannot read either location, and a `.netrc` in the member's home directory is not used for these downloads. For a macOS or Linux fleet that manages credentials centrally, deploy that `.netrc` file yourself instead (on Windows, save the credential in Settings), one `machine <mirror hostname>` block per mirror host with `login` and `password` lines and no comments, and use either the file or Settings, not both: a credential saved in Settings rewrites the file from the saved value at the save and at every restart and environment build, while a file deployed with no credential saved in Settings is left alone.

Environments a member registers from an existing project folder install their packages inside the analysis sandbox during a session, where the credential is hidden by design, so those environments need a mirror that allows anonymous reads.

### Mirror traffic and your other network controls

Configuring a mirror removes the public package hosts from the sandbox's network allowlist and admits the mirror host in their place, so a misconfigured mirror fails with an error that names the mirror rather than falling back to the public hosts. To keep the public hosts reachable alongside the mirror, re-add them under **Settings** > **Network** (`pypi.org`, `*.pypi.org`, `files.pythonhosted.org` for pip, and `conda.anaconda.org`, `repo.anaconda.com`, `anaconda.org`, `*.anaconda.org` for conda). When the organization manages the network allowlist, **Network** settings are read-only, so a member can't re-add them, and the hosts a mirror replaces stay removed even if they are switched on in the organization's list.

Environment builds connect to the mirror host directly, never through your outbound proxy: the workstation needs a direct route (typically your VPN or internal network), any workstation firewall must allow the mirror host as a direct destination, and a proxy allowlist entry alone does not reach it. A package failure that names the mirror on a proxy-only network therefore means the mirror is unreachable directly, and a SaaS repository such as `yourorg.jfrog.io` works only if the workstation can reach it directly, so on a proxy-only network host the mirror inside your network. On a proxy-configured machine the **Check** button and a real build can take different paths, so treat a test environment build as the authoritative signal (a known limitation).

Mirrors that redirect package files to path-style object-storage URLs (such as `s3.us-west-2.amazonaws.com/<bucket>/...`) fail with `CONNECT tunnel failed, response 403`, because path-style object-storage hosts are on a built-in denylist that cannot be overridden; have the mirror serve the files itself, or redirect to bucket-qualified hostnames such as `<bucket>.s3.us-west-2.amazonaws.com` and add that hostname under **Settings** > **Network** > **Allowed domains**. The check warns at save time when it sees a redirect to a denied host. The package manager that builds environments ships inside the app, so a first build on a locked-down network downloads no tooling from GitHub.

## Connect through an outbound proxy

Claude Science reads its proxy configuration once at startup, so restart it after a change. The first source that sets a proxy address wins:

1. The standard proxy variables in its own process environment: `HTTPS_PROXY`, `HTTP_PROXY`, and `NO_PROXY` (lowercase spellings also work). `ALL_PROXY` fills in for either proxy variable that is unset, an empty variable counts as unset, and `NO_PROXY="*"` sends all traffic directly.
2. The `[network] proxy` key in `config.toml`, the form to [deploy with device management](/docs/claude-science/manage-on-devices#deploy-configuration-with-device-management).
3. The proxy field under **Settings** > **Network**, where a member can paste a proxy address by hand. It takes effect at the next restart, and when `config.toml` sets the proxy, the field shows as managed by your organization so members cannot override it.
4. On macOS and Windows, the proxy configured in the operating system's settings, which Claude Science detects automatically: an explicit web proxy in macOS network settings, or the proxy server in Windows proxy settings.

Write the proxy as an `http://` URL; if it requires a username and password, embed them in the address and percent-encode special characters (for example, `@` in a password becomes `%40`):

```text theme={null}
HTTPS_PROXY=http://username:password@proxy.example.corp:8080
HTTP_PROXY=http://username:password@proxy.example.corp:8080
NO_PROXY=.example.corp
```

An `https://` (TLS-to-proxy) address works for the app's own connections only. Sandboxed package downloads tunnel only through `http://` proxies, so with an `https://` address they skip the proxy and connect directly; an `http://` address keeps every connection on the proxy.

Claude Science always bypasses the proxy for loopback addresses (`localhost`, `127.0.0.1`, and their IPv6 equivalents), whether or not they appear in `NO_PROXY`, so the app and its background service can always talk to each other. Add your internal domains to `NO_PROXY`; entries match a host exactly or as a domain suffix (`.example.corp` and `example.corp` behave the same), and CIDR ranges such as `10.0.0.0/8` are not matched. `NO_PROXY` entries from the environment, the configuration file, and (when the system settings supply the proxy address) the macOS or Windows bypass list are combined.

### Proxy settings in the configuration file

For a fleet, set `[network] proxy` and `no_proxy` in `config.toml`; both keys and their formats are in the [configuration file reference](/docs/claude-science/configuration-file-reference#app-connection-keys).

### System proxy settings on macOS and Windows

On macOS, Claude Science detects an explicit system web proxy automatically, so a machine whose proxy your MDM already sets needs no Claude Science configuration unless the proxy requires authentication. macOS keeps an authenticated proxy entry's credentials in the keychain, where Claude Science cannot read them, so connections through the detected proxy fail with HTTP 407 (see [the troubleshooting entry](#the-proxy-requires-its-own-sign-in-http-407)); set `[network] proxy` with the credentials in the address instead. When the network publishes only a PAC or WPAD file, Claude Science on macOS detects it and names the PAC URL in the sign-in error, but does not evaluate it. Set `[network] proxy` to the proxy the PAC file resolves to for Anthropic's hosts.

On Windows, Claude Science reads the proxy server and bypass list from Windows proxy settings at startup, which covers a proxy set under **Settings** > **Network & internet** > **Proxy**, in Internet Options, or by Group Policy, so a PC whose proxy your device management already sets needs no Claude Science configuration unless the proxy requires authentication. Windows proxy settings carry no credentials either, so for a proxy that requires Basic authentication, set `[network] proxy` with the credentials in the address. Bypass entries other than host names and domain suffixes are not applied, including the **Don't use the proxy server for local (intranet) addresses** option and entries written as IP ranges, so list internal domains in `[network] no_proxy`. To restart Claude Science on Windows after a settings change, quit it from its notification-area icon and open it again, because closing the window leaves it running.

When the network publishes only a PAC or WPAD file, the Claude Science app window follows the proxy that the script resolves for Anthropic's hosts and restarts the app's background service once to apply it. A script-resolved proxy that demands a sign-in of any kind, refuses the connection, or does not answer within a few seconds is not used, and Claude Science keeps connecting as it did before, which on such a network means directly. For a proxy that needs credentials, set `[network] proxy` with them in the address. Claude Science started from a terminal with `claude-science serve` does not evaluate PAC files, so set `[network] proxy` there too.

### How the environment variables reach the app

How the variables reach the app depends on the operating system:

* On macOS, the menu-bar app reads `~/.claude-science/env`, a file of `KEY=VALUE` lines (`export KEY=VALUE` also works), when it launches. Put the three variables there, then quit and reopen the app; an app started from the Dock or Finder does not see variables exported in a terminal. The file's `NO_PROXY` entries merge with the other sources rather than replacing them.
* On Windows, the app reads the variables from the user's environment when it starts, so set them as user environment variables, then quit Claude Science from its notification-area icon and open it again; variables typed into an open Command Prompt or PowerShell window do not reach an app started from the Start menu. Because Claude Science already follows Windows proxy settings, most PCs need no variables, and `[network] proxy` in `config.toml` is the form to deploy.
* On Linux, export the variables in the shell or service unit that starts `claude-science serve`. The `env` file is read only by the macOS app.

Only Basic proxy authentication, supplied in the proxy address, is supported; NTLM, Negotiate, and Kerberos proxies are not. On macOS and Linux, networks whose only published proxy configuration is a PAC or WPAD file are not supported either, because Claude Science does not evaluate PAC files there. On Windows, the app window follows a PAC or WPAD file as described under [System proxy settings on macOS and Windows](#system-proxy-settings-on-macos-and-windows).

<Note>
  For a proxy that only speaks NTLM or Kerberos, a local relay such as `cntlm` or `px` works: the relay runs on the workstation, authenticates to your corporate proxy with the user's credentials, and exposes a plain HTTP proxy on the loopback interface. Point `HTTPS_PROXY` and `HTTP_PROXY` at the relay (for example `http://127.0.0.1:3128`). The loopback bypass governs which destinations skip the proxy, not whether the proxy can be reached, so a loopback relay works as a proxy address.
</Note>

Environment builds reach a configured [package mirror](#point-package-installs-at-an-internal-mirror) directly, not through the proxy. Separately, the `claude-science update` terminal command is its own process: it honors proxy variables exported in that shell but not the macOS `env` file, so export the variables in the terminal first. The background updater inside the running app uses the app's proxy settings.

## Work behind TLS inspection

A TLS-inspecting proxy such as Zscaler or Netskope re-signs every HTTPS connection with a certificate from your organization's own root certificate authority, which Claude Science's built-in list of public roots does not include, so until you give it that root, sign-in and package downloads fail certificate verification (the sign-in error is listed under [Troubleshooting](#troubleshooting-corporate-network-errors)).

Two settings carry the corporate root and behave differently. Set the one that matches the traffic, and read the warning in [Corporate root for package downloads](#corporate-root-for-package-downloads) before reusing one file for both.

### Corporate root for app connections

The `[network] ca_bundle` key in `config.toml` points at a PEM file whose certificates Claude Science adds to its default trust for sign-in, the Claude API, Anthropic-hosted connectors, update checks, and [cloud storage](/docs/claude-science/cloud-storage) access from Settings. For cloud storage, the corporate root applies to Amazon S3 and S3-compatible connections, and to Google Cloud Storage connections that use an HMAC key. The public roots stay in place, so the file holds only your corporate root. The path rules are in the [configuration file reference](/docs/claude-science/configuration-file-reference#app-connection-keys). A failing value is ignored with a warning rather than stopping the app, so a sign-in error behind inspection usually means the bundle did not load, and the app re-reads the bundle every few minutes (about every 30 minutes on Windows), so a corrected file takes effect without a restart. When you deploy a `config.toml`, deploy the bundle files alongside it.

On Windows, when neither `[network] ca_bundle` nor `[conda] ca_bundle` (the **CA bundle path** field in **Settings**) is set, Claude Science automatically trusts the root certificates installed for the whole computer (the computer's **Trusted Root Certification Authorities** store, not the current user's) and rechecks that store about every 30 minutes, so a PC whose device management already installs your corporate root there needs no setting. Claude Science reads that store with Windows PowerShell, so on PCs where Windows PowerShell is blocked or restricted for users, set `[network] ca_bundle` for the app's own connections and `[conda] ca_bundle` for code inside sessions instead of relying on the store. If you do set `[network] ca_bundle` on Windows, the file is used instead of the store; write its path in single quotes, for example `'C:\ProgramData\corp\corporate-ca.pem'`, because a backslash inside double quotes is a TOML escape and a file that fails to parse stops Claude Science from starting.

### Corporate root for package downloads

Conda package downloads for the analysis sandbox use their own setting, `[conda] ca_bundle`, the complete list of roots those downloads trust, so it must contain the public roots your packages come from as well as your corporate root. On Linux, when the key is not set, Claude Science uses your distribution's system certificate bundle (maintained by `update-ca-certificates` or `update-ca-trust`), so a Linux image that already trusts your corporate root needs no setting at all. On Windows, leave `[conda] ca_bundle` unset unless Windows PowerShell is blocked or restricted for users (covered under [Corporate root for app connections](#corporate-root-for-app-connections)): package downloads there verify certificates through the Windows certificate store and do not read the key, so a corporate root installed for the whole computer is trusted with no setting. A `[conda] ca_bundle` file that exists on a Windows PC becomes the complete certificate list that code inside sessions trusts, in place of the store, and the app's own connections then stop trusting the Windows certificate store automatically, so set `[network] ca_bundle` as well.

On macOS and Linux, `[conda] ca_bundle` affects package downloads only, and it never fixes sign-in. The CA bundle path field on the Settings page sets this same `[conda]` key, so filling it in helps package downloads only, and on Windows leave the field empty. Behind TLS inspection you also need `[network] ca_bundle`, which has no Settings field and is set in `config.toml`.

pip verifies package downloads against the operating system's trust store, and in this release setting `[conda] ca_bundle` alone may not be sufficient for pip, so also install the corporate root in that trust store: on Linux with `update-ca-certificates` or `update-ca-trust`, on macOS in the system keychain through your MDM, and on Windows in the computer's Trusted Root Certification Authorities store, which pip reads in environments on Python 3.10 or later, the default.

```toml theme={null}
[conda]
ca_bundle = "/etc/claude-science/complete-bundle.pem"
```

The same path rules apply as for `[network] ca_bundle`; the [configuration file reference](/docs/claude-science/configuration-file-reference#package-download-keys) lists them.

<Warning>
  Do not point `[conda] ca_bundle` at the single-root file you use for `[network] ca_bundle`: the package-download setting replaces the whole trust list, so a file containing only your corporate root breaks every package download (on Windows, every download made by code inside a session) on any network your proxy does not inspect, such as a laptop on home Wi-Fi. Build the `[conda]` bundle from your system's public roots plus the corporate root.
</Warning>

### What the certificate settings do not cover

Code that Claude runs inside a session, such as a `pip install` typed into a cell or an R `install.packages()` call, is covered on macOS but not on Linux. On macOS, Python, pip, curl, git, and downloads from R in the session's environments trust the same certificates as environment builds: the `[conda] ca_bundle` file if you set one, otherwise the system's public roots plus the corporate root Claude Science finds in the macOS keychain (`[network] ca_bundle` alone does not reach in-session code). On Windows, Python, pip, and curl inside a session are pointed at an export of the root certificates installed for the whole computer (or the `[conda] ca_bundle` file if one is set). On Linux, neither bundle reaches code inside a session: curl and git there honor a root installed in the operating system's trust store, but the environment's Python, pip, and R see public roots only, so behind TLS inspection, have Claude install packages into an environment rather than in a cell.

The local connectors (the bundled research tools) do not work behind TLS inspection in this release: they run in their own Python environment, and nothing delivers your corporate root to that environment, so their connections fail certificate verification. This is a known limitation. Claude Science does detect TLS inspection from your configured CA bundle and relax the connectors' strict certificate-profile check, which stops them from rejecting a corporate root whose Basic Constraints extension is not marked critical, but that relaxation adds no trust. The Anthropic-hosted connectors keep working once `[network] ca_bundle` is set. Connector installs that use `npm` also keep npm's own certificate configuration.

Voice dictation's server-side speech recognition uses a WebSocket connection that is covered by neither the certificate settings nor the proxy settings, so it does not work behind TLS inspection or a mandatory proxy; in the browser, dictation falls back to the browser's own speech recognition.

Certificate environment variables set in a shell, such as `SSL_CERT_FILE`, `CURL_CA_BUNDLE`, or `PIP_CERT`, never reach package downloads, because those run in an isolated environment. Use the `ca_bundle` keys instead.

## Troubleshooting corporate network errors

### Token exchange failed: unable to get local issuer certificate

Sign-in completes in the browser, then fails with this error when Claude Science's own connection to Anthropic hits TLS inspection without trusting your corporate root. The member sees a notice that the network inspects secure connections, with this error beneath it. Set `[network] ca_bundle` to a PEM file containing your corporate root (see [Corporate root for app connections](#corporate-root-for-app-connections)) and confirm the bundle warning is gone from the app log (`claude-science logs` prints it).

### The proxy requires its own sign-in (HTTP 407)

Sign-in fails with this message when the proxy demands credentials the app is not sending, because the proxy address carries none or the proxy was detected from the macOS or Windows system settings, which never supply credentials. Include the Basic-authentication credentials in the proxy address (percent-encoding special characters) under **Settings** > **Network** > **Proxy address**, in `[network] proxy`, or in `HTTPS_PROXY`, then restart the app. Only Basic authentication works, so a proxy that requires NTLM, Negotiate, or Kerberos cannot be satisfied this way. During an environment build, a proxy authentication failure surfaces as a generic HTTP 502 error rather than a 407 message.

### Package downloads are being blocked by network policy

An environment build reports this (often with HTTP 502) when it tries to reach the public package hosts on a network that blocks them and no mirror is configured. Configure the mirror under **Settings** > **Network** > **Package mirror**, with both the conda channel mirror and the pip index set.

### HTTP 401 or 403 during an environment build

The mirror requires authentication and the build is not presenting a credential it accepts. Check that a credential is saved under **Settings** > **Network** > **Package mirror** > **Mirror credentials** (or, on a fleet that deploys the `.netrc` file directly, that the file has a block for the exact mirror hostname); a credential in `~/.netrc` in the home directory is ignored for these downloads.

### HTTP 401 on the mirror check

With no saved credential, a `401` is expected because the check sends none; enter the credential under **Mirror credentials** and run the check again. When a credential is saved, the check signs in with it, so a `401` means the token is wrong or expired. On a proxy-configured machine the check and a build can also take different network paths (see [Mirror traffic and your other network controls](#mirror-traffic-and-your-other-network-controls)).

### Green check, then nothing provides the package

The conda mirror URL points at an Artifactory remote repository configured for a single channel, which returns an empty index that the check accepts; see the note in [Point package installs at an internal mirror](#point-package-installs-at-an-internal-mirror) for the mirror URL forms that work.

### CONNECT tunnel failed, response 403, naming an amazonaws.com host

The mirror redirects package files to path-style cloud object storage, which the sandbox blocks. Switch the mirror to serve the files itself or to use bucket-qualified storage URLs, as described in [Mirror traffic and your other network controls](#mirror-traffic-and-your-other-network-controls).

### https mirrors must use port 443 or 8443

The mirror is listening on a port the sandbox cannot tunnel to. Put a 443 or 8443 listener or a reverse proxy in front of it, then save the `https://` URL again.

### Local connectors fail with certificate errors behind inspection

The local research connectors report certificate failures, while the Anthropic-hosted connectors keep working once `[network] ca_bundle` is set, because the corporate root does not reach the local connectors' own Python environment (see [What the certificate settings do not cover](#what-the-certificate-settings-do-not-cover)). This is a known limitation on TLS-inspected networks.
