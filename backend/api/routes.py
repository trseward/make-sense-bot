from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PromptRequest(BaseModel):
    age_group: str
    prompt: str

@router.post("/submit-prompt")
async def submit_prompt(request: PromptRequest):
    # Placeholder for summarization logic
    return {"summary": f"Summary for {request.age_group}: {request.prompt}"}

@router.get("/get-summary")
async def get_summary():
    # Placeholder for retrieving summary
    return {"summary": "This is a sample summary."}
