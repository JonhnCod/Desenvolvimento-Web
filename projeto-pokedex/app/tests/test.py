import aiohttp
import asyncio

class PokemonControl():
    pokemon = {}
    listaPokemon = []

    @staticmethod
    async def getTodos():
        url = f"https://pokeapi.co/api/v2/pokemon?offset=0&limit=1350"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    dados =  await resp.json()
                    PokemonControl.listaPokemon.append(*dados['results'])
            return None
        

    @staticmethod
    async def getFotos():
        pokemons = PokemonControl.pokemon
       
    
        


asyncio.run(PokemonControl.getTodos())

print(PokemonControl.listaPokemon)



