from fastapi import APIRouter, Depends
from app.models.schemas.cook_form import CookFormIn, CookFormOut
from app.api.decorator import auth_required
from app.api.dependencies import get_cook_form_service
from app.services.cook_form_service import CookFormService


create_cook_form_router = APIRouter()


@auth_required
@create_cook_form_router.post('/create-cook-form')
async def create_cook_form(cook_form: CookFormIn,
                           cook_form_service: CookFormService = Depends(get_cook_form_service)
                           ) -> CookFormOut:
    created_cook_form = await cook_form_service.create_cook_form(cook_form)
    return CookFormOut(user_id=created_cook_form.user_id,
                       title=created_cook_form.title,
                       description=created_cook_form.description,
                       active=created_cook_form.active)
