from functools import wraps

from fastapi import HTTPException, Request

from app.core.jwt_tokens import Token


def auth_required(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Необходима авторизация")
        token = auth_header.split(" ")[1]
        request.state.user_id = await Token.get_user_info_from_token(token)
        return await func(request, *args, **kwargs)

    return wrapper
