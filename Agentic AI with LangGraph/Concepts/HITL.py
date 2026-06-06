from langchain_openai import ChatOpenAI 
from langchain_core .prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage , BaseMessage
from typing import TypedDict , Literal ,Annotated
from pydantic import BaseModel , Field 


from langgraph.graph import StateGraph , START , END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt , Command
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI( model = "gpt-4o-mini")

class ChatState(TypedDict):
    messages : Annotated [ list [ BaseMessage ] , add_messages ]

def chat_node( state : ChatState ) -> ChatState :
    decision = interrupt(
        {
            "type" : "approval",
            "reason" : "model is about to answer a user question",
            "question" : state["messages"][-1].content ,
            "instruction" : "approve this question ? yes or no ?"
        }
    )

    if decision["approved"] == "no" :
        return { "messages" : [AIMessage(content="Not approved")]}
    else:
        response = llm.invoke(state["messages"])
        return { "messages" : [response]}
    

builder = StateGraph(ChatState)

builder.add_node("chat_node" , chat_node)

builder.add_edge(START , "chat_node")
builder.add_edge("chat_node" , END )


# checkpoint is required for interrupts

checkpoint = InMemorySaver()

# complie the app

app = builder.compile( checkpointer = checkpoint )



# create a new thread id for this conversation


configuration = { "configurable" : { "thread_id" : "1234"}}

# Step 1 => user ask a question 

initial_input = {
    
    "messages" : [ ( "user" , "Explain gardient descent in simlple words" ) ]
}

state1 = app.invoke(initial_input , config= configuration)


result = app.invoke(Command(resume={"approved": "yes"}), config=configuration)

print( result['messages'][-1].content )