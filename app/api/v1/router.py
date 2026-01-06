from fastapi import APIRouter

from app.api.v1.domains import router as domains_router
from app.api.v1.frameworks import router as frameworks_router

router = APIRouter(prefix="/api/v1")

router.include_router(domains_router)
router.include_router(frameworks_router)
