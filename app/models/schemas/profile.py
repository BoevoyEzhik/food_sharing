import uuid

from pydantic import BaseModel
from datetime import date


class Profile(BaseModel):
    firstname: str
    lastname: str
    birthday: date
    city: str
    sex: str


class UpdatedProfile(Profile):
    id: uuid.UUID


