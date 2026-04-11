from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import streamlit as st

load_dotenv()

model = ChatOpenAI()

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result =model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)