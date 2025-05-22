from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email,Length,EqualTo, ValidationError
from flaskimpressionador.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed

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


class FormEditprofile(FlaskForm):
    username = StringField('Nome do usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto do perfil', validators=[FileAllowed(['jpg','png'])])
    curso_excel = BooleanField('Excel impressionador')
    curso_vba = BooleanField('VBA impressionador')
    curso_powerbi = BooleanField('PowerBI impressionador')
    curso_python = BooleanField('Python impressionador')
    curso_sql = BooleanField('SQL impressionador')

    submit_editar = SubmitField('Editar perfil')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = Usuario.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email cdastrado para outro usuario! ')



class FormPost(FlaskForm):
    titulo = StringField('Titulo do post', validators=[DataRequired(), Length(min=2, max=140)])
    corpo = TextAreaField('Escreva o post aqui', validators=[DataRequired()])
    enviar_post = SubmitField('Enviar')