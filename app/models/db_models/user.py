from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from app.models.db_models.base import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column(String(160))
    # dishes: Mapped[list["Cookform"]] = relationship(
    #     'CookForm',
    #     back_populates='author',
    #     cascade='all, delete',
    # )
    # profile: Mapped["Profile"] = relationship(
    #     'Profile',
    #     back_populates='user',
    #     uselist=False,
    #     lazy='joined'
    # )



    