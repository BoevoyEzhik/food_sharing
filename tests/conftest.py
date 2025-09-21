from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.__main__ import app


@pytest.fixture(autouse=True)
def mock_decorator(mocker):
    mocker.patch("app.api.decorator.auth_required", lambda f: f)


@pytest.fixture(autouse=True)
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="session")
def date():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
