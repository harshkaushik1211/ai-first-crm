from fastapi import APIRouter, Body
from app.langgraph_agent.agent import build_agent
from app.database import SessionLocal
from app.models import Interaction

router = APIRouter()
agent = build_agent()

@router.post("/chat")
def chat(payload: dict = Body(...)):
    """
    Expects: { "text": "..." }
    """
    # Run AI agent
    result = agent.invoke(payload)

    interaction_data = result["interaction"]

    # Save to DB
    db = SessionLocal()
    interaction = Interaction(
        hcp_name=interaction_data["hcp_name"],
        summary=interaction_data["summary"],
        sentiment=interaction_data["sentiment"],
        follow_up=interaction_data["follow_up"],
        raw_text=result["text"]
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "message": "Interaction saved successfully",
        "interaction_id": interaction.id,
        "result": result
    }
