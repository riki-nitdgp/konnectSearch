
from fastapi import APIRouter
from .handlers.health import router as health

router = APIRouter()

router.include_router(health, tags=["health-check"])