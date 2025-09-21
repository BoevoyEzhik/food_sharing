from app.models.db_models.profile import Profile


async def test_profile_create_success(profile_repo, mock_session, sample_profile_data):

    result = await profile_repo.profile_create(sample_profile_data)

    assert isinstance(result, Profile)

    assert result.user_id == sample_profile_data.user_id
    assert result.firstname == sample_profile_data.firstname
    assert result.lastname == sample_profile_data.lastname
    assert result.birthday == sample_profile_data.birthday
    assert result.city == sample_profile_data.city
    assert result.sex == sample_profile_data.sex

    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once_with(result)
