import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. .env file se keys load karein
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

documents = [
    "delhi is the capital of india",
    "mumbai is the financial capital of india",
    "kolkata is the cultural capital of india",
]


result = embeddings.embed_documents(documents)

print(str(result))
# 4. Result print kareinprint


print("xtra")
print(f"Vector Length: {len(result)}")
print(f"First 5 values: {result[:5]}")