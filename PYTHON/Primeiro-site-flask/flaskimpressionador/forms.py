from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email,Length,EqualTo, ValidationError
from flaskimpressionador.models import Usuario

class RegisterForm(FlaskForm):
    username = StringField('Nome do usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
    senha_confirm = PasswordField('Confirmacao da senha', validators=[DataRequired(), EqualTo('senha')])
    submit_cadastro = SubmitField('Criar conta')

    def validate_email(self, email):
        user = Usuario.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já existe ! ')




class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(6, 20)])
    remember_me = BooleanField('Lembrar-me')
    submit_login = SubmitField('Entrar')


