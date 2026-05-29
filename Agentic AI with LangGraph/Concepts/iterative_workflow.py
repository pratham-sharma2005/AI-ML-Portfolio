from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict , Literal , Annotated
from pydantic import Field,BaseModel
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

generator_llm = ChatOpenAI( model = "gpt-4o")

evaluator_llm = ChatOpenAI( model = "gpt-4o-mini")

optimizer_llm = ChatOpenAI( model = "gpt-4o")

# state define

class Tweer_state(TypedDict):
    topic : str
    generated_tweet : str
    evaluation : Literal[ "approved" , "need_improvement"]
    iteration : int 
    max_iteration : int


# make a graph

graph = StateGraph(Tweer_state)

def generate_tweet(state : Tweer_state ) ->Tweer_state:

    #prompt
    messages = [
        SystemMessage(content="You are a funny and clever Twitter/X influencer."),
        HumanMessage(content=f"""
        Write a short, original, and hilarious tweet on the topic: "{state['topic']}".

        Rules:
        - Do NOT use question-answer format.
        - Max 280 characters.
        - Use observational humor, irony, sarcasm, or cultural references.
        - Think in meme logic, punchlines, or relatable takes.
        - Use simple, day to day english
        """)
    ]

    #generator llm
    response = generator_llm.invoke(messages).content

    #return response
    return { "generated_tweet" : response}


def evaluate_tweet(state : Tweer_state) -> Tweer_state:
    
    #prompt 

    messages = [
    SystemMessage(content="You are a ruthless, no-laugh-given Twitter critic. You evaluate tweets based on humor, originality, virality, and tweet format."),
    HumanMessage(content=f"""
    Evaluate the following tweet:
    
    Tweet: "{state['tweet']}"
    
    Use the criteria below to evaluate the tweet:
    
    1. Originality  Is this fresh, or have you seen it a hundred times before?  
    2. Humor  Did it genuinely make you smile, laugh, or chuckle?  
    3. Punchiness  Is it short, sharp, and scroll-stopping?  
    4. Virality Potential  Would people retweet or share it?  
    5. Format  Is it a well-formed tweet (not a setup-punchline joke, not a Q&A joke, and under 280 characters)?
    
    Auto-reject if:
    - It's written in question-answer format (e.g., "Why did..." or "What happens when...")
    - It exceeds 280 characters
    - It reads like a traditional setup-punchline joke
    - Dont end with generic, throwaway, or deflating lines that weaken the humor (e.g., “Masterpieces of the auntie-uncle universe” or vague summaries)
    
    ### Respond ONLY in structured format:
    - evaluation: "approved" or "needs_improvement"  
    - feedback: One paragraph explaining the strengths and weaknesses 
    """)
   ]
    
    #


# add nodes
graph.add_node( "generate" , generate_tweet)
graph.add_node( "evaluate" , evaluate_tweet)
graph.add_node( "optimize" , optimize_tweet)


# add edges


# compile the graph


# execute the graph


