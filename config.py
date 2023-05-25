import os
from pathlib import Path
import secrets


class Config(object):
    # generate a secret key each time the server is iniciated.
    # this is suitable here becasuse we are nsecrets.token_hex(16)ot storing sessions
    SECRET_KEY = '9df31cad3eb2f66386575da6dd6641ae'
    # Alpha Advantage api key
    API_KEY = os.environ.get("API_KEY") or None
    # Sqlite database configuration
    DB_NAME = "app.db"
    DB_ENGINE = "sqlite3"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.absolute()}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
