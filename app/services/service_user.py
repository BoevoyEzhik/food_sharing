from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.core.jwt_tokens import Token
from app.models.db_models.user import User
from app.models.schemas.login import Login
from app.models.schemas.register import Register, RegisterRequest
from app.models.schemas.tokendto import TokenDTO
from app.repo.repo_user import UserRepository
from app.services.utils import Password


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register_user(self, user_info: RegisterRequest) -> User:
        password_hash = await Password.create_hash_password(user_info.password)
        info_for_db = Register(email=user_info.email, password_hash=password_hash)
        try:
            user_info = await self.repo.register_user(info_for_db)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="user already exist")
        except Exception as e:
            raise HTTPException(status_code=405, detail=str(e))
        return user_info

    async def authenticate_user(self, login_info: Login) -> TokenDTO:
        user = await self.repo.get_user_by_email(login_info.email)
        if not user:
            raise HTTPException(status_code=400, detail="user not registered")
        if not await Password.is_valid_password(
            password=login_info.password, hashed_password=user.password_hash
        ):
            raise HTTPException(status_code=400, detail="wrong password")
        token = await Token.create_jwt_token({"user_id": str(user.id)})
        return TokenDTO(token=token)
