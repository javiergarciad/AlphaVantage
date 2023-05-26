from datetime import datetime

import sqlalchemy
from flask import flash, jsonify, redirect, render_template, request

from app import db
from app.main import bp
from app.main.forms import AddTicketsForm, DatabaseForm
from app.main.tools import db_info
from app.models import DailyBar, Symbol


@bp.route("/", methods=["GET", "POST"])
def index():
    # forms
    tickets_form = AddTicketsForm()
    db_form = DatabaseForm()

    #  If the database form is submitted
    if db_form.validate_on_submit():
        #  If the database form is submitted and the delete button is pressed
        if "delete" in request.form.keys():
            #  Delete the database
            print("Deleting database")
            # db.drop_all()
            # db.create_all()
            # flash("Database deleted", "success" )
            # return redirect("/")

        #  If the database form is submitted and the update button is pressed
        elif "update" in request.form.keys():
            #  Update the database
            print("Updating database")
            # db.drop_all()
            # db.create_all()
            # flash("Database updated", "success")
            # return redirect("/")

    #  If the add ticket form is submitted
    if tickets_form.validate_on_submit():
        #  If the add ticket form is submitted and the add button is pressed
        if "add" in request.form.keys():
            #  Add the ticket to the database
            ticket = tickets_form.ticket.data.upper()
            new_symbol = Symbol(
                symbol=ticket, created=datetime.utcnow(), updated=datetime.utcnow()
            )
            db.session.add(new_symbol)
            db.session.commit()
            flash(f"Ticket '{ticket}' succesfully added to the database", 'success')
            return redirect("/")



    # render  the index page
    return render_template(
        "index.html",
        title="Alpha Vantage",
        # database status info
        db_info=db_info(),
        db_form=db_form,
        tickets_form=tickets_form,
    )


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
            ans.append({"ticket": s.symbol, "bars": 0, "updated": "N/A"})
        else:
            bars = len(tickets_bars)
            updated = tickets_bars[0].date
            ans.append({"ticket": s.symbol, "bars": bars, "updated": updated})

    return jsonify(ans)


@bp.route("/api/delete_ticket", methods=["POST"])
def delete_ticket():
    ticket = request.form.get("ticket").upper()
    stmt = sqlalchemy.delete(Symbol).where(Symbol.symbol == ticket)
    db.session.execute(stmt)
    db.session.commit()
    return jsonify({"ticket": ticket, "status": True, "action": "delete"})


@bp.route("/api/add_ticket", methods=["POST"])
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
        # flash(f"The ticket '{ticket}' succesfully added to the database", 'success')
        return jsonify({"ticket": ticket, "status": True, "action": "add"})
    else:
        # flash(f"The ticket '{ticket}' already exists in the database", 'danger')
        return jsonify({"ticket": ticket, "status": False, "action": "add"})
