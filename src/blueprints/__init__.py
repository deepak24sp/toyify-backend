from src.blueprints.index import index_blueprint
from src.blueprints.category import category_blueprint

def init_blueprint(app):
    app.register_blueprint(index_blueprint,url_prefix='/')
    app.register_blueprint(category_blueprint,url_prefix = '/category')