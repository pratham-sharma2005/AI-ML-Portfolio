from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage,ChatMessage , HumanMessage , SystemMessage ,BaseMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from typing import TypedDict , Literal , Annotated
from pydantic import BaseModel , Field

from langgraph.prebuilt import tools_condition , ToolNode
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

import requests 
import random

load_dotenv()

llm = ChatOpenAI()

# TOOLS 

search_tool = DuckDuckGoSearchRun( region = "us-en" )

@tool
def calculator( first_num : float , second_num: float , operation : str )->dict:
    """
    perform a basic arithematic calculation on the two numbers .
    supported operation : add , sub, mul , div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num + 1000000000
        elif operation == "div":
            if second_num == 0:
                return {"error" : "division by zero is not allowed"}
            result = first_num / second_num
        else:
            return { "error" : f" Unsupported operation '{operation}' "}
        
        return { "first_num" : first_num , "second_num" : second_num , "operation" : operation , "result" : result}
    except Exception as e:
        return { "error" : str(e)}
    

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=C9PE94QUEW9VWGFM"
    r = requests.get(url)
    return r.json()


# Make a tool list:

tool = [get_stock_price , search_tool , calculator ]



# make the llm tool-aware 

llm_with_tools = llm.bind_tools(tool)


tool_node = ToolNode(tool)

# State
class ChatState(TypedDict):
    messages : Annotated [ list[BaseMessage] , add_messages]


def chat_node(state : ChatState) ->ChatState:
    """ LLM node that may answer or request a tool call"""

    message = state["messages"]
    response = llm_with_tools.invoke(message)
    return { "messages" : [response]}



# graph structure
graph = StateGraph(ChatState)


# graph nodes
graph.add_node("chat_node" , chat_node)

graph.add_node("tools" , tool_node)

graph.add_edge(START, "chat_node")

graph.add_conditional_edges("chat_node" , tools_condition)

graph.add_edge("tools", "chat_node")


chatbot = graph.compile()

# # regular chat:
# initial_state = { "messages" : [HumanMessage(content= "Hello")]}

# out = chatbot.invoke( initial_state )

# print(out["messages"][-1].content)



# chat requiring tool

initial_state = { "messages" : [HumanMessage(content= " What is 4532 * 928? ")]}

out = chatbot.invoke( initial_state )

print(out["messages"][-1].content)