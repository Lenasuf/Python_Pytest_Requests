import requests
TOKEN = "600f3b94aa54e54ef0aff64900917acd"
URL = "https://api.pokemonbattle.ru/v2"
HEADER = {"Content-Type": "application/json", "trainer_token" : TOKEN}

body_1 = {"name": "generate","photo_id": -1}
body_2 = {"id" : 124557 ,"name": "Mopис","photo_id": 876}
body_3 = { "pokemon_id": "124478"}

# Создание покемона
"""response = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_1)
print(response.text) 
pokemon_id = response.json()["id"]"""


# Смена имени покемона
"""response_new_mame = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = body_3)
print(response_new_mame.text)"""

# Поймать в покебол
response_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_3)
print(response_pokeball.text)


