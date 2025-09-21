from fastapi import Depends

from app.db.database import get_async_session
from app.repo.repo_cook_form import CookFormRepository
from app.repo.repo_profile import ProfileRepository
from app.repo.repo_user import UserRepository
from app.services.service_cook_form import CookFormService
from app.services.service_profile import ProfileService
from app.services.service_user import UserService


async def get_user_repository(session=Depends(get_async_session)) -> UserRepository:
    return UserRepository(session)


async def get_user_service(user_repo=Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)


async def get_cook_form_repository(
    session=Depends(get_async_session),
) -> CookFormRepository:
    return CookFormRepository(session)


async def get_cook_form_service(
    cook_form_repo=Depends(get_cook_form_repository),
) -> CookFormService:
    return CookFormService(cook_form_repo)


async def get_profile_repository(
    session=Depends(get_async_session),
) -> ProfileRepository:
    return ProfileRepository(session)


async def get_profile_service(
    profile_repo=Depends(get_profile_repository),
) -> ProfileService:
    return ProfileService(profile_repo)
