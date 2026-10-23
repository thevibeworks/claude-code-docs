> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Schema Reference

## JSON-RPC

### `JSONRPCError`

interface JSONRPCError \{\
  [jsonrpc](#jsonrpcerror-jsonrpc): "2.0";\
  [id](#jsonrpcerror-id): [RequestId](#requestid);\
  [error](#jsonrpcerror-error): \{ code: number; message: string; data?: unknown };\
}A response to a request that indicates an error occurred.  jsonrpc: "2.0"[Permalink](#jsonrpcerror-jsonrpc)  id: RequestId[Permalink](#jsonrpcerror-id)  error: \{ code: number; message: string; data?: unknown }[Permalink](#jsonrpcerror-error)  Type Declaration <ul> <li> code: number The error type that occurred. </li> <li> message: string A short description of the error. The message SHOULD be limited to a concise single sentence. </li> <li> `Optional`data?: unknown Additional information about the error. The value of this member is defined by the sender (e.g. detailed error information, nested errors etc.). </li></ul>

### `JSONRPCMessage`

JSONRPCMessage:\
  | [JSONRPCRequest](#jsonrpcrequest)\
  | [JSONRPCNotification](#jsonrpcnotification)\
  | [JSONRPCResponse](#jsonrpcresponse)\
  | [JSONRPCError](#jsonrpcerror)Refers to any valid JSON-RPC object that can be decoded off the wire, or encoded to be sent.&#x20;

### `JSONRPCNotification`

interface JSONRPCNotification \{\
  [method](#jsonrpcnotification-method): string;\
  [params](#jsonrpcnotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [jsonrpc](#jsonrpcnotification-jsonrpc): "2.0";\
}A notification which does not expect a response.  method: string[Permalink](#jsonrpcnotification-method)  Inherited from Notification.method params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#jsonrpcnotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params jsonrpc: "2.0"[Permalink](#jsonrpcnotification-jsonrpc)&#x20;

### `JSONRPCRequest`

interface JSONRPCRequest \{\
  [method](#jsonrpcrequest-method): string;\
  [params](#jsonrpcrequest-params)?: \{\
    \_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
    \[key: string]: unknown;\
  };\
  [jsonrpc](#jsonrpcrequest-jsonrpc): "2.0";\
  [id](#jsonrpcrequest-id): [RequestId](#requestid);\
}A request that expects a response.  method: string[Permalink](#jsonrpcrequest-method)  Inherited from Request.method params?: \{    \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown };    \[key: string]: unknown; }[Permalink](#jsonrpcrequest-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  <ul> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul></li></ul> Inherited from Request.params jsonrpc: "2.0"[Permalink](#jsonrpcrequest-jsonrpc)  id: RequestId[Permalink](#jsonrpcrequest-id)&#x20;

### `JSONRPCResponse`

interface JSONRPCResponse \{\
  [jsonrpc](#jsonrpcresponse-jsonrpc): "2.0";\
  [id](#jsonrpcresponse-id): [RequestId](#requestid);\
  [result](#jsonrpcresponse-result): [Result](#result);\
}A successful (non-error) response to a request.  jsonrpc: "2.0"[Permalink](#jsonrpcresponse-jsonrpc)  id: RequestId[Permalink](#jsonrpcresponse-id)  result: Result[Permalink](#jsonrpcresponse-result)&#x20;

## Common Types

### `Annotations`

interface Annotations \{\
  [audience](#annotations-audience)?: [Role](#role)\[];\
  [priority](#annotations-priority)?: number;\
  [lastModified](#annotations-lastmodified)?: string;\
}Optional annotations for the client. The client can use annotations to inform how objects are used or displayed  audience?: Role\[][Permalink](#annotations-audience) Describes who the intended customer of this object or data is. It can include multiple entries to indicate content useful for multiple audiences (e.g., `["user", "assistant"]`).  priority?: number[Permalink](#annotations-priority) Describes how important this data is for operating the server. A value of 1 means "most important," and indicates that the data is
effectively required, while 0 means "least important," and indicates that
the data is entirely optional.  lastModified?: string[Permalink](#annotations-lastmodified) The moment the resource was last modified, as an ISO 8601 formatted string. Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z"). Examples: last activity timestamp in an open file, timestamp when the resource
was attached, etc.&#x20;

### `Cursor`

Cursor: stringAn opaque token used to represent a cursor for pagination.&#x20;

### `EmptyResult`

EmptyResult: [Result](#result)A response that indicates success but carries no data.&#x20;

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
} \_meta?: \{ \[key: string]: unknown }[Permalink](#result-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

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
}Audio provided to or from an LLM.  type: "audio"[Permalink](#audiocontent-type)  data: string[Permalink](#audiocontent-data) The base64-encoded audio data.  mimeType: string[Permalink](#audiocontent-mimetype) The MIME type of the audio. Different providers may support different audio types.  annotations?: Annotations[Permalink](#audiocontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#audiocontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

### `BlobResourceContents`

interface BlobResourceContents \{\
  [uri](#blobresourcecontents-uri): string;\
  [mimeType](#blobresourcecontents-mimetype)?: string;\
  [\_meta](#blobresourcecontents-_meta)?: \{ \[key: string]: unknown };\
  [blob](#blobresourcecontents-blob): string;\
} uri: string[Permalink](#blobresourcecontents-uri) The URI of this resource.  Inherited from ResourceContents.uri mimeType?: string[Permalink](#blobresourcecontents-mimetype) The MIME type of this resource, if known.  Inherited from ResourceContents.mimeType \_meta?: \{ \[key: string]: unknown }[Permalink](#blobresourcecontents-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from ResourceContents.\_meta blob: string[Permalink](#blobresourcecontents-blob) A base64-encoded string representing the binary data of the item.&#x20;

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
of the LLM and/or the user.  type: "resource"[Permalink](#embeddedresource-type)  resource: TextResourceContents | BlobResourceContents[Permalink](#embeddedresource-resource)  annotations?: Annotations[Permalink](#embeddedresource-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#embeddedresource-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ImageContent`

interface ImageContent \{\
  [type](#imagecontent-type): "image";\
  [data](#imagecontent-data): string;\
  [mimeType](#imagecontent-mimetype): string;\
  [annotations](#imagecontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#imagecontent-_meta)?: \{ \[key: string]: unknown };\
}An image provided to or from an LLM.  type: "image"[Permalink](#imagecontent-type)  data: string[Permalink](#imagecontent-data) The base64-encoded image data.  mimeType: string[Permalink](#imagecontent-mimetype) The MIME type of the image. Different providers may support different image types.  annotations?: Annotations[Permalink](#imagecontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#imagecontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

### `ResourceLink`

interface ResourceLink \{\
  [name](#resourcelink-name): string;\
  [title](#resourcelink-title)?: string;\
  [uri](#resourcelink-uri): string;\
  [description](#resourcelink-description)?: string;\
  [mimeType](#resourcelink-mimetype)?: string;\
  [annotations](#resourcelink-annotations)?: [Annotations](#annotations);\
  [size](#resourcelink-size)?: number;\
  [\_meta](#resourcelink-_meta)?: \{ \[key: string]: unknown };\
  [type](#resourcelink-type): "resource\_link";\
}A resource that the server is capable of reading, included in a prompt or tool call result. Note: resource links returned by tools are not guaranteed to appear in the results of `resources/list` requests.  name: string[Permalink](#resourcelink-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from [Resource](#resource).[name](#resource-name) title?: string[Permalink](#resourcelink-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from [Resource](#resource).[title](#resource-title) uri: string[Permalink](#resourcelink-uri) The URI of this resource.  Inherited from [Resource](#resource).[uri](#resource-uri) description?: string[Permalink](#resourcelink-description) A description of what this resource represents. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  Inherited from [Resource](#resource).[description](#resource-description) mimeType?: string[Permalink](#resourcelink-mimetype) The MIME type of this resource, if known.  Inherited from [Resource](#resource).[mimeType](#resource-mimetype) annotations?: Annotations[Permalink](#resourcelink-annotations) Optional annotations for the client.  Inherited from [Resource](#resource).[annotations](#resource-annotations) size?: number[Permalink](#resourcelink-size) The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known. This can be used by Hosts to display file sizes and estimate context window usage.  Inherited from [Resource](#resource).[size](#resource-size) \_meta?: \{ \[key: string]: unknown }[Permalink](#resourcelink-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Resource](#resource).[\_meta](#resource-_meta) type: "resource\_link"[Permalink](#resourcelink-type)&#x20;

### `TextContent`

interface TextContent \{\
  [type](#textcontent-type): "text";\
  [text](#textcontent-text): string;\
  [annotations](#textcontent-annotations)?: [Annotations](#annotations);\
  [\_meta](#textcontent-_meta)?: \{ \[key: string]: unknown };\
}Text provided to or from an LLM.  type: "text"[Permalink](#textcontent-type)  text: string[Permalink](#textcontent-text) The text content of the message.  annotations?: Annotations[Permalink](#textcontent-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#textcontent-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

### `TextResourceContents`

interface TextResourceContents \{\
  [uri](#textresourcecontents-uri): string;\
  [mimeType](#textresourcecontents-mimetype)?: string;\
  [\_meta](#textresourcecontents-_meta)?: \{ \[key: string]: unknown };\
  [text](#textresourcecontents-text): string;\
} uri: string[Permalink](#textresourcecontents-uri) The URI of this resource.  Inherited from ResourceContents.uri mimeType?: string[Permalink](#textresourcecontents-mimetype) The MIME type of this resource, if known.  Inherited from ResourceContents.mimeType \_meta?: \{ \[key: string]: unknown }[Permalink](#textresourcecontents-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from ResourceContents.\_meta text: string[Permalink](#textresourcecontents-text) The text of the item. This must only be set if the item can actually be represented as text (not binary data).&#x20;

## `completion/complete`

### `CompleteRequest`

interface CompleteRequest \{\
  [method](#completerequest-method): "completion/complete";\
  [params](#completerequest-params): \{\
    ref: [PromptReference](#promptreference) | [ResourceTemplateReference](#resourcetemplatereference);\
    argument: \{ name: string; value: string };\
    context?: \{ arguments?: \{ \[key: string]: string } };\
  };\
}A request from the client to the server, to ask for completion options.  method: "completion/complete"[Permalink](#completerequest-method)  Overrides Request.method params: \{    ref: PromptReference | ResourceTemplateReference;    argument: \{ name: string; value: string };    context?: \{ arguments?: \{ \[key: string]: string } }; }[Permalink](#completerequest-params)  Type Declaration <ul> <li> ref: [PromptReference](#promptreference) | [ResourceTemplateReference](#resourcetemplatereference)</li> <li> argument: \{ name: string; value: string } The argument's information  <ul> <li> name: string The name of the argument </li> <li> value: string The value of the argument to use for completion matching. </li></ul></li> <li> `Optional`context?: \{ arguments?: \{ \[key: string]: string } } Additional, optional context for completions  <ul> <li> `Optional`arguments?: \{ \[key: string]: string } Previously-resolved variables in a URI template or prompt. </li></ul></li></ul> Overrides Request.params

### `CompleteResult`

interface CompleteResult \{\
  [\_meta](#completeresult-_meta)?: \{ \[key: string]: unknown };\
  [completion](#completeresult-completion): \{ values: string\[]; total?: number; hasMore?: boolean };\
  \[key: string]: unknown;\
}The server's response to a completion/complete request  \_meta?: \{ \[key: string]: unknown }[Permalink](#completeresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) completion: \{ values: string\[]; total?: number; hasMore?: boolean }[Permalink](#completeresult-completion)  Type Declaration <ul> <li> values: string\[] An array of completion values. Must not exceed 100 items. </li> <li> `Optional`total?: number The total number of completion options available. This can exceed the number of values actually sent in the response. </li> <li> `Optional`hasMore?: boolean Indicates whether there are additional completion options beyond those provided in the current response, even if the exact total is unknown. </li></ul>

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
  [method](#elicitrequest-method): "elicitation/create";\
  [params](#elicitrequest-params): \{\
    message: string;\
    requestedSchema: \{\
      type: "object";\
      properties: \{ \[key: string]: [PrimitiveSchemaDefinition](#primitiveschemadefinition) };\
      required?: string\[];\
    };\
  };\
}A request from the server to elicit additional information from the user via the client.  method: "elicitation/create"[Permalink](#elicitrequest-method)  Overrides Request.method params: \{    message: string;    requestedSchema: \{        type: "object";        properties: \{ \[key: string]: PrimitiveSchemaDefinition };        required?: string\[];    }; }[Permalink](#elicitrequest-params)  Type Declaration <ul> <li> message: string The message to present to the user. </li> <li> requestedSchema: \{\
  type: "object";\
  properties: \{ \[key: string]: [PrimitiveSchemaDefinition](#primitiveschemadefinition) };\
  required?: string\[];\
} A restricted subset of JSON Schema.
Only top-level properties are allowed, without nesting. </li></ul> Overrides Request.params

### `ElicitResult`

interface ElicitResult \{\
  [\_meta](#elicitresult-_meta)?: \{ \[key: string]: unknown };\
  [action](#elicitresult-action): "accept" | "decline" | "cancel";\
  [content](#elicitresult-content)?: \{ \[key: string]: string | number | boolean };\
  \[key: string]: unknown;\
}The client's response to an elicitation request.  \_meta?: \{ \[key: string]: unknown }[Permalink](#elicitresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) action: "accept" | "decline" | "cancel"[Permalink](#elicitresult-action) The user action in response to the elicitation. <ul> <li>"accept": User submitted the form/confirmed the action</li> <li>"decline": User explicitly declined the action</li> <li>"cancel": User dismissed without making an explicit choice</li> </ul>  content?: \{ \[key: string]: string | number | boolean }[Permalink](#elicitresult-content) The submitted form data, only present when action is "accept".
Contains values matching the requested schema.&#x20;

### `BooleanSchema`

interface BooleanSchema \{\
  [type](#booleanschema-type): "boolean";\
  [title](#booleanschema-title)?: string;\
  [description](#booleanschema-description)?: string;\
  [default](#booleanschema-default)?: boolean;\
} type: "boolean"[Permalink](#booleanschema-type)  title?: string[Permalink](#booleanschema-title)  description?: string[Permalink](#booleanschema-description)  default?: boolean[Permalink](#booleanschema-default)&#x20;

### `EnumSchema`

interface EnumSchema \{\
  [type](#enumschema-type): "string";\
  [title](#enumschema-title)?: string;\
  [description](#enumschema-description)?: string;\
  [enum](#enumschema-enum): string\[];\
  [enumNames](#enumschema-enumnames)?: string\[];\
} type: "string"[Permalink](#enumschema-type)  title?: string[Permalink](#enumschema-title)  description?: string[Permalink](#enumschema-description)  enum: string\[][Permalink](#enumschema-enum)  enumNames?: string\[][Permalink](#enumschema-enumnames)&#x20;

### `NumberSchema`

interface NumberSchema \{\
  [type](#numberschema-type): "number" | "integer";\
  [title](#numberschema-title)?: string;\
  [description](#numberschema-description)?: string;\
  [minimum](#numberschema-minimum)?: number;\
  [maximum](#numberschema-maximum)?: number;\
} type: "number" | "integer"[Permalink](#numberschema-type)  title?: string[Permalink](#numberschema-title)  description?: string[Permalink](#numberschema-description)  minimum?: number[Permalink](#numberschema-minimum)  maximum?: number[Permalink](#numberschema-maximum)&#x20;

### `PrimitiveSchemaDefinition`

PrimitiveSchemaDefinition:\
  | [StringSchema](#stringschema)\
  | [NumberSchema](#numberschema)\
  | [BooleanSchema](#booleanschema)\
  | [EnumSchema](#enumschema)Restricted schema definitions that only allow primitive types
without nested objects or arrays.&#x20;

### `StringSchema`

interface StringSchema \{\
  [type](#stringschema-type): "string";\
  [title](#stringschema-title)?: string;\
  [description](#stringschema-description)?: string;\
  [minLength](#stringschema-minlength)?: number;\
  [maxLength](#stringschema-maxlength)?: number;\
  [format](#stringschema-format)?: "uri" | "email" | "date" | "date-time";\
} type: "string"[Permalink](#stringschema-type)  title?: string[Permalink](#stringschema-title)  description?: string[Permalink](#stringschema-description)  minLength?: number[Permalink](#stringschema-minlength)  maxLength?: number[Permalink](#stringschema-maxlength)  format?: "uri" | "email" | "date" | "date-time"[Permalink](#stringschema-format)&#x20;

## `initialize`

### `InitializeRequest`

interface InitializeRequest \{\
  [method](#initializerequest-method): "initialize";\
  [params](#initializerequest-params): \{\
    protocolVersion: string;\
    capabilities: [ClientCapabilities](#clientcapabilities);\
    clientInfo: [Implementation](#implementation);\
  };\
}This request is sent from the client to the server when it first connects, asking it to begin initialization.  method: "initialize"[Permalink](#initializerequest-method)  Overrides Request.method params: \{    protocolVersion: string;    capabilities: ClientCapabilities;    clientInfo: Implementation; }[Permalink](#initializerequest-params)  Type Declaration <ul> <li> protocolVersion: string The latest version of the Model Context Protocol that the client supports. The client MAY decide to support older versions as well. </li> <li> capabilities: [ClientCapabilities](#clientcapabilities)</li> <li> clientInfo: [Implementation](#implementation)</li></ul> Overrides Request.params

### `InitializeResult`

interface InitializeResult \{\
  [\_meta](#initializeresult-_meta)?: \{ \[key: string]: unknown };\
  [protocolVersion](#initializeresult-protocolversion): string;\
  [capabilities](#initializeresult-capabilities): [ServerCapabilities](#servercapabilities);\
  [serverInfo](#initializeresult-serverinfo): [Implementation](#implementation);\
  [instructions](#initializeresult-instructions)?: string;\
  \[key: string]: unknown;\
}After receiving an initialize request from the client, the server sends this response.  \_meta?: \{ \[key: string]: unknown }[Permalink](#initializeresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) protocolVersion: string[Permalink](#initializeresult-protocolversion) The version of the Model Context Protocol that the server wants to use. This may not match the version that the client requested. If the client cannot support this version, it MUST disconnect.  capabilities: ServerCapabilities[Permalink](#initializeresult-capabilities)  serverInfo: Implementation[Permalink](#initializeresult-serverinfo)  instructions?: string[Permalink](#initializeresult-instructions) Instructions describing how to use the server and its features. This can be used by clients to improve the LLM's understanding of available tools, resources, etc. It can be thought of like a "hint" to the model. For example, this information MAY be added to the system prompt.&#x20;

### `ClientCapabilities`

interface ClientCapabilities \{\
  [experimental](#clientcapabilities-experimental)?: \{ \[key: string]: object };\
  [roots](#clientcapabilities-roots)?: \{ listChanged?: boolean };\
  [sampling](#clientcapabilities-sampling)?: object;\
  [elicitation](#clientcapabilities-elicitation)?: object;\
}Capabilities a client may support. Known capabilities are defined here, in this schema, but this is not a closed set: any client can define its own, additional capabilities.  experimental?: \{ \[key: string]: object }[Permalink](#clientcapabilities-experimental) Experimental, non-standard capabilities that the client supports.  roots?: \{ listChanged?: boolean }[Permalink](#clientcapabilities-roots) Present if the client supports listing roots.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether the client supports notifications for changes to the roots list. </li></ul> sampling?: object[Permalink](#clientcapabilities-sampling) Present if the client supports sampling from an LLM.  elicitation?: object[Permalink](#clientcapabilities-elicitation) Present if the client supports elicitation from the server.&#x20;

### `Implementation`

interface Implementation \{\
  [name](#implementation-name): string;\
  [title](#implementation-title)?: string;\
  [version](#implementation-version): string;\
}Describes the name and version of an MCP implementation, with an optional title for UI representation.  name: string[Permalink](#implementation-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#implementation-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title version: string[Permalink](#implementation-version)&#x20;

### `ServerCapabilities`

interface ServerCapabilities \{\
  [experimental](#servercapabilities-experimental)?: \{ \[key: string]: object };\
  [logging](#servercapabilities-logging)?: object;\
  [completions](#servercapabilities-completions)?: object;\
  [prompts](#servercapabilities-prompts)?: \{ listChanged?: boolean };\
  [resources](#servercapabilities-resources)?: \{ subscribe?: boolean; listChanged?: boolean };\
  [tools](#servercapabilities-tools)?: \{ listChanged?: boolean };\
}Capabilities that a server may support. Known capabilities are defined here, in this schema, but this is not a closed set: any server can define its own, additional capabilities.  experimental?: \{ \[key: string]: object }[Permalink](#servercapabilities-experimental) Experimental, non-standard capabilities that the server supports.  logging?: object[Permalink](#servercapabilities-logging) Present if the server supports sending log messages to the client.  completions?: object[Permalink](#servercapabilities-completions) Present if the server supports argument autocompletion suggestions.  prompts?: \{ listChanged?: boolean }[Permalink](#servercapabilities-prompts) Present if the server offers any prompt templates.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the prompt list. </li></ul> resources?: \{ subscribe?: boolean; listChanged?: boolean }[Permalink](#servercapabilities-resources) Present if the server offers any resources to read.   Type Declaration <ul> <li> `Optional`subscribe?: boolean Whether this server supports subscribing to resource updates. </li> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the resource list. </li></ul> tools?: \{ listChanged?: boolean }[Permalink](#servercapabilities-tools) Present if the server offers any tools to call.   Type Declaration <ul> <li> `Optional`listChanged?: boolean Whether this server supports notifications for changes to the tool list. </li></ul>

## `logging/setLevel`

### `SetLevelRequest`

interface SetLevelRequest \{\
  [method](#setlevelrequest-method): "logging/setLevel";\
  [params](#setlevelrequest-params): \{ level: [LoggingLevel](#logginglevel) };\
}A request from the client to the server, to enable or adjust logging.  method: "logging/setLevel"[Permalink](#setlevelrequest-method)  Overrides Request.method params: \{ level: LoggingLevel }[Permalink](#setlevelrequest-params)  Type Declaration <ul> <li> level: [LoggingLevel](#logginglevel) The level of logging that the client wants to receive from the server. The server should send all logs at this level and higher (i.e., more severe) to the client as notifications/message. </li></ul> Overrides Request.params

## `notifications/cancelled`

### `CancelledNotification`

interface CancelledNotification \{\
  [method](#cancellednotification-method): "notifications/cancelled";\
  [params](#cancellednotification-params): \{ requestId: [RequestId](#requestid); reason?: string };\
}This notification can be sent by either side to indicate that it is cancelling a previously-issued request. The request SHOULD still be in-flight, but due to communication latency, it is always possible that this notification MAY arrive after the request has already finished. This notification indicates that the result will be unused, so any associated processing SHOULD cease. A client MUST NOT attempt to cancel its `initialize` request.  method: "notifications/cancelled"[Permalink](#cancellednotification-method)  Overrides Notification.method params: \{ requestId: RequestId; reason?: string }[Permalink](#cancellednotification-params)  Type Declaration <ul> <li> requestId: [RequestId](#requestid) The ID of the request to cancel. This MUST correspond to the ID of a request previously issued in the same direction. </li> <li> `Optional`reason?: string An optional string describing the reason for the cancellation. This MAY be logged or presented to the user. </li></ul> Overrides Notification.params

## `notifications/initialized`

### `InitializedNotification`

interface InitializedNotification \{\
  [params](#initializednotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [method](#initializednotification-method): "notifications/initialized";\
}This notification is sent from the client to the server after initialization has finished.  params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#initializednotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params method: "notifications/initialized"[Permalink](#initializednotification-method)  Overrides Notification.method

## `notifications/message`

### `LoggingMessageNotification`

interface LoggingMessageNotification \{\
  [method](#loggingmessagenotification-method): "notifications/message";\
  [params](#loggingmessagenotification-params): \{ level: [LoggingLevel](#logginglevel); logger?: string; data: unknown };\
}Notification of a log message passed from server to client. If no logging/setLevel request has been sent from the client, the server MAY decide which messages to send automatically.  method: "notifications/message"[Permalink](#loggingmessagenotification-method)  Overrides Notification.method params: \{ level: LoggingLevel; logger?: string; data: unknown }[Permalink](#loggingmessagenotification-params)  Type Declaration <ul> <li> level: [LoggingLevel](#logginglevel) The severity of this log message. </li> <li> `Optional`logger?: string An optional name of the logger issuing this message. </li> <li> data: unknown The data to be logged, such as a string message or an object. Any JSON serializable type is allowed here. </li></ul> Overrides Notification.params

## `notifications/progress`

### `ProgressNotification`

interface ProgressNotification \{\
  [method](#progressnotification-method): "notifications/progress";\
  [params](#progressnotification-params): \{\
    progressToken: [ProgressToken](#progresstoken);\
    progress: number;\
    total?: number;\
    message?: string;\
  };\
}An out-of-band notification used to inform the receiver of a progress update for a long-running request.  method: "notifications/progress"[Permalink](#progressnotification-method)  Overrides Notification.method params: \{    progressToken: ProgressToken;    progress: number;    total?: number;    message?: string; }[Permalink](#progressnotification-params)  Type Declaration <ul> <li> progressToken: [ProgressToken](#progresstoken) The progress token which was given in the initial request, used to associate this notification with the request that is proceeding. </li> <li> progress: number The progress thus far. This should increase every time progress is made, even if the total is unknown. </li> <li> `Optional`total?: number Total number of items to process (or total progress required), if known. </li> <li> `Optional`message?: string An optional message describing the current progress. </li></ul> Overrides Notification.params

## `notifications/prompts/list_changed`

### `PromptListChangedNotification`

interface PromptListChangedNotification \{\
  [params](#promptlistchangednotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [method](#promptlistchangednotification-method): "notifications/prompts/list\_changed";\
}An optional notification from the server to the client, informing it that the list of prompts it offers has changed. This may be issued by servers without any previous subscription from the client.  params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#promptlistchangednotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params method: "notifications/prompts/list\_changed"[Permalink](#promptlistchangednotification-method)  Overrides Notification.method

## `notifications/resources/list_changed`

### `ResourceListChangedNotification`

interface ResourceListChangedNotification \{\
  [params](#resourcelistchangednotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [method](#resourcelistchangednotification-method): "notifications/resources/list\_changed";\
}An optional notification from the server to the client, informing it that the list of resources it can read from has changed. This may be issued by servers without any previous subscription from the client.  params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#resourcelistchangednotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params method: "notifications/resources/list\_changed"[Permalink](#resourcelistchangednotification-method)  Overrides Notification.method

## `notifications/resources/updated`

### `ResourceUpdatedNotification`

interface ResourceUpdatedNotification \{\
  [method](#resourceupdatednotification-method): "notifications/resources/updated";\
  [params](#resourceupdatednotification-params): \{ uri: string };\
}A notification from the server to the client, informing it that a resource has changed and may need to be read again. This should only be sent if the client previously sent a resources/subscribe request.  method: "notifications/resources/updated"[Permalink](#resourceupdatednotification-method)  Overrides Notification.method params: \{ uri: string }[Permalink](#resourceupdatednotification-params)  Type Declaration <ul> <li> uri: string The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to. </li></ul> Overrides Notification.params

## `notifications/roots/list_changed`

### `RootsListChangedNotification`

interface RootsListChangedNotification \{\
  [params](#rootslistchangednotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [method](#rootslistchangednotification-method): "notifications/roots/list\_changed";\
}A notification from the client to the server, informing it that the list of roots has changed.
This notification should be sent whenever the client adds, removes, or modifies any root.
The server should then request an updated list of roots using the ListRootsRequest.  params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#rootslistchangednotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params method: "notifications/roots/list\_changed"[Permalink](#rootslistchangednotification-method)  Overrides Notification.method

## `notifications/tools/list_changed`

### `ToolListChangedNotification`

interface ToolListChangedNotification \{\
  [params](#toollistchangednotification-params)?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown };\
  [method](#toollistchangednotification-method): "notifications/tools/list\_changed";\
}An optional notification from the server to the client, informing it that the list of tools it offers has changed. This may be issued by servers without any previous subscription from the client.  params?: \{ \_meta?: \{ \[key: string]: unknown }; \[key: string]: unknown }[Permalink](#toollistchangednotification-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage. </li></ul> Inherited from Notification.params method: "notifications/tools/list\_changed"[Permalink](#toollistchangednotification-method)  Overrides Notification.method

## `ping`

### `PingRequest`

interface PingRequest \{\
  [params](#pingrequest-params)?: \{\
    \_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
    \[key: string]: unknown;\
  };\
  [method](#pingrequest-method): "ping";\
}A ping, issued by either the server or the client, to check that the other party is still alive. The receiver must promptly respond, or else may be disconnected.  params?: \{    \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown };    \[key: string]: unknown; }[Permalink](#pingrequest-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  <ul> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul></li></ul> Inherited from Request.params method: "ping"[Permalink](#pingrequest-method)  Overrides Request.method

## `prompts/get`

### `GetPromptRequest`

interface GetPromptRequest \{\
  [method](#getpromptrequest-method): "prompts/get";\
  [params](#getpromptrequest-params): \{ name: string; arguments?: \{ \[key: string]: string } };\
}Used by the client to get a prompt provided by the server.  method: "prompts/get"[Permalink](#getpromptrequest-method)  Overrides Request.method params: \{ name: string; arguments?: \{ \[key: string]: string } }[Permalink](#getpromptrequest-params)  Type Declaration <ul> <li> name: string The name of the prompt or prompt template. </li> <li> `Optional`arguments?: \{ \[key: string]: string } Arguments to use for templating the prompt. </li></ul> Overrides Request.params

### `GetPromptResult`

interface GetPromptResult \{\
  [\_meta](#getpromptresult-_meta)?: \{ \[key: string]: unknown };\
  [description](#getpromptresult-description)?: string;\
  [messages](#getpromptresult-messages): [PromptMessage](#promptmessage)\[];\
  \[key: string]: unknown;\
}The server's response to a prompts/get request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#getpromptresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) description?: string[Permalink](#getpromptresult-description) An optional description for the prompt.  messages: PromptMessage\[][Permalink](#getpromptresult-messages)&#x20;

### `PromptMessage`

interface PromptMessage \{\
  [role](#promptmessage-role): [Role](#role);\
  [content](#promptmessage-content): [ContentBlock](#contentblock);\
}Describes a message returned as part of a prompt. This is similar to `SamplingMessage`, but also supports the embedding of
resources from the MCP server.  role: Role[Permalink](#promptmessage-role)  content: ContentBlock[Permalink](#promptmessage-content)&#x20;

## `prompts/list`

### `ListPromptsRequest`

interface ListPromptsRequest \{\
  [params](#listpromptsrequest-params)?: \{ cursor?: string };\
  [method](#listpromptsrequest-method): "prompts/list";\
}Sent from the client to request a list of prompts and prompt templates the server has.  params?: \{ cursor?: string }[Permalink](#listpromptsrequest-params)  Type Declaration <ul> <li> `Optional`cursor?: string An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor. </li></ul> Inherited from PaginatedRequest.params method: "prompts/list"[Permalink](#listpromptsrequest-method)  Overrides PaginatedRequest.method

### `ListPromptsResult`

interface ListPromptsResult \{\
  [\_meta](#listpromptsresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listpromptsresult-nextcursor)?: string;\
  [prompts](#listpromptsresult-prompts): [Prompt](#prompt)\[];\
  \[key: string]: unknown;\
}The server's response to a prompts/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listpromptsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listpromptsresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor prompts: Prompt\[][Permalink](#listpromptsresult-prompts)&#x20;

### `Prompt`

interface Prompt \{\
  [name](#prompt-name): string;\
  [title](#prompt-title)?: string;\
  [description](#prompt-description)?: string;\
  [arguments](#prompt-arguments)?: [PromptArgument](#promptargument)\[];\
  [\_meta](#prompt-_meta)?: \{ \[key: string]: unknown };\
}A prompt or prompt template that the server offers.  name: string[Permalink](#prompt-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#prompt-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title description?: string[Permalink](#prompt-description) An optional description of what this prompt provides  arguments?: PromptArgument\[][Permalink](#prompt-arguments) A list of arguments to use for templating the prompt.  \_meta?: \{ \[key: string]: unknown }[Permalink](#prompt-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

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
  [params](#listresourcesrequest-params)?: \{ cursor?: string };\
  [method](#listresourcesrequest-method): "resources/list";\
}Sent from the client to request a list of resources the server has.  params?: \{ cursor?: string }[Permalink](#listresourcesrequest-params)  Type Declaration <ul> <li> `Optional`cursor?: string An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor. </li></ul> Inherited from PaginatedRequest.params method: "resources/list"[Permalink](#listresourcesrequest-method)  Overrides PaginatedRequest.method

### `ListResourcesResult`

interface ListResourcesResult \{\
  [\_meta](#listresourcesresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listresourcesresult-nextcursor)?: string;\
  [resources](#listresourcesresult-resources): [Resource](#resource)\[];\
  \[key: string]: unknown;\
}The server's response to a resources/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listresourcesresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listresourcesresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor resources: Resource\[][Permalink](#listresourcesresult-resources)&#x20;

### `Resource`

interface Resource \{\
  [name](#resource-name): string;\
  [title](#resource-title)?: string;\
  [uri](#resource-uri): string;\
  [description](#resource-description)?: string;\
  [mimeType](#resource-mimetype)?: string;\
  [annotations](#resource-annotations)?: [Annotations](#annotations);\
  [size](#resource-size)?: number;\
  [\_meta](#resource-_meta)?: \{ \[key: string]: unknown };\
}A known resource that the server is capable of reading.  name: string[Permalink](#resource-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#resource-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title uri: string[Permalink](#resource-uri) The URI of this resource.  description?: string[Permalink](#resource-description) A description of what this resource represents. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  mimeType?: string[Permalink](#resource-mimetype) The MIME type of this resource, if known.  annotations?: Annotations[Permalink](#resource-annotations) Optional annotations for the client.  size?: number[Permalink](#resource-size) The size of the raw resource content, in bytes (i.e., before base64 encoding or any tokenization), if known. This can be used by Hosts to display file sizes and estimate context window usage.  \_meta?: \{ \[key: string]: unknown }[Permalink](#resource-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

## `resources/read`

### `ReadResourceRequest`

interface ReadResourceRequest \{\
  [method](#readresourcerequest-method): "resources/read";\
  [params](#readresourcerequest-params): \{ uri: string };\
}Sent from the client to the server, to read a specific resource URI.  method: "resources/read"[Permalink](#readresourcerequest-method)  Overrides Request.method params: \{ uri: string }[Permalink](#readresourcerequest-params)  Type Declaration <ul> <li> uri: string The URI of the resource to read. The URI can use any protocol; it is up to the server how to interpret it. </li></ul> Overrides Request.params

### `ReadResourceResult`

interface ReadResourceResult \{\
  [\_meta](#readresourceresult-_meta)?: \{ \[key: string]: unknown };\
  [contents](#readresourceresult-contents): ([TextResourceContents](#textresourcecontents) | [BlobResourceContents](#blobresourcecontents))\[];\
  \[key: string]: unknown;\
}The server's response to a resources/read request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#readresourceresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) contents: (TextResourceContents | BlobResourceContents)\[][Permalink](#readresourceresult-contents)&#x20;

## `resources/subscribe`

### `SubscribeRequest`

interface SubscribeRequest \{\
  [method](#subscriberequest-method): "resources/subscribe";\
  [params](#subscriberequest-params): \{ uri: string };\
}Sent from the client to request resources/updated notifications from the server whenever a particular resource changes.  method: "resources/subscribe"[Permalink](#subscriberequest-method)  Overrides Request.method params: \{ uri: string }[Permalink](#subscriberequest-params)  Type Declaration <ul> <li> uri: string The URI of the resource to subscribe to. The URI can use any protocol; it is up to the server how to interpret it. </li></ul> Overrides Request.params

## `resources/templates/list`

### `ListResourceTemplatesRequest`

interface ListResourceTemplatesRequest \{\
  [params](#listresourcetemplatesrequest-params)?: \{ cursor?: string };\
  [method](#listresourcetemplatesrequest-method): "resources/templates/list";\
}Sent from the client to request a list of resource templates the server has.  params?: \{ cursor?: string }[Permalink](#listresourcetemplatesrequest-params)  Type Declaration <ul> <li> `Optional`cursor?: string An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor. </li></ul> Inherited from PaginatedRequest.params method: "resources/templates/list"[Permalink](#listresourcetemplatesrequest-method)  Overrides PaginatedRequest.method

### `ListResourceTemplatesResult`

interface ListResourceTemplatesResult \{\
  [\_meta](#listresourcetemplatesresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listresourcetemplatesresult-nextcursor)?: string;\
  [resourceTemplates](#listresourcetemplatesresult-resourcetemplates): [ResourceTemplate](#resourcetemplate)\[];\
  \[key: string]: unknown;\
}The server's response to a resources/templates/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listresourcetemplatesresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listresourcetemplatesresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor resourceTemplates: ResourceTemplate\[][Permalink](#listresourcetemplatesresult-resourcetemplates)&#x20;

### `ResourceTemplate`

interface ResourceTemplate \{\
  [name](#resourcetemplate-name): string;\
  [title](#resourcetemplate-title)?: string;\
  [uriTemplate](#resourcetemplate-uritemplate): string;\
  [description](#resourcetemplate-description)?: string;\
  [mimeType](#resourcetemplate-mimetype)?: string;\
  [annotations](#resourcetemplate-annotations)?: [Annotations](#annotations);\
  [\_meta](#resourcetemplate-_meta)?: \{ \[key: string]: unknown };\
}A template description for resources available on the server.  name: string[Permalink](#resourcetemplate-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#resourcetemplate-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title uriTemplate: string[Permalink](#resourcetemplate-uritemplate) A URI template (according to RFC 6570) that can be used to construct resource URIs.  description?: string[Permalink](#resourcetemplate-description) A description of what this template is for. This can be used by clients to improve the LLM's understanding of available resources. It can be thought of like a "hint" to the model.  mimeType?: string[Permalink](#resourcetemplate-mimetype) The MIME type for all resources that match this template. This should only be included if all resources matching this template have the same type.  annotations?: Annotations[Permalink](#resourcetemplate-annotations) Optional annotations for the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#resourcetemplate-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

## `resources/unsubscribe`

### `UnsubscribeRequest`

interface UnsubscribeRequest \{\
  [method](#unsubscriberequest-method): "resources/unsubscribe";\
  [params](#unsubscriberequest-params): \{ uri: string };\
}Sent from the client to request cancellation of resources/updated notifications from the server. This should follow a previous resources/subscribe request.  method: "resources/unsubscribe"[Permalink](#unsubscriberequest-method)  Overrides Request.method params: \{ uri: string }[Permalink](#unsubscriberequest-params)  Type Declaration <ul> <li> uri: string The URI of the resource to unsubscribe from. </li></ul> Overrides Request.params

## `roots/list`

### `ListRootsRequest`

interface ListRootsRequest \{\
  [params](#listrootsrequest-params)?: \{\
    \_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown };\
    \[key: string]: unknown;\
  };\
  [method](#listrootsrequest-method): "roots/list";\
}Sent from the server to request a list of root URIs from the client. Roots allow
servers to ask for specific directories or files to operate on. A common example
for roots is providing a set of repositories or directories a server should operate
on. This request is typically used when the server needs to understand the file system
structure or access specific locations that the client has permission to read from.  params?: \{    \_meta?: \{ progressToken?: ProgressToken; \[key: string]: unknown };    \[key: string]: unknown; }[Permalink](#listrootsrequest-params)  Type Declaration <ul> <li> \[key: string]: unknown</li> <li> `Optional`\_meta?: \{ progressToken?: [ProgressToken](#progresstoken); \[key: string]: unknown } See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  <ul> <li> `Optional`progressToken?: [ProgressToken](#progresstoken) If specified, the caller is requesting out-of-band progress notifications for this request (as represented by notifications/progress). The value of this parameter is an opaque token that will be attached to any subsequent notifications. The receiver is not obligated to provide these notifications. </li></ul></li></ul> Inherited from Request.params method: "roots/list"[Permalink](#listrootsrequest-method)  Overrides Request.method

### `ListRootsResult`

interface ListRootsResult \{\
  [\_meta](#listrootsresult-_meta)?: \{ \[key: string]: unknown };\
  [roots](#listrootsresult-roots): [Root](#root)\[];\
  \[key: string]: unknown;\
}The client's response to a roots/list request from the server.
This result contains an array of Root objects, each representing a root directory
or file that the server can operate on.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listrootsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) roots: Root\[][Permalink](#listrootsresult-roots)&#x20;

### `Root`

interface Root \{\
  [uri](#root-uri): string;\
  [name](#root-name)?: string;\
  [\_meta](#root-_meta)?: \{ \[key: string]: unknown };\
}Represents a root directory or file that the server can operate on.  uri: string[Permalink](#root-uri) The URI identifying the root. This *must* start with file:// for now.
This restriction may be relaxed in future versions of the protocol to allow
other URI schemes.  name?: string[Permalink](#root-name) An optional name for the root. This can be used to provide a human-readable
identifier for the root, which may be useful for display purposes or for
referencing the root in other parts of the application.  \_meta?: \{ \[key: string]: unknown }[Permalink](#root-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

## `sampling/createMessage`

### `CreateMessageRequest`

interface CreateMessageRequest \{\
  [method](#createmessagerequest-method): "sampling/createMessage";\
  [params](#createmessagerequest-params): \{\
    messages: [SamplingMessage](#samplingmessage)\[];\
    modelPreferences?: [ModelPreferences](#modelpreferences);\
    systemPrompt?: string;\
    includeContext?: "none" | "thisServer" | "allServers";\
    temperature?: number;\
    maxTokens: number;\
    stopSequences?: string\[];\
    metadata?: object;\
  };\
}A request from the server to sample an LLM via the client. The client has full discretion over which model to select. The client should also inform the user before beginning sampling, to allow them to inspect the request (human in the loop) and decide whether to approve it.  method: "sampling/createMessage"[Permalink](#createmessagerequest-method)  Overrides Request.method params: \{    messages: SamplingMessage\[];    modelPreferences?: ModelPreferences;    systemPrompt?: string;    includeContext?: "none" | "thisServer" | "allServers";    temperature?: number;    maxTokens: number;    stopSequences?: string\[];    metadata?: object; }[Permalink](#createmessagerequest-params)  Type Declaration <ul> <li> messages: [SamplingMessage](#samplingmessage)\[]</li> <li> `Optional`modelPreferences?: [ModelPreferences](#modelpreferences) The server's preferences for which model to select. The client MAY ignore these preferences. </li> <li> `Optional`systemPrompt?: string An optional system prompt the server wants to use for sampling. The client MAY modify or omit this prompt. </li> <li> `Optional`includeContext?: "none" | "thisServer" | "allServers" A request to include context from one or more MCP servers (including the caller), to be attached to the prompt. The client MAY ignore this request. </li> <li> `Optional`temperature?: number</li> <li> maxTokens: number The requested maximum number of tokens to sample (to prevent runaway completions). The client MAY choose to sample fewer tokens than the requested maximum. </li> <li> `Optional`stopSequences?: string\[]</li> <li> `Optional`metadata?: object Optional metadata to pass through to the LLM provider. The format of this metadata is provider-specific. </li></ul> Overrides Request.params

### `CreateMessageResult`

interface CreateMessageResult \{\
  [\_meta](#createmessageresult-_meta)?: \{ \[key: string]: unknown };\
  [model](#createmessageresult-model): string;\
  [stopReason](#createmessageresult-stopreason)?: string;\
  [role](#createmessageresult-role): [Role](#role);\
  [content](#createmessageresult-content): [TextContent](#textcontent) | [ImageContent](#imagecontent) | [AudioContent](#audiocontent);\
  \[key: string]: unknown;\
}The client's response to a sampling/create\_message request from the server. The client should inform the user before returning the sampled message, to allow them to inspect the response (human in the loop) and decide whether to allow the server to see it.  \_meta?: \{ \[key: string]: unknown }[Permalink](#createmessageresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) model: string[Permalink](#createmessageresult-model) The name of the model that generated the message.  stopReason?: string[Permalink](#createmessageresult-stopreason) The reason why sampling stopped, if known.  role: Role[Permalink](#createmessageresult-role)  Inherited from [SamplingMessage](#samplingmessage).[role](#samplingmessage-role) content: TextContent | ImageContent | AudioContent[Permalink](#createmessageresult-content)  Inherited from [SamplingMessage](#samplingmessage).[content](#samplingmessage-content)

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
  [content](#samplingmessage-content): [TextContent](#textcontent) | [ImageContent](#imagecontent) | [AudioContent](#audiocontent);\
}Describes a message issued to or received from an LLM API.  role: Role[Permalink](#samplingmessage-role)  content: TextContent | ImageContent | AudioContent[Permalink](#samplingmessage-content)&#x20;

## `tools/call`

### `CallToolRequest`

interface CallToolRequest \{\
  [method](#calltoolrequest-method): "tools/call";\
  [params](#calltoolrequest-params): \{ name: string; arguments?: \{ \[key: string]: unknown } };\
}Used by the client to invoke a tool provided by the server.  method: "tools/call"[Permalink](#calltoolrequest-method)  Overrides Request.method params: \{ name: string; arguments?: \{ \[key: string]: unknown } }[Permalink](#calltoolrequest-params)  Overrides Request.params

### `CallToolResult`

interface CallToolResult \{\
  [\_meta](#calltoolresult-_meta)?: \{ \[key: string]: unknown };\
  [content](#calltoolresult-content): [ContentBlock](#contentblock)\[];\
  [structuredContent](#calltoolresult-structuredcontent)?: \{ \[key: string]: unknown };\
  [isError](#calltoolresult-iserror)?: boolean;\
  \[key: string]: unknown;\
}The server's response to a tool call.  \_meta?: \{ \[key: string]: unknown }[Permalink](#calltoolresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from [Result](#result).[\_meta](#result-_meta) content: ContentBlock\[][Permalink](#calltoolresult-content) A list of content objects that represent the unstructured result of the tool call.  structuredContent?: \{ \[key: string]: unknown }[Permalink](#calltoolresult-structuredcontent) An optional JSON object that represents the structured result of the tool call.  isError?: boolean[Permalink](#calltoolresult-iserror) Whether the tool call ended in an error. If not set, this is assumed to be false (the call was successful). Any errors that originate from the tool SHOULD be reported inside the result
object, with `isError` set to true, *not* as an MCP protocol-level error
response. Otherwise, the LLM would not be able to see that an error occurred
and self-correct. However, any errors in *finding* the tool, an error indicating that the
server does not support tool calls, or any other exceptional conditions,
should be reported as an MCP error response.&#x20;

## `tools/list`

### `ListToolsRequest`

interface ListToolsRequest \{\
  [params](#listtoolsrequest-params)?: \{ cursor?: string };\
  [method](#listtoolsrequest-method): "tools/list";\
}Sent from the client to request a list of tools the server has.  params?: \{ cursor?: string }[Permalink](#listtoolsrequest-params)  Type Declaration <ul> <li> `Optional`cursor?: string An opaque token representing the current pagination position.
If provided, the server should return results starting after this cursor. </li></ul> Inherited from PaginatedRequest.params method: "tools/list"[Permalink](#listtoolsrequest-method)  Overrides PaginatedRequest.method

### `ListToolsResult`

interface ListToolsResult \{\
  [\_meta](#listtoolsresult-_meta)?: \{ \[key: string]: unknown };\
  [nextCursor](#listtoolsresult-nextcursor)?: string;\
  [tools](#listtoolsresult-tools): [Tool](#tool)\[];\
  \[key: string]: unknown;\
}The server's response to a tools/list request from the client.  \_meta?: \{ \[key: string]: unknown }[Permalink](#listtoolsresult-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.  Inherited from PaginatedResult.\_meta nextCursor?: string[Permalink](#listtoolsresult-nextcursor) An opaque token representing the pagination position after the last returned result.
If present, there may be more results available.  Inherited from PaginatedResult.nextCursor tools: Tool\[][Permalink](#listtoolsresult-tools)&#x20;

### `Tool`

interface Tool \{\
  [name](#tool-name): string;\
  [title](#tool-title)?: string;\
  [description](#tool-description)?: string;\
  [inputSchema](#tool-inputschema): \{\
    type: "object";\
    properties?: \{ \[key: string]: object };\
    required?: string\[];\
  };\
  [outputSchema](#tool-outputschema)?: \{\
    type: "object";\
    properties?: \{ \[key: string]: object };\
    required?: string\[];\
  };\
  [annotations](#tool-annotations)?: [ToolAnnotations](#toolannotations);\
  [\_meta](#tool-_meta)?: \{ \[key: string]: unknown };\
}Definition for a tool the client can call.  name: string[Permalink](#tool-name) Intended for programmatic or logical use, but used as a display name in past specs or fallback (if title isn't present).  Inherited from BaseMetadata.name title?: string[Permalink](#tool-title) Intended for UI and end-user contexts — optimized to be human-readable and easily understood,
even by those unfamiliar with domain-specific terminology. If not provided, the name should be used for display (except for Tool,
where `annotations.title` should be given precedence over using `name`,
if present).  Inherited from BaseMetadata.title description?: string[Permalink](#tool-description) A human-readable description of the tool. This can be used by clients to improve the LLM's understanding of available tools. It can be thought of like a "hint" to the model.  inputSchema: \{    type: "object";    properties?: \{ \[key: string]: object };    required?: string\[]; }[Permalink](#tool-inputschema) A JSON Schema object defining the expected parameters for the tool.  outputSchema?: \{    type: "object";    properties?: \{ \[key: string]: object };    required?: string\[]; }[Permalink](#tool-outputschema) An optional JSON Schema object defining the structure of the tool's output returned in
the structuredContent field of a CallToolResult.  annotations?: ToolAnnotations[Permalink](#tool-annotations) Optional additional tool information. Display name precedence order is: title, annotations.title, then name.  \_meta?: \{ \[key: string]: unknown }[Permalink](#tool-_meta) See [General fields: `_meta`](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#meta) for notes on `_meta` usage.&#x20;

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
will have no additional effect on the its environment. (This property is meaningful only when `readOnlyHint == false`) Default: false  openWorldHint?: boolean[Permalink](#toolannotations-openworldhint) If true, this tool may interact with an "open world" of external
entities. If false, the tool's domain of interaction is closed.
For example, the world of a web search tool is open, whereas that
of a memory tool is not. Default: true&#x20;
