from pathlib import Path

from dotenv import dotenv_values, load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from openai.types.chat import (ChatCompletionSystemMessageParam,
                               ChatCompletionUserMessageParam)

# =================================== API SETUP ===================================
load_dotenv()
config = dotenv_values()

api_key = config["GEMINI_API_KEY"]
base_url = config['GEMINI_BASE_URL']

# model = "gemini-2.5-flash"
model = "gpt-4o"

client = OpenAI(
    # api_key=api_key,
    # base_url=base_url
)

print(f"{"="*30} API INFO {"="*40}")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
print(f"{"="*70}")
print()

# =================================================================================


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="flutter_tutorial",
    url="http://localhost:6333"
)

# Take user Input
user_query = input("Enter your question about the Flutter tutorial: ")

# ! Step 1: Similarity Search
# . query: str,
# . k: int = 4, [Number of top similar documents to retrieve]
# . filter: Filter | None = None, [Optional filtering criteria]
# . search_params: SearchParams | None = None, [Additional search parameters]
# . offset: int = 0, [Number of results to skip]
# . score_threshold: float | None = None, [Minimum score threshold for results]
# . consistency: ReadConsistency | None = None, [Consistency level for the read operation]
# . hybrid_fusion: FusionQuery | None = None, [Hybrid fusion query for combining vector and keyword search]
search_results = vector_db.similarity_search(user_query)

# Retrieving context from the search results
context = "\n\n\n".join(
    [f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])


SYSTEM_PROMPT = f"""
 You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.

 You should only ans the user based on the following context and navigate the user to open the right page number to know more.

 Context:
 {context}
"""


system_message: ChatCompletionSystemMessageParam = {
    "role": "system",
    "content": SYSTEM_PROMPT
}

user_message: ChatCompletionUserMessageParam = {
    "role": "user", "content": user_query}

response = client.chat.completions.create(
    model=model,
    messages=[
        system_message,
        user_message,
    ]
)

print(f"🤖: {response.choices[0].message.content}")
