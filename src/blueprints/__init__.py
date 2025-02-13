from src.blueprints.index import index_blueprint

def init_blueprint(app):
    app.register_blueprint(index_blueprint,url_prefix='/')