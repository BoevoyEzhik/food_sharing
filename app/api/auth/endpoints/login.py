from fastapi import APIRouter, Depends
from app.models.schemas.login import Login
from app.api.dependencies import get_user_service
from app.services.user_service import UserService
from app.models.schemas.tokendto import TokenWithType

login_router = APIRouter()


@login_router.post('/login')
async def login_user(login: Login,
                     user_service: UserService = Depends(get_user_service)
                     ) -> TokenWithType:
    token = await user_service.authenticate_user(login)
    return TokenWithType(token=token.token,
                         token_type='Bearer')
