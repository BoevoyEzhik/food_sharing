URL = "/api/v1/get-my-all-cook-form"


async def test_get_my_all_cook_form_success(
    mocker, client, cook_form_response_list, all_cook_forms
):
    mock_service = mocker.patch(
        "app.api.v1.get_my_all_cook_form.CookFormService.get_my_all_cook_form"
    )
    mock_service.return_value = cook_form_response_list
    response = client.get(
        url=URL, params="user_id=9fa009ef-c9e8-4f33-a29c-d8879df07107"
    )

    assert response.status_code == 200
    assert response.json() == all_cook_forms
