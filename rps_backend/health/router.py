from fastapi import APIRouter

from rps_backend.database import service as database_service

from . import schemas

router: APIRouter = APIRouter(prefix="/health", tags=["Health"])


@router.get("/check")
async def health_check_handler() -> schemas.HealthCheckSchema:
    return schemas.HealthCheckSchema(
        db_status=await database_service.check_connection()
    )
