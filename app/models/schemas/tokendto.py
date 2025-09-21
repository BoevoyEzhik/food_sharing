from pydantic import BaseModel


class TokenDTO(BaseModel):
    token: str


class TokenWithType(TokenDTO):
    token_type: str
