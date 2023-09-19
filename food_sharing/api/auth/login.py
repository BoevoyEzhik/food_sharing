from flask import request, make_response, Response

from food_sharing.api.auth import auth_app
from food_sharing.data_base.users_db import *
from food_sharing.login_opereations.login_operations import check_password
from food_sharing.login_opereations.cookie import create_login_cookie


@auth_app.post('/login')
def login():
    body_json_data = request.get_json()
    if not is_user_in_db(body_json_data['email']):
        return Response(status=403, response='User not found')
    if check_password(body_json_data['email'], body_json_data['password']):
        login_cookie = create_login_cookie(body_json_data['email'])
        res = make_response('setting cookies')
        res.set_cookie('name', login_cookie, max_age=60 * 60 * 24 * 365 * 2)
        return res
    return Response(status=403, response='Incorrect email or password')
