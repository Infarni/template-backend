from typing import AsyncGenerator, Annotated

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.exc import DBAPIError

from .config import database_settings

engine: AsyncEngine = create_async_engine(str(database_settings.DATABASE_URL))
async_session_maker: async_sessionmaker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def check_connection() -> bool:
    async for session in get_async_session():
        query: Select[tuple[int]] = select(1)

        try:
            await session.execute(query)
            return True
        except DBAPIError:
            return False

    return False
