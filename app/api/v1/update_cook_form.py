from fastapi import APIRouter, Depends

from app.api.dependencies import get_cook_form_service
from app.models.schemas.cook_form import UpdateCookForm
from app.api.decorator import auth_required
from app.services.cook_form_service import CookFormService

update_cook_form_router = APIRouter()


@auth_required
@update_cook_form_router.put('/update-cook-form')
async def update_cook_form(cook_form: UpdateCookForm,
                           cook_form_service: CookFormService = Depends(get_cook_form_service)
                           ) -> UpdateCookForm:
    return await cook_form_service.update_cook_form(cook_form)
