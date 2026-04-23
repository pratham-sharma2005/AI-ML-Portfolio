from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

embedding_to_use = OpenAIEmbeddings()

vector_space = Chroma.from_documents(
    documents = documents,
    embedding = embedding_to_use,
    collection_name = "my_collection"
)

retriever = vector_space.as_retriever(search_kwargs={ "k" : 2})

query = "Whats chroma"


#Method 1

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


print("\n-----------------\n")
# Method 2 

results = vector_space.similarity_search(query, k=1)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)