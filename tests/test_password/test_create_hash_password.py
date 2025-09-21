from unittest.mock import patch

import pytest

from app.services.utils import Password


async def test_create_hash_password_success():
    test_password = "secure_password123"
    hashed = await Password.create_hash_password(test_password)

    assert isinstance(hashed, str)
    assert len(hashed) > 0
    assert hashed.startswith("$2b$")


async def test_create_hash_password_with_mock():
    test_password = "secure_password123"
    expected_hash = "$2b$12$fakehashedpassword"

    with patch("bcrypt.hashpw") as mock_hash, patch("bcrypt.gensalt") as mock_salt:
        mock_salt.return_value = b"fake_salt"
        mock_hash.return_value = expected_hash.encode()

        result = await Password.create_hash_password(test_password)

        assert result == expected_hash
        mock_hash.assert_called_once_with(test_password.encode(), b"fake_salt")


async def test_create_hash_password_error():
    with patch("bcrypt.hashpw", side_effect=Exception("Hashing error")):
        with pytest.raises(Exception, match="Hashing error"):
            await Password.create_hash_password("test")
