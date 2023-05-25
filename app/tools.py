import sqlalchemy
from app import db


def test_db():
    """
    Tests if the database is accessible and all tables exists
    """
    try:
        a = sqlalchemy.inspect(db.engine).has_table("alembic_version")
        b = sqlalchemy.inspect(db.engine).has_table("symbol")
        c = sqlalchemy.inspect(db.engine).has_table("daily_bar")

        if a and b and c:
            return True, "Responsive"
        else:
            return False, "Unresponsive"
    except:
        return False, "Unresponsive"


def start_new_db():
    """
    Creates a new database
    """
    db.create_all()
    db.session.commit()
    return True