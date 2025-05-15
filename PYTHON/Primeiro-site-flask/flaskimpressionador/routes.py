from flask import render_template,flash,redirect,url_for
from flaskimpressionador import app, database
from flaskimpressionador.forms import LoginForm,RegisterForm
from flaskimpressionador.models import Usuario


lista = ["Jonathan","Bruna","Roger"]

@app.route('/')
def home():
    return render_template('paginas/home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        flash(f'sucesso Login: {form_login.email.data}','alert-success')
        return redirect(url_for('home'))

    return render_template('paginas/login.html',form_login=form_login)

@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    form_cadastro = RegisterForm()
    if form_cadastro.validate_on_submit():
        usuario = Usuario(username=form_cadastro.username.data,email=form_cadastro.email.data,senha=form_cadastro.senha.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Cadastrado: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('paginas/cadastro.html',form_cadastro=form_cadastro)

@app.route('/contato')
def contato():
    return render_template('paginas/contato.html',lista=lista)