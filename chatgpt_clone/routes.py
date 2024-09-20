import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="GPT clone service",
    version = "1.0.0",
    description = "Simple GPT clone service"
)

# llama2 model route
model1 = Ollama(model="llama2")
prompt1 = ChatPromptTemplate(
    [
        ("system", "You're a helpful intelligent chatbot"),
        ("user", "Question:{question}")
    ]
)

add_routes(
    app,
    prompt1|model1,
    path = "/llama2"
)

# gemma2 model route
model1 = Ollama(model="gemma2:2b")
prompt1 = ChatPromptTemplate(
    [
        ("system", "You're a helpful intelligent chatbot"),
        ("user", "Question:{question}")
    ]
)
add_routes(
    app,
    prompt1|model1,
    path = "/gemma2"
)

# qwen2.5 model route
model1 = Ollama(model="qwen2.5:3b")
prompt1 = ChatPromptTemplate(
    [
        ("system", "You're a helpful intelligent chatbot"),
        ("user", "Question:{question}")
    ]
)
add_routes(
    app,
    prompt1|model1,
    path = "/qwen2.5"
)

# phi3.5 model route
model1 = Ollama(model="phi3.5")
prompt1 = ChatPromptTemplate(
    [
        ("system", "You're a helpful intelligent chatbot"),
        ("user", "Question:{question}")
    ]
)
add_routes(
    app,
    prompt1|model1,
    path = "/phi3.5"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)