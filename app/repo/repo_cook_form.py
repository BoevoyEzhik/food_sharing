import uuid
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormIn
from sqlalchemy import update, select


class CookFormRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_cook_form(self, cook_form: CookFormIn):
        self.session.add(cook_form)
        await self.session.commit()
        return cook_form

    async def update_cook_form(self,  user_id: uuid.UUID, cook_form: dict[str: str]):
        stmt = update(CookForm).where(CookForm.user_id == user_id).values(**cook_form)
        await self.session.execute(stmt)
        await self.session.commit()
        updated_cook_form = await self.session.refresh(CookForm)
        return updated_cook_form

    async def get_my_all_cook_form(self, user_id: uuid.UUID, limit: int = 1, offset: int = 10) -> Sequence[CookForm]:
        result = await self.session.execute(
            select(CookForm)
            .where(CookForm.user_id == user_id)
            .offset(offset)
            .limit(limit)
        )
        return result.scalars().all()

    async def get_all_cook_form(self, limit: int = 1, offset: int = 10) -> Sequence[CookForm]:
        result = await self.session.execute(
            select(CookForm)
            .offset(offset)
            .limit(limit)
        )
        return result.scalars().all()
    