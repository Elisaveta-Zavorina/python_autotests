"""
1. код для 3-х запросов с выводом (принтом) ответа по документации Покемонов:
    - Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))
    
    В ответе (терминале) должен прийти объект json
    
    - Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))
    
    В ответе (терминале) должен прийти объект json
    
    - Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))
    
    В ответе (терминале) должен прийти объект json
"""

import requests

URL = "https://api.pokemonbattle.me:9104"
Headers = {'Content-Type': 'application/json', 'trainer_token': 'c18bc7e1137b5357e0dbc6035e554967'}

bodyadd = {
    "name": "Питомон",
    "photo": "https://dolnikov.ru/pokemons/albums/335.png"
}

response = requests.post(url=f'{URL}/pokemons', json=bodyadd, headers=Headers, timeout=5)
print(f'Ответ: {response.text}, Body ответа: {response.json()}, Статус ответа: {response.status_code}')

if response.status_code == 201:
    print('ok')
else:
    print('not ok')

idpokemon = response.json()['id']

bodychange = {
    "pokemon_id": idpokemon,
    "name": "Питомон Изменен",
}

response = requests.patch(url=f'{URL}/pokemons', json=bodychange, headers=Headers, timeout=5)
print(f'Ответ: {response.text}, Body ответа: {response.json()}, Статус ответа: {response.status_code}')

if response.status_code == 200:
    print('ok')
else:
    print('not ok')

bodycatch = {
    "pokemon_id": idpokemon
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=bodycatch, headers=Headers, timeout=5)
print(f'Ответ: {response.text}, Body ответа: {response.json()}, Статус ответа: {response.status_code}')

if response.status_code == 200:
    print('ok')
else:
    print('not ok')