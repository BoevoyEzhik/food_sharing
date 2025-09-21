from fastapi import APIRouter, Depends

from app.api.decorator import auth_required
from app.api.dependencies import get_cook_form_service
from app.models.schemas.cook_form import CookFormList
from app.services.service_cook_form import CookFormService

get_all_cook_router = APIRouter()


@auth_required
@get_all_cook_router.get("/get-all-cook-form")
async def get_all_cook_form(
    limit: int = 10,
    offset: int = 0,
    cook_form_service: CookFormService = Depends(get_cook_form_service),
) -> CookFormList:
    cook_forms = await cook_form_service.get_all_cook_form(limit=limit, offset=offset)
    return CookFormList(all_cook_forms=cook_forms)
