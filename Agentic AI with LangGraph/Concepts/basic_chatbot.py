from langgraph.graph import StateGraph,START,END,add_messages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage,BaseMessage
from typing import TypedDict,Literal,Annotated
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI( model = "gpt-4o")

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages] # basemessage include all types of messages whether tool,human,ai,system
    # add_messages When new messages arrive,append them to the existing list instead of replacing it.”

graph = StateGraph(ChatState)

def chat_node( state : ChatState ) -> ChatState:

    #take user query 
    messages = state["messages"]

    #send to llm
    response = llm.invoke(messages)

    #response store state
    return { "messages" : [response]} # will return the value to the messages in the list form

graph.add_node( "chat_node", chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile()

initial_state = {
    "messages" : [HumanMessage(content="What is the capital of India")]
}

output = chatbot.invoke(initial_state)

print(output["messages"][-1].content)