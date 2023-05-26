import datetime
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import SubmitField, StringField, DateField
from wtforms.validators import DataRequired, ValidationError
from app import db


from app.models import Symbol


def validate_start_date(form, start):
    """
    Check if start date is valid
    """
    years_delta = 2

    current = datetime.date.today()
    if current.month == 2 and current.day == 29:
        years_ago = current.replace(year=current.year - years_delta, day=28)
    else:
        years_ago = current.replace(year=current.year - years_delta)

    if start.data > current:
        raise ValidationError("Start date cannot be in the future.")
    if start.data < years_ago:
        raise ValidationError("Start date cannot be before two years ago.")


class DatabaseForm(FlaskForm):
    """
    Form to delete and update symbols
    """

    start = DateField(
        "Start date",
        format="%Y-%m-%d",
        validators=[DataRequired(), validate_start_date],
    )
    delete = SubmitField("Delete")
    update = SubmitField("Update")


def validate_ticket(form, ticket):
    """
    Check if ticket is already in database lower or upper case are the same
    """
    stmt = sqlalchemy.select(Symbol.symbol)
    qry = db.session.execute(stmt).all()
    tickets_in_db = [symbol.symbol for symbol in qry]

    form_ticket = ticket.data.upper()
    if form_ticket in tickets_in_db:
        raise ValidationError(f"Symbol '{form_ticket}' already exists.")


class AddTicketsForm(FlaskForm):
    """
    Form to add new symbols
    """

    ticket = StringField("", validators=[DataRequired(), validate_ticket])
    add = SubmitField("Add")
