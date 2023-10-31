from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class DraftForm(FlaskForm):
    team_winner = StringField('Team_name', validators=[DataRequired()])
    fly = StringField('weight',  validators=[DataRequired()])
    submit = SubmitField('submit')
