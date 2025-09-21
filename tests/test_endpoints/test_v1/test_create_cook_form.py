URL = "api/v1/create-cook-form"


async def test_create_cook_form_success(
    mocker, client, sample_cook_form, cook_form_response, date
):
    mock_service = mocker.patch(
        "app.api.v1.create_cook_form.CookFormService.create_cook_form"
    )
    mock_service.return_value = sample_cook_form
    json_body = {
        "user_id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "title": "string",
        "description": "string",
        "active": True,
    }
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 200
    assert response.json() == cook_form_response.model_dump(mode="json")


async def test_create_cook_form_wrong_type_body(client):
    json_body = {
        "user_id": "9fa009ef-c9e8-4f33-a29c-d8879df07107",
        "title": 123,
        "description": "string",
        "active": True,
    }
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422


async def test_create_cook_form_empty_body(client):
    json_body = {}
    response = client.post(url=URL, json=json_body)
    assert response.status_code == 422
