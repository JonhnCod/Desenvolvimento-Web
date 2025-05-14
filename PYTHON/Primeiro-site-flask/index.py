from flask import Flask,render_template, url_for
from forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '6e91202e825cd2edea02d586ea56d2d4'

lista = ["Jonathan","Bruna","Roger"]
@app.route('/')
def home():
    return render_template('paginas/home.html')

@app.route('/login')
def login():
    form_login = LoginForm()
    return render_template('paginas/login.html',form_login=form_login)

@app.route('/cadastro')
def cadastro():
    form_cadastro = RegisterForm()
    return render_template('paginas/cadastro.html',form_cadastro=form_cadastro)

@app.route('/contato')
def contato():
    return render_template('paginas/contato.html',lista=lista)


if __name__ == '__main__':
    app.run(debug=True)