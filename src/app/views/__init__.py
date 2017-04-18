from .user import user_bp

blueprints = {
    '/api/user': user_bp,
}


def register_views(app):
    for url, manager in blueprints.items():
        app.register_blueprint(manager, url_prefix=url)
