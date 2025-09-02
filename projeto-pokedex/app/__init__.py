from flask import Flask
from deep_translator import GoogleTranslator



app = Flask(__name__)
tradutor = GoogleTranslator(source="en", target="pt")
app.config['SECRET_KEY'] = 'dc0a80dc5aa93aac5f09390689238d1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'



from app.routes import rotas
from app.models import pokemon