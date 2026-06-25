from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base


class Embedding(Base):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    transcript_id = Column(Integer, ForeignKey("transcripts.id"), nullable=False)
    segment_id = Column(Integer, ForeignKey("transcript_segments.id"), nullable=True)
    content = Column(Text, nullable=False)  # The text that was embedded
    embedding_vector = Column(LargeBinary, nullable=False)  # Store as binary (pickled numpy array or similar)
    model_name = Column(String, nullable=False)  # Which embedding model was used
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    transcript = relationship("Transcript")
    segment = relationship("TranscriptSegment")