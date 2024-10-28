from fastapi import APIRouter

from template_backend.health.router import router as health_router

api_router: APIRouter = APIRouter(prefix="/api")

api_router.include_router(health_router)
