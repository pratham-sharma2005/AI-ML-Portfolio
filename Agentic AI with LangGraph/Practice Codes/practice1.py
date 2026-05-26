from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class BMIState(TypedDict):
    weight_kg : float
    height_m : float 
    bmi : float

def bmi_function(State : BMIState ) -> BMIState:
    height = State["height_m"]
    weight = State["weight_kg"]

    bmi = weight / ( height ** 2 )

    State["bmi"] = bmi

    return State

# define graph
graph = StateGraph(BMIState)


# add nodes
graph.add_node("bmi_calculator" , bmi_function)


# add edge
graph.add_edge(START , "bmi_calculator")
graph.add_edge( "bmi_calculator" , END)


#compile 
workflow = graph.compile()

#execute
initial_state = { "weight_kg" : 80 , "height_m" : 4}

result = workflow.invoke(initial_state)
print(result)