from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

# Define schema
class FactSchema(BaseModel):
    fact1: str = Field(description="Fact 1 about the topic\n")
    fact2: str = Field(description="Fact 2 about the topic\n")
    fact3: str = Field(description="Fact 3 about the topic\n")

# Parser
parser = PydanticOutputParser(pydantic_object=FactSchema)

# Prompt
template = PromptTemplate(
    template="Give 3 facts about {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Chain
chain = template | model | parser

# Run
result = chain.invoke({"topic": "black hole"})

print(result)