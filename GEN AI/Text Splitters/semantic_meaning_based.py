from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings() , breakpoint_threshold_type = "standard_deviation",
    breakpoint_threshold_amount= 1
)

# sample = """
# Machine Learning is a branch of artificial intelligence that focuses on building systems that learn from data. It includes supervised learning, unsupervised learning, and reinforcement learning. Algorithms like decision trees, neural networks, and support vector machines are widely used in applications such as recommendation systems, fraud detection, and image recognition. In the field of healthcare, technology is transforming patient care. Electronic health records, telemedicine, and AI-based diagnostics are improving efficiency and accuracy. Machine learning models are used to predict diseases, assist in medical imaging, and personalize treatment plans for patients.

# Cricket is one of the most popular sports in the world, especially in countries like India, Australia, and England. The game is played between two teams of eleven players, and it includes formats like Test matches, One Day Internationals, and T20. Famous players have contributed to the global popularity of the sport. In finance, data analytics and algorithms play a crucial role in decision-making. Stock market prediction, risk management, and fraud detection rely heavily on statistical models and machine learning. Financial institutions use big data to understand customer behavior and optimize investments.
# """


sample = """
Quantum physics explores subatomic particles, wave functions, and uncertainty principles governing matter and energy. Suddenly, recipes for baking chocolate cake involve flour, sugar, eggs, and oven temperatures to create desserts. Meanwhile, football matches involve players scoring goals, referees enforcing rules, and fans cheering in stadiums worldwide. In contrast, stock trading includes analyzing market trends, managing financial risk, and optimizing investment portfolios for profit."""


docs = text_splitter.split_text(sample)

print(len(docs))

print(docs)