import asyncio
import aiohttp
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto',target='pt')

class PokemonControl():

    pokemons = []
    pokemon = {}


async def getPokemons(session):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0'
    async with session.get(url) as res:
        dados = await res.json()
        return dados['results']


async def getDetalhes(session,url):
    async with session.get(url) as res:
        dados = await res.json()
        pokemon = {
            'id': dados['id'],
            'nome': dados['name'],
            'foto': dados['sprites']["other"]["official-artwork"]["front_default"],
            'descricao': dados['species']['url']
        }
        PokemonControl.pokemons.append(pokemon)

async def getdadosSpecies(session, url, posicao):
    async with session.get(url) as res:
        dados = await res.json()
        for i in dados["flavor_text_entries"]:
            if i['language']['name'] == 'en':
                descricao = i['flavor_text']
                break
        PokemonControl.pokemons[posicao]['descricao'] = descricao



async def main():
    async with aiohttp.ClientSession() as session:

        task1 = await getPokemons(session)

        tasks2 = []
        for pokemon in task1:
            tasks2.append(asyncio.create_task(getDetalhes(session,pokemon['url'])))

        await asyncio.gather(*tasks2)

        tasks3 = []
        for i,poke in enumerate(PokemonControl.pokemons):
            tasks3.append(getdadosSpecies(session,poke['descricao'],i))
        
        await asyncio.gather(*tasks3)

        


    if PokemonControl.pokemons:
        PokemonControl.pokemons = sorted(PokemonControl.pokemons, key=lambda p: p['id'])
        
        
            
        



    


        






  

    

    




        

   

        

    


    






