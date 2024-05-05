from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired


class UserLoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    submit = SubmitField('ОК')

