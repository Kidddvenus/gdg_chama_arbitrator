from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="Chama Arbitrator API",
    description="Arbitration engine for cooperative society disputes",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Chama Arbitrator API is online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
