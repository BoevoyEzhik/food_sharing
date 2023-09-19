from flask import request, Response

from food_sharing.api.cook import cook_app
from food_sharing.data_base.cook_form_db import get_my_all_cook_form_from_db
from food_sharing.data_base.users_db import select_id_from_users
from food_sharing.login_opereations.login_operations import get_email_from_cookie
from food_sharing.middlewares.auth_middleware import auth_middleware


@cook_app.get('/api/v1/get-my-all-cook-form')
@auth_middleware
def get_my_all_cook_form():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    result = get_my_all_cook_form_from_db(my_dict)
    return Response(status=200, response=result)
