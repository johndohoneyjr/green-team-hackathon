import streamlit as st
import numpy as np
import sys
from pathlib import Path
import openai
import tiktoken
import os
from dotenv import load_dotenv 

from langchain.llms import AzureOpenAI
from langchain.document_loaders import TextLoader
from langchain import PromptTemplate, LLMChain
from langchain.chains import LLMChain

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# Configure OpenAI API
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_key = os.environ['OPENAI_API_KEY']

# deployment_name = os.environ["COMPLETIONS_MODEL"]
# model_name = os.environ["CHATGPT_MODEL"]
# DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")

llm_initialized=False

def run_llm(study):
      llm = AzureOpenAI(
          deployment_name="text-davinci-003",
          model_name="text-davinci-003",
          max_tokens=500)
        
      prompt_template = """
        Write a Plain Language Summary of the medical study below in 250 words or less
        {study_text}
        """
      val = len(study)
      chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))
      study_txt = study
      summary = chain.run(study_txt)
      return summary

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

study_txt = ''' It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)'''

st.title('Built by the :green[Green Team] :sunglasses:')

with  st.container():
    st.image("https://th.bing.com/th/id/OIP.a5TUACcDKmTaktRytiaFgQHaD4?w=340&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7", width=750, caption='SDP West CSAs')

    prompt = st.chat_input("Say something")
    if prompt:
      results = run_llm(prompt)
      st.text_area('Summary', value=results, height=200)
      st.write("Summary Length: ", len(results.split()))

with st.sidebar:
    st.subheader(":green[Services]")
    st.write("Gary Klionsky")
    st.write("John Dohoney")
    st.subheader(":green[Backend]")
    st.write("Chris Norton")
    st.write("Stephen Mann")
    st.write("Tyler Kendrick")
    st.write("Yemi Shobowale")
    st.subheader(":green[Frontend]")
    st.write("Alexandra Deany")
    st.write("Cristina Gonzalez")
