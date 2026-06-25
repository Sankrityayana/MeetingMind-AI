from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base


class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"), nullable=False)
    recording_id = Column(Integer, ForeignKey("recordings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    language = Column(String, default="en")
    is_processed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    meeting = relationship("Meeting", back_populates="transcripts")
    recording = relationship("Recording", back_populates="transcripts")
    user = relationship("User", back_populates="transcripts")
    segments = relationship("TranscriptSegment", back_populates="transcript", cascade="all, delete-orphan")


class TranscriptSegment(Base):
    __tablename__ = "transcript_segments"

    id = Column(Integer, primary_key=True, index=True)
    transcript_id = Column(Integer, ForeignKey("transcripts.id"), nullable=False)
    speaker_id = Column(Integer, ForeignKey("speakers.id"), nullable=True)
    text = Column(Text, nullable=False)
    start_time = Column(Float, nullable=False)  # in seconds
    end_time = Column(Float, nullable=False)    # in seconds
    confidence = Column(Float, nullable=True)   # 0.0 to 1.0
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    transcript = relationship("Transcript", back_populates="segments")
    speaker = relationship("Speaker", back_populates="transcript_segments")