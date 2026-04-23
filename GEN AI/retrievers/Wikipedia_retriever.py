from dotenv import load_dotenv

load_dotenv()

from langchain_community.retrievers import WikipediaRetriever 

retriever = WikipediaRetriever( top_k_results= 2 , lang="en" ) #top_ ke results is to specify how many top results we want and lang for the language we want the result in

query = "the geopolitical history of india and pakistan from the perspective of a chinese"

docs = retriever.invoke(query) # since retriever is a runnable thus it has invoke function

print(docs)

print("\n------------------\n")


# Print retrieved content
for i, doc in enumerate(docs):  # syntax ---> enumerate(iterable, start=0)
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display