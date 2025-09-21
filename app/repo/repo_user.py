from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models.user import User
from app.models.schemas.register import Register


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, user: Register) -> User:
        db_user = User(**user.dict())
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user

    async def get_user_by_email(self, email: str) -> User | None:
        user = await self.session.execute(select(User).where(User.email == email))
        return user.scalar_one_or_none()
