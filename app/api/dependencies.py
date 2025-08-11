from fastapi import Depends
from app.db.database import get_async_session

from app.repo.repo_user import UserRepository
from app.services.user_service import UserService

from app.repo.repo_cook_form import CookFormRepository
from app.services.cook_form_service import CookFormService


async def get_user_repository(session=Depends(get_async_session)) -> UserRepository:
    return UserRepository(session)


async def get_user_service(user_repo=Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)


async def get_cook_form_repository(session=Depends(get_async_session)) -> CookFormRepository:
    return CookFormRepository(session)


async def get_cook_form_service(cook_form_repo=Depends(get_cook_form_repository)) -> CookFormService:
    return CookFormService(cook_form_repo)
