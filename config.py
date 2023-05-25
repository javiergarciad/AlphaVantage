import os
from pathlib import Path
from dotenv import load_dotenv

BASEDIR = str(Path(__file__).parent.absolute())
load_dotenv(Path(BASEDIR, '.env'))


class Config(object):
    # Flask secret
    SECRET_KEY = '9df31cad3eb2f66386575da6dd6641ae'

    # Alpha Advantage api key
    API_KEY = os.getenv("API_KEY")

    # Sqlite database configuration
    DB_NAME = "app.db"
    DB_ENGINE = "sqlite3"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASEDIR}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

