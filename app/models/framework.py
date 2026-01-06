from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from app.models.base import Base, generate_uuid


class DevelopmentalFramework(Base):
    """
    Developmental psychology framework model.

    Frameworks provide interpretive lenses that can be applied to any domain.
    Examples: Spiral Dynamics, Maslow's Hierarchy, Kegan's Adult Development
    """
    __tablename__ = "developmental_frameworks"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    code = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    author = Column(String(255), nullable=True)
    is_hierarchical = Column(Boolean, default=True)
    config = Column(JSON, nullable=True, default=dict)
    is_active = Column(Boolean, default=True)

    # Relationship to stages
    stages = relationship(
        "FrameworkStage",
        back_populates="framework",
        cascade="all, delete-orphan",
        order_by="FrameworkStage.ordinal"
    )

    def __repr__(self) -> str:
        return f"<DevelopmentalFramework(code='{self.code}', name='{self.name}')>"


class FrameworkStage(Base):
    """
    Individual stage within a developmental framework.

    Each stage contains rich metadata about values, worldview, behaviors, etc.
    """
    __tablename__ = "framework_stages"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    framework_id = Column(String(36), ForeignKey("developmental_frameworks.id"), nullable=False)
    code = Column(String(50), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    ordinal = Column(Integer, nullable=False)
    color = Column(String(7), nullable=True)  # Hex color code
    characteristics = Column(JSON, nullable=True, default=dict)

    # Relationship to framework
    framework = relationship("DevelopmentalFramework", back_populates="stages")

    def __repr__(self) -> str:
        return f"<FrameworkStage(code='{self.code}', name='{self.name}')>"
