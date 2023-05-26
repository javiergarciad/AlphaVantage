from pathlib import Path


BASEDIR = str(Path(__file__).parent.absolute())

class Config(object):
    # Flask secret
    SECRET_KEY = '9df31cad3eb2f66386575da6dd6641ae'

    # Sqlite database configuration
    DB_NAME = "app.db"
    DB_LOCATION = f"{BASEDIR}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_LOCATION}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

