from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4o-mini")  # fast + cheap

response = llm.invoke("What is the capital of India?")
print(response.content)