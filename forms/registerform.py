from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    nickname = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')
