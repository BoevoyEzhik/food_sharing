from fastapi import APIRouter, Request
from app.api.decorator import auth_required


logout_router = APIRouter()


@logout_router.get('/logout')
@auth_required
async def logout(request: Request):
    return 'logout YEAH!'
