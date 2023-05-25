from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class DatabaseForm(FlaskForm):
    """
    Form to monitor database status
    """

    start = SubmitField("Start New Database")
    delete = SubmitField("Delete")
    update = SubmitField("Update")


class TicketsForm(FlaskForm):
    """
    Form to add new symbols
    """
    ticket = StringField('Tickets', validators=[DataRequired()])
    add = SubmitField("Add")


