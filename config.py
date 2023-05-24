import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # generate a secret key each time the server is iniciated.
    # this is suitable here becasuse we are not storing sessions
    SECRET_KEY = secrets.token_hex(16)
    # Alpha Advantage api key
    API_KEY = os.environ.get('API_KEY') or None
    # Sqlite database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    