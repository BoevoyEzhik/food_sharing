from fastapi import APIRouter, Depends

from app.api.dependencies import get_user_service
from app.models.schemas.register import RegisterRequest, RegisterResponse
from app.services.service_user import UserService

register_router = APIRouter()


@register_router.post("/register")
async def register_user(
    register: RegisterRequest, user_service: UserService = Depends(get_user_service)
) -> RegisterResponse:
    user = await user_service.register_user(register)
    return RegisterResponse.model_validate(user, from_attributes=True)
