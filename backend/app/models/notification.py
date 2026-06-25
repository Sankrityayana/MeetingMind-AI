from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.models.base import Base


class NotificationType(str, enum.Enum):
    PROCESSING_COMPLETE = "processing_complete"
    ACTION_ITEM_DUE = "action_item_due"
    ACTION_ITEM_OVERDUE = "action_item_overdue"
    MEETING_SHARED = "meeting_shared"
    MENTION = "mention"
    COMMENT = "comment"
    REMINDER = "reminder"


class NotificationPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    notification_type = Column(Enum(NotificationType), nullable=False)
    priority = Column(Enum(NotificationPriority), default=NotificationPriority.MEDIUM)
    is_read = Column(Boolean, default=False)
    related_entity_type = Column(String, nullable=True)  # e.g., "meeting", "action_item"
    related_entity_id = Column(Integer, nullable=True)
    action_url = Column(String, nullable=True)  # URL to navigate to when clicked
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    read_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="notifications")