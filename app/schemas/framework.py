from pydantic import BaseModel
from typing import Optional


class StageBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    ordinal: int
    color: Optional[str] = None
    characteristics: Optional[dict] = None


class StageResponse(StageBase):
    id: str
    framework_id: str

    class Config:
        from_attributes = True


class FrameworkBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    author: Optional[str] = None
    is_hierarchical: bool = True
    config: Optional[dict] = None
    is_active: bool = True


class FrameworkResponse(FrameworkBase):
    id: str

    class Config:
        from_attributes = True


class FrameworkWithStages(FrameworkResponse):
    """Framework with all stages included."""
    stages: list[StageResponse] = []

    class Config:
        from_attributes = True
