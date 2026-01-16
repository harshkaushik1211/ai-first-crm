import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def log_interaction(state: dict):
    text = state["text"]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "Return ONLY valid JSON with keys: "
                    "hcp_name, summary, sentiment, follow_up"
                )
            },
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    state["interaction"] = json.loads(response.choices[0].message.content)
    return state


def sentiment_tool(state: dict):
    """Adds sentiment analysis."""
    state["sentiment"] = "Positive"
    return state


def followup_tool(state: dict):
    """Adds follow-up recommendation."""
    state["follow_up"] = "Schedule next visit in 2 weeks"
    return state


def material_tool(state: dict):
    """Adds material recommendation."""
    state["material"] = "Product brochure suggested"
    return state
