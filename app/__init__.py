from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_bootstrap import Bootstrap5
from flask_migrate import upgrade

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)

# https://stackoverflow.com/questions/74206531/flask-migrate-upgrade-fails-because-the-application-needs-to-run-code-that-modif

from app import routes
