from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.db_models.base import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column(String(160))
