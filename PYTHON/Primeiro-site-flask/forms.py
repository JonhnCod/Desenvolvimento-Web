from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email,length,EqualTo


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),length(6, 20)])
    remember_me = BooleanField('Remember Me')
    submit_login = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Nome do usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(),length(6,20)])
    senha_confirm = PasswordField('Confirmacao da senha', validators=[DataRequired(), EqualTo('senha')])
    submit_cadastro = SubmitField('Criar conta')

