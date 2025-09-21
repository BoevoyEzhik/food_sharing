import uuid
from datetime import datetime

from pydantic import BaseModel


class CookFormBase(BaseModel):
    title: str
    description: str
    active: bool


class CookFormCreate(CookFormBase):
    user_id: uuid.UUID


class CookFormUpdate(BaseModel):
    id: uuid.UUID
    title: str | None = None
    description: str | None = None
    active: bool | None = None


class CookFormResponse(CookFormBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class CookFormList(BaseModel):
    all_cook_forms: list[CookFormResponse]

    class Config:
        from_attributes = True
