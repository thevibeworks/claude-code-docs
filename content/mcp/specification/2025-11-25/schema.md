> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Schema Reference

## JSON-RPC

### `JSONRPCErrorResponse`

interface JSONRPCErrorResponse \{\
  [jsonrpc](#jsonrpcerrorresponse-jsonrpc): "2.0";\
  [id](#jsonrpcerrorresponse-id)?: [RequestId](#requestid);\
  [error](#jsonrpcerrorresponse-error): [Error](#error);\
}A response to a request that indicates an error occurred.  jsonrpc: "2.0"[Permalink](#jsonrpcerrorresponse-jsonrpc)  id?: RequestId[Permalink](#jsonrpcerrorresponse-id)  error: Error[Permalink](#jsonrpcerrorresponse-error)&#x20;

### `JSONRPCMessage`

JSONRPCMessage: [JSONRPCRequest](#jsonrpcrequest) | [JSONRPCNotification](#jsonrpcnotification) | [JSONRPCResponse](#jsonrpcresponse)Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.&#x20;

### `JSONRPCNotification`

interface JSONRPCNotification \{\
  [method](#jsonrpcnotification-method): string;\
  [params](#jsonrpcnotification-params)?: \{ \[key: string]: any };\
  [jsonrpc](#jsonrpcnotification-jsonrpc): "2.0";\
}A notification which does not expect a response.  method: string[Permalink](#jsonrpcnotification-method)  Inherited from Notification.method params?: \{ \[key: string]: any }[Permalink](#jsonrpcnotification-params)  Inherited from Notification.params jsonrpc: "2.0"[Permalink](#jsonrpcnotification-jsonrpc)&#x20;

### `JSONRPCRequest`

interface JSONRPCRequest \{\
  [method](#jsonrpcrequest-method): string;\
  [params](#jsonrpcrequest-params)?: \{ \[key: string]: any };\
  [jsonrpc](#jsonrpcrequest-jsonrpc): "2.0";\
  [id](#jsonrpcrequest-id): [RequestId](#requestid);\
}A request that expects a response.  method: string[Permalink](#jsonrpcrequest-method)  Inherited from Request.method params?: \{ \[key: string]: any }[Permalink](#jsonrpcrequest-params)  Inherited from Request.params jsonrpc: "2.0"[Permalink](#jsonrpcrequest-jsonrpc)  id: RequestId[Permalink](#jsonrpcrequest-id)&#x20;

### `JSONRPCResponse`

JSONRPCResponse: [JSONRPCResultResponse](#jsonrpcresultresponse) | [JSONRPCErrorResponse](#jsonrpcerrorresponse)A response to a request, containing either the result or error.&#x20;

### `JSONRPCResultResponse`

interface JSONRPCResultResponse \{\
  [jsonrpc](#jsonrpcresultresponse-jsonrpc): "2.0";\
  [id](#jsonrpcresultresponse-id): [RequestId](#requestid);\
  [result](#jsonrpcresultresponse-result): [Result](#result);\
}A successful (non-error) response to a request.  jsonrpc: "2.0"[Permalink](#jsonrpcresultresponse-jsonrpc)  id: RequestId[Permalink](#jsonrpcresultresponse-id)  result: Result[Permalink](#jsonrpcresultresponse-result)&#x20;

## Common Types

### `Annotations`

interface Annotations \{\
  [audience](#annotations-audience)?: [Role](#role)\[];\
  [priority](#annotations-priority)?: number;\
  [lastModified](#annotations-lastmodified)?: string;\
}Optional annotations for the client. The client can use annotations to inform how objects are used or displayed  audience?: Role\[][Permalink](#annotations-audience) Describes who the intended audience of this object or data is. It can include multiple entries to indicate content useful for multiple audiences (e.g., `["user", "assistant"]`).  priority?: number[Permalink](#annotations-priority) Describes how important this data is for operating the server. A value of 1 means "most important," and indicates that the data is
effectively required, while 0 means "least important," and indicates that
the data is entirely optional.  lastModified?: string[Permalink](#annotations-lastmodified) The moment the resource was last modified, as an ISO 8601 formatted string. Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z"). Examples: last activity timestamp in an open file, timestamp when the resource
was attached, etc.&#x20;

### `Cursor`

Cursor: stringAn opaque token used to represent a cursor for pagination.&#x20;

### `EmptyResult`

EmptyResult: [Result](#result)A response that indicates success but carries no data.&#x20;

### `Error`

interface Error \{\
  [code](#error-code): number;\
  [message](#error-message): string;\
  [data](#error-data)?: unknown;\
} code: number[Permalink](#error-code) The error type that occurred.  message: string[Permalink](#error-message) A short description of the error. The message SHOULD be limited to a concise single sentence.  data?: unknown[Permalink](#error-data) Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.).&#x20;

### `Icon`

interface Icon \{\
  [src](#icon-src): string;\
  [mimeType](#icon-mimetype)?: string;\
  [sizes](#icon-sizes)?: string\[];\
  [theme](#icon-theme)?: "light" | "dark";\
}An optionally-sized icon that can be displayed in a user interface.  src: string[Permalink](#icon-src) A standard URI pointing to an icon resource. May be an HTTP/HTTPS URL or a `data:` URI with Base64-encoded image data. Consumers SHOULD takes steps to ensure URLs serving icons are from the
same domain as the client/server or a trusted domain. Consumers SHOULD take appropriate precautions when consuming SVGs as they can contain
executable JavaScript.  mimeType?: string[Permalink](#icon-mimetype) Optional MIME type override if the source MIME type is missing or generic.
For example: `"image/png"`, `"image/jpeg"`, or `"image/svg+xml"`.  sizes?: string\[][Permalink](#icon-sizes) Optional array of strings that specify sizes at which the icon can be used.
Each string should be in WxH format (e.g., `"48x48"`, `"96x96"`) or `"any"` for scalable formats like SVG. If not provided, the client should assume that the icon can be used at any size.  theme?: "light" | "dark"[Permalink](#icon-theme) Optional specifier for the theme this icon is designed for. `light` indicates
the icon is designed to be used with a light background, and `dark` indicates
the icon is designed to be used with a dark background. If not provided, the client should assume the icon can be used with any theme.&#x20;

### `LoggingLevel`

LoggingLevel:\
  | "debug"\
  | "info"\
  | "notice"\
  | "warning"\
  | "error"\
  | "critical"\
  | "alert"\
  | "emergency"The severity of a log message. These map to syslog message severities, as specified in RFC-5424: [[https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)](https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1)&#x20;

### `ProgressToken`

ProgressToken: string | numberA progress token, used to associate progress notifications with the original request.&#x20;

### `RequestId`

RequestId: string | numberA uniquely identifying ID for a request in JSON-RPC.&#x20;

### `Result`

interface Result \{\
  [\_meta](#result-_meta)?: \{ \[key: string]: unknown };\
  \[key: string]: unknown;\
} \_meta?: \{ \[key: string]: unknown }[Permalink](#result-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `Role`

Role: "user" | "assistant"The sender or recipient of messages and data in a conversation.&#x20;

## Content

### `AudioContent`

interface AudioContent \{\
  [type](#audiocontent-type): "audio";\
  [data](#audiocontent-data): string;\
  [mimeType](#audiocontent-mimetype): string;\
  [annotations](#audiocontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#audiocontent-_meta)?: \{ \[key: string]: unknown };\
}Audio provided to or from an LLM.  type: "audio"[Permalink](#audiocontent-type)  data: string[Permalink](#audiocontent-data) The base64-encoded audio data.  mimeType: string[Permalink](#audiocontent-mimetype) The MIME type of the audio. Different providers may support different audio types.  annotations?: Annotations[Permalink](#audiocontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#audiocontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `BlobResourceContents`

interface BlobResourceContents \{\
  [uri](#blobresourcecontents-uri): string;\
  [mimeType](#blobresourcecontents-mimetype)?: string;\
  [\_meta](#blobresourcecontents-_meta)?: \{ \[key: string]: unknown };\
  [blob](#blobresourcecontents-blob): string;\
} uri: string[Permalink](#blobresourcecontents-uri) The URI of this resource.  Inherited from ResourceContents.uri mimeType?: string[Permalink](#blobresourcecontents-mimetype) The MIME type of this resource, if known.  Inherited from ResourceContents.mimeType \_meta?: \{ \[key: string]: unknown }[Permalink](#blobresourcecontents-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from ResourceContents.\_meta blob: string[Permalink](#blobresourcecontents-blob) A base64-encoded string representing the binary data of the item.&#x20;

### `ContentBlock`

ContentBlock:\
  | [TextContent](#textcontent)\
  | [ImageContent](#imagecontent)\
  | [AudioContent](#audiocontent)\
  | [ResourceLink](#resourcelink)\
  | [EmbeddedResource](#embeddedresource)

### `EmbeddedResource`

interface EmbeddedResource \{\
  [type](#embeddedresource-type): "resource";\
  [resource](#embeddedresource-resource): [TextResourceContents](#textresourcecontents) | [BlobResourceContents](#blobresourcecontents);\
  [annotations](#embeddedresource-annotations)?: [Annotations](#annotations);\
  [\_meta](#embeddedresource-_meta)?: \{ \[key: string]: unknown };\
}The contents of a resource, embedded into a prompt or tool call result. It is up to the client how best to render embedded resources for the benefit
of the LLM and/or the user.  type: "resource"[Permalink](#embeddedresource-type)  resource: TextResourceContents | BlobResourceContents[Permalink](#embeddedresource-resource)  annotations?: Annotations[Permalink](#embeddedresource-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#embeddedresource-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ImageContent`

interface ImageContent \{\
  [type](#imagecontent-type): "image";\
  [data](#imagecontent-data): string;\
  [mimeType](#imagecontent-mimetype): string;\
  [annotations](#imagecontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#imagecontent-_meta)?: \{ \[key: string]: unknown };\
}An image provided to or from an LLM.  type: "image"[Permalink](#imagecontent-type)  data: string[Permalink](#imagecontent-data) The base64-encoded image data.  mimeType: string[Permalink](#imagecontent-mimetype) The MIME type of the image. Different providers may support different image types.  annotations?: Annotations[Permalink](#imagecontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#imagecontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ResourceLink`

interface ResourceLink \{\
  [icons](#resourcelink-icons)?: [Icon](#icon)\[];\
  [name](#resourcelink-name): string;\
  [title](#resourcelink-title)?: string;\
  [uri](#resourcelink-uri): string;\
  [description](#resourcelink-description)?: string;\
  [mimeType](#resourcelink-mimetype)?: string;\
  [annotations](#resourcelink-annotations)?: [Annotations](#annotations);\
  [size](#resourcelink-size)?: number;\
  [\_meta](#resourcelink-_meta)?: \{ \[key: string]: unknown };\
  [type](#resourcelink-type): "resource\_link";\
}A resource that the server is capable of reading, included in a prompt or tool call result. Note: resource links returned by tools are not guaranteed to appear in the results of `resources/list` requests.  icons?: Icon\[][Permalink](#resourcelink-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from [Resource](#resource).[icons](#resource-icons) name: string[Permalink](#resourcelink-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from [Resource](#resource).[name](#resource-name) title?: string[Permalink](#resourcelink-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from [Resource](#resource).[title](#resource-title) uri: string[Permalink](#resourcelink-uri) The URI of this resource.  Inherited from [Resource](#resource).[uri](#resource-uri) description?: string[Permalink](#resourcelink-description) A description of what this resource represents. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  Inherited from [Resource](#resource).[description](#resource-description) mimeType?: string[Permalink](#resourcelink-mimetype) The MIME type of this resource, if known.  Inherited from [Resource](#resource).[mimeType](#resource-mimetype) annotations?: Annotations[Permalink](#resourcelink-annotations) Optional annotations for the client.  Inherited from [Resource](#resource).[annotations](#resource-annotations) size?: number[Permalink](#resourcelink-size) The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known. This can be used by Hosts to display file sizes and estimate context window usage.  Inherited from [Resource](#resource).[size](#resource-size) \_meta?: \{ \[key: string]: unknown }[Permalink](#resourcelink-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Resource](#resource).[\_meta](#resource-_meta) type: "resource\_link"[Permalink](#resourcelink-type)&#x20;

### `TextContent`

interface TextContent \{\
  [type](#textcontent-type): "text";\
  [text](#textcontent-text): string;\
  [annotations](#textcontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#textcontent-_meta)?: \{ \[key: string]: unknown };\
}Text provided to or from an LLM.  type: "text"[Permalink](#textcontent-type)  text: string[Permalink](#textcontent-text) The text content of the message.  annotations?: Annotations[Permalink](#textcontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#textcontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `TextResourceContents`

interface TextResourceContents \{\
  [uri](#textresourcecontents-uri): string;\
  [mimeType](#textresourcecontents-mimetype)?: string;\
  [\_meta](#textresourcecontents-_meta)?: \{ \[key: string]: unknown };\
  [text](#textresourcecontents-text): string;\
} uri: string[Permalink](#textresourcecontents-uri) The URI of this resource.  Inherited from ResourceContents.uri mimeType?: string[Permalink](#textresourcecontents-mimetype) The MIME type of this resource, if known.  Inherited from ResourceContents.mimeType \_meta?: \{ \[key: string]: unknown }[Permalink](#textresourcecontents-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from ResourceContents.\_meta text: string[Permalink](#textresourcecontents-text) The text of the item. This must only be set if the item can actually be represented as text (not binary data).&#x20;

## `completion/complete`

### `CompleteRequest`

interface CompleteRequest \{\
  [jsonrpc](#completerequest-jsonrpc): "2.0";\
  [id](#completerequest-id): [RequestId](#requestid);\
  [method](#completerequest-method): "completion/complete";\
  [params](#completerequest-params): [CompleteRequestParams](#completerequestparams);\
}A request from the client to the server, to ask for completion options.  jsonrpc: "2.0"[Permalink](#completerequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#completerequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "completion/complete"[Permalink](#completerequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: CompleteRequestParams[Permalink](#completerequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `CompleteRequestParams`

interface CompleteRequestParams \{\
  [\_meta](#completerequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [ref](#completerequestparams-ref): [PromptReference](#promptreference) | [ResourceTemplateReference](#resourcetemplatereference);\
  [argument](#completerequestparams-argument): \{ name: string; value: string };\
  [context](#completerequestparams-context)?: \{ arguments?: \{ \[key: string]: string } };\
}Parameters for a `completion/complete` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#completerequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from RequestParams.\_meta ref: PromptReference | ResourceTemplateReference[Permalink](#completerequestparams-ref)  argument: \{ name: string; value: string }[Permalink](#completerequestparams-argument) The argument's information   Type Declaration <ul> <li> name: string The name of the argument </li> <li> value: string The value of the argument to use for completion matching. </li></ul> context?: \{ arguments?: \{ \[key: string]: string } }[Permalink](#completerequestparams-context) Additional, optional context for completions   Type Declaration <ul> <li> `Optional`arguments?: \{ \[key: string]: string } Previously-resolved variables in a URI template or prompt. </li></ul>

### `CompleteResult`

interface CompleteResult \{\
  [\_meta](#completeresult-_meta)?: \{ \[key: string]: unknown };\
  [completion](#completeresult-completion): \{ values: string\[]; total?: number; hasMore?: boolean };\
  \[key: string]: unknown;\
}The server's response to a completion/complete request  \_meta?: \{ \[key: string]: unknown }[Permalink](#completeresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) completion: \{ values: string\[]; total?: number; hasMore?: boolean }[Permalink](#completeresult-completion)  Type Declaration <ul> <li> values: string\[] An array of completion values. Must not exceed 100 items. </li> <li> `Optional`total?: number The total number of completion options available. This can exceed the number of values actually sent in the response. </li> <li> `Optional`hasMore?: boolean Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown. </li></ul>

### `PromptReference`

interface PromptReference \{\
  [name](#promptreference-name): string;\
  [title](#promptreference-title)?: string;\
  [type](#promptreference-type): "ref/prompt";\
}Identifies a prompt.  name: string[Permalink](#promptreference-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#promptreference-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title type: "ref/prompt"[Permalink](#promptreference-type)&#x20;

### `ResourceTemplateReference`

interface ResourceTemplateReference \{\
  [type](#resourcetemplatereference-type): "ref/resource";\
  [uri](#resourcetemplatereference-uri): string;\
}A reference to a resource or resource template definition.  type: "ref/resource"[Permalink](#resourcetemplatereference-type)  uri: string[Permalink](#resourcetemplatereference-uri) The URI or URI template of the resource.&#x20;

## `elicitation/create`

### `ElicitRequest`

interface ElicitRequest \{\
  [jsonrpc](#elicitrequest-jsonrpc): "2.0";\
  [id](#elicitrequest-id): [RequestId](#requestid);\
  [method](#elicitrequest-method): "elicitation/create";\
  [params](#elicitrequest-params): [ElicitRequestParams](#elicitrequestparams);\
}A request from the server to elicit additional information from the user via the client.  jsonrpc: "2.0"[Permalink](#elicitrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#elicitrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "elicitation/create"[Permalink](#elicitrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: ElicitRequestParams[Permalink](#elicitrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `ElicitRequestParams`

ElicitRequestParams: [ElicitRequestFormParams](#elicitrequestformparams) | [ElicitRequestURLParams](#elicitrequesturlparams)The parameters for a request to elicit additional information from the user via the client.&#x20;

### `ElicitResult`

interface ElicitResult \{\
  [\_meta](#elicitresult-_meta)?: \{ \[key: string]: unknown };\
  [action](#elicitresult-action): "accept" | "decline" | "cancel";\
  [content](#elicitresult-content)?: \{ \[key: string]: string | number | boolean | string\[] };\
  \[key: string]: unknown;\
}The client's response to an elicitation request.  \_meta?: \{ \[key: string]: unknown }[Permalink](#elicitresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) action: "accept" | "decline" | "cancel"[Permalink](#elicitresult-action) The user action in response to the elicitation. <ul> <li>"accept": User submitted the form/confirmed the action</li> <li>"decline": User explicitly decline the action</li> <li>"cancel": User dismissed without making an explicit choice</li> </ul>  content?: \{ \[key: string]: string | number | boolean | string\[] }[Permalink](#elicitresult-content) The submitted form data, only present when action is "accept" and mode was "form".
Contains values matching the requested schema.
Omitted for out-of-band mode responses.&#x20;

### `BooleanSchema`

interface BooleanSchema \{\
  [type](#booleanschema-type): "boolean";\
  [title](#booleanschema-title)?: string;\
  [description](#booleanschema-description)?: string;\
  [default](#booleanschema-default)?: boolean;\
} type: "boolean"[Permalink](#booleanschema-type)  title?: string[Permalink](#booleanschema-title)  description?: string[Permalink](#booleanschema-description)  default?: boolean[Permalink](#booleanschema-default)&#x20;

### `ElicitRequestFormParams`

interface ElicitRequestFormParams \{\
  [task](#elicitrequestformparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#elicitrequestformparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [mode](#elicitrequestformparams-mode)?: "form";\
  [message](#elicitrequestformparams-message): string;\
  [requestedSchema](#elicitrequestformparams-requestedschema): \{\
    \$schema?: string;\
    type: "object";\
    properties: \{ \[key: string]: [PrimitiveSchemaDefinition](#primitiveschemadefinition) };\
    required?: string\[];\
  };\
}The parameters for a request to elicit non-sensitive information from the user via a form in the client.  task?: TaskMetadata[Permalink](#elicitrequestformparams-task) If specified, the caller is requesting task-augmented execution for this request.
The request will return a CreateTaskResult immediately, and the actual result can be
retrieved later via tasks/result. Task augmentation is subject to capability negotiation - receivers MUST declare support
for task augmentation of specific request types in their capabilities.  Inherited from TaskAugmentedRequestParams.task \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#elicitrequestformparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from TaskAugmentedRequestParams.\_meta mode?: "form"[Permalink](#elicitrequestformparams-mode) The elicitation mode.  message: string[Permalink](#elicitrequestformparams-message) The message to present to the user describing what information is being requested.  requestedSchema: \{    \$schema?: string;    type: "object";    properties: \{ \[key: string]: PrimitiveSchemaDefinition };    required?: string\[]; }[Permalink](#elicitrequestformparams-requestedschema) A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting.&#x20;

### `ElicitRequestURLParams`

interface ElicitRequestURLParams \{\
  [task](#elicitrequesturlparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#elicitrequesturlparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [mode](#elicitrequesturlparams-mode): "url";\
  [message](#elicitrequesturlparams-message): string;\
  [elicitationId](#elicitrequesturlparams-elicitationid): string;\
  [url](#elicitrequesturlparams-url): string;\
}The parameters for a request to elicit information from the user via a URL in the client.  task?: TaskMetadata[Permalink](#elicitrequesturlparams-task) If specified, the caller is requesting task-augmented execution for this request.
The request will return a CreateTaskResult immediately, and the actual result can be
retrieved later via tasks/result. Task augmentation is subject to capability negotiation - receivers MUST declare support
for task augmentation of specific request types in their capabilities.  Inherited from TaskAugmentedRequestParams.task \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#elicitrequesturlparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from TaskAugmentedRequestParams.\_meta mode: "url"[Permalink](#elicitrequesturlparams-mode) The elicitation mode.  message: string[Permalink](#elicitrequesturlparams-message) The message to present to the user explaining why the interaction is needed.  elicitationId: string[Permalink](#elicitrequesturlparams-elicitationid) The ID of the elicitation, which must be unique within the context of the server.
The client MUST treat this ID as an opaque value.  url: string[Permalink](#elicitrequesturlparams-url) The URL that the user should navigate to.&#x20;

### `EnumSchema`

EnumSchema:\
  | [SingleSelectEnumSchema](#singleselectenumschema)\
  | [MultiSelectEnumSchema](#multiselectenumschema)\
  | [LegacyTitledEnumSchema](#legacytitledenumschema)

### `LegacyTitledEnumSchema`

interface LegacyTitledEnumSchema \{\
  [type](#legacytitledenumschema-type): "string";\
  [title](#legacytitledenumschema-title)?: string;\
  [description](#legacytitledenumschema-description)?: string;\
  [enum](#legacytitledenumschema-enum): string\[];\
  [enumNames](#legacytitledenumschema-enumnames)?: string\[];\
  [default](#legacytitledenumschema-default)?: string;\
}Use TitledSingleSelectEnumSchema instead.
This interface will be removed in a future version.  type: "string"[Permalink](#legacytitledenumschema-type)  title?: string[Permalink](#legacytitledenumschema-title)  description?: string[Permalink](#legacytitledenumschema-description)  enum: string\[][Permalink](#legacytitledenumschema-enum)  enumNames?: string\[][Permalink](#legacytitledenumschema-enumnames) (Legacy) Display names for enum values.
Non-standard according to JSON schema 2020-12.  default?: string[Permalink](#legacytitledenumschema-default)&#x20;

### `MultiSelectEnumSchema`

MultiSelectEnumSchema:\
  | [UntitledMultiSelectEnumSchema](#untitledmultiselectenumschema)\
  | [TitledMultiSelectEnumSchema](#titledmultiselectenumschema)

### `NumberSchema`

interface NumberSchema \{\
  [type](#numberschema-type): "number" | "integer";\
  [title](#numberschema-title)?: string;\
  [description](#numberschema-description)?: string;\
  [minimum](#numberschema-minimum)?: number;\
  [maximum](#numberschema-maximum)?: number;\
  [default](#numberschema-default)?: number;\
} type: "number" | "integer"[Permalink](#numberschema-type)  title?: string[Permalink](#numberschema-title)  description?: string[Permalink](#numberschema-description)  minimum?: number[Permalink](#numberschema-minimum)  maximum?: number[Permalink](#numberschema-maximum)  default?: number[Permalink](#numberschema-default)&#x20;

### `PrimitiveSchemaDefinition`

PrimitiveSchemaDefinition:\
  | [StringSchema](#stringschema)\
  | [NumberSchema](#numberschema)\
  | [BooleanSchema](#booleanschema)\
  | [EnumSchema](#enumschema)Restricted schema definitions that only allow primitive types
without nested objects or arrays.&#x20;

### `SingleSelectEnumSchema`

SingleSelectEnumSchema:\
  | [UntitledSingleSelectEnumSchema](#untitledsingleselectenumschema)\
  | [TitledSingleSelectEnumSchema](#titledsingleselectenumschema)

### `StringSchema`

interface StringSchema \{\
  [type](#stringschema-type): "string";\
  [title](#stringschema-title)?: string;\
  [description](#stringschema-description)?: string;\
  [minLength](#stringschema-minlength)?: number;\
  [maxLength](#stringschema-maxlength)?: number;\
  [format](#stringschema-format)?: "uri" | "email" | "date" | "date-time";\
  [default](#stringschema-default)?: string;\
} type: "string"[Permalink](#stringschema-type)  title?: string[Permalink](#stringschema-title)  description?: string[Permalink](#stringschema-description)  minLength?: number[Permalink](#stringschema-minlength)  maxLength?: number[Permalink](#stringschema-maxlength)  format?: "uri" | "email" | "date" | "date-time"[Permalink](#stringschema-format)  default?: string[Permalink](#stringschema-default)&#x20;

### `TitledMultiSelectEnumSchema`

interface TitledMultiSelectEnumSchema \{\
  [type](#titledmultiselectenumschema-type): "array";\
  [title](#titledmultiselectenumschema-title)?: string;\
  [description](#titledmultiselectenumschema-description)?: string;\
  [minItems](#titledmultiselectenumschema-minitems)?: number;\
  [maxItems](#titledmultiselectenumschema-maxitems)?: number;\
  [items](#titledmultiselectenumschema-items): \{ anyOf: \{ const: string; title: string }\[] };\
  [default](#titledmultiselectenumschema-default)?: string\[];\
}Schema for multiple-selection enumeration with display titles for each option.  type: "array"[Permalink](#titledmultiselectenumschema-type)  title?: string[Permalink](#titledmultiselectenumschema-title) Optional title for the enum field.  description?: string[Permalink](#titledmultiselectenumschema-description) Optional description for the enum field.  minItems?: number[Permalink](#titledmultiselectenumschema-minitems) Minimum number of items to select.  maxItems?: number[Permalink](#titledmultiselectenumschema-maxitems) Maximum number of items to select.  items: \{ anyOf: \{ const: string; title: string }\[] }[Permalink](#titledmultiselectenumschema-items) Schema for array items with enum options and display labels.   Type Declaration <ul> <li> anyOf: \{ const: string; title: string }\[] Array of enum options with values and display labels. </li></ul> default?: string\[][Permalink](#titledmultiselectenumschema-default) Optional default value.&#x20;

### `TitledSingleSelectEnumSchema`

interface TitledSingleSelectEnumSchema \{\
  [type](#titledsingleselectenumschema-type): "string";\
  [title](#titledsingleselectenumschema-title)?: string;\
  [description](#titledsingleselectenumschema-description)?: string;\
  [oneOf](#titledsingleselectenumschema-oneof): \{ const: string; title: string }\[];\
  [default](#titledsingleselectenumschema-default)?: string;\
}Schema for single-selection enumeration with display titles for each option.  type: "string"[Permalink](#titledsingleselectenumschema-type)  title?: string[Permalink](#titledsingleselectenumschema-title) Optional title for the enum field.  description?: string[Permalink](#titledsingleselectenumschema-description) Optional description for the enum field.  oneOf: \{ const: string; title: string }\[][Permalink](#titledsingleselectenumschema-oneof) Array of enum options with values and display labels.   Type Declaration <ul> <li> const: string The enum value. </li> <li> title: string Display label for this option. </li></ul> default?: string[Permalink](#titledsingleselectenumschema-default) Optional default value.&#x20;

### `UntitledMultiSelectEnumSchema`

interface UntitledMultiSelectEnumSchema \{\
  [type](#untitledmultiselectenumschema-type): "array";\
  [title](#untitledmultiselectenumschema-title)?: string;\
  [description](#untitledmultiselectenumschema-description)?: string;\
  [minItems](#untitledmultiselectenumschema-minitems)?: number;\
  [maxItems](#untitledmultiselectenumschema-maxitems)?: number;\
  [items](#untitledmultiselectenumschema-items): \{ type: "string"; enum: string\[] };\
  [default](#untitledmultiselectenumschema-default)?: string\[];\
}Schema for multiple-selection enumeration without display titles for options.  type: "array"[Permalink](#untitledmultiselectenumschema-type)  title?: string[Permalink](#untitledmultiselectenumschema-title) Optional title for the enum field.  description?: string[Permalink](#untitledmultiselectenumschema-description) Optional description for the enum field.  minItems?: number[Permalink](#untitledmultiselectenumschema-minitems) Minimum number of items to select.  maxItems?: number[Permalink](#untitledmultiselectenumschema-maxitems) Maximum number of items to select.  items: \{ type: "string"; enum: string\[] }[Permalink](#untitledmultiselectenumschema-items) Schema for the array items.   Type Declaration <ul> <li> type: "string"</li> <li> enum: string\[] Array of enum values to choose from. </li></ul> default?: string\[][Permalink](#untitledmultiselectenumschema-default) Optional default value.&#x20;

### `UntitledSingleSelectEnumSchema`

interface UntitledSingleSelectEnumSchema \{\
  [type](#untitledsingleselectenumschema-type): "string";\
  [title](#untitledsingleselectenumschema-title)?: string;\
  [description](#untitledsingleselectenumschema-description)?: string;\
  [enum](#untitledsingleselectenumschema-enum): string\[];\
  [default](#untitledsingleselectenumschema-default)?: string;\
}Schema for single-selection enumeration without display titles for options.  type: "string"[Permalink](#untitledsingleselectenumschema-type)  title?: string[Permalink](#untitledsingleselectenumschema-title) Optional title for the enum field.  description?: string[Permalink](#untitledsingleselectenumschema-description) Optional description for the enum field.  enum: string\[][Permalink](#untitledsingleselectenumschema-enum) Array of enum values to choose from.  default?: string[Permalink](#untitledsingleselectenumschema-default) Optional default value.&#x20;

## `initialize`

### `InitializeRequest`

interface InitializeRequest \{\
  [jsonrpc](#initializerequest-jsonrpc): "2.0";\
  [id](#initializerequest-id): [RequestId](#requestid);\
  [method](#initializerequest-method): "initialize";\
  [params](#initializerequest-params): [InitializeRequestParams](#initializerequestparams);\
}This request is sent from the client to the server when it first connects, asking it to begin initialization.  jsonrpc: "2.0"[Permalink](#initializerequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#initializerequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "initialize"[Permalink](#initializerequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: InitializeRequestParams[Permalink](#initializerequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `InitializeRequestParams`

interface InitializeRequestParams \{\
  [\_meta](#initializerequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [protocolVersion](#initializerequestparams-protocolversion): string;\
  [capabilities](#initializerequestparams-capabilities): [ClientCapabilities](#clientcapabilities);\
  [clientInfo](#initializerequestparams-clientinfo): [Implementation](#implementation);\
}Parameters for an `initialize` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#initializerequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from RequestParams.\_meta protocolVersion: string[Permalink](#initializerequestparams-protocolversion) The latest version of the Model Context Protocol that the client supports. The client MAY decide to support older versions as well.  capabilities: ClientCapabilities[Permalink](#initializerequestparams-capabilities)  clientInfo: Implementation[Permalink](#initializerequestparams-clientinfo)&#x20;

### `InitializeResult`

interface InitializeResult \{\
  [\_meta](#initializeresult-_meta)?: \{ \[key: string]: unknown };\
  [protocolVersion](#initializeresult-protocolversion): string;\
  [capabilities](#initializeresult-capabilities): [ServerCapabilities](#servercapabilities);\
  [serverInfo](#initializeresult-serverinfo): [Implementation](#implementation);\
  [instructions](#initializeresult-instructions)?: string;\
  \[key: string]: unknown;\
}After receiving an initialize request from the client, the server sends this response.  \_meta?: \{ \[key: string]: unknown }[Permalink](#initializeresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) protocolVersion: string[Permalink](#initializeresult-protocolversion) The version of the Model Context Protocol that the server wants to use. This may not match the version that the client requested. If the client cannot support this version, it MUST disconnect.  capabilities: ServerCapabilities[Permalink](#initializeresult-capabilities)  serverInfo: Implementation[Permalink](#initializeresult-serverinfo)  instructions?: string[Permalink](#initializeresult-instructions) Instructions describing how to use the server and its features. This can be used by clients to improve the LLM's understanding of available tools, resources, etc. It can be thought of like a "hint" to the model. For example, this information MAY be added to the system prompt.&#x20;

### `ClientCapabilities`

interface ClientCapabilities \{\
  [experimental](#clientcapabilities-experimental)?: \{ \[key: string]: object };\
  [roots](#clientcapabilities-roots)?: \{ listChanged?: boolean };\
  [sampling](#clientcapabilities-sampling)?: \{ context?: object; tools?: object };\
  [elicitation](#clientcapabilities-elicitation)?: \{ form?: object; url?: object };\
  [tasks](#clientcapabilities-tasks)?: \{\
    list?: object;\
    cancel?: object;\
    requests?: \{\
      sampling?: \{ createMessage?: object };\
      elicitation?: \{ create?: object };\
    };\
  };\
}Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.  experimental?: \{ \[key: string]: object }[Permalink](#clientcapabilities-experimental) Experimental, non-standard capabilities that the client supports.  roots?: \{ listChanged?: boolean }[Permalink](#clientcapabilities-roots) Present if the client supports listing roots.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether the client supports notifications for changes to the roots list. </li></ul> sampling?: \{ context?: object; tools?: object }[Permalink](#clientcapabilities-sampling) Present if the client supports sampling from an LLM.   Type Declaration <ul> <li> `Optional`context?: object Whether the client supports context inclusion via includeContext parameter.
If not declared, servers SHOULD only use `includeContext: "none"` (or omit it). </li> <li> `Optional`tools?: object Whether the client supports tool use via tools and toolChoice parameters. </li></ul> elicitation?: \{ form?: object; url?: object }[Permalink](#clientcapabilities-elicitation) Present if the client supports elicitation from the server.  tasks?: \{    list?: object;    cancel?: object;    requests?: \{        sampling?: \{ createMessage?: object };        elicitation?: \{ create?: object };    }; }[Permalink](#clientcapabilities-tasks) Present if the client supports task-augmented requests.   Type Declaration <ul> <li> `Optional`list?: object Whether this client supports tasks/list. </li> <li> `Optional`cancel?: object Whether this client supports tasks/cancel. </li> <li> `Optional`requests?: \{ sampling?: \{ createMessage?: object }; elicitation?: \{ create?: object } } Specifies which request types can be augmented with tasks.  <ul> <li> `Optional`sampling?: \{ createMessage?: object } Task support for sampling-related requests.  <ul> <li> `Optional`createMessage?: object Whether the client supports task-augmented sampling/createMessage requests. </li></ul></li> <li> `Optional`elicitation?: \{ create?: object } Task support for elicitation-related requests.  <ul> <li> `Optional`create?: object Whether the client supports task-augmented elicitation/create requests. </li></ul></li></ul></li></ul>

### `Implementation`

interface Implementation \{\
  [icons](#implementation-icons)?: [Icon](#icon)\[];\
  [name](#implementation-name): string;\
  [title](#implementation-title)?: string;\
  [version](#implementation-version): string;\
  [description](#implementation-description)?: string;\
  [websiteUrl](#implementation-websiteurl)?: string;\
}Describes the MCP implementation.  icons?: Icon\[][Permalink](#implementation-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from Icons.icons name: string[Permalink](#implementation-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#implementation-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title version: string[Permalink](#implementation-version)  description?: string[Permalink](#implementation-description) An optional human-readable description of what this implementation does. This can be used by clients or servers to provide context about their purpose
and capabilities. For example, a server might describe the types of resources
or tools it provides, while a client might describe its intended use case.  websiteUrl?: string[Permalink](#implementation-websiteurl) An optional URL of the website for this implementation.&#x20;

### `ServerCapabilities`

interface ServerCapabilities \{\
  [experimental](#servercapabilities-experimental)?: \{ \[key: string]: object };\
  [logging](#servercapabilities-logging)?: object;\
  [completions](#servercapabilities-completions)?: object;\
  [prompts](#servercapabilities-prompts)?: \{ listChanged?: boolean };\
  [resources](#servercapabilities-resources)?: \{ subscribe?: boolean; listChanged?: boolean };\
  [tools](#servercapabilities-tools)?: \{ listChanged?: boolean };\
  [tasks](#servercapabilities-tasks)?: \{\
    list?: object;\
    cancel?: object;\
    requests?: \{ tools?: \{ call?: object } };\
  };\
}Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.  experimental?: \{ \[key: string]: object }[Permalink](#servercapabilities-experimental) Experimental, non-standard capabilities that the server supports.  logging?: object[Permalink](#servercapabilities-logging) Present if the server supports sending log messages to the client.  completions?: object[Permalink](#servercapabilities-completions) Present if the server supports argument autocompletion suggestions.  prompts?: \{ listChanged?: boolean }[Permalink](#servercapabilities-prompts) Present if the server offers any prompt templates.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the prompt list. </li></ul> resources?: \{ subscribe?: boolean; listChanged?: boolean }[Permalink](#servercapabilities-resources) Present if the server offers any resources to read.   Type Declaration <ul> <li> `Optional`subscribe?: boolean Whether this server supports subscribing to resource updates. </li> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the resource list. </li></ul> tools?: \{ listChanged?: boolean }[Permalink](#servercapabilities-tools) Present if the server offers any tools to call.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the tool list. </li></ul> tasks?: \{    list?: object;    cancel?: object;    requests?: \{ tools?: \{ call?: object } }; }[Permalink](#servercapabilities-tasks) Present if the server supports task-augmented requests.   Type Declaration <ul> <li> `Optional`list?: object Whether this server supports tasks/list. </li> <li> `Optional`cancel?: object Whether this server supports tasks/cancel. </li> <li> `Optional`requests?: \{ tools?: \{ call?: object } } Specifies which request types can be augmented with tasks.  <ul> <li> `Optional`tools?: \{ call?: object } Task support for tool-related requests.  <ul> <li> `Optional`call?: object Whether the server supports task-augmented tools/call requests. </li></ul></li></ul></li></ul>

## `logging/setLevel`

### `SetLevelRequest`

interface SetLevelRequest \{\
  [jsonrpc](#setlevelrequest-jsonrpc): "2.0";\
  [id](#setlevelrequest-id): [RequestId](#requestid);\
  [method](#setlevelrequest-method): "logging/setLevel";\
  [params](#setlevelrequest-params): [SetLevelRequestParams](#setlevelrequestparams);\
}A request from the client to the server, to enable or adjust logging.  jsonrpc: "2.0"[Permalink](#setlevelrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#setlevelrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "logging/setLevel"[Permalink](#setlevelrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: SetLevelRequestParams[Permalink](#setlevelrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `SetLevelRequestParams`

interface SetLevelRequestParams \{\
  [\_meta](#setlevelrequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [level](#setlevelrequestparams-level): [LoggingLevel](#logginglevel);\
}Parameters for a `logging/setLevel` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#setlevelrequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from RequestParams.\_meta level: LoggingLevel[Permalink](#setlevelrequestparams-level) The level of logging that the client wants to receive from the server. The server should send all logs at this level and higher (i.e., more severe) to the client as notifications/message.&#x20;

## `notifications/cancelled`

### `CancelledNotification`

interface CancelledNotification \{\
  [jsonrpc](#cancellednotification-jsonrpc): "2.0";\
  [method](#cancellednotification-method): "notifications/cancelled";\
  [params](#cancellednotification-params): [CancelledNotificationParams](#cancellednotificationparams);\
}This notification can be sent by either side to indicate that it is cancelling a previously-issued request. The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished. This notification indicates that the result will be unused, so any associated processing SHOULD cease. A client MUST NOT attempt to cancel its `initialize` request. For task cancellation, use the `tasks/cancel` request instead of this notification.  jsonrpc: "2.0"[Permalink](#cancellednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/cancelled"[Permalink](#cancellednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: CancelledNotificationParams[Permalink](#cancellednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### `CancelledNotificationParams`

interface CancelledNotificationParams \{\
  [\_meta](#cancellednotificationparams-_meta)?: \{ \[key: string]: unknown };\
  [requestId](#cancellednotificationparams-requestid)?: [RequestId](#requestid);\
  [reason](#cancellednotificationparams-reason)?: string;\
}Parameters for a `notifications/cancelled` notification.  \_meta?: \{ \[key: string]: unknown }[Permalink](#cancellednotificationparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from NotificationParams.\_meta requestId?: RequestId[Permalink](#cancellednotificationparams-requestid) The ID of the request to cancel. This MUST correspond to the ID of a request previously issued in the same direction.
This MUST be provided for cancelling non-task requests.
This MUST NOT be used for cancelling tasks (use the `tasks/cancel` request instead).  reason?: string[Permalink](#cancellednotificationparams-reason) An optional string describing the reason for the cancellation. This MAY be logged or presented to the user.&#x20;

## `notifications/initialized`

### `InitializedNotification`

interface InitializedNotification \{\
  [jsonrpc](#initializednotification-jsonrpc): "2.0";\
  [method](#initializednotification-method): "notifications/initialized";\
  [params](#initializednotification-params)?: NotificationParams;\
}This notification is sent from the client to the server after initialization has finished.  jsonrpc: "2.0"[Permalink](#initializednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/initialized"[Permalink](#initializednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params?: NotificationParams[Permalink](#initializednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `notifications/tasks/status`

### `TaskStatusNotification`

interface TaskStatusNotification \{\
  [jsonrpc](#taskstatusnotification-jsonrpc): "2.0";\
  [method](#taskstatusnotification-method): "notifications/tasks/status";\
  [params](#taskstatusnotification-params): [TaskStatusNotificationParams](#taskstatusnotificationparams);\
}An optional notification from the receiver to the requestor, informing them that a task's status has changed. Receivers are not required to send these notifications.  jsonrpc: "2.0"[Permalink](#taskstatusnotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/tasks/status"[Permalink](#taskstatusnotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: TaskStatusNotificationParams[Permalink](#taskstatusnotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### `TaskStatusNotificationParams`

TaskStatusNotificationParams: NotificationParams & [Task](#task)Parameters for a `notifications/tasks/status` notification.&#x20;

## `notifications/message`

### `LoggingMessageNotification`

interface LoggingMessageNotification \{\
  [jsonrpc](#loggingmessagenotification-jsonrpc): "2.0";\
  [method](#loggingmessagenotification-method): "notifications/message";\
  [params](#loggingmessagenotification-params): [LoggingMessageNotificationParams](#loggingmessagenotificationparams);\
}JSONRPCNotification of a log message passed from server to client. If no logging/setLevel request has been sent from the client, the server MAY decide which messages to send automatically.  jsonrpc: "2.0"[Permalink](#loggingmessagenotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/message"[Permalink](#loggingmessagenotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: LoggingMessageNotificationParams[Permalink](#loggingmessagenotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### `LoggingMessageNotificationParams`

interface LoggingMessageNotificationParams \{\
  [\_meta](#loggingmessagenotificationparams-_meta)?: \{ \[key: string]: unknown };\
  [level](#loggingmessagenotificationparams-level): [LoggingLevel](#logginglevel);\
  [logger](#loggingmessagenotificationparams-logger)?: string;\
  [data](#loggingmessagenotificationparams-data): unknown;\
}Parameters for a `notifications/message` notification.  \_meta?: \{ \[key: string]: unknown }[Permalink](#loggingmessagenotificationparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from NotificationParams.\_meta level: LoggingLevel[Permalink](#loggingmessagenotificationparams-level) The severity of this log message.  logger?: string[Permalink](#loggingmessagenotificationparams-logger) An optional name of the logger issuing this message.  data: unknown[Permalink](#loggingmessagenotificationparams-data) The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here.&#x20;

## `notifications/progress`

### `ProgressNotification`

interface ProgressNotification \{\
  [jsonrpc](#progressnotification-jsonrpc): "2.0";\
  [method](#progressnotification-method): "notifications/progress";\
  [params](#progressnotification-params): [ProgressNotificationParams](#progressnotificationparams);\
}An out-of-band notification used to inform the receiver of a progress update for a long-running request.  jsonrpc: "2.0"[Permalink](#progressnotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/progress"[Permalink](#progressnotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: ProgressNotificationParams[Permalink](#progressnotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### `ProgressNotificationParams`

interface ProgressNotificationParams \{\
  [\_meta](#progressnotificationparams-_meta)?: \{ \[key: string]: unknown };\
  [progressToken](#progressnotificationparams-progresstoken): [ProgressToken](#progresstoken);\
  [progress](#progressnotificationparams-progress): number;\
  [total](#progressnotificationparams-total)?: number;\
  [message](#progressnotificationparams-message)?: string;\
}Parameters for a `notifications/progress` notification.  \_meta?: \{ \[key: string]: unknown }[Permalink](#progressnotificationparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from NotificationParams.\_meta progressToken: ProgressToken[Permalink](#progressnotificationparams-progresstoken) The progress token which was given in the initial request, used to associate this notification with the request that is proceeding.  progress: number[Permalink](#progressnotificationparams-progress) The progress thus far. This should increase every time progress is made, even if the total is unknown.  total?: number[Permalink](#progressnotificationparams-total) Total number of items to process (or total progress required), if known.  message?: string[Permalink](#progressnotificationparams-message) An optional message describing the current progress.&#x20;

## `notifications/prompts/list_changed`

### `PromptListChangedNotification`

interface PromptListChangedNotification \{\
  [jsonrpc](#promptlistchangednotification-jsonrpc): "2.0";\
  [method](#promptlistchangednotification-method): "notifications/prompts/list\_changed";\
  [params](#promptlistchangednotification-params)?: NotificationParams;\
}An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This may be issued by servers without any previous subscription from the client.  jsonrpc: "2.0"[Permalink](#promptlistchangednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/prompts/list\_changed"[Permalink](#promptlistchangednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params?: NotificationParams[Permalink](#promptlistchangednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `notifications/resources/list_changed`

### `ResourceListChangedNotification`

interface ResourceListChangedNotification \{\
  [jsonrpc](#resourcelistchangednotification-jsonrpc): "2.0";\
  [method](#resourcelistchangednotification-method): "notifications/resources/list\_changed";\
  [params](#resourcelistchangednotification-params)?: NotificationParams;\
}An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This may be issued by servers without any previous subscription from the client.  jsonrpc: "2.0"[Permalink](#resourcelistchangednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/resources/list\_changed"[Permalink](#resourcelistchangednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params?: NotificationParams[Permalink](#resourcelistchangednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `notifications/resources/updated`

### `ResourceUpdatedNotification`

interface ResourceUpdatedNotification \{\
  [jsonrpc](#resourceupdatednotification-jsonrpc): "2.0";\
  [method](#resourceupdatednotification-method): "notifications/resources/updated";\
  [params](#resourceupdatednotification-params): [ResourceUpdatedNotificationParams](#resourceupdatednotificationparams);\
}A notification from the server to the client, informing it that a resource has changed and may need to be read again. This should only be sent if the client previously sent a resources/subscribe request.  jsonrpc: "2.0"[Permalink](#resourceupdatednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/resources/updated"[Permalink](#resourceupdatednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: ResourceUpdatedNotificationParams[Permalink](#resourceupdatednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

### `ResourceUpdatedNotificationParams`

interface ResourceUpdatedNotificationParams \{\
  [\_meta](#resourceupdatednotificationparams-_meta)?: \{ \[key: string]: unknown };\
  [uri](#resourceupdatednotificationparams-uri): string;\
}Parameters for a `notifications/resources/updated` notification.  \_meta?: \{ \[key: string]: unknown }[Permalink](#resourceupdatednotificationparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from NotificationParams.\_meta uri: string[Permalink](#resourceupdatednotificationparams-uri) The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.&#x20;

## `notifications/roots/list_changed`

### `RootsListChangedNotification`

interface RootsListChangedNotification \{\
  [jsonrpc](#rootslistchangednotification-jsonrpc): "2.0";\
  [method](#rootslistchangednotification-method): "notifications/roots/list\_changed";\
  [params](#rootslistchangednotification-params)?: NotificationParams;\
}A notification from the client to the server, informing it that the list of roots has changed.
This notification should be sent whenever the client adds, removes, or modifies any root.
The server should then request an updated list of roots using the ListRootsRequest.  jsonrpc: "2.0"[Permalink](#rootslistchangednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/roots/list\_changed"[Permalink](#rootslistchangednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params?: NotificationParams[Permalink](#rootslistchangednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `notifications/tools/list_changed`

### `ToolListChangedNotification`

interface ToolListChangedNotification \{\
  [jsonrpc](#toollistchangednotification-jsonrpc): "2.0";\
  [method](#toollistchangednotification-method): "notifications/tools/list\_changed";\
  [params](#toollistchangednotification-params)?: NotificationParams;\
}An optional notification from the server to the client, informing it that the list of tools it offers has changed. This may be issued by servers without any previous subscription from the client.  jsonrpc: "2.0"[Permalink](#toollistchangednotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/tools/list\_changed"[Permalink](#toollistchangednotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params?: NotificationParams[Permalink](#toollistchangednotification-params)  Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `notifications/elicitation/complete`

### `ElicitationCompleteNotification`

interface ElicitationCompleteNotification \{\
  [jsonrpc](#elicitationcompletenotification-jsonrpc): "2.0";\
  [method](#elicitationcompletenotification-method): "notifications/elicitation/complete";\
  [params](#elicitationcompletenotification-params): \{ elicitationId: string };\
}An optional notification from the server to the client, informing it of a completion of a out-of-band elicitation request.  jsonrpc: "2.0"[Permalink](#elicitationcompletenotification-jsonrpc)  Inherited from [JSONRPCNotification](#jsonrpcnotification).[jsonrpc](#jsonrpcnotification-jsonrpc) method: "notifications/elicitation/complete"[Permalink](#elicitationcompletenotification-method)  Overrides [JSONRPCNotification](#jsonrpcnotification).[method](#jsonrpcnotification-method) params: \{ elicitationId: string }[Permalink](#elicitationcompletenotification-params)  Type Declaration <ul> <li> elicitationId: string The ID of the elicitation that completed. </li></ul> Overrides [JSONRPCNotification](#jsonrpcnotification).[params](#jsonrpcnotification-params)

## `ping`

### `PingRequest`

interface PingRequest \{\
  [jsonrpc](#pingrequest-jsonrpc): "2.0";\
  [id](#pingrequest-id): [RequestId](#requestid);\
  [method](#pingrequest-method): "ping";\
  [params](#pingrequest-params)?: RequestParams;\
}A ping, issued by either the server or the client, to check that the other party is still alive. The receiver must promptly respond, or else may be disconnected.  jsonrpc: "2.0"[Permalink](#pingrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#pingrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "ping"[Permalink](#pingrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params?: RequestParams[Permalink](#pingrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

## `tasks`

### `CreateTaskResult`

interface CreateTaskResult \{\
  [\_meta](#createtaskresult-_meta)?: \{ \[key: string]: unknown };\
  [task](#createtaskresult-task): [Task](#task);\
  \[key: string]: unknown;\
}A response to a task-augmented request.  \_meta?: \{ \[key: string]: unknown }[Permalink](#createtaskresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) task: Task[Permalink](#createtaskresult-task)&#x20;

### `RelatedTaskMetadata`

interface RelatedTaskMetadata \{\
  [taskId](#relatedtaskmetadata-taskid): string;\
}Metadata for associating messages with a task.
Include this in the `_meta` field under the key `io.modelcontextprotocol/related-task`.  taskId: string[Permalink](#relatedtaskmetadata-taskid) The task identifier this message is associated with.&#x20;

### `Task`

interface Task \{\
  [taskId](#task-taskid): string;\
  [status](#task-status): [TaskStatus](#taskstatus);\
  [statusMessage](#task-statusmessage)?: string;\
  [createdAt](#task-createdat): string;\
  [lastUpdatedAt](#task-lastupdatedat): string;\
  [ttl](#task-ttl): number | null;\
  [pollInterval](#task-pollinterval)?: number;\
}Data associated with a task.  taskId: string[Permalink](#task-taskid) The task identifier.  status: TaskStatus[Permalink](#task-status) Current task state.  statusMessage?: string[Permalink](#task-statusmessage) Optional human-readable message describing the current task state.
This can provide context for any status, including: <ul> <li>Reasons for "cancelled" status</li> <li>Summaries for "completed" status</li> <li>Diagnostic information for "failed" status (e.g., error details, what went wrong)</li> </ul>  createdAt: string[Permalink](#task-createdat) ISO 8601 timestamp when the task was created.  lastUpdatedAt: string[Permalink](#task-lastupdatedat) ISO 8601 timestamp when the task was last updated.  ttl: number | null[Permalink](#task-ttl) Actual retention duration from creation in milliseconds, null for unlimited.  pollInterval?: number[Permalink](#task-pollinterval) Suggested polling interval in milliseconds.&#x20;

### `TaskMetadata`

interface TaskMetadata \{\
  [ttl](#taskmetadata-ttl)?: number;\
}Metadata for augmenting a request with task execution.
Include this in the `task` field of the request parameters.  ttl?: number[Permalink](#taskmetadata-ttl) Requested duration in milliseconds to retain task from creation.&#x20;

### `TaskStatus`

TaskStatus: "working" | "input\_required" | "completed" | "failed" | "cancelled"The status of a task.&#x20;

## `tasks/get`

### `GetTaskRequest`

interface GetTaskRequest \{\
  [jsonrpc](#gettaskrequest-jsonrpc): "2.0";\
  [id](#gettaskrequest-id): [RequestId](#requestid);\
  [method](#gettaskrequest-method): "tasks/get";\
  [params](#gettaskrequest-params): \{ taskId: string };\
}A request to retrieve the state of a task.  jsonrpc: "2.0"[Permalink](#gettaskrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#gettaskrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "tasks/get"[Permalink](#gettaskrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: \{ taskId: string }[Permalink](#gettaskrequest-params)  Type Declaration <ul> <li> taskId: string The task identifier to query. </li></ul> Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `GetTaskResult`

GetTaskResult: [Result](#result) & [Task](#task)The response to a tasks/get request.&#x20;

## `tasks/result`

### `GetTaskPayloadRequest`

interface GetTaskPayloadRequest \{\
  [jsonrpc](#gettaskpayloadrequest-jsonrpc): "2.0";\
  [id](#gettaskpayloadrequest-id): [RequestId](#requestid);\
  [method](#gettaskpayloadrequest-method): "tasks/result";\
  [params](#gettaskpayloadrequest-params): \{ taskId: string };\
}A request to retrieve the result of a completed task.  jsonrpc: "2.0"[Permalink](#gettaskpayloadrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#gettaskpayloadrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "tasks/result"[Permalink](#gettaskpayloadrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: \{ taskId: string }[Permalink](#gettaskpayloadrequest-params)  Type Declaration <ul> <li> taskId: string The task identifier to retrieve results for. </li></ul> Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `GetTaskPayloadResult`

interface GetTaskPayloadResult \{\
  [\_meta](#gettaskpayloadresult-_meta)?: \{ \[key: string]: unknown };\
  \[key: string]: unknown;\
}The response to a tasks/result request.
The structure matches the result type of the original request.
For example, a tools/call task would return the CallToolResult structure.  \_meta?: \{ \[key: string]: unknown }[Permalink](#gettaskpayloadresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta)

## `tasks/list`

### `ListTasksRequest`

interface ListTasksRequest \{\
  [jsonrpc](#listtasksrequest-jsonrpc): "2.0";\
  [id](#listtasksrequest-id): [RequestId](#requestid);\
  [params](#listtasksrequest-params)?: PaginatedRequestParams;\
  [method](#listtasksrequest-method): "tasks/list";\
}A request to retrieve a list of tasks.  jsonrpc: "2.0"[Permalink](#listtasksrequest-jsonrpc)  Inherited from PaginatedRequest.jsonrpc id: RequestId[Permalink](#listtasksrequest-id)  Inherited from PaginatedRequest.id params?: PaginatedRequestParams[Permalink](#listtasksrequest-params)  Inherited from PaginatedRequest.params method: "tasks/list"[Permalink](#listtasksrequest-method)  Overrides PaginatedRequest.method

### `ListTasksResult`

interface ListTasksResult \{\
  [\_meta](#listtasksresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listtasksresult-nextcursor)?: string;\
  [tasks](#listtasksresult-tasks): [Task](#task)\[];\
  \[key: string]: unknown;\
}The response to a tasks/list request.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listtasksresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listtasksresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor tasks: Task\[][Permalink](#listtasksresult-tasks)&#x20;

## `tasks/cancel`

### `CancelTaskRequest`

interface CancelTaskRequest \{\
  [jsonrpc](#canceltaskrequest-jsonrpc): "2.0";\
  [id](#canceltaskrequest-id): [RequestId](#requestid);\
  [method](#canceltaskrequest-method): "tasks/cancel";\
  [params](#canceltaskrequest-params): \{ taskId: string };\
}A request to cancel a task.  jsonrpc: "2.0"[Permalink](#canceltaskrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#canceltaskrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "tasks/cancel"[Permalink](#canceltaskrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: \{ taskId: string }[Permalink](#canceltaskrequest-params)  Type Declaration <ul> <li> taskId: string The task identifier to cancel. </li></ul> Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `CancelTaskResult`

CancelTaskResult: [Result](#result) & [Task](#task)The response to a tasks/cancel request.&#x20;

## `prompts/get`

### `GetPromptRequest`

interface GetPromptRequest \{\
  [jsonrpc](#getpromptrequest-jsonrpc): "2.0";\
  [id](#getpromptrequest-id): [RequestId](#requestid);\
  [method](#getpromptrequest-method): "prompts/get";\
  [params](#getpromptrequest-params): [GetPromptRequestParams](#getpromptrequestparams);\
}Used by the client to get a prompt provided by the server.  jsonrpc: "2.0"[Permalink](#getpromptrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#getpromptrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "prompts/get"[Permalink](#getpromptrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: GetPromptRequestParams[Permalink](#getpromptrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `GetPromptRequestParams`

interface GetPromptRequestParams \{\
  [\_meta](#getpromptrequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [name](#getpromptrequestparams-name): string;\
  [arguments](#getpromptrequestparams-arguments)?: \{ \[key: string]: string };\
}Parameters for a `prompts/get` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#getpromptrequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from RequestParams.\_meta name: string[Permalink](#getpromptrequestparams-name) The name of the prompt or prompt template.  arguments?: \{ \[key: string]: string }[Permalink](#getpromptrequestparams-arguments) Arguments to use for templating the prompt.&#x20;

### `GetPromptResult`

interface GetPromptResult \{\
  [\_meta](#getpromptresult-_meta)?: \{ \[key: string]: unknown };\
  [description](#getpromptresult-description)?: string;\
  [messages](#getpromptresult-messages): [PromptMessage](#promptmessage)\[];\
  \[key: string]: unknown;\
}The server's response to a prompts/get request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#getpromptresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) description?: string[Permalink](#getpromptresult-description) An optional description for the prompt.  messages: PromptMessage\[][Permalink](#getpromptresult-messages)&#x20;

### `PromptMessage`

interface PromptMessage \{\
  [role](#promptmessage-role): [Role](#role);\
  [content](#promptmessage-content): [ContentBlock](#contentblock);\
}Describes a message returned as part of a prompt. This is similar to `SamplingMessage`, but also supports the embedding of
resources from the MCP server.  role: Role[Permalink](#promptmessage-role)  content: ContentBlock[Permalink](#promptmessage-content)&#x20;

## `prompts/list`

### `ListPromptsRequest`

interface ListPromptsRequest \{\
  [jsonrpc](#listpromptsrequest-jsonrpc): "2.0";\
  [id](#listpromptsrequest-id): [RequestId](#requestid);\
  [params](#listpromptsrequest-params)?: PaginatedRequestParams;\
  [method](#listpromptsrequest-method): "prompts/list";\
}Sent from the client to request a list of prompts and prompt templates the server has.  jsonrpc: "2.0"[Permalink](#listpromptsrequest-jsonrpc)  Inherited from PaginatedRequest.jsonrpc id: RequestId[Permalink](#listpromptsrequest-id)  Inherited from PaginatedRequest.id params?: PaginatedRequestParams[Permalink](#listpromptsrequest-params)  Inherited from PaginatedRequest.params method: "prompts/list"[Permalink](#listpromptsrequest-method)  Overrides PaginatedRequest.method

### `ListPromptsResult`

interface ListPromptsResult \{\
  [\_meta](#listpromptsresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listpromptsresult-nextcursor)?: string;\
  [prompts](#listpromptsresult-prompts): [Prompt](#prompt)\[];\
  \[key: string]: unknown;\
}The server's response to a prompts/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listpromptsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listpromptsresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor prompts: Prompt\[][Permalink](#listpromptsresult-prompts)&#x20;

### `Prompt`

interface Prompt \{\
  [icons](#prompt-icons)?: [Icon](#icon)\[];\
  [name](#prompt-name): string;\
  [title](#prompt-title)?: string;\
  [description](#prompt-description)?: string;\
  [arguments](#prompt-arguments)?: [PromptArgument](#promptargument)\[];\
  [\_meta](#prompt-_meta)?: \{ \[key: string]: unknown };\
}A prompt or prompt template that the server offers.  icons?: Icon\[][Permalink](#prompt-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from Icons.icons name: string[Permalink](#prompt-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#prompt-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title description?: string[Permalink](#prompt-description) An optional description of what this prompt provides  arguments?: PromptArgument\[][Permalink](#prompt-arguments) A list of arguments to use for templating the prompt.  \_meta?: \{ \[key: string]: unknown }[Permalink](#prompt-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `PromptArgument`

interface PromptArgument \{\
  [name](#promptargument-name): string;\
  [title](#promptargument-title)?: string;\
  [description](#promptargument-description)?: string;\
  [required](#promptargument-required)?: boolean;\
}Describes an argument that a prompt can accept.  name: string[Permalink](#promptargument-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#promptargument-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title description?: string[Permalink](#promptargument-description) A human-readable description of the argument.  required?: boolean[Permalink](#promptargument-required) Whether this argument must be provided.&#x20;

## `resources/list`

### `ListResourcesRequest`

interface ListResourcesRequest \{\
  [jsonrpc](#listresourcesrequest-jsonrpc): "2.0";\
  [id](#listresourcesrequest-id): [RequestId](#requestid);\
  [params](#listresourcesrequest-params)?: PaginatedRequestParams;\
  [method](#listresourcesrequest-method): "resources/list";\
}Sent from the client to request a list of resources the server has.  jsonrpc: "2.0"[Permalink](#listresourcesrequest-jsonrpc)  Inherited from PaginatedRequest.jsonrpc id: RequestId[Permalink](#listresourcesrequest-id)  Inherited from PaginatedRequest.id params?: PaginatedRequestParams[Permalink](#listresourcesrequest-params)  Inherited from PaginatedRequest.params method: "resources/list"[Permalink](#listresourcesrequest-method)  Overrides PaginatedRequest.method

### `ListResourcesResult`

interface ListResourcesResult \{\
  [\_meta](#listresourcesresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listresourcesresult-nextcursor)?: string;\
  [resources](#listresourcesresult-resources): [Resource](#resource)\[];\
  \[key: string]: unknown;\
}The server's response to a resources/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listresourcesresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listresourcesresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor resources: Resource\[][Permalink](#listresourcesresult-resources)&#x20;

### `Resource`

interface Resource \{\
  [icons](#resource-icons)?: [Icon](#icon)\[];\
  [name](#resource-name): string;\
  [title](#resource-title)?: string;\
  [uri](#resource-uri): string;\
  [description](#resource-description)?: string;\
  [mimeType](#resource-mimetype)?: string;\
  [annotations](#resource-annotations)?: [Annotations](#annotations);\
  [size](#resource-size)?: number;\
  [\_meta](#resource-_meta)?: \{ \[key: string]: unknown };\
}A known resource that the server is capable of reading.  icons?: Icon\[][Permalink](#resource-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from Icons.icons name: string[Permalink](#resource-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#resource-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title uri: string[Permalink](#resource-uri) The URI of this resource.  description?: string[Permalink](#resource-description) A description of what this resource represents. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  mimeType?: string[Permalink](#resource-mimetype) The MIME type of this resource, if known.  annotations?: Annotations[Permalink](#resource-annotations) Optional annotations for the client.  size?: number[Permalink](#resource-size) The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known. This can be used by Hosts to display file sizes and estimate context window usage.  \_meta?: \{ \[key: string]: unknown }[Permalink](#resource-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

## `resources/read`

### `ReadResourceRequest`

interface ReadResourceRequest \{\
  [jsonrpc](#readresourcerequest-jsonrpc): "2.0";\
  [id](#readresourcerequest-id): [RequestId](#requestid);\
  [method](#readresourcerequest-method): "resources/read";\
  [params](#readresourcerequest-params): [ReadResourceRequestParams](#readresourcerequestparams);\
}Sent from the client to the server, to read a specific resource URI.  jsonrpc: "2.0"[Permalink](#readresourcerequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#readresourcerequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "resources/read"[Permalink](#readresourcerequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: ReadResourceRequestParams[Permalink](#readresourcerequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `ReadResourceRequestParams`

interface ReadResourceRequestParams \{\
  [\_meta](#readresourcerequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [uri](#readresourcerequestparams-uri): string;\
}Parameters for a `resources/read` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#readresourcerequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from ResourceRequestParams.\_meta uri: string[Permalink](#readresourcerequestparams-uri) The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.  Inherited from ResourceRequestParams.uri

### `ReadResourceResult`

interface ReadResourceResult \{\
  [\_meta](#readresourceresult-_meta)?: \{ \[key: string]: unknown };\
  [contents](#readresourceresult-contents): ([TextResourceContents](#textresourcecontents) | [BlobResourceContents](#blobresourcecontents))\[];\
  \[key: string]: unknown;\
}The server's response to a resources/read request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#readresourceresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) contents: (TextResourceContents | BlobResourceContents)\[][Permalink](#readresourceresult-contents)&#x20;

## `resources/subscribe`

### `SubscribeRequest`

interface SubscribeRequest \{\
  [jsonrpc](#subscriberequest-jsonrpc): "2.0";\
  [id](#subscriberequest-id): [RequestId](#requestid);\
  [method](#subscriberequest-method): "resources/subscribe";\
  [params](#subscriberequest-params): [SubscribeRequestParams](#subscriberequestparams);\
}Sent from the client to request resources/updated notifications from the server whenever a particular resource changes.  jsonrpc: "2.0"[Permalink](#subscriberequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#subscriberequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "resources/subscribe"[Permalink](#subscriberequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: SubscribeRequestParams[Permalink](#subscriberequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `SubscribeRequestParams`

interface SubscribeRequestParams \{\
  [\_meta](#subscriberequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [uri](#subscriberequestparams-uri): string;\
}Parameters for a `resources/subscribe` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#subscriberequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from ResourceRequestParams.\_meta uri: string[Permalink](#subscriberequestparams-uri) The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.  Inherited from ResourceRequestParams.uri

## `resources/templates/list`

### `ListResourceTemplatesRequest`

interface ListResourceTemplatesRequest \{\
  [jsonrpc](#listresourcetemplatesrequest-jsonrpc): "2.0";\
  [id](#listresourcetemplatesrequest-id): [RequestId](#requestid);\
  [params](#listresourcetemplatesrequest-params)?: PaginatedRequestParams;\
  [method](#listresourcetemplatesrequest-method): "resources/templates/list";\
}Sent from the client to request a list of resource templates the server has.  jsonrpc: "2.0"[Permalink](#listresourcetemplatesrequest-jsonrpc)  Inherited from PaginatedRequest.jsonrpc id: RequestId[Permalink](#listresourcetemplatesrequest-id)  Inherited from PaginatedRequest.id params?: PaginatedRequestParams[Permalink](#listresourcetemplatesrequest-params)  Inherited from PaginatedRequest.params method: "resources/templates/list"[Permalink](#listresourcetemplatesrequest-method)  Overrides PaginatedRequest.method

### `ListResourceTemplatesResult`

interface ListResourceTemplatesResult \{\
  [\_meta](#listresourcetemplatesresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listresourcetemplatesresult-nextcursor)?: string;\
  [resourceTemplates](#listresourcetemplatesresult-resourcetemplates): [ResourceTemplate](#resourcetemplate)\[];\
  \[key: string]: unknown;\
}The server's response to a resources/templates/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listresourcetemplatesresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listresourcetemplatesresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor resourceTemplates: ResourceTemplate\[][Permalink](#listresourcetemplatesresult-resourcetemplates)&#x20;

### `ResourceTemplate`

interface ResourceTemplate \{\
  [icons](#resourcetemplate-icons)?: [Icon](#icon)\[];\
  [name](#resourcetemplate-name): string;\
  [title](#resourcetemplate-title)?: string;\
  [uriTemplate](#resourcetemplate-uritemplate): string;\
  [description](#resourcetemplate-description)?: string;\
  [mimeType](#resourcetemplate-mimetype)?: string;\
  [annotations](#resourcetemplate-annotations)?: [Annotations](#annotations);\
  [\_meta](#resourcetemplate-_meta)?: \{ \[key: string]: unknown };\
}A template description for resources available on the server.  icons?: Icon\[][Permalink](#resourcetemplate-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from Icons.icons name: string[Permalink](#resourcetemplate-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#resourcetemplate-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title uriTemplate: string[Permalink](#resourcetemplate-uritemplate) A URI template (according to RFC 6570) that can be used to construct resource URIs.  description?: string[Permalink](#resourcetemplate-description) A description of what this template is for. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  mimeType?: string[Permalink](#resourcetemplate-mimetype) The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.  annotations?: Annotations[Permalink](#resourcetemplate-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#resourcetemplate-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

## `resources/unsubscribe`

### `UnsubscribeRequest`

interface UnsubscribeRequest \{\
  [jsonrpc](#unsubscriberequest-jsonrpc): "2.0";\
  [id](#unsubscriberequest-id): [RequestId](#requestid);\
  [method](#unsubscriberequest-method): "resources/unsubscribe";\
  [params](#unsubscriberequest-params): [UnsubscribeRequestParams](#unsubscriberequestparams);\
}Sent from the client to request cancellation of resources/updated notifications from the server. This should follow a previous resources/subscribe request.  jsonrpc: "2.0"[Permalink](#unsubscriberequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#unsubscriberequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "resources/unsubscribe"[Permalink](#unsubscriberequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: UnsubscribeRequestParams[Permalink](#unsubscriberequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `UnsubscribeRequestParams`

interface UnsubscribeRequestParams \{\
  [\_meta](#unsubscriberequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [uri](#unsubscriberequestparams-uri): string;\
}Parameters for a `resources/unsubscribe` request.  \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#unsubscriberequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from ResourceRequestParams.\_meta uri: string[Permalink](#unsubscriberequestparams-uri) The URI of the resource. The URI can use any protocol; it is up to the server how to interpret it.  Inherited from ResourceRequestParams.uri

## `roots/list`

### `ListRootsRequest`

interface ListRootsRequest \{\
  [jsonrpc](#listrootsrequest-jsonrpc): "2.0";\
  [id](#listrootsrequest-id): [RequestId](#requestid);\
  [method](#listrootsrequest-method): "roots/list";\
  [params](#listrootsrequest-params)?: RequestParams;\
}Sent from the server to request a list of root URIs from the client. Roots allow
servers to ask for specific directories or files to operate on. A common example
for roots is providing a set of repositories or directories a server should operate
on. This request is typically used when the server needs to understand the file system
structure or access specific locations that the client has permission to read from.  jsonrpc: "2.0"[Permalink](#listrootsrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#listrootsrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "roots/list"[Permalink](#listrootsrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params?: RequestParams[Permalink](#listrootsrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `ListRootsResult`

interface ListRootsResult \{\
  [\_meta](#listrootsresult-_meta)?: \{ \[key: string]: unknown };\
  [roots](#listrootsresult-roots): [Root](#root)\[];\
  \[key: string]: unknown;\
}The client's response to a roots/list request from the server.
This result contains an array of Root objects, each representing a root directory
or file that the server can operate on.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listrootsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) roots: Root\[][Permalink](#listrootsresult-roots)&#x20;

### `Root`

interface Root \{\
  [uri](#root-uri): string;\
  [name](#root-name)?: string;\
  [\_meta](#root-_meta)?: \{ \[key: string]: unknown };\
}Represents a root directory or file that the server can operate on.  uri: string[Permalink](#root-uri) The URI identifying the root. This *must* start with file:// for now.
This restriction may be relaxed in future versions of the protocol to allow
other URI schemes.  name?: string[Permalink](#root-name) An optional name for the root. This can be used to provide a human-readable
identifier for the root, which may be useful for display purposes or for
referencing the root in other parts of the application.  \_meta?: \{ \[key: string]: unknown }[Permalink](#root-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

## `sampling/createMessage`

### `CreateMessageRequest`

interface CreateMessageRequest \{\
  [jsonrpc](#createmessagerequest-jsonrpc): "2.0";\
  [id](#createmessagerequest-id): [RequestId](#requestid);\
  [method](#createmessagerequest-method): "sampling/createMessage";\
  [params](#createmessagerequest-params): [CreateMessageRequestParams](#createmessagerequestparams);\
}A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.  jsonrpc: "2.0"[Permalink](#createmessagerequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#createmessagerequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "sampling/createMessage"[Permalink](#createmessagerequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: CreateMessageRequestParams[Permalink](#createmessagerequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `CreateMessageRequestParams`

interface CreateMessageRequestParams \{\
  [task](#createmessagerequestparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#createmessagerequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [messages](#createmessagerequestparams-messages): [SamplingMessage](#samplingmessage)\[];\
  [modelPreferences](#createmessagerequestparams-modelpreferences)?: [ModelPreferences](#modelpreferences);\
  [systemPrompt](#createmessagerequestparams-systemprompt)?: string;\
  [includeContext](#createmessagerequestparams-includecontext)?: "none" | "thisServer" | "allServers";\
  [temperature](#createmessagerequestparams-temperature)?: number;\
  [maxTokens](#createmessagerequestparams-maxtokens): number;\
  [stopSequences](#createmessagerequestparams-stopsequences)?: string\[];\
  [metadata](#createmessagerequestparams-metadata)?: object;\
  [tools](#createmessagerequestparams-tools)?: [Tool](#tool)\[];\
  [toolChoice](#createmessagerequestparams-toolchoice)?: [ToolChoice](#toolchoice);\
}Parameters for a `sampling/createMessage` request.  task?: TaskMetadata[Permalink](#createmessagerequestparams-task) If specified, the caller is requesting task-augmented execution for this request.
The request will return a CreateTaskResult immediately, and the actual result can be
retrieved later via tasks/result. Task augmentation is subject to capability negotiation - receivers MUST declare support
for task augmentation of specific request types in their capabilities.  Inherited from TaskAugmentedRequestParams.task \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#createmessagerequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from TaskAugmentedRequestParams.\_meta messages: SamplingMessage\[][Permalink](#createmessagerequestparams-messages)  modelPreferences?: ModelPreferences[Permalink](#createmessagerequestparams-modelpreferences) The server's preferences for which model to select. The client MAY ignore these preferences.  systemPrompt?: string[Permalink](#createmessagerequestparams-systemprompt) An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt.  includeContext?: "none" | "thisServer" | "allServers"[Permalink](#createmessagerequestparams-includecontext) A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.
The client MAY ignore this request. Default is "none". Values "thisServer" and "allServers" are soft-deprecated. Servers SHOULD only use these values if the client
declares ClientCapabilities.sampling.context. These values may be removed in future spec releases.  temperature?: number[Permalink](#createmessagerequestparams-temperature)  maxTokens: number[Permalink](#createmessagerequestparams-maxtokens) The requested maximum number of tokens to sample (to prevent runaway completions). The client MAY choose to sample fewer tokens than the requested maximum.  stopSequences?: string\[][Permalink](#createmessagerequestparams-stopsequences)  metadata?: object[Permalink](#createmessagerequestparams-metadata) Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific.  tools?: Tool\[][Permalink](#createmessagerequestparams-tools) Tools that the model may use during generation.
The client MUST return an error if this field is provided but ClientCapabilities.sampling.tools is not declared.  toolChoice?: ToolChoice[Permalink](#createmessagerequestparams-toolchoice) Controls how the model uses tools.
The client MUST return an error if this field is provided but ClientCapabilities.sampling.tools is not declared.
Default is `{ mode: "auto" }`.&#x20;

### `CreateMessageResult`

interface CreateMessageResult \{\
  [\_meta](#createmessageresult-_meta)?: \{ \[key: string]: unknown };\
  [model](#createmessageresult-model): string;\
  [stopReason](#createmessageresult-stopreason)?: string;\
  [role](#createmessageresult-role): [Role](#role);\
  [content](#createmessageresult-content): [SamplingMessageContentBlock](#samplingmessagecontentblock) | [SamplingMessageContentBlock](#samplingmessagecontentblock)\[];\
  \[key: string]: unknown;\
}The client's response to a sampling/createMessage request from the server.
The client should inform the user before returning the sampled message, to allow them
to inspect the response (human in the loop) and decide whether to allow the server to see it.  \_meta?: \{ \[key: string]: unknown }[Permalink](#createmessageresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) model: string[Permalink](#createmessageresult-model) The name of the model that generated the message.  stopReason?: string[Permalink](#createmessageresult-stopreason) The reason why sampling stopped, if known. Standard values: <ul> <li>"endTurn": Natural end of the assistant's turn</li> <li>"stopSequence": A stop sequence was encountered</li> <li>"maxTokens": Maximum token limit was reached</li> <li>"toolUse": The model wants to use one or more tools</li> </ul> This field is an open string to allow for provider-specific stop reasons.  role: Role[Permalink](#createmessageresult-role)  Inherited from [SamplingMessage](#samplingmessage).[role](#samplingmessage-role) content: SamplingMessageContentBlock | SamplingMessageContentBlock\[][Permalink](#createmessageresult-content)  Inherited from [SamplingMessage](#samplingmessage).[content](#samplingmessage-content)

### `ModelHint`

interface ModelHint \{\
  [name](#modelhint-name)?: string;\
}Hints to use for model selection. Keys not declared here are currently left unspecified by the spec and are up
to the client to interpret.  name?: string[Permalink](#modelhint-name) A hint for a model name. The client SHOULD treat this as a substring of a model name; for example: <ul> <li>`claude-3-5-sonnet` should match `claude-3-5-sonnet-20241022`</li> <li>`sonnet` should match `claude-3-5-sonnet-20241022`, `claude-3-sonnet-20240229`, etc.</li> <li>`claude` should match any Claude model</li> </ul> The client MAY also map the string to a different provider's model name or a different model family, as long as it fills a similar niche; for example: <ul> <li>`gemini-1.5-flash` could match `claude-3-haiku-20240307`</li> </ul>&#x20;

### `ModelPreferences`

interface ModelPreferences \{\
  [hints](#modelpreferences-hints)?: [ModelHint](#modelhint)\[];\
  [costPriority](#modelpreferences-costpriority)?: number;\
  [speedPriority](#modelpreferences-speedpriority)?: number;\
  [intelligencePriority](#modelpreferences-intelligencepriority)?: number;\
}The server's preferences for model selection, requested of the client during sampling. Because LLMs can vary along multiple dimensions, choosing the "best" model is
rarely straightforward.  Different models excel in different areas—some are
faster but less capable, others are more capable but more expensive, and so
on. This interface allows servers to express their priorities across multiple
dimensions to help clients make an appropriate selection for their use case. These preferences are always advisory. The client MAY ignore them. It is also
up to the client to decide how to interpret these preferences and how to
balance them against other considerations.  hints?: ModelHint\[][Permalink](#modelpreferences-hints) Optional hints to use for model selection. If multiple hints are specified, the client MUST evaluate them in order
(such that the first match is taken). The client SHOULD prioritize these hints over the numeric priorities, but
MAY still use the priorities to select from ambiguous matches.  costPriority?: number[Permalink](#modelpreferences-costpriority) How much to prioritize cost when selecting a model. A value of 0 means cost
is not important, while a value of 1 means cost is the most important
factor.  speedPriority?: number[Permalink](#modelpreferences-speedpriority) How much to prioritize sampling speed (latency) when selecting a model. A
value of 0 means speed is not important, while a value of 1 means speed is
the most important factor.  intelligencePriority?: number[Permalink](#modelpreferences-intelligencepriority) How much to prioritize intelligence and capabilities when selecting a
model. A value of 0 means intelligence is not important, while a value of 1
means intelligence is the most important factor.&#x20;

### `SamplingMessage`

interface SamplingMessage \{\
  [role](#samplingmessage-role): [Role](#role);\
  [content](#samplingmessage-content): [SamplingMessageContentBlock](#samplingmessagecontentblock) | [SamplingMessageContentBlock](#samplingmessagecontentblock)\[];\
  [\_meta](#samplingmessage-_meta)?: \{ \[key: string]: unknown };\
}Describes a message issued to or received from an LLM API.  role: Role[Permalink](#samplingmessage-role)  content: SamplingMessageContentBlock | SamplingMessageContentBlock\[][Permalink](#samplingmessage-content)  \_meta?: \{ \[key: string]: unknown }[Permalink](#samplingmessage-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `SamplingMessageContentBlock`

SamplingMessageContentBlock:\
  | [TextContent](#textcontent)\
  | [ImageContent](#imagecontent)\
  | [AudioContent](#audiocontent)\
  | [ToolUseContent](#toolusecontent)\
  | [ToolResultContent](#toolresultcontent)

### `ToolChoice`

interface ToolChoice \{\
  [mode](#toolchoice-mode)?: "none" | "required" | "auto";\
}Controls tool selection behavior for sampling requests.  mode?: "none" | "required" | "auto"[Permalink](#toolchoice-mode) Controls the tool use ability of the model: <ul> <li>"auto": Model decides whether to use tools (default)</li> <li>"required": Model MUST use at least one tool before completing</li> <li>"none": Model MUST NOT use any tools</li> </ul>&#x20;

### `ToolResultContent`

interface ToolResultContent \{\
  [type](#toolresultcontent-type): "tool\_result";\
  [toolUseId](#toolresultcontent-tooluseid): string;\
  [content](#toolresultcontent-content): [ContentBlock](#contentblock)\[];\
  [structuredContent](#toolresultcontent-structuredcontent)?: \{ \[key: string]: unknown };\
  [isError](#toolresultcontent-iserror)?: boolean;\
  [\_meta](#toolresultcontent-_meta)?: \{ \[key: string]: unknown };\
}The result of a tool use, provided by the user back to the assistant.  type: "tool\_result"[Permalink](#toolresultcontent-type)  toolUseId: string[Permalink](#toolresultcontent-tooluseid) The ID of the tool use this result corresponds to. This MUST match the ID from a previous ToolUseContent.  content: ContentBlock\[][Permalink](#toolresultcontent-content) The unstructured result content of the tool use. This has the same format as CallToolResult.content and can include text, images,
audio, resource links, and embedded resources.  structuredContent?: \{ \[key: string]: unknown }[Permalink](#toolresultcontent-structuredcontent) An optional structured result object. If the tool defined an outputSchema, this SHOULD conform to that schema.  isError?: boolean[Permalink](#toolresultcontent-iserror) Whether the tool use resulted in an error. If true, the content typically describes the error that occurred.
Default: false  \_meta?: \{ \[key: string]: unknown }[Permalink](#toolresultcontent-_meta) Optional metadata about the tool result. Clients SHOULD preserve this field when
including tool results in subsequent sampling requests to enable caching optimizations. See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ToolUseContent`

interface ToolUseContent \{\
  [type](#toolusecontent-type): "tool\_use";\
  [id](#toolusecontent-id): string;\
  [name](#toolusecontent-name): string;\
  [input](#toolusecontent-input): \{ \[key: string]: unknown };\
  [\_meta](#toolusecontent-_meta)?: \{ \[key: string]: unknown };\
}A request from the assistant to call a tool.  type: "tool\_use"[Permalink](#toolusecontent-type)  id: string[Permalink](#toolusecontent-id) A unique identifier for this tool use. This ID is used to match tool results to their corresponding tool uses.  name: string[Permalink](#toolusecontent-name) The name of the tool to call.  input: \{ \[key: string]: unknown }[Permalink](#toolusecontent-input) The arguments to pass to the tool, conforming to the tool's input schema.  \_meta?: \{ \[key: string]: unknown }[Permalink](#toolusecontent-_meta) Optional metadata about the tool use. Clients SHOULD preserve this field when
including tool uses in subsequent sampling requests to enable caching optimizations. See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

## `tools/call`

### `CallToolRequest`

interface CallToolRequest \{\
  [jsonrpc](#calltoolrequest-jsonrpc): "2.0";\
  [id](#calltoolrequest-id): [RequestId](#requestid);\
  [method](#calltoolrequest-method): "tools/call";\
  [params](#calltoolrequest-params): [CallToolRequestParams](#calltoolrequestparams);\
}Used by the client to invoke a tool provided by the server.  jsonrpc: "2.0"[Permalink](#calltoolrequest-jsonrpc)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[jsonrpc](#jsonrpcrequest-jsonrpc) id: RequestId[Permalink](#calltoolrequest-id)  Inherited from [JSONRPCRequest](#jsonrpcrequest).[id](#jsonrpcrequest-id) method: "tools/call"[Permalink](#calltoolrequest-method)  Overrides [JSONRPCRequest](#jsonrpcrequest).[method](#jsonrpcrequest-method) params: CallToolRequestParams[Permalink](#calltoolrequest-params)  Overrides [JSONRPCRequest](#jsonrpcrequest).[params](#jsonrpcrequest-params)

### `CallToolRequestParams`

interface CallToolRequestParams \{\
  [task](#calltoolrequestparams-task)?: [TaskMetadata](#taskmetadata);\
  [\_meta](#calltoolrequestparams-_meta)?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
  [name](#calltoolrequestparams-name): string;\
  [arguments](#calltoolrequestparams-arguments)?: \{ \[key: string]: unknown };\
}Parameters for a `tools/call` request.  task?: TaskMetadata[Permalink](#calltoolrequestparams-task) If specified, the caller is requesting task-augmented execution for this request.
The request will return a CreateTaskResult immediately, and the actual result can be
retrieved later via tasks/result. Task augmentation is subject to capability negotiation - receivers MUST declare support
for task augmentation of specific request types in their capabilities.  Inherited from TaskAugmentedRequestParams.task \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown }[Permalink](#calltoolrequestparams-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.   Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul> Inherited from TaskAugmentedRequestParams.\_meta name: string[Permalink](#calltoolrequestparams-name) The name of the tool.  arguments?: \{ \[key: string]: unknown }[Permalink](#calltoolrequestparams-arguments) Arguments to use for the tool call.&#x20;

### `CallToolResult`

interface CallToolResult \{\
  [\_meta](#calltoolresult-_meta)?: \{ \[key: string]: unknown };\
  [content](#calltoolresult-content): [ContentBlock](#contentblock)\[];\
  [structuredContent](#calltoolresult-structuredcontent)?: \{ \[key: string]: unknown };\
  [isError](#calltoolresult-iserror)?: boolean;\
  \[key: string]: unknown;\
}The server's response to a tool call.  \_meta?: \{ \[key: string]: unknown }[Permalink](#calltoolresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) content: ContentBlock\[][Permalink](#calltoolresult-content) A list of content objects that represent the unstructured result of the tool call.  structuredContent?: \{ \[key: string]: unknown }[Permalink](#calltoolresult-structuredcontent) An optional JSON object that represents the structured result of the tool call.  isError?: boolean[Permalink](#calltoolresult-iserror) Whether the tool call ended in an error. If not set, this is assumed to be false (the call was successful). Any errors that originate from the tool SHOULD be reported inside the result
object, with `isError` set to true, *not* as an MCP protocol-level error
response. Otherwise, the LLM would not be able to see that an error occurred
and self-correct. However, any errors in *finding* the tool, an error indicating that the
server does not support tool calls, or any other exceptional conditions,
should be reported as an MCP error response.&#x20;

## `tools/list`

### `ListToolsRequest`

interface ListToolsRequest \{\
  [jsonrpc](#listtoolsrequest-jsonrpc): "2.0";\
  [id](#listtoolsrequest-id): [RequestId](#requestid);\
  [params](#listtoolsrequest-params)?: PaginatedRequestParams;\
  [method](#listtoolsrequest-method): "tools/list";\
}Sent from the client to request a list of tools the server has.  jsonrpc: "2.0"[Permalink](#listtoolsrequest-jsonrpc)  Inherited from PaginatedRequest.jsonrpc id: RequestId[Permalink](#listtoolsrequest-id)  Inherited from PaginatedRequest.id params?: PaginatedRequestParams[Permalink](#listtoolsrequest-params)  Inherited from PaginatedRequest.params method: "tools/list"[Permalink](#listtoolsrequest-method)  Overrides PaginatedRequest.method

### `ListToolsResult`

interface ListToolsResult \{\
  [\_meta](#listtoolsresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listtoolsresult-nextcursor)?: string;\
  [tools](#listtoolsresult-tools): [Tool](#tool)\[];\
  \[key: string]: unknown;\
}The server's response to a tools/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listtoolsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listtoolsresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor tools: Tool\[][Permalink](#listtoolsresult-tools)&#x20;

### `Tool`

interface Tool \{\
  [icons](#tool-icons)?: [Icon](#icon)\[];\
  [name](#tool-name): string;\
  [title](#tool-title)?: string;\
  [description](#tool-description)?: string;\
  [inputSchema](#tool-inputschema): \{\
    \$schema?: string;\
    type: "object";\
    properties?: \{ \[key: string]: object };\
    required?: string\[];\
  };\
  [execution](#tool-execution)?: [ToolExecution](#toolexecution);\
  [outputSchema](#tool-outputschema)?: \{\
    \$schema?: string;\
    type: "object";\
    properties?: \{ \[key: string]: object };\
    required?: string\[];\
  };\
  [annotations](#tool-annotations)?: [ToolAnnotations](#toolannotations);\
  [\_meta](#tool-_meta)?: \{ \[key: string]: unknown };\
}Definition for a tool the client can call.  icons?: Icon\[][Permalink](#tool-icons) Optional set of sized icons that the client can display in a user interface. Clients that support rendering icons MUST support at least the following MIME types: <ul> <li>`image/png` - PNG images (safe, universal compatibility)</li> <li>`image/jpeg` (and `image/jpg`) - JPEG images (safe, universal compatibility)</li> </ul> Clients that support rendering icons SHOULD also support: <ul> <li>`image/svg+xml` - SVG images (scalable but requires security precautions)</li> <li>`image/webp` - WebP images (modern, efficient format)</li> </ul>  Inherited from Icons.icons name: string[Permalink](#tool-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#tool-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title description?: string[Permalink](#tool-description) A human-readable description of the tool. This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a "hint" to the model.  inputSchema: \{    \$schema?: string;    type: "object";    properties?: \{ \[key: string]: object };    required?: string\[]; }[Permalink](#tool-inputschema) A JSON Schema object defining the expected parameters for the tool.  execution?: ToolExecution[Permalink](#tool-execution) Execution-related properties for this tool.  outputSchema?: \{    \$schema?: string;    type: "object";    properties?: \{ \[key: string]: object };    required?: string\[]; }[Permalink](#tool-outputschema) An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a CallToolResult. Defaults to JSON Schema 2020-12 when no explicit \$schema is provided.
Currently restricted to type: "object" at the root level.  annotations?: ToolAnnotations[Permalink](#tool-annotations) Optional additional tool information. Display name precedence order is: title, annotations.title, then name.  \_meta?: \{ \[key: string]: unknown }[Permalink](#tool-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-11-25/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ToolAnnotations`

interface ToolAnnotations \{\
  [title](#toolannotations-title)?: string;\
  [readOnlyHint](#toolannotations-readonlyhint)?: boolean;\
  [destructiveHint](#toolannotations-destructivehint)?: boolean;\
  [idempotentHint](#toolannotations-idempotenthint)?: boolean;\
  [openWorldHint](#toolannotations-openworldhint)?: boolean;\
}Additional properties describing a Tool to clients. NOTE: all properties in ToolAnnotations are **hints**.
They are not guaranteed to provide a faithful description of
tool behavior (including descriptive properties like `title`). Clients should never make tool use decisions based on ToolAnnotations
received from untrusted servers.  title?: string[Permalink](#toolannotations-title) A human-readable title for the tool.  readOnlyHint?: boolean[Permalink](#toolannotations-readonlyhint) If true, the tool does not modify its environment. Default: false  destructiveHint?: boolean[Permalink](#toolannotations-destructivehint) If true, the tool may perform destructive updates to its environment.
If false, the tool performs only additive updates. (This property is meaningful only when `readOnlyHint == false`) Default: true  idempotentHint?: boolean[Permalink](#toolannotations-idempotenthint) If true, calling the tool repeatedly with the same arguments
will have no additional effect on its environment. (This property is meaningful only when `readOnlyHint == false`) Default: false  openWorldHint?: boolean[Permalink](#toolannotations-openworldhint) If true, this tool may interact with an "open world" of external
entities. If false, the tool's domain of interaction is closed.
For example, the world of a web search tool is open, whereas that
of a memory tool is not. Default: true&#x20;

### `ToolExecution`

interface ToolExecution \{\
  [taskSupport](#toolexecution-tasksupport)?: "forbidden" | "optional" | "required";\
}Execution-related properties for a tool.  taskSupport?: "forbidden" | "optional" | "required"[Permalink](#toolexecution-tasksupport) Indicates whether this tool supports task-augmented execution.
This allows clients to handle long-running operations through polling
the task system. <ul> <li>"forbidden": Tool does not support task-augmented execution (default when absent)</li> <li>"optional": Tool may support task-augmented execution</li> <li>"required": Tool requires task-augmented execution</li> </ul> Default: "forbidden"&#x20;
