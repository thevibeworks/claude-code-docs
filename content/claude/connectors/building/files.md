> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Support file uploads and downloads

> Let a tool on your MCP server receive files from Claude and return files to it: requirements, host approval, uploads, downloads, limits, and testing.

File transfers let a tool on your MCP server receive a user's file from Claude (an upload) or return a file to Claude (a download). For example, when a user asks Claude to save a PDF to a folder in your product, your tool receives the PDF. When a user asks for an export from your product, your tool returns the export.

This page is for developers whose remote MCP server already works as a connector in Claude. File transfers are in beta and use an experimental MCP extension, [File Uploads and Downloads](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md) (`io.modelcontextprotocol/files`). Expect breaking changes to the extension.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Saving a file from an MCP App's view to the user's device**: see [Download files from your MCP App](https://claude.com/docs/connectors/building/mcp-apps/download-files.md)
> * **Building your first MCP server**: see [Build your first MCP server for Claude](https://claude.com/docs/connectors/building/quickstart.md)

First, [check the requirements](#requirements-for-file-transfers) and [advertise the extension](#advertise-the-extension). Then build uploads, downloads, or both:

* **Uploads**: [receive a file in a tool](#receive-a-file-in-a-tool)
* **Downloads**: [return a file from a tool](#return-a-file-from-a-tool)

## Requirements for file transfers

Before you build, check that your connector, server, storage, and account meet these requirements:

* **Directory listing**: Claude transfers files for connectors that people add from the [Connectors Directory](https://claude.com/docs/connectors/directory.md). The address that they connect to must exactly match an address on your listing. Adding your server by URL doesn't link the connector to your listing. If a connector isn't linked, Claude sends it no files and removes any files from its tools' results. Your server receives no error.
* **Server URL**: your listing needs one URL that every user connects to, or a fixed set under [**Multiple URLs**](https://claude.com/docs/connectors/building/authentication.md#servers-with-per-customer-urls). If each customer enters their own URL, such as with a **URL pattern**, Claude doesn't transfer files.
* **MCP revision**: serve [MCP revision 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) over Streamable HTTP, along with the revisions that you serve today
* **Library**: use a version that supports revision 2026-07-28. To receive uploads, it must also let a tool return the `upload_required` result type, which the extension adds. See the tested versions under [SDK support for file transfers](#sdk-support-for-file-transfers). Version 1.32.2 of `@modelcontextprotocol/sdk`, the package that the [quickstart](https://claude.com/docs/connectors/building/quickstart.md) uses, supports neither uploads nor downloads.
* **Storage**: for uploads, your storage must accept a whole file in one `PUT` or `POST` request. For downloads, it must serve a file to a `GET` request, in byte ranges if it can.
* **Approved hosts**: Anthropic must approve the hosts that store your connector's files. Your connector needs at least one approved host, even if every file goes through your MCP server. [Request approval for your hosts](#request-approval-for-your-hosts) before you build on them. Claude can also get files from your MCP server's own host, and send files to it with [`include` credentials](#targets-with-include-credentials). Claude refuses a URL on any other host, on an IP address, or on another company's storage or CDN host that all its customers share.
* **Account for testing**: use a Claude account that has access to file transfers. Name the account when you [request approval for your hosts](#request-approval-for-your-hosts). If it doesn't have access, or you aren't sure, ask Anthropic in the same email to turn on file transfers for testing. Use made-up files in your tests, not real ones. On Team and Enterprise plans, an Owner must also go to [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors). Under **File transfers**, the Owner turns on the **File uploads to connectors** toggle, the **File downloads from connectors** toggle, or both. Some organizations can't use file transfers, such as those with HIPAA settings, zero data retention, customer-managed encryption keys, an IP allowlist, or a default workspace that keeps data outside the US.

### Request approval for your hosts

Before Claude transfers files for a listing, Anthropic approves the listing's hosts. If your connector isn't listed yet, [submit it](https://claude.com/docs/connectors/building/submission.md) first. To request approval, email `mcp-review@anthropic.com` with the subject `Connector file hosts: <connector name>` and these details:

* **Listing**: your listing's name and its server URLs
* **Hosts**: the full name of each host that Claude sends files to or gets files from, in every region. You can name up to 50. If files go through your MCP server, include its host. If your storage generates host names, you can ask for a wildcard, such as `*.downloads.example.com`. Anthropic reviews each one, and you must control every name under it.
* **Use of each host**: whether it's for production or testing, whether all your customers share it, and whether it's behind a CDN
* **Ownership**: for a host on another domain of yours, a public page that shows that the domain is yours. For a bucket or account host on a storage provider's domain, a statement that the exact host name is yours.
* **Test organization**: the email address of the Claude account that you test with. If that account is in a Team or Enterprise organization, also the **Organization ID**, which you copy from [**Organization settings > Organization and access**](https://claude.ai/admin-settings/organization).

Wait for Anthropic to confirm the hosts and the test organization before you rely on them. An approval covers the hosts that Anthropic confirmed and the server URLs that your listing had at that time. Before you use a host that it doesn't cover, or a new server URL, email again. Claude doesn't transfer files there until Anthropic approves it.

### URLs, headers, and fields of a target

A target is an object in your server's response that says where Claude sends or gets one file. In each upload target and download target, follow these rules:

* **Address**: use `https` on port 443 and a host name that resolves to public IPv4 addresses, with a certificate from a public certificate authority. Use TLS 1.3, or TLS 1.2 with an ECDHE suite that uses AES-GCM or ChaCha20-Poly1305. Use a host on a domain that you own where you can.
* **Authorization**: make the URL carry its own authorization, such as a short-lived signature, and set the target's `credentials` field to `"omit"`. If you sign the URL with temporary credentials, such as a cloud role's, use ones that last at least as long as the URL. Anyone who has the URL can use it until it expires, so make each URL work for one file, and either for its upload or for its download. For a URL on your MCP server itself, see [targets with `include` credentials](#targets-with-include-credentials).
* **Characters**: percent-encode spaces and other characters that a URL's query can't contain, and leave out `#`
* **Headers**: in the target's `headers` field, list only the headers that your storage needs, each name once. Headers that Claude refuses include `Authorization`, `Cookie`, `Host`, `Content-Length`, `Date`, and `User-Agent`.
* **Fields**: add no fields that the extension doesn't define
* **Logs**: keep target URLs, target headers, form fields, inline file data, and an upload's [`requestState`](#return-an-upload-target) out of logs, traces, and error reports

If a target's host, query, header, or field breaks a rule, expect these results:

* **Upload**: Claude refuses your server's whole response, including the targets for other files
* **Download**: Claude leaves that target's file out of the result, or replaces the result with an error

Have your storage answer at the target's URL directly. A redirect fails the transfer. Don't put a sign-in page, a bot challenge, or a filter on `User-Agent` or source address in front of the URL.

### Targets with `include` credentials

If a target's URL has the same scheme, host, and port as your connector's address, you can set `credentials` to `"include"`. Claude then sends or gets the file with the `Authorization` header that it sent on the tool call. For an `include` target, follow these rules:

* **Application**: name a URL that your MCP server's own application serves. Don't name one that another application on the same host serves, because that application would receive the user's token.
* **User**: check that the token belongs to the user that you issued the target to
* **Token lifetime**: a large upload can reach your server 20 minutes after the tool call, with that call's token. If your server can refuse the token by then, use `"omit"` for large files.
* **Several uploads**: use `"omit"` if you return several upload targets. With `"include"`, Claude has to start each upload within five minutes of your response, and it can send the files one after another.
* **Large downloads**: use `"omit"` for a large file. With `"include"`, Claude gets the whole file in one `GET` and doesn't resume it.
* **Refusal**: use `"omit"` if Claude calls your server without an `Authorization` header, or if your listing says that the connector handles personal health data. Claude refuses `include` targets in these cases, and for some other connectors.

## Advertise the extension

In your response to `server/discover`, list `io.modelcontextprotocol/files` under `capabilities.extensions`. If you take uploads, set it to `{ "upload": {} }`. If you only return files, set it to `{}`. `download` is a client setting, so leave it out. This example leaves out the response's other members:

```json theme={null}
{
  "supportedVersions": ["2026-07-28"],
  "capabilities": {
    "extensions": {
      "io.modelcontextprotocol/files": { "upload": {} }
    }
  }
}
```

Answer `server/discover` well within two seconds, in the same way for every user and on every instance of your server. A `401` for a missing or expired token has no effect on the extension. If any instance responds with another error, such as `-32601`, Claude can stop using the extension with your server for about a day after the last error.

### Check what each call declares

In `params._meta`, each `tools/call` request of revision 2026-07-28 can declare that the client supports `upload`, `download`, both, or neither. Treat a request of an older revision as declaring neither. Read the declaration on every call. If the declaration has a `revision` field with a value that you don't know, treat the extension as not declared. This `_meta` value declares both:

```json theme={null}
{
  "io.modelcontextprotocol/clientCapabilities": {
    "extensions": {
      "io.modelcontextprotocol/files": { "upload": {}, "download": {} }
    }
  }
}
```

If a call doesn't declare what a tool needs, respond in this way:

* **You advertise `upload`, the call doesn't declare it, and a [file argument](#mark-the-file-argument) has a `size` above 0 and no `data`**: return error `-32021` and don't run the tool. `data` is the extension's field for a file's bytes in the call itself. Claude doesn't send it in a call that declares `upload`.
* **The call doesn't declare `download`**: respond without a download target. In `content`, say that no file was delivered and, if you can, where the user can get it. If the tool can't work without the download, return error `-32021` and don't run the tool.

Name what is missing in the error's `data.requiredCapabilities`. On a call of revision 2026-07-28, send the error as a JSON body with HTTP status `400`. This error leaves out `jsonrpc` and `id`:

```json theme={null}
{
  "error": {
    "code": -32021,
    "message": "This app can't send files to this connector, so the tool didn't run.",
    "data": {
      "requiredCapabilities": {
        "extensions": { "io.modelcontextprotocol/files": { "upload": {} } }
      }
    }
  }
}
```

## Receive a file in a tool

In an upload, Claude calls your tool twice, and the bytes go to your storage between the two calls:

1. Claude calls the tool with the file's name, type, size, and digest
2. Your server responds with an upload target for the file
3. Anthropic's servers send the bytes to the target
4. Claude calls the tool again with the same arguments, and your server runs the tool

The JSON examples of uploads leave out `jsonrpc`, `id`, and `_meta`.

### Mark the file argument

A file argument is a tool argument that takes a user's file. To mark a file argument, add `x-mcp-file` to the object schema of a top-level argument. This tool takes a folder ID and a PDF:

```json theme={null}
{
  "name": "save_to_folder",
  "description": "Save a file to a folder",
  "annotations": { "title": "Save to folder", "readOnlyHint": false, "destructiveHint": true },
  "inputSchema": {
    "type": "object",
    "properties": {
      "folderId": { "type": "string" },
      "file": {
        "type": "object",
        "description": "A PDF of up to 50 MiB.",
        "x-mcp-file": { "accept": ["application/pdf"], "maxSize": 52428800 },
        "properties": {
          "id": { "type": "string", "minLength": 1, "maxLength": 128 },
          "name": { "type": "string" },
          "mimeType": { "type": "string" },
          "size": { "type": "integer", "minimum": 0 },
          "digest": {
            "type": "object",
            "properties": {
              "algorithm": { "const": "sha-256" },
              "value": { "type": "string" }
            },
            "required": ["algorithm", "value"]
          }
        },
        "required": ["id", "mimeType", "size"]
      }
    },
    "required": ["folderId", "file"]
  }
}
```

Copy the file object's `properties` and `required`. If you change them, Claude might not recognize the argument, and then calls that set it don't reach your server, or don't declare `upload`. These variations work, with `x-mcp-file` on the file object itself:

* **Optional file**: an `anyOf` of the file object and `{"type": "null"}`
* **Several files**: an array whose `items` is the file object
* **Digest that you verify**: `digest` added to the file object's `required`

Keep `x-mcp-file`, `allOf`, `anyOf`, and `oneOf` off the root of `inputSchema`. If the root has any of them, calls of the tool might not reach your server. Other root keywords, such as `patternProperties`, can stop file transfers.

Design the tool with these rules in mind:

* **Size and type**: state your limits in `description` as well, and check the size and type yourself. Claude can refuse a file over `maxSize` before it calls your tool, and `accept` is a hint.
* **Unknown types**: Claude takes `mimeType` from the file's name or its first bytes, and sends `application/octet-stream` for types that it doesn't know. Accept that value on the first call, and `text/plain` too if you take text files, such as JSON. Check the bytes on the second call.
* **Unverified fields**: don't assume that a field of the file argument is correct. Rely on `digest`, the SHA-256 of the bytes in base64url with no padding, only after you verify it.
* **New tool**: add the file argument to a new tool. A client without the extension can't reliably fill a file argument, so adding one to a tool that people use today can break that tool.
* **Tool list**: include the tool in every `tools/list` response to an account that you show it to, even if the request doesn't declare the extension. Then [check what each call declares](#check-what-each-call-declares).
* **Annotations**: in `annotations`, give a tool that saves a file a `title`, `readOnlyHint: false`, and `destructiveHint: true`. See [Provide tool annotations](https://claude.com/docs/connectors/building/review-criteria.md#provide-tool-annotations).
* **Validation**: check each call's arguments in your own code, with a validator that accepts `x-mcp-file`
* **Questions to the user**: don't return an input request from a tool that moves a file

### Return an upload target

On the first call of an upload, Claude sends the file's details and no bytes:

```json theme={null}
{
  "name": "save_to_folder",
  "arguments": {
    "folderId": "fld_8c1a",
    "file": {
      "id": "file-1",
      "name": "Q3 report.pdf",
      "mimeType": "application/pdf",
      "size": 41204133,
      "digest": {
        "algorithm": "sha-256",
        "value": "uU0nuZNNPgilLlLX2n2r-sSE7-N6U4D6ZVe-_rYh2sU"
      }
    }
  }
}
```

Check that the user can write to the destination, and check the quota, the type, and the size. If you can take the file, don't run the tool yet. Respond with a result whose `resultType` is `upload_required`, which asks Claude to send the file. This result is an upload request. List one target for each file that has a `size` above 0 and no `data`:

```json theme={null}
{
  "result": {
    "resultType": "upload_required",
    "uploads": [
      {
        "fileId": "file-1",
        "url": "https://upload.example.com/u/01JD3V7K2M?sig=...",
        "headers": { "Content-Type": "application/pdf" },
        "credentials": "omit"
      }
    ],
    "requestState": "..."
  }
}
```

Return the upload request as your response to Claude's first `tools/call`, and follow these rules:

* **Refusal**: if you can't take the file, return a result with `resultType` `"complete"`, `isError: true`, and a sentence in `content` that the user can act on. Refuse a call in which two files have the same `id`, or a file has `data` that you don't accept.
* **Target**: set `fileId` to the file's `id`. Claude sends a `PUT` unless you set `method` to `"POST"`. If your MCP server takes the upload itself, list `Content-Type: application/octet-stream`, so that its JSON parser leaves the body alone.
* **Form uploads**: if your storage takes nothing but `multipart/form-data`, use a target with the extension's [`form` field](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md#upload-request). Set `method` to `"POST"` and list no `Content-Type` header. The form's fields can carry the authorization and the staging place instead of the URL.
* **Lifetime**: keep the URL valid for at least 20 minutes after you return it, or 75 minutes if you return several targets. A large file can reach your storage that late.
* **Staging**: point each URL at its own randomly named place in a staging location, which takes one write and enforces the declared size. Show no staged file to users until the second call succeeds.
* **Signed headers**: if the URL's signature can cover headers, have it cover `Content-Length` and a write-once condition as headers, not in the query. Use a condition that your storage enforces, such as `If-None-Match: *`. List it in the target's `headers`, and leave `Content-Length` out. Without `form`, Claude sets `Content-Length` to the file's `size`.
* **Signed headers with `boto3`**: create the client with the bucket's region and `Config(signature_version="s3v4", s3={"addressing_style": "virtual"})`. In some regions, the default signature covers neither header. Use a bucket with no dot in its name. A dot puts the URL on a host that all customers share.
* **Checksum of an empty body**: if your signed URL's query holds `x-amz-checksum-crc32=AAAAAA%3D%3D`, it names the checksum of an empty body. Create your storage's JavaScript client with `requestChecksumCalculation: "WHEN_REQUIRED"`.
* **Empty files**: return no target for a file whose `size` is 0. If your schema requires `digest` and the digest doesn't match, return a result with `isError: true`. If no file needs a target, run the tool and return its result.
* **Repeated calls**: the first call can arrive more than once. Respond with a new target and a new `requestState` each time.

#### Build the `requestState` value

With `requestState`, your server matches the second call to the upload request that it issued. Your server creates this string, and Claude sends it back unchanged. Build it with these properties:

* **Contents**: tie it to the tool name, the arguments, each target, and the signed-in user's ID, and record that you issued an upload request. Leave out the access token, which can change between the two calls.
* **Protection**: keep the contents in storage that all your instances share, and use a random ID that looks them up as `requestState`. If you put the contents in the string itself, seal them with authenticated encryption and a key that all your instances hold.
* **Expiry**: make it expire after about an hour, or about two hours if you return several targets. Each target has to stop working before `requestState` expires.

### Accept the bytes of an upload

After your server returns an upload request, Anthropic's servers send each file to its target at most once. Unless the target has a `form` field, the body of the request is the file, with a `Content-Type` if you listed one. With `form`, the request is `multipart/form-data`. Each request has a `Content-Length` and the headers that you listed.

* **Success**: respond with a `2xx` status only after the whole file is stored. Claude ignores the response body. Send the response uncompressed.
* **Time**: receive the file within the [limits on file transfers](#limits-on-file-transfers)
* **Failure**: any other status fails the upload. If an upload fails, your server receives no second call, so delete staged bytes after `requestState` expires.

### Finish the upload on the second call

The second call of an upload has the same arguments as the first and adds `requestState` to `params`. The call doesn't prove that the bytes arrived. Complete these steps in order:

1. **State**: verify that you issued `requestState`, and that it hasn't expired or been used. If a check fails, return JSON-RPC error `-32602`.
2. **Call**: compare the tool name, the arguments, and the user with what `requestState` holds. Compare the arguments as JSON values, so that member order and number spelling don't matter. If they differ, return `-32602`.
3. **Files**: if the target can still overwrite the staged file, copy the file to a place in staging that is new for each call and that the target can't write. Use the copy from here on. Confirm with your storage that each file that you gave a target arrived, and check its size. Check its bytes if the tool restricts the type, and verify its digest if your schema requires one. If a check fails, return a result with `isError: true` and don't run the tool.
4. **Repeats**: if it's unsafe to run the tool twice, mark `requestState` as used in one atomic write to storage that all your instances share. If the string holds sealed contents, mark a random ID that you sealed in them, because another string can decode to the same contents. Keep the mark until `requestState` expires. If another call used it first, return `-32602`.
5. **Result**: finalize the file that you checked, copying it out of staging. Run the tool, and return its result. If you can't finalize the file, return a result with `isError: true` and don't run the tool. Keep the staged bytes until `requestState` expires.

Follow these rules as you check the files and return the result:

* **Digest**: hash the bytes yourself, or compare a SHA-256 that your storage computed. A value from the client or a weaker hash doesn't verify the file.
* **No second upload request**: don't answer the second call with another upload request
* **Secrets**: keep the upload URL and `requestState` out of results and errors
* **Time**: respond well within 60 seconds. If Claude doesn't receive your response in 60 seconds, it can tell the user that it doesn't know whether the tool ran.

### SDK support for file transfers

To receive uploads, use the low-level `Server` in the TypeScript or Python SDK. The samples were run with these versions:

* **TypeScript**: `@modelcontextprotocol/server` 2.4.0, served with `createMcpHandler`. Add `"content": []` to the upload request. Without it, the SDK responds with error `-32602`.
* **Python**: `mcp` 2.3.0. Return results as dictionaries that include `resultType`, and in `tools/list` results also `ttlMs` and `cacheScope`. Put a valid `content` list in each tool result. Without one, the SDK can drop `isError`, and a refusal looks like a success. Don't add `RequestStateBoundary`, which refuses the second call.

In Python, `MCPServer` in `mcp` 2.3.0 and `FastMCP` in `fastmcp` 4.0.10 turn an upload request that a tool returns into an ordinary result, so Claude sends no file.

The samples advertise the extension, require sign-in, read what a call declares, and answer the first call of an upload. They leave out your other tools, empty files, and your checks of the user's permissions, the quota, the type, and the size. Define these names yourself, above the sample:

* **Tools**: `listTools`, `createTarget`, and `secondCall` (in Python, `list_tools`, `create_target`, and `second_call`). `createTarget` returns a signed URL and `requestState`.
* **Sign-in in TypeScript**: `signIn` is Express middleware. It responds with a `401` that names [your discovery metadata](https://claude.com/docs/connectors/building/authentication.md#serve-discovery-metadata) to a request whose token is missing, invalid, expired, or issued for another server. For a valid token, it sets `req.auth`, which your code reads as `ctx.http?.authInfo`.
* **Sign-in in Python**: `AUTH` is an `AuthSettings` from the SDK, with your authorization server's URL as `issuer_url` and your connector's address as `resource_server_url`. Keep `AUTH` and `TOKEN_VERIFIER` in the sample. Without them, a call with no token reaches your tool.
* **Token check in Python**: `TOKEN_VERIFIER` is an object with an async `verify_token` method. It returns `None` for a token that is invalid, expired, or issued for another server, and an `AccessToken` for a valid one. Your code reads that with `get_access_token()` from `mcp.server.auth.middleware.auth_context`.

> [tab] TypeScript
>
> ```ts theme={null}
> import { createMcpHandler, ProtocolError, Server } from "@modelcontextprotocol/server";
> import { hostHeaderValidation, originValidation } from "@modelcontextprotocol/express";
> import { toNodeHandler } from "@modelcontextprotocol/node";
> import express from "express";
>
> const FILES = "io.modelcontextprotocol/files";
> const HOSTS = ["mcp.example.com"];
>
> function checkUpload(params: any, declared: any) {
>   const { file } = params.arguments;
>   const canUpload = declared.upload instanceof Object && !Array.isArray(declared.upload);
>   if (!canUpload && file.size > 0 && file.data === undefined) {
>     throw new ProtocolError(-32021, "This app can't send files to this connector, so the tool didn't run.", {
>       requiredCapabilities: { extensions: { [FILES]: { upload: {} } } }
>     });
>   }
> }
>
> async function firstCall(params: any, ctx: any): Promise<any> {
>   const { file } = params.arguments;
>   const { url, requestState } = await createTarget(params, ctx);
>   return {
>     resultType: "upload_required",
>     content: [],
>     uploads: [{ fileId: file.id, url, headers: { "Content-Type": file.mimeType }, credentials: "omit" }],
>     requestState
>   };
> }
>
> function makeServer() {
>   const server = new Server(
>     { name: "example", version: "1.0.0" },
>     { capabilities: { tools: {}, extensions: { [FILES]: { upload: {} } } } }
>   );
>   server.setRequestHandler("tools/list", listTools);
>   server.setRequestHandler("tools/call", async (request, ctx) => {
>     const envelope = (ctx.mcpReq.envelope ?? {}) as Record<string, any>;
>     // Treat a call of an older revision as declaring neither direction.
>     const isNew = envelope["io.modelcontextprotocol/protocolVersion"] >= "2026-07-28";
>     const settings = envelope["io.modelcontextprotocol/clientCapabilities"]?.extensions?.[FILES] ?? {};
>     // This server knows no "revision".
>     const declared = !isNew || "revision" in settings ? {} : settings;
>     try {
>       checkUpload(request.params, declared);
>       const state = ctx.mcpReq.requestState();
>       return state === undefined
>         ? await firstCall(request.params, ctx)
>         : await secondCall(request.params, declared, ctx, state);
>     } catch (error) {
>       if (error instanceof ProtocolError) throw error;
>       // Log the error's type, not its text, which can hold a URL.
>       return {
>         resultType: "complete",
>         isError: true,
>         content: [{ type: "text", text: "The tool failed. It might have done part of its work." }]
>       };
>     }
>   });
>   return server;
> }
>
> const app = express();
> app.use(hostHeaderValidation(HOSTS), originValidation(HOSTS));
> app.use("/mcp", signIn);
> const handler = toNodeHandler(createMcpHandler(makeServer, { responseMode: "json" }));
> app.all("/mcp", (req, res) => handler(req, res, req.body));
> app.listen(3000);
> ```

> [tab] Python
>
> ```python theme={null}
> from mcp.server.lowlevel import Server
> from mcp.server.transport_security import TransportSecuritySettings
> from mcp.shared.exceptions import MCPError
>
> FILES = "io.modelcontextprotocol/files"
>
> def check_upload(params, declared):
>     file = params.arguments.get("file", {})
>     # The value of "upload" is {}, which is false in Python, so test its type.
>     can_upload = isinstance(declared.get("upload"), dict)
>     if not can_upload and file["size"] > 0 and "data" not in file:
>         raise MCPError(
>             -32021,
>             "This app can't send files to this connector, so the tool didn't run.",
>             {"requiredCapabilities": {"extensions": {FILES: {"upload": {}}}}},
>         )
>
> async def first_call(params, ctx):
>     file = params.arguments["file"]
>     url, request_state = await create_target(params, ctx)
>     return {
>         "resultType": "upload_required",
>         "uploads": [{
>             "fileId": file["id"],
>             "url": url,
>             "headers": {"Content-Type": file["mimeType"]},
>             "credentials": "omit",
>         }],
>         "requestState": request_state,
>     }
>
> async def call_tool(ctx, params):
>     # Treat a call of an older revision as declaring neither direction.
>     meta = (ctx.protocol_version >= "2026-07-28" and ctx.meta) or {}
>     caps = meta.get("io.modelcontextprotocol/clientCapabilities") or {}
>     settings = (caps.get("extensions") or {}).get(FILES) or {}
>     # This server knows no "revision".
>     declared = {} if "revision" in settings else settings
>     try:
>         check_upload(params, declared)
>         if params.request_state is None:
>             return await first_call(params, ctx)
>         return await second_call(params, declared, ctx, params.request_state)
>     except MCPError:
>         raise
>     except Exception:
>         # Log the error's type, not its text, which can hold a URL.
>         return {
>             "resultType": "complete",
>             "isError": True,
>             "content": [{"type": "text", "text": "The tool failed. It might have done part of its work."}],
>         }
>
> server = Server("example", on_list_tools=list_tools, on_call_tool=call_tool)
> server.extensions[FILES] = {"upload": {}}
> app = server.streamable_http_app(
>     json_response=True,
>     transport_security=TransportSecuritySettings(allowed_hosts=["mcp.example.com"]),
>     auth=AUTH,
>     token_verifier=TOKEN_VERIFIER,
> )
> ```

In `firstCall` and `secondCall`, throw the errors that you mean to send, such as `-32602`. The samples turn every other exception there into a result with `isError: true`. In `listTools`, catch exceptions yourself and throw error `-32603` with your own message (in Python, with `from None`). Otherwise, an exception's text can reach Claude or your logs, with any URL in it.

In TypeScript, don't run a body parser on `/mcp`, and don't use `createMcpExpressApp()`, which adds `express.json()`. By default, that parser refuses a call over 100 KiB. Express can also log a call that the parser can't read, including its `requestState`.

To confirm that your library sends the upload request's `resultType`, `uploads`, and `requestState` unchanged, [test your server with curl](#test-your-server-with-curl).

## Return a file from a tool

In a download, your tool's result says where the file is, and Anthropic's servers get it from there. The JSON example leaves out `jsonrpc` and `id`.

### List the file in the result

Add a download target for each file to the result's `_meta`, and describe the file in `content`. If the result has `structuredContent`, describe the file in that field too. This result returns one CSV file:

```json theme={null}
{
  "result": {
    "resultType": "complete",
    "content": [{ "type": "text", "text": "Offering q3-orders.csv for download." }],
    "_meta": {
      "io.modelcontextprotocol/files": {
        "downloads": [
          {
            "name": "q3-orders.csv",
            "mimeType": "text/csv",
            "size": 20971520,
            "digest": {
              "algorithm": "sha-256",
              "value": "Oc8Nw8lkNGMsrnY87ttPsxM_LQMU2sEeeLbd6zmwGmI"
            },
            "url": "https://download.example.com/d/01JD3V9P4Q?sig=...",
            "credentials": "omit"
          }
        ]
      }
    }
  }
}
```

Write each target with these rules in mind:

* **URL**: give the address that responds with the file itself. If your API redirects to storage, have your server request the file without following the redirect. Give the storage address that the `Location` header names, which has to be on an approved host. Following the redirect can use up a single-use URL.
* **Permission**: before you create the URL, check that the user can read the file
* **Size and type**: state the exact `size` and the real `mimeType`
* **Digest**: state the SHA-256 of the whole file if you have it, in base64url with no padding. The download fails if the bytes don't match `size` or `digest`.
* **Name**: give a file name with an extension and no folders. Claude can shorten or change the name.
* **Ready files**: list a file only after it's ready to fetch, and don't change the file while its URL is valid
* **Lifetime**: keep the URL valid for about an hour, and let it serve more than one `GET` if your storage can
* **No copies**: don't repeat the URL, its query string or a long value from it, a token from its path, or a header's value elsewhere in the result, and add no other signed link to your storage. A copy can cause Claude to leave the file out or replace the result with an error.
* **When to return a file**: return a target from a tool that is meant to hand over a file, such as an export, in a result without `isError: true`. Make the tool safe to repeat.

### Serve the download

Claude can fetch a file whole. With `"omit"`, it can also fetch the file in parts, or from where an earlier request stopped. Set up your storage to answer these requests:

* **`GET` for a whole file**: respond with status `200` and the whole file
* **`GET` with a `Range` header**: respond with status `206`, the bytes that the header asks for, and a `Content-Range` header. If your storage can't serve parts, respond with `200` and the whole file. A file too large for one request then can't be fetched.
* **`ETag`**: send the same strong `ETag` in each response if you can. Without it, Claude might not finish a large download.
* **Encoding**: send the file uncompressed

A redirect or any other status fails the download.

## Limits on file transfers

Keep each transfer within these limits:

| What is limited | Limit | If you exceed the limit |
| - | - | - |
| Files in one call of an upload | 10. Claude Code sends up to 8. | A call with more files doesn't reach your server |
| Files in one download result | 10 | Claude leaves out the rest |
| Time to respond to each call, including both calls of an upload | 60 seconds | Claude can tell the user that it doesn't know whether the tool ran |
| Time for both calls of an upload and all their files, in a Claude chat | About 200 seconds | The upload fails, or Claude can tell the user that it doesn't know whether the tool ran |
| Response that finishes an upload, asks Claude to send a file, or returns a file | Under 1,000,000 bytes, with room to spare. The bytes at a target don't count. | Claude can refuse the response |
| Time to receive an upload and respond | The longer of 80 seconds, or 30 seconds plus 1 second for each 4 MiB | The upload fails |
| Time to respond after an upload's last byte | 60 seconds, which also count toward the time to receive the upload | The upload fails |
| Pause in reading an upload | 30 seconds | The upload fails |
| Time to start responding to a `GET` | 30 seconds | The download fails |
| Time to send the body of a `GET` response | 30 seconds plus 1 second for each 256 KiB, with at least 1.875 MiB in any 30 seconds | The download fails |
| Total time of one `GET` | 290 seconds | The download fails |
| Target URL | 8,192 bytes | Claude refuses the upload request, or leaves the file out of a download |
| Target headers | 16 headers, with names up to 128 bytes and values up to 4,096 bytes | The same results as for the URL |
| Form of an upload target | 32 fields. Names up to 128 bytes, values up to 8,192 bytes, and 65,536 bytes in all. | Claude refuses the upload request |
| `requestState` | Keep it under 32,000 ASCII characters | Claude can refuse the upload request |

Send each result with HTTP status `200`. Under another status, Claude might read it as an error, or not at all.

## Test file transfers

Test your server on its own first, and then test it in Claude Code.

### Test your server with curl

In your terminal, send the first call of an upload to your own address, with your own token, tool, and arguments. The tool's name is in the `Mcp-Name` header and in `params`. Set `size` to the size of a file that you have, and add `digest` if your schema requires it:

```bash theme={null}
curl --include 'https://mcp.example.com/mcp' \
  --header 'Authorization: Bearer TOKEN' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json, text/event-stream' \
  --header 'MCP-Protocol-Version: 2026-07-28' \
  --header 'Mcp-Method: tools/call' \
  --header 'Mcp-Name: save_to_folder' \
  --data '{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {
    "name": "save_to_folder",
    "arguments": {"folderId": "fld_8c1a", "file": {
      "id": "file-1", "name": "Q3 report.pdf",
      "mimeType": "application/pdf", "size": 41204133}},
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": {"name": "test", "version": "1"},
      "io.modelcontextprotocol/clientCapabilities": {"extensions": {
        "io.modelcontextprotocol/files": {"upload": {}, "download": {}}}}}}}'
```

Your server responds with `"resultType": "upload_required"`, a target, and `requestState`. Next, test the rest of the upload:

1. From a machine outside your network, send the file to the target's URL. Replace `FILE` and `URL`, and use your target's method and headers:

   ```bash theme={null}
   curl --http1.1 --ipv4 --request PUT --data-binary @FILE \
     --header 'Content-Type: application/pdf' --header 'Expect:' --max-time 80 \
     --output /dev/null --write-out '%{http_code}\n' 'URL'
   ```

   The command prints your storage's status, such as `200`. If the target lists no `Content-Type`, write `--header 'Content-Type:'`, so that curl doesn't add its own. For a file over 200 MiB, raise `--max-time` to 30 plus one second for each 4 MiB.
2. Send the first call again, with `"id": 1` changed to `"id": 2`. Add `"requestState": "..."` beside `"name"`, with the value that your server returned. The tool runs, and your server responds with its result.
3. Check that your server refuses these calls without running the tool. Start each check with a new first call:
   * **Changed argument, another user, or a letter of `requestState` changed in the middle or 10 places from either end**: your server responds with `-32602`
   * **No token, or a made-up token**: your server responds with `401`
   * **No upload, or bytes of another size**: your server responds with `isError: true`
   * **No `upload` in the first call's declaration**: your server responds with `-32021`
   * **A repeat of a second call that succeeded**: if it's unsafe to run the tool twice, your server responds with `-32602`
   * **Two copies of a second call, sent at once**: if it's unsafe to run the tool twice, your server runs it once, and responds to the other copy with `-32602` or `isError: true`

For a download, call your tool in the same way, for a file of at least 300 bytes that doesn't repeat. Then fetch its target's URL with `curl`, once whole and once with `--range 100-199`. If the URL is single-use, get a new one for the second fetch. If your storage serves parts, it responds with `200`, and then with `206` and the file's bytes 100 to 199.

### Test in Claude Code

To test with Claude, you need a published directory listing with [approved hosts](#request-approval-for-your-hosts). To get a listing, [submit your connector](https://claude.com/docs/connectors/building/submission.md). Use the connector as added from that listing, and an [account that has file transfers](#requirements-for-file-transfers).

By default, everyone who uses your connector can see a new tool once you deploy it. To test the tool before other people see it, include it in `tools/list` responses only for your test accounts. Set `cacheScope` to `"private"` in all your `tools/list` responses.

Claude can keep an account's `tools/list` response for up to about six hours, so add each test account before it connects to your connector. If an account connected first, the new tool can take that long to appear.

1. In [your connectors](https://claude.ai/customize/connectors/yours), remove the connector if you added it by URL, and [add it from the directory](https://claude.com/docs/connectors/directory.md)
2. Remove or disable every other entry for your server in Claude Code, such as one from a plugin or an administrator. Claude Code uses that entry in place of the connector. To find or turn off an entry, run `/mcp` at the Claude Code prompt. It lists a replaced connector as hidden. For an entry that you added, run `claude mcp remove` with its name in your terminal.
3. If Anthropic gave you a Claude Code version to test with, [install that version](https://code.claude.com/docs/en/setup#install-a-specific-version), [turn off auto-updates](https://code.claude.com/docs/en/setup#disable-auto-updates), and start it in your terminal. Otherwise, start the newest version from the [`latest` release channel](https://code.claude.com/docs/en/setup#configure-release-channel). Sign in with the Claude account that you added the connector to, with no API key set. Then quit, and start an interactive session in a new terminal, not in plan mode or Don't Ask mode.
4. At the Claude Code prompt, ask Claude to send a test file from the folder where you started it to your tool, or to get one from your tool
5. Approve the tool call and the transfer when Claude asks

After an upload, the file is in your product. After a download, your storage has served a `GET` for the file.

## Troubleshoot file transfers

Read the tool result in Claude Code first, because it can say why a transfer failed. Your server isn't told when Claude refuses its response. If the result gives no reason, check which requests reached your server and your storage, and find that symptom in this list:

* **No file moves, and Claude shows no error**: check the [requirements](#requirements-for-file-transfers) and each step of the [test in Claude Code](#test-in-claude-code). Then check for these causes:
  * Your server responded to `server/discover` with an error in the last day. Wait a day, and start a new session.
  * `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set. Claude Code doesn't transfer files in that session, so unset all of them.
* **Your server receives no call**: check the server's address against your listing, and the tool's schema against the [file argument](#mark-the-file-argument)
* **Your Python server responds with `500`, and its log says "Task group is not initialized"**: you mounted `app` in another app. Serve it as its own process.
* **Your server responds with `421`, or with `403` and `Invalid Host`**: list your host name in `allowed_hosts` (Python) or `hostHeaderValidation` (TypeScript)
* **Your server refuses a browser-based client with `403` and `Invalid Origin`**: list the client's origin in `allowed_origins` (Python) or its host name in `originValidation` (TypeScript)
* **The result includes "has not approved this connector's current address"**: you added or changed a server URL on your listing after Anthropic approved your hosts. [Request approval again](#request-approval-for-your-hosts).
* **Your server receives the first call, and your storage receives no upload**: check the URL's host against the [requirements](#requirements-for-file-transfers), an `include` target against [its rules](#targets-with-include-credentials), and your server's response against the [upload request](#return-an-upload-target)
* **Your storage receives an upload, and your server receives no second call**: check how your storage [responds to the upload](#accept-the-bytes-of-an-upload), such as with a redirect, too late, or before it had the whole file
* **Your server returns a download target, and your storage receives no `GET`**: check the URL's host against the [requirements](#requirements-for-file-transfers), and check that Claude Code isn't in plan mode. Compare the target with the [rules for targets](#urls-headers-and-fields-of-a-target), and an `include` target with [its rules](#targets-with-include-credentials).
* **An error replaces your tool's result**: look for a copy of the download URL outside its target, a header name listed twice, or a response over its [limit](#limits-on-file-transfers)
* **Your storage receives a `GET`, and the download fails**: compare the status, size, digest, and `ETag` that your storage sends with [what Claude expects](#serve-the-download)

## Next steps

* [File Uploads and Downloads extension](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md): read the complete rules for servers
* [Connector pre-submission checklist](https://claude.com/docs/connectors/building/review-criteria.md): check your tools before you submit your connector
* [Troubleshoot your connector](https://claude.com/docs/connectors/building/troubleshooting.md): fix connection and sign-in failures
