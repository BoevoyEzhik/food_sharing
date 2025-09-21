import pytest

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormList, CookFormResponse


@pytest.fixture
def cook_form_response(date):
    return CookFormResponse(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="string",
        description="string",
        active=True,
        created_at=date,
        updated_at=date,
    )


@pytest.fixture
def sample_cook_form(date):
    return CookForm(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="string",
        description="string",
        active=True,
        created_at=date,
        updated_at=date,
    )


@pytest.fixture
def cook_form_response_list(sample_cook_form):
    return [
        CookFormResponse.model_validate(sample_cook_form, from_attributes=True),
        CookFormResponse.model_validate(sample_cook_form, from_attributes=True),
    ]


@pytest.fixture
def all_cook_forms(cook_form_response_list):
    return CookFormList(all_cook_forms=cook_form_response_list).model_dump(mode="json")
