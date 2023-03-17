import requests

token = '7342e392fdf11361a09cafc3a21ca00a'

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json = {
    "name": "Буля",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(add_pokemon_response.text)

put_pokemon_response = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json = {
    "pokemon_id": 6299,
    "name": "petya",
    "photo": ""
})

print(put_pokemon_response.text)



add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json = {"pokemon_id": "6299"
    
})

print(add_pokeball_response.text)