from flask import Blueprint


digitizationknowledge = Blueprint(
    "digitizationknowledge", __name__)


def page():
    return "Hello, digitizationknowledge!"


digitizationknowledge.add_url_rule(
    "/digitizationknowledge/page", view_func=page)


def get_blueprints():
    return [digitizationknowledge]
