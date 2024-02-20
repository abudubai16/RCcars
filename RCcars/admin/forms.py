from wtforms import PasswordField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from RCcars.config import Config


class LoginAdminForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class Positions(FlaskForm):
    positions = []
    for i in range(Config.num_players):
        positions.append(IntegerField(str(i), validators=[DataRequired(), NumberRange(min=1, max=Config.num_players)]))
