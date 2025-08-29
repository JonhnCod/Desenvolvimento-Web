from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from deep_translator import GoogleTranslator
from app.controllers.pokeControl import PokemonControl
import asyncio


app = Flask(__name__)
tradutor = GoogleTranslator(source= "en", target= "pt")
app.config['SECRET_KEY'] = 'dc0a80dc5aa93aac5f09390689238d1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'

database = SQLAlchemy(app)

URL_POKEMON = 'https://pokeapi.co/api/v2/pokemon/{ID_NOME}'
URL_POKE_SPECIE = 'https://pokeapi.co/api/v2/pokemon-species/{ID}/'



asyncio.run(PokemonControl.getTodos())

from app.routes import rotas
from app import models