import pytest
from unittest.mock import AsyncMock
from app.core.jwt_tokens import Token

from fastapi import Request


@pytest.fixture
def mock_request():
    return AsyncMock(spec=Request)


