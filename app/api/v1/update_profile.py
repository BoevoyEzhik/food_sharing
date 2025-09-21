from fastapi import APIRouter, Depends

from app.api.decorator import auth_required
from app.api.dependencies import get_profile_service
from app.models.schemas.profile import ProfileResponse, ProfileUpdate
from app.services.service_profile import ProfileService

update_user_info_router = APIRouter()


@auth_required
@update_user_info_router.put("/update-profile")
async def update_user_info(
    info_to_update: ProfileUpdate,
    profile_service: ProfileService = Depends(get_profile_service),
) -> ProfileResponse:
    result = await profile_service.profile_update(info_to_update)
    return ProfileResponse.model_validate(result, from_attributes=True)
