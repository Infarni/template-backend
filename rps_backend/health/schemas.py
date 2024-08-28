from rps_backend.schemas import BaseSchema


class HealthCheckSchema(BaseSchema):
    db_status: bool
