from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

# Run a prompt
result = llm.invoke("Write a very short story!")  # correct method in new API

print(result)