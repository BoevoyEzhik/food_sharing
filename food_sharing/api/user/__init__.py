from flask import Blueprint

user_app = Blueprint('user', __name__)

from . import (
    update_user_info,
)