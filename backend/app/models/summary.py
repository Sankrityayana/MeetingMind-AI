from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base


class SummaryType(str, enum.Enum):
    EXECUTIVE = "executive"
    SHORT = "short"
    DETAILED = "detailed"


class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    summary_type = Column(Enum(SummaryType), nullable=False)
    content = Column(Text, nullable=False)
    is_generated_by_ai = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    meeting = relationship("Meeting", back_populates="summaries")
    user = relationship("User", back_populates="summaries")