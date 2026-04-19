from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4o")

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment : Literal["positive","negative"] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(

    template="Classify the sentimnet of the following text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

classifier_chain = prompt | model | parser2

review = "The phone delivers worst performance with a poor design and rough user experience."

prompt2 = PromptTemplate(
    template="Create an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Create an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

branch_chian = RunnableBranch(
    ( lambda x: x.sentiment == "positive", prompt2 | model | parser),
    ( lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chian

result = chain.invoke({ "feedback" : review})

print(result)