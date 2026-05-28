from langgraph.graph import StateGraph,START, END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict,Literal
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()


model = ChatOpenAI( model = "gpt-4o")

class SentimentSchema(BaseModel):
    sentiment : Literal [ "positive" , "negative" ] = Field( description="Sentiment of the review")


model_structured = model.with_structured_output(SentimentSchema)


class review_State(TypedDict):

    review : str
    sentimnet : Literal [ "positive" , "negative"]
    diagnosis : dict
    response : str


def find_sentiment(state : review_State ) -> review_State:
    prompt = f'What is the sentimnet of the following review : { state["review"] } '
    sentimnet = model_structured.invoke(prompt).sentiment # only extracts the setimnet and if u dont use .sentimnet it will return the full output as SentimentSchema(sentiment='negative')

    state["sentimnet"] = sentimnet

    return { "sentimnet" : sentimnet}


# make a graph 
graph = StateGraph(review_State)

# add nodes
graph.add_node( "find_sentiment" , find_sentiment)

# add edges 
graph.add_edge( START , "find_sentiment")
graph.add_edge( "find_sentiment" , END)


# compile the graph 
workflow = graph.compile()


# execute the graph
initial_state = {
    "review" : """The Apple iPhone is often considered overpriced compared to other smartphones with similar features.
Its battery charging speed is slower than many competing flagship devices.
The lack of major customization options in iOS can feel restrictive for some users.
Additionally, accessories and repairs for iPhones tend to be expensive.
"""
}

final_state = workflow.invoke(initial_state)

print(final_state)