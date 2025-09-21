from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models.cook_form import CookForm
from app.repo.repo_cook_form import CookFormRepository


@pytest.fixture
def mock_session():
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def cook_form_repo(mock_session):
    return CookFormRepository(mock_session)


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
