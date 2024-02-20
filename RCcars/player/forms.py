from wtforms import StringField, SubmitField, PasswordField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo
from RCcars.config import Config


class RegistrationPlayerForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=30)])
    number = StringField('Phone number', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    car = IntegerField('Car', validators=[DataRequired(), NumberRange(min=1, max=Config.num_players)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    car = IntegerField('Car', validators=[DataRequired(), NumberRange(min=1, max=Config.num_players)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
