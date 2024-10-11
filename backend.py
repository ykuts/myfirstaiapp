from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()  # Load variables from .env

api_key = os.getenv('API_KEY')

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

tweet_chain = tweet_prompt | gemini_model

response = tweet_chain.invoke({"number": 2, "topic": "Submarine"})

print(response.content)