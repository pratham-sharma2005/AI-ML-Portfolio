from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


url="https://en.wikipedia.org/wiki/Apple"
loader = WebBaseLoader(url)

docs = loader.load()


model = ChatOpenAI(model = "gpt-4o")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="answer the following question \n {question} from the following text - \n {text} ",
    input_variables=["question","text"]
)

chain = prompt | model | parser


question = "What is the scientific name of the domestic apple tree?"


result = chain.invoke({ "question" : question , "text" : docs[0].page_content})

print(result)