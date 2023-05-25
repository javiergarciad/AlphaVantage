from datetime import datetime
from flask import jsonify, redirect, render_template, request
from flask import flash
import sqlalchemy
from app import db
from app.main import bp
from app.main.forms import DatabaseForm, TicketsForm
from app.main.tools import db_info
from app.models import DailyBar, Symbol


@bp.route("/", methods=["GET", "POST"])
def index():
    db_form = DatabaseForm()
    tickets_form = TicketsForm()

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



########################################################################
# API
########################################################################
@bp.route("/api/tickets_info", methods=["GET"])
def tickets_info():
    """
    Return json info of tickets in the database
    """
    tickets = db.session.execute(sqlalchemy.select(Symbol)).scalars()
    if tickets is None:
        return []

    ans = []
    for s in tickets:
        stmt = (
            sqlalchemy.select(DailyBar)
            .where(DailyBar.symbol == s.symbol)
            .order_by(DailyBar.date.desc())
        )

        tickets_bars = db.session.execute(stmt).all()
        if len(tickets_bars) == 0:
            ans.append({"ticket": s.symbol, "bars": 0, "updated": 'N/A'})
        else:
            bars = len(tickets_bars)
            updated = tickets_bars[0].date
            ans.append({"ticket": s.symbol, "bars": bars, "updated": updated})

    return jsonify(ans)

