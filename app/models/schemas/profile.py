import uuid
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


class ProfileDTO(BaseModel):
    user_id: uuid.UUID
    firstname: str
    lastname: str
    birthday: date
    city: str
    sex: Literal["M", "F"]

    class Config:
        from_attributes = True


class ProfileResponse(ProfileDTO):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class ProfileUpdate(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID | None = None
    firstname: str | None = None
    lastname: str | None = None
    birthday: date | None = None
    city: str | None = None
    sex: Literal["M", "F"] | None = None

    class Config:
        from_attributes = True
