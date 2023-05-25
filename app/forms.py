from flask_wtf import FlaskForm
from wtforms import SubmitField


class DatabaseForm(FlaskForm):
    """
    Form to monitor database status
    """

    start = SubmitField("Start New Database")
    delete = SubmitField("Delete")
    update = SubmitField("Update")
