from datetime import timedelta
from flask import Flask
from app.factories.jwt import setup_jwt
from app.blueprints.auth.api import auth_bp
from i18n import init_i18n, DEFAULT_LANGUAGE


def setup_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'my-secret-key'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

    app.config['LANGUAGE'] = DEFAULT_LANGUAGE
    init_i18n(app.config.get('LANGUAGE'))

    setup_jwt(app)

    app.register_blueprint(auth_bp)

    return app
