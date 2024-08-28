from datetime import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), default=datetime.utcnow, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), default=datetime.utcnow, nullable=False
    )
