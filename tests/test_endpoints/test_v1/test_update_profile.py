from datetime import date as d

import pytest

from app.models.db_models.profile import Profile
from app.models.schemas.profile import ProfileResponse

URL = "/api/v1/update-profile"


@pytest.fixture
def sample_profile(date):
    return Profile(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
        created_at=date,
        updated_at=date,
    )


@pytest.fixture
def profile_response(date):
    return ProfileResponse(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        firstname="firstname",
        lastname="lastname",
        birthday=d(2000, 12, 21).isoformat(),
        city="city",
        sex="M",
        created_at=date,
        updated_at=date,
    )


async def test_update_profile_success(mocker, client, sample_profile, profile_response):
    mock_service = mocker.patch(
        "app.api.v1.update_profile.ProfileService.profile_update"
    )
    mock_service.return_value = sample_profile
    json_body = {
        "id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "user_id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "firstname": "firstname",
        "lastname": "lastname",
        "birthday": d(2000, 12, 21).isoformat(),
        "city": "city",
        "sex": "M",
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 200
    assert response.json() == profile_response.model_dump(mode="json")


async def test_update_profile_wrong_type(client):
    json_body = {
        "user_id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "title": 123,
        "description": "lastname",
        "birthday": "description",
        "sex": "M",
        "active": True,
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 422


async def test_update_profile_missed_required_field(client):
    json_body = {
        "description": "lastname",
        "birthday": "description",
        "active": True,
    }
    response = client.put(url=URL, json=json_body)
    assert response.status_code == 422
