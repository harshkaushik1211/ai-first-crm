from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Interaction

router = APIRouter()

@router.post("/log")
def log_interaction(data: dict):
    db = SessionLocal()
    interaction = Interaction(
        hcp_name=data["hcp_name"],
        summary=data["summary"],
        sentiment=data["sentiment"],
        raw_text=data["raw_text"]
    )
    db.add(interaction)
    db.commit()
    return {"status": "saved"}
