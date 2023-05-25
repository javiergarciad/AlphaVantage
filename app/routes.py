from flask import render_template, request
from app import app
from app.forms import DatabaseForm
from app.tools import start_new_db, test_db
from config import Config


@app.route("/", methods=['GET', 'POST'])
def index():
    db_name = Config().DB_NAME
    db_engine = Config().DB_ENGINE
    db_status = test_db()

    db_form = DatabaseForm()

    symbols = {}

    if request.method == 'POST' and db_form.validate():
        if "start" in request.form.keys():
            print("start")
            start_new_db()
        elif  "delete" in request.form.keys():
            print("delete")
        elif  "update" in request.form.keys():
            print("update")



    return render_template(
        "index.html",
        title="Alpha Vantage",
        # database status info
        db_name=db_name,
        db_engine=db_engine,
        db_status=db_status,
        db_form=db_form,

        # symbosl data
        symbols=symbols,
    )


@app.route("/db_start", methods=["POST"])
def db_start():
    return "start"


@app.route("/db_delete", methods=["POST"])
def db_delete():
    return "delete"


@app.route("/db_update_all", methods=["POST"])
def db_update_all():
    return "update all"
