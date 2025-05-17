from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '6e91202e825cd2edea02d586ea56d2d4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetoflask.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view  = 'login'
login_manager.login_message_category = 'alert-info'



from flaskimpressionador import routes