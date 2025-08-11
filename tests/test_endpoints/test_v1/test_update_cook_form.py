import pytest

URL = '/api/v1/update-cook-form'


async def test_update_user_info_success(mocker, client, sample_cook_form):
    mock_service = mocker.patch('app.api.v1.update_cook_form.CookFormService.update_cook_form')
    mock_service.return_value = sample_cook_form
    json_body = {'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'title': 'pizza',
                 'description': 'колбаска, сыр, лук, тесто',
                 'active': True}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 200
    assert response.json() == {'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                               'title': 'pizza',
                               'description': 'колбаска, сыр, лук, тесто',
                               'active': True}


async def test_update_cook_form_wrong_type(client):
    json_body = {'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'title': 123,
                 'description': 'description',
                 'active': True}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 422


async def test_update_user_cook_form_missed_field(client):
    json_body = {'user_id': '9fa009ef-c9e8-4f33-a29c-d8879df07107',
                 'description': 'description',
                 'active': True}
    response = client.put(url=URL,
                          json=json_body)
    assert response.status_code == 422
