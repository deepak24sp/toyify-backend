from flask import Blueprint
from src.handlers.categories import CategoryHandler
category_blueprint = Blueprint("category",__name__)

@category_blueprint.route('/')
def category():
    return CategoryHandler.get_categories()