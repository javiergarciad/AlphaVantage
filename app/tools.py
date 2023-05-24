import sqlalchemy
from app import db


def test_db():
    """
    Tests if the database is accessible and all tables exists
    """
    try:
        sqlalchemy.inspect(db.engine).has_table("alembic_version")
        sqlalchemy.inspect(db.engine).has_table("symbol")
        sqlalchemy.inspect(db.engine).has_table("daily_bar")

        return True, "Responsive"
    except:
        return False, "Unresponsive"
