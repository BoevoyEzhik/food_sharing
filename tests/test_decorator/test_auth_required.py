from unittest.mock import patch

import pytest
from fastapi import HTTPException, Request

from app.api.decorator import auth_required


async def test_auth_required_success(mock_request):
    fake_token = "valid.token.here"
    mock_request.headers = {"Authorization": f"Bearer {fake_token}"}

    with patch("app.core.jwt_tokens.Token.get_user_info_from_token") as mocked_token:
        mocked_token.return_value = 1234

        @auth_required
        async def test_func(request: Request):
            return {"status": "success", "user_id": request.state.user_id}

        result = await test_func(mock_request)

        assert result == {"status": "success", "user_id": 1234}


async def test_auth_required_missing_token(mock_request):
    mock_request.headers = {}

    @auth_required
    async def test_func(request: Request):
        pass

    with pytest.raises(HTTPException) as exc_info:
        await test_func(mock_request)

    assert exc_info.value.status_code == 401
    assert "Необходима авторизация" in exc_info.value.detail


async def test_auth_required_invalid_token_format(mock_request):
    mock_request.headers = {"Authorization": "InvalidTokenFormat"}

    @auth_required
    async def test_func(request: Request):
        pass

    with pytest.raises(HTTPException) as exc_info:
        await test_func(mock_request)

    assert exc_info.value.status_code == 401
    assert "Необходима авторизация" in exc_info.value.detail
