import uuid
from typing import Sequence, Type

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormCreate, CookFormUpdate


class CookFormRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_cook_form(self, cook_form: CookFormCreate) -> CookForm:
        db_cook_form = CookForm(**cook_form.dict())
        self.session.add(db_cook_form)
        await self.session.commit()
        await self.session.refresh(db_cook_form)
        return db_cook_form

    async def update_cook_form(self, cook_form: CookFormUpdate) -> Type[CookForm]:
        update_data = cook_form.model_dump(exclude_unset=True)
        cook_id = update_data.pop("id")
        db_form = await self.session.get(CookForm, cook_id)

        if not db_form:
            raise HTTPException(status_code=400, detail="cook not created")

        for field, value in update_data.items():
            setattr(db_form, field, value)

        await self.session.commit()
        await self.session.refresh(db_form)
        return db_form

    async def get_my_all_cook_form(
        self, user_id: uuid.UUID, limit: int = 1, offset: int = 10
    ) -> Sequence[CookForm]:
        result = await self.session.execute(
            select(CookForm)
            .where(CookForm.user_id == user_id)
            .offset(offset)
            .limit(limit)
        )
        return result.scalars().all()

    async def get_all_cook_form(
        self, limit: int = 1, offset: int = 10
    ) -> Sequence[CookForm]:
        result = await self.session.execute(
            select(CookForm).offset(offset).limit(limit)
        )
        return result.scalars().all()
