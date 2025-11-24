### Rag (Retrieval-Augmented Generation)

- **RAG** is a technique that combines retrieval-based and generation-based approaches to improve the quality of generated responses
- It involves retrieving relevant documents or information from a large corpus and using that information to inform the generation process
  ![alt text](Rag.png)

- RAG models typically consist of phases:

```mermaid

 flowchart TD
  %% Phase 1: Indexing/Ingestion/Data Preparation/Extraction
  subgraph IndexingPhase["Indexing Phase"]
    classDef indexGroup fill:#26619C,stroke:#1E5631,stroke-width:2px,color:#fff;
    RawData["📄 Raw Data"]:::rawData
    Chunking["🔗 Chunking"]:::chunk
    Embedding["💠 Embedding"]:::embedding
    VectorDB["🗄️ Vector DB"]:::vectorDB
    RawData -->|Prepare| Chunking
    Chunking -->|Split & Vectorize| Embedding
    Embedding -->|Store Embeddings| VectorDB
  end

  %% Phase 2: Retrieval
  subgraph RetrievalPhase["Retrieval Phase"]
    classDef retrievalGroup fill:#33658A,stroke:#2F4858,stroke-width:2px,color:#fff;
    UserQuery["💬 User Query"]:::userQuery
    QueryEmbedding["💠 Query Embedding"]:::queryEmbedding
    SimilaritySearch["🔍 Similarity Search"]:::similarity
    Reranking["⏫ Reranking (optional)"]:::reranking
    RetrievedChunks["📦 Retrieved Chunks"]:::retrieved
    UserQuery -->|Vectorize Query| QueryEmbedding
    QueryEmbedding --> SimilaritySearch
    SimilaritySearch -->|Rerank| Reranking
    Reranking --> RetrievedChunks
    SimilaritySearch --> RetrievedChunks
    VectorDB -->|Provide Indexed Vectors| SimilaritySearch
  end

  %% Phase 3: Generation
  subgraph GenerationPhase["Generation Phase"]
    classDef genGroup fill:#4527A0,stroke:#38761D,stroke-width:2px,color:#fff;
    MergeContext["🔗 Merge Context"]:::mergeContext
    LLM["💡 LLM Inference"]:::llm
    PostProcessing["🛠️ Post-processing"]:::postProc
    FinalResponse["🚀 Final Response"]:::finalResp
    RetrievedChunks --> MergeContext
    UserQuery --> MergeContext
    MergeContext --> LLM
    LLM --> PostProcessing
    PostProcessing --> FinalResponse
    FinalResponse --> UserQuery
  end

  %% Node styles for color contrast
  class RawData indexGroup,rawData;
  class Chunking indexGroup,chunk;
  class Embedding indexGroup,embedding;
  class VectorDB indexGroup,vectorDB;
  class UserQuery retrievalGroup,userQuery;
  class QueryEmbedding retrievalGroup,queryEmbedding;
  class SimilaritySearch retrievalGroup,similarity;
  class Reranking retrievalGroup,reranking;
  class RetrievedChunks retrievalGroup,retrieved;
  class MergeContext genGroup,mergeContext;
  class LLM genGroup,llm;
  class PostProcessing genGroup,postProc;
  class FinalResponse genGroup,finalResp;

  %% Additional custom node styles
  classDef rawData fill:#1E5631,stroke:#26619C,color:#fff;
  classDef chunk fill:#915C83,stroke:#26619C,color:#fff;
  classDef embedding fill:#C34A36,stroke:#26619C,color:#fff;
  classDef vectorDB fill:#C8963E,stroke:#26619C,color:#fff;

  classDef userQuery fill:#2F4858,stroke:#33658A,color:#fff;
  classDef queryEmbedding fill:#6C3483,stroke:#33658A,color:#fff;
  classDef similarity fill:#C72C41,stroke:#33658A,color:#fff;
  classDef reranking fill:#24527A,stroke:#33658A,color:#fff;
  classDef retrieved fill:#B95F21,stroke:#33658A,color:#fff;

  classDef mergeContext fill:#1481BA,stroke:#4527A0,color:#fff;
  classDef llm fill:#0B3C5D,stroke:#4527A0,color:#fff;
  classDef postProc fill:#38761D,stroke:#4527A0,color:#fff;
  classDef finalResp fill:#8E24AA,stroke:#4527A0,color:#fff;
```

- **Phases Explained**:

  1.  **Indexing/Ingestion/Data Preparation/Extraction**: Prepare raw data (documents, PDFs, texts, etc.) for efficient search and retrieval.
      ![alt text](Indexing_phase.png)
      ![alt text](Indexing_phase_1.png)

      - **Chunking**: Split documents into smaller, manageable pieces (chunks) to facilitate retrieval.
      - **Embedding**: Convert chunks into vector representations using embedding models.
      - **Indexing**: Store the vector representations in a vector database for efficient similarity search.

2.  **Retrieval**: Fetch relevant context from the knowledge base in response to a user query.

    - **Query Embedding**: Convert the user query into a vector representation.
    - **Similarity Search**: Use the query vector to find the most relevant chunks in the vector database.
    - **Reranking**: Optionally rerank the retrieved chunks based on relevance to the query.

3.  **Generation**: Augment the original query with retrieved context to generate an accurate and relevant response.

    - **Merge Context**: Combine the retrieved chunks with the original query.
    - **LLM Inference**: Use a large language model to generate a response based on the augmented input.
    - **Post-processing**: Refine the generated response for clarity and coherence.

    ![alt text](retreval_phase.png)
    | Phase      | Purpose                           | Main Steps                                 |
    | ---------- | --------------------------------- | ------------------------------------------ |
    | Ingestion  | Prepare data for retrieval        | Chunking, embedding, indexing              |
    | Retrieval  | Find relevant context for a query | Query embedding, similarity search, rerank |
    | Generation | Create final response             | Merge context, LLM inference, post-process |

**Summary:**
Ingest -> chunk -> embed-> store -> query -> retrieve -> rerank -> generate

to build this pipeline we can use libraries like Langchain, Haystack, etc.
and without using the library
