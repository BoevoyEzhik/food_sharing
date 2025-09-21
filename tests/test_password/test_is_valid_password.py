from unittest.mock import patch

import pytest

from app.services.utils import Password


async def test_is_valid_password_correct():
    plain_password = "correct_password"
    hashed = await Password.create_hash_password(plain_password)

    is_valid = await Password.is_valid_password(plain_password, hashed)
    assert is_valid is True


async def test_is_valid_password_incorrect():
    hashed = await Password.create_hash_password("real_password")
    is_valid = await Password.is_valid_password("wrong_guess", hashed)
    assert is_valid is False


async def test_is_valid_password_with_mock():
    test_password = "test123"
    test_hash = "$2b$12$fakehashedpassword"

    with patch("bcrypt.checkpw") as mock_check:
        mock_check.return_value = True

        result = await Password.is_valid_password(test_password, test_hash)

    assert result is True
    mock_check.assert_called_once_with(test_password.encode(), test_hash.encode())


async def test_is_valid_password_error():
    with patch("bcrypt.checkpw", side_effect=Exception("Check error")):
        with pytest.raises(Exception, match="Check error"):
            await Password.is_valid_password("test", "hash")
