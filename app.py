from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn


# Initialize FastAPI app
app = FastAPI(
    title="LangServe Example with Ollama",
    description="An example FastAPI application using LangServe with Ollama LLM.",
    version="1.0.0",
)

# LLM setup
ollama_llm = OllamaLLM(model="deepseek-r1:latest")

# Example prompt
prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} in 30 words")

# Add routes
add_routes(app, prompt1 | ollama_llm, path="/essay")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
