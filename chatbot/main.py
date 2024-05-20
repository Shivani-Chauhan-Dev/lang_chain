from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 
import os
from dotenv import load_dotenv 

load_dotenv() 

os.environ["OPENAI_API_KEY"]=os.getenv("OPEN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["API_KEY"]=os.getenv("API_KEY")





prompt = ChatPromptTemplate.from_messages(
    [("system","you are a helpful assistant.Please response to the user queries"),
    ("user","Question:{question}")
    ]

)

st.title("LangChain Demo with OPENAI API")
input_text= st.text_input("search the topic you want")

llm =ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
