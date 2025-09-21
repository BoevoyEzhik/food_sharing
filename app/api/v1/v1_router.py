from fastapi import APIRouter

from app.api.v1.create_cook_form import create_cook_form_router
from app.api.v1.create_profile import create_profile_router
from app.api.v1.get_all_cook_form import get_all_cook_router
from app.api.v1.get_my_all_cook_form import get_my_all_cook_router
from app.api.v1.update_cook_form import update_cook_form_router
from app.api.v1.update_profile import update_user_info_router

v1_router = APIRouter(prefix="/api/v1")


v1_router.include_router(create_cook_form_router)
v1_router.include_router(get_my_all_cook_router)
v1_router.include_router(get_all_cook_router)
v1_router.include_router(update_cook_form_router)
v1_router.include_router(update_user_info_router)
v1_router.include_router(create_profile_router)
