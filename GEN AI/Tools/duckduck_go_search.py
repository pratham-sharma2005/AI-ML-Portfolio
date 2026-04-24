from langchain_community.tools import DuckDuckGoSearchResults

serach_tool = DuckDuckGoSearchResults() #duckduck go is a search engine like google

query = "ipl news"

result = serach_tool.invoke(query)

print(result)