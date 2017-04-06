from app.database import db
from app.models.user import get_datastore, get_users
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_security import Security, login_required, roles_required


def create_app(config='Base', instance=True):
    app = Flask(__name__, instance_relative_config=instance)

    # Base Configuration
    app.config.from_object('app.config.' + config)

    # Load the instance configuration if True
    app.config.from_pyfile('config.py', silent=True)

    # Load from env
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    # CSRF
    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    user_datastore = get_datastore(db)
    app.security = Security(app, user_datastore)

    @app.before_first_request
    def init_db():
        try:
            get_users()
        except:
            from app.models import init_db
            init_db(user_datastore)

    @app.route('/', methods=['GET'])
    @login_required
    @roles_required('user')
    def index():
        return render_template('dashboard.html')

    return app
