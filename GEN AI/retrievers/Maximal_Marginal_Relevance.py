from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS



# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding_model = OpenAIEmbeddings()

vector_score = FAISS.from_documents(
    documents=docs,
    embedding= embedding_model 
)

retriever = vector_score.as_retriever(
    search_type = "mmr",
    search_kwargs = { "k" : 2 , "lambda_mult" : 0.5} #lambda_mult controls the balance between: Relevance (similarity to query) and Diversity (different results)
)

# about lambda_mult if 1.0--> Only relevance (like normal similarity search) , if 0.5 --> Balance (recommended) and if 0.0 -->Only diversity

query = "What is Langchain"

result = retriever.invoke(query)

for i ,doc in enumerate(result):
    print(f"\n--Result{i+1}--")
    print(doc.page_content)