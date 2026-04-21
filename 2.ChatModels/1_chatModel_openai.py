from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

result = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_completion_tokens=10)
result.invoke("What is the Capital of India")
print(result.content)