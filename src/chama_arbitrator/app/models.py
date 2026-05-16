from pydantic import BaseModel
from typing import List, Optional

class DisputeRequest(BaseModel):
    query: str
    member_id: str
    chama_id: str
    context_files: Optional[List[str]] = None

class ArbitrationResponse(BaseModel):
    ruling: str
    references: List[str]
    confidence_score: float
    financial_breakdown: Optional[dict] = None
