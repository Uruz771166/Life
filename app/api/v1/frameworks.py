from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models.framework import DevelopmentalFramework, FrameworkStage
from app.schemas.framework import FrameworkResponse, FrameworkWithStages, StageResponse

router = APIRouter(prefix="/frameworks", tags=["frameworks"])


@router.get("", response_model=list[FrameworkResponse])
def list_frameworks(db: Session = Depends(get_db)):
    """List all developmental frameworks."""
    query = select(DevelopmentalFramework).where(
        DevelopmentalFramework.is_active == True
    )
    result = db.execute(query)
    return result.scalars().all()


@router.get("/{code}", response_model=FrameworkWithStages)
def get_framework(code: str, db: Session = Depends(get_db)):
    """
    Get a specific framework by its code.

    Includes all stages in the response.
    """
    query = select(DevelopmentalFramework).where(
        DevelopmentalFramework.code == code.upper()
    )
    result = db.execute(query)
    framework = result.scalar_one_or_none()

    if not framework:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")

    return framework


@router.get("/{code}/stages", response_model=list[StageResponse])
def get_framework_stages(code: str, db: Session = Depends(get_db)):
    """Get all stages for a specific framework."""
    # First find the framework
    framework_query = select(DevelopmentalFramework).where(
        DevelopmentalFramework.code == code.upper()
    )
    framework = db.execute(framework_query).scalar_one_or_none()

    if not framework:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")

    # Get stages
    stages_query = select(FrameworkStage).where(
        FrameworkStage.framework_id == framework.id
    ).order_by(FrameworkStage.ordinal)

    result = db.execute(stages_query)
    return result.scalars().all()


@router.get("/{code}/stages/{stage_code}", response_model=StageResponse)
def get_framework_stage(code: str, stage_code: str, db: Session = Depends(get_db)):
    """Get a specific stage within a framework."""
    # First find the framework
    framework_query = select(DevelopmentalFramework).where(
        DevelopmentalFramework.code == code.upper()
    )
    framework = db.execute(framework_query).scalar_one_or_none()

    if not framework:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")

    # Get the specific stage
    stage_query = select(FrameworkStage).where(
        FrameworkStage.framework_id == framework.id,
        FrameworkStage.code == stage_code.upper()
    )
    stage = db.execute(stage_query).scalar_one_or_none()

    if not stage:
        raise HTTPException(
            status_code=404,
            detail=f"Stage '{stage_code}' not found in framework '{code}'"
        )

    return stage
