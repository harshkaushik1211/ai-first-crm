from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class HCP(Base):
    __tablename__ = "hcps"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String, index=True)
    summary = Column(Text)
    sentiment = Column(String)
    follow_up = Column(String)
    raw_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
