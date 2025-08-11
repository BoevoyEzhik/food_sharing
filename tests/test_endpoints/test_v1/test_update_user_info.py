import pytest
from datetime import date

from app.models.db_models.profile import Profile

URL = '/api/v1/update-user-info'


@pytest.fixture
def sample_user_profile():
    return Profile(id='9fa009ef-c9e8-4f33-a29c-d8879df07107',
                   firstname='firstname',
                   lastname='lastname',
                   birthday=date(2000, 12, 21).isoformat(),
                   city='city',
                   sex='sex')


async def test_update_user_info_success(mocker, client, sample_user_profile):
    mock_service = mocker.patch('app.api.v1.update_user_info.UserService.update_user_info')
    mock_service.return_value = sample_user_profile
    json_body = {'id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'firstname': 'firstname',
                 'lastname': 'lastname',
                 'birthday': date(2000, 12, 21).isoformat(),
                 'city': 'city',
                 'sex': 'sex'}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 200
    assert response.json() == {'id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                               'firstname': 'firstname',
                               'lastname': 'lastname',
                               'birthday': date(2000, 12, 21).isoformat(),
                               'city': 'city',
                               'sex': 'sex'}


async def test_update_user_info_wrong_type(client):
    json_body = {'id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'title': 123,
                 'description': 'lastname',
                 'birthday': 'description',
                 'active': True}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 422


async def test_update_user_info_missed_field(client):
    json_body = {'id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'description': 'lastname',
                 'birthday': 'description',
                 'active': True}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 422
