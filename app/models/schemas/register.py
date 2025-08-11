import uuid
from pydantic import BaseModel, EmailStr


class RegisterIn(BaseModel):
    email: EmailStr
    password: str


class RegisterInDB(BaseModel):
    email: str
    password_hash: str


class RegisterOut(BaseModel):
    id: uuid.UUID
    email: str
    password_hash: str

    class Config:
        from_attributes = True
