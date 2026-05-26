from langgraph.graph import START,END, StateGraph
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI( model = "gpt-4o")
parsing = StrOutputParser()

#create state

class LLMState(TypedDict):
    question : str
    answer : str

def llm_qa_func(state:LLMState) -> LLMState:

    #extract question from the state
    question = state["question"]

    #make a prompt
    prompt = PromptTemplate(
        template="Answer the following quetion in 5 lines :{question}",
        input_variables=["question"]
    )

    #ask that queestion in the LLM

    chain = prompt | model | parsing

    answer = chain.invoke({"question" : question })

    state["answer"] = answer

    return state

# create our graph 
graph = StateGraph(LLMState)


#add nodes 
graph.add_node( "llm_qa" , llm_qa_func)

#add edges
graph.add_edge( START , "llm_qa" )
graph.add_edge( "llm_qa" , END )

#compile
workflow = graph.compile()

#execute 

initial_state = {
    "question" : " Whats badminton"
}
final_state = workflow.invoke(initial_state)
print(final_state["answer"])