import aiohttp

class PokemonControl():

    pokemon = []

    @staticmethod
    async def getTodos():
        url = f"https://pokeapi.co/api/v2/pokemon?offset=0&limit=1300"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    dados =  await resp.json()
                    for i,pokemon in enumerate(dados['results']):
                        nome = pokemon['name']

                        if i > 1025:
                            i += 8975
                        foto = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{i}.png"
                        if session.get(foto).status_code != 200:
                            foto = None

                        pokem ={
                            'nome':nome,
                            'img': foto

                        }
                    
                    PokemonControl.pokemon.append(pokem)
            return None
        

   

        

    


    






