from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.schemas.register import RegisterInDB
from app.models.db_models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, user: RegisterInDB) -> User:
        db_user = User(**user.dict())
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user

    async def get_user_by_email(self, email: str) -> User | None:
        user = await self.session.execute(
            select(User).where(User.email == email)
        )
        return user.scalar_one_or_none()

    async def update_user_info(self, user_id, user_info: dict):
        stmt = (
            update(User)
            .where(id == user_id)
            .values(**user_info)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        user = await self.session.refresh(User)
        return user
