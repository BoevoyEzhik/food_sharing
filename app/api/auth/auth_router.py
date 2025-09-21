from fastapi import APIRouter

from app.api.auth.login import login_router
from app.api.auth.register import register_router

auth_router = APIRouter(prefix="/auth")

auth_router.include_router(register_router)
auth_router.include_router(login_router)
