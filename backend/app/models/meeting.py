from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.models.base import Base


class MeetingStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MeetingType(str, enum.Enum):
    IN_PERSON = "in_person"
    VIRTUAL = "virtual"
    HYBRID = "hybrid"


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    scheduled_start = Column(DateTime(timezone=True), nullable=True)
    scheduled_end = Column(DateTime(timezone=True), nullable=True)
    actual_start = Column(DateTime(timezone=True), nullable=True)
    actual_end = Column(DateTime(timezone=True), nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    status = Column(Enum(MeetingStatus), default=MeetingStatus.SCHEDULED)
    meeting_type = Column(Enum(MeetingType), default=MeetingType.VIRTUAL)
    meeting_url = Column(String, nullable=True)  # For virtual meetings (Zoom, Teams, etc.)
    location = Column(String, nullable=True)  # For in-person meetings
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    owner = relationship("User", back_populates="meetings")
    organization = relationship("Organization", back_populates="meetings")
    recordings = relationship("Recording", back_populates="meeting")
    transcripts = relationship("Transcript", back_populates="meeting")
    summaries = relationship("Summary", back_populates="meeting")
    action_items = relationship("ActionItem", back_populates="meeting")
    decisions = relationship("Decision", back_populates="meeting")
    attendees = relationship("MeetingAttendee", back_populates="meeting")


class MeetingAttendee(Base):
    __tablename__ = "meeting_attendees"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String, default="attendee")  # organizer, presenter, attendee
    joined_at = Column(DateTime(timezone=True), nullable=True)
    left_at = Column(DateTime(timezone=True), nullable=True)
    is_present = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    meeting = relationship("Meeting", back_populates="attendees")
    user = relationship("User")