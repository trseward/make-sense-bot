from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Check if the required environment variables are set
if not all(var in os.environ for var in ["OPENAI_API_KEY", "RAG_API_KEY"]):
    raise ValueError("Missing required environment variables: OPENAI_API_KEY, RAG_API_KEY")

# Import LangChain and OpenAI
# from langchain import OpenAI
# from langchain.chains import RetrievalQA
# from langchain.vectorstores import Chroma
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.chains import RetrievalQA
# from langchain.memory import ConversationBufferMemory
# from langchain.agents import initialize_agent, Tool
# from langchain.agents import AgentType
# from langchain.agents import create_openai_functions_agent
# from langchain.prompts import MessagesPlaceholder
# from langchain.prompts import ChatPromptTemplate
# from langchain.prompts import HumanMessagePromptTemplate
# from langchain.prompts import SystemMessagePromptTemplate

class SummarizeRequest(BaseModel):
    context: str  # Age group
    explain: str  # Text to summarize

class SummarizeResponse(BaseModel):
    summary: str

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):
    if not req.context:
        raise HTTPException(status_code=400, detail="Age group (context) is required.")
    if not req.explain:
        raise HTTPException(status_code=400, detail="Prompt (explain) is required.")
    # TODO: Integrate LangChain, OpenAI, and RAG here
    # For now, return a placeholder summary
    summary = f"[MOCK] Summary for '{req.explain}' (Age group: {req.context})"
    return SummarizeResponse(summary=summary)
