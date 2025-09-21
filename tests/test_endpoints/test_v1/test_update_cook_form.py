import pytest

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormResponse

URL = "/api/v1/update-cook-form"


@pytest.fixture
def updated_cook_form(date):
    return CookForm(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="string2",
        description="string2",
        active=True,
        created_at=date,
        updated_at=date,
    )


@pytest.fixture
def cook_form_updated_response(date):
    return CookFormResponse(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        title="string2",
        description="string2",
        active=True,
        created_at=date,
        updated_at=date,
    )


async def test_update_cook_form_info_success(
    mocker, client, sample_cook_form, updated_cook_form, cook_form_updated_response
):
    mock_service = mocker.patch(
        "app.api.v1.update_cook_form.CookFormService.update_cook_form"
    )
    mock_service.return_value = updated_cook_form
    json_body = {
        "id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "title": "string2",
        "description": "string2",
        "active": True,
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 200
    assert response.json() == cook_form_updated_response.model_dump(mode="json")


async def test_update_cook_form_wrong_type(client):
    json_body = {
        "id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "title": 123,
        "description": "description",
        "active": True,
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 422


async def test_update_cook_form_missed_required_field(client):
    json_body = {
        "description": "description",
        "active": True,
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 422
