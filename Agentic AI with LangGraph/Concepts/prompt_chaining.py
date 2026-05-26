from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict

model = ChatOpenAI( model = "gpt-4o" )


# define state
class Blog_State(TypedDict):
    topic: str
    gen_outline : str
    gen_blog : str


def gen_outline(state:Blog_State) -> Blog_State:
    topic = state["topic"]
    
    prompts = f"Create a general outline on {topic}"

    gen_outline = model.invoke(prompts).content

    state["gen_outline"] = gen_outline

    return state

def gen_blog(state:Blog_State) -> Blog_State:
    topic = state["topic"]
    gen_outline = state["gen_outline"]
    
    prompts = f"Create a general blog using the general outline :{gen_outline} made on the topic: {topic}"

    gen_blog = model.invoke(prompts).content

    state["gen_blog"] = gen_blog

    return state

# make graph
graph = StateGraph(Blog_State)

# add nodes 
graph.add_node( "gen_outline" , gen_outline )
graph.add_node( "gen_blog" , gen_blog)


# add edges
graph.add_edge( START , "gen_outline" )
graph.add_edge( "gen_outline" , "gen_blog" )
graph.add_edge( "gen_blog" , END )

# compile
llm_workflow = graph.compile()

# execute 

initial_state = { "topic" : "football" }

final_state = llm_workflow.invoke(initial_state)

print(final_state["topic"])
print("------------------------------------------------")


print(final_state["gen_outline"])
print("------------------------------------------------")


print(final_state["gen_blog"])