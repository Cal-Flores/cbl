from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DraftForm(FlaskForm):
    team_name = StringField('Team_name', validators=[DataRequired()])
    weight = StringField('weight',  validators=[DataRequired()])
    submit = SubmitField('submit')
