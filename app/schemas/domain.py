from pydantic import BaseModel
from typing import Optional


class DomainBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    level: int = 0
    ordinal: int = 0
    metadata_: Optional[dict] = None
    is_active: bool = True


class DomainCreate(DomainBase):
    parent_id: Optional[str] = None


class DomainResponse(DomainBase):
    id: str
    parent_id: Optional[str] = None

    class Config:
        from_attributes = True


class DomainTree(DomainResponse):
    """Domain with nested children for tree representation."""
    children: list["DomainTree"] = []

    class Config:
        from_attributes = True


# Required for self-referential model
DomainTree.model_rebuild()
