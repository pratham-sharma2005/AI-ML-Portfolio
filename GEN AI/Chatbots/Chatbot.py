from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

while True:
    user_input = input("You:")
    if user_input == "exit":
        break
    else:
        result = model.invoke(user_input)
        print("AI:",result.content)