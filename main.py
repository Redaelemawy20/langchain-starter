from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse

load_dotenv()

# define arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("--task", default="write a very short story!")

llm = OpenAI()
# args = parser.parse_args();
# Run a prompt
question_template = PromptTemplate(input_variables=["word", "language"],
                                    template="give the translation of this word: {word} in {language} language")
question_chain = LLMChain(llm=llm, prompt= question_template )
result = question_chain({
    "language": "English",
    "word": "حمار"
}) # correct method in new API

print(result)