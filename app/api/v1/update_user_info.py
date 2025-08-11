from fastapi import APIRouter, Depends

from app.api.dependencies import get_user_service
from app.models.schemas.profile import UpdatedProfile
from app.api.decorator import auth_required
from app.services.user_service import UserService

update_user_info_router = APIRouter()


@auth_required
@update_user_info_router.put('/update-user-info')
async def update_user_info(info_to_update: UpdatedProfile,
                           user_service: UserService = Depends(get_user_service)
                           ) -> UpdatedProfile:
    result = await user_service.update_user_info(info_to_update)
    return UpdatedProfile.model_validate(result, from_attributes=True)
