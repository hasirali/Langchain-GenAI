import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. .env file se keys load karein
load_dotenv()

# 2. Sahi model name use karein (Jo aapki list mein support ho raha hai)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


text = "Delhi is the capital of India"
result = embeddings.embed_query(text)

# 4. Result print karein
print(f"Vector Length: {len(result)}")
print(f"First 5 values: {result[:5]}")