from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model1 = ChatOpenAI(model = "gpt-4o")
model2 = ChatOpenAI(model = "gpt-4o")

prompt1 = PromptTemplate(
    template="Generate short and simple notes on the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single doucumnet \n notes -> {notes} and quiz-> {quiz}",
    input_variables=[ "notes" , "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes" : prompt1 | model1 | parser , 
    "quiz" : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Machine learning is a branch of artificial intelligence that enables computers to learn from data without being explicitly programmed. It focuses on building algorithms that can identify patterns and make predictions or decisions. There are three main types: supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled data to train models, while unsupervised learning finds hidden structures in unlabeled data. Reinforcement learning involves agents learning through rewards and penalties. Machine learning is widely used in applications like recommendation systems, fraud detection, and image recognition. It relies heavily on large datasets and computational power. Common algorithms include decision trees, neural networks, and support vector machines. Model performance is evaluated using metrics such as accuracy, precision, and recall. As data continues to grow, machine learning plays an increasingly important role in modern technology.
"""

result = chain.invoke({"text" : text })

# print(result)

chain.get_graph().print_ascii()