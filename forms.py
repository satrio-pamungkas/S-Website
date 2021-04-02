from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField("Alamat Surel", validators = [InputRequired(), Email()])
    password = PasswordField("Kata Sandi", validators = [InputRequired()])
    submit = SubmitField("Masuk")


class RegisterForm(FlaskForm):
    name = StringField('Nama Pengguna', validators = [InputRequired(), Length(min=5)])
    email = StringField("Alamat Surel", validators = [InputRequired(), Email(), Length(min=5)])
    password = PasswordField("Kata Sandi", validators = [InputRequired(), Length(min=6)])
    repeat_password = PasswordField("Ulangi Kata Sandi", validators = [InputRequired(), EqualTo('password'), Length(min=6)])
    submit = SubmitField('Daftar')