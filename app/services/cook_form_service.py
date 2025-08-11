from fastapi import HTTPException

import uuid

from app.models.schemas.cook_form import UpdateCookForm
from app.repo.repo_cook_form import CookFormRepository
from app.models.schemas.cook_form import CookFormOut


class CookFormService:

    def __init__(self, repo: CookFormRepository):
        self.repo = repo

    async def create_cook_form(self, data):
        try:
            return await self.repo.create_cook_form(data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update_cook_form(self, cook_form_info: UpdateCookForm) -> UpdateCookForm:
        updated_dict = cook_form_info.dict()
        user_id = updated_dict.pop('user_id')
        try:
            updated_cook_form = await self.repo.update_cook_form(user_id, updated_dict)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return updated_cook_form

    async def get_my_all_cook_form(self, user_id: uuid.UUID, limit: int, offset: int) -> list[CookFormOut]:
        try:
            cook_forms = await self.repo.get_my_all_cook_form(
                user_id=user_id,
                limit=limit,
                offset=offset
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return [CookFormOut.model_validate(cook_form, from_attributes=True) for cook_form in cook_forms]

    async def get_all_cook_form(self, limit: int, offset: int) -> list[CookFormOut]:
        try:
            cook_forms = await self.repo.get_all_cook_form(
                limit=limit,
                offset=offset
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        return [CookFormOut.model_validate(cook_form, from_attributes=True) for cook_form in cook_forms]
    