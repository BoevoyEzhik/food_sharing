from pydantic import BaseModel
import uuid


class CookFormIn(BaseModel):
    title: str
    description: str
    active: bool

    class Config:
        from_attributes = True


class CookFormOut(CookFormIn):
    user_id: uuid.UUID


class UpdateCookForm(CookFormOut):
    pass


class CookFormList(BaseModel):
    all_cook_forms: list[CookFormOut]

    class Config:
        from_attributes = True