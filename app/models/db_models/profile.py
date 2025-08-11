from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from app.models.db_models.base import Base
from datetime import date
from sqlalchemy.dialects.postgresql import ENUM


#class Gender(str, Enum):
#    MALE = 'мужчина'
#    FEMALE = 'женщина'

gender_enum = ENUM("M", "F", name="gender", create_type=False)


class Profile(Base):
    __tablename__ = 'profile'

    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    birthday: Mapped[date] = mapped_column()
    city: Mapped[str] = mapped_column(String(80))
    sex: Mapped[ENUM] = mapped_column(gender_enum)
    # user: Mapped["User"] = relationship(
    #     "User",
    #     back_populates="profile",
    #     uselist=False
    # )
