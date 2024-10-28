from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    DATABASE_URL: PostgresDsn = PostgresDsn(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
    )


database_settings: DatabaseConfig = DatabaseConfig()
