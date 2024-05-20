from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import ollama
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPEN_API_KEY")


app = FastAPI(
    title="Langchain server",
    version= "1.0",
    description="A simple API server"

)


add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()

# ollama llama2

llm = ollama.Ollama(model="llama2")

Prompt1= ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words.")
Prompt2= ChatPromptTemplate.from_template("write me an poem about {topic} with 100 words.")

add_routes(
    app,
    Prompt1|model,
    path="/essay"
)

add_routes(
    app,
    Prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="locaihost",port=8000)


