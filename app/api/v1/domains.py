from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models.domain import Domain
from app.schemas.domain import DomainResponse, DomainTree

router = APIRouter(prefix="/domains", tags=["domains"])


def build_domain_tree(domain: Domain) -> DomainTree:
    """Recursively build a domain tree from a domain and its children."""
    return DomainTree(
        id=domain.id,
        code=domain.code,
        name=domain.name,
        description=domain.description,
        level=domain.level,
        ordinal=domain.ordinal,
        metadata_=domain.metadata_,
        is_active=domain.is_active,
        parent_id=domain.parent_id,
        children=[build_domain_tree(child) for child in sorted(domain.children, key=lambda x: x.ordinal)]
    )


@router.get("", response_model=list[DomainResponse])
def list_domains(
    level: int | None = None,
    db: Session = Depends(get_db)
):
    """
    List all domains.

    Optionally filter by level (0 = top-level domains).
    """
    query = select(Domain).where(Domain.is_active == True)
    if level is not None:
        query = query.where(Domain.level == level)
    query = query.order_by(Domain.level, Domain.ordinal)

    result = db.execute(query)
    return result.scalars().all()


@router.get("/tree", response_model=list[DomainTree])
def get_domain_tree(db: Session = Depends(get_db)):
    """
    Get the full domain hierarchy as a tree structure.

    Returns top-level domains with nested children.
    """
    query = select(Domain).where(
        Domain.is_active == True,
        Domain.parent_id == None
    ).order_by(Domain.ordinal)

    result = db.execute(query)
    top_level = result.scalars().all()

    return [build_domain_tree(domain) for domain in top_level]


@router.get("/{code}", response_model=DomainResponse)
def get_domain(code: str, db: Session = Depends(get_db)):
    """Get a specific domain by its code."""
    query = select(Domain).where(Domain.code == code.upper())
    result = db.execute(query)
    domain = result.scalar_one_or_none()

    if not domain:
        raise HTTPException(status_code=404, detail=f"Domain '{code}' not found")

    return domain


@router.get("/{code}/children", response_model=list[DomainResponse])
def get_domain_children(code: str, db: Session = Depends(get_db)):
    """Get all direct children of a domain."""
    # First find the parent domain
    parent_query = select(Domain).where(Domain.code == code.upper())
    parent = db.execute(parent_query).scalar_one_or_none()

    if not parent:
        raise HTTPException(status_code=404, detail=f"Domain '{code}' not found")

    # Get children
    children_query = select(Domain).where(
        Domain.parent_id == parent.id,
        Domain.is_active == True
    ).order_by(Domain.ordinal)

    result = db.execute(children_query)
    return result.scalars().all()
