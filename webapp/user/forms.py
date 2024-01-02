from collections.abc import Mapping, Sequence
from typing import Any
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField(label='Имя пользователя', validators=[DataRequired()])
    password = PasswordField(label='Пароль', validators=[DataRequired()])
    remember_me = BooleanField(label='Запомнить меня', default=True)
    submit = SubmitField(label='Отправить')


class RegistrationForm(FlaskForm):
    username = StringField(label='Имя пользователя', validators=[DataRequired()])
    email = StringField(label='Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField(label='Пароль', validators=[DataRequired(), EqualTo('password')])
    password2 = PasswordField(label='Повторите пароль', validators=[DataRequired()])
    remember_me = BooleanField(label='Запомнить меня', default=True)
    submit = SubmitField(label='Отправить')


    def validate_username(self, username) -> ValidationError:
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким именем уже существует')
        
    def validate_email(self, email) -> ValidationError:
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с такой почтой уже существует')
        
        