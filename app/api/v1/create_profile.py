from fastapi import APIRouter, Depends

from app.api.decorator import auth_required
from app.api.dependencies import get_profile_service
from app.models.schemas.profile import ProfileDTO, ProfileResponse
from app.services.service_profile import ProfileService

create_profile_router = APIRouter()


@auth_required
@create_profile_router.post("/create-profile")
async def create_profile(
    create_profile_info: ProfileDTO,
    profile_service: ProfileService = Depends(get_profile_service),
) -> ProfileResponse:
    result = await profile_service.profile_create(create_profile_info)
    return ProfileResponse.model_validate(result, from_attributes=True)
