import uuid
from unittest.mock import AsyncMock

import pytest

from app.models.db_models.cook_form import CookForm
from app.models.schemas.cook_form import CookFormResponse
from app.repo.repo_cook_form import CookFormRepository
from app.services.service_cook_form import CookFormService


@pytest.fixture
def mock_repo():
    return AsyncMock(spec=CookFormRepository)


@pytest.fixture
def cook_form_service(mock_repo):
    return CookFormService(repo=mock_repo)


@pytest.fixture
def cook_form_response(date):
    return CookFormResponse(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07107",
        user_id=uuid.UUID("9fa009ef-c9e8-4f33-a29c-d8879df07107"),
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
def sample_cook_form2(date):
    return CookForm(
        id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
        user_id="9fa009ef-c9e8-4f33-a29c-d8879df07106",
        title="string",
        description="string",
        active=True,
        created_at=date,
        updated_at=date,
    )
