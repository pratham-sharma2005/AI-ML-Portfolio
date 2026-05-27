from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI( model = "gpt-4o" )

class Feedback(TypedDict):
    essay_text : str

    clarity_of_thoughts_score : int
    depth_of_analysis_score : int
    language_score : int

    final_evaluation_score : float
    text_feedback : str



def clarity_of_though_func( state : Feedback) -> Feedback:

    essay = state["essay_text"]

    prompt = f"Evalaute the given essay on the basis of the clarity of thughts on a score of 0 to 10 both numbers included and only give the numerical value: {essay}"

    clarity_of_thoughts_score = int(model.invoke(prompt).content.strip() )

    state["clarity_of_thoughts_score"] = clarity_of_thoughts_score

    return { "clarity_of_thoughts_score" : clarity_of_thoughts_score}



def depth_of_analysis_func( state : Feedback) -> Feedback:

    essay = state["essay_text"]

    prompt = f"Evalaute the given essay on the basis on the depth of the analysis on a score of 0 to 10 both numbers included and only give the numerical value: {essay}"

    depth_of_analysis_score = int ( model.invoke(prompt).content.strip() ) 

    state["depth_of_analysis_score"] = depth_of_analysis_score

    return { "depth_of_analysis_score" : depth_of_analysis_score}


def language_score_func( state : Feedback) -> Feedback:

    essay = state["essay_text"]

    prompt = f"Evalaute the given essay on the basis on the language of the essay on a score of 0 to 10 both numbers included and only give the numerical value: {essay}"

    language_score = int ( model.invoke(prompt).content.strip() )

    state["language_score"] = language_score

    return { "language_score" : language_score}


def final_evaluation_feedabck_func( state : Feedback) -> Feedback:

    essay = state["essay_text"]
    language_score = state["language_score"]
    depth_of_analysis_score = state["depth_of_analysis_score"]
    clarity_of_thoughts_score = state["clarity_of_thoughts_score"]

    final_evaluation_score_raw = ( language_score + depth_of_analysis_score + clarity_of_thoughts_score ) / 3 

    final_evaluation_score = round( final_evaluation_score_raw , 2 )

    state["final_evaluation_score"] = final_evaluation_score


    prompts = f" give a short feedback on the essay : {essay}"

    text_feedback = model.invoke(prompts).content

    state["text_feedback"] = text_feedback

    return {
    "final_evaluation_score": final_evaluation_score,
    "text_feedback": text_feedback
}



# make graph
graph = StateGraph(Feedback)


# add nodes 

graph.add_node( "clarity_of_thought" , clarity_of_though_func)
graph.add_node( "depth_of_analysis" , depth_of_analysis_func)
graph.add_node( "language_score" , language_score_func)

graph.add_node( "final_evaluation_feedabck" , final_evaluation_feedabck_func)


# add edges

graph.add_edge( START , "clarity_of_thought")
graph.add_edge( START , "depth_of_analysis")
graph.add_edge( START , "language_score")


graph.add_edge("clarity_of_thought" , "final_evaluation_feedabck" )
graph.add_edge("depth_of_analysis" , "final_evaluation_feedabck" )
graph.add_edge("language_score" , "final_evaluation_feedabck" )

graph.add_edge( "final_evaluation_feedabck" , END)


# compile graph 

llm_workflow = graph.compile()

# execute graph

initial_state = {
    "essay_text" : """India is a country of great diversity and culture which has many peoples, languages and traditions living together from centuries. Unity in diversity is often said to be the biggest strength of India but in todays time many challenges are also coming infront of it. Communalism, regionalism, caste discrimination and social inequalities are affecting the harmony of nation in very serious manner. If these problems are not addressed properly then it can create disturbance in national integration and development of country.

Firstly, communalism is becoming a major issue in India. Many political leaders uses religion for gaining votes and creating divisions among peoples. This not only weakens democracy but also increases hatred among communities. Social media is also spreading fake informations and rumors very rapidly which sometimes leads to riots and violence. Government should take strict actions against such activites and promote secular values among youth and society.

Secondly, caste system though legally abolished in many forms still exists in practical life. Lower caste peoples are facing discrimination in villages as well as urban areas. Even in education and employment many peoples are judged by caste identity rather than their talent and hardwork. Reservation policy has helped some sections but still complete equality is not achieved till now. Society need to change its mindset for true social justice.

Another challenge is regionalism and language conflicts. Some states gives more importance to their own regional identity and oppose other languages or migrants. This creates tensions between different parts of country and weakens national unity. India should promote multilingualism and mutual respect among all cultures because every culture contributes in development of nation.

Apart from these social issues, economic inequality is also increasing continuously. Rich peoples are becoming more richer while poor sections are struggling for basic facilities like education, healthcare and employment. Due to unemployment many youths are getting frustrated and some are moving towards crimes and anti-social activites. Government schemes are present but implementation at ground level is often very poor and corrupted.

In conclusion, unity in diversity is not just a slogan but it is essential for survival and progress of India. Citizens, government, educational institutions and media all have important role in maintaining social harmony. If India want to become a developed nation then it must overcome communalism, casteism, regionalism and inequality with collective efforts and proper policies. Only then the dream of strong and united India can be achieved successfully."""

}

final_state = llm_workflow.invoke(initial_state)

print( "Essay_text:" , final_state["essay_text"])
print("-----------------------------------------------")

print( "clarity_of_thoughts_score:" , final_state["clarity_of_thoughts_score"])
print("-----------------------------------------------")

print( "depth_of_analysis_score:" , final_state["depth_of_analysis_score"])
print("-----------------------------------------------")

print( "language_score:" , final_state["language_score"])
print("-----------------------------------------------")

print( "final_evaluation_score:" , final_state["final_evaluation_score"])
print("-----------------------------------------------")

print( "text_feedback:" , final_state["text_feedback"])
print("-----------------------------------------------")

