import datetime
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import SubmitField, StringField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app import db
from app.main.tools import tickets_in_db


from app.models import Symbol


class DatabaseForm(FlaskForm):
    """
    Form to delete and update symbols
    """

    # use some of the periods from yfinace
    # https://github.com/ranaroussi/yfinance/wiki/Ticker#parameters
    # period = SelectField(
    #     "Period",
    #     choices=[
    #         ("1d", "1 day"),
    #         ("5d", "5 day"),
    #         ("1m", "1 month"),
    #         ("3m", "3 months"),
    #         ("6m", "6 months"),
    #         ("1y", "1 year"),
    #         ("2y", "2 years"),
    #         ("5y", "5 years"),
    #         ("ytd", "Year to date"),
    #     ],
    # )

    delete = SubmitField("Delete")
    update = SubmitField("Update")


def validate_ticket(form, ticket):
    """
    Check if ticket is already in database lower or upper case are the same
    """
    if ticket.data.upper() in tickets_in_db():
        raise ValidationError(f"Symbol '{ticket.data.upper()}' already exists.")


class AddTicketsForm(FlaskForm):
    """
    Form to add new symbols
    """

    ticket = StringField("", validators=[DataRequired(), validate_ticket])
    add = SubmitField("Add")
