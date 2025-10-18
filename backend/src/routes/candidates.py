from fastapi import APIRouter

router = APIRouter(prefix="/candidates", tags=["Candidates"])

@router.get("/")
async def get_candidates():
    return {"message": "List of candidates will be here"}

@router.get("/ask")
async def ask(prompt: str):
    from services.ai import ask_gemini
    return {"answer": ask_gemini(prompt)}
