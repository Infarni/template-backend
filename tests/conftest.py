from typing import AsyncGenerator

import pytest_asyncio

from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession


from template_backend.main import app
from template_backend.database.service import get_async_session


@pytest_asyncio.fixture
async def http_client() -> AsyncGenerator[AsyncClient, None]:
    host, port = "127.0.0.1", 8000

    async with AsyncClient(
        transport=ASGITransport(app=app, client=(host, port)),
        base_url=f"http://{host}:{port}/api",
    ) as client:
        yield client
