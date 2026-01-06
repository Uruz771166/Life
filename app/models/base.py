from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String
import uuid


class Base(DeclarativeBase):
    """Base class for all models."""
    pass


def generate_uuid() -> str:
    """Generate a UUID string for use as primary key."""
    return str(uuid.uuid4())
