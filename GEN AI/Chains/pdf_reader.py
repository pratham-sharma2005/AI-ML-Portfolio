from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

load_dotenv()

# Load document
loader = TextLoader("docs.txt")
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Create embeddings + vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Create retriever
retriever = vectorstore.as_retriever()

# Query
query = "What are the key takeaways from the document?"
retrieved_docs = retriever.invoke(query)   # ✅ updated method

# Combine retrieved text
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# LLM
model = ChatOpenAI(model="gpt-4o")

response = model.invoke(f"Answer the question based on context:\n{retrieved_text}")

print(response.content)