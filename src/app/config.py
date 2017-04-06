import os
import tempfile


class Base():
    TESTING = False
    DEBUG = False

    SECRET_KEY = 'changeThisKey'
    CSRF_ENABLED = True

    # CHANGE the database path and name
    DATABASE = os.path.basename('app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

    SECURITY_TRACKABLE = True
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['email', 'username']
    SECURITY_PASSWORD_SALT = "changeThisInInstanceConfiguration"

    # Flask-User settings
    USER_APP_NAME = "App"
    USER_ENABLE_REGISTRATION = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Delete Warnings
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Base):
    f, DATABASE = tempfile.mkstemp(
        prefix='flask-security-test-db', suffix='.db', dir='/tmp')

    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    USER_APP_NAME = "App-Testing"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
