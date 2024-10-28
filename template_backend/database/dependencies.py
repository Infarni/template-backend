from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .service import get_async_session

DbDep = Annotated[AsyncSession, Depends(get_async_session)]
