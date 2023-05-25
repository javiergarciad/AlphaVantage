from flask import render_template, request
from app.main.forms import DatabaseForm
from app.main.tools import db_info

from app.main import bp


@bp.route("/", methods=['GET', 'POST'])
def index():
    
    db_form = DatabaseForm()

    symbols = {}

    if request.method == 'POST' and db_form.validate():
        if  "delete" in request.form.keys():
            print("delete")
        elif  "update" in request.form.keys():
            print("update")



    return render_template(
        "index.html",
        title="Alpha Vantage",
        # database status info
        db_info=db_info(),
        db_form=db_form,

        # symbosl data
        symbols=symbols,
    )

