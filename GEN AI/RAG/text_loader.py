from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI( model = "gpt-4o" )

prompt = PromptTemplate(
    template="Write the summary on the following poem \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("/Users/prathamsharma/Desktop/LangChain Model/RAG/cricket.txt" , encoding="utf-8")

docs = loader.load()

# print(docs)

# print("Type of doumnets:",type(docs))

# print("Length of the documnet:",len(docs))

# print("Print the docs[0]:",docs[0])

# print("Print the docs[0]:",docs[0].page_content)

# print("Print the docs[0]:",docs[0].metadata)

# print("Print the type of docs[0]:",type(docs[0]))


chain = prompt | model | parser

result = chain.invoke({"poem":docs[0].page_content})

print(result)