from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader("/Users/prathamsharma/Desktop/ELECTRICL SOP ZAFAR SIR/ThesisReportZafarSir.pdf")

docs = loader.load()

print(len(docs)) # length of the documnet is the number of pages in that pdf


print("------PAGE CONTENT------")
print(docs[0].page_content)


print("------META DATA------")
print(docs[0].metadata)