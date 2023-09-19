from flask import request, make_response

from food_sharing.api.auth import auth_app


@auth_app.post('/logout')
def logout():
    resp = make_response()
    cookies = request.cookies
    for cookie in cookies:
        resp.delete_cookie(cookie)
    return resp
