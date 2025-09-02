from flask import render_template
from app import app
from app.controllers.pokeControl import main, PokemonControl as pk
from deep_translator import GoogleTranslator
import asyncio

tradutor = GoogleTranslator(source='auto', target='pt')


@app.route("/")
def home():

    asyncio.run(main()) 
    
    return render_template(
        "home.html"
        
    )



@app.route("/lista")
@app.route("/lista/<int:page>")
def mostrarPokemon(page=1):
    
    limit = 12
    offset = (page - 1) * limit

    pokemon = pk.pokemons[offset:offset + limit]
    for i in pokemon:
        i['descricao'] = tradutor.translate(i['descricao'])

    total = 1302
    total_pages = (total // limit) + 1
        
    return render_template(
        "mostraPokemon.html",
        lista=pokemon,
        page=page,
        total_pages=total_pages
    )