from langgraph.graph import StateGraph, END
from app.langgraph_agent.tools import (
    log_interaction,
    sentiment_tool,
    followup_tool,
    material_tool
)

def build_agent():
    graph = StateGraph(dict)

    graph.add_node("log", log_interaction)
    graph.add_node("sentiment", sentiment_tool)
    graph.add_node("followup", followup_tool)
    graph.add_node("material", material_tool)

    graph.set_entry_point("log")
    graph.add_edge("log", "sentiment")
    graph.add_edge("sentiment", "followup")
    graph.add_edge("followup", "material")
    graph.add_edge("material", END)

    return graph.compile()
