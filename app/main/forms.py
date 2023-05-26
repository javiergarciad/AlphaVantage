from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from app import db


from app.models import Symbol


class DatabaseForm(FlaskForm):
    """
    Form to monitor database status
    """

    start = SubmitField("Start New Database")
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

    ticket = StringField("Tickets", validators=[DataRequired(), validate_ticket])
    add = SubmitField("Add")
