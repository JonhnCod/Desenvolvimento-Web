from flask import render_template,flash,redirect,url_for,request
from flaskimpressionador import app, database,bcrypt
from flaskimpressionador.forms import LoginForm,RegisterForm
from flaskimpressionador.models import Usuario
from flask_login import login_user, logout_user,current_user,login_required

lista = ["Jonathan","Bruna","Roger"]

@app.route('/')
def home():
    form_login = LoginForm()
    usuario = Usuario.query.filter_by(email=form_login.email.data).first()

    return render_template('paginas/home.html',usuario=usuario)

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.password.data):
            login_user(usuario,remember=form_login.remember_me.data)
            flash(f'sucesso Login: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha Login: email Não existe ou senha incorreta', 'alert-danger')


    return render_template('paginas/login.html',form_login=form_login)

@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    form_cadastro = RegisterForm()
    if form_cadastro.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form_cadastro.senha.data)
        usuario = Usuario(username=form_cadastro.username.data,email=form_cadastro.email.data,senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Cadastrado: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('paginas/cadastro.html',form_cadastro=form_cadastro)

@app.route('/contato')
def contato():
    return render_template('paginas/contato.html',lista=lista)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
    return render_template('paginas/perfil.html')

@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('paginas/criarpost.html')

