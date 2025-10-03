from datetime import datetime, timedelta
from unittest.mock import patch

import jwt

from app.core.jwt_tokens import ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM, SECRET_KEY, Token


async def test_create_jwt_token_with_valid_data():
    test_data = {"user_id": 123, "username": "testuser"}

    result = await Token.create_jwt_token(test_data)

    assert isinstance(result, str)
    assert len(result) > 0

    decoded = jwt.decode(result, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded["user_id"] == 123
    assert decoded["username"] == "testuser"
    assert "exp" in decoded


async def test_create_jwt_token_with_empty_data():
    test_data = {}

    result = await Token.create_jwt_token(test_data)

    assert isinstance(result, str)
    assert len(result) > 0

    decoded = jwt.decode(result, SECRET_KEY, algorithms=[ALGORITHM])
    assert "exp" in decoded


async def test_create_jwt_token_expiration_calculation():
    test_data = {"user_id": 123}

    with (
        patch("app.core.jwt_tokens.datetime") as mock_datetime,
        patch("app.core.jwt_tokens.jwt.encode") as mock_encode,
    ):

        fixed_now = datetime(2025, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = fixed_now

        await Token.create_jwt_token(test_data)

        call_args = mock_encode.call_args
        payload = call_args[1]["payload"]

        expected_exp = int(
            (fixed_now + timedelta(days=float(ACCESS_TOKEN_EXPIRE_DAYS))).timestamp()
        )
        assert payload["exp"] == expected_exp
