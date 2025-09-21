from unittest.mock import AsyncMock

import pytest
from fastapi import Request


@pytest.fixture
def mock_request():
    return AsyncMock(spec=Request)
