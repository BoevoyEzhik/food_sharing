import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_DAYS = os.getenv("ACCESS_TOKEN_EXPIRE_DAYS")


class Token:
    @staticmethod
    async def create_jwt_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now() + timedelta(days=float(ACCESS_TOKEN_EXPIRE_DAYS))  # type: ignore[arg-type] # noqa E501
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_user_info_from_token(token: str) -> str:
        try:
            payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Неверный токен")
        if datetime.fromtimestamp(payload["exp"]) < datetime.now():
            raise HTTPException(status_code=401, detail="Токен истёк")
        return payload.get("user_id")
