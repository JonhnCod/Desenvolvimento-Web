from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('paginas/home.html')

@app.route('/login')
def login():
    return render_template('paginas/login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('paginas/cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)