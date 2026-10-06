---
title: Embeddings
url: https://platform.claude.com/docs/en/build-with-claude/embeddings
description: Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.
---

## Before implementing embeddings

When selecting an embeddings provider, there are several factors you can consider depending on your needs and preferences:

* Dataset size & domain specificity: size of the model training dataset and its relevance to the domain you want to embed. Larger or more domain-specific data generally produces better in-domain embeddings
* Inference performance: embedding lookup speed and end-to-end latency. This is a particularly important consideration for large scale production deployments
* Customization: options for continued training on private data, or specialization of models for very specific domains. This can improve performance on unique vocabularies

## How to get embeddings with Anthropic

Anthropic does not offer its own embedding model. One embeddings provider with a wide variety of models and capabilities is Voyage AI by MongoDB.

Voyage AI makes embedding models and rerankers. Its embedding models include general-purpose, multimodal, contextualized, and domain-specific models.

The rest of this guide is for Voyage AI, but you should assess a variety of embeddings vendors to find the best fit for your specific use case.

## Available models

Voyage AI offers the following text embedding models:

**Latest generation**

| Model            | Context length | Embedding dimension            | Description                                                                                                                                                                                                                                                                                          |
| ---------------- | -------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-4-large` | 32,000         | 1024 (default), 256, 512, 2048 | The best general-purpose and multilingual retrieval quality. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                                                                                                                               |
| `voyage-4`       | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for general-purpose and multilingual retrieval quality. Balances quality and efficiency. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                                                                                         |
| `voyage-4-lite`  | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for latency and cost. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details.                                                                                                                                                                            |
| `voyage-code-4`  | 32,000         | 1024 (default), 256, 512, 2048 | Optimized for **code** retrieval and agentic coding applications. See the [voyage-code-4 blog post](https://blog.voyageai.com/2026/08/13/voyage-code-4/) for details.                                                                                                                                |
| `voyage-4-nano`  | 32,000         | 2048 (default), 256, 512, 1024 | Open-weight model (Apache 2.0 license) that you download from [Hugging Face](https://huggingface.co/voyageai/voyage-4-nano) and run yourself. Not available through the Atlas Embedding and Reranking API. See the [Voyage 4 blog post](https://blog.voyageai.com/2026/01/15/voyage-4/) for details. |

**Previous generation**

For each model's lifecycle status and recommended replacement, see [Model deprecations, lifecycle states, and support](https://www.mongodb.com/docs/voyageai/models/lifecycle/) in the MongoDB documentation.

| Model              | Context length | Embedding dimension            | Description                                                                                                                                                                                         |
| ------------------ | -------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-3-large`   | 32,000         | 1024 (default), 256, 512, 2048 | Previous generation of `voyage-4-large`. See the [voyage-3-large blog post](https://blog.voyageai.com/2025/01/07/voyage-3-large/) for details.                                                      |
| `voyage-3.5`       | 32,000         | 1024 (default), 256, 512, 2048 | Previous generation of `voyage-4`. See the [voyage-3.5 blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                                    |
| `voyage-3.5-lite`  | 32,000         | 1024 (default), 256, 512, 2048 | Previous generation of `voyage-4-lite`. See the [voyage-3.5 blog post](https://blog.voyageai.com/2025/05/20/voyage-3-5/) for details.                                                               |
| `voyage-code-3`    | 32,000         | 1024 (default), 256, 512, 2048 | Previous generation of `voyage-code-4`. See the [voyage-code-3 blog post](https://blog.voyageai.com/2024/12/04/voyage-code-3/) for details.                                                         |
| `voyage-finance-2` | 32,000         | 1024                           | Optimized for **finance** retrieval and RAG. See the [voyage-finance-2 blog post](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/) for details.   |
| `voyage-law-2`     | 16,000         | 1024                           | Optimized for **legal** retrieval and RAG. See the [voyage-law-2 blog post](https://blog.voyageai.com/2024/04/15/domain-specific-embeddings-and-retrieval-legal-edition-voyage-law-2/) for details. |

Additionally, Voyage AI offers the following multimodal embedding models. Call these models with `multimodal_embed()` instead of `embed()`:

| Model                   | Context length | Embedding dimension            | Description                                                                                                                                                                                                                                                                              |
| ----------------------- | -------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-multimodal-3.5` | 32,000         | 1024 (default), 256, 512, 2048 | Rich multimodal embedding model that can vectorize interleaved text, images, and videos. Includes video support as the first production-grade video embedding model. See the [voyage-multimodal-3.5 blog post](https://blog.voyageai.com/2026/01/15/voyage-multimodal-3-5/) for details. |
| `voyage-multimodal-3`   | 32,000         | 1024                           | Previous generation of `voyage-multimodal-3.5`. Vectorizes interleaved text and content-rich images, such as screenshots of PDFs, slides, tables, figures, and more. See the [voyage-multimodal-3 blog post](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/) for details.     |

The following contextualized chunk embedding models produce chunk-level vectors that capture full document context without manual metadata augmentation. Call these models with `contextualized_embed()` instead of `embed()`:

| Model              | Context length | Embedding dimension            | Description                                                                                                                                                                                                 |
| ------------------ | -------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `voyage-context-4` | 120,000        | 1024 (default), 256, 512, 2048 | Contextualized chunk embeddings optimized for general-purpose and multilingual retrieval quality. See the [voyage-context-4 blog post](https://blog.voyageai.com/2026/06/29/voyage-context-4/) for details. |
| `voyage-context-3` | 120,000        | 1024 (default), 256, 512, 2048 | Previous generation of `voyage-context-4`. See the [voyage-context-3 blog post](https://blog.voyageai.com/2025/07/23/voyage-context-3/) for details.                                                        |

The 120,000-token limit applies when you set `enable_auto_chunking` to `true`. Otherwise, the total number of tokens across all inputs can't exceed 32,000.

Voyage AI also offers rerankers, which take a query and a list of documents and return them ranked by relevance to the query. Call these models with `rerank()`:

| Model             | Context length | Description                                                                                                                                    |
| ----------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `rerank-3`        | 32,000         | Highest accuracy. Recommended for most applications. See the [rerank-3 blog post](https://blog.voyageai.com/2026/09/30/rerank-3/) for details. |
| `rerank-3-lite`   | 32,000         | Optimized for latency and cost. See the [rerank-3 blog post](https://blog.voyageai.com/2026/09/30/rerank-3/) for details.                      |
| `rerank-2.5`      | 32,000         | Previous generation of `rerank-3`. See the [rerank-2.5 blog post](https://blog.voyageai.com/2025/08/11/rerank-2-5/) for details.               |
| `rerank-2.5-lite` | 32,000         | Previous generation of `rerank-3-lite`. See the [rerank-2.5 blog post](https://blog.voyageai.com/2025/08/11/rerank-2-5/) for details.          |

Need help deciding which model to use? See [Voyage AI embedding and reranking models overview](https://www.mongodb.com/docs/voyageai/models/) in the MongoDB documentation.

## Getting started with Voyage AI

To access Voyage AI models, create a model API key in MongoDB Atlas:

1. Sign up for a MongoDB Atlas account, or log in.
2. In your Atlas project, select **AI Model APIs** in the navigation bar, click **Create model API key**, name the key, and click **Create**.
3. Set the API key as an environment variable for convenience:

```bash
export VOYAGE_API_KEY="<your model API key>"
```

For more detail, see [Voyage AI quick start](https://www.mongodb.com/docs/voyageai/quickstart/) in the MongoDB documentation.

You can obtain the embeddings by either using the official [`voyageai` Python package](https://github.com/voyage-ai/voyageai-python) or HTTP requests, as described in the following sections. Voyage AI also has an official TypeScript client. To use it with a model API key from Atlas, set its `environment` option to `https://ai.mongodb.com/v1`, as described in [TypeScript client](https://www.mongodb.com/docs/voyageai/api-and-clients/#typescript-client) in the MongoDB documentation.

### Voyage AI Python library

Install the `voyageai` package using the following command. To use a model API key from Atlas, you need version 0.3.7 or later.

```bash
pip install -U voyageai
```

Then, you can create a client object and start using it to embed your texts:

```python
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your model API key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-4", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

`result.embeddings` is a list of two embedding vectors, each containing 1024 floating-point numbers. After running the preceding code, the two embeddings are printed on the screen:

```text
[-0.013131560757756233, 0.019828535616397858, ...]   # embedding for "Sample text 1"
[-0.0069352793507277966, 0.020878976210951805, ...]  # embedding for "Sample text 2"
```

When creating the embeddings, you can specify a few other arguments to the `embed()` function.

For more information on the Python package, see [Accessing Voyage AI models](https://www.mongodb.com/docs/voyageai/api-and-clients/) in the MongoDB documentation.

### Voyage AI HTTP API

You can also get embeddings by sending HTTP requests to the Atlas Embedding and Reranking API. For example, you can send an HTTP request through the `curl` command in a terminal:

```bash cURL
curl https://ai.mongodb.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-4",
    "input_type": "document"
  }'
```

The response you would get is a JSON object containing the embeddings and the token usage:

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [-0.013131560757756233, 0.019828535616397858 /* ... */],
      "index": 0
    },
    {
      "object": "embedding",
      "embedding": [-0.0069352793507277966, 0.020878976210951805 /* ... */],
      "index": 1
    }
  ],
  "model": "voyage-4",
  "usage": {
    "total_tokens": 10
  }
}
```

Model API keys from Atlas work with `ai.mongodb.com`, except keys scoped to a geography, which use that geography's endpoint. If you have an API key from the Voyage AI platform instead, see [Migrate your applications to use the Atlas Embedding and Reranking API](https://www.mongodb.com/docs/voyageai/tutorials/migrate-to-atlas/) in the MongoDB documentation.

For the full request and response reference, see [Create text embeddings](https://www.mongodb.com/docs/api/doc/atlas-embedding-and-reranking-api/operation/operation-createembedding) in the Atlas Embedding and Reranking API documentation.

### AWS Marketplace

Voyage AI models are also available on AWS Marketplace through [MongoDB's seller profile](https://aws.amazon.com/marketplace/seller-profile?id=c9032c7b-70dd-459f-834f-c1e23cf3d092). For instructions, see [Deploy Voyage AI models using AWS Marketplace](https://www.mongodb.com/docs/voyageai/management/aws-marketplace/) in the MongoDB documentation.

## Quickstart example

The following brief example shows how to use embeddings.

Suppose you have a small corpus of six documents to retrieve from

```python
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature.",
]
```

First, use Voyage AI to convert each document into an embedding vector.

```python
import voyageai

vo = voyageai.Client()

# Embed the documents
doc_embds = vo.embed(documents, model="voyage-4", input_type="document").embeddings
```

The embeddings allow you to do semantic search / retrieval in the vector space. Given an example query,

```python
query = "When is Apple's conference call scheduled?"
```

Next, convert it into an embedding and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.

```python
import numpy as np

# Embed the query
query_embd = vo.embed([query], model="voyage-4", input_type="query").embeddings[0]

# Compute the similarity
# Voyage AI embeddings are normalized to length 1, so dot-product
# and cosine similarity are the same.
similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

Note that `input_type="document"` and `input_type="query"` are used for embedding the document and query, respectively. For more about `input_type`, see [When and how should I use the input\_type parameter?](https://platform.claude.com/docs/en/build-with-claude/embeddings#faq) in the FAQ.

The output is the fifth document, which is indeed the most relevant to the query:

```text wrap
Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.
```

If you are looking for a detailed set of recipes on how to do RAG with embeddings, including vector databases, check out the [RAG recipe](https://platform.claude.com/cookbook/third-party-pinecone-rag-using-pinecone).

## FAQ

<AccordionGroup>
  <Accordion title="Why do Voyage AI embeddings have superior quality?">
    Embedding models rely on powerful neural networks to capture and compress semantic context, similar to generative models. Voyage AI's team of experienced AI researchers optimizes every component of the embedding process, including:

    * Model architecture
    * Data collection
    * Loss functions
    * Optimizer selection

    Learn more about Voyage AI's technical approach on the [Voyage AI blog](https://blog.voyageai.com/).
  </Accordion>

  <Accordion title="What embedding models are available and which should I use?">
    For general-purpose embedding, the recommended models are:

    * `voyage-4-large`: Best quality
    * `voyage-4-lite`: Lowest latency and cost
    * `voyage-4`: Balanced performance

    For retrieval, use the `input_type` parameter to specify whether the text is a query or document type.

    Domain-specific models:

    * Legal tasks: `voyage-law-2`
    * Code retrieval and agentic coding: `voyage-code-4`
    * Finance-related tasks: `voyage-finance-2`

    For chunk-level and document-level retrieval: `voyage-context-4`

    For text, images, and video: `voyage-multimodal-3.5`
  </Accordion>

  <Accordion title="Which similarity function should I use?">
    You can use Voyage AI embeddings with dot-product similarity, cosine similarity, or Euclidean distance. For an explanation of embedding similarity, see this [vector similarity guide](https://www.pinecone.io/learn/vector-similarity/).

    Voyage AI embeddings are normalized to length 1, which means that:

    * Cosine similarity is equivalent to dot-product similarity, while the latter can be computed more quickly.
    * Cosine similarity and Euclidean distance result in identical rankings.
  </Accordion>

  <Accordion title="What is the relationship between characters, words, and tokens?">
    See [Tokenization](https://www.mongodb.com/docs/voyageai/tutorials/tokenization/) in the MongoDB documentation.
  </Accordion>

  <Accordion title="When and how should I use the input_type parameter?">
    For all retrieval tasks and use cases (for example, RAG), use the `input_type` parameter to specify whether the input text is a query or document. Do not omit `input_type` or set `input_type=None`. Specifying whether input text is a query or document can create better dense vector representations for retrieval, which can lead to better retrieval quality.

    When using the `input_type` parameter, special prompts are prepended to the input text prior to embedding. Specifically:

    > 📘 **Prompts associated with `input_type`**
    >
    > * For a query, the prompt is `"Represent the query for retrieving supporting documents: "`.
    >
    > * For a document, the prompt is `"Represent the document for retrieval: "`.
    >
    > * Example
    >
    >   * When `input_type="query"`, a query such as "When is Apple's conference call scheduled?" will become "**Represent the query for retrieving supporting documents:** When is Apple's conference call scheduled?"
    >   * When `input_type="document"`, a document such as "Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET." will become "**Represent the document for retrieval:** Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET."
  </Accordion>

  <Accordion title="What quantization options are available?">
    Quantization in embeddings converts high-precision values, such as 32-bit single-precision floating-point numbers, to lower-precision formats such as 8-bit integers or 1-bit binary values, reducing storage, memory, and costs by 4x and 32x, respectively. Supported Voyage AI models enable quantization by specifying the output data type with the `output_dtype` parameter:

    * `float`: Each returned embedding is a list of 32-bit (4-byte) single-precision floating-point numbers. This is the default and provides the highest precision / retrieval accuracy.
    * `int8` and `uint8`: Each returned embedding is a list of 8-bit (1-byte) integers ranging from -128 to 127 and 0 to 255, respectively.
    * `binary` and `ubinary`: Each returned embedding is a list of 8-bit integers that represent bit-packed, quantized single-bit embedding values: `int8` for `binary` and `uint8` for `ubinary`. The length of the returned list of integers is 1/8 of the actual dimension of the embedding. The binary type uses the offset binary method, as the following example shows.

    > **Binary quantization example**
    >
    > Consider the following eight embedding values: -0.03955078, 0.006214142, -0.07446289, -0.039001465, 0.0046463013, 0.00030612946, -0.08496094, and 0.03994751. With binary quantization, values less than or equal to zero will be quantized to a binary zero, and positive values to a binary one, resulting in the following binary sequence: 0, 1, 0, 0, 1, 1, 0, 1. These eight bits are then packed into a single 8-bit integer, 01001101 (with the leftmost bit as the most significant bit).
    >
    > * `ubinary`: The binary sequence is directly converted and represented as the unsigned integer (`uint8`) 77.
    > * `binary`: The binary sequence is represented as the signed integer (`int8`) -51, calculated using the offset binary method (77 - 128 = -51).

    For the models that support each data type, see [Create text embeddings](https://www.mongodb.com/docs/api/doc/atlas-embedding-and-reranking-api/operation/operation-createembedding) in the Atlas Embedding and Reranking API documentation.
  </Accordion>

  <Accordion title="How can I truncate Matryoshka embeddings?">
    Matryoshka learning creates embeddings with coarse-to-fine representations within a single vector. Voyage AI models that support multiple output dimensions, such as `voyage-code-4`, generate such Matryoshka embeddings. To get shorter vectors from the API, pass `output_dimension` (for example, `output_dimension=256`). To shorten vectors you already stored, truncate them by keeping the leading subset of dimensions, then normalize them again. For example, the following Python code demonstrates how to truncate 1024-dimensional vectors to 256 dimensions:

    ```python
    import voyageai
    import numpy as np


    def embd_normalize(v: np.ndarray) -> np.ndarray:
        """
        Normalize the rows of a 2D numpy array to unit vectors by dividing each row by its Euclidean
        norm. Raises a ValueError if any row has a norm of zero to prevent division by zero.
        """
        row_norms = np.linalg.norm(v, axis=1, keepdims=True)
        if np.any(row_norms == 0):
            raise ValueError("Cannot normalize rows with a norm of zero.")
        return v / row_norms


    vo = voyageai.Client()

    # Generate voyage-code-4 vectors, which by default are 1024-dimensional floating-point numbers
    embd = vo.embed(["Sample text 1", "Sample text 2"], model="voyage-code-4").embeddings

    # Set shorter dimension
    short_dim = 256

    # Resize and normalize vectors to shorter dimension
    resized_embd = embd_normalize(np.array(embd)[:, :short_dim]).tolist()
    ```
  </Accordion>
</AccordionGroup>

## Pricing

For the most up-to-date pricing details, see [Model pricing](https://www.mongodb.com/docs/voyageai/management/billing/#model-pricing) in the MongoDB documentation.
