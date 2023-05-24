

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class DatabaseForm(FlaskForm):
    """
    Form to monitor database status
    """
    name = StringField('name', validators=[DataRequired(),], render_kw={'disabled': ''})
    driver = StringField('driver', validators=[DataRequired(),], render_kw={'disabled': ''})
    status = StringField('status', validators=[DataRequired(),], render_kw={'disabled': ''})
    last_update = DateField('last_update', validators=[DataRequired(),], render_kw={'disabled': ''})
    start = SubmitField('Start')
    delete = SubmitField('Delete')

class UpdateForm(FlaskForm):
    """
    Form to update database
    """
    update = SubmitField('Update')





