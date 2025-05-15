from flask import Flask,render_template, url_for,flash, redirect
from forms import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '6e91202e825cd2edea02d586ea56d2d4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto_site_flask.db'
database = SQLAlchemy(app)


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
        flash(f'Cadastrado: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('paginas/cadastro.html',form_cadastro=form_cadastro)

@app.route('/contato')
def contato():
    return render_template('paginas/contato.html',lista=lista)


if __name__ == '__main__':
    app.run(debug=True)