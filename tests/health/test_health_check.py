import pytest

from httpx import AsyncClient, Response


@pytest.mark.asyncio
async def test_health_check(http_client: AsyncClient) -> None:
    response: Response = await http_client.get("/health/check")
    assert response.status_code == 200

    json = response.json()
    assert json["dbStatus"]
