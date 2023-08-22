import requests

host = 'https://api.pokemonbattle.me:9104'

token = "7b984911b96b9840b2d17198270b65df"

#Добавили покемона

add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Кролик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : "application/json",
              "trainer_token": token})

print(add_pokemon.text)

#Изменили имя покемона

name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6408",
    "name": "New Name",
}, headers = {"Content-Type" : "application/json",
            "trainer_token": token})

print(name_pokemon.text)

#Поймали покемона в покеболл

cach_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6408"
}, headers = {"Content-Type" : "application/json",
            "trainer_token": token})

print(cach_pokemon.text)

#Изменили имя тренера

name_trainer = requests.put(f'{host}/trainers', json = {
    "name": "Trainer1",
    "city": "Tokyo"
}, headers = {"Content-Type" : "application/json",
            "trainer_token": token})

print(name_trainer.text)