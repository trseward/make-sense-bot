from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
