from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl
from typing import List, Optional, Union
import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "MeetingMind AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days
    ALGORITHM: str = "HS256"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "meetingmind"
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @property
    def SQLALCHEMY_DATABASE_URI_STR(self) -> str:
        return str(self.SQLALCHEMY_DATABASE_URI)

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        if isinstance(self.SQLALCHEMY_DATABASE_URI, str):
            return self.SQLALCHEMY_DATABASE_URI
        return PostgresDsn.build(
            scheme="postgresql",
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=f"/{self.POSTGRES_DB or ''}",
        )

    # Redis (for Celery)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # Default Redis database

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # Whisper
    WHISPER_MODEL_SIZE: str = "base"  # tiny, base, small, medium, large

    # Gemini/OpenAI
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    # Email (for notifications)
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # Frontend URL for email links
    FRONTEND_HOST: str = "http://localhost:3000"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()