from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
# ! Step 1: Loading the files
pdf_path = Path(__file__).parent / "flutter_tutorial.pdf"

# making a object of PyPDFLoader
loader = PyPDFLoader(str(pdf_path))
# loading the documents .load() returns a list of Document objects
docs = loader.load()

# to print in proper format use repr() function
# print(repr(docs[2]))
# print(docs)


# ! Step 2: Splitting the files into chunks

# making a object of RecursiveCharacterTextSplitter
# . chunk_size is the size of each chunk
# . chunk_overlap take some part of previous chunk to next chunk for better context
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200)

# splitting the documents into chunks
docs_chunks = text_splitter.split_documents(docs)
print(len(docs_chunks))


# ! Step 3: Creating Vector Embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


# ! Step 4: Creating Vector Store using Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=docs_chunks,
    embedding=embedding_model,
    collection_name="flutter_tutorial",
    url="http://localhost:6333"
)

print("Vector Store created successfully!")
