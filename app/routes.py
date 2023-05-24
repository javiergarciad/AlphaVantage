from flask import render_template
from app import app
from app.forms import DatabaseForm, UpdateForm


@app.route("/")
@app.route("/index")
def index():
    db_form = DatabaseForm()
    update_form = UpdateForm()
    symbols = {}
    return render_template(
        "index.html", title="Home", db_form=db_form, update_form=update_form, symbols=symbols
    )
