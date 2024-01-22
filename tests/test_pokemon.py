"""
Проверь, что ответ запрос GET /trainers приходит с кодом 200
Проверь, что в ответе приходит строчка с именем твоего тренера
(Не забудь прописать в квери id твоего тренера
"""
import requests
import pytest

URL = "https://api.pokemonbattle.me:9104"
Headers = {'Content-Type': 'application/json', 'trainer_token': 'c18bc7e1137b5357e0dbc6035e554967'}
trainerid = 3758

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', headers=Headers, params={"trainer_id": trainerid}, timeout=5)
    assert response.status_code == 200

def test_check_response():
    response = requests.get(url=f'{URL}/trainers', headers=Headers, params={"trainer_id": trainerid}, timeout=5)
    data = response.json()
    assert data["trainer_name"] == "LizaZvr_tg"

