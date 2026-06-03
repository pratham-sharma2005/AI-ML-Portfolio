from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from typing import TypedDict,Literal,Annotated
from pydantic import Field , BaseModel
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI( model="gpt-4o")


class resume(TypedDict):
    resume : str 
    name : str 
    age : int 
    highest_degree : Literal[ "ug" , "pg"]
    domain : str 
    specifications :  list[str] 
    class_number : int 
    board_marks_percentage : float



def name( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the name of the applicant"
    response_name = llm.invoke(prompt).content
    return { "name" : response_name}



def age( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the age of the applicant"
    response_age = llm.invoke(prompt).content
    return { "age" : response_age}



def highest_degree( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f"""From this resume determine the highest degree.Return ONLY one word :ug or pg. Resume: {resume_text} """
    response_highest_degree = llm.invoke(prompt).content
    return { "highest_degree" : response_highest_degree}



def domain( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the domain of the applicant"
    response_domain = llm.invoke(prompt).content
    return { "domain" : response_domain}



def specifications( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the specifiactions or skill set of the applicant"
    response_specifiactions = llm.invoke(prompt).content
    return { "specifications" : response_specifiactions}



def class_number( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the class of the applicant"
    response_class = llm.invoke(prompt).content
    return { "class_number" : response_class}



def board_marks_percentage( state :resume ) -> resume :
    resume_text = state["resume"]
    prompt = f" from the resume : {resume_text} , give me the 12th marks of the applicant"
    response_board_marks = llm.invoke(prompt).content
    return { "board_marks_percentage" : response_board_marks}

def highest_degree_ug_pg( state : resume) -> resume:
    highest_degree = state["highest_degree"].strip().lower()
    if highest_degree == "ug":
        return "class_number"
    if highest_degree == "pg":
        return "domain"

# make the graph 
graph = StateGraph(resume)


# make the nodes
graph.add_node("name" , name )
graph.add_node("age" , age )
graph.add_node("highest_degree" , highest_degree )
graph.add_node("domain" , domain )
graph.add_node("specifications" , specifications )
graph.add_node("class_number" , class_number )
graph.add_node("board_marks_percentage" , board_marks_percentage )


# make the edges
graph.add_edge( START , "name")
graph.add_edge( "name" , "age")
graph.add_edge( "age" , "highest_degree")

graph.add_conditional_edges( "highest_degree" , highest_degree_ug_pg )
graph.add_edge( "class_number" , "board_marks_percentage")
graph.add_edge( "board_marks_percentage" , END)

graph.add_edge( "domain" , "specifications" )
graph.add_edge( "specifications" , END)


# compile the graph
workflow = graph.compile()


# execute the graph
initial_state_1 = { "resume" : """
Name: Rahul Sharma

Age: 19

Education:
Currently pursuing Bachelor of Technology (B.Tech) in Computer Science
from Thapar Institute of Engineering and Technology.

Class: 12

Board Examination:
CBSE Board

12th Percentage: 92.4%

Skills:
Python, Java, Data Structures, SQL

Projects:
- Student Management System using Java
- Personal Portfolio Website using HTML, CSS, JavaScript

Achievements:
- Secured 92.4% in CBSE Class 12 Board Examination
- Participated in Smart India Hackathon

Highest Degree: UG
"""}

initial_state_2 = { "resume" : """Name: Priya Verma

Age: 25

Education:
Master of Technology (M.Tech) in Artificial Intelligence
Indian Institute of Technology Delhi

Bachelor of Technology (B.Tech) in Computer Science
Delhi Technological University

Domain:
Artificial Intelligence and Machine Learning

Skills:
Python, TensorFlow, PyTorch, Deep Learning,
Natural Language Processing, Generative AI,
Computer Vision, Data Analysis

Projects:
1. AI-Powered Resume Screening System
   - Built a resume parser using LLMs and LangGraph.
   - Automated candidate ranking and filtering.

2. Medical Image Classification
   - Developed a CNN-based system for disease detection.
   - Achieved 94% classification accuracy.

3. Conversational AI Assistant
   - Created a chatbot using LangChain and OpenAI APIs.
   - Implemented RAG and memory management.

Research:
Published a paper on Transformer-based Text Classification
in an international conference.

Internships:
Machine Learning Intern at ABC Technologies

Achievements:
- Winner of National AI Hackathon 2025
- Google Cloud Certified Professional

Highest Degree: PG"""}


final_state = workflow.invoke(initial_state_2)

print(final_state["name"])
print(final_state["age"])
print(final_state["highest_degree"])

print(final_state["domain"])
print(final_state["specifications"])

# print(final_state["class_number"])
# print(final_state["board_marks_percentage"])
