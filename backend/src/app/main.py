from fastapi import FastAPI
from routes import candidates  # import router

app = FastAPI()

app.include_router(candidates.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
