from flask import Blueprint

auth_app = Blueprint('auth', __name__)

from . import (
    logout,
    login,
    register,
)
