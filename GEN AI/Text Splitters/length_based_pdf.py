from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("/Users/prathamsharma/Desktop/ELECTRICL SOP ZAFAR SIR/ThesisReportZafarSir.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=""
)

text_splitted = splitter.split_documents(docs)

print(text_splitted[0].page_content)