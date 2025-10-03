from datetime import datetime, timedelta
from unittest.mock import patch

import jwt
import pytest
from fastapi import HTTPException

from app.core.jwt_tokens import ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM, SECRET_KEY, Token

payload = {
    "user_id": 123,
    "username": "testuser",
    "exp": int(
        (datetime.now() + timedelta(days=float(ACCESS_TOKEN_EXPIRE_DAYS))).timestamp()  # type: ignore[arg-type] # noqa E501
    ),
}


async def test_get_user_info_from_token_with_valid_data():
    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)

    result = await Token.get_user_info_from_token(token)

    assert result == 123


async def test_get_user_info_from_token_invalid_token():
    token = jwt.encode(payload=payload, key="SECRET_KEY", algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as exc_info:
        await Token.get_user_info_from_token(token)

    assert exc_info.value.status_code == 401
    assert "Неверный токен" in exc_info.value.detail


async def test_get_user_info_from_token_expired():
    expired_payload = {
        "user_id": "12345",
        "exp": (datetime.now() - timedelta(days=1)).timestamp(),
    }

    with patch("app.core.jwt_tokens.jwt.decode") as mock_decode:
        mock_decode.return_value = expired_payload

        with pytest.raises(HTTPException) as exc_info:
            await Token.get_user_info_from_token("any_token")

        assert exc_info.value.status_code == 401
        assert "Токен истёк" in exc_info.value.detail
