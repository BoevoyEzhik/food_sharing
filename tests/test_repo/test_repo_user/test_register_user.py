from app.models.db_models.user import User
from app.models.schemas.register import Register


async def test_register_user_with_mocks(mock_session, user_repo):
    user_data = Register(email="test@example.com", password_hash="password_hash")

    result = await user_repo.register_user(user_data)

    assert isinstance(result, User)
    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once_with(result)
    assert result.email == "test@example.com"
    assert result.password_hash == "password_hash"
