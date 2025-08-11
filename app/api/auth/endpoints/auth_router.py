from fastapi import APIRouter
from app.api.auth.endpoints.login import login_router
from app.api.auth.endpoints.logout import logout_router
from app.api.auth.endpoints.register import register_router


auth_router = APIRouter(prefix='/auth')

auth_router.include_router(register_router)
auth_router.include_router(login_router)
auth_router.include_router(logout_router)