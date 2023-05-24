from flask import render_template
from app import app
from app.forms import DatabaseForm, UpdateForm
from app.tools import test_db
from config import Config


@app.route("/")
@app.route("/index")
def index():
    db_name = Config().DB_NAME
    db_drive = Config().DB_ENGINE
    db_status = test_db()[1]

    db_form = DatabaseForm()
    update_form = UpdateForm()
    symbols = {}


    return render_template(
        "index.html",
        title="Alpha Vantage",
        # database status info
        db_name=db_name,
        db_drive=db_drive,
        db_status=db_status,
        db_form=db_form,
        # update form
        update_form=update_form,
        # symbosl data
        symbols=symbols,
    )

