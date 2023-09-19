from flask import request, Response

from food_sharing.api.cook import cook_app
from food_sharing.data_base.cook_form_db import insert_into_cook_form_db
from food_sharing.data_base.users_db import select_id_from_users
from food_sharing.login_opereations.login_operations import get_email_from_cookie
from food_sharing.middlewares.auth_middleware import auth_middleware


@cook_app.post('/create-cook-form')
@auth_middleware
def create_cook_form():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    insert_into_cook_form_db(my_dict)
    return Response("Вставил блюдо", status=200)
