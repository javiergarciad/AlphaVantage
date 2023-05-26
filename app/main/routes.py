import csv
from datetime import datetime
from pathlib import Path
import tempfile
import os
import sqlalchemy
from flask import abort, flash, jsonify, redirect, render_template, request, send_file, url_for

from app import db
from app.main import bp
from app.main.forms import AddTicketsForm, DatabaseForm
from app.main.tools import db_info, get_daily_bars_in_db, tickets_in_db, update_database
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
            db.drop_all()
            db.create_all()
            flash("Database restarted", "success")
            return redirect("/")

        #  If the database form is submitted and the update button is pressed
        elif "update" in request.form.keys():
            #  Update the database
            # period = db_form.period.data

            # Hard coding this for the open source version
            period = "1y"
            update = update_database(period)

            # count how many successfully updated
            errors = [x["ticket"] for x in update if x["success"] == False]
            sucess = [x["ticket"] for x in update if x["success"] == True]
            flash(f"Database updated. Errors with: {errors}")

            return redirect(url_for("main.index"))

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
            flash(f"Ticket '{ticket}' succesfully added to the database", "success")
            return redirect(url_for("main.index"))

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
    tickets = tickets_in_db()
    ans = []
    for s in tickets:
        bars = get_daily_bars_in_db(s)
        if len(bars) == 0:
            ans.append({"ticket": s, "bars": 0, "updated": "N/A"})
        else:
            total_bars = len(bars)
            updated = bars[0].date
            ans.append({"ticket": s, "bars": total_bars, "updated": updated})

    return jsonify(ans)


@bp.route("/api/delete_ticket", methods=["POST"])
def delete_ticket():
    ticket = request.form.get("ticket").upper()
    stmt = sqlalchemy.delete(Symbol).where(Symbol.symbol == ticket)
    db.session.execute(stmt)
    stmt = sqlalchemy.delete(DailyBar).where(DailyBar.symbol == ticket)
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


@bp.route("/api/export_data/<filename>", methods=["POST", "GET"])
def export_data(filename):
    """
    Export the data from the database
    """

    #  Get the data from the database
    ticket = request.form.get("ticket").upper()
    bars = get_daily_bars_in_db(ticket)

    file_path = Path(tempfile.gettempdir(), str(filename)).absolute()

    # Create CSV file
    f = open(file_path, "w")

    file_writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Write headers to CSV file
    file_header = ["Date", "Symbol", "Open", "High", "Low", "Close", "Volume"]
    file_writer.writerow(file_header)
    # Write data to CSV file
    for bar in bars:
        file_writer.writerow(bar.to_list())
    f.close()

    try:
        print("export data")
        return send_file(file_path, as_attachment=True, download_name=f"{ticket}.csv")
    except FileNotFoundError:
        abort(404)