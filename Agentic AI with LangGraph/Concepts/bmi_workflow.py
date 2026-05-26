from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from PIL import Image
import io


#define state
class BMIState(TypedDict):
    weight_kg : float
    height_m :float
    bmi : float
    category : str

def calculate_bmi_function(State: BMIState) -> BMIState :
    weight = State["weight_kg"]
    height = State["height_m"]

    bmi = weight / (height**2)

    State["bmi"] = round( bmi , 2)

    return State

def label_bmi_func(state:BMIState)-> BMIState:

    bmi = state["bmi"]

    if bmi < 18:
        state["category"] = "underweight"
    elif 18 <= bmi <= 25:
        state["category"] =  "Fit"
    else:  
        state["category"] = "Overweight"

    return state


#define your graph
graph = StateGraph(BMIState)


# add nodes to your graph
graph.add_node( "calculate_bmi" , calculate_bmi_function)
graph.add_node("label_bmi" , label_bmi_func)

# add edges to your graph
graph.add_edge(START , "calculate_bmi")
graph.add_edge("calculate_bmi" , "label_bmi")
graph.add_edge("label_bmi" , END)


#complie the graph 
workflow = graph.compile()


#execute the graph
initial_state = {"weight_kg" : 80 , "height_m" : 2 }

final_state = workflow.invoke( initial_state )

print(final_state)

# Generate graph image
graph_png = workflow.get_graph().draw_mermaid_png()

# Open image using PIL
img = Image.open(io.BytesIO(graph_png))

# Show image
img.show()