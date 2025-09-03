from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = GoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=api_key)

text = "Generate a poem about Elon Musk taking people to Mars"

response = llm.invoke(text)

print(response)