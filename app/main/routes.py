from datetime import datetime
from flask import redirect, render_template, request
from flask import flash
from app import db
from app.main import bp
from app.main.forms import DatabaseForm, TicketsForm
from app.main.tools import db_info
from app.models import Symbol


@bp.route("/", methods=["GET", "POST"])
def index():
    db_form = DatabaseForm()
    tickets_form = TicketsForm()
    symbols = {}

    if request.method == "POST" and db_form.validate():
        if "delete" in request.form.keys():
            print("delete")
        elif "update" in request.form.keys():
            print("update")

    return render_template(
        "index.html",
        title="Alpha Vantage",
        # database status info
        db_info=db_info(),
        db_form=db_form,
        tickets_form=tickets_form,
        # symbosl data
        symbols=symbols,
    )


@bp.route("/add_ticket", methods=["POST"])
def add_ticket():
    """
    Insert one ticket in the symbols table if it does not exists
    """
    ticket = request.form.get("ticket").upper()
    ticket_in_bd = db.session.execute(
        db.select(Symbol).filter_by(symbol=ticket)
    ).first()

    if ticket_in_bd is None:
        new_symbol = Symbol(
            symbol=ticket, created=datetime.utcnow(), updated=datetime.utcnow()
        )
        db.session.add(new_symbol)
        db.session.commit()
        flash(f"The ticket '{ticket}' succesfully added to the database", 'success')
    else:
        flash(f"The ticket '{ticket}' already exists in the database", 'danger')

    return redirect("/", code=302)
