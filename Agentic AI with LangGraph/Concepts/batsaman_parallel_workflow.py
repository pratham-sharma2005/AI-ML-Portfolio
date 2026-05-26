from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI( model = "gpt-4o")

class Batsman_State(TypedDict):
    runs : int
    balls : int
    fours : int
    sixes : int

    strike_rate : float
    balls_per_boundary :float 
    boundary_percent : float 
    summary : str


def calculate_strike_rate( state : Batsman_State ) -> Batsman_State:
    strike_rate = state["runs"] / state["balls"] * 100

    state["strike_rate"] = strike_rate

    return {"strike_rate":strike_rate}


def calculate_balls_per_boundary( state : Batsman_State ) -> Batsman_State:
   balls_per_boundary =  state["balls"] / ( state["fours"] + state["sixes"] )

   state["balls_per_boundary"] = balls_per_boundary

   return {"balls_per_boundary":balls_per_boundary}


def calculate_boundary_percent( state : Batsman_State ) -> Batsman_State:
   boundary_percent = ( ( ( state["fours"] * 4 ) + ( state["sixes"] * 6 ) ) / state["runs"] ) * 100

   state["boundary_percent"] = boundary_percent

   return {"boundary_percent":boundary_percent}

def summary(state : Batsman_State) -> Batsman_State:
    summary = f"""
    Strike Rate - {state['strike_rate']} \n
    Balls per boundary - {state['balls_per_boundary']} \n 
    Boundary percent - {state['boundary_percent']}
    """
    return {"summary":summary}



# make graph 
graph = StateGraph(Batsman_State)

# add nodes
graph.add_node("calculate_strike_rate" , calculate_strike_rate)
graph.add_node( "calculate_balls_per_boundary", calculate_balls_per_boundary)
graph.add_node( "calculate_boundary_percent", calculate_boundary_percent )
graph.add_node( "summary", summary )


# add edges 
graph.add_edge( START , "calculate_strike_rate" )
graph.add_edge( START , "calculate_balls_per_boundary" )
graph.add_edge( START , "calculate_boundary_percent" )
graph.add_edge( START , "calculate_strike_rate" )

graph.add_edge( "calculate_strike_rate" , "summary" )
graph.add_edge( "calculate_balls_per_boundary" , "summary" )
graph.add_edge( "calculate_boundary_percent" , "summary" )

graph.add_edge( "summary" , END )

# compile 

workflow = graph.compile()


#execute 

initial_state = {
    "runs" : 100 ,
    "balls" : 50 , 
    "fours" : 6 , 
    "sixes" : 4
}

final_state = workflow.invoke(initial_state)

print(final_state)


# in parallel worklow we cant return state as whole cause it woukd create an error thus we only pass that particular pararamter and the ouput as retun in a dictionary form and note in sequential manner we passed state in return which too is a dictionary 