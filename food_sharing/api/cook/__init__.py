from flask import Blueprint

cook_app = Blueprint('cook', __name__)

from . import (
    create_cook_form,
    get_all_cook_form,
    get_my_all_cook_form,
    update_cook_form,
)
