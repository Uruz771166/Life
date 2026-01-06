from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import Base, generate_uuid


class Domain(Base):
    """
    MECE Life Domain model.

    Domains are organized hierarchically using path-based codes:
    - "SELF" (top-level)
    - "SELF.IDENTITY" (subdomain)
    - "SELF.IDENTITY.VALUES" (sub-subdomain)
    """
    __tablename__ = "domains"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    code = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    parent_id = Column(String(36), ForeignKey("domains.id"), nullable=True)
    level = Column(Integer, nullable=False, default=0)
    ordinal = Column(Integer, nullable=False, default=0)
    metadata_ = Column("metadata", JSON, nullable=True, default=dict)
    is_active = Column(Boolean, default=True)

    # Self-referential relationship for hierarchy
    parent = relationship("Domain", remote_side=[id], back_populates="children")
    children = relationship("Domain", back_populates="parent", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Domain(code='{self.code}', name='{self.name}')>"
