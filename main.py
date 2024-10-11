import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

response = tweet_chain.invoke({"number": 2, "topic": "Submarine"})

print(response.content)

import streamlit as st

st.header("Tweet Genarator")
st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)