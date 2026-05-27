from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict , Literal
import math

class QuadState(TypedDict):
    a :int 
    b : int
    c : int  
    equation : str
    discriminant : float
    result : str

def show_equation( state : QuadState ) -> QuadState:
    equation = f'{ state["a"] }x² + { state["b"] }x + { state["c"]} '

    state["equation"] = equation

    return { "equation" : equation }

def calculate_discriminant( state : QuadState) -> QuadState:
    discriminant =  ( (state["b"]**2) ) - ( 4 * state["a"] * state["c"] )

    state["discriminant"] = discriminant

    return { "discriminant" : discriminant}

def real_roots( state :QuadState ) -> QuadState:
    root1 = ( - state["b"] + math.sqrt(  state["discriminant"] ) )  / ( 2 * state["a"] )
    root2 = ( - state["b"] - math.sqrt(  state["discriminant"] ) )  / ( 2 * state["a"] )

    result = f" The roots  are {root1} , {root2} "

    return { "result" : result}


def repeated_roots( state :QuadState ) -> QuadState:
    root =  - state["b"] / ( 2 * state["a"] )

    result = f" The only repeating root is {root} "

    return { "result" : result}


def no_real_roots( state :QuadState ) -> QuadState:

    result = f" There are no real roots "

    return { "result" : result}


def check_condition( state : QuadState ) -> Literal[ "real_roots" , "repeated_roots" , "no_real_roots" ] :

    if state["discriminant"] > 0:
        return "real_roots"
    
    if state["discriminant"] == 0:
        return "repeated_roots"
    
    if state["discriminant"] < 0:
        return "no_real_roots"



# make graph

graph = StateGraph(QuadState)

# add nodes 
graph.add_node( "show_equation" , show_equation )
graph.add_node( "calculate_discriminant" , calculate_discriminant)
graph.add_node( "real_roots" , real_roots )
graph.add_node( "repeated_roots" , repeated_roots )
graph.add_node( "no_real_roots" , no_real_roots )


# add edges
graph.add_edge( START , "show_equation")
graph.add_edge( "show_equation" , "calculate_discriminant")

graph.add_conditional_edges("calculate_discriminant" , check_condition)

graph.add_edge("real_roots" , END)
graph.add_edge("repeated_roots" , END)
graph.add_edge("no_real_roots" , END)

# compile the graph 

workflow = graph.compile()


# execute the graph 

initial_state = {
    "a" : 4 , 
    "b" : 12 ,
    "c" : 9
}

final_state = workflow.invoke(initial_state)
print(final_state)