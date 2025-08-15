from langchain_openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

# define arguments
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="write a very short story!")

llm = OpenAI()
args = parser.parse_args();
# Run a prompt
result = llm.invoke(args.task)  # correct method in new API

print(result)