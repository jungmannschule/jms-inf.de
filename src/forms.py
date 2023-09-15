from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, SelectField, EmailField, MultipleFileField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    # loginname = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    # remember_me = BooleanField('Angemeldet bleiben?')
    submit = SubmitField('Einloggen')
