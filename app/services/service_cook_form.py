import uuid
from typing import Type

from fastapi import HTTPException

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import (
    CookFormCreate,
    CookFormResponse,
    CookFormUpdate,
)
from app.repo.repo_cook_form import CookFormRepository


class CookFormService:
    def __init__(self, repo: CookFormRepository):
        self.repo = repo

    async def create_cook_form(self, cook_form: CookFormCreate) -> CookForm:
        try:
            return await self.repo.create_cook_form(cook_form)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update_cook_form(self, cook_form: CookFormUpdate) -> Type[CookForm]:
        try:
            updated_cook_form = await self.repo.update_cook_form(cook_form)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return updated_cook_form

    async def get_my_all_cook_form(
        self, user_id: uuid.UUID, limit: int, offset: int
    ) -> list[CookFormResponse]:
        try:
            cook_forms = await self.repo.get_my_all_cook_form(
                user_id=user_id, limit=limit, offset=offset
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return [
            CookFormResponse.model_validate(cook_form, from_attributes=True)
            for cook_form in cook_forms
        ]

    async def get_all_cook_form(
        self, limit: int, offset: int
    ) -> list[CookFormResponse]:
        try:
            cook_forms = await self.repo.get_all_cook_form(limit=limit, offset=offset)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return [
            CookFormResponse.model_validate(cook_form, from_attributes=True)
            for cook_form in cook_forms
        ]
