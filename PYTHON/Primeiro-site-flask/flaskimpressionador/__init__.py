from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '6e91202e825cd2edea02d586ea56d2d4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetoflask.db'

database = SQLAlchemy(app)



from flaskimpressionador import routes