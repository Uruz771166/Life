from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine
from app.models.base import Base
from app.api.v1.router import router as api_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="A system for mapping life domains with developmental framework lenses",
    version="0.1.0",
)

# CORS middleware for future React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "docs": "/docs",
        "endpoints": {
            "domains": "/api/v1/domains",
            "frameworks": "/api/v1/frameworks",
        }
    }


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "healthy"}
