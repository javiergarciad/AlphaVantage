

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class DatabaseForm(FlaskForm):
    """
    Form to monitor database status
    """
    start = SubmitField('Start')
    delete = SubmitField('Delete')
    update = SubmitField('Update')







