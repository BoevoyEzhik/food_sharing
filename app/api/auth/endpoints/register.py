from fastapi import APIRouter, Depends
from app.models.schemas.register import RegisterIn, RegisterOut
from app.api.dependencies import get_user_service
from app.services.user_service import UserService

register_router = APIRouter()


@register_router.post('/register')
async def register_user(register: RegisterIn,
                        user_service: UserService = Depends(get_user_service)
                        ) -> RegisterOut:
    user = await user_service.register_user(register)
    return RegisterOut.model_validate(user, from_attributes=True)
