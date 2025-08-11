from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
import uuid
from app.models.db_models.base import Base


class CookForm(Base):
    __tablename__ = 'cookform'

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(String(3000))
    active: Mapped[bool] = mapped_column()
    # author: Mapped[User] = relationship(
    #     'User',
    #     back_populates='dishes'
    # )
