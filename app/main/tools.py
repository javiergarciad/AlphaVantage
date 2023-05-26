import sqlalchemy
from app import db
from config import Config
from app.models import Symbol, DailyBar


def db_info():
    """
    Returns the database information
    """
    url = Config.SQLALCHEMY_DATABASE_URI
    symbols = len(Symbol.query.all())
    records = len(DailyBar.query.all())
    stmt = db.select(DailyBar.updated).order_by(sqlalchemy.desc(DailyBar.updated))
    last_update = db.session.execute(stmt).scalar()

    return {
        "url": url,
        "symbols": symbols,
        "records": records,
        "last_update": last_update,
    }

