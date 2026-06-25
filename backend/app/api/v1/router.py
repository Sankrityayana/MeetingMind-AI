from fastapi import APIRouter

api_router = APIRouter()

# Import and include routers here as they are created
# from app.api.v1.endpoints import auth, meetings, transcripts, etc.
# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# api_router.include_router(meetings.router, prefix="/meetings", tags=["meetings"])