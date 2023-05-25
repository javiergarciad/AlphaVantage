import sqlalchemy
from app import db
from config import Config


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



def startup_jobs():
    """
    Runs the startup jobs
    """
    # Chack thah the database exist and it has a complete schema
    try:
        db_uri = Config().SQLALCHEMY_DATABASE_URI
        engine = sqlalchemy.create_engine(db_uri)
        a = sqlalchemy.inspect(engine).has_table("alembic_version")
        b = sqlalchemy.inspect(engine).has_table("symbol")
        c = sqlalchemy.inspect(engine).has_table("daily_bar")

        if a and b and c:
           there_is_db = True
        else:
            there_is_db = False
    except:
        there_is_db = False

    if not there_is_db:
        

