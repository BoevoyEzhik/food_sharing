from fastapi import APIRouter, Depends

from app.api.decorator import auth_required
from app.api.dependencies import get_cook_form_service
from app.models.schemas.cook_form import CookFormResponse, CookFormUpdate
from app.services.service_cook_form import CookFormService

update_cook_form_router = APIRouter()


@auth_required
@update_cook_form_router.put("/update-cook-form")
async def update_cook_form(
    cook_form: CookFormUpdate,
    cook_form_service: CookFormService = Depends(get_cook_form_service),
) -> CookFormResponse:
    updated_cook_form = await cook_form_service.update_cook_form(cook_form)
    return CookFormResponse.model_validate(updated_cook_form, from_attributes=True)
