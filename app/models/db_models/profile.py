import uuid
from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column

from app.models.db_models.base import Base

gender_enum = ENUM("M", "F", name="gender", create_type=False)


class Profile(Base):
    __tablename__ = "profile"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[date] = mapped_column()
    city: Mapped[str] = mapped_column(String(80))
    sex: Mapped[ENUM] = mapped_column(gender_enum)
