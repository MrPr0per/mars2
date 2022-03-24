from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('почта/логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('имя', validators=[DataRequired()])
    surname = StringField('фамилия', validators=[DataRequired()])
    age = IntegerField('возраст', validators=[DataRequired()])
    position = StringField('должность', validators=[DataRequired()])
    speciality = StringField('спецальность', validators=[DataRequired()])
    address = StringField('адрес', validators=[DataRequired()])
    submit = SubmitField('зарегистрироваться')