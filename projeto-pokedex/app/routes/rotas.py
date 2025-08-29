from flask import render_template
import requests as r
from app import app,tradutor
from app.controllers.pokeControl import PokemonControl as pk


@app.route("/")
@app.route("/lista/<int:page>")
def mostrarPokemon(page=1):

    limit = 9
    offset = (page - 1) * limit

    response = r.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}")
    
    npokemon = response.json()

    listaPokemon = []

    
    for idx, pokemon in enumerate(npokemon['results'], start=offset+1):

        nome = pokemon['name']
        getUrlPokemon = r.get(pokemon['url']).json()
        getUrlspecies = r.get(getUrlPokemon['species']['url']).json()
       
    
        if idx > 1025:
            idx += 8975

        
        foto = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{idx}.png" 
        if (r.get(foto).status_code) != 200:
            foto = None


        listaPokemon.append({
            "nome": nome,
            "img":  foto,
            "descricao": tradutor.translate(getUrlspecies["flavor_text_entries"][0]["flavor_text"].replace('\n', ' ').replace('\f', ' '))
            
        })

    total = npokemon["count"]
    total_pages = (total // limit) + 1
        
    return render_template(
        "mostraPokemon.html",
        lista=listaPokemon,
        page=page,
        total_pages=total_pages
    )