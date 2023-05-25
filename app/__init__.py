from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from app.main.startup import startup_jobs
from config import Config
from flask_bootstrap import Bootstrap5


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    with app.app_context():
        db.create_all()
        return app



from app import models