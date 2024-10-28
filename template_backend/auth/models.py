from sqlalchemy.orm import Mapped, mapped_column

from template_backend.database.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
    avatar: Mapped[bytes | None]
