from fastapi import APIRouter, Depends

from app.api.decorator import auth_required
from app.api.dependencies import get_cook_form_service
from app.models.schemas.cook_form import CookFormCreate, CookFormResponse
from app.services.service_cook_form import CookFormService

create_cook_form_router = APIRouter()


@auth_required
@create_cook_form_router.post("/create-cook-form")
async def create_cook_form(
    cook_form: CookFormCreate,
    cook_form_service: CookFormService = Depends(get_cook_form_service),
) -> CookFormResponse:
    created_cook_form = await cook_form_service.create_cook_form(cook_form)
    return CookFormResponse.model_validate(created_cook_form, from_attributes=True)
