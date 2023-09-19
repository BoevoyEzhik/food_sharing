from flask import request, Response

from food_sharing.api.user import user_app
from food_sharing.data_base.users_db import select_id_from_users, update_user_info_in_db
from food_sharing.login_opereations.login_operations import get_email_from_cookie
from food_sharing.middlewares.auth_middleware import auth_middleware


@user_app.put('/update-user-info')
@auth_middleware
def update_user_info():
    body_json_data = request.get_json()
    my_dict = {"user_id": ''}
    sign_cookie = request.cookies.get('name')
    email = get_email_from_cookie(sign_cookie)
    my_dict['user_id'] = select_id_from_users(email)
    my_dict.update(body_json_data)
    update_user_info_in_db(my_dict)
    return Response('Обновил табличку юзерс', status=200)
